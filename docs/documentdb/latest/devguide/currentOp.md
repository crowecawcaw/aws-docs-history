

# $currentOp
<a name="currentOp"></a>

The `$currentOp` aggregation stage returns information about currently running operations in the database. This stage is useful for monitoring active queries and operations in an aggregation pipeline.

**Parameters**
+ `allUsers` (optional): When set to `true`, returns operations for all users. Default is `false`.
+ `idleConnections` (optional): When set to `true`, includes idle connections. Default is `false`.
+ `idleCursors` (optional): When set to `true`, includes information about idle cursors. Default is `false`.
+ `idleSessions` (optional): When set to `true`, includes information about idle sessions. Default is `true`.
+ `localOps` (optional): When set to `true`, includes local operations. Default is `false`.

## Example (MongoDB Shell)
<a name="currentOp-examples"></a>

The following example demonstrates using the `$currentOp` aggregation stage to retrieve information about active read operations.

**Query example**

```
db.aggregate([
  { $currentOp: { allUsers: true, idleConnections: false } },
  { $match: { op: "query" } }
])
```

**Output**

```
[
  {
    "opid": "12345",
    "active": true,
    "op": "query",
    "ns": "test.users",
    "secs_running": 2
  }
]
```

## Code examples
<a name="currentOp-code"></a>

To view a code example for using the `$currentOp` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('admin');

  const result = await db.aggregate([
    { $currentOp: { allUsers: true, idleConnections: false } },
    { $match: { op: "query" } }
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
    db = client['admin']

    result = list(db.aggregate([
        { '$currentOp': { 'allUsers': True, 'idleConnections': False } },
        { '$match': { 'op': 'query' } }
    ]))

    print(result)
    client.close()

example()
```

------