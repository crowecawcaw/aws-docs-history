

# $redact
<a name="redact"></a>

The `$redact` aggregation stage in Amazon DocumentDB is used to selectively include or exclude content from the output documents based on the values of specified fields. This is particularly useful in scenarios where you need to control the visibility of sensitive data based on access levels or user permissions.

**Parameters**
+ `$cond`: An expression that evaluates to either `$$KEEP`, `$$PRUNE`, or `$$DESCEND` for each field in the document.
+ `$$KEEP`: Retains the current field in the output document.
+ `$$PRUNE`: Removes the current field from the output document.
+ `$$DESCEND`: Recursively applies the `$redact` stage to the current field, which is an object or array.

## Example (MongoDB Shell)
<a name="redact-examples"></a>

In this example, we'll use the `$redact` stage to filter orders based on their status, showing only orders with specific status values.

**Create sample documents**

```
db.orders.insert([
  { "_id": 1, "status": "shipped", "customer": "Carlos Salazar", "total": 150.00, "date": "2025-01-15" },
  { "_id": 2, "status": "processing", "customer": "Saanvi Sarkar", "total": 89.99, "date": "2025-01-20" },
  { "_id": 3, "status": "cancelled", "customer": "Zhang Wei", "total": 220.50, "date": "2025-01-18" }
])
```

**Query example**

```
db.orders.aggregate([
  {
    $redact: {
      $cond: {
        if: { $in: ["$status", ["shipped", "processing"]] },
        then: "$$KEEP",
        else: "$$PRUNE"
      }
    }
  }
])
```

**Output**

```
[
  { _id: 1, status: 'shipped', customer: 'Carlos Salazar', total: 150, date: '2025-01-15' },
  { _id: 2, status: 'processing', customer: 'Saanvi Sarkar', total: 89.99, date: '2025-01-20' }
]
```

In this example, the `$redact` stage checks the value of the `status` field in each document. If the `status` is "shipped" or "processing", the document is kept (`$$KEEP`). Otherwise, the document is pruned (`$$PRUNE`).

## Code examples
<a name="redact-code"></a>

To view a code example for using the `$redact` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('orders');

  const result = await collection.aggregate([
    {
      $redact: {
        $cond: {
          if: { $in: ['$status', ['shipped', 'processing']] },
          then: '$$KEEP',
          else: '$$PRUNE'
        }
      }
    }
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

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['orders']

    result = list(collection.aggregate([
        {
            '$redact': {
                '$cond': {
                    'if': { '$in': ['$status', ['shipped', 'processing']] },
                    'then': '$$KEEP',
                    'else': '$$PRUNE'
                }
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------