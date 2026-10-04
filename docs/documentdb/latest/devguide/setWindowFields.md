

# $setWindowFields
<a name="setWindowFields"></a>

New from version 8.0.2.

The `$setWindowFields` stage in Amazon DocumentDB performs operations on a specified span of documents (a *window*) in a partition, and returns the results based on the chosen window operator. The stage groups the input documents into partitions, optionally sorts them, and for each document computes one or more output fields over a window of surrounding documents.

**Syntax**

```
{
  $setWindowFields: {
    partitionBy: <expression>,
    sortBy: { <sortField1>: <sortOrder>, ... },
    output: {
      <outputField1>: {
        <windowOperator>: <expression>,
        window: {
          documents: [ <lowerBound>, <upperBound> ],
          range: [ <lowerBound>, <upperBound> ],
          unit: <time unit>
        }
      },
      ...
    }
  }
}
```

**Parameters**
+ `partitionBy`: Optional. A single expression used to group the documents into partitions. This can be a field path (for example, `"$state"`) or another expression. If omitted, all input documents belong to a single partition.
+ `sortBy`: Optional. A document that specifies the field or fields to sort the documents in each partition by, in the form `{ <field>: 1 }` for ascending order or `{ <field>: -1 }` for descending order. A `sortBy` is required when you use document-based or range-based window bounds, and when you use one of the ranking operators.
+ `output`: Required. A document that specifies the fields to append to each document. You can specify multiple output fields, but each output field takes exactly one window operator, its argument, and an optional `window` document that defines the window boundaries: `{ <field>: { <windowOperator>: <expression>, window: { ... } } }`.

## Window boundaries
<a name="setWindowFields-bounds"></a>

Within each `output` field you can optionally define the window boundaries with a `window` document. A window can be defined by document position or by a range of values.
+ `documents`: Specifies the window as a number of documents before and after the current document, in the form `[ <lowerBound>, <upperBound> ]`. Each bound is an integer offset (for example, `-1` or `2`), or one of the keywords `"unbounded"` and `"current"`. `"unbounded"` extends the window to the start of the partition when used as the lower bound, or to the end of the partition when used as the upper bound. `"current"` means the current document. A `documents` window requires a `sortBy` unless both bounds are `"unbounded"`.
+ `range`: Specifies the window as a range of `sortBy` field values relative to the current document, in the form `[ <lowerBound>, <upperBound> ]`. Each bound is a number that is added to the `sortBy` value of the current document, or the `"unbounded"` keyword. A `range` window requires exactly one ascending `sortBy` field and does not accept the `"current"` keyword.
+ `unit`: Optional. Used with `range` to interpret the numeric window bounds as a span of time when the `sortBy` field holds date values. Amazon DocumentDB supports the following units: `"year"`, `"quarter"`, `"month"`, `"week"`, `"day"`, `"hour"`, `"minute"`, `"second"`, and `"millisecond"`. When `unit` is specified, the `range` bounds must be integers.

When the `window` document is omitted, the default window is `documents: ["unbounded", "unbounded"]`, which spans the entire partition.

**Note**  
When you use a `range` window over date values, we recommend a fixed-duration `unit` such as `"day"` (or smaller) rather than `"month"`, `"quarter"`, or `"year"`, whose calendar-dependent lengths can produce ambiguous window boundaries.

## Supported window operators
<a name="setWindowFields-operators"></a>

Amazon DocumentDB supports the following 26 window operators in the `output` field of the `$setWindowFields` stage:
+ `$sum`
+ `$avg`
+ `$count`
+ `$push`
+ `$addToSet`
+ `$stdDevPop`
+ `$stdDevSamp`
+ `$covariancePop`
+ `$covarianceSamp`
+ `$first`
+ `$last`
+ `$firstN`
+ `$lastN`
+ `$top`
+ `$bottom`
+ `$topN`
+ `$bottomN`
+ `$min`
+ `$minN`
+ `$max`
+ `$maxN`
+ `$median`
+ `$percentile`
+ `$rank`
+ `$denseRank`
+ `$documentNumber`

