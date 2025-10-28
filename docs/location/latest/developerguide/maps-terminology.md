# Maps terminology

This section defines key terms related to Amazon Location Service Maps, providing insights into core concepts like basemaps, vector and raster data, map rendering, and map styles. Understanding these terms is essential for effectively utilizing the Amazon Location Service mapping APIs and resources.

**Basemap**

A basemap provides geographic context to your map, stored as vector tile layers. These tile layers include geographical features such as street names, buildings, and land use for visual reference.

**Vector**

Vector data consists of points, lines, and polygons, and is used to represent roads, locations, and areas on a map. Vector shapes can also be used as icons for markers on a map.

**Raster**

Raster data is image data made up of a grid, typically representing continuous data like terrain, satellite imagery, or heat maps. Raster images can also be used as icons or textures on a map.

**Map Rendering**

The map rendering library pulls data from Amazon Location Service at runtime, rendering the map based on the selected map resource. A map resource defines the data provider and map style. Amazon Location Service recommends using the MapLibre rendering engine.

**Vector Tile**

A vector tile is a format that stores map data using vector shapes. It adjusts to the display resolution and selectively renders features, while maintaining a small file size for optimal performance. Supported format: Mapbox Vector Tiles (MVT).

**Map Style**

A map style defines color and other styling information for the map data, determining how the map will appear when rendered. Amazon Location Service provides map styles based on the Mapbox GL style specification.

**Glyph File**

A binary file containing encoded Unicode characters, used by a map renderer to display labels.

**Sprite File**

A Portable Network Graphic (PNG) image file that contains small raster images and corresponding location descriptions in a JSON file. Used by a map renderer to display icons or textures on a map.

**Bounding Box**

A bounding box is defined by two diagonal corner points: the northwest (NW) (top-left) and southeast (SE) (bottom-right) points. These points are key for specifying the spatial extent of an map.
