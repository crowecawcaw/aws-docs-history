

# $max
<a name="max-update"></a>

The `$max` update operator updates a field's value only if the specified value is greater than the current field value. This operator is useful for maintaining maximum values across updates.

**Parameters**
+ `field`: The field to update.
+ `value`: The value to compare with the current field value.

## Example (MongoDB Shell)
<a name="max-update-examples"></a>

The following example demonstrates using the `$max` operator to update the highest recorded score for a player.

**Create sample documents**

```
db.scores.insertMany([
  { _id: 1, player: "Alice", highScore: 85 },
  { _id: 2, player: "Bob", highScore: 92 },
  { _id: 3, player: "Charlie", highScore: 78 }
])
```

**Update example**

```
db.scores.updateOne(
  { _id: 1 },
  { $max: { highScore: 95 } }
)
```

**Result**

The `highScore` field for Alice is updated to 95 because 95 is greater than the current value of 85.

```
{ "_id": 1, "player": "Alice", "highScore": 95 }
```

## Code examples
<a name="max-update-code"></a>

To view a code example for using the `$max` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('scores');

  const result = await collection.updateOne(
    { _id: 1 },
    { $max: { highScore: 95 } }
  );

  console.log(result);
  await client.close();
}

example();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['scores']

    result = collection.update_one(
        { '_id': 1 },
        { '$max': { 'highScore': 95 } }
    )

    print(result)
    client.close()

example()
```

------