Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Points

ST_Points returns a multipoint geometry containing all nonempty points in the input
geometry. ST_Points doesn't remove points that are duplicated in the input, including
the start and end points of ring geometries.

## Syntax

```
ST_Points(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY` of subtype `MULTIPOINT`.

The spatial reference system identifier (SRID) value of the returned geometry is
the same as _geom_.

If _geom_ is null, then null is returned.

If _geom_ is empty, then the empty multipoint
is returned.

## Examples

The following SQL examples construct a multipoint geometry from the input
geometry. The result is a multipoint geometry containing the nonempty points in the
input geometry.

```
SELECT ST_AsEWKT(ST_Points(ST_SetSRID(ST_GeomFromText('LINESTRING(1 0,2 0,3 0)'), 4326)));
```

```

st_asewkt
-------------
SRID=4326;MULTIPOINT((1 0),(2 0),(3 0))

```

```
SELECT ST_AsEWKT(ST_Points(ST_SetSRID(ST_GeomFromText('MULTIPOLYGON(((0 0,1 0,0 1,0 0)))'), 4326)));
```

```

st_asewkt
-------------
SRID=4326;MULTIPOINT((0 0),(1 0),(0 1),(0 0))

```
