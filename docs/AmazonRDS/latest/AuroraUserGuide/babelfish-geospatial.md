

# Babelfish supports Geospatial data types
<a name="babelfish-geospatial"></a>

Starting with versions 3.5.0 and 4.1.0, Babelfish includes support for the following two spatial data types:
+ **Geometry data type** – This data type is intended for storing planar or Euclidean (flat-earth) data.
+ **Geography data type** – This data type is intended for storing ellipsoidal or round-earth data, such as GPS latitude and longitude coordinates.

These data types allow for the storage and manipulation of spatial data, but with limitations.

## Understanding the Geospatial data types in Babelfish
<a name="babelfish-geospatial-overview"></a>
+ Geospatial data types are supported in various database objects such as views, procedures, and tables.
+ Supports point data type to store location data as points defined by latitude, longitude, and a valid Spatial Reference System Identifier (SRID). A point may contain Z (elevation), M (measure) values and can be empty.
+ Supports linestring data type (from version 5.4.0) defined by a sequence of points and the line segments connecting them and a valid Spatial Reference System Identifier (SRID). A linestring may contain points with Z (elevation), M (measure) values and can be empty.
+ Supports polygon data type (from version 5.5.0 and 6.0.0). A Polygon is a two-dimensional surface stored as a sequence of points defining an exterior bounding ring and zero or more interior rings.
+ Supports Multipoint data type (from version 5.6.0 and 6.1.0). A MultiPoint is a collection of zero or more points. The boundary of a MultiPoint instance is empty.
+ Applications connecting to Babelfish through drivers like JDBC, ODBC, DOTNET, and PYTHON can utilize this Geospatial feature.

### Geometry data type functions supported in Babelfish
<a name="babelfish-geospatial-overview-geometry"></a>
+ **STGeomFromText ({{geometry\_tagged\_text}}, SRID )** – Creates a geometry instance using Well-Known Text (WKT) representation.
+ **STPointFromText ({{point\_tagged\_text}}, SRID )** – Creates a point instance using WKT representation.
+ **Point ( X, Y, SRID )** – Creates a point instance using float values of x and y coordinates.
+ **<geometry\_instance>.STAsText ( )** – Extracts WKT representation from geometry instance.
+ **<geometry\_instance>.STAsBinary ( )** – Extracts WKB representation from geometry instance.
+ **<geometry\_instance>.STArea ( )** – Calculates the total surface area of geometry instance.
+ **<geometry\_instance>.STSrid ( )** – Extracts the spatial reference identifier (SRID) of the geometry instance.
+ **<geometry\_instance>.STDimension ( )** – Retrieves spatial dimension of geometry instance.
+ **<geometry\_instance>.STIsEmpty ( )** – Checks if the geometry instance is empty.
+ **<geometry\_instance>.STIsClosed ( )** – Checks if the geometry instance is closed.
+ **<geometry\_instance>.STIsValid ( )** – Checks if the geometry instance is valid.
+ **<geometry\_instance>.STDistance (other\_geometry)** – Calculates the distance between two geometry instances.
+ **<geometry\_instance>.STEquals (other\_geometry)** – Checks if the geometry instance represents the same point set as another geometry instance.
+ **<geometry\_instance>.STContains (other\_geometry)** – Checks if the geometry instance contains the other\_geometry instance.
+ **<geometry\_instance>.STDisjoint (other\_geometry)** – Checks if two geometry instances have no points in common.
+ **<geometry\_instance>.STIntersects (other\_geometry)** – Checks if two geometry instances spatially intersect.
+ **<geometry\_instance>.STX** – Extracts the X coordinate (longitude) for geometry instance.
+ **<geometry\_instance>.STY** – Extracts the Y coordinate (latitude) for geometry instance.

Starting with versions 4.7.0 and 5.3.0, Babelfish includes support for the following spatial data functions:
+ **<geometry\_instance>.M** – Extracts the M coordinate of the geometry instance.
+ **<geometry\_instance>.Z** – Extracts the Z coordinate of the geometry instance.
+ **<geometry\_instance>.HasM** – Checks if the geometry instance has atleast one M value.
+ **<geometry\_instance>.HasZ** – Checks if the geometry instance has atleast one Z value.

Starting with versions 5.4.0, Babelfish includes support for the following spatial data function:
+ **STLineFromText ({{linestring\_tagged\_text}}, SRID )** – Creates a linestring instance using WKT representation.

Starting with versions 5.5.0 and 6.0.0, Babelfish includes support for the following spatial data function:
+ **STPolyFromText ({{polygon\_tagged\_text}}, SRID )** – Creates a polygon instance using WKT representation.

Starting with versions 5.6.0 and 6.1.0, Babelfish includes support for the following spatial data functions:
+ **STMPointFromText ({{multipoint\_tagged\_text}}, SRID )** – Creates a multipoint instance using WKT representation.
+ **<geometry\_instance>.STNumPoints** – Returns the sum of the number of points in each of the figures in a geometry instance.
+ **<geometry\_instance>.STGeometryType** – Returns the geometry type name represented by a geometry instance.
+ **<geometry\_instance>.MakeValid()** – Creates a valid representation of a given invalid geometry without losing any of the input vertices.
+ **Parse ({{WKT representation}})** – Creates a geometry instance from a Well-Known Text (WKT) string, assuming SRID 0. Equivalent to STGeomFromText() but without requiring the SRID parameter. Supports optional Z and M values.

