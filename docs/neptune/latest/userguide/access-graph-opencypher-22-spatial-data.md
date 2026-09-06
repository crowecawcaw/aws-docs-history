

# Spatial Data
<a name="access-graph-opencypher-22-spatial-data"></a>

Amazon Neptune now supports spatial queries, allowing you to store and analyze geometric data in your graph. While commonly used for geographic locations (like coordinates on a map), spatial features work with any two-dimensional data where position and proximity matter. Use this feature to answer questions like "Which stores are within 5 miles of this customer?", "Find all delivery routes that intersect with this service area," or "Which components in this floor plan overlap with the HVAC zone?" Neptune implements spatial support using industry-standard Spatial Types functions that work with points, polygons, and other geometric shapes. You can store spatial data as properties on nodes and edges, then use spatial functions to calculate distances, check if points fall within boundaries, or find overlapping regions, all within your openCypher queries.

**Common use cases**:
+ **Geographic applications**: Location-based recommendations, geofencing, route planning, and territory analysis
+ **Facility and space management**: Floor plan layouts, equipment placement, and zone coverage
+ **Network topology**: Physical infrastructure mapping, coverage areas, and service boundaries
+ **Design and CAD**: Component positioning, collision detection, and spatial relationships in 2D designs
+ **Game development**: Character positioning, collision detection, and area-of-effect calculations

The Spatial Types implementation in Amazon Neptune follows the ISO/IEC 13249-3:2016 directives, like other databases. The [Spatial Functions](access-graph-opencypher-22-spatial-functions.md) are available in the openCypher query language.

## Coordinate system
<a name="access-graph-opencypher-22-spatial-data-coordinate-system"></a>

Neptune has one Spatial Reference Identifier (SRID) for an entire database. Homogeneity of the coordinate system reduce user errors in querying and improves the database performance. The first release (1.4.7.0) supports the Cartesian coordinate system, also referred as SRID 0.

The Neptune implementation of SRID 0 is compatible with longitude and latitude values. Use `ST_DistanceSpheroid` to calculate distances based on WGS84/SRID 4326.

The current implementation supports storing 3-dimensional coordinates. The Spatial Functions currently only support using the x- and y-axis (2-dimensional) coordinates. The z-axis coordinates are currently not supported by the available Spatial Functions.

## Storing location data
<a name="storing-spatial-data"></a>

Store location data on nodes and edges using the Geometry property type. Create Geometry values from Well-Known Text (WKT) format, a standard way to represent geographic shapes as text. For example, to store a point location:

```
CREATE (n:airport {code: 'ATL', location: ST_GeomFromText('POINT (-84.4281 33.6367)')})
```

When working with geographic coordinates, the first argument (x) represents longitude and the second argument (y) represents latitude. This follows the standard coordinate order used in spatial databases and the ISO 19125 standard.

**Note**  
 Neptune now supports a new data type called "Geometry". The Geometry property of a node or an edge can be created from a WKT string using the `ST_GeomFromText` function.  
Neptune will automatically store Points data in a specialized spatial index to improve the performance of the Spatial Types functions. For instance, `ST_Contains` used to find the points within a polygon is accelerated by the specialized spatial index.  
[ Wikipedia page for Well-Known Text representation of geometry ](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)

## Loading spatial data in bulk
<a name="loading-spatial-data-bulk"></a>

When bulk loading data, specify the Geometry type in your CSV header. Neptune will parse WKT strings and create the appropriate Geometry properties:

```
:ID,:LABEL,code:String,city:String,location:Geometry
21,airport,ATL,Atlanta,POINT (-84.42810059 33.63669968)
32,airport,ANC,Anchorage,POINT (-149.9960022 61.17440033)
43,airport,AUS,Austin,POINT (-97.66989899 30.19449997)
```

For complete CSV format details, see [openCypher bulk load format](bulk-load-tutorial-format-opencypher.md).

## Querying spatial data
<a name="querying-spatial-data"></a>

The following query examples use the [air-routes dataset](https://github.com/krlawrence/graph/tree/main/sample-data) to demonstrate how to use Spatial Functions in Neptune.

If your data has separate latitude and longitude properties instead of a Geometry property, you can convert them to points at query time. Find the 10 nearest airports to a given location:

```
MATCH (a:airport)
WITH a, ST_GeomFromText('POINT (' + a.lon + ' ' + a.lat + ')') AS airportLocation
WITH a, airportLocation, ST_Distance(ST_GeomFromText('POINT (-84.4281 33.6367)'), airportLocation) AS distance
WHERE distance IS NOT NULL
RETURN a.code, a.city, distance
ORDER BY distance ASC
LIMIT 10
```

If you already have locations stored as `ST_Point` then you can use those location values directly:

1. Set the property

   ```
   MATCH (a:airport)
   SET a.location = ST_GeomFromText('POINT (' + a.lon + ' ' + a.lat + ')')
   ```

1. Query using ST\_Distance:

   ```
   MATCH (a:airport)
   WHERE a.location IS NOT NULL
   WITH a, ST_Distance(ST_GeomFromText('POINT (-84.4281 33.6367)'), a.location) AS distance
   RETURN a.code, a.city, distance
   ORDER BY distance ASC
   LIMIT 10
   ```

### Using the Bolt driver
<a name="querying-spatial-data-bolt"></a>

Most query methods return Geometry values as WKT strings, which are human-readable. If you're using the Bolt driver, Geometry values are returned in WKB (Well-Known Binary) format for efficiency. Convert WKB to a Geometry object in your application:

```
try (Session session = driver.session()) {
    Result result = session.run("MATCH (n:airport {code: 'ATL'}) RETURN n.location as geom");
    
    Record record = result.single();
    byte[] wkbBytes = record.get("geom").asByteArray();
    
    // Convert WKB to Geometry object using JTS library
    WKBReader wkbReader = new WKBReader();
    Geometry geom = wkbReader.read(wkbBytes);
}
```