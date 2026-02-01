Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_LineInterpolatePoint

ST_LineInterpolatePoint returns a point along a line at a fractional distance from the start of the line.

To determine point equality, ST_LineInterpolatePoint operates on the 2D projection of
the input geometry. If the input geometry is empty, a copy of it is returned in the same
dimension as the input. For 3DZ, 3DM, and 4D geometries, the `z` or
`m` coordinate is the average of the `z` or `m`
coordinates of the segment where the point lies.

## Syntax

```
ST_LineInterpolatePoint(*geom*, *fraction*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The subtype is `LINESTRING`.

_fraction_

A value of data type `DOUBLE PRECISION` that represents the
position of a point along the linestring for the line. The value is a fraction
in the range 0–1, inclusive.

## Return type

`GEOMETRY` of subtype `POINT`.

If _geom_ or _fraction_ is null, then null is returned.

If _geom_ is empty, then the empty point is returned.

The spatial reference system identifier (SRID) value of the returned geometry is
the SRID value of the input geometry.

If _fraction_ is out of range, then an error is returned.

If _geom_ is not a linestring, then an error is returned.

## Examples

The following SQL returns a point halfway along a linestring.

```
SELECT ST_AsEWKT(ST_LineInterpolatePoint(ST_GeomFromText('LINESTRING(0 0, 5 5, 7 7, 10 10)'), 0.50));
```

```

st_asewkt
-----------
 POINT(5 5)

```

The following SQL returns a point 90 percent of the way along a linestring.

```
SELECT ST_AsEWKT(ST_LineInterpolatePoint(ST_GeomFromText('LINESTRING(0 0, 5 5, 7 7, 10 10)'), 0.90));
```

```

st_asewkt
-----------
 POINT(9 9)

```
