Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_MMax

ST\_MMax returns the maximum `m` coordinate of an input geometry.

## Syntax

```
ST_MMax(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`DOUBLE PRECISION` value of the maximum `m` coordinate.

If _geom_ is empty, then null is returned.

If _geom_ is null, then null is returned.

If _geom_ is a 2D or 3DZ geometry, then null is returned.

## Examples

The following SQL returns the largest `m` coordinate of a linestring in a 3DM geometry.

```
SELECT ST_MMax(ST_GeomFromEWKT('LINESTRING M (0 1 2, 3 4 5, 6 7 8)'));
```

```

st_mmax
-----------
  8

```

The following SQL returns the largest `m` coordinate of a linestring in a 4D geometry.

```
SELECT ST_MMax(ST_GeomFromEWKT('LINESTRING ZM (0 1 2 3, 4 5 6 7, 8 9 10 11)'));
```

```

st_mmax
-----------
  11

```
