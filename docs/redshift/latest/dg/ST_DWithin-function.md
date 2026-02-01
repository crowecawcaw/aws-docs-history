Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_DWithin

ST_DWithin returns true if the Euclidean distance between the 2D projections of the two input geometry values is not larger than a threshold value.

## Syntax

```
ST_DWithin(*geom1*, *geom2*, *threshold*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

_geom2_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

_threshold_

A value of data type `DOUBLE PRECISION`. This value is in the
units of the input arguments.

## Return type

`BOOLEAN`

If _geom1_ or _geom2_ is null, then null is returned.

If _threshold_ is negative, then an error is returned.

If _geom1_ and _geom2_ don't have the same
value for the spatial reference system identifier (SRID), then an error is returned.

If _geom1_ or _geom2_ is a geometry collection, then an error is returned.

## Examples

The following SQL checks if the distance between two polygons is within five
units.

```
SELECT ST_DWithin(ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'), ST_GeomFromText('POLYGON((-1 3,2 1,0 -3,-1 3))'),5);
```

```

st_dwithin
-----------
 true

```
