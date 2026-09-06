

# $sortByCount
<a name="sortByCount"></a>

New from version 8.0.1.

The `$sortByCount` aggregation stage in Amazon DocumentDB groups incoming documents based on the value of a specified expression, then computes the count of documents in each distinct group, and sorts the results by count in descending order. It is equivalent to a `$group` stage with a `$sum` accumulator followed by a `$sort` stage on the count field.

**Parameters**
+ `expression`: The expression to group by. This can be a field path (prefixed with `$`) or any valid aggregation expression.

## Example (MongoDB Shell)
<a name="sortByCount-examples"></a>

The following example shows how to use the `$sortByCount` stage to count and sort documents by a category field.

**Create sample documents**

```
db.products.insertMany([
  { name: "Widget", category: "electronics" },
  { name: "Gadget", category: "electronics" },
  { name: "Doohickey", category: "electronics" },
  { name: "Apple", category: "food" },
  { name: "Banana", category: "food" },
  { name: "Hammer", category: "tools" }
]);
```

**Query example**

```
db.products.aggregate([
  { $sortByCount: "$category" }
]);
```

**Output**

```
[
  { "_id": "electronics", "count": 3 },
  { "_id": "food", "count": 2 },
  { "_id": "tools", "count": 1 }
]
```

The results are automatically sorted by `count` in descending order.

## Code examples
<a name="sortByCount-code"></a>

To view a code example for using the `$sortByCount` stage, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  try {
    await client.connect();
    const db = client.db('test');
    const collection = db.collection('products');

    const result = await collection.aggregate([
      { $sortByCount: "$category" }
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
        collection = db['products']

        result = list(collection.aggregate([
            { '$sortByCount': '$category' }
        ]))

        print(result)
    finally:
        client.close()

example()
```

------