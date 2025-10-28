Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_NumPoints

ST_NumPoints returns the number of points in an input geometry.

## Syntax

```
ST_NumPoints(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`INTEGER`

If _geom_ is null, then null is returned.

If _geom_ is not of subtype `LINESTRING`, then null is returned.

## Examples

The following SQL returns the number of points in the input linestring.

```
SELECT ST_NumPoints(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'));
```

```

st_numpoints
-------------
4

```

The following SQL returns null because the input _geom_ is not of subtype `LINESTRING`.

```
SELECT ST_NumPoints(ST_GeomFromText('MULTIPOINT(1 2,3 4)'));
```

```

st_numpoints
-------------


```
