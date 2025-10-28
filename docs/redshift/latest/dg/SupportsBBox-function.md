Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SupportsBBox

SupportsBBox returns true if the input geometry supports encoding with a precomputed bounding box.
For more information about support for bounding boxes, see
[Bounding box](spatial-terminology.md#spatial-terminology-bounding-box "spatial-terminology.md#spatial-terminology-bounding-box").

## Syntax

```
SupportsBBox(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

## Return type

`BOOLEAN`

If _geom_ is null, then null is returned.

## Examples

The following SQL returns true because the input point geometry supports being encoded with a bounding box.

```
SELECT SupportsBBox(AddBBox(ST_GeomFromText('POLYGON((0 0,1 0,0 1,0 0))')));
```

```

supportsbbox
--------------
t

```

The following SQL returns false because the input point geometry doesn't support being encoded with a bounding box.

```
SELECT SupportsBBox(DropBBox(ST_GeomFromText('POLYGON((0 0,1 0,0 1,0 0))')));
```

```

supportsbbox
--------------
f

```
