Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# GeometryType

GeometryType returns the subtype of an input geometry as a string.

## Syntax

```
GeometryType(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

## Return type

`VARCHAR` representing the subtype of _geom_.

If _geom_ is null, then null is returned.

The values returned are as follows.

| Returned string value for 2D, 3DZ, 4D geometries | Returned string value for 3DM geometries | Geometry subtype                                          |
| ------------------------------------------------ | ---------------------------------------- | --------------------------------------------------------- |
| `POINT`                                          | `POINTM`                                 | Returned if \*geom<br>• is a `POINT` subtype              |
| `LINESTRING`                                     | `LINESTRINGM`                            | Returned if \*geom<br>• is a `LINESTRING` subtype         |
| `POLYGON`                                        | `POLYGONM`                               | Returned if \*geom<br>• is a `POLYGON` subtype            |
| `MULTIPOINT`                                     | `MULTIPOINTM`                            | Returned if \*geom<br>• is a `MULTIPOINT` subtype         |
| `MULTILINESTRING`                                | `MULTILINESTRINGM`                       | Returned if \*geom<br>• is a `MULTILINESTRING` subtype    |
| `MULTIPOLYGON`                                   | `MULTIPOLYGONM`                          | Returned if \*geom<br>• is a `MULTIPOLYGON` subtype       |
| `GEOMETRYCOLLECTION`                             | `GEOMETRYCOLLECTIONM`                    | Returned if \*geom<br>• is a `GEOMETRYCOLLECTION` subtype |

## Examples

The following SQL converts a well-known text (WKT) representation of a polygon and
returns the `GEOMETRY` subtype as a string.

```
SELECT GeometryType(ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'));
```

```

geometrytype
-------------
 POLYGON

```
