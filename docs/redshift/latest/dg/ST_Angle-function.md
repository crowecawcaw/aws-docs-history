Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Angle

ST_Angle returns the angle in radians between points measured clockwise as follows:

- If three points are input,
  then the returned angle P1-P2-P3 is measured as if the angle was obtained by rotating from P1 to P3 around P2 clockwise.
- If four points are input,
  then the returned clockwise angle formed by the directed lines P1-P2 and P3-P4 is returned.
  If the input is a degenerate case (that is, P1 equals P2, or P3 equals P4), then null is returned.
  The return value is in radians and in the range [0, 2π).

ST_Angle operates on 2D projections of the input geometries.

## Syntax

```
ST_Angle(*geom1*, *geom2*, *geom3*)
```

```
ST_Angle(*geom1*, *geom2*, *geom3*, *geom4*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The subtype must be `POINT`.

_geom2_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The subtype must be `POINT`.

_geom3_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The subtype must be `POINT`.

_geom4_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The subtype must be `POINT`.

## Return type

`DOUBLE PRECISION`.

If _geom1_ equals _geom2_, or _geom2_ equals
_geom3_, then a null is returned.

If _geom1_, _geom2_,
_geom3_, or _geom4_ is null, then a null is returned.

If any of _geom1_, _geom2_,
_geom3_, or _geom4_ is the empty point, then an
error is returned.

If _geom1_, _geom2_,
_geom3_, and _geom4_ don't have the same value
for the spatial reference system identifier (SRID), then an error is returned.

## Examples

The following SQL returns the angle converted to degrees of three input points.

```
SELECT ST_Angle(ST_Point(1,1), ST_Point(0,0), ST_Point(1,0)) / Pi() * 180.0 AS angle;
```

```

 angle
---------------
    45

```

The following SQL returns the angle converted to degrees of four input points.

```
SELECT ST_Angle(ST_Point(1,1), ST_Point(0,0), ST_Point(1,0), ST_Point(2,0)) / Pi() * 180.0 AS angle;
```

```

 angle
---------------
   225

```
