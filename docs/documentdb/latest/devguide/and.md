

# $and
<a name="and"></a>

The `$and` operator in Amazon DocumentDB is used to combine multiple expressions and evaluate them as a single condition. It returns `true` if all the provided expressions evaluate to `true`, and `false` otherwise. This operator is useful for applying multiple criteria to a query.

**Parameters**
+ `expression1`: A required expression that evaluates to a boolean value.
+ `expression2`: A required expression that evaluates to a boolean value.
+ `...`: Additional required expressions that evaluate to boolean values.

## Example (MongoDB Shell)
<a name="and-examples"></a>

The following example demonstrates the use of the `$and` operator to find all documents in the "users" collection where the "age" field is greater than 18 and the "status" field is "active".

**Create sample documents**

```
db.users.insertMany([
  { name: "John", age: 25, status: "active" },
  { name: "Jane", age: 17, status: "active" },
  { name: "Bob", age: 30, status: "inactive" },
  { name: "Alice", age: 22, status: "active" }
]);
```

**Query example**

```
db.users.find({
  $and: [
    { age: { $gt: 18 } },
    { status: "active" }
  ]
});
```

**Output**

```
[
  { "_id" : ObjectId("614e3c4b63f5892e7c4e2345"), "name" : "John", "age" : 25, "status" : "active" },
  { "_id" : ObjectId("614e3c4b63f5892e7c4e2347"), "name" : "Alice", "age" : 22, "status" : "active" }
]
```

## Code examples
<a name="and-code"></a>

To view a code example for using the `$and` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function findActiveUsersOlderThan18() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const users = db.collection('users');

  const activeUsersOlderThan18 = await users.find({
    $and: [
      { age: { $gt: 18 } },
      { status: 'active' }
    ]
  }).toArray();

  console.log(activeUsersOlderThan18);
  await client.close();
}

findActiveUsersOlderThan18();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def find_active_users_older_than_18():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    users = db['users']

    active_users_older_than_18 = list(users.find({
        '$and': [
            {'age': {'$gt': 18}},
            {'status': 'active'}
        ]
    }))

    print(active_users_older_than_18)
    client.close()

find_active_users_older_than_18()
```

------