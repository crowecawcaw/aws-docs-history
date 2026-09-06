

# Query plan analysis
<a name="performance-query-plan-analysis"></a>

Query plan analysis through explain plan provides essential insights into Amazon DocumentDB query performance. Query plan with executionStats reveals key metrics including:
+ Documents returned per stage (nReturned)
+ Stage-specific execution times (executionTimeMillisEstimate)
+ Plan generation duration (planningTimeMillis)

By examining the query plan output, developers can analyze execution patterns, evaluate index utilization, and identify potential optimization opportunities across the query pipeline stages.

To analyze the query plan, you can use the explain() command in the following formats.

```
db.runCommand({explain: {query document}, verbosity: "executionStats"})
db.collection.find().explain("executionStats");
```

The following is an example operation:

```
db.collection.find({ companyname: { '$eq': 'ANYCOMPANY' }, isDeleted: { '$eq': false } }).sort({"createdAt":1}).limit(2).explain("executionStats");
```

Output from this operation looks something like the following:

```
{
  queryPlanner: {
    plannerVersion: 2,
    namespace: 'limit_test.test',
    winningPlan: {
      stage: 'LIMIT_SKIP',
      inputStage: {
        stage: 'SORT',
        sortPattern: { createdAt: 1 },
        inputStage: {
          stage: 'IXSCAN',
          indexName: 'companyname_1_createdAt_1_isDeleted_1',
          direction: 'forward',
          indexCond: {
            '$and': [
              { companyname: { '$eq': 'ANYCOMPANY' } },
              { isDeleted: { '$eq': false } }
            ]
          }
        }
      }
    }
  },
  indexFilterSet: false,
  indexFilterApplied: false,
  executionStats: {
    executionSuccess: true,
    executionTimeMillis: '4.186',
    planningTimeMillis: '3.909',
    executionStages: {
      stage: 'LIMIT_SKIP',
      nReturned: '2',
      executionTimeMillisEstimate: '0.199',
      inputStage: {
        stage: 'SORT',
        nReturned: '2',
        executionTimeMillisEstimate: '0.197',
        sortPattern: { createdAt: 1 },
        inputStage: {
          stage: 'IXSCAN',
          nReturned: '34',
          executionTimeMillisEstimate: '0.151',
          indexName: 'companyname_1_createdAt_1_isDeleted_1',
          direction: 'forward',
          indexCond: {
            '$and': [
              { companyname: { '$eq': 'ANYCOMPANY' } },
              { isDeleted: { '$eq': false } }
            ]
          }
        }
      }
    }
  },
  serverInfo: { host: 'demo-cluster', port: 27017, version: '5.0.0' },
  ok: 1,
  operationTime: Timestamp({ t: 1759915116, i: 1 })
}
```

Below is a detailed analysis of a Amazon DocumentDB query execution plan, breaking down each component and its performance characteristics.

## Overall timing
<a name="overall-timing"></a>

executionTimeMillis represents the total time taken by the query including planning time.

planningTimeMillis represents the total planning time taken by the query.

## Execution stages
<a name="execution-stages"></a>

It describes the step-by-step process Amazon DocumentDB uses to execute a query, showing how data flows through different operations.

```
"executionStages": {
    "stage": "[STAGE_NAME]",
    "nReturned": "[NUMBER_OF_DOCS]",
    "executionTimeMillisEstimate": "[TIME]",
    "inputStage": {
        // Nested stages
    }
}
```

### Common stages in a query plan
<a name="common-stages"></a>

Below are the common execution stages in a query plan. Each stage returns executionTimeMillisEstimate (execution time) and nReturned (number of documents) metrics to help evaluate query performance at every stage.

#### COLLSCAN (Collection Scan)
<a name="collscan-stage"></a>
+ Scans the entire collection document by document
+ nReturned: Returns all matching documents in the collection
+ Can be an expensive operation, seen when no index is available

#### IXSCAN (Index Scan)
<a name="ixscan-stage"></a>
+ Uses an index to find matching documents
+ nReturned: Only matching documents based on the index
+ Efficient operation, preferred over COLLSCAN

#### SORT
<a name="sort-stage"></a>
+ Sorts documents based on specified fields
+ If the sort attribute in the query is not part of an index, this stage will appear explicitly
+ nReturned: Same number as input documents
+ Memory-intensive for large result sets. To optimize, add the sort field name to an index

