# $maxN

New from version 8.0.1.

The `$maxN` operator in Amazon DocumentDB returns the N largest values. When used as an accumulator in a `$group` stage, it returns an array of the N maximum values in each group. When used as an array expression operator, it returns the N maximum elements of an array.

**Parameters**

- `input`: An expression that resolves to the array or field from which to return the maximum `n` values.
- `n`: An expression that resolves to a positive integer specifying how many maximum values to return.

## Behavior

**Array expression operator behavior**

- You cannot specify a value of `n` less than `1`.
- `$maxN` filters out `null` values found in the `input` array.
- If the specified `n` is greater than or equal to the number of elements in the `input` array, `$maxN` returns all elements in the `input` array.
- If `input` resolves to a non-array value, the aggregation operation errors.
- If `input` contains both numeric and string elements, the string elements are sorted before numeric elements according to the BSON comparison order.

**Accumulator behavior**

- When used as an accumulator, `n` must be a positive integral expression that is either a constant or depends on the `_id` value for `$group`.
- `$maxN` filters out null and missing values.
- If the group contains fewer than `n` elements, `$maxN` returns all elements in the group.
- `$maxN` compares input data following the BSON comparison order to determine the appropriate output type. When the input data contains multiple data types, the `$maxN` output type is the highest in the comparison order.

**Output ordering**

`$maxN` returns values in no particular sort order. If guaranteeing a particular sort order is a requirement, use `$topN` instead, or wrap the result with `$sortArray`.

## Example (MongoDB Shell)

The following example shows how to use the `$maxN` accumulator to retrieve the two highest scores for each subject.

**Create sample documents**

```
db.scores.insertMany([
  { subject: "math", score: 85 },
  { subject: "math", score: 72 },
  { subject: "math", score: 93 },
  { subject: "math", score: 68 },
  { subject: "science", score: 90 },
  { subject: "science", score: 78 },
  { subject: "science", score: 65 },
  { subject: "science", score: 88 }
]);
```

**Query example**

```
db.scores.aggregate([
  { $group: { _id: "$subject", highestTwo: { $maxN: { input: "$score", n: 2 } } } }
]);
```

**Output**

```
[
  { "_id": "math", "highestTwo": [85, 93] },
  { "_id": "science", "highestTwo": [88, 90] }
]
```

## Expression usage example (MongoDB Shell)

The `$maxN` operator can also be used as an expression within a `$project` stage to return the N largest elements from an array field.

**Create sample documents**

```
db.readings.insertMany([
  { _id: 1, sensor: "A", values: [45, 12, 78, 3, 56] },
  { _id: 2, sensor: "B", values: [90, 23, 67, 11, 44] }
]);
```

**Query example**

```
db.readings.aggregate([
  { $project: {
      highestThree: { $maxN: { input: "$values", n: 3 } }
    }}
]);
```

**Output**

```
[
  { "_id": 1, "highestThree": [45, 56, 78] },
  { "_id": 2, "highestThree": [44, 90, 67] }
]
```

## Code examples

To view a code example for using the `$maxN` operator, choose the tab for the language that you want to use. The following examples show both accumulator usage (in `$group`) and expression usage (in `$project`):

Node.js

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  try {
    await client.connect();
    const db = client.db('test');

    // Accumulator usage: N largest values per group
    const scores = db.collection('scores');
    const accumulatorResult = await scores.aggregate([
      { $group: { _id: "$subject", highestTwo: { $maxN: { input: "$score", n: 2 } } } }
    ]).toArray();
    console.log('Accumulator result:', accumulatorResult);

    // Expression usage: N largest elements from an array field
    const readings = db.collection('readings');
    const expressionResult = await readings.aggregate([
      { $project: { highestThree: { $maxN: { input: "$values", n: 3 } } } }
    ]).toArray();
    console.log('Expression result:', expressionResult);

  } finally {
    await client.close();
  }
}

example();
```

Python

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

    try:
        db = client['test']

        # Accumulator usage: N largest values per group
        scores = db['scores']
        accumulator_result = list(scores.aggregate([
            { '$group': { '_id': '$subject', 'highestTwo': { '$maxN': { 'input': '$score', 'n': 2 } } } }
        ]))
        print('Accumulator result:', accumulator_result)

        # Expression usage: N largest elements from an array field
        readings = db['readings']
        expression_result = list(readings.aggregate([
            { '$project': { 'highestThree': { '$maxN': { 'input': '$values', 'n': 3 } } } }
        ]))
        print('Expression result:', expression_result)

    finally:
        client.close()

example()
```
