

# $not
<a name="not"></a>

The `$not` operator is used to negate the result of a given expression. It allows you to select documents where the specified condition does not match.

Planner version 2.0 added index support for `$not {eq}` and `$not {in}`.

**Parameters**
+ `expression`: The expression to negate.

## Example (MongoDB Shell)
<a name="not-examples"></a>

The following example demonstrates how to use the `$not` operator to find documents where the `status` field is not equal to "active".

**Create sample documents**

```
db.users.insertMany([
  { name: "John", status: "active" },
  { name: "Jane", status: "inactive" },
  { name: "Bob", status: "pending" },
  { name: "Alice", status: "active" }
]);
```

**Query example**

```
db.users.find({ status: { $not: { $eq: "active" } } });
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
    status: 'pending'
  }
]
```

## Code examples
<a name="not-code"></a>

To view a code example for using the `$not` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient, Filters } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('users');

  const result = await collection.find({
    status: { $not: { $eq: "active" } }
  }).toArray();

  console.log(result);

  await client.close();
}

main();
```

------
#### [ Python ]

```
from pymongo import MongoClient
from bson.son import SON

client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
db = client['test']
collection = db['users']

result = collection.find({
    "status": {"$not": {"$eq": "active"}}
})

for doc in result:
    print(doc)

client.close()
```

------