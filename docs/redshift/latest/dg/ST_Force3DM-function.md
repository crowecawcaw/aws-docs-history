Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Force3DM

ST_Force3DM returns a 3DM geometry of the input geometry.
For 2D geometries, the `m` coordinates of the nonempty points in the output geometry are all set to `0`.
For 3DM geometries, a copy of the input geometry is returned.
For 3DZ geometries, the geometry is projected to the xy-Cartesian plane,
and the `m` coordinates of the nonempty points in the output geometry are all set to `0`.
For 4D geometries, the geometry is projected to the xym-Cartesian space.
Empty points in the input geometry remain empty points in the output geometry.

## Syntax

```
ST_Force3DM(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that
evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY`.

The spatial reference system identifier (SRID) value of the returned geometry is
the SRID value of the input geometry.

If _geom_ is null, then null is returned.

If _geom_ is empty, then an empty geometry is returned.

## Examples

The following SQL returns a 3DM geometry from a 3DZ geometry.

```
SELECT ST_AsEWKT(ST_Force3DM(ST_GeomFromText('MULTIPOINT Z(0 1 2, EMPTY, 2 3 4, 5 6 7)')));
```

```

st_asewkt
-----------
  MULTIPOINT M ((0 1 0),EMPTY,(2 3 0),(5 6 0))

```
