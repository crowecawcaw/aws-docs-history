

# $bitsAnySet
<a name="bitsAnySet"></a>

The `$bitsAnySet` operator in Amazon DocumentDB is used to query documents where at least one bit is set to 1 in the specified bits in a field. This operator allows you to perform bitwise operations on the values stored in fields, enabling efficient querying and analysis of data with bitwise characteristics.

**Parameters**
+ `field`: The field name to apply the bitwise operation to.
+ `value`: The numeric bitmask that specifies which bits should be checked, or a list of bits positions to be checked. A numeric bitmask can be a binary (0b...), decimal, hexadecimal (0x...), octal (0o...), or binary (BinData) form. In a list of bits positions, the position of the least significant bit is 0.

## Example (MongoDB Shell)
<a name="bitsAnySet-examples"></a>

The following example demonstrates how to use the `$bitsAnySet` operator to find documents where at least one bit is set in the `flags` field.

**Create sample documents**

```
db.collection.insertMany([
  { _id: 1, flags: 0b1010 },
  { _id: 2, flags: 0b1100 },
  { _id: 3, flags: 0b0011 },
  { _id: 4, flags: 0b0100 }
]);
```

**Query example**

```
db.collection.find({
  flags: { $bitsAnySet: 0b1010 }
})
```

**Output**

```
{ "_id" : 1, "flags" : 10 }
{ "_id" : 2, "flags" : 12 }
{ "_id" : 3, "flags" : 3 }
```

The query returns the documents where at least one of the bits specified in the bitmask `0b1010` is set in the `flags` field.

## Code examples
<a name="bitsAnySet-code"></a>

To view a code example for using the `$bitsAnySet` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('collection');

  const result = await collection.find({
    flags: { $bitsAnySet: 0b1010 }
  }).toArray();

  console.log(result);

  await client.close();
}

main();
```

------
#### [ Python ]

```
from pymongo import MongoClient

client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
db = client['test']
collection = db['collection']

result = list(collection.find({
    'flags': { '$bitsAnySet': 0b1010 }
}))

print(result)

client.close()
```

------