

# $listSearchIndexes
<a name="listSearchIndexes"></a>

New from version 8.0.1.

The `$listSearchIndexes` aggregation stage in Amazon DocumentDB returns information about existing search indexes on a collection. It must be the first stage in an aggregation pipeline.

**Parameters**
+ `name`: (optional) The name of the search index to return information about. If omitted, all search indexes on the collection are returned.

**Output fields**

Each returned document contains the following fields:
+ `name`: The name of the search index.
+ `status`: The build state of the index. One of `READY` (built and valid), `BUILDING` (a concurrent build is in progress), or `FAILED` (the index build did not complete successfully).
+ `queryable`: A boolean indicating whether the index can currently be used to serve queries. This is `false` for hidden indexes (which remain `READY`) and for `FAILED` indexes. A hidden index is the case where `status` is `READY` but `queryable` is `false`.
+ `latestDefinitionVersion`: A document containing `version` (the index format version) and `createdAt` (the time the index was created).

**Syntax**

```
db.collection.aggregate([
  { $listSearchIndexes: {} }
])

// Or filter by name:
db.collection.aggregate([
  { $listSearchIndexes: { name: "mySearchIndex" } }
])
```

## Example (MongoDB Shell)
<a name="listSearchIndexes-examples"></a>

The following example shows how to use the `$listSearchIndexes` stage to list all search indexes on a collection.

**Query example**

```
db.movies.aggregate([
  { $listSearchIndexes: {} }
]);
```

**Output**

```
[
  {
    "name": "default",
    "status": "READY",
    "queryable": true,
    "latestDefinitionVersion": {
      "version": 2,
      "createdAt": ISODate("2026-05-11T21:12:57.974Z")
    }
  }
]
```

A hidden index remains `READY` but reports `queryable: false`, because it cannot be used to serve queries while hidden:

```
[
  {
    "name": "myHiddenIndex",
    "status": "READY",
    "queryable": false,
    "latestDefinitionVersion": {
      "version": 2,
      "createdAt": ISODate("2026-05-11T21:12:57.974Z")
    }
  }
]
```

To filter by a specific index name:

```
db.movies.aggregate([
  { $listSearchIndexes: { name: "default" } }
]);
```

## Code examples
<a name="listSearchIndexes-code"></a>

To view a code example for using the `$listSearchIndexes` stage, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  try {
    await client.connect();
    const db = client.db('test');
    const collection = db.collection('movies');

    // List all search indexes
    const allIndexes = await collection.aggregate([
      { $listSearchIndexes: {} }
    ]).toArray();
    console.log('All search indexes:', allIndexes);

    // List a specific search index by name
    const namedIndex = await collection.aggregate([
      { $listSearchIndexes: { name: "default" } }
    ]).toArray();
    console.log('Named index:', namedIndex);

  } finally {
    await client.close();
  }
}

example();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

    try:
        db = client['test']
        collection = db['movies']

        # List all search indexes
        all_indexes = list(collection.aggregate([
            { '$listSearchIndexes': {} }
        ]))
        print('All search indexes:', all_indexes)

        # List a specific search index by name
        named_index = list(collection.aggregate([
            { '$listSearchIndexes': { 'name': 'default' } }
        ]))
        print('Named index:', named_index)

    finally:
        client.close()

example()
```

------