# Tiles

Map tiles are pre-rendered, small sections of a larger map, typically displayed as
square images. They are used to efficiently display geographic data by loading only the
visible portions at different zoom levels. There are three main types of map
tiles:

For more information, see [GetTile](../APIReference/API_geomaps_GetTile.md "../APIReference/API_geomaps_GetTile.md") in the
_Amazon Location Service API Reference_.

## Tile types

**Vector map tiles**

Vector map tiles store map data as geometric shapes (points, lines,
polygons) rather than as images. This enables the creation of
high-quality, scalable maps that remain clear at any resolution.

**Raster map tiles**

Raster map tiles are pre-rendered images representing a specific
geographic area. Unlike vector tiles, raster tiles are simpler but lack
flexibility for restyling.

**Hybrid map tiles**

Hybrid map tiles combine both vector and raster data. They use vector
data for core map elements, such as roads, while using raster imagery
for more complex elements like detailed satellite or aerial
photography.

## Vector tile layers

The following are the 10 layers of vector map tiles:

- **Boundaries**: Defines administrative and
  geographic boundaries, including country, state, and city borders.
- **Buildings and addresses**: Represents
  building shapes and detailed address points.
- **Earth**: Shows global terrain and surface
  coverage for natural features like deserts, mountains, and forests.
- **Land use**: Displays categorized areas such
  as parks, farmland, and urban zones.
- **Places**: Identifies important locations
  like cities, towns, and notable landmarks.
- **Points of interest (POIs)**: Highlights
  attractions, businesses, and other key locations.
- **Roads**: Represents the network of streets,
  highways, and pathways.
- **Road labels**: Provides text labels for
  road names and route numbers.
- **Transit**: Depicts public transport lines
  such as buses, trains, and subways.
- **Water**: Displays bodies of water,
  including lakes, rivers, and oceans.

## Use cases

- Fetching map tiles for rendering different sections of a map at various
  zoom levels.
- Optimizing map tile requests based on user interaction, such as panning
  and zooming.
- Accessing vector or raster tiles for detailed rendering purposes.

## Understand the request

The request requires the following parameters: `Tileset`,
`X`, `Y`, and `Z` to identify the specific tile
to be fetched. The `Key` parameter can be optionally included for
authorization.

- **`Tileset`**: Specifies the
  desired tileset for fetching the tile.
- **`X`**: The X-axis value for the
  map tile.
- **`Y`**: The Y-axis value for the
  map tile.
- **`Z`**: The zoom value, defining
  the zoom level for the tile.
- **`Key`**: Optionally included for
  authorization purposes.

## Understand the response

The response includes headers such as `CacheControl`,
`ContentType`, and `ETag`, and contains the map tile data
as a binary blob in MVT format. These headers manage cache control, provide content
format details, and version control for tiles.

- **`CacheControl`**: Controls
  client-side caching for the map tile.
- **`ContentType`**: Specifies the
  format of the tile data.
- **`ETag`**: Provides a version
  identifier for the tile.
- **`Blob`**: Contains the vector
  tile data in MVT format.
