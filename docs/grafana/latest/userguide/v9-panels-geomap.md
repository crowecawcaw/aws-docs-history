# Geomap panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

The Geomap panel visualization allows you to view and customize the world map using
geospatial data. You can configure various overlay styles and map view settings to
easily focus on the important location-based characteristics of the data.

## Map View

The map view controls the initial view of the map when the dashboard loads.

**Initial View**

The initial view configures how the GeoMap panel renders when the panel is
first loaded.

- **View** sets the center for the map
  when the panel first loads.
  - **Fit to data** fits the map
    view based on the data extents of Map
    layers and updates when data changes.
    - **Data**
      option allows selection of extent based on
      data from “All layers”, a single “Layer”, or the
      “Last value” from a selected layer.
    - **Layer**
      can be selected if fitting data from a
      single “Layer” or the “Last value” of a
      layer.
    - **Padding**
      sets padding in relative percent beyond
      data extent (not available when looking at “Last
      value” only).
    - **Max Zoom**
      sets the maximum zoom level when fitting
      data.

  - **Coordinates**
    sets the map view based on:
    - **Latitude**
    - **Longitude**

  - Default Views are also available including:
    - **(0°, 0°)**
    - **North America**
    - **South America**
    - **Europe**
    - **Africa**
    - **West Asia**
    - **South Asia**
    - **South-East Asia**
    - **East Asia**
    - **Australia**
    - **Oceania**

- **Zoom** sets the initial zoom level.

## Map layers

The Geomap visualization supports showing multiple layers. Each layer determines
how you visualize geospatial data on top of the base map.

**Types**

There are three map layer types to choose from in the Geomap
visualization.

