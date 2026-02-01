Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Crosses

ST_Crosses returns true if the 2D projections of the two input geometries cross each other.

## Syntax

```
ST_Crosses(*geom1*, *geom2*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

_geom2_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`BOOLEAN`

If _geom1_ or _geom2_ is null, then an error is returned.

If _geom1_ or _geom2_ is a geometry collection, then an error is returned.

If _geom1_ and _geom2_ don't have the same
value for the spatial reference system identifier (SRID), then an error is returned.

## Examples

The following SQL checks if the first polygon crosses the second multipoint. In
this example, the multipoint intersects both the interior and exterior of the polygon,
which is why ST_Crosses returns true.

```
SELECT ST_Crosses (ST_GeomFromText('polygon((0 0,10 0,10 10,0 10,0 0))'), ST_GeomFromText('multipoint(5 5,0 0,-1 -1)'));
```

```

st_crosses
-------------
 true

```

The following SQL checks if the first polygon crosses the second multipoint. In
this example, the multipoint intersects the exterior of the polygon but not its
interior, which is why ST_Crosses returns false.

```
SELECT ST_Crosses (ST_GeomFromText('polygon((0 0,10 0,10 10,0 10,0 0))'), ST_GeomFromText('multipoint(0 0,-1 -1)'));
```

```

st_crosses
-------------
 false

```
