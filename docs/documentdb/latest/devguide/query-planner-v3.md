# Query planner v3

Planner Version 3 in Amazon DocumentDB 8.0 supports 21 aggregation stages, including 6 new stages.
Planner V3 comes with inbuilt support for distinct commands.
It offers upto 2x overall performance improvement over Planner v2 in Amazon DocumentDB 5.0.
All new features and operators in Amazon DocumentDB 8.0 are compatible with Planner v3.
New aggregation stages in Amazon DocumentDB 8.0 that are supported by Planner v3 include $replaceWith, $vectorSearch, $merge, $set, $unset, $bucket.
Planner v3 also supports new features and operators in Amazon DocumentDB 8.0 including Collation, Views, $merge, $pow, $rand, $dateTrunc, $dateToParts, $dateFromParts.

###### Topics

- [Prerequisites](#nqp-prerequisites "#nqp-prerequisites")
- [Selecting planner version 3.0 as the default query planner](#second-concept-chapter "#second-concept-chapter")
- [Best practices](#nqp-best-practices "#nqp-best-practices")
- [Limitations](#nqp-limitations "#nqp-limitations")
- [Improvements to aggregate and distinct Operators](#operator-improvements "#operator-improvements")
- [Potential behavior differences between planner version 1.0, 3.0, and MongoDB](#planner-behavior-differences "#planner-behavior-differences")

## Prerequisites

The following prerequisites apply to planner version 3.0:

- Planner version 3.0 is available in all regions where engine version 8.0 is available.
- Planner version 3.0 is the default query planner when engine version 8.0 is selected.

## Selecting planner version 3.0 as the default query planner

If you changed your default query planner in Amazon DocumentDB 8.0, and need to revert to planner v3, you can do so from the console or CLI:

- Follow the steps in [Modifying Amazon DocumentDB cluster parameters](cluster_parameter_groups-parameters.md "cluster_parameter_groups-parameters.md") to modify your cluster’s parameter group.
- For the parameter titled ‘plannerVersion’, change the value to 3.0 indicating planner version 3.0.
- Select **Apply immediately** (selecting **Apply at reboot** will render the selection ineffective until next reboot of the cluster).

## Best practices

For expected results, use the following best practices when applying planner version 3.0:

- In a global cluster, select the same `plannerVersion` value (1.0 or 2.0 or 3.0) in the cluster parameter groups for both regions.
  Note that selecting different planner versions in primary and secondary regions may cause inconsistent query behavior and performance.
- Updating to planner version 3.0 during a scheduled maintenance windows or during reduced traffic periods will be the least disruptive, as there may be increased error rates if the planner version is changed when workloads are actively running.

## Limitations

The following limitations apply to planner version 3.0:

- Planner version 3.0 is not supported in elastic clusters, which will fall back to planner version 1.0.

- While Planner v1 allows the use of 'planHint' to ensure that a specific query plan is selected by the query optimizer, Planner v3 does not allow the use of 'planHint' and relies on internal optimizations to choose the best plan for the given query.

## Improvements to `aggregate` and `distinct` Operators

Planner version 3.0 introduces improvements across $aggregate stages, and $distinct command. The following are some of the most noteworthy improvements..

- The planner moves $match stages earlier in the pipeline when possible, reducing the number of documents processed by subsequent stages.

```
//Planner v1
db.orders.aggregate([
  { $project: { customerId: 1, orderDate: 1, totalAmount: 1 } },
  { $match: { customerId: { $gt: 1000 } } }
])

// Planner v3 pulls up the match since customerId exists in original documents
// Optimized internally as:
db.orders.aggregate([
  { $match: { customerId: { $gt: 1000 } } },  // Pulled up before project
  { $project: { customerId: 1, orderDate: 1, totalAmount: 1 } }
])
```

- The planner automatically combines $lookup and $unwind stages when they operate on the same field, reducing intermediate data processing and improving performance.

```

                 Example query:
//Planner v1
db.orders.aggregate([
  { $lookup: { from: "products", localField: "productId", foreignField: "_id", as: "productInfo" } },
  { $unwind: "$productInfo" },
  { $project: { orderDate: 1, "productInfo.name": 1, "productInfo.price": 1 } }
])

// Planner version 3.0 optimizes this internally by coalescing the $lookup and $unwind stages

```

- Planner version 3.0 introduces a new Distinct Scan execution strategy that significantly improves performance for distinct operations on low cardinality indexes.

```

                 Example query:
//// If there is a low cardinality index on "category", you may see a query plan like below
db.explain().products.distinct("category")

"queryPlanner" : {
        "plannerVersion" : 3,
        "namespace" : "db.products",
        "winningPlan" : {
                "stage" : "AGGREGATE",
                "inputStage" : {
                        "stage" : "DISTINCT_SCAN",
                        "inputStage" : {
                                "stage" : "IXONLYSCAN",
                                "indexName" : "category_1",
                                "direction" : "forward"
                        }
                }
        }
}


```

## Potential behavior differences between planner version 1.0, 3.0, and MongoDB

In some edge cases, it is possible that planner version 3.0 may produce results that slightly vary from planner version 1.0.
This section walks through some examples of these possibilities.

Feature Differences

- On an empty collection or when previous stages like match filters all documents, Planner v1 gives the output “field”:0. Planner v3 and MongoDB won't give any outputs.
- With Plannerv1, {"$skip":n} does not skip if there are less than n documents returned by the previous stage. Plannerv3 and MongoDB correctly skip irrespective of number of documents returned.
- When a foreign collection referenced in $lookup does not exist, plannerv1 throws an error. Planner v3 and MongoDB treat the foreign collection as empty collection and performs $lookup.

```
db.coll.aggregate([
    {$lookup: {from: "does_not_exist", localField: "a", foreignField: "a", as: "c"}}
])

```

- Only Planner v1 will allow using multiple $search in a pipeline Planner v2/v3 will throw an error and MongoDB does not support it.

```
VectorSearch = { "$search": { "vectorSearch": {
   "vector": [0.2, 0.5, 0.8],
   "path": "vectorEmbedding",
   "similarity": "cosine",
   "k": 2,
   "efSearch": 1
   }}}
db.coll.aggregate([VectorSearch, VectorSearch])

```

- Only Planner v3 works when vectorSearch stage is not the first stage. In this case, MongoDB will throw an error and Planner v1 does not support $vectorSearch stage.

```
VectorSearch = { {"$vectorSearch": {
    "queryVector": [0.2, 0.5, 0.8],
    "path": "vectorEmbedding",
    "similarity": "euclidean",
    "limit": 4,
    "numCandidates": 100} }

db.coll.aggregate([$match:{}, VectorSearch])

```
