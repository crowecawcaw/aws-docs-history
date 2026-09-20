

# $expr
<a name="expr"></a>

New from version 4.0.

Not supported by Elastic cluster.

The `$expr` operator in Amazon DocumentDB allows you to use aggregation expressions within the query language. It enables you to perform complex comparisons and computations on fields within a document, similar to the way you would use aggregation pipeline stages.

The `$eq`, `$lt`, `$lte`, `$gt`, and `$gte` comparison operators placed in an `$expr` operator can use an index, including an index on the `from` collection referenced in a `$lookup` stage.

**Limitations**
+ Indexes can only be used for comparisons between fields and constants, so the operand must resolve to a constant. For example, a comparison between `$a` and a constant value can use an index, but a comparison between `$a` and `$b` cannot.
+ Multikey, partial, or sparse indexes are not used. In those cases the query falls back to a collection scan.
+ When the `let` operand resolves to an empty or missing value, the comparison cannot use a targeted index seek. In this case, Amazon DocumentDB performs a full index scan.

**Parameters**
+ `expression`: An expression that returns a boolean value, allowing you to perform comparisons and computations on document fields.

## Example (MongoDB Shell)
<a name="expr-examples"></a>

The following example demonstrates how to use the `$expr` operator to find all documents where the `manufacturingCost` field is greater than the `price` field.

**Create sample documents**

```
db.inventory.insertMany([
  { item: "abc", manufacturingCost: 500, price: 100 },
  { item: "def", manufacturingCost: 300, price: 450 },
  { item: "ghi", manufacturingCost: 400, price: 120 }
]);
```

**Query example**

```
db.inventory.find({
  $expr: {
    $gt: ["$manufacturingCost", "$price"]
  }
})
```

**Output**

```
{ "_id" : ObjectId("60b9d4d68d2cac581bc5a89a"), "item" : "abc", "manufacturingCost" : 500, "price" : 100 },
{ "_id" : ObjectId("60b9d4d68d2cac581bc5a89c"), "item" : "ghi", "manufacturingCost" : 400, "price" : 120 }
```

## Code examples
<a name="expr-code"></a>

To view a code example for using the `$expr` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('inventory');

  const result = await collection.find({
    $expr: {
      $gt: ['$manufacturingCost', '$price']
    }
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
    collection = db['inventory']

    result = list(collection.find({
        '$expr': {
            '$gt': ['$manufacturingCost', '$price']
        }
    }))

    print(result)
    client.close()

example()
```

------