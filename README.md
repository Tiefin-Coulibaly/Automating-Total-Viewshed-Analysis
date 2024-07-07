![Cover](https://i.imgur.com/AvqAVQU.png)

<!-- <img src="https://i.imgur.com/AvqAVQU.png" alt="Cover" heigh="2000"> -->

# A python-based script for generating total viewsheds

The interplay of landscapes and visibility within Geographic Information Systems (GIS) is a domain of continuous exploration and critical importance across a variety of disciplines. Total viewshed analysis, which assesses the visibility from one or multiple points across diverse landscapes, has proven to be indispensable in fields such as landscape conservation, urban planning, and archaeology. This technique enables a nuanced understanding of how landscapes are visually experienced from different vantage points, informing both historical insights and contemporary planning strategies.

The relevance of total viewshed analysis is underscored by its application in numerous studies. For instance, Llobera (2003) and Llobera et al. (2010) have emphasized its utility in understanding historical landscapes and their socio-spatial dynamics. Similarly, La Rosa and Izakovičová (2022) highlight its importance in landscape protection planning, where visibility assessments from significant roadways inform guidelines to preserve critical landscape features. Moreover, in their study, Dungan et al. (2018) demonstrate the strategic placement of Chacoan great houses to maximize visibility, highlighting the method’s applicability in historical and archaeological context.

Despite its extensive applications, conducting total viewshed analyses, particularly over large areas equipped with high-resolution Digital Elevation Models (DEMs), involves substantial computational resources and time. The computational intensity required for processing large datasets often results in prohibitive costs and extended processing times, which can impede the scalability and practicality of GIS projects. Recent advancements in distributed computing methods are increasingly being developed to effectively handle the vast data volumes and computational demands inherent in these analyses.

Addressing these technical challenges, the _TotalViewshed_ tool I developed is an innovative ArcGIS Pro geoprocessing tool specifically designed to optimize the total viewshed analysis process. The primary objective of this solution is to reduce computational loads while maintaining the accuracy and reliability of the results. This system aims to leverage advanced algorithms and distributed computing techniques to facilitate rapid processing of large-scale viewshed analyses, making it feasible to integrate these methods into regular GIS workflows.

## Script Functionalities and Optimization Strategies

The _TotalViewshed.py_ script enhances the efficiency and accessibility of generating total viewsheds, making it feasible for users with varying levels of GIS expertise. The tool incorporates several features:

### 1. DEM Input and Processing

- **Input Handling:** The script allows for direct input of a Digital Elevation Model (DEM). This flexibility ensures that users can work with any DEM stored on their system or network.
- **Automatic Projection:** If the DEM is in a geographic coordinate system, the script projects it to the appropriate Universal Transverse Mercator (UTM) projection. This is crucial for ensuring accurate distance calculations in the viewshed analysis.

### 2. Viewpoint Generation and Customization

- **Dynamic Viewpoint Spacing:** The script dynamically generates observer points using a fishnet grid, where the spacing between points can be manually set or automatically determined based on the DEM size. This strategic spacing of viewpoints reduces computational demands while covering the study area comprehensively.
- **Flexible Observer Offset:** Users can specify the observer height, or it defaults to 1.70 meters, simulating the average human eye level, which affects visibility calculations especially in varied terrain.

### 3. Optimized Viewshed Calculation

- **Parallel Processing:** The script enables parallel processing by setting the Parallel Processing Factor to 100%, allowing the use of all available CPU cores to speed up the computation significantly.
- **Use of ArcGIS Tools:** It employs ArcGIS Pro’s Geodesic Viewshed tool, which is optimized for performance (enables the utilization of the GPU and CPU) and can handle complex visibility calculations efficiently.
- **Efficient Memory Management:** Temporary data during processing, like the intermediate DEM and fishnet, are stored in memory to speed up processing and reduce disk I/O.

### 4. Output Customization and Management

- **User-defined Outputs:** The output raster name is user-defined, offering flexibility in managing output files.

The figure below schematically illustrates the process.

![Process illustration](https://imgur.com/rH3FM6p.png)

After developing the script, I integrated it into ArcGIS Pro and converted it into a functional tool. This script tool is stored within a toolbox labeled **_TotalViewshed.atbx._** located in this repository.

To learn how to install and use the tool, please refer to the user manual.

if you are interested in learning more about the entire process behind the development of this solution, click [here](https://storymaps.arcgis.com/stories/c13f7f8ed5314a4bb646c60ecfe2ba2a) to read my article.

## Limitations

- **Computational Load:** While the tool is optimized for efficiency, processing very large or extremely high-resolution DEMs can still be computationally intensive and time-consuming. Users with limited computational resources may experience longer processing times.
- **Terrain Complexity:** The tool may struggle with highly complex or irregular terrain features where standard algorithms might not capture all visibility nuances. In such cases, additional refinement of the script or advanced algorithms might be necessary.
- **Integration with Other Tools:** The tool is designed for ArcGIS Pro, which may limit its use for users of other GIS platforms like QGIS. Integration with other platforms would require additional development.

## References

- La Rosa, D., & Izakovičová, Z. (2022). Visibility analysis to enhance landscape protection: A proposal of planning norms and regulations for Slovakia. Land, 11(7), 977. [Link](https://www.mdpi.com/2073-445X/11/7/977).
- Llobera, M. (2003). Extending GIS-based visual analysis: The concept of visualscapes. International Journal of Geographical Information Science, 17(1), 25-48. [Link](https://www.researchgate.net/publication/32897058_Extending_GIS-based_visual_analysis_The_concept_of_visualscapes).
- Llobera, M., Wheatley, D., Steele, J., Cox, S., & Parchment, O. (2010). Calculating the inherent visual structure of a landscape (‘total viewshed’) using high-throughput computing. In F. Niccolucci & S. Hermon (Eds.), Beyond the artefact: Digital interpretation of the past: Proceedings of CAA2004, Prato 13–17 April 2004 (pp. 146–151). Budapest: Archaeolingua. [Google scholar](<https://scholar.google.com/scholar?q=Llobera,+M.,+Wheatley,+D.,+Steele,+J.,+Cox,+S.+&+Parchment,+O..+2010.+Calculating+the+inherent+visual+structure+of+a+landscape+(%E2%80%98total+viewshed%E2%80%99)+using+high-throughput+computing,+in+F.+Niccolucci+&+S.+Hermon+(ed.)+Beyond+the+artefact:+digital+interpretation+of+the+past:+Proceedings+of+CAA2004,+Prato+13%E2%80%9317+April+2004:+146%E2%80%9351.+Budapest:+Archaeolingua.>).

## License

This project is licensed under the MIT License. See the LICENSE file for details.
