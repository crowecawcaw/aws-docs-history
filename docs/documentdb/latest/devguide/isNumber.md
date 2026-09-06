

# $isNumber
<a name="isNumber"></a>

New from version 8.0.1.

The `$isNumber` operator in Amazon DocumentDB returns a boolean indicating whether a given expression resolves to a numeric type (integer, decimal, double, long). Note that arrays are not considered numeric, even if all elements in the array are numbers. For example, `$isNumber` applied to the value `[1, 2, 3]` returns `false`.

**Parameters**
+ `expression`: Any expression to check whether it resolves to a numeric type.

## Example (MongoDB Shell)
<a name="isNumber-examples"></a>

The following example shows how to use the `$isNumber` operator to check whether field values are numeric.

**Create sample documents**

```
db.data.insertMany([
  {_id: 1, value: 42},
  {_id: 2, value: "hello"},
  {_id: 3, value: 3.14},
  {_id: 4, value: null}
]);
```

**Query example**

```
db.data.aggregate([
  { $project: { isNum: { $isNumber: "$value" } } }
]);
```

**Output**

```
[
  {_id: 1, isNum: true},
  {_id: 2, isNum: false},
  {_id: 3, isNum: true},
  {_id: 4, isNum: false}
]
```

## Code examples
<a name="isNumber-code"></a>

To view a code example for using the `$isNumber` operator, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  try {
    await client.connect();
    const db = client.db('test');
    const collection = db.collection('data');
    const result = await collection.aggregate([
      { $project: { isNum: { $isNumber: "$value" } } }
    ]).toArray();
    console.log(result);
  } finally {
    await client.close();
  }
}
example();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    try:
        db = client['test']
        collection = db['data']
        result = list(collection.aggregate([
            {'$project': {'isNum': {'$isNumber': '$value'}}}
        ]))
        print(result)
    finally:
        client.close()

example()
```

------