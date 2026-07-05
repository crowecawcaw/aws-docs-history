Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# default\_geometry\_encoding

## Values (default in bold)

1, **2**

## Description

A session configuration that specifies if spatial geometries created during this session are encoded with a bounding box.
If `default_geometry_encoding` is `1`, then geometries are not encoded with a bounding box.
If `default_geometry_encoding` is `2`, then geometries are encoded with a bounding box.
For more information about support for bounding boxes, see
[Bounding box](spatial-terminology.md#spatial-terminology-bounding-box "spatial-terminology.md#spatial-terminology-bounding-box").
