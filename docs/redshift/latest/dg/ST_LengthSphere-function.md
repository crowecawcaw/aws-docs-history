Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_LengthSphere

ST_LengthSphere returns the length of a linear geometry in meters.
For point, multipoint, and areal geometries, ST_LengthSphere returns 0.
For geometry collections, ST_LengthSphere returns the total length of the linear geometries in the collection in meters.

ST_LengthSphere interprets the coordinates of each point of the input geometry as longitude and latitude in degrees.
For 3DZ, 3DM, or 4D geometries, only the first two coordinates are used.

## Syntax

```
ST_LengthSphere(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`DOUBLE PRECISION` length in meters.
The length computation is based on the spherical model of the Earth
whose radius is Earth's mean radius of the World Geodetic System (WGS) 84 ellipsoidal model of the Earth.

If _geom_ is null, then null is returned.

## Examples

The following example SQL computes the length of a linestring in meters.

```
SELECT ST_LengthSphere(ST_GeomFromText('LINESTRING(10 10,45 45)'));
```

```

 st_lengthsphere
------------------
 5127736.08292556

```
