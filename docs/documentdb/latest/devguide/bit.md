

# $bit
<a name="bit"></a>

The `$bit` operator in Amazon DocumentDB allows you to perform bitwise operations on the bits of a given field. This can be useful for tasks like setting, clearing, or checking the state of individual bits within a number.

**Parameters**
+ `field`: The field to perform bitwise operations on.
+ `and`: An integer value that is used to perform a bitwise AND operation on the field.
+ `or`: An integer value that is used to perform a bitwise OR operation on the field.
+ `xor`: An integer value that is used to perform a bitwise XOR operation on the field.

## Example (MongoDB Shell)
<a name="bit-examples"></a>

The following example demonstrates how to use the `$bit` operator to perform bitwise operations on a numerical field.

**Create sample documents**

```
db.numbers.insert([
  { "_id": 1, "number": 5 },
  { "_id": 2, "number": 12 }
])
```

**Query example**

```
db.numbers.update(
  { "_id": 1 },
  { "$bit": { "number": { "and": 3 } } }
)
```

**Output**

```
{
  "_id": 1,
  "number": 1
}
```

In this example, the `$bit` operator is used to perform a bitwise AND operation on the "number" field of the document with the `_id` of 1. The result is that the value of the "number" field is set to 1, which is the result of the bitwise AND operation between the original value of 5 and the value 3.

## Code examples
<a name="bit-code"></a>

To view a code example for using the `$bit` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('numbers');

  await collection.updateOne(
    { "_id": 1 },
    { "$bit": { "number": { "and": 3 } } }
  );

  const result = await collection.findOne({ "_id": 1 });
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
collection = db['numbers']

collection.update_one(
    {"_id": 1},
    {"$bit": {"number": {"and": 3}}}
)

result = collection.find_one({"_id": 1})
print(result)

client.close()
```

------