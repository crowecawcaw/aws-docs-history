

# $in
<a name="in"></a>

The `$in` operator in Amazon DocumentDB is a logical query operator that allows you to find documents where the value of a field equals any of the values specified in an array.

**Parameters**
+ `field`: The field to check against the provided array.
+ `[value1, value2, ...]`: An array of values to match against the specified field.

 

**Dollar (`$`) in field names**

See [Dollar($) and dot(.) in field names](functional-differences.md#functional-differences-dollardot) for limitations regarding querying `$` prefixed fields in `$in` in nested objects.

## Example (MongoDB Shell)
<a name="in-examples"></a>

The following example demonstrates how to use the `$in` operator to find documents where the `color` field is one of the values in the provided array.

**Create sample documents**

```
db.colors.insertMany([
  { "_id": 1, "color": "red" },
  { "_id": 2, "color": "green" },
  { "_id": 3, "color": "blue" },
  { "_id": 4, "color": "yellow" },
  { "_id": 5, "color": "purple" }
])
```

**Query example**

```
db.colors.find({ "color": { "$in": ["red", "blue", "purple"] } })
```

**Output**

```
{ "_id": 1, "color": "red" },
{ "_id": 3, "color": "blue" },
{ "_id": 5, "color": "purple" }
```

## Code examples
<a name="in-code"></a>

To view a code example for using the `$in` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function findByIn() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('colors');

  const result = await collection.find({ "color": { "$in": ["red", "blue", "purple"] } }).toArray();
  console.log(result);

  await client.close();
}

findByIn();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def find_by_in():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    collection = db.colors

    result = list(collection.find({ "color": { "$in": ["red", "blue", "purple"] } }))
    print(result)

    client.close()

find_by_in()
```

------