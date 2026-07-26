# $bitAnd

New from version 8.0.1.

The `$bitAnd` operator in Amazon DocumentDB performs a bitwise AND operation on integer or long values.

**Parameters**

- `expressions`: An array of two or more expressions, which can resolve to integers or longs.

## Example (MongoDB Shell)

The following example shows how to use the `$bitAnd` operator to perform bitwise AND on two fields.

**Create sample documents**

```
db.flags.insertMany([
  {_id: 1, a: 13, b: 10},
  {_id: 2, a: 7, b: 5},
  {_id: 3, a: 15, b: 9}
]);
```

**Query example**

```
db.flags.aggregate([
  { $project: { result: { $bitAnd: ["$a", "$b"] } } }
]);
```

**Output**

```
[
  {_id: 1, result: 8},
  {_id: 2, result: 5},
  {_id: 3, result: 9}
]
```

In binary: 13 (1101) AND 10 (1010) = 8 (1000); 7 (0111) AND 5 (0101) = 5 (0101); 15 (1111) AND 9 (1001) = 9 (1001).

## Code examples

To view a code example for using the `$bitAnd` operator, choose the tab for the language that you want to use:

Node.js

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  try {
    await client.connect();
    const db = client.db('test');
    const collection = db.collection('flags');
    const result = await collection.aggregate([
      { $project: { result: { $bitAnd: ["$a", "$b"] } } }
    ]).toArray();
    console.log(result);
  } finally {
    await client.close();
  }
}
example();
```

Python

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    try:
        db = client['test']
        collection = db['flags']
        result = list(collection.aggregate([
            {'$project': {'result': {'$bitAnd': ['$a', '$b']}}}
        ]))
        print(result)
    finally:
        client.close()

example()
```
