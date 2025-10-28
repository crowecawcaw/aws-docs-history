Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Y

ST_Y returns the second coordinate of an input point.

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
