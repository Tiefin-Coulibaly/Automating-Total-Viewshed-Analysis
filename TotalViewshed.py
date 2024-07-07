####################################################################################################
# program		: TotalViewshed.py
#
# purpose	: This script automates total viewshed analysis using a 
#             digital elevation model (DEM). Key functionalities include reading and processing 
#             DEM data, projecting it to UTM when needed, dynamically generating observer points 
#             using fishnets, and calculating viewshed with specified observer 
#             offsets. The script utilizes parallel processing to optimize performance. Outputs are 
#             tailored based on user-defined parameters.
#                   
# Author	: Mamadou Coulibaly                           			                        May 2024
####################################################################################################

import arcpy
from arcpy.sa import *

def TotalViewshed():  # Main function for performing viewshed analysis
    # User inputs for the analysis
    DEM_path = arcpy.GetParameterAsText(0)  
    output_raster = arcpy.GetParameterAsText(1) 
    observer_offset = arcpy.GetParameterAsText(2) 
    distance = arcpy.GetParameterAsText(3) 
    
    # Format observer offset for later use
    if  observer_offset:
        observer_offset_updated = f"{observer_offset} Meters"
    else :
        observer_offset_updated = "1.70 Meters" # i consider the average height of a human being stand up at each observer point. 
    
    
    arcpy.AddMessage("Loading DEM and getting spatial reference...")

    # Load the DEM and get its spatial reference
    DEM = arcpy.Raster(DEM_path)
    spatial_ref = DEM.spatialReference
    # Project DEM to UTM coordinate system if it is in a geographic coordinate system
    if spatial_ref.type == "Geographic":
        # Get the extent of the raster
        initial_DEM_extent = DEM.extent
        # Calculate the centroid from the extent
        centroid_x = (initial_DEM_extent.XMin + initial_DEM_extent.XMax) / 2
        centroid_y = (initial_DEM_extent.YMin + initial_DEM_extent.YMax) / 2
        # Determine the UTM zone based on the longitude
        utm_zone = int((centroid_x + 180) / 6) + 1
        # Determine the correct UTM code based on hemisphere
        if centroid_y >= 0:
            utm_code = 32600
        else:
            utm_code = 32700
        # Create the UTM spatial reference
        utm_sr = arcpy.SpatialReference(utm_code + utm_zone)
        # Project the DEM
        DEM_Projected = arcpy.management.ProjectRaster(in_raster=DEM, out_raster="DEM_Projected", out_coor_system=utm_sr) 
        DEM = arcpy.Raster(DEM_Projected)
   
    arcpy.AddMessage("Generating observer points dynamically...")

    # Process to handle observer points dynamically if not predefined
    minX, minY = DEM.extent.XMin, DEM.extent.YMin
    # fishnet origin and y axis coordinates
    origin_coord = f"{minX} {minY}"
    y_axis_coord = f"{minX} {minY + 10}"
    # Get DEM extent
    width = DEM.extent.width
    height = DEM.extent.height
    if not distance :
        # Determine the distance between viewpoints based on DEM size
        if max(width, height) <= 10000:  # 10 km or smaller
            distance = 100
        elif max(width, height) <= 20000:  # between 10 km and 20 km
            distance = 115
        elif max(width, height) <= 30000: # between 20 km and 30 km
            distance = 130
        elif max(width, height) <= 40000: # between 30 km and 40 km
            distance = 140
        elif max(width, height) <= 50000: # between 40 km and 50 km
            distance = 155
        else:
            distance = 155 + 15 * ((max(width, height) // 10000) - 5)  # Increment by 15 meters for each 10km beyond 50km

    arcpy.AddMessage("Converting DEM to integer raster...")
    # Process: Integer raster
    arcpy.ddd.Int(DEM, "Int_DEM")
    arcpy.AddMessage("DEM converted to integer raster")
    
    arcpy.AddMessage("Converting raster to polygon...")
    # Process: Raster to Polygon 
    arcpy.conversion.RasterToPolygon("Int_DEM", "in_memory/Int_DEM_Polygon")
    arcpy.AddMessage("Raster converted to polygon")

    arcpy.AddMessage("Creating fishnet...")
    # Process: Create Fishnet 
    fishnet = arcpy.management.CreateFishnet(out_feature_class="in_memory/fishnet", origin_coord=origin_coord, 
                                            y_axis_coord=y_axis_coord, cell_width=distance, cell_height=distance, 
                                            number_rows=None, number_columns=None, labels="LABELS", template="Int_DEM")[0]
    arcpy.AddMessage("Fishnet created")

    arcpy.AddMessage("Clipping fishnet to DEM extent...")
    # Process: Clip (clip the Viewpoints_Grid created to the minimum bounding of the area of interest)
    viewpoints_grid = f"Viewpoints_Grid_{DEM.name}"
    arcpy.analysis.Clip("in_memory/fishnet_label", "in_memory/Int_DEM_Polygon", viewpoints_grid)
    arcpy.AddMessage("Clipping completed.")

    # Enable parallel processing to enhance performance
    arcpy.env.parallelProcessingFactor = "100%"
    arcpy.AddMessage("Parallel processing enabled.")

    arcpy.AddMessage("Performing viewshed analysis...")
    # Perform the viewshed analysis
    arcpy.ddd.Viewshed2(in_raster=DEM, in_observer_features=viewpoints_grid, out_raster=output_raster, 
                        observer_offset=observer_offset_updated)
    arcpy.AddMessage("Viewshed analysis completed.")

    arcpy.AddMessage("Deleting the integer raster...")
    # Delete the integer raster
    arcpy.arcpy.management.Delete("Int_DEM")
    arcpy.AddMessage("Deletion completed")

if __name__ == '__main__':
    arcpy.AddMessage("Setting up environment and running TotalViewshed script...")
    # Access the currently active ArcGIS Pro project
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    # Get the path to the default geodatabase
    default_gdb = aprx.defaultGeodatabase
    # Set environment settings for the script
    arcpy.env.workspace =  default_gdb
    arcpy.env.overwriteOutput = True 
    TotalViewshed()
    arcpy.AddMessage("Total Viewshed executed successfully.")
