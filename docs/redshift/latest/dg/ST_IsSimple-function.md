Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_IsSimple

ST_IsSimple returns true if the 2D projection of the input geometry is simple.
For more information about the definition of a simple geometry, see
[Geometric simplicity](spatial-terminology.md#spatial-terminology-simplicity "spatial-terminology.md#spatial-terminology-simplicity").

## Syntax

```
ST_IsSimple(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`BOOLEAN`

If _geom_ is null, then null is returned.

## Examples

The following SQL checks if the specified linestring is simple. In this example,
it isn't simple because it has self-intersection.

```
SELECT ST_IsSimple(ST_GeomFromText('LINESTRING(0 0,10 0,5 5,5 -5)'));
```

```

 st_issimple
-----------
 false

```
