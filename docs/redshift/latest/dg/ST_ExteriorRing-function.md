Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_ExteriorRing

ST_ExteriorRing returns a closed linestring that represents the exterior ring of an input polygon.
The dimension of the returned geometry is the same as that of the input geometry.

## Syntax

```
ST_ExteriorRing(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY` of subtype `LINESTRING`.

The spatial reference system identifier (SRID) value of the returned geometry is
the SRID value of the input geometry.

If _geom_ is null, then null is returned.

If _geom_ is not a polygon, then null is returned.

If _geom_ is empty, then an empty polygon is returned.

## Examples

The following SQL returns the exterior ring of a polygon as a closed linestring.

```
SELECT ST_AsEWKT(ST_ExteriorRing(ST_GeomFromText('POLYGON((7 9,8 7,11 6,15 8,16 6,17 7,17 10,18 12,17 14,15 15,11 15,10 13,9 12,7 9),(9 9,10 10,11 11,11 10,10 8,9 9),(12 14,15 14,13 11,12 14))')));
```

```

st_asewkt
-----------
 LINESTRING(7 9,8 7,11 6,15 8,16 6,17 7,17 10,18 12,17 14,15 15,11 15,10 13,9 12,7 9)

```
