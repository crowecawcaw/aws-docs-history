

# Hybrid map style
<a name="hybrid-map-style"></a>

The Hybrid map style combines global satellite imagery with the same clear labels and configurable points of interest (POI) categories found in the Standard map style. This combination provides rich geographic detail while ensuring readability and usability for your application.

## Rich points of interest (POI)
<a name="hybrid-rich-poi"></a>

The labels and POIs have been specifically designed for contrast and readability, providing the necessary context for the satellite layer without distracting from the detailed imagery. Light road lines highlight the urban structure when zoomed out and gradually fade as you zoom in, revealing more detailed street-level information.

The Hybrid map style supports the same `PoiDensity` and `PoiCategories` parameters as the Standard style. For details on supported values and use cases, see [Rich points of interest (POI)](standard-map-style.md#standard-rich-poi) in the Standard map style and the [Maps features](https://docs.aws.amazon.com/location/latest/developerguide/maps-concepts.html#maps-concepts-features) reference.

For instructions on using these parameters, see [How to filter POI on the map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-filter-poi-map.html).

------
#### [ Zoom ]

![Animated demonstration of the Hybrid map style zooming through multiple levels, showing satellite imagery with overlaid labels.](http://docs.aws.amazon.com/location/latest/developerguide/images/hybrid_zoom.gif)


------
#### [ Neighborhood ]

![Hybrid map style at neighborhood zoom level showing satellite imagery with street names and points of interest labels.](http://docs.aws.amazon.com/location/latest/developerguide/images/hybrid-neighborhood.png)


------
#### [ Zoomed-in ]

![Hybrid map style at high zoom level showing detailed satellite imagery with building outlines and street labels.](http://docs.aws.amazon.com/location/latest/developerguide/images/hybrid-zoom.png)


------

## Designed for the world
<a name="designed-for-the-world"></a>

The Hybrid style supports different political views, ensuring that the map displays the correct borders for your users. This style also allows for easy switching between languages for map labels, with dozens of supported languages and writing systems available to ensure a localized experience.