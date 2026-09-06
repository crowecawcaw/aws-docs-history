

# $add
<a name="add"></a>

The `$add` operator in Amazon DocumentDB is used to add numbers or dates together. It can be used to perform arithmetic operations on numeric fields or to perform date arithmetic by adding a number of time units to a date field.

**Parameters**
+ `expression1`: The first number or date to add.
+ `expression2`: The second number or date to add.
+ `expression3`: (optional) Additional numbers or dates to add.

## Example (MongoDB Shell)
<a name="add-examples"></a>

The following example demonstrates how to use the `$add` operator to add two numbers together.

**Create sample documents**

```
db.numbers.insertMany([
  { _id: 1, a: 5, b: 3 },
  { _id: 2, a: 10, b: 7 },
  { _id: 3, a: 2, b: 8 }
]);
```

**Query example**

```
db.numbers.aggregate([
  { $project: {
    _id: 1,
    sum: { $add: ["$a", "$b"] }
  }}
])
```

**Output**

```
[
  { "_id" : 1, "sum" : 8 },
  { "_id" : 2, "sum" : 17 },
  { "_id" : 3, "sum" : 10 }
]
```

In this example, the `$add` operator is used to add the values of the `a` and `b` fields for each document and store the result in the `sum` field.

## Code examples
<a name="add-code"></a>

To view a code example for using the `$add` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('numbers');

  const result = await collection.aggregate([
    { $project: {
      _id: 1,
      sum: { $add: ['$a', '$b'] }
    }}
  ]).toArray();

  console.log(result);
  client.close();
}

example();
```

------
#### [ Python ]

```
from pymongo import MongoClient

client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
db = client['test']
collection = db['numbers']

result = list(collection.aggregate([
    { '$project': {
        '_id': 1,
        'sum': { '$add': ['$a', '$b'] }
    }}
]))

print(result)
client.close()
```

------