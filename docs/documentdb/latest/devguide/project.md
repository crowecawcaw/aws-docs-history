

# $project
<a name="project"></a>

The `$project` operator in Amazon DocumentDB allows you to selectively include or exclude fields from output documents, pass values to the next pipeline stage, and compute new fields from input document values.

**Parameters**
+ `field`: The field to include or exclude from the output documents, it can be a field path (e.g., "a.b.c").
+ `1` or `true`: Includes the field in the output.
+ `0` or `false`: Excludes the field from the output.

## Example (MongoDB Shell)
<a name="project-examples"></a>

The following example demonstrates the usage of the `$project` operator on students collection

**Create sample documents**

```
db.students.insertMany([
  { "_id": 1, "name": "Alejandro Rosalez", "math": 85, "science": 92, "grade": "A" },
  { "_id": 2, "name": "Carlos Salazar", "math": 78, "science": 84, "grade": "B" },
  { "_id": 3, "name": "Nikhil Jayashankar", "math": 95, "science": 89, "grade": "A" },
  { "_id": 4, "name": "Shirley Rodriguez", "math": 72, "science": 76, "grade": "B" }
  ]);
```

This query includes only the `name` and `math` fields in the output. The `_id` field is included by default unless explicitly excluded.

```
db.students.aggregate([
  { $project: { "name": 1, "math": 1 } }
])
```

**Output**

```
{ _id: 1, name: "Alejandro Rosalez", math: 85 }
{ _id: 2, name: "Carlos Salazar", math: 78 }
{ _id: 3, name: "Nikhil Jayashankar", math: 95 }
{ _id: 4, name: "Shirley Rodriguez", math: 72 }
```

This query excludes the `grade` and `_id` fields from the output, showing all other fields (`name`, `math`, `science`).

```
db.students.aggregate([
  { $project: { "grade": 0, "_id": 0 } }
])
```

**Output**

```
{ name: "Alejandro Rosalez", math: 85, science: 92 }
{ name: "Carlos Salazar", math: 78, science: 84 }
{ name: "Nikhil Jayashankar", math: 95, science: 89 }
{ name: "Shirley Rodriguez", math: 72, science: 76 }
```

## Code examples
<a name="project-code"></a>

To view a code example for using the `$project` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('students');

  const result = await collection.aggregate([
    { $project: { "name": 1, "math": 1 } }
  ]).toArray();
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
    collection = db['students']

    result = list(collection.aggregate([
        { '$project': { 'name': 1, 'math': 1 } }
    ]))
    print(result)

    client.close()

example()
```

------