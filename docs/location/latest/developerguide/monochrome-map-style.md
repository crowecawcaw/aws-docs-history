

# Monochrome map style
<a name="monochrome-map-style"></a>

The Monochrome style is a minimalist canvas with a constrained color palette, designed for use with data visualization overlays. This style supports both light and dark modes, each of which communicates all the essential information needed for geographic context.

## Color schemes
<a name="color-schemes"></a>

The Monochrome style offers color choices for both dark and light modes.

------
#### [ Continent ]

![Map of North America showing the United States, Canada, Mexico, and parts of Central and South America.](http://docs.aws.amazon.com/location/latest/developerguide/images/monochrome-continent.png)


------
#### [ Neighborhood ]

![Map of Downtown Miami showing streets, parks, and landmarks in light and dark modes.](http://docs.aws.amazon.com/location/latest/developerguide/images/monochrome-neighborhood-colors.png)


------

## Use cases
<a name="use-case"></a>

The Monochrome style is well-suited for data visualization and minimalistic design needs.

### Data visualization
<a name="data-visualization"></a>

The Monochrome style deliberately uses only shades of gray, allowing you complete freedom of color choice for data overlay layers such as choropleths, heatmaps, or dot maps.

![Amazon Location Service Monochrome style used as a base layer for data visualization, with custom red data points overlaid on a neutral lower Manhattan map.](http://docs.aws.amazon.com/location/latest/developerguide/images/monochrome-data-vis.png)


### Minimalist design
<a name="minimalist"></a>

To maintain a clean and unobtrusive map, the Monochrome styles include a reduced set of points of interest (POIs) for essential features, such as airports, parks, hospitals, and universities.

------
#### [ Airport ]

![Map showing Miami International Airport and surrounding roads including Airport Expy and Dolphin Expy.](http://docs.aws.amazon.com/location/latest/developerguide/images/monochrome-airport.png)


------
#### [ Neighborhood ]

![Map showing Jackson Memorial Hospital, UHealth Tower, and nearby streets in light and dark modes.](http://docs.aws.amazon.com/location/latest/developerguide/images/monochrome-neighborhood.png)


------

Although the Monochrome style includes a reduced set of POIs, the underlying tiles still contain the complete set of POI data. This allows you to display POIs that are not visually present in the style.

## Designed for the world
<a name="designed-for-the-world"></a>

The Monochrome style supports different political views, ensuring that maps display the correct borders for your users. The style also allows for easy switching between languages for map labels, with dozens of supported languages and writing systems.

![Map of Taiwan showing major cities and the Taiwan Strait, with a monochrome color scheme.](http://docs.aws.amazon.com/location/latest/developerguide/images/monochrome-language-switcher.gif)
