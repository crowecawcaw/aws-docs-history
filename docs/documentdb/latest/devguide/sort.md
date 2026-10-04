

# $sort
<a name="sort"></a>

The `$sort` aggregation stage orders documents in the pipeline based on specified field values. Documents are arranged in ascending or descending order according to the sort criteria provided.

**Parameters**
+ `field`: The field name to sort by.
+ `order`: Use `1` for ascending order or `-1` for descending order.

## Example (MongoDB Shell)
<a name="sort-examples"></a>

The following example demonstrates using the `$sort` stage to order products by price in descending order.

**Create sample documents**

```
db.products.insertMany([
  { _id: 1, name: "Laptop", category: "Electronics", price: 1200 },
  { _id: 2, name: "Mouse", category: "Electronics", price: 25 },
  { _id: 3, name: "Desk", category: "Furniture", price: 350 },
  { _id: 4, name: "Chair", category: "Furniture", price: 150 },
  { _id: 5, name: "Monitor", category: "Electronics", price: 400 }
]);
```

**Query example**

```
db.products.aggregate([
  { $sort: { price: -1 } }
]);
```

**Output**

```
[
  { _id: 1, name: 'Laptop', category: 'Electronics', price: 1200 },
  { _id: 5, name: 'Monitor', category: 'Electronics', price: 400 },
  { _id: 3, name: 'Desk', category: 'Furniture', price: 350 },
  { _id: 4, name: 'Chair', category: 'Furniture', price: 150 },
  { _id: 2, name: 'Mouse', category: 'Electronics', price: 25 }
]
```

## Code examples
<a name="sort-code"></a>

To view a code example for using the `$sort` aggregation stage, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('products');

  const result = await collection.aggregate([
    { $sort: { price: -1 } }
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
    collection = db['products']

    result = list(collection.aggregate([
        { '$sort': { 'price': -1 } }
    ]))

    print(result)
    client.close()

example()
```

------

## Incremental sort
<a name="sort-incremental-sort"></a>

**Incremental sort** is an optimization in which Amazon DocumentDB uses an index that already orders the *leading* fields of a multi-field sort. Amazon DocumentDB then sorts only the remaining fields within each group of documents that share the same leading values. Instead of sorting the entire result set in memory as one block (a full sort), Amazon DocumentDB reads documents in index order. It then performs many small, independent sorts, one per group. The results are identical to a full sort. Only the query plan and the amount of memory and work it uses change.

**Benefits**

Incremental sort provides the following benefits:
+ **Lower memory use and fewer disk-based sort spills.** Amazon DocumentDB orders one small group at a time instead of the whole result set at once.
+ **Faster results with `limit`.** Amazon DocumentDB can emit sorted documents before it reads the entire input. A sort followed by a `limit` (for example, a top-N or paginated query) can stop as soon as it has produced enough documents.

**When Amazon DocumentDB chooses an incremental sort**

For example, given a sort on `{ customerId: 1, orderDate: -1 }` and an index on only `{ customerId: 1 }`, the index already returns documents ordered by `customerId`. Amazon DocumentDB only needs to order each group of documents that share the same `customerId` by `orderDate`. The already-ordered leading field (`customerId`) is the **presorted key**. Depending on how much of the sort an index already provides, Amazon DocumentDB chooses one of three behaviors:
+ **The index orders every sort key.** No sort is needed. Amazon DocumentDB reads documents directly in the requested order.
+ **The index orders a leading prefix of the sort keys.** Amazon DocumentDB uses an incremental sort, ordering only the trailing keys within each presorted group.
+ **No index orders any leading sort key.** Amazon DocumentDB performs a full sort over the entire input.

**Requirements and limitations**

Incremental sort requires Amazon DocumentDB 8.0.2 or later, running planner version 3.0 (the default query planner as of Amazon DocumentDB 8.0.2). For more information about planner versions, see [Query planner v3](query-planner-v3.md).

Amazon DocumentDB cannot use a partial index or a multikey (array) index to supply the presorted prefix for an incremental sort. In those cases, Amazon DocumentDB falls back to a full sort. This never affects the correctness of results.

**Verifying an incremental sort with `explain()`**

Use `explain()` to confirm that a query uses an incremental sort. In the winning plan, an incremental sort appears as a `SORT` stage that includes a `presortedKeys` array listing the leading sort fields the index already ordered. A full sort appears as a `SORT` stage without a `presortedKeys` array. The `presortedKeys` field is a Amazon DocumentDB-specific addition to the `explain()` output and does not appear in MongoDB explain plans.

```
db.orders.createIndex({ customerId: 1 })

db.orders.find({}).sort({ customerId: 1, orderDate: -1 }).explain()
```

```
{
    "stage": "SORT",
    "sortPattern": {
        "customerId": 1,
        "orderDate": -1
    },
    "presortedKeys": [
        "customerId"
    ],
    "inputStage": {
        "stage": "IXSCAN",
        "indexName": "customerId_1",
        "direction": "forward"
    }
}
```