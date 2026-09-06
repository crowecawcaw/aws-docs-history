

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ST\_GeoSquare
<a name="ST_GeoSquare-function"></a>

ST\_GeoSquare recursively subdivides the domain ([-180, 180], [-90, 90]) into equal square regions called *geosquares* to a specified depth. The subdivision is based on the location of a provided point. One of the geosquares containing the point is subdivided at each step until reaching the maximum depth. The selection of this geosquare is stable, that is, the function result depends on the input arguments only. The function returns a unique value that identifies the final geosquare in which the point is located.

The ST\_GeoSquare accepts a POINT where the x coordinate is representing the longitude, and the y coordinate is representing the latitude. The longitude and latitude are limited to [-180, 180] and [-90, 90], respectively. The output of ST\_GeoSquare can be used as input to the [ST\_GeomFromGeoSquare](ST_GeomFromGeoSquare-function.md) function.

There are 360° around the arc of the equatorial circumference of the Earth that are divided into two hemispheres (Eastern and Western), each with 180° of longitudinal lines (Meridians) from the 0° Meridian. By convention, the eastern longitudes are "\+" (positive) coordinates when projected to an x-axis on a Cartesian plane and the western longitudes are "-" (negative) coordinates when projected to an x-axis on a Cartesian plane. There are 90° of latitudinal lines north and south of the 0° equatorial circumference of the Earth, each parallel to the 0° equatorial circumference of the Earth. By convention, the northern latitudinal lines intersect the "\+" (positive) y-axis when projected to a Cartesian plane, and the southern latitudinal lines intersect the "-" (negative) y-axis when projected to a Cartesian plane. The spherical grid formed by the intersection of longitudinal lines and latitudinal lines is converted to a grid projected onto a Cartesian plane with standard positive and negative x-coordinates and positive and negative y-coordinates on the Cartesian plane.

The purpose of ST\_GeoSquare is to tag or mark close points with equal code values. Points that are located in the same geosquare receive the same code value. A geosquare is used to encode geographic coordinates (latitude and longitude) into an integer. A larger region is divided into grids to delineate an area on a map with varying resolutions. A geosquare can be used for spatial indexing, spatial binning, proximity searches, location searching, and creating unique place identifiers. The [ST\_GeoHash](ST_GeoHash-function.md) function follows a similar process of dividing a region into grids, but has a different encoding.

## Syntax
<a name="ST_GeoSquare-function-syntax"></a>

```
ST_GeoSquare(geom)
```

```
ST_GeoSquare(geom, max_depth)
```

## Arguments
<a name="ST_ST_GeoSquare-function-arguments"></a>

 *geom*   
A POINT value of data type `GEOMETRY` or an expression that evaluates to a POINT subtype. The x coordinate (longitude) of the point must be within the range: `-180` – `180`. The y coordinate (latitude) of the point must be within the range: `-90` – `90`. 

 *max\_depth*   
A value of data type `INTEGER`. The maximum number of times the domain containing the point is subdivided recursively. The value must be an integer from 1 – 32. The default is 32. The actual final number of the subdivisions is less than or equal to the specified *max\_depth*. 

## Return type
<a name="ST_GeoSquare-function-return"></a>

`BIGINT`

The function returns a unique value that identifies the final geosquare in which the input point is located. 

If the input *geom* is not a point, the function returns an error. 

If the input point is empty, the return value is not a valid input to the [ST\_GeomFromGeoSquare](ST_GeomFromGeoSquare-function.md) function. Use the [ST\_IsEmpty](ST_IsEmpty-function.md) function to prevent calls to ST\_GeoSquare with an empty point. 

If the input point is not within range, the function returns an error. 

If the input *max\_depth* is out of range, the function returns an error. 

## Examples
<a name="ST_ST_GeoSquare-function-examples"></a>

The following SQL returns a geosquare from an input point. 

```
SELECT ST_GeoSquare(ST_Point(13.5, 52.5));
```

```
  st_geosquare
-----------------------
 -4410772491521635895
```

The following SQL returns a geosquare from an input point with a maximum depth of `10`. 

```
SELECT ST_GeoSquare(ST_Point(13.5, 52.5), 10);
```

```
 st_geosquare
--------------
 797852
```