- [Markers layer](#v9-panels-geomap-markers "#v9-panels-geomap-markers") renders a marker at each data point.
- [Heatmap layer](#v9-panels-geomap-heatmap "#v9-panels-geomap-heatmap") visualizes a heatmap of the data.
- [GeoJSON layer](#v9-panels-geomap-geojson "#v9-panels-geomap-geojson") renders static data from a GeoJSON file.

There are also five layer types that are currently in alpha.

- [Night / Day layer (Alpha)](#v9-panels-geomap-nightday "#v9-panels-geomap-nightday") renders a night or day
  region.
- **Icon at last point (alpha)** renders an
  icon at the last data point.
- **Dynamic GeoJSON (alpha)** styles a
  GeoJSON file based on query results.
- **Route (alpha)** render data points as a
  route.
- [Photos layer (Alpha)](#v9-panels-geomap-photos "#v9-panels-geomap-photos") renders a photo at each data point.

**Layer Controls**

The layer controls allow you to create layers, change their name, reorder and
delete layers.

- **Add layer** creates an additional,
  configurable data layer for the Geomap
  visualization. When you add a layer, you are prompted to select a
  layer type. You can change the layer type at any point during panel
  configuration. See the **Layer Types**
  section above for details on each layer type.
- The layer controls allow you to rename, delete, and reorder the
  layers of the panel.
  - **Edit layer name** (pencil
    icon) renames the layer.
  - **Trash Bin** deletes the layer.
  - **Reorder** (six dots/grab
    handle) allows you to change the layer order. Data on higher
    layers will appear above data on lower layers. The panel
    will update the layer order as you drag and drop to help
    simplify choosing a layer order.

You can add multiple layers of data to a single Geomap panel in order to
create rich, detailed visualizations.

**Location**

The Geomap panel needs a source of geographical data. This data comes from a
database query, and there are four mapping options for your data.

- **Auto** automatically searches for
  location data. Use this option when
  your query is based on one of the following names for data
  fields.
  - geohash: “geohash”
  - latitude: “latitude”, “lat”
  - longitude: “longitude”, “lng”, “lon”
  - lookup: “lookup”

- **Coords** specifies that your query
  holds coordinate data. You will get
  prompted to select numeric data fields for latitude and longitude
  from your database query.
- **Geohash** specifies that your query
  holds geohash data. You will be
  prompted to select a string data field for the geohash from your
  database query.
- **Lookup**
  specifies that your query holds location name data that needs to
  be mapped to a value. You will be prompted to select the lookup
  field from your database query and a gazetteer. The gazetteer is the
  directory that is used to map your queried data to a geographical
  point.

## Markers layer

The markers layer allows you to display data points as different marker shapes
such as circles, squares, triangles, stars, and more.

Markers have many customization options.

- **Marker Color** configures the color
  of the marker. The default `Single color` keeps all points
  a single color. There is an alternate option to have
  multiple colors depending on the data point values and the threshold set
  at the `Thresholds` section.
- **Marker Size** configures the size of
  the marker. The default is `Fixed size`, which makes all
  marker sizes the same regardless of the data points.
  However, there is also an option to scale the circles to the
  corresponding data points. `Min` and `Max`
  marker size has to be set such that the Marker layer can scale within
  this range.
- **Marker Shape** allows you to choose
  the shape, icon, or graphic to aid in providing
  additional visual context to your data. Choose from assets that are
  included with Grafana such as simple shapes or the Unicon library. You
  can also specify a URL containing an image asset. The image must be a
  scalable vector graphic (SVG).
- **Fill opacity** configures the
  transparency of each marker.

## Heatmap layer

The heatmap layer clusters various data points to visualize locations with
different densities. To add a heatmap layer:

Click on the dropdown menu under Data Layer and choose
`Heatmap`.

Similar to `Markers`, you are prompted with options to
determine which data points to visualize and how you want to visualize
them.

- **Weight values** configure the intensity
  of the heatmap clusters. `Fixed value` keeps a constant
  weight value throughout all data points. This value
  should be in the range of 0~1. Similar to Markers, there is an alternate
  option in the dropdown to automatically scale the weight values
  depending on data values.
- **Radius** configures the size of the
  heatmap clusters.
- **Blur** configures the amount of
  blur on each cluster.

## GeoJSON layer

The GeoJSON layer allows you to select and load a static GeoJSON file from the
filesystem.

- **GeoJSON URL** provides a choice
  of GeoJSON files that ship with Grafana.
- **Default Style** controls which
  styles to apply when no rules above match.
  - **Color** configures
    the color of the default style
  - **Opacity** configures
    the default opacity

- **Style Rules** apply styles
  based on feature properties
  - **Rule** allows you to
    select a _feature_,
    _condition_, and
    _value_ from the GeoJSON file in
    order to define a rule. The trash bin icon can be used
    to delete the current rule.
  - **Color** configures the color
    of the style for the current rule
  - **Opacity** configures the
    transparency level for the current rule

- **Add style rule** creates additional
  style rules.

## CARTO layer

A CARTO layer is from [CARTO](https://carto.com/about-us/ "https://carto.com/about-us/")
Raster basemaps.

**Options**

- **Theme**

Choose a theme, either a **Light** theme,
**Dark** theme, or
**Auto** theme.

- **Show labels** shows the Country
  details on top of the map.
- **Opacity** from 0 (transparent)
  to 1 (opaque)

## XYZ tile layer

The XYZ tile layer is a map from a generic tile layer.

###### Note

For more information about generic tile layers, see [Tiled Web
Maps](https://en.wikipedia.org/wiki/Tiled_web_map "https://en.wikipedia.org/wiki/Tiled_web_map"), and [List of Open Street Map Tile Servers](https://wiki.openstreetmap.org/wiki/Tile_servers "https://wiki.openstreetmap.org/wiki/Tile_servers").

**Options**

- **URL template**

###### Note

Set a valid tile server url, with {z}/{x}/{y} for example:
`https://tile.openstreetmap.org/{z}/{x}/{y}.png`.

- **Attribution** sets the reference
  string for the layer if displayed in [map controls](#v9-panels-geomap-controls "#v9-panels-geomap-controls")
- **Opacity** from 0 (transparent) to 1
  (opaque)

## Open Street Map layer

A map from [Open Street
Map](https://www.openstreetmap.org/about "https://www.openstreetmap.org/about"), a collaborative, free geographic world database.

**Options**

- **Opacity** from 0 (transparent)
  to 1 (opaque)

## ArcGIS layer

An [ArcGIS](https://services.arcgisonline.com/arcgis/rest/services "https://services.arcgisonline.com/arcgis/rest/services") layer is a layer from an [ESRI](https://www.esri.com/en-us/about/about-esri/overview "https://www.esri.com/en-us/about/about-esri/overview")
ArcGIS MapServer.

**Options**

- **Server Instance** to select from the
  following map types.
  - World Street Map
  - World Imagery
  - World Physical
  - Topographic
  - USA Topographic
  - World Ocean
  - Custom MapServer (see [XYZ](#v9-panels-geomap-xyz "#v9-panels-geomap-xyz") for formatting)
    - URL template
    - Attribution

- **Opacity** from 0 (transparent) to 1
  (opaque)

## Night / Day layer (Alpha)

The Night / Day layer displays night and day regions based on the current time
range.

###### Note

For more information, see[Extensions for OpenLayers - DayNight](https://viglino.github.io/ol-ext/examples/layer/map.daynight.html "https://viglino.github.io/ol-ext/examples/layer/map.daynight.html").

**Options**

- **Show** toggles time source from panel
  time range
- **Night region color** picks color for night
  region
- **Display sun** toggles sun icon
- **Opacity** from 0 (transparent) to 1
  (opaque)

## Photos layer (Alpha)

The Photos layer renders a photo at each data point.

###### Note

For more information, see [Extensions for OpenLayers - Image Photo Style](http://viglino.github.io/ol-ext/examples/style/map.style.photo.html "http://viglino.github.io/ol-ext/examples/style/map.style.photo.html").

**Options**

- **Image Source Field**

Select a string field containing image data in either of the
following formats:

    + **Image URLs**
    + **Base64 encoded** image
     binary (`data:image/png;base64,…`)

- **Kind**

select the frame style around the images

    + **Square**
    + **Circle**
    + **Anchored**
    + **Folio**

- **Crop** toggle if the images are
  cropped to fit
- **Shadow** toggle a box shadow behind
  the images
- **Border** set the border size around
  images
- **Border color** set the border color
  around images
- **Radius** set the overall size of
  images in pixels

## Map Controls

The map controls interface contains the following options for map information
and tool overlays.

**Zoom**

This section describes each of the zoom controls.

_Show zoom control_

Displays zoom controls in the upper left corner.

_Mouse wheel zoom_

Turns on or off using the mouse wheel for zooming in or out.

**Show attribution**

Displays attribution for basemap layers on the map.

**Show scale**

Displays scale information in the bottom left corner.

###### Note

Displays units in [m]/[km].

**Show measure tools**

Displays measure tools in the upper right corner. Measurements appear only
when this control is open.

- **Click** to start measuring
- **Continue clicking** to continue
  measurement
- **Double-click** to end measurement

###### Note

When you change measurement type or units, the previous measurement is
removed from the map.

If the control is closed and then re-opened, the most recent measurement
is displayed.

A measurement can be modified by clicking and dragging on it.

_Length_

Get the spherical length of a geometry. This length is the sum of the
great circle distances between coordinates. For multi-part geometries, the
length is the sum of the length of each part. Geometries are assumed to be
in ‘EPSG:3857’.

You can choose the following units for length measurements:

- **Metric (m/km)**
- **Feet (ft)**
- **Miles (mi)**
- **Nautical miles (nmi)**

_Area_

Get the spherical area of a geometry. This area is calculated assuming
that polygon edges are segments of great circles on a sphere. Geometries are
assumed to be in ‘EPSG:3857’.

You can choose the following units for area measurements:

- **Square Meters (m²)**
- **Square Kilometers (km²)**
- **Square Feet (ft²)**
- **Square Miles (mi²)**
- **Acres (acre)**
- **Hectare (ha)**

**Show debug**

Displays debug information in the upper right corner of the map. This can be
useful for debugging or validating a data source.

- **Zoom** displays the current zoom level
  of the map.
- **Center** displays the current
  **longitude**, and **latitude** of the map center.

**Tooltip**

- **None** displays tooltips only when a
  data point is clicked.
- **Details** displays tooltips when a pointer
  hovers over a data point.
