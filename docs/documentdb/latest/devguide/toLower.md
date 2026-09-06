

# $toLower
<a name="toLower"></a>

The `$toLower` operator in Amazon DocumentDB is used to convert a string to lowercase.

**Parameters**
+ `expression`: The string expression to convert to lowercase.

## Example (MongoDB Shell)
<a name="toLower-examples"></a>

The following example demonstrates how to use the `$toLower` operator to convert the `Desk` field to lowercase.

**Create sample documents**

```
db.locations.insertMany([
  { "_id": 1, "Desk": "Düsseldorf-BVV-021" },
  { "_id": 2, "Desk": "Munich-HGG-32a" }
]);
```

**Query example**

```
db.locations.aggregate([
  { $project: { item: { $toLower: "$Desk" } } }
]);
```

**Output**

```
{ "_id" : 1, "item" : "düsseldorf-bvv-021" }
{ "_id" : 2, "item" : "munich-hgg-32a" }
```

## Code examples
<a name="toLower-code"></a>

To view a code example for using the `$toLower` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require("mongodb");

async function main() {
  const client = await MongoClient.connect("mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false");
  const db = client.db("test");
  const collection = db.collection("locations");

  const result = await collection.aggregate([
    { $project: { item: { $toLower: "$Desk" } } }
  ]).toArray();

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
    client = MongoClient("mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false")
    db = client["test"]
    collection = db["locations"]

    result = list(collection.aggregate([
        { "$project": { "item": { "$toLower": "$Desk" } } }
    ]))

    print(result)

    client.close()

if __name__ == "__main__":
    main()
```

------