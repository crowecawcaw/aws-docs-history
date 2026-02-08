# 3D Features

Amazon Location Service's 3D visualization capabilities - terrain and buildings - help users make better decisions by adding depth and perspective to geographic data. 3D terrain reveals elevation changes critical for route optimization, emergency response planning, and outdoor recreation, while 3D buildings provide spatial context for urban navigation, real estate assessment, and landmark identification. These features integrate seamlessly through simple API parameters (terrain, buildings), enabling applications across logistics, public safety, tourism, and real estate to deliver more intuitive and engaging user experiences without complex implementation.

## 3D Terrain

The 3D Terrain feature renders elevation data of the Earth’s surface as a three-dimensional surface, allowing users to view landscapes from multiple angles and perspectives. By controlling the viewing angle, users can more easily gain depth perception and assess terrain complexity, slopes, and relative heights across mapped areas.

Use the `terrain` parameter in your API request to enable three-dimensional terrain visualization. This feature provides an immersive perspective of topographic features, making it particularly useful for understanding spatial relationships in mountainous or varied terrain.

Combine 3D terrain with `contour-density` parameter in your API request for enhanced elevation precision and visual context. See [how to show 3D features on a map](how-to-show-3d-features-map.md "how-to-show-3d-features-map.md").

![](/images/location/latest/developerguide/images/zoom-3d-terrain.gif)

## 3D Buildings

The 3D Buildings feature renders building footprints as three-dimensional structures with height and volume, allowing users to visualize urban environments from multiple angles and perspectives. By controlling the viewing angle, users can more easily understand building density, height relationships, and spatial context within cities and developed areas.

Use the `buildings` parameter in your API request to enable three-dimensional building visualization. This feature provides an immersive perspective of urban landscapes, making it particularly useful for understanding city layouts, identifying landmarks, and navigating complex urban environments.See [how to show 3D features on a map](how-to-show-3d-features-map.md "how-to-show-3d-features-map.md").

![](/images/location/latest/developerguide/images/zoom-3d-buildings.gif)
