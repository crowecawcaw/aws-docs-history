

# $setIntersection
<a name="setIntersection"></a>

The `$setIntersection` operator in Amazon DocumentDB is used to return the common elements between two or more arrays. This operator is particularly useful when working with sets of data, allowing you to find the intersection of multiple sets.

**Parameters**
+ `array1`: The first array to intersect.
+ `array2`: The second array to intersect.
+ `arrayN`: (optional) Additional arrays to intersect.

## Example (MongoDB Shell)
<a name="setIntersection-examples"></a>

The following example demonstrates how to use the `$setIntersection` operator to find the common elements between two arrays.

**Create sample documents**

```
db.collection.insertMany([
  { _id: 1, colors: ["red", "blue", "green"] },
  { _id: 2, colors: ["blue", "yellow", "orange"] },
  { _id: 3, colors: ["red", "green", "purple"] }
])
```

**Query example**

```
db.collection.aggregate([
  { $project: {
      _id: 1,
      commonColors: { $setIntersection: ["$colors", ["red", "blue", "green"]] }
    }
  }
])
```

**Output**

```
[
  { "_id": 1, "commonColors": ["red", "blue", "green"] },
  { "_id": 2, "commonColors": ["blue"] },
  { "_id": 3, "commonColors": ["red", "green"] }
]
```

## Code examples
<a name="setIntersection-code"></a>

To view a code example for using the `$setIntersection` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('mycollection');

  const result = await collection.aggregate([
    {
      $project: {
        _id: 1,
        commonColors: { $setIntersection: ["$colors", ["red", "blue", "green"]] }
      }
    }
  ]).toArray();

  console.log(result);
  client.close();
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
    collection = db['mycollection']

    result = list(collection.aggregate([
        {
            '$project': {
                '_id': 1,
                'commonColors': { '$setIntersection': ["$colors", ["red", "blue", "green"]] }
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------