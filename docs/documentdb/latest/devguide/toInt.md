

# $toInt
<a name="toInt"></a>

New from version 4.0

The `$toInt` operator in Amazon DocumentDB is used to convert an input value to an integer data type. This operator is useful when you need to ensure that a field or expression is represented as an integer, which can be important for certain operations or data processing tasks.

**Parameters**
+ `expression`: The expression to be converted to an integer.

## Example (MongoDB Shell)
<a name="toInt-examples"></a>

The following example demonstrates how to use the `$toInt` operator to convert a string value to an integer.

**Create sample documents**

```
db.numbers.insertMany([
  { "name": "one", "value": "1" },
  { "name": "hundred", "value": "100" }
]);
```

**Query example**

```
db.numbers.aggregate([
  { $project: {
    "_id": 0,
    "name": 1,
    "intValue": { $toInt: "$value" }
  }}
]);
```

**Output**

```
{ "name": "one", "intValue": 1 }
{ "name": "hundred", "intValue": 100 }
```

## Code examples
<a name="toInt-code"></a>

To view a code example for using the `$toInt` command, choose the tab for the language that you want to use:

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
      "_id": 0,
      "name": 1,
      "intValue": { $toInt: "$value" }
    }}
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
    collection = db['numbers']

    result = list(collection.aggregate([
        { "$project": {
            "_id": 0,
            "name": 1,
            "intValue": { "$toInt": "$value" }
        }}
    ]))

    print(result)
    client.close()

example()
```

------