# $count (accumulator)

New from version 8.0.1.

Use the `$count` accumulator within a `$group` stage to return the number of documents in each group. It accepts an empty object `{}` as its argument.

This is different from the `$count` pipeline stage, which is a standalone stage that counts all documents passing through the pipeline. The `$count` accumulator instead counts documents within each group produced by `$group`.

**Syntax**

```
{ $count: {} }
```

**Parameters**

- The `$count` accumulator takes no arguments. It accepts an empty object `{}` and returns the count of documents in each group.

## Example (MongoDB Shell)

The following example demonstrates how to use the `$count` accumulator to count the number of products in each category.

**Create sample documents**

```
db.products.insertMany([
  { name: "Widget", category: "A" },
  { name: "Gadget", category: "A" },
  { name: "Doohickey", category: "B" },
  { name: "Thingamajig", category: "B" },
  { name: "Whatsit", category: "B" }
])
```

**Query example**

```
db.products.aggregate([
  { $group: { _id: "$category", count: { $count: {} } } }
])
```

**Output**

```
[
  { "_id": "A", "count": 2 },
  { "_id": "B", "count": 3 }
]
```

## Code examples

To view a code example for using the `$count` accumulator, choose the tab for the language that you want to use:

Node.js

```
const { MongoClient } = require('mongodb');

async function example() {
  const uri = 'mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false';
  const client = new MongoClient(uri);

  try {
    await client.connect();

    const db = client.db('test');
    const collection = db.collection('products');

    const result = await collection.aggregate([
      { $group: { _id: "$category", count: { $count: {} } } }
    ]).toArray();

    console.log(result);

  } catch (error) {
    console.error('Error:', error);
  } finally {
    await client.close();
  }
}

example();
```

Python

```
from pymongo import MongoClient
from pprint import pprint

def example():
    client = None
    try:
        client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

        db = client['test']
        collection = db['products']

        result = list(collection.aggregate([
            { '$group': { '_id': '$category', 'count': { '$count': {} } } }
        ]))

        pprint(result)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if client:
            client.close()

example()
```
