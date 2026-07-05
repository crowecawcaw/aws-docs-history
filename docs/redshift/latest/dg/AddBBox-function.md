Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# AddBBox

AddBBox returns a copy of the input geometry that supports encoding with a precomputed bounding box.
For more information about support for bounding boxes, see
[Bounding box](spatial-terminology.md#spatial-terminology-bounding-box "spatial-terminology.md#spatial-terminology-bounding-box").

## Syntax

```
AddBBox(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY`

If _geom_ is null, then null is returned.

## Examples

The following SQL returns a copy of an input polygon geometry that supports being encoded with a bounding box.

```
SELECT ST_AsText(AddBBox(ST_GeomFromText('POLYGON((0 0,1 0,0 1,0 0))')));
```

```

 st_astext
----------
 POLYGON((0 0,1 0,0 1,0 0))

```
