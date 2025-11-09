Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_NDims

ST_NDims returns the coordinate dimension of a geometry. ST_NDims doesn't consider
the topological dimension of a geometry. Instead, it returns a constant value depending on
the dimension of the geometry.

## Syntax

```
ST_NDims(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`INTEGER` representing the inherent dimension of _geom_.

If _geom_ is null, then null is returned.

The values returned are as follows.

| Returned value | Dimension of input geometry |
| -------------- | --------------------------- |
| 2              | 2D                          |
| 3              | 3DZ or 3DM                  |
| 4              | 4D                          |

## Examples

The following SQL returns the number of dimensions of a 2D linestring.

```
SELECT ST_NDims(ST_GeomFromText('LINESTRING(0 0,1 1,2 2,0 0)'));
```

```

st_ndims
-------------
 2

```

The following SQL returns the number of dimensions of a 3DZ linestring.

```
SELECT ST_NDims(ST_GeomFromText('LINESTRING Z(0 0 3,1 1 3,2 2 3,0 0 3)'));
```

```

st_ndims
-------------
 3

```

The following SQL returns the number of dimensions of a 3DM linestring.

```
SELECT ST_NDims(ST_GeomFromText('LINESTRING M(0 0 4,1 1 4,2 2 4,0 0 4)'));
```

```

st_ndims
-------------
 3

```

The following SQL returns the number of dimensions of a 4D linestring.

```
SELECT ST_NDims(ST_GeomFromText('LINESTRING ZM(0 0 3 4,1 1 3 4,2 2 3 4,0 0 3 4)'));
```

```

st_ndims
-------------
 4

```
