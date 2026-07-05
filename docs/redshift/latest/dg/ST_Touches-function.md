Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_Touches

ST\_Touches returns true if the 2D projections of the two input geometries touch. The two geometries touch
if they are nonempty, intersect, and have no interior points in common.

## Syntax

```
ST_Touches(*geom1*, *geom2*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

_geom2_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`BOOLEAN`

If _geom1_ or _geom2_ is null, then null is returned.

If _geom1_ and _geom2_ don't have the
same value for the spatial reference system identifier (SRID), then an error is
returned.

If _geom1_ or _geom2_ is a geometry collection, then an error is returned.

## Examples

The following SQL checks if a polygon touches a linestring.

```
SELECT ST_Touches(ST_GeomFromText('POLYGON((0 0,10 0,0 10,0 0))'), ST_GeomFromText('LINESTRING(20 10,20 0,10 0)'));
```

```

 st_touches
-------------
 t

```
