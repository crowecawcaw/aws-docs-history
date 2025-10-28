Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Querying spatial data in Amazon Redshift

_Spatial data_ describes the position and shape of a
geometry in a defined space (a spatial reference system). Amazon Redshift supports spatial data with the
`GEOMETRY` and `GEOGRAPHY` data types, which contain spatial data and
optionally the data's spatial reference system identifier (SRID).

Spatial data contains geometric data that you can use to represent geographic features.
Examples of this type of data include weather reports, map directions, tweets with geographic
positions, store locations, and airline routes. Spatial data plays an important role in
business analytics, reporting, and forecasting.

You can query spatial data with Amazon Redshift SQL functions. Spatial data contains geometric values
for an object.

The `GEOMETRY` data type operations work on the Cartesian plane.
Although the spatial reference system identifier (SRID) is stored inside the object,
this SRID is merely an identifier of the coordinate system and plays no role in the algorithms used to process the `GEOMETRY` objects.
Conversely, the operations on the `GEOGRAPHY` data type treat the coordinates inside objects as spherical coordinates on a spheroid.
This spheroid is defined by the SRID, which references a geographic spatial reference system.
By default, `GEOGRAPHY` data types are created with spatial reference (SRID) 4326, referencing the
World Geodetic System (WGS) 84. For more information about SRIDs, see
[Spatial reference system](https://en.wikipedia.org/wiki/Spatial_reference_system "https://en.wikipedia.org/wiki/Spatial_reference_system")
in Wikipedia.

You can use the ST_Transform function to transform the coordinates from various spatial
reference systems. After the transformation of the coordinates is done, you can also use a
simple cast between the two, as long as the input `GEOMETRY` is encoded with the
geographic SRID. This cast simply copies coordinates without any further transformation. For
example:

```
SELECT ST_AsEWKT(ST_GeomFromEWKT('SRID=4326;POINT(10 20)')::geography);
```

```
st_asewkt
------------------------
 SRID=4326;POINT(10 20)
```

To better understand the difference between `GEOMETRY` and
`GEOGRAPHY` data types, consider calculating the distance between the Berlin
airport (BER) and the San Francisco airport (SFO) using the World Geodetic System (WGS) 84.
Using the `GEOGRAPHY` data type, the result is in meters. When using
`GEOMETRY` data type with SRID 4326, the result is in degrees, which can’t
convert to meters because the distance of one degree depends on where on the globe geometries
are located.

Calculations on the `GEOGRAPHY` data type are mostly used for realistic round
earth calculations such as the precise area of a country without distortion. But they are far
more expensive to compute. Therefore, ST_Transform can transform your coordinates to an
appropriate local projected coordinate system and do the calculation on the
`GEOMETRY` data type faster.

Using spatial data, you can run queries to do the following:

- Find the distance between two points.
- Check whether one area (polygon) contains another.
- Check whether one linestring intersects another linestring or polygon.
  You can use the `GEOMETRY` data type to hold the values of spatial data. A
  `GEOMETRY` value in Amazon Redshift can define two-dimensional (2D), three-dimensional
  (3DZ), two-dimensional with a measure (3DM), and four-dimensional (4D) geometry primitive data
  types:

- A two-dimensional (2D) geometry is specified by two Cartesian coordinates (x, y) in a plane.
- A three-dimensional (3DZ) geometry is specified by three Cartesian coordinates (x, y, z) in space.
- A two-dimensional with measure (3DM) geometry is specified by three coordinates (x, y, m),
  where the first two are Cartesian coordinates in a plane and the third is a measurement.
- A four-dimensional (4D) geometry is specified by four coordinates (x, y, z, m),
  where the first three are Cartesian coordinates in a space and the fourth is a measurement.
  For more information about geometry primitive data types, see [Well-known
  text representation of geometry](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry "https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry") in Wikipedia.

You can use the `GEOGRAPHY` data type to hold the values of spatial data. A
`GEOGRAPHY` value in Amazon Redshift can define two-dimensional (2D), three-dimensional
(3DZ), two-dimensional with a measure (3DM), and four-dimensional (4D) geometry primitive data
types:

- A two-dimensional (2D) geometry is specified by longitude and latitude coordinates on a spheroid.
- A three-dimensional (3DZ) geometry is specified by longitude, latitude, and altitude coordinates on a spheroid.
- A two-dimensional with measure (3DM) geometry is specified by three coordinates
  (longitude, latitude, measure), where the first two are angular coordinates on a sphere
  and the third is a measurement.
- A four-dimensional (4D) geometry is specified by four coordinates (longitude, latitude, altitude, measure),
  where the first three are longitude, latitude and altitude, and the fourth is a measurement.
  For more information about geographic coordinate systems, see [Geographic coordinate system](https://en.wikipedia.org/wiki/Geographic_coordinate_system "https://en.wikipedia.org/wiki/Geographic_coordinate_system")
  and
  [Spherical coordinate system](https://en.wikipedia.org/wiki/Spherical_coordinate_system "https://en.wikipedia.org/wiki/Spherical_coordinate_system")
  in Wikipedia.

The `GEOMETRY` and `GEOGRAPHY` data types have the following subtypes:

- `POINT`
- `LINESTRING`
- `POLYGON`
- `MULTIPOINT`
- `MULTILINESTRING`
- `MULTIPOLYGON`
- `GEOMETRYCOLLECTION`
  There are Amazon Redshift SQL functions that support the following representations of geometric data:

- GeoJSON
- Well-known text (WKT)
- Extended well-known text (EWKT)
- Well-known binary (WKB) representation
- Extended well-known binary (EWKB)
  You can cast between `GEOMETRY` and `GEOGRAPHY` data types.

The following SQL casts a linestring from a `GEOMETRY` to a `GEOGRAPHY`.

```
SELECT ST_AsEWKT(ST_GeomFromText('LINESTRING(110 40, 2 3, -10 80, -7 9)')::geography);
```

```

 st_asewkt
----------------------------------------------
 SRID=4326;LINESTRING(110 40,2 3,-10 80,-7 9)

```

The following SQL casts a linestring from a `GEOGRAPHY` to a `GEOMETRY`.

```
SELECT ST_AsEWKT(ST_GeogFromText('LINESTRING(110 40, 2 3, -10 80, -7 9)')::geometry);
```

```

 st_asewkt
----------------------------------------------
 SRID=4326;LINESTRING(110 40,2 3,-10 80,-7 9)

```

Amazon Redshift provides many SQL functions to query spatial data. Except for the
`ST_IsValid` function, spatial functions that accept a `GEOMETRY`
object as an argument expect this `GEOMETRY` object to be a valid geometry. If the
`GEOMETRY` or `GEOGRAPHY` object isn't valid, then the behavior of the spatial function is
undefined. For more information about validity, see [Geometric validity](spatial-terminology.md#spatial-terminology-validity "spatial-terminology.md#spatial-terminology-validity").

For details about SQL functions to query spatial data, see
[Spatial functions](geospatial-functions.md "geospatial-functions.md").

For details about loading spatial data, see
[Loading a column of the GEOMETRY or GEOGRAPHY data
type](copy-usage_notes-spatial-data.md "copy-usage_notes-spatial-data.md").

###### Topics

- [Tutorial: Using spatial SQL functions with Amazon Redshift](spatial-tutorial.md "spatial-tutorial.md")
- [Loading a shapefile into Amazon Redshift](spatial-copy-shapefile.md "spatial-copy-shapefile.md")
- [Terminology for Amazon Redshift spatial data](spatial-terminology.md "spatial-terminology.md")
- [Considerations when using spatial data with Amazon Redshift](spatial-limitations.md "spatial-limitations.md")
