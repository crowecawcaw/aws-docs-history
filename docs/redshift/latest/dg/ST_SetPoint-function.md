Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_SetPoint

ST_SetPoint returns a linestring with updated coordinates with respect to the input linestring's position as specified by the index.
The new coordinates are the coordinates of the input point.

The dimension of the returned geometry is the same as that of the
_geom1_ value. If _geom1_ and
_geom2_ have different dimensions, _geom2_ is
projected to the dimension of _geom1_.

## Syntax

```
ST_SetPoint(*geom1*, *index*, *geom2*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The subtype must be `LINESTRING`.

_index_

A value of data type `INTEGER` that represents the position of an index.
A `0` refers to the first point of the linestring from the left,
`1` refers to the second point, and so on.
The index can be a negative value.
A `-1` refers to the first point of the linestring from the right,
`-2` refers to the second point of the linestring from the right, and so on.

_geom2_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The subtype must be `POINT`.

## Return type

`GEOMETRY`

If _geom2_ is the empty point, then _geom1_ is returned.

If _geom1_, _geom2_, or _index_ is null, then null is returned.

If _geom1_ is not a linestring, then an error is returned.

If _index_ is not within a valid index range, then an error is returned.

If _geom2_ is not a point, then an error is returned.

If _geom1_ and _geom2_ don't have the same
value for the spatial reference system identifier (SRID), then an error is returned.

## Examples

The following SQL returns a new linestring where we set the second point of the input linestring with the specified point.

```
SELECT ST_AsText(ST_SetPoint(ST_GeomFromText('LINESTRING(1 2, 3 2, 5 2, 1 2)'), 2, ST_GeomFromText('POINT(7 9)')));
```

```

st_astext
-------------
 LINESTRING(1 2,3 2,7 9,1 2)

```

The following SQL example returns a new linestring where we set the third point
from the right (the index is negative) of the linestring with the specified point.

```
SELECT ST_AsText(ST_SetPoint(ST_GeomFromText('LINESTRING(1 2, 3 2, 5 2, 1 2)'), -3, ST_GeomFromText('POINT(7 9)')));
```

```

st_astext
-------------
 LINESTRING(1 2,7 9,5 2,1 2)

```
