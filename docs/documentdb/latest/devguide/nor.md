

# $nor
<a name="nor"></a>

The `$nor` operator is used to match documents where none of the specified query conditions are true. It is similar to the logical "NOR" operation, where the result is true if none of the operands are true.

**Parameters**
+ `expression1`: The first expression to evaluate.
+ `expression2`: The second expression to evaluate.
+ `expressionN`: Additional expressions to evaluate.

## Example (MongoDB Shell)
<a name="nor-examples"></a>

The following example demonstrates the usage of the `$nor` operator by retrieving documents where the `qty` field is not less than 20 and the `size` field is not equal to "XL".

**Create sample documents**

```
db.items.insertMany([
  { qty: 10, size: "M" },
  { qty: 15, size: "XL" },
  { qty: 25, size: "L" },
  { qty: 30, size: "XL" }
])
```

**Query example**

```
db.items.find({
  $nor: [
    { qty: { $lt: 20 } },
    { size: "XL" }
  ]
})
```

**Output**

```
[
  { "_id" : ObjectId("..."), "qty" : 25, "size" : "L" }
]
```

## Code examples
<a name="nor-code"></a>

To view a code example for using the `$nor` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('items');

  const result = await collection.find({
    $nor: [
      { qty: { $lt: 20 } },
      { size: "XL" }
    ]
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
    collection = db['items']

    result = list(collection.find({
        '$nor': [
            { 'qty': { '$lt': 20 } },
            { 'size': 'XL' }
        ]
    }))

    print(result)

    client.close()

example()
```

------