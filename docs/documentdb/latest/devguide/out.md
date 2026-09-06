

# $out
<a name="out"></a>

The `$out` operator in Amazon DocumentDB is used to write the result of an aggregation pipeline to a specified collection.

`$out` should be the last stage in the pipeline.

**Parameters**
+ `output_collection`: The name of the output collection to write the aggregation results to.

**Note**: If the collection already exists, it will be replaced with the results of the aggregation stage.

## Example (MongoDB Shell)
<a name="out-examples"></a>

The following example demonstrates how to use the `$out` operator in Amazon DocumentDB to write the results of an aggregation pipeline to a new collection.

**Create sample documents**

```
db.products.insertMany([
  { _id: 1, name: "Wireless Headphones", category: "Electronics", price: 100.0 },
  { _id: 2, name: "Smartphone", category: "Electronics", price: 200.0 },
  { _id: 3, name: "JavaScript Guide", category: "Books", price: 50.0 },
  { _id: 4, name: "Database Design Handbook", category: "Books", price: 75.0 }
]);
```

**Query example**

```
db.products.aggregate([
  { $group: { _id: "$category", totalPrice: { $sum: "$price" } } },
  { $out: "product_categories" }
])
```

**Output**

None (the results are written to the output collection).

The aggregation pipeline groups the products by category and calculates the total price of the items for each category. The `$out` operator writes the results to a new collection named "product\_categories".

**To view the results in the output collection:**

```
db.product_categories.find()
[
{ "_id" : "Books", "totalPrice" : 125 },
{ "_id" : "Electronics", "totalPrice" : 300 }
]
```

## Code examples
<a name="out-code"></a>

To view a code example for using the `$out` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function demo_out_operator() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const products = db.collection('products');

  // Execute aggregation with $out - results are stored in 'product_categories' collection
  await products.aggregate([
    { $group: { _id: "$category", totalPrice: { $sum: "$price" } } },
    { $out: "product_categories" }
  ]).toArray();

  // Retrieve the results from the output collection (limited to 20 records)
  const productCategories = db.collection('product_categories');
  const results = await productCategories.find({}).limit(20).toArray();
  
  console.log('Results stored in product_categories collection:', results);
  await client.close();
}

demo_out_operator();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def demo_out_operator():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    products = db['products']

    # Execute aggregation with $out - results are stored in 'product_categories' collection
    list(products.aggregate([
        { '$group': { '_id': '$category', 'totalPrice': { '$sum': '$price' } } },
        { '$out': 'product_categories' }
    ]))

    # Retrieve the results from the output collection (limited to 20 records)
    product_categories = db['product_categories']
    results = list(product_categories.find({}).limit(20))
    
    print('Results stored in product_categories collection:', results)
    client.close()

demo_out_operator()
```

------