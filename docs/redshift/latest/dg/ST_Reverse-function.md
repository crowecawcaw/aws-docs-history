Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Reverse

ST_Reverse reverses the order of the vertices for linear and areal geometries. For
point or multipoint geometries, a copy of the original geometry is returned. For geometry
collections, ST_Reverse reverses the order of the vertices for each of the geometries in
the collection.

The dimension of the returned geometry is the same as that of the input geometry.

## Syntax

```
ST_Reverse(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY`

The spatial reference system identifier (SRID) of the returned geometry is the same
as that of the input geometry.

If _geom_ is null, then null is returned.

## Examples

The following SQL reverses the order of the points in a linestring.

```
SELECT ST_AsEWKT(ST_Reverse(ST_GeomFromText('LINESTRING(1 0,2 0,3 0,4 0)', 4326)));
```

```

    st_asewkt
------------------------------------
  SRID=4326;LINESTRING(4 0,3 0,2 0,1 0)

```
