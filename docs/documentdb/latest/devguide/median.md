

# $median
<a name="median"></a>

New from version 8.0.1.

The `$median` operator in Amazon DocumentDB calculates the median value of numeric data. As an accumulator, it computes the median of numeric values across documents within a group in the `$group` stage of an aggregation pipeline. As an expression, it calculates the median of an array of numbers.

**Parameters**
+ `input`: An expression that resolves to a numeric value or an array of numeric values.
+ `method`: A string specifying the calculation method. Currently only `"approximate"` is supported, which uses the t-digest algorithm.

## Behavior
<a name="median-behavior"></a>

The `"approximate"` method uses the t-digest algorithm to calculate an approximate median. The result is an existing value from the dataset rather than an interpolation between values. Precision improves as the number of data points increases.

## Example (MongoDB Shell)
<a name="median-examples"></a>

The following example shows how to use the `$median` operator to calculate the median test score per class.

**Create sample documents**

```
db.students.insertMany([
  { class: "A", score: 72 },
  { class: "A", score: 85 },
  { class: "A", score: 90 },
  { class: "A", score: 68 },
  { class: "A", score: 95 },
  { class: "B", score: 80 },
  { class: "B", score: 75 },
  { class: "B", score: 92 },
  { class: "B", score: 88 },
  { class: "B", score: 70 }
]);
```

**Query example**

```
db.students.aggregate([
  { $group: {
      _id: "$class",
      medianScore: { $median: { input: "$score", method: "approximate" } }
    }}
]);
```

**Output**

```
[
  { "_id": "A", "medianScore": 85 },
  { "_id": "B", "medianScore": 80 }
]
```

## Expression usage example (MongoDB Shell)
<a name="median-expression-examples"></a>

The `$median` operator can also be used as an expression within a `$project` stage to compute the median of an array field.

**Create sample documents**

```
db.surveys.insertMany([
  { _id: 1, ratings: [3, 5, 7, 9, 2] },
  { _id: 2, ratings: [10, 20, 30, 40, 50] },
  { _id: 3, ratings: [1, 1, 2, 3, 5] }
]);
```

**Query example**

```
db.surveys.aggregate([
  { $project: {
      medianRating: { $median: { input: "$ratings", method: "approximate" } }
    }}
]);
```

**Output**

```
[
  { "_id": 1, "medianRating": 5 },
  { "_id": 2, "medianRating": 30 },
  { "_id": 3, "medianRating": 2 }
]
```

## Code examples
<a name="median-code"></a>

To view a code example for using the `$median` operator, choose the tab for the language that you want to use. The following examples show both accumulator usage (in `$group`) and expression usage (in `$project`):

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

    // Accumulator usage: median across grouped documents
    const students = db.collection('students');
    const accumulatorResult = await students.aggregate([
      { $group: {
          _id: "$class",
          medianScore: { $median: { input: "$score", method: "approximate" } }
        }}
    ]).toArray();
    console.log('Accumulator result:', accumulatorResult);

    // Expression usage: median of an array field
    const surveys = db.collection('surveys');
    const expressionResult = await surveys.aggregate([
      { $project: {
          medianRating: { $median: { input: "$ratings", method: "approximate" } }
        }}
    ]).toArray();
    console.log('Expression result:', expressionResult);

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

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

    try:
        db = client['test']

        # Accumulator usage: median across grouped documents
        students = db['students']
        accumulator_result = list(students.aggregate([
            { '$group': {
                '_id': '$class',
                'medianScore': { '$median': { 'input': '$score', 'method': 'approximate' } }
            }}
        ]))
        print('Accumulator result:', accumulator_result)

        # Expression usage: median of an array field
        surveys = db['surveys']
        expression_result = list(surveys.aggregate([
            { '$project': {
                'medianRating': { '$median': { 'input': '$ratings', 'method': 'approximate' } }
            }}
        ]))
        print('Expression result:', expression_result)

    finally:
        client.close()

example()
```

------