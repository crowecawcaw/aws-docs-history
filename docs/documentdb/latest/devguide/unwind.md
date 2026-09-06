

# $unwind
<a name="unwind"></a>

The `$unwind` operator is used to deconstruct an array field from the input documents to output a document for each element. This can be useful when you want to perform operations on the individual elements of an array, such as filtering, sorting, or transforming the data.

**Parameters**
+ `path`: The path to the array field to be unwound.
+ `includeArrayIndex`: (optional) Specifies the name of the new field to hold the index of the array element.
+ `preserveNullAndEmptyArrays`: (optional) Determines whether the operation keeps the original document when the array field is null or an empty array.

## Example (MongoDB Shell)
<a name="unwind-examples"></a>

The following example demonstrates how to use the `$unwind` operator to deconstruct an array field and perform further operations on the individual elements.

**Create sample documents**

```
db.people.insertMany([
  { _id: 1, name: "jon", hobbies: ["painting", "dancing", "singing"] },
  { _id: 2, name: "jane", hobbies: ["reading", "swimming"] },
  { _id: 3, name: "jack", hobbies: [] }
])
```

**Query example**

```
db.people.aggregate([
  { $unwind: "$hobbies" }
])
```

**Output**

```
[
  { _id: 1, name: 'jon', hobbies: 'painting' },
  { _id: 1, name: 'jon', hobbies: 'dancing' },
  { _id: 1, name: 'jon', hobbies: 'singing' },
  { _id: 2, name: 'jane', hobbies: 'reading' },
  { _id: 2, name: 'jane', hobbies: 'swimming' }
]
```

## Code examples
<a name="unwind-code"></a>

To view a code example for using the `$unwind` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('people');

  const result = await collection.aggregate([
    { $unwind: '$hobbies' }
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
        { '$unwind': '$hobbies' }
    ]))

    print(result)
    client.close()

example()
```

------