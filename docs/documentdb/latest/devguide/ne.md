

# $ne
<a name="ne"></a>

The `$ne` operator is used to match documents where the value of a field is not equal to the specified value. It is a comparison operator that can be used in query predicates to filter documents.

Planner version 2.0 added index support for `$ne`.

**Parameters**
+ `field`: The field to check.
+ `value`: The value to check against.

## Example (MongoDB Shell)
<a name="ne-examples"></a>

In this example, we'll find all documents in the `users` collection where the `status` field is not equal to `"active"`.

**Create sample documents**

```
db.users.insertMany([
  { name: "John", status: "active" },
  { name: "Jane", status: "inactive" },
  { name: "Bob", status: "suspended" },
  { name: "Alice", status: "active" }
]);
```

**Query example**

```
db.users.find({ status: { $ne: "active" } });
```

**Output**

```
[
  {
    _id: ObjectId('...'),
    name: 'Jane',
    status: 'inactive'
  },
  {
    _id: ObjectId('...'),
    name: 'Bob',
    status: 'suspended'
  }
]
```

## Code examples
<a name="ne-code"></a>

To view a code example for using the `$ne` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const users = db.collection('users');

  const result = await users.find({ status: { $ne: 'active' } }).toArray();
  console.log(result);

  await client.close();
}

main();
```

------
#### [ Python ]

```
from pymongo import MongoClient

client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
db = client['test']
users = db['users']

result = list(users.find({ 'status': { '$ne': 'active' } }))
print(result)

client.close()
```

------