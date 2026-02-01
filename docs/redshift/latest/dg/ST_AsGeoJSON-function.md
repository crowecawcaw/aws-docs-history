Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_AsGeoJSON

ST_AsGeoJSON returns the GeoJSON representation of an input geometry or geography. For more
information about GeoJSON, see [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON "https://en.wikipedia.org/wiki/GeoJSON") in Wikipedia.

For 3DZ and 4D geometries, the output geometry is a 3DZ projection of the input 3DZ or 4D geometry.
That is, the `x`, `y`, and `z` coordinates are present in the output.
For 3DM geometries, the output geometry is a 2D projection of the input 3DM geometry.
That is, only `x` and `y` coordinates are present in the output.

For input geographies, ST_AsGeoJSON returns the GeoJSON representation of an input geography.
The coordinates of the geography are displayed using the specified precision.

## Syntax

```
ST_AsGeoJSON(*geo*)
```

```
ST_AsGeoJSON(*geo*, *precision*)
```

## Arguments

_geo_

A value of data type `GEOMETRY` or `GEOGRAPHY`, or an expression that evaluates to a `GEOMETRY` or `GEOGRAPHY` type.

_precision_

A value of data type `INTEGER`. For geometries, the coordinates of _geo_
are displayed using the specified precision 1–20. If
_precision_ is not specified, the default is 15.
For geographies, the coordinates of _geo_
are displayed using the specified precision. If
_precision_ is not specified, the default is 15.

## Return type

`VARCHAR`

If _geo_ is null, then null is returned.

If _precision_ is null, then null is returned.

If the result is larger than a 64-KB `VARCHAR`, then an error is
returned.

## Examples

The following SQL returns the GeoJSON representation of a linestring.

```
SELECT ST_AsGeoJSON(ST_GeomFromText('LINESTRING(3.141592653589793 -6.283185307179586,2.718281828459045 -1.414213562373095)'));
```

```

st_asgeojson
----------------------------------------------------------------------------------------------------------------
 {"type":"LineString","coordinates":[[3.14159265358979,-6.28318530717959],[2.71828182845905,-1.41421356237309]]}

```

The following SQL returns the GeoJSON representation of a linestring. The coordinates of the geometries are displayed with six digits of precision.

```
SELECT ST_AsGeoJSON(ST_GeomFromText('LINESTRING(3.141592653589793 -6.283185307179586,2.718281828459045 -1.414213562373095)'), 6);
```

```

st_asgeojson
-----------------------------------------------------------------------------
  {"type":"LineString","coordinates":[[3.14159,-6.28319],[2.71828,-1.41421]]}

```

The following SQL returns the GeoJSON representation of a geography.

```
SELECT ST_AsGeoJSON(ST_GeogFromText('LINESTRING(110 40, 2 3, -10 80, -7 9)'));
```

```

                             st_asgeojson
----------------------------------------------------------------------
 {"type":"LineString","coordinates":[[110,40],[2,3],[-10,80],[-7,9]]}

```
