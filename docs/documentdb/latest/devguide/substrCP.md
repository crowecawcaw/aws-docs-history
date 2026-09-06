

# $substrCP
<a name="substrCP"></a>

The `$substrCP` operator in Amazon DocumentDB is used to extract a substring from a string, where the substring is specified as a range of UTF-8 code points (CP). This operator is particularly useful when working with Unicode strings, as it allows you to extract substrings without having to worry about the underlying byte representation of the characters.

Unlike the `$substrBytes` operator, which operates on byte positions, the `$substrCP` operator works with code point positions. This makes it easier to work with strings that contain non-ASCII characters, as the number of code points may not match the number of bytes or characters.

**Parameters**
+ `string`: The input string from which to extract the substring.
+ `start`: The starting code point position (zero-based) from which to extract the substring.
+ `length`: The number of code points to extract.

## Example (MongoDB Shell)
<a name="substrCP-examples"></a>

In this example, we'll use the `$substrCP` operator to extract the state abbreviation from a string containing the employee's desk location.

**Create sample documents**

```
db.people.insert([
  { "_id": 1, "first_name": "Jane", "last_name": "Doe", "Desk": "12 Main St, Minneapolis, MN 55401" },
  { "_id": 2, "first_name": "John", "last_name": "Doe", "Desk": "456 Oak Rd, New Orleans, LA 70032" },
  { "_id": 3, "first_name": "Steve", "last_name": "Smith", "Desk": "789 Elm Ln, Bakersfield, CA 93263" }
]);
```

**Query example**

```
db.people.aggregate([
  {
    $project: {
      "state": { $substrCP: ["$Desk", 25, 2] }
    }
  }
]);
```

**Output**

```
{ "_id" : 1, "state" : "MN" }
{ "_id" : 2, "state" : "LA" }
{ "_id" : 3, "state" : "CA" }
```

In this example, we know that the state abbreviation starts at the 25th code point in the `Desk` field and is 2 code points long. By using the `$substrCP` operator, we can extract the state abbreviation without having to worry about the underlying byte representation of the string.

## Code examples
<a name="substrCP-code"></a>

To view a code example for using the `$substrCP` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function findStates() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const result = await db.collection('people').aggregate([
    {
      $project: {
        "state": { $substrCP: ["$Desk", 25, 2] }
      }
    }
  ]).toArray();
  console.log(result);
  client.close();
}

findStates();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def find_states():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    result = list(db.people.aggregate([
        {
            '$project': {
                'state': { '$substrCP': ['$Desk', 25, 2] }
            }
        }
    ]))
    print(result)
    client.close()

find_states()
```

In both the Node.js and Python examples, we use the `$substrCP` operator to extract the state abbreviation from the `Desk` field, similar to the MongoDB Shell example.

------