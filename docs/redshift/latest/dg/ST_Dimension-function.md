Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Dimension

ST_Dimension returns the inherent dimension of an input geometry. The _inherent dimension_ is the dimension value of the subtype that
is defined in the geometry.

For 3DM, 3DZ, and 4D geometry inputs, ST_Dimension returns the same result as for 2D geometry inputs.

## Syntax

```
ST_Dimension(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`INTEGER` representing the inherent dimension of _geom_.

If _geom_ is null, then null is returned.

The values returned are as follows.

| Returned value                                        | Geometry subtype                                                           |
| ----------------------------------------------------- | -------------------------------------------------------------------------- |
| 0                                                     | Returned if \*geom<br>• is a `POINT` or `MULTIPOINT`<br>subtype            |
| 1                                                     | Returned if \*geom<br>• is a `LINESTRING` or<br>`MULTILINESTRING` subtype. |
| 2                                                     | Returned if \*geom<br>• is a `POLYGON` or `MULTIPOLYGON`<br>subtype        |
| 0                                                     | Returned if \*geom<br>• is an empty `GEOMETRYCOLLECTION`<br>subtype        |
| Largest dimension of the components of the collection | Returned if \*geom<br>• is a `GEOMETRYCOLLECTION` subtype                  |

## Examples

The following SQL converts a well-known text (WKT) representation of a four-point
LINESTRING to a GEOMETRY object and returns the dimension of the linestring.

```
SELECT ST_Dimension(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'));
```

```

st_dimension
-------------
1

```
