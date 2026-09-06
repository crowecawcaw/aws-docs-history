

# $percentile
<a name="percentile"></a>

New from version 8.0.1.

The `$percentile` operator in Amazon DocumentDB calculates specified percentile values for numeric data. As an accumulator, it computes percentile values across documents within a group in the `$group` stage of an aggregation pipeline. As an expression, it calculates percentiles for an array of numbers.

**Parameters**
+ `input`: An expression that resolves to a numeric value or an array of numeric values.
+ `p`: An array of percentile values between 0 and 1, where each value represents a percentile to calculate. For example, `[0.25, 0.5, 0.75]` calculates the 25th, 50th, and 75th percentiles.
+ `method`: A string specifying the calculation method. Currently only `"approximate"` is supported.

## Behavior
<a name="percentile-behavior"></a>

The `"approximate"` method uses the t-digest algorithm to calculate approximate, percentile-based metrics. With small datasets, distinct percentile values may resolve to the same result. For example, with only 5 values per group, p90 and p99 may both return the maximum value in the group. Precision improves as the number of data points increases.

## Example (MongoDB Shell)
<a name="percentile-examples"></a>

The following example shows how to use the `$percentile` operator to calculate the 25th and 75th percentile of scores per class.

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
      percentiles: { $percentile: { input: "$score", p: [0.25, 0.75], method: "approximate" } }
    }}
]);
```

**Output**

```
[
  { "_id": "A", "percentiles": [72, 90] },
  { "_id": "B", "percentiles": [75, 88] }
]
```

## Expression usage example (MongoDB Shell)
<a name="percentile-expression-examples"></a>

The `$percentile` operator can also be used as an expression within a `$project` stage to compute percentiles of an array field.

**Create sample documents**

```
db.surveys.insertMany([
  { _id: 1, responses: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] },
  { _id: 2, responses: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] }
]);
```

**Query example**

```
db.surveys.aggregate([
  { $project: {
      quartiles: { $percentile: { input: "$responses", p: [0.25, 0.5, 0.75], method: "approximate" } }
    }}
]);
```

**Output**

```
[
  { "_id": 1, "quartiles": [6, 10, 16] },
  { "_id": 2, "quartiles": [5, 9, 15] }
]
```

## Code examples
<a name="percentile-code"></a>

To view a code example for using the `$percentile` operator, choose the tab for the language that you want to use. The following examples show both accumulator usage (in `$group`) and expression usage (in `$project`):

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

    // Accumulator usage: percentiles across grouped documents
    const students = db.collection('students');
    const accumulatorResult = await students.aggregate([
      { $group: {
          _id: "$class",
          percentiles: { $percentile: { input: "$score", p: [0.25, 0.75], method: "approximate" } }
        }}
    ]).toArray();
    console.log('Accumulator result:', accumulatorResult);

    // Expression usage: percentiles of an array field
    const surveys = db.collection('surveys');
    const expressionResult = await surveys.aggregate([
      { $project: {
          quartiles: { $percentile: { input: "$responses", p: [0.25, 0.5, 0.75], method: "approximate" } }
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

        # Accumulator usage: percentiles across grouped documents
        students = db['students']
        accumulator_result = list(students.aggregate([
            { '$group': {
                '_id': '$class',
                'percentiles': { '$percentile': { 'input': '$score', 'p': [0.25, 0.75], 'method': 'approximate' } }
            }}
        ]))
        print('Accumulator result:', accumulator_result)

        # Expression usage: percentiles of an array field
        surveys = db['surveys']
        expression_result = list(surveys.aggregate([
            { '$project': {
                'quartiles': { '$percentile': { 'input': '$responses', 'p': [0.25, 0.5, 0.75], 'method': 'approximate' } }
            }}
        ]))
        print('Expression result:', expression_result)

    finally:
        client.close()

example()
```

------