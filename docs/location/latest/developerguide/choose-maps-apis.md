

# Map APIs
<a name="choose-maps-apis"></a>

Maps provide access to both dynamic and static map types for a variety of applications. For more information, See [Amazon Location Service Maps](maps.md).
+ **Dynamic Maps**: Interactive maps that can be customized in real time, allowing users to pan, zoom, and overlay data. For more information, See [Dynamic maps](dynamic-maps.md).
+ **Static Maps**: Static images of maps that display specific locations or routes without interactive elements, suitable for applications with limited interactivity. For more information, See [Static maps](static-maps.md).

The following table presents a number of business use cases that are best solved with Maps APIs.

## Maps use cases
<a name="maps-table"></a>

The following section presents a number of business use cases that are best solved with Maps APIs.


| **Business need** | **Useful API** | **Examples** | 
| --- | --- | --- | 
| **Display interactive maps**<br />Supports map gestures, such as zoom, pan, ease, fly, pitch, rotate, and bearing. | `GetTile` and `GetStyleDescriptor` with rendering engine (MapLibre) | [How to display a map](how-to-display-a-map.md) | 
| **Add markers to a map**<br />Examples are markers, icon, and more. | `GetTile` and `GetStyleDescriptor` with rendering engine (MapLibre) | [How to add a marker on the map](how-to-add-marker-on-map.md)<br />[How to add an icon on the map](how-to-add-icon-on-map.md) | 
| **Add user interaction components to a map**<br />Examples are showing map in preferred language or geo-political view. | `GetTile` and `GetStyleDescriptor` with rendering engine (MapLibre) | [How to add control on the map](how-to-add-control-on-map.md)<br />[How to add a popup to a map](how-to-add-popup-to-map.md) | 
| **Visualize real time or pre-recorded data on a map**<br />Examples are heat map, KML, GeoJSON features, polygons, rectangles, polylines, circles, markers, and more. | `GetTile` and `GetStyleDescriptor` with rendering engine (MapLibre) | [How to add a line on the map](how-to-add-line-on-map.md)<br />[How to add a polygon on the map](how-to-add-polygon-on-map.md) | 
| **Display map with localization**Examples are showing map in preferred language or geo-political view. | `GetTile` and `GetStyleDescriptor` with rendering engine (MapLibre) | [How to set a preferred language for a map](how-to-set-preferred-language-map.md)<br />[How to set the political view of a map](how-to-set-political-view-map.md) | 
| **Display a static map image**<br />For example, use map image in application, email, report, or print. | `GetStaticMap` | [How to get a static map of a specific position](get-static-map-specific-position.md)<br />[How to get a static map of a specific dimension](get-static-map-specific-dimension.md)<br />[How to decide between radius and zoom for a static map](choose-radius-vs-zoom.md)<br />[How to add scale for a static map](add-scale-static-map.md) | 
| **Add marker to a map image**<br />Examples are markers, proximity circle, icon, and more. | `GetStaticMap` | [How to add a marker to a static map](add-marker-static-map.md) | 
| **Visualize data on a map image**<br />Examples are GeoJSON features, polygons, rectangles, polylines, circles, and more. | `GetStaticMap` | [How to add a line to a static map](how-to-add-line-static.md) | 
| **Visualize real world use case on a map**<br />Examples include routes, proximity circle, and more. | `GetStaticMap` | [How to add a route to a static map](how-to-add-route.md) | 
| **Visualize Places search and/or geocode result on a map **All APIs return geocoordinates, except autocomplete.  | GetTile and GetStyleDescriptor with rendering engine (MapLibre) with Places API |  | 
| **Draw a route on a map**Supports waypoint marking. | GetTile and GetStyleDescriptor with rendering engine (MapLibre) with Calculate route  |  | 
| **Visualize matched GPS traces on a map **Supports travel modes, such as truck, pedestrian, car, and scooter.  | GetStyleDescriptor with rendering engine (MapLibre) with Snap to road  |  | 