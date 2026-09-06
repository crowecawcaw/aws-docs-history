

# $sampleRate
<a name="sampleRate"></a>

New from version 8.0.1.

Not supported by Elastic cluster.

The `$sampleRate` operator in Amazon DocumentDB matches a random sample of the input documents based on the specified rate. You can use it in a `find()` query filter or in an aggregation `$match` stage. Because selection is probabilistic, the number of documents returned is approximate and can vary between runs.

**Parameters**
+ `value`: A number in the range `[0, 1]` (inclusive), passed directly to the operator (for example, `{ $sampleRate: 0.3 }`), that sets the probability of including each document. A value of `0` returns no documents; a value of `1` returns all documents.

## Example (MongoDB Shell)
<a name="sampleRate-examples"></a>

The following example uses `$sampleRate` to return approximately 30 percent of the documents in a collection.

**Create sample documents**

```
db.events.insertMany([
  { _id: 1, type: "click" },
  { _id: 2, type: "view" },
  { _id: 3, type: "click" },
  { _id: 4, type: "view" },
  { _id: 5, type: "purchase" }
]);
```

**Query example**

```
db.events.aggregate([
  { $match: { $sampleRate: 0.3 } }
]);
```

**Output**

The operation returns a random subset of the documents. Because `$sampleRate` is probabilistic, the specific documents returned and their count vary each time the query runs.

## Code examples
<a name="sampleRate-code"></a>

To view a code example for using the `$sampleRate` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const uri = 'mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false';
  const client = new MongoClient(uri);

  try {
    await client.connect();
    const db = client.db('test');
    const collection = db.collection('events');

    // Return approximately 30% of the documents
    const result = await collection.aggregate([
      { $match: { $sampleRate: 0.3 } }
    ]).toArray();

    console.log(result);
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
        collection = db['events']

        # Return approximately 30% of the documents
        result = list(collection.aggregate([
            { '$match': { '$sampleRate': 0.3 } }
        ]))

        print(result)
    finally:
        client.close()

example()
```

------