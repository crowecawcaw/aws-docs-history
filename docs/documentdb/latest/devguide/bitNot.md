# $bitNot

New from version 8.0.1.

The `$bitNot` operator in Amazon DocumentDB performs a bitwise NOT operation on an integer or long value, returning the bitwise complement. For a given integer or long n, the result is -(n+1).

**Parameters**

- `expression`: An expression that resolves to an integer or long. Returns the bitwise complement, which is -(n+1) for a given integer or long n.

## Example (MongoDB Shell)

The following example demonstrates how to use the `$bitNot` operator to compute the bitwise complement of integer values.

**Create sample documents**

```
db.numbers.insertMany([
  {_id: 1, value: 0},
  {_id: 2, value: 5},
  {_id: 3, value: -3}
]);
```

**Query example**

```
db.numbers.aggregate([
  { $project: { result: { $bitNot: "$value" } } }
]);
```

**Output**

```
[
  {_id: 1, result: -1},
  {_id: 2, result: -6},
  {_id: 3, result: 2}
]
```

In binary: NOT 0 = -1; NOT 5 = -6; NOT -3 = 2.

## Code examples

To view a code example for using the `$bitNot` operator, choose the tab for the language that you want to use:

Node.js

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  try {
    await client.connect();
    const db = client.db('test');
    const collection = db.collection('numbers');
    const result = await collection.aggregate([
      { $project: { result: { $bitNot: "$value" } } }
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
        collection = db['numbers']
        result = list(collection.aggregate([
            {'$project': {'result': {'$bitNot': '$value'}}}
        ]))
        print(result)
    finally:
        client.close()

example()
```
