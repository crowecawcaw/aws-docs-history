

# $cmp
<a name="cmp"></a>

The `$cmp` operator in Amazon DocumentDB is used to compare two values and return an integer value that indicates their relative order. It is a comparison operator that compares two expressions and returns an integer value of -1, 0, or 1, depending on whether the first value is less than, equal to, or greater than the second value, respectively.

**Parameters**
+ `expression1`: The first expression to compare.
+ `expression2`: The second expression to compare.

## Example (MongoDB Shell)
<a name="cmp-examples"></a>

The following example demonstrates the usage of the `$cmp` operator to compare two numeric values.

**Create sample documents**

```
db.collection.insertMany([
  { _id: 1, value1: 10, value2: 20 },
  { _id: 2, value1: 15, value2: 15 },
  { _id: 3, value1: 20, value2: 10 }
]);
```

**Query example**

```
db.collection.find({
  $expr: {
    $cmp: ["$value1", "$value2"]
  }
})
```

**Output**

```
[
  { "_id" : 1, "value1" : 10, "value2" : 20 },
  { "_id" : 3, "value1" : 20, "value2" : 10 }
]
```

In this example, the `$cmp` operator compares the `value1` and `value2` fields for each document. The result is:

```
- `$cmp: ["$value1", "$value2"]` returns -1 for the first document (10 < 20), 0 for the second document (15 = 15), and 1 for the third document (20 > 10).
```

## Code examples
<a name="cmp-code"></a>

To view a code example for using the `$cmp` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

Here's an example of using the `$cmp` operator in a Node.js application with the `mongodb` driver:

```
const { MongoClient } = require('mongodb');

const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

async function main() {
  await client.connect();
  const db = client.db('test');
  const collection = db.collection('mycollection');

  // Insert sample documents
  await collection.insertMany([
    { _id: 1, value1: 10, value2: 20 },
    { _id: 2, value1: 15, value2: 15 },
    { _id: 3, value1: 20, value2: 10 }
  ]);

  // Query using $cmp operator
  const result = await collection.find({
    $expr: {
      $cmp: ['$value1', '$value2']
    }
  }).toArray();

  console.log(result);

  await client.close();
}

main();
```

------
#### [ Python ]

Here's an example of using the `$cmp` operator in a Python application with the `pymongo` driver:

```
from pymongo import MongoClient

client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
db = client['test']
collection = db['mycollection']

# Insert sample documents
collection.insert_many([
    {'_id': 1, 'value1': 10, 'value2': 20},
    {'_id': 2, 'value1': 15, 'value2': 15},
    {'_id': 3, 'value1': 20, 'value2': 10}
])

# Query using $cmp operator
result = list(collection.find({
    '$expr': {
        '$cmp': ['$value1', '$value2']
    }
}))

print(result)

client.close()
```

The output of both the Node.js and Python examples will be the same as the MongoDB Shell example:

```
[
  { "_id" : 1, "value1" : 10, "value2" : 20 },
  { "_id" : 2, "value1" : 15, "value2" : 15 },
  { "_id" : 3, "value1" : 20, "value2" : 10 }
]
```

------