Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_AddPoint

ST_AddPoint returns a linestring geometry that is the same as the input geometry with a point added.
If an index is provided, then the point is added at the index position.
If the index is -1 or not provided, then the point is appended to the linestring.

The index is zero-based. The spatial reference system identifier (SRID) of the result
is the same as that of the input geometry.

The dimension of the returned geometry is the same as that of the
_geom1_ value. If _geom1_ and
_geom2_ have different dimensions, _geom2_ is
projected to the dimension of _geom1_.

## Syntax

```
ST_AddPoint(*geom1*, *geom2*)
```

```
ST_AddPoint(*geom1*, *geom2*, *index*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The subtype must be
`LINESTRING`.

_geom2_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The subtype must be
`POINT`. The point can be the empty point.

_index_

A value of data type `INTEGER` that represents the position of a zero-based index.

## Return type

`GEOMETRY`

If _geom1_, _geom2_, or _index_ is null, then null is returned.

If _geom2_ is the empty point, then a copy of _geom1_ is returned.

If _geom1_ is not a `LINESTRING`, then an error is returned.

If _geom2_ is not a `POINT`, then an error is returned.

If _index_ is out of range, then an error is returned. Valid
values for the index position are -1 or a value between 0 and
`ST_NumPoints(geom1)`.

## Examples

The following SQL adds a point to a linestring to make it a closed linestring.

```
WITH tmp(g) AS (SELECT ST_GeomFromText('LINESTRING(0 0,10 0,10 10,5 5,0 5)',4326))
SELECT ST_AsEWKT(ST_AddPoint(g, ST_StartPoint(g))) FROM tmp;
```

```

 st_asewkt
------------------------------------------------
 SRID=4326;LINESTRING(0 0,10 0,10 10,5 5,0 5,0 0)

```

The following SQL adds a point to a specific position in a linestring.

```
WITH tmp(g) AS (SELECT ST_GeomFromText('LINESTRING(0 0,10 0,10 10,5 5,0 5)',4326))
SELECT ST_AsEWKT(ST_AddPoint(g, ST_SetSRID(ST_Point(5, 10), 4326), 3)) FROM tmp;
```

```

 st_asewkt
------------------------------------------------
 SRID=4326;LINESTRING(0 0,10 0,10 10,5 10,5 5,0 5)

```
