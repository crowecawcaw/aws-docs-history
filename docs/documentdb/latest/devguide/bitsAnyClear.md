

# $bitsAnyClear
<a name="bitsAnyClear"></a>

The `$bitsAnyClear` operator in Amazon DocumentDB is used to match the documents where any of the specified bit in a field are cleared (set to 0). This can be useful for performing bitwise operations on field values stored in documents.

**Parameters**
+ `field`: The field to check.
+ `value`: The numeric bitmask that specifies which bits should be checked, or a list of bits positions to be checked. A numeric bitmask can be a binary (0b...), decimal, hexadecimal (0x...), octal (0o...), or binary (BinData) form. In a list of bits positions, the position of the least significant bit is 0.

## Example (MongoDB Shell)
<a name="bitsAnyClear-examples"></a>

The following example demonstrates how to use the `$bitsAnyClear` operator to check if any bit is clear in the `status` field of the `items` collection.

**Create sample documents**

```
db.items.insertMany([
  { "_id": 1, "status": 7 },
  { "_id": 2, "status": 15 },
  { "_id": 3, "status": 31 }
]);
```

**Query example**

```
db.items.find({ "status": { $bitsAnyClear: 8 } })
```

**Output**

```
{ "_id" : 1, "status" : 7 }
```

In this example, the query checks for documents where the `status` field has any bits clear (0) in the bitmask `8` (binary `1000`). The document with `status` values of `7` (binary `111`) matches the query, as it has at least one bit clear in the provided bitmask. The matching clear bit is the 4th least significant bit.

## Code examples
<a name="bitsAnyClear-code"></a>

To view a code example for using the `$bitsAnyClear` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('items');

  const result = await collection.find({ "status": { $bitsAnyClear: 8 } }).toArray();
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
    collection = db.items

    result = list(collection.find({ "status": { "$bitsAnyClear": 8 } }))
    print(result)

    client.close()

example()
```

------