Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_Y

ST\_Y returns the second coordinate of an input point.

## Syntax

```
ST_Y(*point*)
```

## Arguments

_point_

A `POINT` value of data type `GEOMETRY`.

## Return type

`DOUBLE PRECISION` value of the second coordinate.

If _point_ is null, then null is returned.

If _point_ is the empty point, then null is returned.

If _point_ is not a `POINT`, then an error is returned.

## Examples

The following SQL returns the second coordinate of a point.

```
SELECT ST_Y(ST_Point(1,2));
```

```

st_y
-----------
 2.0

```
