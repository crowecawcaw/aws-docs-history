Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_ContainsProperly

ST_ContainsProperly returns true if both input geometries are nonempty, and all
points of the 2D projection of the second geometry are interior points of the 2D projection of the first geometry.

## Syntax

```
ST_ContainsProperly(*geom1*, *geom2*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The subtype can't be `GEOMETRYCOLLECTION`.

_geom2_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The subtype can't be `GEOMETRYCOLLECTION`.
This value is compared with _geom1_ to determine if all its points are interior points of _geom1_.

## Return type

`BOOLEAN`

If _geom1_ or _geom2_ is null, then null is returned.

If _geom1_ and _geom2_ don't have the same
value for the spatial reference system identifier (SRID), then an error is returned.

If _geom1_ or _geom2_ is a geometry collection, then an error is returned.

## Examples

The following SQL returns the values of ST_Contains and ST_ContainsProperly where
the input linestring intersects the interior and the boundary of the input polygon (but
not its exterior). The polygon contains the linestring but doesn't properly contain
the linestring.

```
WITH tmp(g1, g2)
AS (SELECT ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0))'), ST_GeomFromText('LINESTRING(5 5,10 5,10 6,5 5)')) SELECT ST_Contains(g1, g2), ST_ContainsProperly(g1, g2)
FROM tmp;
```

```

 st_contains | st_containsproperly
-------------+---------------------
 t           | f

```
