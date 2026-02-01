Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_ZMax

ST_ZMax returns the maximum `z` coordinate of an input geometry.

## Syntax

```
ST_ZMax(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`DOUBLE PRECISION` value of the maximum `z` coordinate.

If _geom_ is empty, then null is returned.

If _geom_ is null, then null is returned.

If _geom_ is a 2D or 3DM geometry, then null is returned.

## Examples

The following SQL returns the largest `z` coordinate of a linestring in a 3DZ geometry.

```
SELECT ST_ZMax(ST_GeomFromEWKT('LINESTRING Z (0 1 2, 3 4 5, 6 7 8)'));
```

```

st_zmax
-----------
  8

```

The following SQL returns the largest `z` coordinate of a linestring in a 4D geometry.

```
SELECT ST_ZMax(ST_GeomFromEWKT('LINESTRING ZM (0 1 2 3, 4 5 6 7, 8 9 10 11)'));
```

```

st_zmax
-----------
  10

```
