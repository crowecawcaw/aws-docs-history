

# $lookup
<a name="lookup"></a>

The `$lookup` aggregation stage in Amazon DocumentDB allows you to perform a left outer join between two collections. This operation lets you combine data from multiple collections based on matching field values. It is particularly useful when you need to incorporate data from related collections into your query results.

**Parameters**
+ `from`: The name of the collection to perform the join with.
+ `localField`: The field from the input documents to match against the `foreignField`.
+ `foreignField`: The field from the documents in the `from` collection to match against the `localField`.
+ `as`: The name of the new field to add to the output documents containing the matching documents from the `from` collection.

## Example (MongoDB Shell)
<a name="lookup-examples"></a>

The following example demonstrates a simple `$lookup` operation that joins data from the `orders` collection into the `customers` collection.

**Create sample documents**

```
db.customers.insertMany([
  { _id: 1, name: "Alice" },
  { _id: 2, name: "Bob" },
  { _id: 3, name: "Charlie" }
]);

db.orders.insertMany([
  { _id: 1, customer_id: 1, total: 50 },
  { _id: 2, customer_id: 1, total: 100 },
  { _id: 3, customer_id: 2, total: 75 }
]);
```

**Query example**

```
db.customers.aggregate([
  {
    $lookup: {
      from: "orders",           
      localField: "_id",        
      foreignField: "customer_id", 
      as: "orders" 
    }
  }
]);
```

**Output**

```
[
  {
    _id: 1,
    name: 'Alice',
    orders: [
      { _id: 2, customer_id: 1, total: 100 },
      { _id: 1, customer_id: 1, total: 50 }
    ]
  },
  { _id: 3, name: 'Charlie', orders: [] },
  {
    _id: 2,
    name: 'Bob',
    orders: [ { _id: 3, customer_id: 2, total: 75 } ]
  }
]
```

## Code examples
<a name="lookup-code"></a>

To view a code example for using the `$lookup` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  await client.connect();

  const db = client.db('test');

  const result = await db.collection('customers').aggregate([
    {
      $lookup: {
        from: 'orders',
        localField: '_id',
        foreignField: 'customer_id',
        as: 'orders'
      }
    }
  ]).toArray();

  console.log(JSON.stringify(result, null, 2));
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

    db = client.test
    
    collection = db.customers

    pipeline = [
        {
            "$lookup": {
                "from": "orders",
                "localField": "_id",
                "foreignField": "customer_id",
                "as": "orders"
            }
        }
    ]

    result = collection.aggregate(pipeline)

    for doc in result:
        print(doc)

    client.close()

example()
```

------