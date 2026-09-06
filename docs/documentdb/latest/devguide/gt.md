

# $gt
<a name="gt"></a>

The `$gt` operator in Amazon DocumentDB is used to select documents where the value of the specified field is greater than the specified value. This operator is useful for filtering and querying data based on numerical comparisons.

**Parameters**
+ `field`: The field to compare.
+ `value`: The value to compare against.

## Example (MongoDB Shell)
<a name="gt-examples"></a>

The following example demonstrates how to use the `$gt` operator to find all documents where the `age` field is greater than 30.

**Create sample documents**

```
db.users.insertMany([
  { name: "John", age: 25 },
  { name: "Jane", age: 32 },
  { name: "Bob", age: 45 },
  { name: "Alice", age: 28 }
]);
```

**Query example**

```
db.users.find({ age: { $gt: 30 } });
```

**Output**

```
{ "_id" : ObjectId("6249e5c22a5d39884a0a0001"), "name" : "Jane", "age" : 32 },
{ "_id" : ObjectId("6249e5c22a5d39884a0a0002"), "name" : "Bob", "age" : 45 }
```

## Code examples
<a name="gt-code"></a>

To view a code example for using the `$gt` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function findUsersOlderThan30() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const users = await db.collection('users').find({ age: { $gt: 30 } }).toArray();
  console.log(users);
  await client.close();
}

findUsersOlderThan30();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def find_users_older_than_30():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    users = list(db.users.find({ 'age': { '$gt': 30 } }))
    print(users)
    client.close()

find_users_older_than_30()
```

------