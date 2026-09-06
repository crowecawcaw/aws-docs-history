

# $pow
<a name="pow"></a>

Introduced in 8.0

The `$pow` operator in Amazon DocumentDB allows you to raise a number to a power. This can be useful for performing exponential calculations within your aggregation pipeline.

**Parameters**
+ `<number>` (required): The number to be raised to a power.
+ `<exponent>` (required): The power to which the number should be raised.

## Example (MongoDB Shell)
<a name="pow-examples"></a>

The following example demonstrates how to use the `$pow` operator to calculate the square of a number.

**Create sample documents**

```
db.numbers.insertMany([
  { "_id": 1, "value": 2 },
  { "_id": 2, "value": 3 },
  { "_id": 3, "value": 4 }
]);
```

**Query example**

```
db.numbers.aggregate([
  { $addFields: { "square": { $pow: ["$value", 2] } } }
])
```

**Output**

```
[
  { "_id": 1, "value": 2, "square": 4 },
  { "_id": 2, "value": 3, "square": 9 },
  { "_id": 3, "value": 4, "square": 16 }
]
```

## Code examples
<a name="pow-code"></a>

To view a code example for using the `$pow` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

Here's an example of using the $pow operator in a Node.js application:

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('numbers');

  const result = await collection.aggregate([
    { $addFields: { "square": { $pow: ["$value", 2] } } }
  ]).toArray();

  console.log(result);
  await client.close();
}

example();
```

------
#### [ Python ]

Here's an example of using the $pow operator in a Python application:

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['numbers']

    result = list(collection.aggregate([
        { "$addFields": { "square": { "$pow": ["$value", 2] } } }
    ]))

    print(result)
    client.close()

example()
```

------