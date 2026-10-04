

# $facet
<a name="facet"></a>

New from version 8.0.2.

The `$facet` aggregation stage in Amazon DocumentDB processes multiple aggregation pipelines within a single stage on the same set of input documents. Each output field defines its own pipeline, and every pipeline receives the same input documents. This lets you compute several independent aggregations, such as counts, groupings, and summary statistics, in a single query instead of running the collection through multiple separate queries.

Each sub-pipeline runs independently and produces an array of documents that is stored in its corresponding output field. Because the sub-pipelines do not share state, the output of one pipeline does not affect another.

**Syntax**

```
{
  $facet: {
    <outputField1>: [ <stage1>, <stage2>, ... ],
    <outputField2>: [ <stage1>, <stage2>, ... ],
    ...
  }
}
```

**Parameters**
+ `outputField` (required): The name of an output field that holds the result array of its associated aggregation pipeline. You can specify one or more output fields. Each output field maps to an array of aggregation pipeline stages that is applied to the input documents.

**Output**

The `$facet` stage returns a single document. Each output field that you specify contains an array of documents produced by its corresponding sub-pipeline.

**Limitations**
+ A `$facet` sub-pipeline cannot include the following stages: `$changeStream`, `$collStats`, `$facet` (nesting is not allowed), `$geoNear`, `$indexStats`, `$listSearchIndexes`, `$merge`, `$out`, `$planCacheStats`, `$search`, `$searchMeta`, and `$vectorSearch`.
+ The document that the `$facet` stage returns must stay within the 16 MB BSON document size limit.
+ A `$sort` stage that comes before a `$facet` stage cannot determine the order of an order-sensitive accumulator (`$first`, `$last`, `$push`, `$firstN`, `$lastN`, or `$mergeObjects`) in a `$group`, `$bucket`, or `$bucketAuto` stage when that ordering would have to be applied across the `$facet` boundary. This applies whether the grouping stage is inside a `$facet` sub-pipeline or after the `$facet` stage. In this case, Amazon DocumentDB returns an error instead of running the pipeline. To order such an accumulator, place the `$sort` stage inside the `$facet` sub-pipeline, immediately before the grouping stage. Order-insensitive accumulators, such as `$sum`, `$min`, `$max`, and `$count`, are not affected.

## Example (MongoDB Shell)
<a name="facet-examples"></a>

The following example demonstrates how to use the `$facet` stage to compute several aggregations over the same sales data in a single query.

**Create sample documents**

```
db.sales.insertMany([
  { item: "abc", price: 10, quantity: 2, date: new Date("2020-09-01") },
  { item: "def", price: 20, quantity: 1, date: new Date("2020-10-01") },
  { item: "ghi", price: 5, quantity: 3, date: new Date("2020-11-01") },
  { item: "jkl", price: 15, quantity: 2, date: new Date("2020-12-01") },
  { item: "abc", price: 25, quantity: 1, date: new Date("2021-01-01") }
]);
```

**Query example**

The following command uses `$facet` to compute, in a single stage, the total quantity sold per item, overall price statistics, and the total document count:

```
db.sales.aggregate([
  {
    $facet: {
      "totalByItem": [
        { $group: { _id: "$item", totalQuantity: { $sum: "$quantity" } } }
      ],
      "priceStats": [
        { $group: { _id: null, avgPrice: { $avg: "$price" }, maxPrice: { $max: "$price" } } }
      ],
      "documentCount": [
        { $count: "total" }
      ]
    }
  }
])
```

**Output**

The command returns the following output:

```
[
  {
    totalByItem: [
      { _id: "abc", totalQuantity: 3 },
      { _id: "def", totalQuantity: 1 },
      { _id: "ghi", totalQuantity: 3 },
      { _id: "jkl", totalQuantity: 2 }
    ],
    priceStats: [
      { _id: null, avgPrice: 15, maxPrice: 25 }
    ],
    documentCount: [
      { total: 5 }
    ]
  }
]
```

## Code examples
<a name="facet-code"></a>

To view a code example for using the `$facet` command, choose the tab for the language that you want to use:

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
      $facet: {
        "totalByItem": [
          { $group: { _id: "$item", totalQuantity: { $sum: "$quantity" } } }
        ],
        "priceStats": [
          { $group: { _id: null, avgPrice: { $avg: "$price" }, maxPrice: { $max: "$price" } } }
        ],
        "documentCount": [
          { $count: "total" }
        ]
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
            '$facet': {
                'totalByItem': [
                    {'$group': {'_id': '$item', 'totalQuantity': {'$sum': '$quantity'}}}
                ],
                'priceStats': [
                    {'$group': {'_id': None, 'avgPrice': {'$avg': '$price'}, 'maxPrice': {'$max': '$price'}}}
                ],
                'documentCount': [
                    {'$count': 'total'}
                ]
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------