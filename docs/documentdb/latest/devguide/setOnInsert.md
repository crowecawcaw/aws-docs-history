

# $setOnInsert
<a name="setOnInsert"></a>

The `$setOnInsert` operator in Amazon DocumentDB is used to set the value of a field if a document is being inserted, but it has no effect if the document is being updated.

**Parameters**
+ `field`: The field to be set.
+ `value`: The value to assign to the field.

## Example (MongoDB Shell)
<a name="setOnInsert-examples"></a>

The following example demonstrates the usage of the `$setOnInsert` operator in Amazon DocumentDB. It creates a new document if the document does not already exist, but it has no effect if the document is being updated.

**Create sample documents**

```
db.users.insertOne({
  _id: 1,
  name: "John Doe",
  age: 30
})
```

**Query example 1 - Update existing document**

```
db.users.update(
  { _id: 1 },
  {
    $set: { age: 31 },
    $setOnInsert: { createdAt: new Date() }
  },
  { upsert: true }
)
```

**Output 1**

```
{
  _id: 1,
  name: "John Doe",
  age: 31
}
```

The output shows that the document was updated, but the `createdAt` field was **NOT added** since the document already existed. The `$setOnInsert` operator only applies when inserting new documents.

**Query example 2 - Insert new document (upsert)**

```
db.users.update(
  { _id: 2 },
  {
    $set: { name: "Jane Smith", age: 25 },
    $setOnInsert: { createdAt: new Date() }
  },
  { upsert: true }
)
```

**Output 2**

```
{
  _id: 2,
  name: "Jane Smith", 
  age: 25,
  createdAt: ISODate("2025-10-31T09:57:52.459Z")
}
}
```

## Code examples
<a name="setOnInsert-code"></a>

To view a code example for using the `$setOnInsert` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function updateWithSetOnInsert() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const users = db.collection('users');

  await users.updateOne(
    { _id: 1 },
    {
      $set: { age: 31 },
      $setOnInsert: { createdAt: new Date() }
    },
    { upsert: true }
  );

  const updatedUser = await users.findOne({ _id: 1 });
  console.log(updatedUser);

  await client.close();
}

updateWithSetOnInsert();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def update_with_set_on_insert():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    users = db['users']

    result = users.update_one(
        {'_id': 1},
        {
            '$set': {'age': 31},
            '$setOnInsert': {'createdAt': datetime.datetime.now()}
        },
        upsert=True
    )

    updated_user = users.find_one({'_id': 1})
    print(updated_user)

    client.close()

update_with_set_on_insert()
```

------