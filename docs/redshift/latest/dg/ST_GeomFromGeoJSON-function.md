Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_GeomFromGeoJSON

ST_GeomFromGeoJSON constructs a geometry object from the GeoJSON representation of an input geometry.
For more information about the GeoJSON format, see [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON "https://en.wikipedia.org/wiki/GeoJSON") in Wikipedia.

If there is at least one point with three or more coordinates, the resulting geometry is 3DZ,
where the Z component is zero for the points that have only two coordinates.
If all points in the input GeoJSON contain two coordinates or are empty,
ST_GeomFromGeoJSON returns a 2D geometry.
The returned geometry always has the spatial reference identifier (SRID) of 4326.

## Syntax

```
ST_GeomFromGeoJSON(*geojson\_string*)
```

## Arguments

_geojson_string_

A value of data type `VARCHAR` or `SUPER`, or an expression that evaluates to a `VARCHAR` type,
that is a GeoJSON representation of a geometry.

## Return type

`GEOMETRY`

If _geojson_string_ is null, then null is returned.

If _geojson_string_ is not valid, then an error is returned.

## Examples

The following SQL returns a 2D geometry represented in the input GeoJSON.

```
SELECT ST_AsEWKT(ST_GeomFromGeoJSON('{"type":"Point","coordinates":[1,2]}'));
```

```

 st_asewkt
-----------------------
 SRID=4326;POINT(1 2)

```

The following SQL returns a 3DZ geometry represented in the input GeoJSON.

```
SELECT ST_AsEWKT(ST_GeomFromGeoJSON('{"type":"LineString","coordinates":[[1,2,3],[4,5,6],[7,8,9]]}'));
```

```

 st_asewkt
------------------------------------------
 SRID=4326;LINESTRING Z (1 2 3,4 5 6,7 8 9)

```

The following SQL returns 3DZ geometry when only one point has three coordinates while all other points have two coordinates in the input GeoJSON.

```
SELECT ST_AsEWKT(ST_GeomFromGeoJSON('{"type":"Polygon","coordinates":[[[0, 0],[0, 1, 8],[1, 0],[0, 0]]]}'));
```

```

 st_asewkt
------------------------------------------------
 SRID=4326;POLYGON Z ((0 0 0,0 1 8,1 0 0,0 0 0))

```
