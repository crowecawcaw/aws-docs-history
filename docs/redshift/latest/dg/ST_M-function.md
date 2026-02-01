Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_M

ST_M returns the `m` coordinate of an input point.

## Syntax

```
ST_M(*point*)
```

## Arguments

_point_

A `POINT` value of data type `GEOMETRY`.

## Return type

`DOUBLE PRECISION` value of the `m` coordinate.

If _point_ is null, then null is returned.

If _point_ is a 2D or 3DZ point, then null is returned.

If _point_ is the empty point, then null is returned.

If _point_ is not a `POINT`, then an error is returned.

## Examples

The following SQL returns the `m` coordinate of a point in a 3DM geometry.

```
SELECT ST_M(ST_GeomFromEWKT('POINT M (1 2 3)'));
```

```

st_m
-----------
 3

```

The following SQL returns the `m` coordinate of a point in a 4D geometry.

```
SELECT ST_M(ST_GeomFromEWKT('POINT ZM (1 2 3 4)'));
```

```

st_m
-----------
 4

```
