

# $map
<a name="map"></a>

The `$map` operator in Amazon DocumentDB allows you to apply a specified expression to each element in an array and return a new array with the transformed elements. This operator is particularly useful for manipulating and transforming data within arrays, which can help simplify your application code and improve query performance by pushing the array processing to the database level.

**Parameters**
+ `input`: The array to be transformed.
+ `as`: (optional) The name of the variable to be used within the in expression to represent the current element being processed.
+ `in`: The expression to be applied to each element in the input array.

## Example (MongoDB Shell)
<a name="map-examples"></a>

The following example demonstrates how to use the $map operator to transform an array of numbers, doubling each value.

**Create sample documents**

```
db.collection.insertMany([
  { _id: 1, numbers: [1, 2, 3, 4, 5] },
  { _id: 2, numbers: [10, 20, 30, 40, 50] }
])
```

**Query example**

```
db.collection.aggregate([
  {
    $project: {
      doubledNumbers: { $map: { input: "$numbers", as: "num", in: { $multiply: ["$$num", 2] } } }
    }
  }
])
```

**Output**

```
[
  { _id: 1, doubledNumbers: [2, 4, 6, 8, 10] },
  { _id: 2, doubledNumbers: [20, 40, 60, 80, 100] }
]
```

## Code examples
<a name="map-code"></a>

To view a code example for using the `$map` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('collection');

  const result = await collection.aggregate([
    {
      $project: {
        doubledNumbers: { $map: { input: "$numbers", as: "num", in: { $multiply: ["$$num", 2] } } }
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
    db = client.test
    collection = db.collection

    result = list(collection.aggregate([
        {
            '$project': {
                'doubledNumbers': { '$map': { 'input': '$numbers', 'as': 'num', 'in': { '$multiply': ['$$num', 2] } } }
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------