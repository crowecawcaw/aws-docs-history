# Amazon Location Service Maps

![Map icon leading to SDK package, then to multiple devices showing maps.](images/maps-overview.png)
Amazon Location Service Maps give you access to base map data for 190 countries with 5 million daily updates. Static and dynamic map capabilities provide flexibility to meet diverse user needs and deliver immersive, contextually relevant mapping solutions.

## Maps offering

Amazon Location Service offers dynamic and static maps.

**Dynamic maps**

Use AWS Map Styles including standard, monochrome, hybrid, and satellite. Add interactive maps to your application using AWS map style and [MapLibre](https://maplibre.org/ "https://maplibre.org/") rendering engine. Dynamic maps support gestures including zoom, pan, ease, fly, pitch, rotate, and bearing. For more details, see [dynamic maps](dynamic-maps.md "dynamic-maps.md").

**Static maps**

Use static map URLs to embed simple map images in websites, reports, or emails without a map rendering engine. Static maps support overlays including markers (pins), routes, and polygon areas for your application. For more details, see [static maps](static-maps.md "static-maps.md").

## Prebuilt map styles

AWS map styles follow recognized industry conventions and deliver a polished, professional visual appearance. These ready-made styles accelerate development without requiring custom cartographic design. Build attractive, user-ready maps with minimal effort. For more details, see [AWS map styles](map-styles.md "map-styles.md").

## Features

AWS Map features provide enhanced visualization options for geographic, [topographic](maps-topographic-map.md "maps-topographic-map.md"), and [navigation](maps-navigation-map.md "maps-navigation-map.md") such as transit, logistics, and real-time traffic data. Create informative, context-aware map experiences tailored to your specific needs. AWS maps support [internationalization and localization](maps-localization-internationalization.md "maps-localization-internationalization.md") including political views and languages. Choose Point of interest (POI) and [color schemes](maps-color-scheme.md "maps-color-scheme.md") that suit your use case. For more details, see [map features](maps-concepts.md "maps-concepts.md").

## Common use cases

**Embed maps in your application**

Build maps into your applications to create location-based experiences.
Visualize business locations, search for points of interest, and help users
find specific addresses. Enable seamless location sharing and geotagging
features to engage your customers. Use comprehensive map data, robust
geocoding, and flexible rendering to create customized, interactive maps
tailored to your needs. Integrate dynamic, high-quality mapping experiences
that drive user engagement and business insights into your application,
whether you're building a directory, ride-sharing app, or social
platform.

**Static maps for reporting or printing**

Seamlessly add images of street maps, satellite imagery, and
location-based visuals into your websites, documents, and applications.
Static maps enable you to create customizable map images that provide
geographical context, without complex client-side rendering. Display
delivery route on receipts, include location details in documents, or
integrate maps into your digital experiences.

**Analyze and visualize data**

Overlay your data onto high-quality maps to uncover transformative spatial
patterns and trends. Empower your teams to create customizable, interactive
map visualizations with your geographic data. Use maps and your data to
optimize site selection, plan infrastructure, or analyze market
opportunities.

**Enhance real estate experiences**

Provide prospective buyers with comprehensive location context for real
estate listings. Display the property's exact location, as well as
surrounding neighborhood details like jurisdictional boundaries, local
businesses, parks, and schools. Help customers find directions to your open
houses. Create informative, location-centric real estate experiences that
engage and inform your clients.

**Build engaging travel experiences**

Display dynamic maps showcasing destinations, with detailed street views
and key geographical features. Highlight hotels, restaurants, and other
points of interest for tourists and travelers. Plot outdoor amenities, like
hiking trails, to help users plan their ideal itinerary.

**Use maps to support disaster response efforts**

Timely and accurate location information is critical during crises. Use
mapping capabilities to build websites and applications that provide
essential context to communities during pending disasters like fires,
hurricanes, and floods. Display dynamic maps showcasing evacuation routes,
safe shelters, road closures, and traffic congestion to help empower
communities to quickly assess the situation and make informed
decisions.

## Standalone Map APIs

| API Name           | Short Description                                                                                                                             | Resources                                                    |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| GetStyleDescriptor | Retrieves the available map styles, such as standard, monochrome,<br>hybrid, and satellite, that can be applied to maps.                      | [AWS map styles and features](map-styles.md "map-styles.md") |
| GetTile            | Fetches individual map tiles based on a specified style and zoom<br>level, allowing for the rendering of maps at various levels of<br>detail. | [Tiles](tiles.md "tiles.md")                                 |
| GetStaticMap       | Generates a static map image based on specific coordinates and<br>parameters, useful for embedding maps in reports or emails.                 | [Static maps](static-maps.md "static-maps.md")               |

## Displaying Map

| Topic                  | Short Description                                                                                                                                                           | Resources                                                                                                                                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Styling Dynamic Map    | Amazon Location Service provides two options for styling your dynamic maps namely<br>using predesigned AWS Map Styles and customizing map style using<br>style descriptors. | [Style dynamic maps](styling-dynamic-maps.md "styling-dynamic-maps.md")<br>[Standard map style](standard-map-style.md "standard-map-style.md")<br>[Monochrome map style](monochrome-map-style.md "monochrome-map-style.md")<br>[Hybrid map style](hybrid-map-style.md "hybrid-map-style.md") |
| Rendering Dynamic Map  | Amazon Location Service recommends rendering maps using the MapLibre rendering engine.<br>MapLibre is an engine for displaying maps in web<br>or mobile applications.       | [Map Rendering SDK by language](map-rendering-by-language.md "map-rendering-by-language.md")                                                                                                                                                                                                 |
| Customizing Static Map | How to customize static maps generated using Amazon Location Service.                                                                                                       | [Customize static maps](customizing-static-maps.md "customizing-static-maps.md")                                                                                                                                                                                                             |
| Overlaying Static Map  | Overlay on your static maps to enhance the map's visual<br>representation.                                                                                                  | [Overlay on the static map](overlaying-static-map.md "overlaying-static-map.md")                                                                                                                                                                                                             |
