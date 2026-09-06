

# $indexOfBytes
<a name="indexOfBytes"></a>

The $indexOfBytes operator in Amazon DocumentDB is used to find the starting index of a substring within a string, based on the byte positions of the characters. This can be useful when working with text data that may contain multi-byte characters, such as those found in non-Latin scripts.

**Parameters**
+ `string`: The input string to search.
+ `substring`: The substring to search for within the input string.
+ `[<start>]`: (optional) The starting position (zero-based) of the search. If not specified, the search starts at the beginning of the string.

## Example (MongoDB Shell)
<a name="indexOfBytes-examples"></a>

The following example demonstrates the use of `$indexOfBytes` to find the index of the first hyphen character in a set of strings representing desk locations.

**Create sample documents**

```
db.people.insertMany([
  { "_id": 1, "Desk": "Düsseldorf-BVV-021" },
  { "_id": 2, "Desk": "Munich-HGG-32a" },
  { "_id": 3, "Desk": "Cologne-ayu-892.50" },
  { "_id": 4, "Desk": "Dortmund-Hop-78" }
]);
```

**Query example**

```
db.people.aggregate([
  { $project: { stateLocation: { $indexOfBytes: ["$Desk", "-"] } } }
]);
```

**Output**

```
{ "_id" : 1, "stateLocation" : 11 }
{ "_id" : 2, "stateLocation" : 6 }
{ "_id" : 3, "stateLocation" : 7 }
{ "_id" : 4, "stateLocation" : 8 }
```

## Code examples
<a name="indexOfBytes-code"></a>

To view a code example for using the `$indexOfBytes` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const events = db.collection('people');

  const result = await db.collection('people').aggregate([
    { $project: { stateLocation: { $indexOfBytes: ["$Desk", "-"] } } }
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
    db = client['test']
    collection = db['people']
    
    result = list(db.people.aggregate([
        { '$project': { 'stateLocation': { '$indexOfBytes': ['$Desk', '-'] } } }
    ]))
    print(result)
    client.close()

example()
```

------