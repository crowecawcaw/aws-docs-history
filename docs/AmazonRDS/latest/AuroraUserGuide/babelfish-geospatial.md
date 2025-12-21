# Babelfish supports Geospatial data types

Starting with versions 3.5.0 and 4.1.0, Babelfish includes support for the following two spatial data types:

- Geometry data type – This data type is intended for storing planar or Euclidean (flat-earth) data.
- Geography data type – This data type is intended for storing ellipsoidal or round-earth data, such as GPS latitude and longitude coordinates.
  These data types allow for the storage and manipulation of spatial data, but with limitations.

## Understanding the Geospatial data types in Babelfish

- Geospatial data types are supported in various database objects such as views, procedures, and tables.
- Supports point data type to store location data as points defined by latitude, longitude, and a valid Spatial Reference System Identifier (SRID). A point may contain Z (elevation), M (measure) values and can be empty.
- Supports linestring data type (from version 5.4.0) defined by a sequence of points and the line segments connecting them and a valid Spatial Reference System Identifier (SRID). A linestring may contain points with Z (elevation), M (measure) values and can be empty.
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
- <geometry_instance>.STAsBinary ( ) –
  Extracts WKB representation from geometry instance.
- <geometry_instance>.STArea ( ) –
  Calculates the total surface area of geometry instance.
- <geometry_instance>.STSrid ( ) –
  Extracts the spatial reference identifier (SRID) of the geometry instance.
- <geometry_instance>.STDimension ( ) –
  Retrieves spatial dimension of geometry instance.
- <geometry_instance>.STIsEmpty ( ) –
  Checks if the geometry instance is empty.
- <geometry_instance>.STIsClosed ( ) –
  Checks if the geometry instance is closed.
- <geometry_instance>.STIsValid ( ) –
  Checks if the geometry instance is valid.
- <geometry_instance>.STDistance (other_geometry) –
  Calculates the distance between two geometry instances.
- <geometry_instance>.STEquals (other_geometry) –
  Checks if the geometry instance represents the same point set as another geometry instance.
- <geometry_instance>.STContains (other_geometry) –
  Checks if the geometry instance contains the other_geometry instance.
- <geometry_instance>.STDisjoint (other_geometry) –
  Checks if two geometry instances have no points in common.
- <geometry_instance>.STIntersects (other_geometry) –
  Checks if two geometry instances spatially intersect.
- <geometry_instance>.STX –
  Extracts the X coordinate (longitude) for geometry instance.
- <geometry_instance>.STY –
  Extracts the Y coordinate (latitude) for geometry instance.

Starting with versions 4.7.0 and 5.3.0, Babelfish includes support for the following spatial data functions:

- <geometry_instance>.M –
  Extracts the M coordinate of the geometry instance.
- <geometry_instance>.Z –
  Extracts the Z coordinate of the geometry instance.
- <geometry_instance>.HasM –
  Checks if the geometry instance has atleast one M value.
- <geometry_instance>.HasZ –
  Checks if the geometry instance has atleast one Z value.

Starting with versions 5.4.0, Babelfish includes support for the following spatial data function:

- STLineFromText (`linestring_tagged_text`, SRID ) –
  Creates a linestring instance using WKT representation.

### Geography data type functions supported in Babelfish

- STGeomFromText (`geography_tagged_text`, SRID ) –
  Creates a geography instance using WKT representation.
- STPointFromText (`point_tagged_text`, SRID ) –
  Creates a point instance using WKT representation.
- Point (Lat, Long, SRID) –
  Creates a point instance using float values of Latitude and Longitude.
- <geography_instance>.STAsText ( ) –
  Extracts WKT representation from geography instance.
- <geography_instance>.STAsBinary ( ) –
  Extracts WKB representation from geography instance.
- <geography_instance>.STArea ( ) –
  Calculates the total surface area of geography instance.
- <geography_instance>.STSrid ( ) –
  Extracts the spatial reference identifier (SRID) of the geography instance.
- <geography_instance>.STDimension ( ) –
  Retrieves spatial dimension of geography instance.
- <geography_instance>.STIsEmpty ( ) –
  Checks if the geography instance is empty.
- <geography_instance>.STIsClosed ( ) –
  Checks if the geography instance is closed.
- <geography_instance>.STIsValid( ) –
  Checks if the geography instance is valid.
- <geography_instance>.STDistance (other_geography) –
  Calculates the distance between two geography instances.
- <geography_instance>.STEquals (other_geography) –
  Checks if the geography instance represents the same point set as another geography instance.
- <geography_instance>.STContains (other_geography) –
  Checks if the geography instance contains the other_geography instance.
- <geography_instance>.STDisjoint (other_geography) –
  Checks if two geography instances have no points in common.
- <geography_instance>.STIntersects (other_geography) –
  Checks if two geography instances spatially intersect.
- <geography_instance>.Lat –
  Extracts the Latitude value for geography instance.
- <geography_instance>.Long –
  Extracts the Longitude value for geography instance.

Starting with versions 4.7.0 and 5.3.0, Babelfish includes support for the following spatial data functions:

- <geography_instance>.M –
  Extracts the M coordinate of the geography instance.
- <geography_instance>.Z –
  Extracts the Z coordinate of the geography instance.
- <geography_instance>.HasM –
  Checks if the geography instance has atleast one M value.
- <geography_instance>.HasZ –
  Checks if the geography instance has atleast one Z value.

Starting with versions 5.4.0, Babelfish includes support for the following spatial data function:

- STLineFromText (`linestring_tagged_text`, SRID ) –
  Creates a linestring instance using WKT representation.

## Limitations in Babelfish for Geospatial data types

- Geometry and Geography types other than point and linestring instances aren't currently supported:
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
- STIsValid function output for both Geometry and Geography data might have some deviations compared to T-SQL.
  Due to this, the functions - STDistance, STContains, STInstersects, STDisjoint, STDimension, STArea, STEquals may also deviate from T-SQL for some cases ( returns output instead of throwing error ).
  This is due to the underlying PostGIS implementation.
  For more information, see [ST_IsValid](https://postgis.net/docs/ST_IsValid.html "https://postgis.net/docs/ST_IsValid.html").
- For optimal performance, use built-in Geospatial data types, without creating additional layers of abstraction in Babelfish.
- In Babelfish, Geospatial function names are used as keywords and will perform spatial operations only if used in the intended way.
