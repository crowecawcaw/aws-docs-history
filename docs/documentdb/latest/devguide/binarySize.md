# $binarySize

New from version 8.0.1.

The `$binarySize` operator in Amazon DocumentDB returns the size in bytes of a given string or binary data value.
For string values, this is the UTF-8 encoded byte count, not the character count.
Multi-byte UTF-8 characters (such as accented characters or CJK characters) will produce a byte count larger than the number of characters in the string.

**Parameters**

- `expression`: An expression that resolves to a string or binary data value.

## Example (MongoDB Shell)

The following example shows how to use the `$binarySize` operator to return the byte size of string fields.

**Create sample documents**

```
db.docs.insertMany([
  {_id: 1, content: "hello"},
  {_id: 2, content: "Amazon DocumentDB"},
  {_id: 3, content: ""}
]);
```

**Query example**

```
db.docs.aggregate([
  { $project: { size: { $binarySize: "$content" } } }
]);
```

**Output**

```
[
  {_id: 1, size: 5},
  {_id: 2, size: 17},
  {_id: 3, size: 0}
]
```

## Code examples

To view a code example for using the `$binarySize` operator, choose the tab for the language that you want to use:

Node.js

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  try {
    await client.connect();
    const db = client.db('test');
    const collection = db.collection('docs');
    const result = await collection.aggregate([
      { $project: { size: { $binarySize: "$content" } } }
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
        collection = db['docs']
        result = list(collection.aggregate([
            {'$project': {'size': {'$binarySize': '$content'}}}
        ]))
        print(result)
    finally:
        client.close()

example()
```
