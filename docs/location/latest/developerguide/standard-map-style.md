# Standard map style

The Standard map style offers a clean, modern, and general-purpose map design that can
seamlessly fit into almost any application or website.

## Color scheme

The Standard map style comes in both light and dark modes. The light mode is
versatile and can fit into any context, while the dark mode features a constrained
palette, designed to show details clearly and maintain readability in darker
environments. This ensures minimal distractions, especially in scenarios such as
night-time navigation.

Forest

![Amazon Location Service Standard map style Forest color scheme showing the Pacific Northwest with green terrain emphasis in light and dark modes.](images/color-scheme-forest.png)

Road

![Amazon Location Service Standard map style Road color scheme emphasizing highway networks and road infrastructure in light and dark modes.](images/color-scheme-road.png)

City

![Amazon Location Service Standard map style City color scheme optimized for urban detail with building footprints and transit in light and dark modes.](images/color-scheme-city.png)

Neighborhood

![Amazon Location Service Standard map style Neighborhood color scheme showing local streets, parks, and points of interest at a neighborhood zoom level.](images/color-scheme-neighborhood.png)

## A pleasing, modern palette

Soft colors provide important land-use context without overwhelming the map,
offering useful information at both high and low zoom levels. Zoomed out, features
such as forests, deserts, and glaciers add richness to the map. When zoomed in, a
range of colors highlights important landmarks like schools, hospitals, recreation
areas (like parks and sports facilities), and urban districts like commercial and
industrial zones.

The overall style features a cohesive color palette, including POI markers that
complement their respective land-use areas. The road network is displayed in shades
of gray, providing detail without overwhelming the map with bright, distracting
colors.

Highway

![Map of San Francisco Bay Area showing cities and highways in standard and dark modes.](images/modern-highway.png)

Beach

![Map of Malibu area showing Pacific Coast Highway, Legacy Park, and Malibu Lagoon State Beach.](images/modern-beach.png)

Island

![Map of Oahu island showing major highways, Honolulu, and surrounding areas in day and night views.](images/modern-island.png)

Neighborhood

![Map of downtown Honolulu showing streets, landmarks, and neighborhoods in light and dark modes.](images/modern-neighborhood.png)

Intersection

![Map of Lower Manhattan showing City Hall Park, streets, and landmarks in light and dark modes.](images/style-intersection.png)

Roundabout

![Map of Washington Circle area showing streets, landmarks, and points of interest in light and dark modes.](images/style-roundabout.png)

## Rich points of interest (POI)

The Standard map style supports a rich array of configurable points of interest
(POIs). Using the `PoiCategories` and `PoiDensity` parameters
in [GetStyleDescriptor](../APIReference/API_geomaps_GetStyleDescriptor.md "../APIReference/API_geomaps_GetStyleDescriptor.md"), you can choose which POI categories appear and how
many are shown. Amazon Location Service returns a style descriptor that renders only the requested
POIs, so maps display correctly with no additional client-side code.

### POI density

The `PoiDensity` parameter controls how many POIs render on the
map. Use lower density values to reduce visual clutter for apps with custom
markers, or higher values for discovery-focused applications.

### POI categories

The `PoiCategories` parameter filters the map to show only the
POI categories you specify. You can pass one or more categories to tailor the
map to your application's needs. When omitted, all categories are displayed.
For example, a property-listing site can surface only accommodations, a logistics
fleet app can show only transit and fuel, and a tourist map can highlight sights
and dining.

