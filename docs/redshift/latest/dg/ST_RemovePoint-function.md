Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_RemovePoint

ST_RemovePoint returns a linestring geometry that has the point of the input geometry at an index position removed.

The index is zero-based. The spatial reference system identifier (SRID) of the result is the same as the input geometry.
The dimension of the returned geometry is the same as that of the input geometry.

## Syntax

```
ST_RemovePoint(*geom*, *index*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The subtype must be
`LINESTRING`.

_index_

A value of data type `INTEGER` that represents the position of a zero-based index.

## Return type

`GEOMETRY`

If _geom_ or _index_ is null, then null is returned.

If _geom_ is not subtype `LINESTRING`, then an error is returned.

If _index_ is out of range, then an error is returned. Valid
values for the index position are between 0 and `ST_NumPoints(geom)` minus 1.

## Examples

The following SQL removes the last point in a linestring.

```
WITH tmp(g) AS (SELECT ST_GeomFromText('LINESTRING(0 0,10 0,10 10,5 5,0 5)',4326))
SELECT ST_AsEWKT(ST_RemovePoint(g, ST_NumPoints(g) - 1)) FROM tmp;
```

```

   st_asewkt
-----------------------------------------
 SRID=4326;LINESTRING(0 0,10 0,10 10,5 5)

```
