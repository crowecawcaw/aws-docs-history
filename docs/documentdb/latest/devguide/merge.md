

# $merge
<a name="merge"></a>

Introduced in 8.0

The `$merge` aggregation stage in Amazon DocumentDB is used to merge the results of the previous pipeline stage into a target collection. This is useful for updating or inserting documents in a target collection based on the data from the input documents.

The `$merge` stage allows you to perform various actions based on the matching condition between the input documents and the target collection, such as:

```
- Insert new documents
- Update existing documents
- Delete documents
- Fail the operation if there are any conflicts
```

**Parameters**
+ `into`: (required) The name of the target collection to merge the input documents into.
+ `on`: (required) The field(s) to use as the matching condition between the input documents and the target collection.
+ `whenMatched`: (optional) The action to perform when the input document matches an existing document in the target collection. Supported values are: `"merge"`, `"replace"`, `"keepExisting"`, and `"fail"`.
+ `whenNotMatched`: (optional) The action to perform when the input document does not match any document in the target collection. Supported values are: `"insert"` and `"fail"`.
+ `bypassDocumentValidation`: (optional) When set to `true`, documents written to the target collection by the `$merge` stage bypass any schema validation rules (`$jsonSchema`) defined on that collection. The default is `false`, which enforces the target collection's validation rules. This is supported in Amazon DocumentDB 8.0.

## Example (MongoDB Shell)
<a name="merge-examples"></a>

The following example demonstrates how to use the `$merge` stage to update a `users` collection with new data from an input pipeline.

**Create sample documents**

```
db.users.insertMany([
  { _id: 1, name: "John Doe", email: "john@example.com" },
  { _id: 2, name: "Jane Smith", email: "jane@example.com" }
]);

db.inputData.insertMany([
  { _id: 1, name: "John Doe", email: "john@example.com", phone: "123-456-7890" },
  { _id: 3, name: "Bob Johnson", email: "bob@example.com", phone: "987-654-3210" }
]);
```

**Query example**

```
db.inputData.aggregate([
  {
    $merge: {
      into: "users",
      on: "_id",
      whenMatched: "merge",
      whenNotMatched: "insert"
    }
  }
])
```

**Output**

After running the `$merge` pipeline, the `users` collection will contain the following documents:

```
[
  { _id: 1, name: "John Doe", email: "john@example.com", phone: "123-456-7890" },
  { _id: 2, name: "Jane Smith", email: "jane@example.com" },
  { _id: 3, name: "Bob Johnson", email: "bob@example.com", phone: "987-654-3210" }
]
```

## Code examples
<a name="merge-code"></a>

To view a code example for using the `$merge` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

Here's an example of using the $merge operator in a Node.js application:

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');

  await db.collection('inputData').aggregate([
    {
      $merge: {
        into: 'users',
        on: '_id',
        whenMatched: 'merge',
        whenNotMatched: 'insert'
      }
    }
  ]).toArray();

  const users = await db.collection('users').find({}).toArray();
  console.log(users);

  await client.close();
}

example();
```

------
#### [ Python ]

Here's an example of using the $merge operator in a Python application:

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']

    # Assumes collections 'users' and 'inputData' already exist with sample data
    db.inputData.aggregate([
        {
            '$merge': {
                'into': 'users',
                'on': '_id',
                'whenMatched': 'merge',
                'whenNotMatched': 'insert'
            }
        }
    ])

    users = list(db.users.find({}))
    print(users)

    client.close()

example()
```

------