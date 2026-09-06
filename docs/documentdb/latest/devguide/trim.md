

# $trim
<a name="trim"></a>

New from version 4.0

The `$trim` operator in Amazon DocumentDB is used to remove leading and/or trailing whitespace characters from a string.

**Parameters**
+ `input`: The string expression to trim.
+ `chars`: (optional) Specifies the characters to trim from the beginning and end of the input, the default is whitespace.

## Example (MongoDB Shell)
<a name="trim-examples"></a>

The following example demonstrates how to use the `$trim` operator to remove leading and trailing whitespace from a string.

**Create sample documents**

```
db.people.insertMany([
  { "name": "   John Doe   " },
  { "name": "   Bob Johnson   " }
])
```

**Query example**

```
db.people.aggregate([
  { $project: {
    "name": { $trim: {input: "$name"}}
  }}
])
```

**Output**

```
[
  { "name": "John Doe" },
  { "name": "Bob Johnson" }
]
```

## Code examples
<a name="trim-code"></a>

To view a code example for using the `$trim` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('people');

  const result = await collection.aggregate([
    { $project: {
      "name": { $trim: {input: "$name" }}
    }}
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
    db = client['test']
    collection = db['people']

    result = list(collection.aggregate([
        {"$project": {
            "name": {"$trim": {"input": "$name"}}
        }}
    ]))

    print(result)
    client.close()

example()
```

------