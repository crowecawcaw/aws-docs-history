

# $setUnion
<a name="setUnion"></a>

The `$setUnion` aggregation operator in Amazon DocumentDB is used to combine two or more sets of values and return a set that contains all the unique elements from the input sets. This operator is useful when you need to perform set-based operations on array fields in your documents.

**Parameters**
+ `expression1`: An expression that resolves to an array.
+ `expression2`: An expression that resolves to an array.
+ `expressionN`: Additional expressions that resolve to arrays (optional).

## Example (MongoDB Shell)
<a name="setUnion-examples"></a>

The following example demonstrates how to use the `$setUnion` operator to combine the unique elements from two array fields in a collection.

**Create sample documents**

```
db.users.insertMany([
  { _id: 1, name: "Alice", hobbies: ["reading", "swimming"], skills: ["coding", "writing"] },
  { _id: 2, name: "Bob", hobbies: ["cooking", "gardening"], skills: ["coding", "photography"] },
  { _id: 3, name: "Charlie", hobbies: ["reading", "painting"], skills: ["gardening", "music"] }
]);
```

**Query example**

```
db.users.aggregate([
  {
    $project: {
      name: 1,
      allInterests: { $setUnion: ["$hobbies", "$skills"] }
    }
  }
]);
```

**Output**

```
[
  { "_id" : 1, "name" : "Alice", "allInterests" : [ "coding", "reading", "swimming", "writing" ] },
  { "_id" : 2, "name" : "Bob", "allInterests" : [ "coding", "cooking", "gardening", "photography" ] },
  { "_id" : 3, "name" : "Charlie", "allInterests" : [ "gardening", "music", "painting", "reading" ] }
]
```

In this example, the `$setUnion` operator is used to combine the unique elements from the `hobbies` and `skills` array fields for each user document. The resulting `allInterests` field contains the union of all the unique hobbies and skills for each user.

## Code examples
<a name="setUnion-code"></a>

To view a code example for using the `$setUnion` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const users = db.collection('users');

  const result = await users.aggregate([
    {
      $project: {
        _id: 1,
        name: 1,
        allInterests: { $setUnion: ["$hobbies", "$skills"] }
      }
    }
  ]).toArray();

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
    users = db['users']

    result = list(users.aggregate([
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'allInterests': { '$setUnion': ["$hobbies", "$skills"] }
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------