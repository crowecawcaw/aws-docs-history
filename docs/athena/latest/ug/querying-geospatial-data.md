# Query geospatial data

Geospatial data contains identifiers that specify a geographic position for an object. Examples of this type of data include weather reports, map directions, tweets with geographic positions, store locations, and airline routes. Geospatial data plays an important role in business analytics, reporting, and forecasting.

Geospatial identifiers, such as latitude and longitude, allow you to convert any mailing address into a set of geographic coordinates.

## What is a geospatial query?

Geospatial queries are specialized types of SQL queries supported in Athena. They differ from non-spatial SQL queries in the following ways:

- Using the following specialized geometry data types: `point`, `line`, `multiline`, `polygon`, and `multipolygon`.
- Expressing relationships between geometry data types, such as `distance`, `equals`, `crosses`, `touches`, `overlaps`, `disjoint`, and others.

Using geospatial queries in Athena, you can run these and other similar operations:

- Find the distance between two points.
- Check whether one area (polygon) contains another.
- Check whether one line crosses or touches another line or polygon.

For example, to obtain a `point` geometry data type from values of type
`double` for the geographic coordinates of Mount Rainier in Athena, use the
`ST_Point (longitude, latitude)` geospatial function, as in the following
example.

```
ST_Point(-121.7602, 46.8527)
```

## Input data formats

and geometry data types

To use geospatial functions in Athena, input your data in the WKT format, or use the Hive
JSON SerDe. You can also use the geometry data types supported in Athena.

### Input data formats

To handle geospatial queries, Athena supports input data in these data formats:

- **WKT (Well-known Text)**. In Athena, WKT is
  represented as a `varchar(x)` or `string` data
  type.
- **JSON-encoded geospatial data**. To parse JSON
  files with geospatial data and create tables for them, Athena uses the [Hive JSON SerDe](https://github.com/Esri/spatial-framework-for-hadoop/wiki/Hive-JSON-SerDe "https://github.com/Esri/spatial-framework-for-hadoop/wiki/Hive-JSON-SerDe"). For more information about using this SerDe in
  Athena, see [JSON SerDe libraries](json-serde.md "json-serde.md").

### Geometry data types

To handle geospatial queries, Athena supports these specialized geometry data
types:

- `point`
- `line`
- `polygon`
- `multiline`
- `multipolygon`

## Supported geospatial functions

For information about the geospatial functions in Athena engine version 3, see [Geospatial
functions](https://trino.io/docs/current/functions/geospatial.html "https://trino.io/docs/current/functions/geospatial.html") in the Trino documentation.