#### LIMIT\_SKIP
<a name="limit-skip-stage"></a>
+ Controls the number of documents returned and skipped
+ nReturned: Limited by the LIMIT value
+ Used for pagination or LIMIT operations

#### SUBSCAN
<a name="subscan-stage"></a>
+ Performs nested query operations
+ nReturned: Varies based on subquery results
+ Used in complex queries with multiple stages

Stages with high executionTimeMillisEstimate are good candidates for optimization.

**Note**  
The executionStats parameter does not currently support update and delete commands.

## Understanding docsExamined in Explain Plan Execution Stats
<a name="docs-examined"></a>

When you run a query with `explain("executionStats")`, Amazon DocumentDB provides examination metrics that help you understand how many documents were scanned to produce the query results. These metrics are useful for identifying inefficient query plans and optimizing performance.

**Note**  
Available only in Amazon DocumentDB 5.0.1\+ and 8.0.0\+.

### Fields
<a name="docs-examined-fields"></a>


| Field | Description | Level | 
| --- | --- | --- | 
| totalDocsExamined | Total number of documents examined across all execution stages. | Top-level executionStats | 
| docsExamined | Number of documents examined by a specific execution stage. | Stage-level | 

The `docsExamined` field appears on the following stages:


| Stage | Description | 
| --- | --- | 
| COLLSCAN | Collection scan. All documents in the collection are examined. | 
| IXSCAN | Index scan. Only documents matching the index condition are examined. | 
| FETCH | When the optimizer retrieves documents in a separate stage from IXSCAN, the FETCH stage reports docsExamined. In index scan plans, the child IXSCAN stages do not report docsExamined. In $lookup plans, both the FETCH stage and its child stages may report docsExamined. | 

**Note**  
`docsExamined` does not appear on IXONLYSCAN stages because the query is satisfied entirely from the index without accessing documents.

### Show docsExamined in Explain Plan executionStats Output
<a name="docs-examined-examples"></a>

The following examples use a collection with 500,000 documents and demonstrate how `docsExamined` changes across different query execution stages.

Create sample data:

```
for (let i = 0; i < 500000; i++) {
    db.coll.insertOne({ number: i, arr: [i, [i+1]], value: "test", bool: i % 2 === 0 });
}
```

#### Collection scan (COLLSCAN)
<a name="docs-examined-collscan"></a>

Without an index, Amazon DocumentDB performs a full collection scan.

```
db.coll.find({ "number": { "$lt": 500 } }).explain("executionStats").executionStats
```

Output:

```
{
    "executionSuccess" : true,
    "nReturned" : "500",
    "executionTimeMillis" : "282.055",
    "planningTimeMillis" : "0.085",
    "totalDocsExamined" : "500000",
    "executionStages" : {
        "stage" : "COLLSCAN",
        "nReturned" : "500",
        "executionTimeMillisEstimate" : "281.915",
        "docsExamined" : "500000",
        "filter" : {
            "number" : {
                "$lt" : 500
            }
        }
    }
}
```

All 500,000 documents were examined to return 500 results. Creating an index on the number field improves this.

#### Index scan (IXSCAN)
<a name="docs-examined-ixscan"></a>

```
db.coll.createIndex({ number: 1 });
db.coll.find({ "number": { "$lt": 5000 } }).explain("executionStats").executionStats
```

Output:

```
{
    "executionSuccess" : true,
    "nReturned" : "5000",
    "executionTimeMillis" : "3.047",
    "planningTimeMillis" : "0.296",
    "totalDocsExamined" : "5000",
    "executionStages" : {
        "stage" : "IXSCAN",
        "nReturned" : "5000",
        "executionTimeMillisEstimate" : "2.576",
        "indexName" : "number_1",
        "direction" : "forward",
        "docsExamined" : "5000",
        "indexCond" : {
            "$and" : [
                {
                    "number" : {
                        "$lt" : 5000
                    }
                }
            ]
        }
    }
}
```

With the index, only 5,000 out of 500,000 documents were examined and fetched, matching the number returned. The index condition filtered out 495,000 documents that did not match the query.

#### Index scan with residual filter
<a name="docs-examined-ixscan-residual"></a>

```
db.coll.find({ "number": { "$lt": 5000 }, "arr": { "$gt": 4000 } }).explain("executionStats").executionStats
```

Output:

