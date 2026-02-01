Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Simplify

ST_Simplify returns a simplified copy of the input geometry using the Ramer-Douglas-Peucker algorithm with the given tolerance.
The topology of the input geometry might not be preserved.
For more information about the algorithm, see [Ramer–Douglas–Peucker algorithm](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm "https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm") in Wikipedia.

When ST_Simplify calculates distances to simplify a geometry, ST_Simplify operates on the 2D projection of the input geometry.

## Syntax

```
ST_Simplify(*geom*, *tolerance*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

_tolerance_

A value of data type `DOUBLE PRECISION` that represents the tolerance level of the Ramer-Douglas-Peucker algorithm.
If _tolerance_ is a negative number, then zero is used.

## Return type

`GEOMETRY`.

The spatial reference system identifier (SRID) value of the returned geometry is
the SRID value of the input geometry.

The dimension of the returned geometry is
the same as that of the input geometry.

If _geom_ is null, then null is returned.

## Examples

The following SQL simplifies the input linestring using a Euclidean distance
tolerance of 1 with the Ramer-Douglas-Peucker algorithm. The units of the distance are
the same as those of the coordinates of the geometry.

```
SELECT ST_AsEWKT(ST_Simplify(ST_GeomFromText('LINESTRING(0 0,1 2,1 1,2 2,2 1)'), 1));
```

```

 st_asewkt
-----------
LINESTRING(0 0,1 2,2 1)

```
