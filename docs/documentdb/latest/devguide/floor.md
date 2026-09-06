

# $floor
<a name="floor"></a>

New from version 4.0.

The `$floor` operator in Amazon DocumentDB returns the largest integer that is less than or equal to the specified number. This operator is useful for rounding down numeric values.

**Parameters**
+ `expression`: The numeric expression to round down.

## Example (MongoDB Shell)
<a name="floor-examples"></a>

The following example demonstrates the use of the `$floor` operator to round a decimal value down to the nearest integer.

**Create sample documents**

```
db.numbers.insertOne({ value: 3.14 });
```

**Query example**

```
db.numbers.aggregate([
  { $project: { _id: 0, floored: { $floor: "$value" } } }
]);
```

**Output**

```
{ "floored" : 3 }
```

## Code examples
<a name="floor-code"></a>

To view a code example for using the `$floor` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const uri = 'mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false';
  const client = new MongoClient(uri);

  try {
    await client.connect();

    const db = client.db('test');
    const collection = db.collection('numbers');

    const result = await collection.aggregate([
      { $project: { _id: 0, floored: { $floor: "$value" } } }
    ]).toArray();

    console.log(result);

  } catch (error) {
    console.error('Error:', error);
  } finally {
    await client.close();
  }
}

example();
```

------
#### [ Python ]

```
from pymongo import MongoClient
from pprint import pprint

def example():
    client = None
    try:
        client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

        db = client.test
        collection = db.numbers

        result = list(collection.aggregate([
            { '$project': { '_id': 0, 'floored': { '$floor': '$value' }}}
        ]))

        pprint(result)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if client:
            client.close()

example()
```

------