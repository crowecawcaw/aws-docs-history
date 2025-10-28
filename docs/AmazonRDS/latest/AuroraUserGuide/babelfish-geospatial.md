# Babelfish supports Geospatial data types

Starting with versions 3.5.0 and 4.1.0, Babelfish includes support for the following two spatial data types:

- Geometry data type – This data type is intended for storing planar or Euclidean (flat-earth) data.
- Geography data type – This data type is intended for storing ellipsoidal or round-earth data, such as GPS latitude and longitude coordinates.
  These data types allow for the storage and manipulation of spatial data, but with limitations.

## Understanding the Geospatial data types in Babelfish

- Geospatial data types are supported in various database objects such as views, procedures, and tables.

- Supports 2-D point data type to store location data as points defined by latitude, longitude, and a valid Spatial Reference System Identifier (SRID).
- Applications connecting to Babelfish through drivers like JDBC, ODBC, DOTNET, and PYTHON can utilize this Geospatial feature.

### Geometry data type functions supported in Babelfish

- STGeomFromText (`geometry_tagged_text`, SRID ) –
  Creates a geometry instance using Well-Known Text (WKT) representation.
- STPointFromText (`point_tagged_text`, SRID ) –
  Creates a point instance using WKT representation.
- Point ( X, Y, SRID ) –
  Creates a point instance using float values of x and y coordinates.
- <geometry_instance>.STAsText ( ) –
  Extracts WKT representation from geometry instance.
- <geometry_instance>.STDistance (other_geometry) –
  Calculates the distance between two geometry instances.
- <geometry_instance>.STX –
  Extracts the X coordinate (longitude) for geometry instance.
- <geometry_instance>.STY –
  Extracts the Y coordinate (latitude) for geometry instance.

### Geography data type functions supported in Babelfish

- STGeomFromText (`geography_tagged_text`, SRID ) –
  Creates a geography instance using WKT representation.
- STPointFromText (`point_tagged_text`, SRID ) –
  Creates a point instance using WKT representation.
- Point (Lat, Long, SRID) –
  Creates a point instance using float values of Latitude and Longitude.
- <geography_instance>.STAsText ( ) –
  Extracts WKT representation from geography instance.
- <geography_instance>.STDistance (other_geography) –
  Calculates the distance between two geography instances.
- <geography_instance>.Lat –
  Extracts the Latitude value for geography instance.
- <geography_instance>.Long –
  Extracts the Longitude value for geography instance.

## Limitations in Babelfish for Geospatial data types

- Currently, Babelfish doesn't support more advanced features like Z-M flags for point instances of Geospatial data types.
- Geometry types other than point instance aren't currently supported:
  - LineString
  - CircularString
  - CompoundCurve
  - Polygon
  - CurvePolygon
  - MultiPoint
  - MultiLineString
  - MultiPolygon
  - GeometryCollection

- Currently, spatial indexing isn't supported for Geospatial data types.
- Only the listed functions are currently supported for these data types. For more information, see
  [Geometry data type functions supported in Babelfish](#babelfish-geospatial-overview-geometry "#babelfish-geospatial-overview-geometry") and
  [Geography data type functions supported in Babelfish](#babelfish-geospatial-overview-geography "#babelfish-geospatial-overview-geography").
- STDistance function output for Geography data might have minor precision variations compared to T-SQL.
  This is due to the underlying PostGIS implementation.
  For more information, see [ST_Distance](https://postgis.net/docs/ST_Distance.html "https://postgis.net/docs/ST_Distance.html")
- For optimal performance, use built-in Geospatial data types, without creating additional layers of abstraction in Babelfish.

###### Tip

While you can create custom data types, it's not recommended to create it on top of Geospatial data. This could introduce complexities,
potentially leading to unexpected behavior due to the limited support.

- In Babelfish, Geospatial function names are used as keywords and will perform spatial operations only if used in the intended way.

###### Tip

When creating user-defined functions and procedures in Babelfish, avoid using the same names as built-in Geospatial functions.
If you have any existing database objects with the same names, use `sp_rename` to rename them.
