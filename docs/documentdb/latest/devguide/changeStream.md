

# $changeStream
<a name="changeStream"></a>

Not supported by Elastic cluster.

The `$changeStream` aggregation stage opens a change stream cursor to monitor real-time changes to a collection. It returns change event documents when insert, update, replace, or delete operations occur.

**Parameters**
+ `fullDocument`: Specifies whether to return the full document for update operations. Options are `default` or `updateLookup`.
+ `resumeAfter`: Optional. Resume token to continue from a specific point in the change stream.
+ `startAtOperationTime`: Optional. Timestamp to start the change stream from.
+ `allChangesForCluster`: Optional. Boolean value. When `true`, watches all changes across the cluster (for admin database). When `false` (default), watches only the specified collection.

## Example (MongoDB Shell)
<a name="changeStream-examples"></a>

The following example demonstrates using the `$changeStream` stage to monitor changes to a collection.

**Query example**

```
// Open change stream first
const changeStream = db.inventory.aggregate([
  { $changeStream: { fullDocument: "updateLookup" } }
]);

// In another session, insert a document
db.inventory.insertOne({ _id: 1, item: "Widget", qty: 10 });

// Back in the first session, read the change event
if (changeStream.hasNext()) {
  print(tojson(changeStream.next()));
}
```

**Output**

```
{
  _id: { _data: '...' },
  operationType: 'insert',
  clusterTime: Timestamp(1, 1234567890),
  fullDocument: { _id: 1, item: 'Widget', qty: 10 },
  ns: { db: 'test', coll: 'inventory' },
  documentKey: { _id: 1 }
}
```

## Code examples
<a name="changeStream-code"></a>

To view a code example for using the `$changeStream` aggregation stage, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('inventory');

  // Open change stream
  const changeStream = collection.watch([]);

  changeStream.on('change', (change) => {
    console.log('Change detected:', change);
  });

  // Simulate insert in another operation
  setTimeout(async () => {
    await collection.insertOne({ _id: 1, item: 'Widget', qty: 10 });
  }, 1000);

  // Keep connection open to receive changes
  // In production, handle cleanup appropriately
}

example();
```

------
#### [ Python ]

```
from pymongo import MongoClient
import threading
import time

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['inventory']

    # Open change stream
    change_stream = collection.watch([])

    # Insert document in separate thread after delay
    def insert_doc():
        time.sleep(1)
        collection.insert_one({'_id': 1, 'item': 'Widget', 'qty': 10})

    threading.Thread(target=insert_doc).start()

    # Watch for changes
    for change in change_stream:
        print('Change detected:', change)
        break  # Exit after first change

    client.close()

example()
```

------