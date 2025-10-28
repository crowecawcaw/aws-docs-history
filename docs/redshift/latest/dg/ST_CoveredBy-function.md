Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_CoveredBy

ST_CoveredBy returns true if the 2D projection of the first input geometry is covered by the 2D projection of the second input
geometry. Geometry `A` is covered by geometry `B` if both are
nonempty and every point in `A` is a point in `B`.

ST_CoveredBy(`A`, `B`) is equivalent to ST_Covers(`B`, `A`).

## Syntax

```
ST_CoveredBy(*geom1*, *geom2*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. This value is compared with
_geom2_ to determine if it's covered by
_geom2_.

_geom2_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`BOOLEAN`

If _geom1_ or _geom2_ is null, then null is returned.

If _geom1_ and _geom2_ don't have the same
value for the spatial reference system identifier (SRID), then an error is returned.

If _geom1_ or _geom2_ is a geometry collection, then an error is returned.

## Examples

The following SQL checks if the first polygon is covered by the second polygon.

```
SELECT ST_CoveredBy(ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'), ST_GeomFromText('POLYGON((-1 3,2 1,0 -3,-1 3))'));
```

```

st_coveredby
-----------
 true

```
