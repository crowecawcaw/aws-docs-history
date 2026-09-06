

# $substrBytes
<a name="substrBytes"></a>

The `$substrBytes` operator in Amazon DocumentDB is used to extract a substring from a string based on a specified byte range. This operator is useful when you need to extract a substring from a string and the number of bytes required to represent each character in the string is important.

Unlike `$substrCP`, which operates on the number of Unicode code points, `$substrBytes` operates on the number of bytes required to represent the characters in the string. This can be particularly useful when working with strings that contain non-ASCII characters, as these characters may require more than one byte to represent.

\*Note:\* `$substr` has been deprecated since version 3.4. `$substr` is now an alias for `$substrBytes`.

**Parameters**
+ `string`: The input string from which the substring will be extracted.
+ `startByte`: The zero-based starting byte position of the substring to be extracted. A negative value can be used to specify a position from the end of the string.
+ `length`: The number of bytes in the substring to be extracted.

## Example (MongoDB Shell)
<a name="substrBytes-examples"></a>

In this example, we'll use `$substrBytes` to extract a substring from a string that contains non-ASCII characters.

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
      "state": { $substrBytes: [ "$Desk", 12, 3] }
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

In this example, we use `$substrBytes` to extract a 3-byte substring starting from the 12th byte of the `Desk` field. This allows us to extract the 2-character state abbreviation, even though the string may contain non-ASCII characters.

## Code examples
<a name="substrBytes-code"></a>

To view a code example for using the `$substrBytes` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const people = db.collection('people');

  const result = await people.aggregate([
    {
      $project: {
        "state": { $substrBytes: ["$Desk", 12, 3] }
      }
    }
  ]).toArray();

  console.log(result);
  client.close();
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
    people = db.people

    result = list(people.aggregate([
        {
            '$project': {
                "state": { '$substrBytes': ["$Desk", 12, 3] }
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------