### Geography data type functions supported in Babelfish
<a name="babelfish-geospatial-overview-geography"></a>
+ **STGeomFromText ({{geography\_tagged\_text}}, SRID )** – Creates a geography instance using WKT representation.
+ **STPointFromText ({{point\_tagged\_text}}, SRID )** – Creates a point instance using WKT representation.
+ **Point (Lat, Long, SRID)** – Creates a point instance using float values of Latitude and Longitude.
+ **<geography\_instance>.STAsText ( )** – Extracts WKT representation from geography instance.
+ **<geography\_instance>.STAsBinary ( )** – Extracts WKB representation from geography instance.
+ **<geography\_instance>.STArea ( )** – Calculates the total surface area of geography instance.
+ **<geography\_instance>.STSrid ( )** – Extracts the spatial reference identifier (SRID) of the geography instance.
+ **<geography\_instance>.STDimension ( )** – Retrieves spatial dimension of geography instance.
+ **<geography\_instance>.STIsEmpty ( )** – Checks if the geography instance is empty.
+ **<geography\_instance>.STIsClosed ( )** – Checks if the geography instance is closed.
+ **<geography\_instance>.STIsValid( )** – Checks if the geography instance is valid.
+ **<geography\_instance>.STDistance (other\_geography)** – Calculates the distance between two geography instances.
+ **<geography\_instance>.STEquals (other\_geography)** – Checks if the geography instance represents the same point set as another geography instance.
+ **<geography\_instance>.STContains (other\_geography)** – Checks if the geography instance contains the other\_geography instance.
+ **<geography\_instance>.STDisjoint (other\_geography)** – Checks if two geography instances have no points in common.
+ **<geography\_instance>.STIntersects (other\_geography)** – Checks if two geography instances spatially intersect.
+ **<geography\_instance>.Lat** – Extracts the Latitude value for geography instance.
+ **<geography\_instance>.Long** – Extracts the Longitude value for geography instance.

Starting with versions 4.7.0 and 5.3.0, Babelfish includes support for the following spatial data functions:
+ **<geography\_instance>.M** – Extracts the M coordinate of the geography instance.
+ **<geography\_instance>.Z** – Extracts the Z coordinate of the geography instance.
+ **<geography\_instance>.HasM** – Checks if the geography instance has atleast one M value.
+ **<geography\_instance>.HasZ** – Checks if the geography instance has atleast one Z value.

Starting with versions 5.4.0, Babelfish includes support for the following spatial data function:
+ **STLineFromText ({{linestring\_tagged\_text}}, SRID )** – Creates a linestring instance using WKT representation.

Starting with versions 5.5.0 and 6.0.0, Babelfish includes support for the following spatial data function:
+ **STPolyFromText ({{polygon\_tagged\_text}}, SRID )** – Creates a polygon instance using WKT representation.

Starting with versions 5.6.0 and 6.1.0, Babelfish includes support for the following spatial data functions:
+ **STMPointFromText ({{multipoint\_tagged\_text}}, SRID )** – Creates a multipoint instance using WKT representation.
+ **<geography\_instance>.STNumPoints** – Returns the sum of the number of points in each of the figures in a geography instance.
+ **<geography\_instance>.STGeometryType** – Returns the geography type name represented by a geography instance.
+ **<geography\_instance>.MakeValid()** – Creates a valid representation of a given invalid geography without losing any of the input vertices.
+ **Parse ({{WKT representation}})** – Creates a geography instance from a Well-Known Text (WKT) string, assuming SRID 4326. Equivalent to STGeomFromText() but without requiring the SRID parameter. Supports optional Z and M values.

## Limitations in Babelfish for Geospatial data types
<a name="babelfish-geospatial-limitations"></a>
+ Geometry and Geography types other than point, linestring, polygon and multipoint instances aren't currently supported:
  + CircularString
  + CompoundCurve
  + CurvePolygon
  + MultiLineString
  + MultiPolygon
  + GeometryCollection
+ Currently, spatial indexing isn't supported for Geospatial data types.
+ Only the listed functions are currently supported for these data types. For more information, see [Geometry data type functions supported in Babelfish](#babelfish-geospatial-overview-geometry) and [Geography data type functions supported in Babelfish](#babelfish-geospatial-overview-geography).
+ STDistance function output for Geography data might have minor precision variations compared to T-SQL. This is due to the underlying PostGIS implementation. For more information, see [ST\_Distance](https://postgis.net/docs/ST_Distance.html)
+ STIsValid function output for both Geometry and Geography data might have some deviations compared to T-SQL. Due to this, the functions - STDistance, STContains, STInstersects, STDisjoint, STDimension, STArea, STEquals may also deviate from T-SQL for some cases ( returns output instead of throwing error ). This is due to the underlying PostGIS implementation. For more information, see [ST\_IsValid](https://postgis.net/docs/ST_IsValid.html).
+ For optimal performance, use built-in Geospatial data types, without creating additional layers of abstraction in Babelfish.
+ In Babelfish, Geospatial function names are used as keywords and will perform spatial operations only if used in the intended way.