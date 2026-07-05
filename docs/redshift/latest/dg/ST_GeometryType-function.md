Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_GeometryType

ST\_GeometryType returns the subtype of an input geometry as a string.

For 3DM, 3DZ, and 4D geometry inputs, ST\_GeometryType returns the same result as for 2D geometry inputs.

## Syntax

```
ST_GeometryType(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`VARCHAR` representing the subtype of _geom_.

If _geom_ is null, then null is returned.

The values returned are as follows.

| Returned string value   | Geometry subtype                                         |
| ----------------------- | -------------------------------------------------------- |
| `ST_Point`              | Returned if *geom<br>• is a `POINT` subtype              |
| `ST_LineString`         | Returned if *geom<br>• is a `LINESTRING` subtype         |
| `ST_Polygon`            | Returned if *geom<br>• is a `POLYGON` subtype            |
| `ST_MultiPoint`         | Returned if *geom<br>• is a `MULTIPOINT` subtype         |
| `ST_MultiLineString`    | Returned if *geom<br>• is a `MULTILINESTRING` subtype    |
| `ST_MultiPolygon`       | Returned if *geom<br>• is a `MULTIPOLYGON` subtype       |
| `ST_GeometryCollection` | Returned if *geom<br>• is a `GEOMETRYCOLLECTION` subtype |

## Examples

The following SQL returns the subtype of the input linestring geometry.

```
SELECT ST_GeometryType(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'));
```

```

st_geometrytype
-------------
 ST_LineString

```