**Note**  
The `$rand` operator is not supported within a window operator in the `$setWindowFields` stage.

**Empty windows**

When a window contains no documents (for example, a `range` window with no values in range), the result depends on the operator: `$count` and `$sum` return `0`; `$push`, `$addToSet`, `$firstN`, `$lastN`, `$minN`, `$maxN`, `$topN`, and `$bottomN` return an empty array; `$percentile` returns an array of `null` values (one per requested percentile); all other operators return `null`.

## Example (MongoDB Shell)
<a name="setWindowFields-examples"></a>

The following example partitions the documents by `region`, sorts each partition by `day`, and computes a running total of `revenue` from the start of the partition through the current document.

**Create sample documents**

```
db.sales.insertMany([
  { _id: 1, region: "east", day: 1, revenue: 100 },
  { _id: 2, region: "east", day: 2, revenue: 150 },
  { _id: 3, region: "east", day: 3, revenue: 120 },
  { _id: 4, region: "west", day: 1, revenue: 200 },
  { _id: 5, region: "west", day: 2, revenue: 180 }
]);
```

**Query example**

```
db.sales.aggregate([
  {
    $setWindowFields: {
      partitionBy: "$region",
      sortBy: { day: 1 },
      output: {
        runningRevenue: {
          $sum: "$revenue",
          window: { documents: ["unbounded", "current"] }
        }
      }
    }
  }
]);
```

**Output**

```
[
  { "_id": 1, "region": "east", "day": 1, "revenue": 100, "runningRevenue": 100 },
  { "_id": 2, "region": "east", "day": 2, "revenue": 150, "runningRevenue": 250 },
  { "_id": 3, "region": "east", "day": 3, "revenue": 120, "runningRevenue": 370 },
  { "_id": 4, "region": "west", "day": 1, "revenue": 200, "runningRevenue": 200 },
  { "_id": 5, "region": "west", "day": 2, "revenue": 180, "runningRevenue": 380 }
]
```

Each document is augmented with `runningRevenue`, the cumulative sum of `revenue` within its partition up to and including the current document.

## Code examples
<a name="setWindowFields-code"></a>

To view a code example for using the `$setWindowFields` stage, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  try {
    await client.connect();
    const db = client.db('test');
    const sales = db.collection('sales');

    await sales.insertMany([
      { _id: 1, region: "east", day: 1, revenue: 100 },
      { _id: 2, region: "east", day: 2, revenue: 150 },
      { _id: 3, region: "east", day: 3, revenue: 120 },
      { _id: 4, region: "west", day: 1, revenue: 200 },
      { _id: 5, region: "west", day: 2, revenue: 180 }
    ]);

    const result = await sales.aggregate([
      {
        $setWindowFields: {
          partitionBy: "$region",
          sortBy: { day: 1 },
          output: {
            runningRevenue: {
              $sum: "$revenue",
              window: { documents: ["unbounded", "current"] }
            }
          }
        }
      }
    ]).toArray();

    console.log(result);
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
        sales = db['sales']

        sales.insert_many([
            { '_id': 1, 'region': 'east', 'day': 1, 'revenue': 100 },
            { '_id': 2, 'region': 'east', 'day': 2, 'revenue': 150 },
            { '_id': 3, 'region': 'east', 'day': 3, 'revenue': 120 },
            { '_id': 4, 'region': 'west', 'day': 1, 'revenue': 200 },
            { '_id': 5, 'region': 'west', 'day': 2, 'revenue': 180 }
        ])

        result = list(sales.aggregate([
            {
                '$setWindowFields': {
                    'partitionBy': '$region',
                    'sortBy': { 'day': 1 },
                    'output': {
                        'runningRevenue': {
                            '$sum': '$revenue',
                            'window': { 'documents': ['unbounded', 'current'] }
                        }
                    }
                }
            }
        ]))

        print(result)
    finally:
        client.close()

example()
```

------