

# $addToSet
<a name="addToSet"></a>

The `$addToSet` operator in Amazon DocumentDB is used to add a value to an array only if the value is not already present in the array. This is useful for ensuring that an array contains unique elements.

**Parameters**
+ `field`: The field to update.
+ `value`: The value to add to the array field. This can be a single value or an expression.

## Example (MongoDB Shell)
<a name="addToSet-examples"></a>

The following example demonstrates how to use the `$addToSet` operator to add unique elements to an array.

**Create sample documents**

```
db.products.insertMany([
  { "_id": 1, "item": "apple", "tags": ["fruit", "red", "round"] },
  { "_id": 2, "item": "banana", "tags": ["fruit", "yellow"] },
  { "_id": 3, "item": "cherry", "tags": ["fruit", "red"] }
])
```

**Query example**

```
db.products.update(
  { "item": "apple" },
  { $addToSet: { "tags": "green" } }
)
```

**Output**

```
{ "_id": 1, "item": "apple", "tags": ["fruit", "red", "round", "green"] }
```

In this example, the `$addToSet` operator adds the "green" tag to the "tags" array of the document where the "item" field is "apple". Since "green" was not already in the array, it was added.

## Code examples
<a name="addToSet-code"></a>

To view a code example for using the `$addToSet` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('products');

  await collection.updateOne(
    { "item": "apple" },
    { $addToSet: { "tags": "green" } }
  );

  const updatedDoc = await collection.findOne({ "item": "apple" });
  console.log(updatedDoc);

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
    collection = db.products

    collection.update_one(
        {"item": "apple"},
        {"$addToSet": {"tags": "green"}}
    )

    updated_doc = collection.find_one({"item": "apple"})
    print(updated_doc)

    client.close()

example()
```

------