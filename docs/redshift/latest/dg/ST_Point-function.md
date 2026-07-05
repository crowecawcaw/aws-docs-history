Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_Point

ST\_Point returns a point geometry from the input coordinate values.

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
