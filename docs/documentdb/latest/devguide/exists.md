

# $exists
<a name="exists"></a>

The `$exists` operator is used to check whether a field exists in a document or not. `$exists` particularly useful when working with sparse indexes in Amazon DocumentDB, where the indexed field may not be present in all documents.

To use a sparse index that you have created in a query, you must use the `$exists` clause on the fields that cover the index. If you omit `$exists`, Amazon DocumentDB will not use the sparse index for the query.

**Parameters**
+ `field`: The field name to check for existence.
+ `value`: A boolean value (`true` or `false`) that specifies whether the field should exist (`true`) or not exist (`false`) in the matching documents.

## Example (MongoDB Shell)
<a name="exists-examples"></a>

The following example demonstrates the use of the `$exists` operator with a sparse index on the `special_diets` field in the `food` collection.

**Create sample documents**

```
db.food.insertMany([
  { _id: 1, name: "Apple", special_diets: ["vegetarian", "gluten-free"] },
  { _id: 2, name: "Broccoli" },
  { _id: 3, name: "Chicken", special_diets: ["dairy-free"] }
]);
```

**Create a sparse index on the `special\_diets` field**

```
db.food.createIndex({ "special_diets": 1 }, { sparse: true, name: "special_diets_sparse_asc" });
```

**Query example**

```
db.food.find({ "special_diets": { $exists: true } });
```

**Output**

```
[
  { "_id" : 1, "name" : "Apple", "special_diets" : [ "vegetarian", "gluten-free" ] },
  { "_id" : 3, "name" : "Chicken", "special_diets" : [ "dairy-free" ] }
]
```

## Code examples
<a name="exists-code"></a>

To view a code example for using the `$exists` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('food');

  const result = await collection.find({ "special_diets": { $exists: true } }).toArray();
  console.log(result);

  await client.close();
}

main();
```

------
#### [ Python ]

```
import pymongo

client = pymongo.MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
db = client['test']
collection = db['food']

result = list(collection.find({"special_diets": {"$exists": True}}))
print(result)

client.close()
```

------