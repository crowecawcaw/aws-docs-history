

# $lte
<a name="lte"></a>

The `$lte` operator in Amazon DocumentDB is used to match documents where the value of a specified field is less than or equal to the specified value. This operator is useful for filtering and querying data based on numerical comparisons.

**Parameters**
+ `field`: The field to compare.
+ `value`: The value to compare against.

## Example (MongoDB Shell)
<a name="lte-examples"></a>

The following example demonstrates the usage of the `$lte` operator to retrieve documents where the `quantity` field is less than or equal to 10.

**Create sample documents**

```
db.inventory.insertMany([
  { item: "canvas", qty: 100 },
  { item: "paint", qty: 50 },
  { item: "brush", qty: 10 },
  { item: "paper", qty: 5 }
]);
```

**Query example**

```
db.inventory.find({ qty: { $lte: 10 } });
```

**Output**

```
{ "_id" : ObjectId("..."), "item" : "brush", "qty" : 10 },
{ "_id" : ObjectId("..."), "item" : "paper", "qty" : 5 }
```

## Code examples
<a name="lte-code"></a>

To view a code example for using the `$lte` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require("mongodb");

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db("test");
  const collection = db.collection("inventory");

  const result = await collection.find({ qty: { $lte: 10 } }).toArray();
  console.log(result);

  await client.close();
}

main();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client["test"]
    collection = db["inventory"]

    result = list(collection.find({ "qty": { "$lte": 10 } }))
    print(result)

    client.close()

if __name__ == "__main__":
    main()
```

------