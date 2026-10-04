

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

## Window operator usage example (MongoDB Shell)
<a name="median-window"></a>

New from version 8.0.2.

The `$median` operator can also be used as a window operator in the `$setWindowFields` stage. In this context, it computes the median of the numeric values for the documents in each window. You specify the operator under the `output` field, and optionally define the window boundaries with a `window` document.

**Note**  
When used as a window operator in `$setWindowFields`, `$median` is limited to 100 MB of intermediate data. An operation that exceeds this limit returns an error.

**Create sample documents**

```
db.temperatures.insertMany([
  { _id: 1, city: "A", reading: 60 },
  { _id: 2, city: "A", reading: 65 },
  { _id: 3, city: "A", reading: 70 },
  { _id: 4, city: "B", reading: 80 },
  { _id: 5, city: "B", reading: 85 },
  { _id: 6, city: "B", reading: 90 }
]);
```

**Query example**

The following example partitions the documents by `city` and computes the median `reading` across all documents in each partition.

```
db.temperatures.aggregate([
  {
    $setWindowFields: {
      partitionBy: "$city",
      output: {
        medianReading: {
          $median: { input: "$reading", method: "approximate" },
          window: { documents: ["unbounded", "unbounded"] }
        }
      }
    }
  }
]);
```

**Output**

```
[
  { "_id": 1, "city": "A", "reading": 60, "medianReading": 65 },
  { "_id": 2, "city": "A", "reading": 65, "medianReading": 65 },
  { "_id": 3, "city": "A", "reading": 70, "medianReading": 65 },
  { "_id": 4, "city": "B", "reading": 80, "medianReading": 85 },
  { "_id": 5, "city": "B", "reading": 85, "medianReading": 85 },
  { "_id": 6, "city": "B", "reading": 90, "medianReading": 85 }
]
```

Each document is augmented with `medianReading`, the approximate median of `reading` across all documents in its partition.

## Code examples
<a name="median-code"></a>

To view a code example for using the `$median` operator, choose the tab for the language that you want to use. The following examples show accumulator usage (in `$group`), expression usage (in `$project`), and window operator usage (in `$setWindowFields`):

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
    await students.insertMany([
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
    const accumulatorResult = await students.aggregate([
      { $group: {
          _id: "$class",
          medianScore: { $median: { input: "$score", method: "approximate" } }
        }}
    ]).toArray();
    console.log('Accumulator result:', accumulatorResult);

    // Expression usage: median of an array field
    const surveys = db.collection('surveys');
    await surveys.insertMany([
      { _id: 1, ratings: [3, 5, 7, 9, 2] },
      { _id: 2, ratings: [10, 20, 30, 40, 50] },
      { _id: 3, ratings: [1, 1, 2, 3, 5] }
    ]);
    const expressionResult = await surveys.aggregate([
      { $project: {
          medianRating: { $median: { input: "$ratings", method: "approximate" } }
        }}
    ]).toArray();
    console.log('Expression result:', expressionResult);

    // Window operator usage: median across each partition
    const temperatures = db.collection('temperatures');
    await temperatures.insertMany([
      { _id: 1, city: "A", reading: 60 },
      { _id: 2, city: "A", reading: 65 },
      { _id: 3, city: "A", reading: 70 },
      { _id: 4, city: "B", reading: 80 },
      { _id: 5, city: "B", reading: 85 },
      { _id: 6, city: "B", reading: 90 }
    ]);
    const windowResult = await temperatures.aggregate([
      {
        $setWindowFields: {
          partitionBy: "$city",
          output: {
            medianReading: {
              $median: { input: "$reading", method: "approximate" },
              window: { documents: ["unbounded", "unbounded"] }
            }
          }
        }
      }
    ]).toArray();
    console.log('Window result:', windowResult);

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
        students.insert_many([
            { 'class': 'A', 'score': 72 },
            { 'class': 'A', 'score': 85 },
            { 'class': 'A', 'score': 90 },
            { 'class': 'A', 'score': 68 },
            { 'class': 'A', 'score': 95 },
            { 'class': 'B', 'score': 80 },
            { 'class': 'B', 'score': 75 },
            { 'class': 'B', 'score': 92 },
            { 'class': 'B', 'score': 88 },
            { 'class': 'B', 'score': 70 }
        ])
        accumulator_result = list(students.aggregate([
            { '$group': {
                '_id': '$class',
                'medianScore': { '$median': { 'input': '$score', 'method': 'approximate' } }
            }}
        ]))
        print('Accumulator result:', accumulator_result)

        # Expression usage: median of an array field
        surveys = db['surveys']
        surveys.insert_many([
            { '_id': 1, 'ratings': [3, 5, 7, 9, 2] },
            { '_id': 2, 'ratings': [10, 20, 30, 40, 50] },
            { '_id': 3, 'ratings': [1, 1, 2, 3, 5] }
        ])
        expression_result = list(surveys.aggregate([
            { '$project': {
                'medianRating': { '$median': { 'input': '$ratings', 'method': 'approximate' } }
            }}
        ]))
        print('Expression result:', expression_result)

        # Window operator usage: median across each partition
        temperatures = db['temperatures']
        temperatures.insert_many([
            { '_id': 1, 'city': 'A', 'reading': 60 },
            { '_id': 2, 'city': 'A', 'reading': 65 },
            { '_id': 3, 'city': 'A', 'reading': 70 },
            { '_id': 4, 'city': 'B', 'reading': 80 },
            { '_id': 5, 'city': 'B', 'reading': 85 },
            { '_id': 6, 'city': 'B', 'reading': 90 }
        ])
        window_result = list(temperatures.aggregate([
            {
                '$setWindowFields': {
                    'partitionBy': '$city',
                    'output': {
                        'medianReading': {
                            '$median': { 'input': '$reading', 'method': 'approximate' },
                            'window': { 'documents': ['unbounded', 'unbounded'] }
                        }
                    }
                }
            }
        ]))
        print('Window result:', window_result)

    finally:
        client.close()

example()
```

------