Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# default_geometry_encoding

## Values (default in bold)

1, **2**

## Description

A session configuration that specifies if spatial geometries created during this session are encoded with a bounding box.
If `default_geometry_encoding` is `1`, then geometries are not encoded with a bounding box.
If `default_geometry_encoding` is `2`, then geometries are encoded with a bounding box.
For more information about support for bounding boxes, see
[Bounding box](spatial-terminology.md#spatial-terminology-bounding-box "spatial-terminology.md#spatial-terminology-bounding-box").
