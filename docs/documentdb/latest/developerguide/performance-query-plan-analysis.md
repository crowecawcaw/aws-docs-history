# Query Plan Analysis

Query plan analysis through explain plan provides essential insights into Amazon Amazon DocumentDB query performance. Query plan with executionStats reveals key metrics including:

- Documents returned per stage (nReturned)
- Stage-specific execution times (executionTimeMillisEstimate)
- Plan generation duration (planningTimeMillis)
  By examining the query plan output, developers can analyze execution patterns, evaluate index utilization, and identify potential optimization opportunities across the query pipeline stages.

To analyze the query plan, you can use the explain() command in the following formats.

```

db.runCommand({explain: {query document}, verbosity: "executionStats"})
db.collection.find().explain("executionStats");

```

The following is an example operation:

```

db.collection.find({ companyname: { '$eq': 'ANYCOMPANY' } }, { isDeleted: { '$eq': false } }).sort({"createdAt":1}).limit(2).explain("executionStats");

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

## Overall Timing

executionTimeMillis represents the total time taken by the query including planning time.

planningTimeMillis represents the total planning time taken by the query.

## Execution Stages

It describes the step-by-step process Amazon Amazon DocumentDB uses to execute a query, showing how data flows through different operations.

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

### Common Stages in a Query Plan

Below are the common execution stages in a query plan. Each stage returns executionTimeMillisEstimate (execution time) and nReturned (number of documents) metrics to help evaluate query performance at every stage.

#### COLLSCAN (Collection Scan)

- Scans the entire collection document by document
- nReturned: Returns all matching documents in the collection
- Can be an expensive operation, seen when no index is available

#### IXSCAN (Index Scan)

- Uses an index to find matching documents
- nReturned: Only matching documents based on the index
- Efficient operation, preferred over COLLSCAN

#### SORT

- Sorts documents based on specified fields
- If the sort attribute in the query is not part of an index, this stage will appear explicitly
- nReturned: Same number as input documents
- Memory-intensive for large result sets. To optimize, add the sort field name to an index

#### LIMIT_SKIP

- Controls the number of documents returned and skipped
- nReturned: Limited by the LIMIT value
- Used for pagination or LIMIT operations

#### SUBSCAN

- Performs nested query operations
- nReturned: Varies based on subquery results
- Used in complex queries with multiple stages

Stages with high executionTimeMillisEstimate are good candidates for optimization.

###### Note

The executionStats parameter does not currently support update and delete commands.
