Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_GeoSquare

ST_GeoSquare recursively subdivides the domain ([-180, 180], [-90, 90]) into equal square regions called _geosquares_ to a specified depth.
The subdivision is based on the location of a provided point.
One of the geosquares containing the point is subdivided at each step until reaching the maximum depth.
The selection of this geosquare is stable, that is, the function result depends on the input arguments only.
The function returns a unique value that identifies the final geosquare in which the point is located.

The ST_GeoSquare accepts a POINT where the x coordinate is representing the longitude, and the y coordinate is representing the latitude.
The longitude and latitude are limited to [-180, 180] and [-90, 90], respectively.
The output of ST_GeoSquare can be used as input to the [ST_GeomFromGeoSquare](ST_GeomFromGeoSquare-function.md "ST_GeomFromGeoSquare-function.md") function.

There are 360° around the arc of the equatorial circumference of the Earth
that are divided into two hemispheres (Eastern and Western), each with 180° of longitudinal lines (Meridians) from the 0° Meridian.
By convention, the eastern longitudes are "+" (positive) coordinates when projected to an x-axis on a Cartesian plane and
the western longitudes are "-" (negative) coordinates when projected to an x-axis on a Cartesian plane.
There are 90° of latitudinal lines north and south of the 0° equatorial circumference of the Earth, each parallel to the 0° equatorial circumference of the Earth.
By convention, the northern latitudinal lines intersect the "+" (positive) y-axis when projected to a Cartesian plane,
and the southern latitudinal lines intersect the "-" (negative) y-axis when projected to a Cartesian plane.
The spherical grid formed by the intersection of longitudinal lines and latitudinal lines is converted to a grid projected onto a Cartesian plane
with standard positive and negative x-coordinates and positive and negative y-coordinates on the Cartesian plane.

The purpose of ST_GeoSquare is to tag or mark close points with equal code values.
Points that are located in the same geosquare receive the same code value.
A geosquare is used to encode geographic coordinates (latitude and longitude) into an integer.
A larger region is divided into grids to delineate an area on a map with varying resolutions.
A geosquare can be used for spatial indexing, spatial binning, proximity searches, location searching, and creating unique place identifiers.

The [ST_GeoHash](ST_GeoHash-function.md "ST_GeoHash-function.md") function follows a similar process of dividing a region into grids, but has a different encoding.

## Syntax

```
ST_GeoSquare(*geom*)
```

```
ST_GeoSquare(*geom*, *max\_depth*)
```

## Arguments

_geom_

A POINT value of data type `GEOMETRY` or an expression that evaluates to a POINT subtype.
The x coordinate (longitude) of the point must be within the range: `-180` – `180`.
The y coordinate (latitude) of the point must be within the range: `-90` – `90`.

_max_depth_

A value of data type `INTEGER`.
The maximum number of times the domain containing the point is subdivided recursively.
The value must be an integer from 1 – 32.
The default is 32.

The actual final number of the subdivisions is less than or equal to the specified _max_depth_.

## Return type

`BIGINT`

The function returns a unique value that identifies the final geosquare in which the input point is located.

If the input _geom_ is not a point, the function returns an error.

If the input point is empty, the return value is not a valid input to the [ST_GeomFromGeoSquare](ST_GeomFromGeoSquare-function.md "ST_GeomFromGeoSquare-function.md") function.
Use the [ST_IsEmpty](ST_IsEmpty-function.md "ST_IsEmpty-function.md") function to prevent calls to ST_GeoSquare with an empty point.

If the input point is not within range, the function returns an error.

If the input _max_depth_ is out of range, the function returns an error.

## Examples

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
