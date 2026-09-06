

# $inc
<a name="inc"></a>

The `$inc` operator is used to increment the value of a field by a specified amount. It is used to update a numeric field, such as a counter or a rating, without having to retrieve the current value, calculate the new value, and then update the field.

**Parameters**
+ `field`: The name of the field to increment.
+ `amount`: The amount by which to increment the field. This can be a positive or negative value.

## Example (MongoDB Shell)
<a name="inc-examples"></a>

The following example demonstrates how to use the `$inc` operator to increment the `age` field of a document.

**Create sample documents**

```
db.users.insertOne({_id: 123, name: "John Doe", age: 30})
```

**Query example**

```
db.users.updateOne({_id: 123}, {$inc: {age: 1}})
```

**View updated document**

```
db.users.findOne({_id: 123})
```

**Output**

```
{ "_id" : 123, "name" : "John Doe", "age" : 31 }
```

## Code examples
<a name="inc-code"></a>

To view a code example for using the `$inc` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function updateWithInc() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('users');

  const result = await collection.updateOne(
    { _id: 123 },
    { $inc: { age: 1 } }
  );

  console.log(result);

  await client.close();
}

updateWithInc();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def update_with_inc():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['users']

    result = collection.update_one(
        {'_id': 123},
        {'$inc': {'age': 1}}
    )

    print(result.modified_count)

    client.close()

update_with_inc()
```

------