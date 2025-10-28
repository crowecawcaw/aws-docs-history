Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_DistanceSphere

ST_DistanceSphere returns the distance between two point geometries lying on a
sphere.

## Syntax

```
ST_DistanceSphere(*geom1*, *geom2*)
```

```
ST_DistanceSphere(*geom1*, *geom2*, *radius*)
```

## Arguments

_geom1_

A point value in degrees of data type `GEOMETRY` lying on a
sphere. The first coordinate of the point is the longitude value. The second
coordinate of the point is the latitude value. For 3DZ, 3DM, or 4D geometries,
only the first two coordinates are used.

_geom2_

A point value in degrees of data type `GEOMETRY` lying on a
sphere. The first coordinate of the point is the longitude value. The second
coordinate of the point is the latitude value. For 3DZ, 3DM, or 4D geometries,
only the first two coordinates are used.

_radius_

The radius of a sphere of data type `DOUBLE PRECISION`. If no
_radius_ is provided, the sphere defaults to Earth and
the radius is computed from the World Geodetic System (WGS) 84 representation
of the ellipsoid.

## Return type

`DOUBLE PRECISION` in the same units as the radius. If no radius is provided, the distance is in meters.

If _geom1_ or _geom2_ is null or empty, then null is returned.

If no _radius_ is provided, then the result is in meters along the Earth's surface.

If _radius_ is a negative number, then an error is returned.

If _geom1_ and _geom2_ don't have the same
value for the spatial reference system identifier (SRID), then an error is returned.

If _geom1_ or _geom2_ is not a point, then an error is returned.

## Examples

The following example SQL computes the distance in kilometers between two points on Earth.

```
SELECT ROUND(ST_DistanceSphere(ST_Point(-122, 47), ST_Point(-122.1, 47.1))/ 1000, 0);
```

```

  round
-----------
 13

```

The following example SQL computes the distances in kilometers between three airport locations in Germany:
Berlin Tegel (TXL), Munich International (MUC), and Frankfurt International (FRA).

```
WITH airports_raw(code,lon,lat) AS (
(SELECT 'MUC', 11.786111, 48.353889) UNION
(SELECT 'FRA', 8.570556, 50.033333) UNION
(SELECT 'TXL', 13.287778, 52.559722)),
airports1(code,location) AS (SELECT code, ST_Point(lon, lat) FROM airports_raw),
airports2(code,location) AS (SELECT * from airports1)
SELECT (airports1.code || ' <-> ' || airports2.code) AS airports,
round(ST_DistanceSphere(airports1.location, airports2.location) / 1000, 0) AS distance_in_km
FROM airports1, airports2 WHERE airports1.code < airports2.code ORDER BY 1;
```

```

  airports   | distance_in_km
-------------+----------------
 FRA <-> MUC |            299
 FRA <-> TXL |            432
 MUC <-> TXL |            480

```
