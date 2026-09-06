

# $geoNear
<a name="geoNear"></a>

The `$geoNear` aggregation stage returns documents in order of proximity to a specified point. It calculates the distance from the point and includes the distance in the output documents.

**Parameters**
+ `near`: The point from which to calculate distances, specified as GeoJSON or legacy coordinates.
+ `distanceField`: The field name to store the calculated distance.
+ `spherical`: Boolean indicating whether to use spherical geometry (required for GeoJSON points).
+ `maxDistance`: Optional. Maximum distance from the center point.
+ `minDistance`: Optional. Minimum distance from the center point.
+ `query`: Optional. Additional filter criteria to apply.
+ `limit`: Optional. Maximum number of documents to return.
+ `key`: Optional. Field to use for geospatial query when multiple geospatial indexes exist.

## Example (MongoDB Shell)
<a name="geoNear-examples"></a>

The following example demonstrates using the `$geoNear` stage to find stores nearest to a given location.

**Create sample documents**

```
db.stores.createIndex({ location: "2dsphere" });

db.stores.insertMany([
  { _id: 1, name: "Store A", location: { type: "Point", coordinates: [-122.4, 37.8] } },
  { _id: 2, name: "Store B", location: { type: "Point", coordinates: [-122.5, 37.7] } },
  { _id: 3, name: "Store C", location: { type: "Point", coordinates: [-122.3, 37.9] } }
]);
```

**Query example**

```
db.stores.aggregate([
  {
    $geoNear: {
      near: { type: "Point", coordinates: [-122.4, 37.8] },
      distanceField: "distance",
      spherical: true
    }
  }
]);
```

**Output**

```
[
  { _id: 1, name: 'Store A', location: { type: 'Point', coordinates: [ -122.4, 37.8 ] }, distance: 0 },
  { _id: 3, name: 'Store C', location: { type: 'Point', coordinates: [ -122.3, 37.9 ] }, distance: 13877.82 },
  { _id: 2, name: 'Store B', location: { type: 'Point', coordinates: [ -122.5, 37.7 ] }, distance: 15557.89 }
]
```

## Code examples
<a name="geoNear-code"></a>

To view a code example for using the `$geoNear` aggregation stage, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('stores');

  const result = await collection.aggregate([
    {
      $geoNear: {
        near: { type: "Point", coordinates: [-122.4, 37.8] },
        distanceField: "distance",
        spherical: true
      }
    }
  ]).toArray();

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
    collection = db['stores']

    result = list(collection.aggregate([
        {
            '$geoNear': {
                'near': { 'type': 'Point', 'coordinates': [-122.4, 37.8] },
                'distanceField': 'distance',
                'spherical': True
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------