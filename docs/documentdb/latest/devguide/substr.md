

# $substr
<a name="substr"></a>

The `$substr` operator in Amazon DocumentDB is used to extract a substring from a given string. It is particularly useful when you need to define substrings based on a range of characters, rather than a range of bytes. This is especially important when dealing with Unicode strings, where the number of bytes used to represent a character can vary.

**Parameters**
+ `string`: The input string from which to extract the substring.
+ `start`: The starting position (zero-based) of the substring to be extracted. Can be a non-negative integer expression.
+ `length`: The number of characters in the extracted substring. Can be a non-negative integer expression.

## Example (MongoDB Shell)
<a name="substr-examples"></a>

In this example, we'll demonstrate the use of `$substr` to extract the state abbreviation from an employee's desk location.

**Create sample documents**

```
db.people.insertMany([
  { "_id": 1, "Desk": "Düsseldorf-NRW-021" },
  { "_id": 2, "Desk": "Bremerhaven-HBB-32a" },
  { "_id": 3, "Desk": "Norderstedt-SHH-892.50" },
  { "_id": 4, "Desk": "Brandenburg-BBB-78" }
]);
```

**Query example**

```
db.people.aggregate([
  {
    $project: {
      "state": { $substr: ["$Desk", 12, 3] }
    }
  }
])
```

**Output**

```
{ "_id": 1, "state": "NRW" },
{ "_id": 2, "state": "HBB" },
{ "_id": 3, "state": "SHH" },
{ "_id": 4, "state": "BBB" }
```

## Code examples
<a name="substr-code"></a>

To view a code example for using the `$substr` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require("mongodb");

async function example() {
  const client = await MongoClient.connect("mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false");
  const db = client.db("test");
  const collection = db.collection("people");

  const result = await collection.aggregate([
    {
      $project: {
        "state": { $substrCP: ["$Desk", 12, 3] }
      }
    }
  ]).toArray();

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
    client = MongoClient("mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false")
    db = client["test"]
    collection = db["people"]

    result = list(collection.aggregate([
        {
            "$project": {
                "state": { "$substrCP": ["$Desk", 12, 3] }
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------