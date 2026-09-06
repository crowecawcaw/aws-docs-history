

# $avg
<a name="avg"></a>

The `$avg` aggregation operator in Amazon DocumentDB calculates the average value of the specified expression across the documents that are input to the stage. This operator is useful for computing the average of a numeric field or expression across a set of documents.

**Parameters**
+ `expression`: The expression to use to calculate the average. This can be a field path (e.g. `"$field"`) or an expression (e.g. `{ $multiply: ["$field1", "$field2"] }`).

## Example (MongoDB Shell)
<a name="avg-examples"></a>

The following example demonstrates how to use the `$avg` operator to calculate the average score across a set of student documents.

**Create sample documents**

```
db.students.insertMany([
  { name: "John", score: 85 },
  { name: "Jane", score: 92 },
  { name: "Bob", score: 78 },
  { name: "Alice", score: 90 }
]);
```

**Query example**

```
db.students.aggregate([
  { $group: { 
    _id: null,
    avgScore: { $avg: "$score" }
  }}
]);
```

**Output**

```
[
  {
    "_id": null,
    "avgScore": 86.25
  }
]
```

## Code examples
<a name="avg-code"></a>

To view a code example for using the `$avg` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function calculateAvgScore() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const result = await db.collection('students').aggregate([
    { $group: {
      _id: null,
      avgScore: { $avg: '$score' }
    }}
  ]).toArray();
  console.log(result);
  await client.close();
}

calculateAvgScore();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def calculate_avg_score():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    result = list(db.students.aggregate([
        { '$group': {
            '_id': None,
            'avgScore': { '$avg': '$score' }
        }}
    ]))
    print(result)
    client.close()

calculate_avg_score()
```

------