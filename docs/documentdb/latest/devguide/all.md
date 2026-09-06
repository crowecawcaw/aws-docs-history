

# $all
<a name="all"></a>

The `$all` operator in Amazon DocumentDB is used to match documents where the value of a field is an array and contains all the specified elements, regardless of the order of the elements in the array.

**Parameters**
+ `field`: The name of the field to check.
+ `[value1, value2, ...]`: The list of values to match in the array.

 

**Using `$elemMatch` within an `$all` expression**

See [Using `$elemMatch` within an `$all` expression](functional-differences.md#functional-differences.elemMatch) for limitations regarding the use of the `$elemMatch` operator within an `$all` expression.

 

**Dollar ($) in field names**

See [Dollar($) and dot(.) in field names](functional-differences.md#functional-differences-dollardot) for limitations regarding querying `$` prefixed fields in `$all` in nested objects.

## Example (MongoDB Shell)
<a name="all-examples"></a>

The following example demonstrates the usage of the `$all` operator to retrieve documents where the "Colors" field is an array that contains both "Red" and "Blue".

**Create sample documents**

```
db.example.insertMany([
  { "Item": "Pen", "Colors": ["Red", "Blue", "Green"] },
  { "Item": "Notebook", "Colors": ["Blue", "White"] },
  { "Item": "Poster Paint", "Colors": ["Red", "Yellow", "White"] }
])
```

**Query example**

```
db.example.find({ "Colors": { $all: ["Red", "Blue"] } }).pretty()
```

**Output**

```
{
  "_id" : ObjectId("6137d6c5b3a1d35e0b6ee6ad"),
  "Item" : "Pen",
  "Colors" : [ 
          "Red", 
          "Blue", 
          "Green" 
  ]
}
```

## Code examples
<a name="all-code"></a>

To view a code example for using the `$all` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('example');

  const result = await collection.find({ "Colors": { $all: ["Red", "Blue"] } }).toArray();
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
    collection = db['example']

    result = list(collection.find({ "Colors": { "$all": ["Red", "Blue"] } }))
    print(result)

    client.close()

example()
```

------