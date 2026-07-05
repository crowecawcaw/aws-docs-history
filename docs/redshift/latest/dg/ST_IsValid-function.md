Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_IsValid

ST\_IsValid returns true if the 2D projection of the input geometry is valid.
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
