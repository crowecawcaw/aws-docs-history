

# $each
<a name="each"></a>

The `$each` operator is used in conjunction with other update operators, such as `$push` and `$addToSet`, to add multiple values to an array field. It allows adding multiple elements to an array in a single operation, rather than having to execute multiple update operations.

**Parameters**
+ `value`: The array of values to add to the array field.

## Example (MongoDB Shell)
<a name="each-examples"></a>

The following example demonstrates using the `$each` operator with the `$push` operator to add multiple elements to an array field.

**Create sample documents**

```
db.fruits.insertOne({
  _id: 1,
  fruits: ["apple", "banana"]
})
```

**Query example**

```
db.fruits.updateOne(
  { _id: 1 },
  { $push: { fruits: { $each: ["cherry", "durian", "elderberry"] } } }
)
```

**View updated document**

```
db.fruits.findOne({ _id: 1 })
```

**Output**

```
{
  _id: 1,
  fruits: [ 'apple', 'banana', 'cherry', 'durian', 'elderberry' ]
}
```

## Code examples
<a name="each-code"></a>

To view a code example for using the `$each` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('fruits');

  await collection.updateOne(
    { _id: 1 },
    { $push: { fruits: { $each: ["cherry", "durian", "elderberry"] } } }
  );

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
    collection = db['fruits']

    collection.update_one(
        {'_id': 1},
        {'$push': {'fruits': {'$each': ['cherry', 'durian', 'elderberry']}}}
    )

    client.close()

example()
```

------