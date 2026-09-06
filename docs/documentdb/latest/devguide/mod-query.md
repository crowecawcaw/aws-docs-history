

# $mod
<a name="mod-query"></a>

The `$mod` query operator selects documents where a field value divided by a divisor has a specified remainder. This is useful for filtering documents based on modulo arithmetic conditions.

**Parameters**
+ `divisor`: The number to divide by.
+ `remainder`: The expected remainder value.

## Example (MongoDB Shell)
<a name="mod-query-examples"></a>

The following example demonstrates using the `$mod` operator to find all orders where the quantity is an odd number.

**Create sample documents**

```
db.orders.insertMany([
  { _id: 1, item: "Widget", quantity: 15 },
  { _id: 2, item: "Gadget", quantity: 20 },
  { _id: 3, item: "Tool", quantity: 7 },
  { _id: 4, item: "Device", quantity: 12 },
  { _id: 5, item: "Part", quantity: 9 }
]);
```

**Query example**

```
db.orders.find({ quantity: { $mod: [2, 1] } });
```

**Output**

```
{ "_id" : 1, "item" : "Widget", "quantity" : 15 }
{ "_id" : 3, "item" : "Tool", "quantity" : 7 }
{ "_id" : 5, "item" : "Part", "quantity" : 9 }
```

This query returns documents where the quantity divided by 2 has a remainder of 1, effectively selecting all odd quantities.

## Code examples
<a name="mod-query-code"></a>

To view a code example for using the `$mod` query operator, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('orders');

  const result = await collection.find({ quantity: { $mod: [2, 1] } }).toArray();

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
    db = client['test']
    collection = db['orders']

    result = list(collection.find({'quantity': {'$mod': [2, 1]}}))

    print(result)
    client.close()

example()
```

------