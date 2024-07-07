# Total Viewshed Script Tool User Manual

## Tool installation and utilization

Here is a detailed guide on how you can install and use this tool in ArcGIS Pro:

### 1. Open ArcGIS Pro

- Launch ArcGIS Pro and open or create a new project.

### 2. Access the Catalog Pane

- Navigate to the Catalog pane. If the Catalog pane is not visible, you can open it by going to the _View_ tab and selecting _Catalog Pane_.

### 3. Add the Toolbox

- In the Catalog pane, right-click on the "Toolboxes" section.
- Select the first option, _Add Toolbox_.

### 4. Navigate to the Toolbox File

- In the dialog that appears, navigate to the folder containing the _TotalViewshed.atbx_ toolbox file.
- Select the toolbox file and click _OK_ to add it to your project.

### 5. Use the Total Viewshed Tool

- Once the toolbox is added, it will appear under the _Toolboxes_ section in the Catalog pane.
- Expand the _TotalViewshed_ toolbox to see the _Total Viewshed_ tool.
- Double-click on the tool to open its parameters window.

### 6. Configure and Run the Tool

- In the parameters window, input the required parameters such as the Digital Elevation Model (DEM) file and any other necessary settings.
- Click "Run" to execute the tool. The tool will perform the total viewshed analysis based on the provided parameters and generate the output.

Parameters explanation :

- **Input Raster:** The input surface raster.
- **Output Raster:** The output raster. It will record the number of times that each cell location in the input surface raster can be seen by the observation points.
- **Observer Offset (Optional):** A vertical distance to be added to the observer elevation. It must be a positive integer or floating-point value. If not specified, the default value will be 1.70 metres.
- **Viewpoints_distance (Optional):** refers to the spacing, measured in meters, between individual viewpoints in a viewshed analysis. This parameter is crucial as it balances the accuracy of visibility analysis against computational costs: closer distances between viewpoints increase the accuracy but also raise the computational requirements. If not specified by the user, default distances are automatically assigned based on the size of the Digital Elevation Model (DEM):
  - For DEMs up to 10x10 km: The default viewpoint distance is set at 100 meters.
  - For DEMs larger than 10x10 km but up to 20x20 km: The viewpoint distance increases to 115 meters.
  - For DEMs larger than 20x20 km but up to 30x30 km: The distance is set at 130 meters.
  - For DEMs larger than 30x30 km but up to 40x40 km: The distance extends to 140 meters.
  - For DEMs larger than 40x40 km but up to 50x50 km: The viewpoint distance is 155 meters.
  - For DEMs larger than 50x50 km: There is an incremental increase of 15 meters for every additional 10 km beyond 50 km. <br><br>

![summary](https://i.imgur.com/ndOgVRY.png)<br>
_Installation steps_

By following these steps, you will be able to seamlessly integrate the _Total Viewshed_ tool into your ArcGIS Pro environment and leverage it for efficient and accurate viewshed analysis.
