

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ST\_GeomFromGeoSquare
<a name="ST_GeomFromGeoSquare-function"></a>

ST\_GeomFromGeoSquare returns a geometry that covers the area that is represented by an input geosquare value. The returned geometry is always two-dimensional. To calculate a geosquare value, see [ST\_GeoSquare](ST_GeoSquare-function.md).

## Syntax
<a name="ST_GeomFromGeoSquare-function-syntax"></a>

```
ST_GeomFromGeoSquare(geosquare)
```

```
ST_GeomFromGeoSquare(geosquare, max_depth)
```

## Arguments
<a name="ST_GeomFromGeoSquare-function-arguments"></a>

 *geosquare*   
A value of data type `BIGINT` or an expression that evaluates to a `BIGINT` type that is a geosquare value that describes the sequence of subdivisions made on the initial domain to reach the desired square. This value is calculated by [ST\_GeoSquare](ST_GeoSquare-function.md).

 *max\_depth*   
A value of data type `INTEGER` that represents the maximum number of domain subdivisions made on the initial domain. The value must be greater than or equal to `1`.

## Return type
<a name="ST_GeomFromGeoSquare-function-return"></a>

`GEOMETRY`

If *geosquare* is not valid, the function returns an error. 

If the input *max\_depth* is not within range, the function returns an error. 

## Examples
<a name="ST_GeomFromGeoSquare-function-examples"></a>

The following SQL returns a geometry from a geosquare value.

```
SELECT ST_AsText(ST_GeomFromGeoSquare(797852));
```

```
 st_astext       
--------------------------------------------------------------------------------------------------------------------
 POLYGON((13.359375 52.3828125,13.359375 52.734375,13.7109375 52.734375,13.7109375 52.3828125,13.359375 52.3828125))
```

The following SQL returns a geometry from a geosquare value and a maximum depth of `3`. 

```
SELECT ST_AsText(ST_GeomFromGeoSquare(797852, 3));
```

```
 st_astext       
--------------------------------------
 POLYGON((0 45,0 90,45 90,45 45,0 45))
```

The following SQL first calculates the geosquare value for Seattle by specifying the x coordinate as longitude and the y coordinate as latitude (-122.3, 47.6). Then it returns the polygon for the geosquare. Although the output is a two-dimensional geometry, it can be used to calculate spatial data in terms of longitude and latitude.

```
SELECT ST_AsText(ST_GeomFromGeoSquare(ST_GeoSquare(ST_Point(-122.3, 47.6))));
```

```
 st_astext
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
POLYGON((-122.335167014971 47.6080129947513,-122.335167014971 47.6080130785704,-122.335166931152 47.6080130785704,-122.335166931152 47.6080129947513,-122.335167014971 47.6080129947513))
```