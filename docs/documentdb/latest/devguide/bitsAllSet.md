

# $bitsAllSet
<a name="bitsAllSet"></a>

The `$bitsAllSet` operator in Amazon DocumentDB is used to query for documents where a specific set of bits are all set to 1 in a field. This operator allows you to perform bitwise operations on field values and can be useful when you need to check the state of individual bits within a numeric value.

**Parameters**
+ `field`: The name of the numeric field to perform the bitwise operation on.
+ `value`: The numeric bitmask that specifies which bits should be checked, or a list of bits positions to be checked. A numeric bitmask can be a binary (0b...), decimal, hexadecimal (0x...), octal (0o...), or binary (BinData) form. In a list of bits positions, the position of the least significant bit is 0.

## Example (MongoDB Shell)
<a name="bitsAllSet-examples"></a>

The following example demonstrates how to use the `$bitsAllSet` operator to find documents where the `flags` field has all the bits set that are specified by the bitmask.

**Create sample documents**

```
db.collection.insert([
  { _id: 1, flags: 0b1010 },
  { _id: 2, flags: 0b1100 },
  { _id: 3, flags: 0b1110 }
])
```

**Query example**

```
db.collection.find({ flags: { $bitsAllSet: 0b1100 } })
```

**Output**

```
{ "_id": 2, "flags": 12 },
{ "_id": 3, "flags": 14 }
```

In this example, the query checks for documents where the `flags` field has all the bits set that are specified by the bitmask `0b1100` (which represents the decimal value 12). The documents with `_id` 2 and 3 match this criteria, as their `flags` field values have all the required bits set (the 3rd and 4th least significant bits).

## Code examples
<a name="bitsAllSet-code"></a>

To view a code example for using the `$bitsAllSet` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function findWithBitsAllSet() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('collection');

  const result = await collection.find({ flags: { $bitsAllSet: 0b1100 } }).toArray();
  console.log(result);

  await client.close();
}

findWithBitsAllSet();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def find_with_bits_all_set():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    collection = db.collection

    result = list(collection.find({ 'flags': { '$bitsAllSet': 0b1100 } }))
    print(result)

    client.close()

find_with_bits_all_set()
```

------