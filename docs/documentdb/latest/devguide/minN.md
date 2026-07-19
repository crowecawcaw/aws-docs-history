# $minN

New from version 8.0.1.

The `$minN` operator in Amazon DocumentDB returns the N smallest values. When used as an accumulator in a `$group` stage, it returns an array of the N minimum values in each group. When used as an array expression operator, it returns the N minimum elements of an array.

**Parameters**

- `input`: An expression that resolves to the array or field from which to return the minimum `n` values.
- `n`: An expression that resolves to a positive integer specifying how many minimum values to return.

## Behavior

**Array expression operator behavior**

- You cannot specify a value of `n` less than `1`.
- `$minN` filters out `null` values found in the `input` array.
- If the specified `n` is greater than or equal to the number of elements in the `input` array, `$minN` returns all elements in the `input` array.
- If `input` resolves to a non-array value, the aggregation operation errors.
- If `input` contains both numeric and string elements, the numeric elements are sorted before string elements according to the BSON comparison order.

**Accumulator behavior**

- When used as an accumulator, `n` must be a positive integral expression that is either a constant or depends on the `_id` value for `$group`.
- `$minN` filters out null and missing values.
- If the group contains fewer than `n` elements, `$minN` returns all elements in the group.
- `$minN` compares input data following the BSON comparison order to determine the appropriate output type. When the input data contains multiple data types, the `$minN` output type is the lowest in the comparison order.

**Output ordering**

`$minN` returns values in no particular sort order. If guaranteeing a particular sort order is a requirement, use `$bottomN` instead, or wrap the result with `$sortArray`.

## Example (MongoDB Shell)

The following example demonstrates the use of the `$minN` accumulator to retrieve the two lowest scores for each subject.

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
  { $group: { _id: "$subject", lowestTwo: { $minN: { input: "$score", n: 2 } } } }
]);
```

**Output**

```
[
  { "_id": "math", "lowestTwo": [72, 68] },
  { "_id": "science", "lowestTwo": [78, 65] }
]
```

## Expression usage example (MongoDB Shell)

The `$minN` operator can also be used as an expression within a `$project` stage to return the N smallest elements from an array field.

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
      lowestThree: { $minN: { input: "$values", n: 3 } }
    }}
]);
```

**Output**

```
[
  { "_id": 1, "lowestThree": [45, 12, 3] },
  { "_id": 2, "lowestThree": [44, 23, 11] }
]
```

## Code examples

To view a code example for using the `$minN` operator, choose the tab for the language that you want to use. The following examples show both accumulator usage (in `$group`) and expression usage (in `$project`):

Node.js

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  try {
    await client.connect();
    const db = client.db('test');

    // Accumulator usage: N smallest values per group
    const scores = db.collection('scores');
    const accumulatorResult = await scores.aggregate([
      { $group: { _id: "$subject", lowestTwo: { $minN: { input: "$score", n: 2 } } } }
    ]).toArray();
    console.log('Accumulator result:', accumulatorResult);

    // Expression usage: N smallest elements from an array field
    const readings = db.collection('readings');
    const expressionResult = await readings.aggregate([
      { $project: { lowestThree: { $minN: { input: "$values", n: 3 } } } }
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

        # Accumulator usage: N smallest values per group
        scores = db['scores']
        accumulator_result = list(scores.aggregate([
            { '$group': { '_id': '$subject', 'lowestTwo': { '$minN': { 'input': '$score', 'n': 2 } } } }
        ]))
        print('Accumulator result:', accumulator_result)

        # Expression usage: N smallest elements from an array field
        readings = db['readings']
        expression_result = list(readings.aggregate([
            { '$project': { 'lowestThree': { '$minN': { 'input': '$values', 'n': 3 } } } }
        ]))
        print('Expression result:', expression_result)

    finally:
        client.close()

example()
```
