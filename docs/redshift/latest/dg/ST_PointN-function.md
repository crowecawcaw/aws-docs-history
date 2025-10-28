Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_PointN

ST_PointN returns a point in a linestring as specified by an index value. Negative
index values are counted backward from the end of the linestring, so that -1 is the last
point.

The dimension of the returned geometry is the same as that of the input geometry.

## Syntax

```
ST_PointN(*geom*, *index*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The subtype must be
`LINESTRING`.

_index_

A value of data type `INTEGER` that represents the index of a point in a linestring.

## Return type

`GEOMETRY` of subtype `POINT`.

The spatial reference system identifier (SRID) value of the returned geometry is
set to 0.

If _geom_ or _index_ is null, then null is returned.

If _index_ is out of range, then null is returned.

If _geom_ is empty, then null is returned.

If _geom_ is not a `LINESTRING`, then null is returned.

## Examples

The following SQL returns an extended well-known text (EWKT) representation of a six-point
`LINESTRING` to a `GEOMETRY` object and returns the point at index 5 of the linestring.

```
SELECT ST_AsEWKT(ST_PointN(ST_GeomFromText('LINESTRING(0 0,10 0,10 10,5 5,0 5,0 0)',4326), 5));
```

```

st_asewkt
-------------
 SRID=4326;POINT(0 5)

```
