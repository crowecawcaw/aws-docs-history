

# $strLenCP
<a name="strLenCP"></a>

The `$strLenCP` operator in Amazon DocumentDB is used to determine the length of a string expression in code points (Unicode characters). This is useful when you need to know the number of characters in a string, rather than the number of bytes.

**Parameters**
+ `expression`: The string expression for which to return the length in code points.

## Example (MongoDB Shell)
<a name="strLenCP-examples"></a>

The following example demonstrates the usage of the `$strLenCP` operator to determine the length of strings with Unicode characters.

**Create sample documents**

```
db.people.insertMany([
  { "_id": 1, "Desk": "Düsseldorf-BVV-021" },
  { "_id": 2, "Desk": "Munich-HGG-32a" },
  { "_id": 3, "Desk": "Cologne-ayu-892.50" },
  { "_id": 4, "Desk": "Dortmund-Hop-78" }
])
```

**Query example**

```
db.people.aggregate([
  {
    $project: {
      "Desk": 1,
      "length": { $strLenCP: "$Desk" }
    }
  }
])
```

**Output**

```
{ "_id" : 1, "Desk" : "Düsseldorf-BVV-021", "length" : 18 }
{ "_id" : 2, "Desk" : "Munich-HGG-32a", "length" : 14 }
{ "_id" : 3, "Desk" : "Cologne-ayu-892.50", "length" : 18 }
{ "_id" : 4, "Desk" : "Dortmund-Hop-78", "length" : 15 }
```

Notice the difference in the length measurement for the "Düsseldorf-BVV-021" string, which contains a Unicode character (Ü). The `$strLenCP` operator correctly counts the number of Unicode characters, while the `$strLenBytes` operator counts the number of bytes.

## Code examples
<a name="strLenCP-code"></a>

To view a code example for using the `$strLenCP` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

Here's an example of using the `$strLenCP` operator in a Node.js application with the MongoDB driver:

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('people');

  const result = await collection.aggregate([
    {
      $project: {
        "Desk": 1,
        "length": { $strLenCP: "$Desk" }
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

Here's an example of using the `$strLenCP` operator in a Python application with the PyMongo driver:

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    collection = db.people

    result = list(collection.aggregate([
        {
            '$project': {
                "Desk": 1,
                "length": { "$strLenCP": "$Desk" }
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------