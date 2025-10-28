Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DropBBox

DropBBox returns a copy of the input geometry that doesn't support encoding with a precomputed bounding box.
For more information about support for bounding boxes, see
[Bounding box](spatial-terminology.md#spatial-terminology-bounding-box "spatial-terminology.md#spatial-terminology-bounding-box").

## Syntax

```
DropBBox(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY`

If _geom_ is null, then null is returned.

## Examples

The following SQL returns a copy of an input polygon geometry that doesn't support being encoded with a bounding box.

```
SELECT ST_AsText(DropBBox(ST_GeomFromText('POLYGON((0 0,1 0,0 1,0 0))')));
```

```

 st_astext
----------
 POLYGON((0 0,1 0,0 1,0 0))

```
