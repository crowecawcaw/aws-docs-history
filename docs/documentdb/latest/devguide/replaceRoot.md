

# $replaceRoot
<a name="replaceRoot"></a>

The `$replaceRoot` operator is used to replace the root document with the specified embedded document. This is useful when you want to promote a nested document to the top level or restructure your data output.

**Parameters**
+ `newRoot`: The new root document that will replace the existing root document.

## Example (MongoDB Shell)
<a name="replaceRoot-examples"></a>

This example shows how to extract shipping address information from customer orders, which is useful for generating shipping labels or address lists.

**Create sample documents**

```
db.orders.insertMany([
  {
    "_id":1, "orderId": "ORD-2024-001", "customerId": "CUST-12345", "orderDate": "2024-01-15", "shippingAddress": { "name": "María García", "street": "123 Main St", "city": "Seattle", "state": "WA", "zipCode": "98101", "country": "USA" },"totalAmount": 149.99 },
  { "_id":2, "orderId": "ORD-2024-002", "customerId": "CUST-67890", "orderDate": "2024-01-16", "shippingAddress": { "name": "Arnav Desai", "street": "456 Oak Ave", "city": "Portland", "state": "OR", "zipCode": "97201", "country": "USA" }, "totalAmount": 89.50 } ])
```

**Query example**

```
db.orders.aggregate([
  {
    $replaceRoot: {
      newRoot: "$shippingAddress"
    }
  }
])
```

**Output**

```
{
    name: 'María García',
    street: '123 Main St',
    city: 'Seattle',
    state: 'WA',
    zipCode: '98101',
    country: 'USA'
  },
  {
    name: 'Arnav Desai',
    street: '456 Oak Ave',
    city: 'Portland',
    state: 'OR',
    zipCode: '97201',
    country: 'USA'
  }
```

## Code examples
<a name="replaceRoot-code"></a>

To view a code example for using the `$replaceRoot` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function extractShippingAddresses() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('orders');

  const result = await collection.aggregate([
    {
      $replaceRoot: {
        newRoot: "$shippingAddress"
      }
    }
  ]).toArray();

  console.log(result);

  await client.close();
}

extractShippingAddresses();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def extract_shipping_addresses():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['orders']

    result = list(collection.aggregate([
        {
            "$replaceRoot": {
                "newRoot": "$shippingAddress"
            }
        }
    ]))

    print(result)

    client.close()

extract_shipping_addresses()
```

------