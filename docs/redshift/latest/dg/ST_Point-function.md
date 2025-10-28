Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Point

ST_Point returns a point geometry from the input coordinate values.

## Syntax

```
ST_Point(*x*, *y*)
```

## Arguments

_x_

A value of data type `DOUBLE PRECISION` that represents a first coordinate.

_y_

A value of data type `DOUBLE PRECISION` that represents a second coordinate.

## Return type

`GEOMETRY` of subtype `POINT`.

The spatial reference system identifier (SRID) value of the returned geometry is
set to 0.

If _x_ or _y_ is null, then null is returned.

## Examples

The following SQL constructs a point geometry from the input coordinates.

```
SELECT ST_AsText(ST_Point(5.0, 7.0));
```

```

st_astext
-------------
POINT(5 7)

```
