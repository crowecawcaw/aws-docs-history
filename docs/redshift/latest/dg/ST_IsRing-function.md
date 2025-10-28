Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_IsRing

ST_IsRing returns true if the input linestring is a ring. A linestring is a ring if it is closed and simple.

## Syntax

```
ST_IsRing(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The geometry must be a `LINESTRING`.

## Return type

`BOOLEAN`

If _geom_ is not a `LINESTRING`, then an error is returned.

## Examples

The following SQL checks if the specified linestring is a ring.

```
SELECT ST_IsRing(ST_GeomFromText('linestring(0 0, 1 1, 1 2, 0 0)'));
```

```

st_isring
-----------
 true

```