```
{
    "executionSuccess" : true,
    "nReturned" : "999",
    "executionTimeMillis" : "15.367",
    "planningTimeMillis" : "0.115",
    "totalDocsExamined" : "5000",
    "executionStages" : {
        "stage" : "IXSCAN",
        "nReturned" : "999",
        "executionTimeMillisEstimate" : "15.170",
        "indexName" : "number_1",
        "direction" : "forward",
        "docsExamined" : "5000",
        "indexCond" : {
            "$and" : [
                {
                    "number" : {
                        "$lt" : 5000
                    }
                }
            ]
        },
        "filter" : {
            "arr" : {
                "$gt" : 4000
            }
        }
    }
}
```

The index condition matched 5,000 documents out of 500,000, then the residual filter on `arr` reduced the result to 999. The `docsExamined` value of 5,000 reflects all documents examined after the index condition but before the residual filter was applied.

#### Fetch with IXSCAN
<a name="docs-examined-fetch-ixscan"></a>

```
db.coll.find({ "$or": [{ "number": { "$lt": 100000 } }, { "number": { "$gt": 400000 } }] }).explain("executionStats").executionStats
```

Output:

```
{
    "executionSuccess" : true,
    "nReturned" : "199999",
    "executionTimeMillis" : "899.801",
    "planningTimeMillis" : "0.183",
    "totalDocsExamined" : "199999",
    "executionStages" : {
        "stage" : "FETCH",
        "nReturned" : "199999",
        "executionTimeMillisEstimate" : "894.141",
        "docsExamined" : "199999",
        "inputStage" : {
            "stage" : "IXOR",
            "nReturned" : "0",
            "executionTimeMillisEstimate" : "874.897",
            "inputStages" : [
                {
                    "stage" : "IXSCAN",
                    "nReturned" : "100000",
                    "executionTimeMillisEstimate" : "462.208",
                    "indexName" : "number_1",
                    "indexCond" : {
                        "$and" : [
                            {
                                "number" : {
                                    "$lt" : 100000
                                }
                            }
                        ]
                    }
                },
                {
                    "stage" : "IXSCAN",
                    "nReturned" : "99999",
                    "executionTimeMillisEstimate" : "412.684",
                    "indexName" : "number_1",
                    "indexCond" : {
                        "$and" : [
                            {
                                "number" : {
                                    "$gt" : 400000
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
}
```

When Amazon DocumentDB optimizer uses a fetch stage to retrieve documents, the FETCH stage reports `docsExamined`. The child IXSCAN stages do not report `docsExamined` because they only scan index keys without accessing documents directly.

#### FETCH with Aggregate Lookup
<a name="docs-examined-fetch-lookup"></a>

```
db.coll.explain("executionStats").aggregate([
    { $match: { "number": { "$lt": 5 } } },
    { $lookup: { from: "coll", pipeline: [{ $match: { "number": { "$lt": 3 } } }], as: "sub" } }
]).executionStats
```

Output:

```
{
    "executionSuccess" : true,
    "nReturned" : "5",
    "executionTimeMillis" : "0.525",
    "planningTimeMillis" : "0.327",
    "totalDocsExamined" : "9",
    "executionStages" : {
        "stage" : "NESTED_LOOP_LOOKUP",
        "nReturned" : "5",
        "executionTimeMillisEstimate" : "0.163",
        "inputStages" : [
            {
                "stage" : "IXSCAN",
                "nReturned" : "5",
                "executionTimeMillisEstimate" : "0.039",
                "indexName" : "number_1",
                "direction" : "forward",
                "docsExamined" : "5",
                "indexCond" : {
                    "$and" : [
                        {
                            "number" : {
                                "$lt" : 5
                            }
                        }
                    ]
                }
            },
            {
                "stage" : "FETCH",
                "nReturned" : "1",
                "executionTimeMillisEstimate" : "0.009",
                "docsExamined" : "1",
                "inputStage" : {
                    "stage" : "AGGREGATE",
                    "nReturned" : "1",
                    "executionTimeMillisEstimate" : "0.044",
                    "inputStage" : {
                        "stage" : "IXSCAN",
                        "nReturned" : "3",
                        "executionTimeMillisEstimate" : "0.013",
                        "indexName" : "number_1",
                        "direction" : "forward",
                        "docsExamined" : "3",
                        "indexCond" : {
                            "$and" : [
                                {
                                    "number" : {
                                        "$lt" : 3
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        ]
    }
}
```

The outer IXSCAN examined 5 documents matching number < 5. The inner IXSCAN examined 3 documents matching number < 3, and the FETCH stage examined 1 aggregated result. The `totalDocsExamined` of 9 is the sum across all stages (5 \+ 3 \+ 1).