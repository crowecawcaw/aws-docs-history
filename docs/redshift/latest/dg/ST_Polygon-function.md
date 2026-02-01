Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Polygon

ST_Polygon returns a polygon geometry whose outer ring is the input linestring with
the value that was input for the spatial reference system identifier (SRID).

The dimension of the returned geometry is the same as that of the input geometry.

## Syntax

```
ST_Polygon(*linestring*, *srid*)
```

## Arguments

_linestring_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type. The subtype must be
`LINESTRING` that represents a linestring. The
_linestring_ value must be closed.

_srid_

A value of data type `INTEGER` that represents a SRID.

## Return type

`GEOMETRY` of subtype `POLYGON`.

The SRID value of the returned geometry is set to _srid_.

If _linestring_ or _srid_ is null, then null is returned.

If _linestring_ is not a linestring, then an error is returned.

If _linestring_ is not closed, then an error is returned.

If _srid_ is negative, then an error is returned.

## Examples

The following SQL constructs a polygon with an SRID value.

```
SELECT ST_AsEWKT(ST_Polygon(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'),4356));
```

```

st_asewkt
-------------
 SRID=4356;POLYGON((77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07))

```
