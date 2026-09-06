

# $gte
<a name="gte"></a>

The `$gte` operator in Amazon DocumentDB is used to match values that are greater than or equal to a specified value. This operator is useful for filtering and querying data based on numerical comparisons.

**Parameters**
+ `field`: The field to check against the provided value.
+ `value`: The value to compare against the field.

## Example (MongoDB Shell)
<a name="gte-examples"></a>

The following example demonstrates the usage of the `$gte` operator in Amazon DocumentDB to find all documents where the "age" field is greater than or equal to 25.

**Create sample documents**

```
db.users.insertMany([
  { _id: 1, name: "John", age: 20 },
  { _id: 2, name: "Jane", age: 25 },
  { _id: 3, name: "Bob", age: 30 },
  { _id: 4, name: "Alice", age: 35 }
]);
```

**Query example**

```
db.users.find({ age: { $gte: 25 } }, { _id: 0, name: 1, age: 1 });
```

**Output**

```
{ "name" : "Jane", "age" : 25 }
{ "name" : "Bob", "age" : 30 }
{ "name" : "Alice", "age" : 35 }
```

## Code examples
<a name="gte-code"></a>

To view a code example for using the `$gte` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function findUsersAboveAge(age) {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const users = db.collection('users');

  const result = await users.find({ age: { $gte: age } }, { projection: { _id: 0, name: 1, age: 1 } }).toArray();
  console.log(result);

  await client.close();
}

findUsersAboveAge(25);
```

------
#### [ Python ]

```
from pymongo import MongoClient

def find_users_above_age(age):
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    users = db.users

    result = list(users.find({ 'age': { '$gte': age } }, { '_id': 0, 'name': 1, 'age': 1 }))
    print(result)

    client.close()

find_users_above_age(25)
```

------