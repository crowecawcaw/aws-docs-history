Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_LineFromMultiPoint

ST_LineFromMultiPoint returns a linestring from an input multipoint geometry. The
order of the points is preserved. The spatial reference system identifier (SRID) of the
returned geometry is the same as that of the input geometry.
The dimension of the returned geometry is the same as that of the input geometry.

## Syntax

```
ST_LineFromMultiPoint(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.
The subtype must be `MULTIPOINT`.

## Return type

`GEOMETRY`

If _geom_ is null, then null is returned.

If _geom_ is empty, then an empty `LINESTRING` is returned.

If _geom_ contains empty points, then these empty points are ignored.

If _geom_ isn't a `MULTIPOINT`, then error is returned.

## Examples

The following SQL creates a linestring from a multipoint.

```
SELECT ST_AsEWKT(ST_LineFromMultiPoint(ST_GeomFromText('MULTIPOINT(0 0,10 0,10 10,5 5,0 5)',4326)));
```

```

 st_asewkt
---------------------------------------------
 SRID=4326;LINESTRING(0 0,10 0,10 10,5 5,0 5)

```
