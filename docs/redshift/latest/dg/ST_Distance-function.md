Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Distance

For input geometries, ST_Distance returns the minimum Euclidean distance between the 2D projections of the two input geometry values.

For 3DM, 3DZ, 4D geometries, ST_Distance returns the Euclidean distance between the 2D projections of two input geometry values.

For input geographies, ST_Distance returns the geodesic distance of the two 2D points.
The unit of distance is in meters. For geographies other than points and empty points an error is returned.

## Syntax

```
ST_Distance(*geo1*, *geo2*)
```

## Arguments

_geo1_

A value of data type `GEOMETRY` or `GEOGRAPHY`, or an expression that evaluates to a `GEOMETRY` or `GEOGRAPHY` type.
The data type of _geo1_ must be the same as _geo2_.

_geo2_

A value of data type `GEOMETRY` or `GEOGRAPHY`, or an expression that evaluates to a `GEOMETRY` or `GEOGRAPHY` type.
The data type of _geo2_ must be the same as _geo1_.

## Return type

`DOUBLE PRECISION` in the same units as the input geometries or geographies.

If _geo1_ or _geo2_ is null or empty, then null is returned.

If _geo1_ and _geo2_ don't have the same
value for the spatial reference system identifier (SRID), then an error is returned.

If _geo1_ or _geo2_ is a geometry collection, then an error is returned.

## Examples

The following SQL returns the distance between two polygons.

```
SELECT ST_Distance(ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'), ST_GeomFromText('POLYGON((-1 -3,-2 -1,0 -3,-1 -3))'));
```

```

  st_distance
-----------
1.4142135623731

```

The following SQL returns the distance (in meters) between the Brandenburg Gate and the Reichstag building in Berlin using a GEOGRAPHY data type.

```
SELECT ST_Distance(ST_GeogFromText('POINT(13.37761826722198 52.516411678282445)'), ST_GeogFromText('POINT(13.377950831464005 52.51705102546893)'));
```

```

   st_distance
------------------
 74.64129172609631

```
