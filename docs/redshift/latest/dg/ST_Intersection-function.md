Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Intersection

ST_Intersection returns a geometry representing the point-set intersection of two geometries.
That is, it returns the portion of the two input geometries that is shared between them.

## Syntax

```
ST_Intersection(*geom1*, *geom2*)
```

## Arguments

_geom1_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

_geom2_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`GEOMETRY`

If _geom1_ and _geom2_ don't share any space (they are disjoint), then an empty geometry is returned.

If _geom1_ or _geom2_ are empty, then an empty geometry is returned.

If _geom1_ and _geom2_ don't have the same
value for the spatial reference system identifier (SRID), then an error is returned.

If _geom1_ or _geom2_ is a geometry collection, then an error is returned.

If _geom1_ or _geom2_ is not a two-dimensional (2D) geometry, then an error is returned.

## Examples

The following SQL returns the non-empty geometry representing the intersection of two input geometries.

```
SELECT ST_AsEWKT(ST_Intersection(ST_GeomFromText('polygon((0 0,100 100,0 200,0 0))'), ST_GeomFromText('polygon((0 0,10 0,0 10,0 0))')));
```

```

        st_asewkt
-------------------------
 POLYGON((0 0,0 10,5 5,0 0))

```

The following SQL returns an empty geometry when passed disjoint (non-intersecting) input geometries.

```
SELECT ST_AsEWKT(ST_Intersection(ST_GeomFromText('linestring(0 100,0 0)'), ST_GeomFromText('polygon((1 0,10 0,1 10,1 0))')));
```

```

    st_asewkt
------------------
 LINESTRING EMPTY

```
