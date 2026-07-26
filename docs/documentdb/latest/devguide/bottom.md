# $bottom

New from version 8.0.1.

Use the `$bottom` accumulator in the `$group` stage to return the lowest-ranked document per group according to a specified sort order.

**Parameters**

- `sortBy`: A document specifying the sort order. Use `1` for ascending or `-1` for descending.
- `output`: An expression that specifies the fields to return from the bottom document.

## Example (MongoDB Shell)

The following example shows how to use the `$bottom` accumulator to find the bottom sale (lowest quantity) per item in a sales collection.

**Create sample documents**

```
db.sales.insertMany([
  { item: "abc", quantity: 10, price: 5 },
  { item: "abc", quantity: 5, price: 8 },
  { item: "xyz", quantity: 15, price: 3 },
  { item: "xyz", quantity: 7, price: 6 }
])
```

**Query example**

```
db.sales.aggregate([
  { $group: { _id: "$item", bottomSale: { $bottom: { sortBy: { quantity: -1 }, output: { quantity: "$quantity", price: "$price" } } } } }
])
```

**Output**

```
[
  { "_id": "xyz", "bottomSale": { "quantity": 7, "price": 6 } },
  { "_id": "abc", "bottomSale": { "quantity": 5, "price": 8 } }
]
```

## Code examples

To view a code example for using the `$bottom` operator, choose the tab for the language that you want to use:

Node.js

```
const { MongoClient } = require('mongodb');

async function example() {
  const uri = 'mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false';
  const client = new MongoClient(uri);

  try {
    await client.connect();

    const db = client.db('test');
    const collection = db.collection('sales');

    const result = await collection.aggregate([
      { $group: { _id: "$item", bottomSale: { $bottom: { sortBy: { quantity: -1 }, output: { quantity: "$quantity", price: "$price" } } } } }
    ]).toArray();

    console.log(result);

  } catch (error) {
    console.error('Error:', error);
  } finally {
    await client.close();
  }
}

example();
```

Python

```
from pymongo import MongoClient
from pprint import pprint

def example():
    client = None
    try:
        client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

        db = client['test']
        collection = db['sales']

        result = list(collection.aggregate([
            { '$group': { '_id': '$item', 'bottomSale': { '$bottom': { 'sortBy': { 'quantity': -1 }, 'output': { 'quantity': '$quantity', 'price': '$price' } } } } }
        ]))

        pprint(result)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if client:
            client.close()

example()
```