For more information about supported density levels and categories, see [Maps
features](maps-concepts.md#maps-concepts-features "maps-concepts.md#maps-concepts-features") and the [GetStyleDescriptor API Reference](../APIReference/API_geomaps_GetStyleDescriptor.md "../APIReference/API_geomaps_GetStyleDescriptor.md").
For instructions on using these parameters, see [How to filter
POI on the map](how-to-filter-poi-map.md "how-to-filter-poi-map.md").

The following tabs show examples of POI filtering and density configurations.

POI filtering

![Map showing POI category filtering with only selected categories visible on the map.](images/poi-toggle-animation.gif)

POI density

![Comparison of POI density levels showing increasing numbers of points of interest on the map.](images/poi-density.gif)

## Designed for the world

The Standard style supports different political views, ensuring that maps display
the correct borders for your users. The style also allows easy language switching
for map labels, with dozens of supported languages and writing systems.

To learn more, see [Localization and internationalization](maps-localization-internationalization.md "maps-localization-internationalization.md").

Languages

![Animated demonstration of the Amazon Location Service language switcher, cycling through map labels in different languages on a map of Taiwan.](/images/location/latest/developerguide/images/standard-language-switcher.gif)

Political view

![Two maps of Cyprus demonstrating Amazon Location Service political view options, showing how disputed territorial boundaries render differently based on country-specific perspectives.](images/maps-political-view.png)

## Topography

The Standard map style provides detailed topographic visualization that highlights
elevation variations and natural geographic features. Contour lines, shading, and terrain
textures create a realistic representation of the landscape, enabling users to easily
interpret slopes, valleys, and peaks. This topographic rendering is ideal for outdoor planning,
environmental analysis, and applications where understanding terrain characteristics enhances
decision-making and spatial awareness.

Both Terrain and Contour Density

![Topographic map showing Ireland Lake surrounded by contour lines indicating mountainous terrain.](images/map-terrain-contour-light.png)

![Topographic map showing terrain with contour lines, elevation changes, and Ireland Lake labeled.](images/map-terrain-contour-dark.png)

Only terrain

![Topographic map showing Yosemite National Park area with labeled lakes and terrain features.](images/map-terrain-light.png)

![Topographic map showing Yosemite National Park with surrounding lakes including Cherry Lake, Benson Lake, Tenaya Lake, Merced Lake, and Ireland Lake.](images/map-terrain-dark.png)

Only contour density

![Topographic map showing Ireland Lake surrounded by contour lines indicating terrain elevation.](images/map-contour-light.png)

![Topographic map showing terrain contours with Ireland Lake labeled in the center.](images/map-contour-dark.png)

## Navigation

The Standard map style provides options to provide dynamic visualization designed to
optimize navigation and route planning. Live traffic data highlights congestion, incidents,
and road conditions, enabling users to anticipate delays and adjust their routes accordingly.
With multiple travel modes—such as truck or public transit—this feature empowers users to select
the most efficient and context-appropriate option for their route, ensuring smoother and more informed
routing experiences.

Traffic

![Traffic map of New York City area showing road conditions with green, orange, and red routes.](images/traffic-light.png)

![Traffic map of New York City area showing road conditions with green, yellow, and red routes.](images/traffic-dark.png)

Transit

![Map showing New York City area including Manhattan, Brooklyn, Jersey City, and Hoboken with major highways and waterways.](images/transit-light.png)

![Map showing New York City area with colored route lines connecting Manhattan, Brooklyn, Jersey City, and surrounding regions.](images/transit-dark.png)

Truck

![Map of New York City area showing road closures marked with prohibition icons on major routes.](images/truck-light.png)

![Map of New York City area showing locations marked with circular icons containing symbols.](images/truck-dark.png)

## 3D

The Standard map style provides immersive three-dimensional visualization that renders terrain elevation and building structures with spatial depth and perspective. Adjustable viewing angles, pitch controls, and three-
dimensional rendering create a realistic representation of both natural landscapes and urban environments, enabling users to easily interpret elevation changes, terrain complexity, and spatial relationships.
This three-dimensional rendering is ideal for route planning, urban navigation, and applications where understanding vertical dimensions and depth perception enhances decision-making and spatial awareness..

3D Terrain

![3D terrain map showing snow-covered mountain peaks, valleys, and glaciers in an alpine region.](images/3d-terrain-light.png)

![Satellite map view showing terrain with water bodies in blue, land masses in dark gray, and labeled locations including Lac de Moiry and Siders.](images/3d-terrain-dark.png)

3D Buildings

![3D map view of downtown Seattle showing buildings, Interstate 5, and city blocks in gray and white.](images/3d-buildings-light.png)

![3D map view of urban area showing buildings, streets, and Interstate 5 highway with navigation routes.](images/3d-buildings-dark.png)

## Land use

The Standard map style uses vibrant colors to indicate designated land uses.
Greens represent forests, grass, golf courses, sports centers, and parks. Relevant
colors are used for water bodies, glaciers, deserts, and beaches. Additionally, land
uses such as commercial, industrial, airports, military zones, medical facilities,
and educational areas are highlighted with specific vibrant categories.

Light

![Land use color legend for the Amazon Location Service Standard Light style, showing color-coded categories such as parks, water, residential, and commercial areas with hex values.](images/land-use-light.png)

Dark

![Land use color legend for the Amazon Location Service Standard Dark style, showing color-coded categories for parks, water, residential, and commercial areas with hex values.](images/land-use-dark.png)
