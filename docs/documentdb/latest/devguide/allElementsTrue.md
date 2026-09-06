

# $allElementsTrue
<a name="allElementsTrue"></a>

New from version 4.0

The `$allElementsTrue` operator is used to check if all elements in an array evaluate to a true value.

**Parameters**
+ `expression`: An expression that evaluates to an array.

## Example (MongoDB Shell)
<a name="allElementsTrue-examples"></a>

The following example demonstrates the usage of `$allElementsTrue` to check if all elements in an array are true.

**Create sample documents**

```
db.collection.insert([
  { "name": "John", "scores": [100, 90, 80] },
  { "name": "Jane", "scores": [80, 85, 0] },
  { "name": "Bob", "scores": [90, 95, null] }
])
```

**Query example**

```
db.collection.find({
  "scores": { "$allElementsTrue": [{ "$gt": 0 }] }
})
```

**Output**

```
[
  { "_id" : ObjectId("..."), "name" : "John", "scores" : [ 100, 90, 80 ] },
  { "_id" : ObjectId("..."), "name" : "Bob", "scores" : [ 90, 95, null ] }
]
```

In this example, the query checks if all elements in the `scores` array are greater than 0. The document with `&quot;name&quot;: &quot;Jane&quot;` is excluded because the `scores` array contains a 0, which is a falsy value.

## Code examples
<a name="allElementsTrue-code"></a>

To view a code example for using the `$allElementsTrue` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('collection');

  const result = await collection.find({
    "scores": { "$allElementsTrue": [{ "$gt": 0 }] }
  }).toArray();

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
    collection = db['collection']

    result = list(collection.find({
        "scores": {"$allElementsTrue": [{"$gt": 0}]}
    }))

    print(result)

    client.close()

example()
```

------