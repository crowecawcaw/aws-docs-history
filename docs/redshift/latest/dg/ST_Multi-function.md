Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_Multi

ST\_Multi converts a geometry to the corresponding multitype. If the input geometry is
already a multitype or a geometry collection, a copy of it is returned. If the input
geometry is a point, linestring, or polygon, then a multipoint, multilinestring, or
multipolygon, respectively, that contains the input geometry is returned.

## Syntax

```
ST_Multi(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY` with subtype `MULTIPOINT`, `MULTILINESTRING`,
`MULTIPOLYGON`, or `GEOMETRYCOLLECTION`.

The spatial reference system identifier (SRID) of the returned geometry is the same
as that of the input geometry.

If _geom_ is null, then null is returned.

## Examples

The following SQL returns a multipoint from an input multipoint.

```
SELECT ST_AsEWKT(ST_Multi(ST_GeomFromText('MULTIPOINT((1 2),(3 4))', 4326)));
```

```

    st_asewkt
------------------------------------
  SRID=4326;MULTIPOINT((1 2),(3 4))

```

The following SQL returns a multipoint from an input point.

```
SELECT ST_AsEWKT(ST_Multi(ST_GeomFromText('POINT(1 2)', 4326)));
```

```

    st_asewkt
------------------------------------
  SRID=4326;MULTIPOINT((1 2))

```

The following SQL returns a geometry collection from an input geometry collection.

```
SELECT ST_AsEWKT(ST_Multi(ST_GeomFromText('GEOMETRYCOLLECTION(POINT(1 2),MULTIPOINT((1 2),(3 4)))', 4326)));
```

```

    st_asewkt
------------------------------------
  SRID=4326;GEOMETRYCOLLECTION(POINT(1 2),MULTIPOINT((1 2),(3 4)))

```
