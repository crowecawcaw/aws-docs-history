

# $bucketAuto
<a name="bucketAuto"></a>

New from version 8.0.2.

The `$bucketAuto` aggregation stage in Amazon DocumentDB automatically groups input documents into a specified number of buckets based on a specified expression. Unlike `$bucket`, where you define the bucket boundaries explicitly, `$bucketAuto` automatically determines the boundaries so that the documents are distributed as evenly as possible across the requested number of buckets. This can be useful when you want to categorize data into a fixed number of groups without knowing the distribution of the values in advance.

**Parameters**
+ `groupBy` (required): The expression that specifies the value to group by.
+ `buckets` (required): A positive integer that specifies the number of buckets into which the documents are grouped. Depending on the input documents and the `groupBy` expression, the actual number of buckets can be less than the specified number.
+ `output` (optional): An object that specifies the information to output for each bucket. You can use accumulator operators like `$sum`, `$avg`, `$min`, and `$max` to compute aggregations for each bucket. If omitted, each bucket outputs a `count` field by default.
+ `granularity` (optional): A string that specifies the preferred number series to use for the bucket boundaries. This snaps the computed boundaries to a standard numerical progression. This parameter is available only if all `groupBy` values are numeric and none of them are `NaN`. Valid values are: `R5`, `R10`, `R20`, `R40`, `R80`, `1-2-5`, `E6`, `E12`, `E24`, `E48`, `E96`, `E192`, and `POWERSOF2`.

**Output**

Each bucket is returned as a separate document that contains an `_id` object describing the bounds of the bucket:
+ `_id.min`: The inclusive lower bound of the bucket.
+ `_id.max`: The upper bound of the bucket. This bound is exclusive for every bucket except the final bucket in the series, where it is inclusive.

## Example (MongoDB Shell)
<a name="bucketAuto-examples"></a>

The following example demonstrates how to use the `$bucketAuto` stage to group sales data into buckets by price.

**Create sample documents**

```
db.sales.insertMany([
  { item: "abc", price: 10, quantity: 2, date: new Date("2020-09-01") },
  { item: "def", price: 20, quantity: 1, date: new Date("2020-10-01") },
  { item: "ghi", price: 5, quantity: 3, date: new Date("2020-11-01") },
  { item: "jkl", price: 15, quantity: 2, date: new Date("2020-12-01") },
  { item: "mno", price: 25, quantity: 1, date: new Date("2021-01-01") }
]);
```

**Query example**

The following command groups the sample documents into three buckets by price:

```
db.sales.aggregate([
  {
    $bucketAuto: {
      groupBy: "$price",
      buckets: 3,
      output: {
        "count": { $sum: 1 },
        "totalQuantity": { $sum: "$quantity" }
      }
    }
  }
])
```

**Output**

The command returns the following output:

```
[
  { _id: { min: 5, max: 15 }, count: 2, totalQuantity: 5 },
  { _id: { min: 15, max: 25 }, count: 2, totalQuantity: 3 },
  { _id: { min: 25, max: 25 }, count: 1, totalQuantity: 1 }
]
```

**Query example with granularity**

The following example adds the `granularity` option to snap the computed bucket boundaries to powers of 2.

```
db.sales.aggregate([
  {
    $bucketAuto: {
      groupBy: "$price",
      buckets: 2,
      granularity: "POWERSOF2",
      output: {
        "count": { $sum: 1 },
        "totalQuantity": { $sum: "$quantity" }
      }
    }
  }
])
```

**Output**

The command returns the following output:

```
[
  { _id: { min: 4, max: 16 }, count: 3, totalQuantity: 7 },
  { _id: { min: 16, max: 32 }, count: 2, totalQuantity: 2 }
]
```

## Code examples
<a name="bucketAuto-code"></a>

To view a code example for using the `$bucketAuto` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const sales = db.collection('sales');

  const result = await sales.aggregate([
    {
      $bucketAuto: {
        groupBy: "$price",
        buckets: 3,
        output: {
          "count": { $sum: 1 },
          "totalQuantity": { $sum: "$quantity" }
        }
      }
    }
  ]).toArray();

  console.log(result);
  client.close();
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
    sales = db['sales']

    result = list(sales.aggregate([
        {
            '$bucketAuto': {
                'groupBy': '$price',
                'buckets': 3,
                'output': {
                    'count': {'$sum': 1},
                    'totalQuantity': {'$sum': '$quantity'}
                }
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------