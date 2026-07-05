Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_SetSRID

ST\_SetSRID returns a geometry that is the same as input geometry, except updated with
the value input for the spatial reference system identifier (SRID).

## Syntax

```
ST_SetSRID(*geom*, *srid*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

_srid_

A value of data type `INTEGER` that represents a SRID.

## Return type

`GEOMETRY`

The SRID value of the returned geometry is set to _srid_.

If _geom_ or _srid_ is null, then null is returned.

If _srid_ is negative, then an error is returned.

## Examples

The following SQL sets the SRID value of a linestring.

```
SELECT ST_AsEWKT(ST_SetSRID(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'),50));
```

```

st_asewkt
-------------
 SRID=50;LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)

```
