Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_IsEmpty

ST\_IsEmpty returns true if the input geometry is empty. A geometry is not empty if it
contains at least one nonempty point.

ST\_IsEmpty returns true if the input geometry has at least one nonempty point.

## Syntax

```
ST_IsEmpty(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`BOOLEAN`

If _geom_ is null, then null is returned.

## Examples

The following SQL checks if the specified polygon is empty.

```
SELECT ST_IsEmpty(ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'));
```

```

st_isempty
-----------
 false

```
