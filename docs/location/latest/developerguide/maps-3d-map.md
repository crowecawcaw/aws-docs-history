

# 3D Features
<a name="maps-3d-map"></a>

Amazon Location Service's 3D visualization capabilities - terrain and buildings - help users make better decisions by adding depth and perspective to geographic data. 3D terrain reveals elevation changes critical for route optimization, emergency response planning, and outdoor recreation, while 3D buildings provide spatial context for urban navigation, real estate assessment, and landmark identification. These features integrate seamlessly through simple API parameters (terrain, buildings), enabling applications across logistics, public safety, tourism, and real estate to deliver more intuitive and engaging user experiences without complex implementation.

## 3D Terrain
<a name="maps-3d-terrain"></a>

The 3D Terrain feature renders elevation data of the Earth’s surface as a three-dimensional surface, allowing users to view landscapes from multiple angles and perspectives. By controlling the viewing angle, users can more easily gain depth perception and assess terrain complexity, slopes, and relative heights across mapped areas.

Use the `terrain` parameter in your API request to enable three-dimensional terrain visualization. This feature provides an immersive perspective of topographic features, making it particularly useful for understanding spatial relationships in mountainous or varied terrain.

Combine 3D terrain with `contour-density` parameter in your API request for enhanced elevation precision and visual context. See [Create a 3D map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-create-a-3d-map.html).

------
#### [ Satellite ]

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-hybrid-3d-terrain.gif)


------
#### [ Standard ]

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-3d-terrain.gif)


------

## 3D Buildings
<a name="maps-3d-buildings"></a>

The 3D Buildings feature renders building footprints as three-dimensional structures with height and volume, allowing users to visualize urban environments from multiple angles and perspectives. By controlling the viewing angle, users can more easily understand building density, height relationships, and spatial context within cities and developed areas.

Use the `buildings` parameter in your API request to enable three-dimensional building visualization. This feature provides an immersive perspective of urban landscapes, making it particularly useful for understanding city layouts, identifying landmarks, and navigating complex urban environments. See [Create a 3D map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-create-a-3d-map.html).

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-3d-buildings.gif)


## Globe View
<a name="maps-3d-globe-view"></a>

The Globe View feature provides a spherical representation of the Earth, allowing users to visualize geographic data on a three-dimensional globe. This perspective offers a natural and intuitive way to understand global spatial relationships, continental layouts, and the curvature of the Earth's surface.

Use Globe View to display maps with realistic Earth curvature and global perspective. See [Create a 3D map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-create-a-3d-map.html).

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-globe-view.gif)
