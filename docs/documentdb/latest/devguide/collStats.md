

# $collStats
<a name="collStats"></a>

New from version 4.0

The `$collStats` aggregation stage in Amazon DocumentDB provides statistics about the specified collection, similar to the `db.collection.stats()` command in the MongoDB shell. This stage can be used to retrieve information about the collection, such as the number of documents, the total size of the collection, and various performance metrics.

**Parameters**
+ `latencyStats`: (optional) A document that specifies the options for collecting latency statistics. This parameter is not supported in Amazon DocumentDB.
+ `recordStats`: (optional) A document that specifies the options for collecting record statistics. This parameter is not supported in Amazon DocumentDB.
+ `queryExecStats`: (optional) A document that specifies the options for collecting query execution statistics. This parameter is not supported in Amazon DocumentDB.

## Example (MongoDB Shell)
<a name="collStats-examples"></a>

The following example demonstrates how to use the `$collStats` aggregation stage to retrieve statistics about a collection named `test` in the `db` database.

**Create sample documents**

```
db.test.insertMany([
  { "name": "John", "age": 30 },
  { "name": "Jane", "age": 25 },
  { "name": "Bob", "age": 35 }
]);
```

**Query example**

```
db.test.aggregate([
  { $collStats: {} }
]);
```

**Output**

```
{
  "ns" : "db.test",
  "count" : 3,
  "size" : 87,
  "avgObjSize" : 29,
  "storageSize" : 40960,
  "capped" : false,
  "nindexes" : 1,
  "totalIndexSize" : 8192,
  "indexSizes" : {
    "_id_" : 8192
  },
  "collScans" : 0,
  "idxScans" : 0,
  "opCounter" : {
    "numDocsIns" : 3,
    "numDocsUpd" : 0,
    "numDocsDel" : 0
  },
  "cacheStats" : {
    "collBlksHit" : 0,
    "collBlksRead" : 0,
    "collHitRatio" : 0,
    "idxBlksHit" : 0,
    "idxBlksRead" : 0,
    "idxHitRatio" : 0
  },
  "lastReset" : "2023-04-11T12:00:00Z",
  "ok" : 1,
  "operationTime" : Timestamp(1681206000, 1)
}
```

## Code examples
<a name="collStats-code"></a>

To view a code example for using the `$collStats` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

Here's an example of how to use the `$collStats` aggregation stage in a Node.js application using the official MongoDB Node.js driver:

```
const { MongoClient } = require('mongodb');

async function runCollStatsExample() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('db');
  const collection = db.collection('test');

  const result = await collection.aggregate([
    { $collStats: {} }
  ]).toArray();

  console.log(result);

  await client.close();
}

runCollStatsExample();
```

------
#### [ Python ]

Here's an example of how to use the `$collStats` aggregation stage in a Python application using the PyMongo driver:

```
from pymongo import MongoClient

def run_coll_stats_example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['db']
    collection = db['test']

    result = list(collection.aggregate([
        { '$collStats': {} }
    ]))

    print(result)

    client.close()

run_coll_stats_example()
```

------