Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_InteriorRingN

ST_InteriorRingN returns a closed linestring corresponding to the interior ring of an input polygon at the index position.
The dimension of the returned geometry is the same as that of the input geometry.

## Syntax

```
ST_InteriorRingN(*geom*, *index*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

_index_

A value of data type `INTEGER` that represents the position of
a ring of a one-based index.

## Return type

`GEOMETRY` of subtype `LINESTRING`.

The spatial reference system identifier (SRID) value of the returned geometry is
the SRID value of the input geometry.

If _geom_ or _index_ is null, then null is returned.

If _index_ is out of range, then null is returned.

If _geom_ is not a polygon, then null is returned.

If _geom_ is an empty polygon, then null is returned.

## Examples

The following SQL returns the second ring of the polygon as a closed linestring.

```
SELECT ST_AsEWKT(ST_InteriorRingN(ST_GeomFromText('POLYGON((7 9,8 7,11 6,15 8,16 6,17 7,17 10,18 12,17 14,15 15,11 15,10 13,9 12,7 9),(9 9,10 10,11 11,11 10,10 8,9 9),(12 14,15 14,13 11,12 14))'),2));
```

```

st_asewkt
-----------
 LINESTRING(12 14,15 14,13 11,12 14)

```
