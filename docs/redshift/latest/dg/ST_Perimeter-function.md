Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_Perimeter

For an input areal geometry, ST_Perimeter returns the Cartesian perimeter (length of the boundary) of the 2D projection.
The perimeter units are the same as the units in which the coordinates of
the input geometry are expressed. The function returns zero (0) for points, multipoints,
and linear geometries. When the input is a geometry collection, the function returns the
sum of the perimeters of the geometries in the collection.

For an input geography, ST_Perimeter returns the geodesic perimeter (length of the boundary) of the 2D projection of an input areal geography computed on the spheroid determined by the SRID.
The unit of perimeter is in meters. The function returns zero (0) for points, multipoints, and linear geographies.
When the input is a geometry collection, the function returns the sum of the perimeters of the geographies in the collection.

## Syntax

```
ST_Perimeter(*geo*)
```

## Arguments

_geo_

A value of data type `GEOMETRY` or `GEOGRAPHY`, or an expression that
evaluates to a `GEOMETRY` or `GEOGRAPHY` type.

## Return type

`DOUBLE PRECISION`

If _geo_ is null, then null is returned.

If the SRID value is not found, then an error is returned.

## Examples

The following SQL returns the Cartesian perimeter of a multipolygon.

```
SELECT ST_Perimeter(ST_GeomFromText('MULTIPOLYGON(((0 0,10 0,0 10,0 0)),((10 0,20 0,20 10,10 0)))'));
```

```

 st_perimeter
--------------------------------
    68.2842712474619

```

The following SQL returns the Cartesian perimeter of a multipolygon.

```
SELECT ST_Perimeter(ST_GeomFromText('MULTIPOLYGON(((0 0,10 0,0 10,0 0)),((10 0,20 0,20 10,10 0)))'));
```

```

 st_perimeter
--------------------------------
    68.2842712474619

```

The following SQL returns the perimeter of a polygon in a geography.

```
SELECT ST_Perimeter(ST_GeogFromText('SRID=4326;POLYGON((0 0,1 0,0 1,0 0))'));
```

```

 st_perimeter
------------------
 378790.428393693

```

The following SQL returns the perimeter of a linestring in a geography.

```
SELECT ST_Perimeter(ST_GeogFromText('SRID=4326;LINESTRING(5 0,10 0)'));
```

```

 st_perimeter
--------------
 0

```
