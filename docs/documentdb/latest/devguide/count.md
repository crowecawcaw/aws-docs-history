# $count (stage)

The `$count` aggregation stage in Amazon DocumentDB is used to count the number of documents that pass into the stage. It is often used as the final stage in an aggregation pipeline to return the total count of documents matching the previous stages.

**Parameters**

- `field`: The field to count. This parameter is optional, and if not provided, the stage will count the total number of input documents.

## Example (MongoDB Shell)

The following example demonstrates how to use the `$count` stage to get the total number of documents in a collection.

**Create sample documents**

```
db.users.insertMany([
  { name: "John", age: 30 },
  { name: "Jane", age: 25 },
  { name: "Bob", age: 35 },
  { name: "Alice", age: 28 }
]);
```

**Query example**

```
db.users.aggregate([
  { $count: "total" }
]);
```

**Output**

```
{ "total" : 4 }
```

The example aggregates the `users` collection and uses the `$count` stage to count the total number of documents.

## Code examples

To view a code example for using the `$count` command, choose the tab for the language that you want to use:

Node.js

```
const { MongoClient } = require('mongodb');

async function countDocuments() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('mydb');
  const collection = db.collection('users');

  const result = await collection.aggregate([
    { $count: "total" }
  ]).toArray();

  console.log(result[0].total);

  await client.close();
}

countDocuments();
```

Python

```
from pymongo import MongoClient

def count_documents():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['mydb']
    collection = db['users']

    result = list(collection.aggregate([
        { '$count': "total" }
    ]))

    print(result[0]['total'])

    client.close()

count_documents()
```
