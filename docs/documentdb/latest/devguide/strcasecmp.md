

# $strcasecmp
<a name="strcasecmp"></a>

The `$strcasecmp` operator in Amazon DocumentDB performs a case-insensitive comparison between two strings. It returns an integer value indicating the lexicographic comparison of the two input strings, ignoring case differences.

**Parameters**
+ `string1`: The first string to compare.
+ `string2`: The second string to compare.

## Example (MongoDB Shell)
<a name="strcasecmp-examples"></a>

This example demonstrates how to use the `$strcasecmp` operator to compare desk location strings in a `people` collection, ignoring case differences.

**Create sample documents**

```
db.people.insertMany([
  { "_id": 1, "Desk": "mke233-wi" },
  { "_id": 2, "Desk": "MKE233-WI" },
  { "_id": 3, "Desk": "mke233-wi" }
]);
```

**Query example**

```
db.people.aggregate([
  {
    $project: {
      item: 1,
      compare: { $strcasecmp: ["$Desk", "mke233-wi"] }
    }
  }
]);
```

**Output**

```
{ "_id" : 1, "compare" : 0 }
{ "_id" : 2, "compare" : 0 }
{ "_id" : 3, "compare" : 0 }
```

The output shows that the comparison between the `&quot;Desk&quot;` field and the string `&quot;mke233-wi&quot;` returns `0` for all three documents, indicating that the strings are equal when case is ignored.

## Code examples
<a name="strcasecmp-code"></a>

To view a code example for using the `$strcasecmp` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('people');

  const result = await collection.aggregate([
    {
      $project: {
        item: 1,
        compare: { $strcasecmp: ["$Desk", "mke233-wi"] }
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
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    collection = db.people

    result = list(collection.aggregate([
        {
            '$project': {
                'item': 1,
                'compare': { '$strcasecmp': ['$Desk', 'mke233-wi'] }
            }
        }
    ]))

    print(result)

    client.close()

example()
```

------