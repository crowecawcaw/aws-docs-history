

# $push
<a name="push"></a>

The `$push` operator in Amazon DocumentDB is used to add an item to an array field in a document. This operator is particularly useful when you need to append new data to an existing array without overwriting the entire array.

**Parameters**
+ `field`: The name of the array field to which the new element should be added.
+ `value`: The value to be added to the array.
+ `position`: (optional) A modifier that specifies the position in the array where the new element should be added. Supported modifiers include `$` (add to the end of the array) and `$[]` (add to the end of the array, ignoring any array filters).

## Example (MongoDB Shell)
<a name="push-examples"></a>

The following example demonstrates how to use the `$push` operator to add new elements to an array field in a document.

**Create sample documents**

```
db.users.insert([
  { _id: 1, name: "John Doe", hobbies: ["reading", "swimming"] },
  { _id: 2, name: "Jane Smith", hobbies: ["gardening", "cooking"] }
])
```

**Query example**

```
db.users.updateOne(
  { _id: 1 },
  { $push: { hobbies: "hiking" } }
)
```

**Output**

```
{
  "acknowledged" : true,
  "matchedCount" : 1,
  "modifiedCount" : 1
}
```

After running the update, the document with `_id: 1` will have the `hobbies` array updated to `[&quot;reading&quot;, &quot;swimming&quot;, &quot;hiking&quot;]`.

## Code examples
<a name="push-code"></a>

To view a code example for using the `$push` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function updateDocument() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('users');

  const result = await collection.updateOne(
    { _id: 1 },
    { $push: { hobbies: "hiking" } }
  );

  console.log(result);
  client.close();
}

updateDocument();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def update_document():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['users']

    result = collection.update_one(
        {'_id': 1},
        {'$push': {'hobbies': 'hiking'}}
    )

    print(result.raw_result)
    client.close()

update_document()
```

------