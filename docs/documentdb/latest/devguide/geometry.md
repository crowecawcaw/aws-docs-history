

# $geometry
<a name="geometry"></a>

The `$geometry` operator in Amazon DocumentDB is used to specify a GeoJSON geometry object as part of a geospatial query. This operator is used in conjunction with other geospatial query operators like `$geoWithin` and `$geoIntersects` to perform spatial queries on your data.

In Amazon DocumentDB, the `$geometry` operator supports the following GeoJSON geometry types:
+ Point
+ LineString
+ Polygon
+ MultiPoint
+ MultiLineString
+ MultiPolygon
+ GeometryCollection

**Parameters**
+ `type`: The type of the GeoJSON geometry object, e.g., `Point`, `Polygon`, etc.
+ `coordinates`: An array of coordinates representing the geometry. The structure of the coordinates array depends on the geometry type.

## Example (MongoDB Shell)
<a name="geometry-examples"></a>

The following example demonstrates how to use the `$geometry` operator to perform a `$geoIntersects` query in Amazon DocumentDB.

**Create sample documents**

```
db.locations.insertMany([
  { 
    "_id": 1,
    "name": "Location 1",
    "location": { 
      "type": "Point",
      "coordinates": [-73.983253, 40.753941]
    }
  },
  { 
    "_id": 2,
    "name": "Location 2", 
    "location": {
      "type": "Polygon",
      "coordinates": [[
        [-73.998427, 40.730309],
        [-73.954348, 40.730309],
        [-73.954348, 40.780816],
        [-73.998427, 40.780816],
        [-73.998427, 40.730309]
      ]]
    }
  }
]);
```

**Query example**

```
db.locations.find({
  "location": {
    "$geoIntersects": {
      "$geometry": {
        "type": "Polygon",
        "coordinates": [[
          [-73.998, 40.730],
          [-73.954, 40.730],
          [-73.954, 40.781],
          [-73.998, 40.781],
          [-73.998, 40.730]
        ]]
      }
    }
  }
})
```

**Output**

```
[
  {
    "_id": 2,
    "name": "Location 2",
    "location": {
      "type": "Polygon",
      "coordinates": [
        [
          [-73.998427, 40.730309],
          [-73.954348, 40.730309],
          [-73.954348, 40.780816],
          [-73.998427, 40.780816],
          [-73.998427, 40.730309]
        ]
      ]
    }
  }
]
```

## Code examples
<a name="geometry-code"></a>

To view a code example for using the `$geometry` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('locations');

  const query = {
    "location": {
      "$geoIntersects": {
        "$geometry": {
          "type": "Polygon",
          "coordinates": [[
            [-73.998, 40.730],
            [-73.954, 40.730],
            [-73.954, 40.781],
            [-73.998, 40.781],
            [-73.998, 40.730]
          ]]
        }
      }
    }
  };

  const result = await collection.find(query).toArray();
  console.log(result);

  await client.close();
}

example();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['locations']

    query = {
        "location": {
            "$geoIntersects": {
                "$geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [-73.998, 40.730],
                        [-73.954, 40.730],
                        [-73.954, 40.781],
                        [-73.998, 40.781],
                        [-73.998, 40.730]
                    ]]
                }
            }
        }
    }

    result = list(collection.find(query))
    print(result)

    client.close()

example()
```

------