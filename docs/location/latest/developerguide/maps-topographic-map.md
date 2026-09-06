

# Topography
<a name="maps-topographic-map"></a>

Topographic features such as terrain and contour lines display elevation changes and geographic features. This helps users better understand the physical landscape and terrain characteristics of their mapped areas.

## Terrain
<a name="maps-topographic-terrain"></a>

The terrain feature displays the earth's surface with elevation shading, representing elevation changes and natural landforms. It helps users interpret the shape and structure of the landscape within their mapped regions.

Use the `terrain` parameter in your API request to display regional topography with elevation shading. This feature highlights variations in elevation and geographic features, helping users better visualize the physical landscape. See [How to create topographic maps](https://docs.aws.amazon.com/location/latest/developerguide/how-to-create-topographic-maps.html).

![](http://docs.aws.amazon.com/location/latest/developerguide/images/map-topographic-terrain.gif)


## 3D Terrain
<a name="maps-topographic-3d-terrain"></a>

The 3D Terrain feature renders elevation data of the Earth's surface as a three-dimensional surface, allowing users to view landscapes from multiple angles and perspectives. By controlling the viewing angle, users can more easily gain depth perception and assess terrain complexity, slopes, and relative heights across mapped areas.

Use the `terrain` parameter in your API request to enable three-dimensional terrain visualization. This feature provides an immersive perspective of topographic features, making it particularly useful for understanding spatial relationships in mountainous or varied terrain.

Combine 3D terrain with `contour-density` parameter in your API request for enhanced elevation precision and visual context. See [Create a 3D map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-create-a-3d-map.html).

------
#### [ Satellite ]

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-hybrid-3d-terrain.gif)


------
#### [ Standard ]

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-3d-terrain.gif)


------

## Contour density
<a name="maps-topographic-contour-density"></a>

The contour density feature visualizes contour lines to represent terrain steepness and elevation variation. Users can easily identify slopes, elevation gradients, and other topographic patterns with this.

Use the `contour-density` parameter in your API request to render topographical elevation contour lines that represent terrain steepness and shape. This provides detailed visualization of landforms at varying density levels for enhanced topographic understanding. See [How to create topography maps](https://docs.aws.amazon.com/location/latest/developerguide/how-to-create-topographic-maps.html).

------
#### [ Low ]

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-contours-low.gif)


------
#### [ Medium ]

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-contours-medium.gif)


------
#### [ High ]

![](http://docs.aws.amazon.com/location/latest/developerguide/images/zoom-contours-high.gif)


------