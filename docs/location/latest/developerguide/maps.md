# Amazon Location Service Maps

![Map icon leading to SDK package, then to multiple devices showing maps.](images/maps-overview.png)
The Amazon Location Service Map gives you access to the underlying base map data for 190 countries with 5
million daily updates. Through both static and dynamic map capabilities, you gain
flexibility to cater to diverse user needs and deliver immersive, contextually relevant
mapping solutions.

Static maps offer pre-rendered representations of geographic data, enabling you to embed
high-quality visuals that enhance reports and provide spatial context in emails. Dynamic
maps allow you to create interactive and responsive experiences, where users can pan, zoom,
and explore the map in real-time, aligning with the requirements and preferences of your
business. Whether you're showing real-time turn-by-turn navigation, visualizing
location-based data, or enabling users to explore new areas, Amazon’s services equip you
with the tools to deliver tailored solutions that resonate with your audience.

## Features

The Amazon Location Service offers dynamic maps and static maps.

**Dynamic maps**

You can use AWS Map Styles such as standard, monochrome, hybrid, and
satellite. You can add an interactive map to your application using AWS
Map Styles with a map rendering engine such as MapLibre. Dynamic maps also
support map gestures such as zoom, pan, ease, fly, pitch, rotate, and
bearing.

**Static maps**

You can use static map URLs to embed simple map images on your website,
report, or email without the need for a map rendering engine. Static maps
allow you to overlay markers (or pins), routes, and polygon areas as needed
for your application.

**Political view**

To switch from the international perspective to a country-specific
geopolitical view, use the political view parameter in your API query. This
helps businesses comply with local laws, as certain countries require
adherence to their specific geopolitical views for maps and map data.

**Terrain**

You can display topography of a region with elevation shading using the
terrain parameter in your API query. This helps show physical terrain
details and geographic elevation changes.

**ContourDensity**

You can show terrain steepness and shape through elevation contour lines
using the contour density parameter in your API query. This provides
detailed information about land forms at varying density levels.

**Traffic**

You can display real-time traffic conditions on your map using the traffic
parameter in your API query. This shows current road congestion,
construction, and incidents, enabling informed routing decisions.

**TravelMode**

You can display transportation-specific routing information using the
travel mode parameter in your API query. This shows relevant transit systems
(buses, trains, subways) or truck routing data with road restrictions for
specialized navigation needs.

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

| API Name           | Short Description                                                                                                                             | Resources                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| GetStyleDescriptor | Retrieves the available map styles, such as standard, monochrome,<br>hybrid, and satellite, that can be applied to maps.                      | [AWS map styles and customization](map-styles.md "map-styles.md") |
| GetTile            | Fetches individual map tiles based on a specified style and zoom<br>level, allowing for the rendering of maps at various levels of<br>detail. | [Tiles](tiles.md "tiles.md")                                      |
| GetStaticMap       | Generates a static map image based on specific coordinates and<br>parameters, useful for embedding maps in reports or emails.                 | [Static maps](static-maps.md "static-maps.md")                    |

## Displaying Map

| Topic                  | Short Description                                                                                                                                                           | Resources                                                                                                                                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Styling Dynamic Map    | Amazon Location Service provides two options for styling your dynamic maps namely<br>using predesigned AWS Map Styles and customizing map style using<br>style descriptors. | [Style dynamic maps](styling-dynamic-maps.md "styling-dynamic-maps.md")<br>[Standard map style](standard-map-style.md "standard-map-style.md")<br>[Monochrome map style](monochrome-map-style.md "monochrome-map-style.md")<br>[Hybrid map style](hybrid-map-style.md "hybrid-map-style.md") |
| Rendering Dynamic Map  | Amazon Location Service recommends rendering maps using the MapLibre rendering engine.<br>MapLibre is an engine for displaying maps in web<br>or mobile applications.       | [Map Rendering SDK by language](map-rendering-by-language.md "map-rendering-by-language.md")                                                                                                                                                                                                 |
| Customizing Static Map | How to customize static maps generated using Amazon Location Service.                                                                                                       | [Customize static maps](customizing-static-maps.md "customizing-static-maps.md")                                                                                                                                                                                                             |
| Overlaying Static Map  | Overlay on your static maps to enhance the map's visual<br>representation.                                                                                                  | [Overlay on the static map](overlaying-static-map.md "overlaying-static-map.md")                                                                                                                                                                                                             |
