Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_MakeEnvelope

ST_MakeEnvelope returns a geometry as follows:

- If the input coordinates specify a point, then the returned geometry is a point.
- If the input coordinates specify a line, then the returned geometry is a linestring.
- Otherwise, the returned geometry is a polygon, where the input coordinates specify the
  lower-left and upper-right corners of a box.
  If provided, the spatial reference system identifier (SRID) value of the returned geometry is set
  to the input SRID value.

## Syntax

```
ST_MakeEnvelope(*xmin*, *ymin*, *xmax*, *ymax*)
```

```
ST_MakeEnvelope(*xmin*, *ymin*, *xmax*, *ymax*, *srid*)
```

## Arguments

_xmin_

A value of data type `DOUBLE PRECISION`. This value is the
first coordinate of the lower-left corner of a box.

_ymin_

A value of data type `DOUBLE PRECISION`. This value is the
second coordinate of the lower-left corner of a box.

_xmax_

A value of data type `DOUBLE PRECISION`. This value is the
first coordinate of the upper-right corner of a box.

_ymax_

A value of data type `DOUBLE PRECISION`. This value is the
second coordinate of the upper-right corner of a box.

_srid_

A value of data type `INTEGER`
that represents a spatial reference system identifier (SRID).
If the SRID value is not provided, then it is set to zero.

## Return type

`GEOMETRY` of subtype `POINT`, `LINESTRING`, or `POLYGON`.

The SRID of the returned geometry is set to `srid` or zero if
`srid` isn't set.

If _xmin_, _ymin_, _xmax_, _ymax_,
or _srid_ is null, then null is returned.

If _srid_ is negative, then an error is returned.

## Examples

The following SQL returns a polygon representing an envelope defined by the four input coordinate values.

```
SELECT ST_AsEWKT(ST_MakeEnvelope(2,4,5,7));
```

```

 st_astext
---------------
 POLYGON((2 4,2 7,5 7,5 4,2 4))

```

The following SQL returns a polygon representing an envelope defined by
the four input coordinate values and an SRID value.

```
SELECT ST_AsEWKT(ST_MakeEnvelope(2,4,5,7,4326));
```

```

 st_astext
----------------------------------
 SRID=4326;POLYGON((2 4,2 7,5 7,5 4,2 4))

```
