Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Azimuth

ST_Azimuth returns the north-based Cartesian azimuth using the 2D projections of the two input points.

## Syntax

```
ST_Azimuth(*point1*, *point2*)
```

## Arguments

_point1_

A `POINT` value of data type `GEOMETRY`. The
spatial reference system identifier (SRID) of _point1_
must match the SRID of _point2_.

_point2_

A `POINT` value of data type `GEOMETRY`. The SRID of _point2_ must match the SRID of _point1_.

## Return type

A number that is an angle in radians of `DOUBLE PRECISION` data type.
Values range from 0 (inclusive) to 2 pi (exclusive).

If _point1_ or _point2_
is the empty point, then an error is returned.

If either _point1_ or _point2_ is null, then null is returned.

If _point1_ and _point2_ are equal, then null is returned.

If _point1_ or _point2_ is not a point, then an error is returned.

If _point1_ and _point2_ don't have the value for the spatial reference system identifier (SRID), then an error is returned.

## Examples

The following SQL returns the azimuth of the input points.

```
SELECT ST_Azimuth(ST_Point(1,2), ST_Point(5,6));
```

```

st_azimuth
-------------------
 0.7853981633974483

```
