

# $bitsAllClear
<a name="bitsAllClear"></a>

The `$bitsAllClear` operator in Amazon DocumentDB is used to match the documents where all the specified bits in a field are cleared (set to 0). This operator can be useful for performing bitwise operations on stored data.

**Parameters**
+ `field`: The field to check for the specified bits being cleared.
+ `value`: The numeric bitmask that specifies which bits should be checked, or a list of bits positions to be checked. A numeric bitmask can be a binary (0b...), decimal, hexadecimal (0x...), octal (0o...), or binary (BinData) form. In a list of bits positions, the position of the least significant bit is 0.

## Example (MongoDB Shell)
<a name="bitsAllClear-examples"></a>

The following example demonstrates the usage of the `$bitsAllClear` operator in Amazon DocumentDB.

**Create sample documents**

```
db.collection.insertMany([
  { _id: 1, bits: 0b1010 },
  { _id: 2, bits: 0b1100 },
  { _id: 3, bits: 0b0101 }
]);
```

**Query example**

```
db.collection.find({
  bits: { $bitsAllClear: 0b0011 }
})
```

**Output**

```
{ "_id" : 2, "bits" : 12 }
```

The query checks if all the bits specified by the bitmask `0b0011` (the two least significant bits) are cleared in the `bits` field. The document with `_id` 2 satisfies this condition, as its `bits` field has those bits cleared.

## Code examples
<a name="bitsAllClear-code"></a>

To view a code example for using the `$bitsAllClear` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('collection');

  const result = await collection.find({
    bits: { $bitsAllClear: 0b0011 }
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
    collection = db['collection']

    result = list(collection.find({
        'bits': { '$bitsAllClear': 0b0011 }
    }))

    print(result)

    client.close()

example()
```

------