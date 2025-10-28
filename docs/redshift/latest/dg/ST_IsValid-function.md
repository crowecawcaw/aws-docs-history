Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_IsValid

ST_IsValid returns true if the 2D projection of the input geometry is valid.
For more information about the definition of a valid geometry, see
[Geometric validity](spatial-terminology.md#spatial-terminology-validity "spatial-terminology.md#spatial-terminology-validity").

## Syntax

```
ST_IsValid(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`BOOLEAN`

If _geom_ is null, then null is returned.

## Examples

The following SQL checks if the specified polygon is valid. In this example, the
polygon is invalid because the interior of the polygon isn't simply connected.

```
SELECT ST_IsValid(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0),(5 0,10 5,5 10,0 5,5 0))'));
```

```

 st_isvalid
-----------
 false

```
