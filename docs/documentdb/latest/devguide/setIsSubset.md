

# $setIsSubset
<a name="setIsSubset"></a>

The `$setIsSubset` operator in Amazon DocumentDB is used to determine if a set of values is a subset of another set. It is useful for performing set-based comparisons and operations on array fields.

**Parameters**
+ `field`: The field to apply the `$setIsSubset` operator to.
+ `set`: The set to compare the field against.

## Example (MongoDB Shell)
<a name="setIsSubset-examples"></a>

The following example demonstrates the usage of the `$setIsSubset` operator to check if the `tags` field is a subset of the specified set.

**Create sample documents**

```
db.products.insertMany([
  { _id: 1, name: "Product A", tags: ["tag1", "tag2", "tag3"] },
  { _id: 2, name: "Product B", tags: ["tag1", "tag2"] },
  { _id: 3, name: "Product C", tags: ["tag2", "tag3"] }
]);
```

**Query example**

```
db.products.find({
  $expr: { $setIsSubset: [["tag1", "tag2"], "$tags"] }
})
```

\*Note:\* `$setIsSubset` is an aggregation operator and cannot be used directly in find() queries. In this example, `$expr` is used with `find()` to bridge the gap between query operators and aggregation expressions.

**Output**

```
[
  { "_id" : 1, "name" : "Product A", "tags" : [ "tag1", "tag2", "tag3" ] },
  { "_id" : 2, "name" : "Product B", "tags" : [ "tag1", "tag2" ] }
]
```

The query returns the documents where the `tags` field is a subset of the set `[&quot;tag1&quot;, &quot;tag2&quot;]`.

## Code examples
<a name="setIsSubset-code"></a>

To view a code example for using the `$setIsSubset` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('products');

  const result = await collection.find({
    $expr: { $setIsSubset: [["tag1", "tag2"], "$tags"] }
  }).toArray();

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

    result = list(collection.find({
        '$expr': {'$setIsSubset': [['tag1', 'tag2'], '$tags']}
    }))

    print(result)

    client.close()

example()
```

------