# Querying geospatial data with Amazon DocumentDB

This section covers how you can query Geospatial data with Amazon DocumentDB. After you read this
section, you will be able to answer how do store, query and index Geospatial data in
Amazon DocumentDB.

###### Topics

- [Overview](#overview "#overview")
- [Indexing and storing geospatial data](#indexing "#indexing")
- [Querying geospatial data](#querying_geospatial "#querying_geospatial")
- [Limitations](#limitations "#limitations")

## Overview

Common use cases for Geospatial involve proximity analysis from your data. For
example, “finding all airports within 50 miles of Seattle”, or “find the closest
restaurants from a given location”. Amazon DocumentDB uses the [GeoJSON specification](https://datatracker.ietf.org/doc/html/rfc7946 "https://datatracker.ietf.org/doc/html/rfc7946") to
represent geospatial data. GeoJSON is an open-source specification for the
JSON-formatting of shapes in a coordinate space. GeoJSON coordinates captures both
longitude and latitude, representing positions on an earth-like sphere.

## Indexing and storing geospatial data

Amazon DocumentDB uses the ‘Point’ GeoJSON type to store geospatial data. Each GeoJSON document
(or subdocument) is generally composed of two fields:

- **type** - the shape being represented, which informs Amazon DocumentDB
  how to interpret the "coordinates" field. At this moment, Amazon DocumentDB only supports
  points
- **coordinates** – a latitude and longitude pair represented
  as an object in an array – [longitude, latitude]

Amazon DocumentDB also uses 2dsphere indexes to index Geospatial data. Amazon DocumentDB supports indexing
points. Amazon DocumentDB supports proximity querying with 2dsphere indexing.

Let’s consider a scenario where you are building an application for food delivery
service. You want to store various restaurant’s latitudes and longitude pair in Amazon DocumentDB.
To do so, first we recommend that you create an index on the Geospatial field that holds
the latitude and longitude pair.

```
use restaurantsdb
db.usarestaurants.createIndex({location:"2dsphere"})

```

The output of this command would look something like this:

```
{
	"createdCollectionAutomatically" : true,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}
```

Once you have created an index, you can start inserting data into your Amazon DocumentDB
collection.

```
db.usarestaurants.insert({
   "state":"Washington",
   "city":"Seattle",
   "name":"Thai Palace",
   "rating": 4.8,
   "location":{
      "type":"Point",
      "coordinates":[
         -122.3264,
         47.6009
      ]
   }
});

db.usarestaurants.insert({
   "state":"Washington",
   "city":"Seattle",
   "name":"Noodle House",
   "rating": 4.8,
   "location":{
      "type":"Point",
      "coordinates":[
        -122.3517,
         47.6159
      ]
   }
});

db.usarestaurants.insert({
   "state":"Washington",
   "city":"Seattle",
   "name":"Curry House",
   "rating": 4.8,
   "location":{
      "type":"Point",
      "coordinates":[
         -121.4517,
         47.6229
      ]
   }
});
```

## Querying geospatial data

Amazon DocumentDB supports proximity, inclusion and intersection querying of Geospatial data. A
good example of a proximity query is finding all points (all airports) that are less
than a certain distance and more than a distance from another point (city). A good
example of inclusion querying is to find all points (all airports) that located in a
specified area/polygon (state of New York). A good example of intersection query is
finding a polygon (state) which intersects with a point (city). You can use the
following Geospatial operators to gain insights from your data.

- `**$nearSphere**` - `$nearSphere` is a
  find operator that supports finding points from nearest to farthest from a
  GeoJSON point.
- `**$geoNear**` - `$geoNear` is an
  aggregation operator that supports calculating the distance in meters from a
  GeoJSON point.
- `**$minDistance**` - `$minDistance` is
  a find operator that is used in conjunction with `$nearSphere` or
  `$geoNear` to filter documents that are at least at the specified
  minimum distance from the center point.
- `**$maxDistance**` - `$maxDistance` is
  a find operator that is used in conjunction with `$nearSphere` or
  `$geoNear` to filter documents that are at most at the specified
  maximum distance from the center point.
- `**$geoWithin**` - `$geoWithin` is a
  find operator that supports finding documents with geospatial data that exists
  entirely within a specified shape such as a polygon.
- `**$geoIntersects**` - `$geoIntersects`
  is a find operator that supports finding documents whose geospatial data
  intersects with a specified GeoJSON object.

###### Note

`$geoNear` and `$nearSphere` require a 2dsphere index on the
GeoJSON field that you use in your proximity query.

### Example 1

In this example, you will learn how to find all restaurants (points) sorted by
closest distance from an address (point).

To perform such a query, you can use `$geoNear` to calculate distance
of set of points from another point. You can also add the
`distanceMultiplier` to measure the distance in kilometers.

```
db.usarestaurants.aggregate([
   {
      "$geoNear":{
         "near":{
            "type":"Point",
            "coordinates":[
               -122.3516,
               47.6156
            ]
         },
         "spherical":true,
         "distanceField":"DistanceKilometers",
         "distanceMultiplier":0.001
      }
   }
])

```

The command above would return restaurants sorted by distance (closest to
furthest) from the point specified. The output of this command would look something
like this

```
{ "_id" : ObjectId("611f3da985009a81ad38e74b"), "state" : "Washington", "city" : "Seattle", "name" : "Noodle House", "rating" : 4.8, "location" : { "type" : "Point", "coordinates" : [ -122.3517, 47.6159 ] }, "DistanceKilometers" : 0.03422834547294996 }
{ "_id" : ObjectId("611f3da185009a81ad38e74a"), "state" : "Washington", "city" : "Seattle", "name" : "Thai Palace", "rating" : 4.8, "location" : { "type" : "Point", "coordinates" : [ -122.3264, 47.6009 ] }, "DistanceKilometers" : 2.5009390081704277 }
{ "_id" : ObjectId("611f3dae85009a81ad38e74c"), "state" : "Washington", "city" : "Seattle", "name" : "Curry House", "rating" : 4.8, "location" : { "type" : "Point", "coordinates" : [ -121.4517, 47.6229 ] }, "DistanceKilometers" : 67.52845344856914 }
```

To limit the number of results in a query, use the `limit` or `num` option.

`limit`:

```
db.usarestaurants.aggregate([
   {
      "$geoNear":{
         "near":{
            "type":"Point",
            "coordinates":[
               -122.3516,
               47.6156
            ]
         },
         "spherical":true,
         "distanceField":"DistanceKilometers",
         "distanceMultiplier":0.001,
         "limit": 10
      }
   }
])
```

`num`:

```
db.usarestaurants.aggregate([
   {
      "$geoNear":{
         "near":{
            "type":"Point",
            "coordinates":[
               -122.3516,
               47.6156
            ]
         },
         "spherical":true,
         "distanceField":"DistanceKilometers",
         "distanceMultiplier":0.001,
         "num": 10
      }
   }
])
```

###### Note

`$geoNear` stage supports the `limit` and `num` options to specify maximum number of documents to return.
`$geoNear` returns a maximum of 100 documents by default if the `limit` or `num` options are not specified.
This is overridden by the value of the `$limit` stage if present and the value is less than 100.

### Example 2

In this example, you will learn how to find all restaurants (points) within 2
kilometers of a specific address (point). To perform such a query, you can use
`$nearSphere` within a minimum `$minDistance` and maximum
`$maxDistance` from a GeoJSON Point

```
db.usarestaurants.find({
   "location":{
      "$nearSphere":{
         "$geometry":{
            "type":"Point",
            "coordinates":[
               -122.3516,
               47.6156
            ]
         },
         "$minDistance":1,
         "$maxDistance":2000
      }
   }
},
{
   "name":1
})
```

The command above would return restaurants at a maximum distance of 2 kilometers
from the point specified. The output of this command would look something like this

```
{ "_id" : ObjectId("611f3da985009a81ad38e74b"), "name" : "Noodle House" }
```

## Limitations

Amazon DocumentDB does not support querying or indexing of Polygons, LineString, MultiPoint,
MultiPolygon, MultiLineString, and GeometryCollection.
