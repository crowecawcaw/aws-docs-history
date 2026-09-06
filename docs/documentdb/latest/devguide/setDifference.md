

# $setDifference
<a name="setDifference"></a>

New from version 4.0.

The `$setDifference` operator in Amazon DocumentDB is used to compare two sets and return the elements that are in the first set but not in the second set. This operator is useful for finding the unique elements between two sets.

**Parameters**
+ `firstSet` : The first set to compare.
+ `secondSet` : The second set to compare.

## Example (MongoDB Shell)
<a name="setDifference-examples"></a>

The following example demonstrates how to use the `$setDifference` operator to find the unique elements between two sets.

**Create sample documents**

```
db.collection.insertMany([
  { _id: 1, fruits: ["apple", "banana", "cherry", "date"] },
  { _id: 2, fruits: ["banana", "cherry", "date", "elderberry"] }
]);
```

**Query example**

```
db.collection.aggregate([
  {
    $project: {
      uniqueFruits: { $setDifference: ["$fruits", ["banana", "cherry", "date"]] }
    }
  }
]);
```

**Output**

```
[
  { "_id": 1, "uniqueFruits": ["apple"] },
  { "_id": 2, "uniqueFruits": ["elderberry"] }
]
```

The query performs the following steps:

1. It uses the `$project` stage to create a new field `uniqueFruits` for each document.

2. The `$setDifference` operator compares the `fruits` array with the array `[&quot;banana&quot;, &quot;cherry&quot;, &quot;date&quot;]` and returns the unique elements in the `fruits` array.

## Code examples
<a name="setDifference-code"></a>

To view a code example for using the `$setDifference` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

Here's an example of how to use the `$setDifference` operator in a Node.js application:

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('mycollection');

  // Insert sample documents
  await collection.insertMany([
    { _id: 1, fruits: ["apple", "banana", "cherry", "date"] },
    { _id: 2, fruits: ["banana", "cherry", "date", "elderberry"] }
  ]);

 // Query using $setDifference
  const result = await collection.aggregate([
    {
      $project: {
        uniqueFruits: { $setDifference: ["$fruits", ["banana", "cherry", "date"]] }
      }
    }
  ]).toArray();

  console.log(result);
  await client.close();
}

main();
```

------
#### [ Python ]

Here's an example of how to use the `$setDifference` operator in a Python application:

```
from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['mycollection']

    # Insert sample documents
    collection.insert_many([
        {'_id': 1, 'fruits': ["apple", "banana", "cherry", "date"]},
        {'_id': 2, 'fruits': ["banana", "cherry", "date", "elderberry"]}
    ])

    # Query using $setDifference
    result = list(collection.aggregate([
        {
            '$project': {
                'uniqueFruits': {'$setDifference': ['$fruits', ["banana", "cherry", "date"]]}
            }
        }
    ]))

    print(result)
    client.close()

if __name__ == '__main__':
    main()
```

------