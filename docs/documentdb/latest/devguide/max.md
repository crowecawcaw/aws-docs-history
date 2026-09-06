

# $max
<a name="max"></a>

The `$max` aggregation stage is used to return the maximum value of a specified field across all documents in a pipeline stage. This operator is useful for finding the highest value in a set of documents.

**Parameters**
+ `expression`: The expression to use to calculate the maximum value.

## Example (MongoDB Shell)
<a name="max-examples"></a>

The following example demonstrates how to use the `$max` operator to find the maximum score in a collection of student documents. The `$group` stage groups all documents together, and the `$max` operator is used to calculate the maximum value of the `score` field across all documents.

**Create sample documents**

```
db.students.insertMany([
  { name: "John", score: 85 },
  { name: "Jane", score: 92 },
  { name: "Bob", score: 78 },
  { name: "Alice", score: 90 }
])
```

**Query example**

```
db.students.aggregate([
  { $group: { _id: null, maxScore: { $max: "$score" } } },
  { $project: { _id: 0, maxScore: 1 } }
])
```

**Output**

```
[ { maxScore: 92 } ]
```

## Code examples
<a name="max-code"></a>

To view a code example for using the `$max` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function findMaxScore() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const students = db.collection('students');

  const result = await students.aggregate([
    { $group: { _id: null, maxScore: { $max: "$score" } } }
  ]).toArray();

  console.log(result);
  await client.close();
}

findMaxScore();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def find_max_score():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    students = db.students

    result = list(students.aggregate([
        { "$group": { "_id": None, "maxScore": { "$max": "$score" } } }
    ]))

    print(result)
    client.close()

find_max_score()
```

------