# Geomap panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The **Geomap** panel visualization enables you to view and customize
the world map using geospatial data. To easily focus on the important location-based
characteristics of the data, you can configure various overlay styles and map view
settings.

## Data layer

The data layer in the Geomap plugin determines how you visualize geospatial data
on top of the base map.

### Location

The **Geomap** panel needs a source of geographical data.
This data comes from a database query, and there are four mapping options for
your data.

- Auto automatically searches for
  location data. Use this option when your query is based on one of the
  following names for data fields.
  - geohash: “geohash”
  - latitude: “latitude”, “lat”
  - longitude: “longitude”, “lng”, “lon”
  - lookup: “lookup”

- Coords specifies that your query holds
  coordinate data. You will get prompted to select numeric data fields for
  latitude and longitude from your database query.
- Geohash specifies that your query holds
  geohash data. You will get prompted to select a string data field for
  the geohash from your database query.
- Lookup specifies that your query holds
  location name data that needs to be mapped to a value. You will get
  prompted to select the lookup field from your database query and a
  `gazetteer`. The `gazetteer` is the directory that is used to map your queried data to a
  geographical point.

## Markers layer

The **Markers** layer allows you to display data points as
different marker shapes such as circle, squares, triangles, stars, and more.

- Marker Color configures the color of the
  marker. The default Fixed size keeps all points a single color. There is an
  alternate option to have multiple colors depending on the data point values
  and the threshold set at the **Thresholds** section.
- Marker Size configures the size of the
  marker. Default is `Fixed size` , making all marker size
  the same regardless of the data points. However, there is also an option to
  scale the circles to the corresponding data points. `Min`
  and `Max` marker size has to be set such that the Marker
  layer can scale within these ranges.
- Marker Shape provides you with the
  flexibility to visualize the data points differently.
  - Circle
  - Square
  - Triangle
  - Cross
  - X

- Fill opacity configures the transparency of
  each marker.

## Heatmap layer

The **Heatmap** layer clusters various data points to visualize
locations with different densities. To add a heatmap layer, under **Data
Layer**, choose **Heatmap**.

Similar to **Markers**, you are prompted with various options to
determine which data points to visualize and how.

- Weight values configures the intensity of
  the heatmap clusters. Fixed value keeps a constant weight value throughout
  all data points. This value should be in the range of 0~1. Similar to
  **Markers**, there is an alternate option in the
  dropdown to automatically scale the weight values depending on data values.
- Radius configures the size of the heatmap
  clusters.
- Blur configures the amount of blur on each
  cluster.
