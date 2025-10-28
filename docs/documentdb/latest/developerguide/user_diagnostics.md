# Troubleshooting performance and resource utilization

This section provides questions and solutions for common diagnostics
issues in Amazon DocumentDB deployments. The examples provided use the
_mongo shell_ and are scoped to an individual
instance. To find an instance endpoint, see [Understanding Amazon DocumentDB endpoints](endpoints.md "endpoints.md").

###### Topics

- [How do I determine the number of insert, update, and delete operations performed on my collection through the Mongo API?](#user-diag-performed-operations "#user-diag-performed-operations")
- [How do I analyze cache performance?](#user-diag-cache-perf "#user-diag-cache-perf")
- [How do I find
  and terminate long running or blocked queries?](#user_diagnostics-query_terminating "#user_diagnostics-query_terminating")
- [How can I see a query
  plan and optimize a query?](#user_diagnostics-query_plan "#user_diagnostics-query_plan")
- [How can I see a query plan in elastic clusters?](#user-diagnostics-ec-query-plan "#user-diagnostics-ec-query-plan")
- [How do I list all
  running operations on an instance?](#user_diagnostics-list_queries "#user_diagnostics-list_queries")
- [How do I know
  when a query is making progress?](#user_diagnostics-query_progressing "#user_diagnostics-query_progressing")
- [How do I determine why a system suddenly runs slowly?](#user_diagnostics-speed_change "#user_diagnostics-speed_change")
- [How do I
  determine the cause of high CPU utilization on one or more
  cluster instances?](#user_diagnostics-cpu_utilization "#user_diagnostics-cpu_utilization")
- [How do I determine
  the open cursors on an instance?](#user_diagnostics-open_cursors "#user_diagnostics-open_cursors")
- [How do I determine the current Amazon DocumentDB engine version?](#user_diagnostics-engine_version "#user_diagnostics-engine_version")
- [How do I analyze index usage and identify unused indexes?](#user-diag-index-usage "#user-diag-index-usage")
- [How do I
  identify missing indexes?](#user_diagnostics-identify_missing_indexes "#user_diagnostics-identify_missing_indexes")
- [How do I determine database collection bloat?](#performance-collection-bloat "#performance-collection-bloat")
- [Summary of useful
  queries](#user_diagnostics-useful_queries "#user_diagnostics-useful_queries")

## How do I determine the number of insert, update, and delete operations performed on my collection through the Mongo API?

To view the number of insert, update, and delete operations performed on a certain collection, run the following command on that collection:

```
db.collection.stats()
```

The output from this command describes the following under its `opCounters` field:

- **numDocsIns** - The number of documents inserted into this collection.
  This includes documents inserted using the `insert` and `insertMany` commands, as well as documents inserted by an upsert.
- **numDocsUpd** - The number of documents updates in this collection.
  This includes documents updated using the `update` and `findAndModify` commands.
- **numDocsDel** - The number of documents deleted from this collection.
  This includes documents deleted using the `deleteOne`, `deleteMany`, `remove`, and `findAndModify` commands.
- **lastReset** - The time these counters have been last reset.
  The statistics provided by this command are reset when starting/stopping the cluster or scaling up/down the instance.

An example output from running `db.collection.stats()` is shown below.

```
{
    "ns" : "db.test",
    "count" : ...,
    "size" : ...,
    "avgObjSize" : ...,
    "storageSize" : ...,
    "capped" : false,
    "nindexes" : ...,
    "totalIndexSize" : ...,
    "indexSizes" : {
        "_id_" : ...,
        "x_1" : ...
    },
    "collScans" : ...,
    "idxScans" : ...,
    "opCounter" : {
        "numDocsIns" : ...,
        "numDocsUpd" : ...,
        "numDocsDel" : ...
    },
    "cacheStats" : {
        "collBlksHit" : ...,
        "collBlksRead" : ..,
        "collHitRatio" : ...,
        "idxBlksHit" : ...,
        "idxBlksRead" : ...,
        "idxHitRatio" : ...
    },
    "lastReset" : "2022-09-02 19:41:40.471473+00",
    "ok" : 1,
    "operationTime" : Timestamp(1662159707, 1)
}
```

This stats command should be used when viewing collection-specific counters for insert, update, and delete operation through the Mongo API.
Another way to view collection-specific operation counters is by enabling DML auditing.
The number of insert, update, and delete operations over all collections during one minute time intervals can be viewed in [Monitoring Amazon DocumentDB with CloudWatch](cloud_watch.md "cloud_watch.md").

## How do I analyze cache performance?

Analyzing cache performance can give insights into the efficiency of data retrieval and system performance, and is based on how much data is read from the disk versus the cache.
We provide cache statistics about the number of cache hits (data read from the cache) and cache misses (data that is not found in the cache and read from the disk) in order give insight into the cache performance.
The cache statistics for a specific collection can by found by running the following command on that collection:

```
db.collection.stats()
```

The values in the `cacheStats` field in the output of this command provide cache statistics for the collection as well as the total cache statistics for the indexes created on the collection.
These statistics are listed below:

- **`collBlksHit`** - The number of blocks read from the cache during operations on this collection.
- **`collBlksRead`** - The number of blocks read from the disk (cache misses) during operations on this collection.
- **`collHitRatio`** - The cache hit ratio for this collection (`100 * [collBlksHit / (collBlksHit + collBlksRead)]`).
- **`idxBlksHit`** - The number of blocks read from the cache for any index created on this collection.
- **`idxBlksRead`** - The number of blocks read from the disk (cache misses) for any index created on this collection.
- **`idxHitRatio`** - The cache hit ratio for the indexes created on this collection (`100 * [idxBlksHit / (idxBlksHit + idxBlksRead)]`).
- **`lastReset`** - The time these statistics have been last reset.
  The statistics provided by `db.collection.stats()` are reset when starting/stopping the cluster or scaling up/down the instance.

A breakdown of the `idxBlksHit` and `idxBlksRead` fields for each index can also be found using the `indexStats` command.
Index specific cache statistics can be found by running the following command:

```
db.collection.aggregate([{$indexStats:{}}]).pretty()
```

For each index, the following cache statistics can be found under the `cacheStats` field:

- **`blksHit`** - The number of blocks read from cache for this index.
- **`blksRead`** - The number of blocks read from the disk for this index.
- **`blksHitRatio`** - The cache hit ratio rounded to four decimal places, calculated by `100 * [blksHit / (blksHit + blksRead)]`.

## How do I find

and terminate long running or blocked queries?

User queries can run slowly because of a suboptimal query plan or
can be blocked due to resource contention.

To find long running queries that slow down due to a suboptimal
query plan, or queries that are blocked due to resource contention,
use the `currentOp` command. You can filter the command
to help narrow down the list of relevant queries to terminate. You
must have `opid` associated with the long running query
to be able to terminate the query.

The following query uses the `currentOp` command to
list all queries that are either blocked or running for more than 10
seconds.

```
db.adminCommand({
    aggregate: 1,
    pipeline: [
        {$currentOp: {}},
        {$match:
            {$or: [
                {secs_running: {$gt: 10}},
                {WaitState: {$exists: true}}]}},
        {$project: {_id:0, opid: 1, secs_running: 1}}],
    cursor: {}
});
```

Next, you can narrow down the query to find the `opid` of a query running for more than 10 seconds and terminate it.

###### To find and terminate a query running for more than 10

seconds

1. Find the `opid` of the query.

```
db.adminCommand({
    aggregate: 1,
    pipeline: [
        {$currentOp: {}},
        {$match:
            {$or:
                [{secs_running: {$gt: 10}},
                 {WaitState: {$exists: true}}]}}],
    cursor: {}
});
```

Output from this operation looks something like the following (JSON format).

```
{
    "waitedMS" : NumberLong(0),
    "cursor" : {
        "firstBatch" : [
            {
                `"opid" : 24646`,
                "secs_running" : 12
            }
        ],
        "id" : NumberLong(0),
        "ns" : "admin.$cmd"
    },
    "ok" : 1
}
```

2. Terminate the query using the `killOp`
   operation.

```
db.adminCommand({killOp: 1, op: 24646});
```

## How can I see a query

plan and optimize a query?

If a query runs slow, it could be because the query execution
requires a full scan of the collection to choose the relevant
documents. Sometimes creating appropriate indexes enables the query
to run faster. To detect this scenario and decide the fields on
which to create the indexes, use the `explain` command.

###### Note

Amazon DocumentDB emulates the MongoDB 3.6 API on a purpose-built
database engine that utilizes a distributed, fault-tolerant,
self-healing storage system. As a result, query plans and the
output of `explain()` may differ between Amazon DocumentDB and
MongoDB. Customers who want control over their query plan can
use the `$hint` operator to enforce selection of a
preferred index.

Run the query that you want to improve under the
`explain` command as follows.

```
db.runCommand({explain: {`<query document>`}})
```

The following is an example operation.

```
db.runCommand({explain:{
    aggregate: "sample-document",
    pipeline: [{$match: {x: {$eq: 1}}}],
    cursor: {batchSize: 1}}
});
```

Output from this operation looks something like the following (JSON format).

```
{
    "queryPlanner" : {
        "plannerVersion" : 1,
        "namespace" : "db.test",
        "winningPlan" : {
            "stage" : "`COLLSCAN`"
        }
    },
    "serverInfo" : {
        "host" : "...",
        "port" : ...,
        "version" : "..."
    },
    "ok" : 1
}
```

The preceding output indicates that the `$match` stage
requires scanning the whole collection and checking if the field
`"x"` in each document is equal to 1. If there are many
documents in the collection, the collection scan (and therefore the
overall query performance) is very slow. Thus the presence of the
`"COLLSCAN"` in the output of the `explain`
command indicates that the query performance can be improved by
creating appropriate indexes.

In this example, the query checks whether the field
`"x"` equals 1 in all documents. So creating an index on
field `"x"` enables the query to avoid the complete
collection scan and use the index to return the relevant documents
sooner.

After creating an index on field `"x"`, the
`explain` output is as follows.

```
{
    "queryPlanner" : {
         "plannerVersion" : 1,
         "namespace" : "db.test",
         "winningPlan" : {
             "stage" : "`IXSCAN`",
             "indexName" : "`x_1`",
             "direction" : "`forward`"
         }
    },
    "serverInfo" : {
        "host" : "...",
        "port" : ...,
        "version" : "..."
    },
    "ok" : 1
}
```

Creating an index on field `"x"` enables the
`$match` stage to use an index scan to reduce the number
of documents on which the predicate `"x = 1"` must be
evaluated.

For small collections, the Amazon DocumentDB query processor can choose not to use an index if the performance gains are negligible.

## How can I see a query plan in elastic clusters?

To examine a query plan in elastic clusters, use the `explain` command.
The following is an example `explain` operation on a find query targeting a sharded collection:

```
db.runCommand(
   {
     explain: { find: "cities", filter: {"name": "Seoul"}}
   }
)
```

###### Note

Amazon DocumentDB emulates MongoDB on a purpose-built database engine.
As a result, query plans and the output of `explain()` may differ between Amazon DocumentDB and MongoDB.
You can control query plan with the use of the `$hint` operator to enforce selection of a preferred index.

Output from this operation may look something like the following (JSON format):

```
{
  "queryPlanner" : {
    "elasticPlannerVersion" : 1,
    "winningPlan" : {
      "stage" : "SINGLE_SHARD",
      "shards" : [
        {
          "plannerVersion" : 1,
          "namespace" : "population.cities",
          "winningPlan" : {
            "stage" : "SHARD_MERGE",
            "shards" : [
              {
                "shardName" : "f2cf5cfd-fe9c-40ca-b4e5-298ca0d11111",
                "plannerVersion" : 1,
                "namespace" : "population.cities",
                "winningPlan" : {
                  "stage" : "PARTITION_MERGE",
                  "inputStages" : [
                    {
                      "stage" : "COLLSCAN",
                      "partitionCount" : 21
                    }
                  ]
                }
              },
              {
                "shardName" : "8f3f80e2-f96c-446e-8e9d-aab8c7f22222",
                "plannerVersion" : 1,
                "namespace" : "population.cities",
                "winningPlan" : {
                  "stage" : "PARTITION_MERGE",
                  "inputStages" : [
                    {
                      "stage" : "COLLSCAN",
                      "partitionCount" : 21
                    }
                  ]
                }
              },
              {
                "shardName" : "32c5a06f-1b2b-4af1-8849-d7c4a033333",
                "plannerVersion" : 1,
                "namespace" : "population.cities",
                "winningPlan" : {
                  "stage" : "PARTITION_MERGE",
                  "inputStages" : [
                    {
                      "stage" : "COLLSCAN",
                      "partitionCount" : 22
                    }
                  ]
                }
              }
            ]
          },
          "shardName" : "32c5a06f-1b2b-4af1-8849-d7c4a0f3fb58"
        }
      ]
    }
  },
  "serverInfo" : {
    "host" : "example-4788267630.us-east-1.docdb-elastic.amazonaws.com:27017",
    "version" : "5.0.0"
  },
  "ok" : 1,
  "operationTime" : Timestamp(1695097923, 1)
}
```

The preceding output shows the query plan for the `find` query on a three-shard cluster.
Each shard has multiple data partitions which can have different input stages.
In this example, a “COLLSCAN“ (a collection scan) is run on all partitions before the results are merged at the ”PARTITION_MERGE“ stage within each shard.
The results across the shards are then merged together at the ”SHARD_MERGE“ stage before being sent back to the client.

## How do I list all

running operations on an instance?

As a user or primary user, you often want to list all the current
operations running on an instance for diagnostics and
troubleshooting purposes. (For information about managing users, see [Managing Amazon DocumentDB users](security.md "security.md").)

With the `mongo` shell, you can use the following query
to list all the running operations on an Amazon DocumentDB instance.

```
db.adminCommand({currentOp: 1, $all: 1});
```

The query returns the complete list of all user queries and
internal system tasks currently operating on the instance.

Output from this operation looks something like the following (JSON format).

```
{
    "inprog" : [
        {
            "desc" : "INTERNAL"
        },
        {
            "desc" : "TTLMonitor",
            "active" : false
        },
        {
            "client" : ...,
            "desc" : "Conn",
            "active" : true,
            "killPending" : false,
            "opid" : 195,
            "ns" : "admin.$cmd",
            "command" : {
                "currentOp" : 1,
                "$all" : 1
            },
            "op" : "command",
            "$db" : "admin",
            "secs_running" : 0,
            "microsecs_running" : NumberLong(68),
            "clientMetaData" : {
            "application" : {
                "name" : "MongoDB Shell"
            },
            "driver" : {
                ...
            },
            "os" : {
                ...
            }
          }
       },
       {
          "desc": "GARBAGE_COLLECTION",
          "garbageCollection": {
             "databaseName": "testdb",
             "collectionName": "testCollectionA"
          },
          "secs_running": 3,
          "microsecs_running": NumberLong(3123456)
       },
       {
          "desc": "GARBAGE_COLLECTION",
          "garbageCollection": {
             "databaseName": "testdb",
             "collectionName": "testCollectionB"
          },
          "secs_running": 4,
          "microsecs_running": NumberLong(4123456)
       }
    ],
    "ok" : 1
}
```

The following are valid values for the `"desc"` field:

- `INTERNAL` — Internal system
  tasks like the cursor cleanup or stale user cleanup tasks.
- `TTLMonitor` — The Time to
  Live (TTL) monitor thread. Its running status is reflected
  in the `"active"` field.
- `GARBAGE_COLLECTION` — The
  internal garbage collector thread.
- `CONN` — The user query.
- `CURSOR` — The operation is an idle cursor waiting on the user to call the "getMore" command to get the next batch of results. In this state, the cursor is consuming memory, but is not consuming any compute.

The preceding output also lists all user queries running in the
system. Each user query runs in the context of a database and
collection, and the union of these two is called a
_namespace_. The namespace of each user query is
available in the `"ns"` field.

Sometimes you need to list all user queries that are running in a
particular namespace. So the previous output must be filtered on the
`"ns"` field. The following is an example query to
achieve the output to filter. The query lists all user queries that
are currently running in the database `"db"` and
collection `"test"` (that is, the `"db.test"`
namespace).

```
db.adminCommand({aggregate: 1,
    pipeline: [{$currentOp: {allUsers: true, idleConnections: true}},
               {$match: {ns: {$eq: "db.test"}}}],
    cursor: {}
});
```

As the primary user of the system, you can see queries of all users
and also all internal system tasks. All other users can see only
their respective queries.

If the total number of queries and internal system tasks exceeds
the default batch cursor size, the `mongo` shell
automatically generates an iterator object `'it'` to view
the rest of the results. Keep executing the `'it'`
command until all results have been exhausted.

## How do I know

when a query is making progress?

User queries can run slowly due to a suboptimal query plan, or
they can be blocked due to resource contention. Debugging such
queries is a multi-step process that can require executing the same
step multiple times.

The first step of debugging is to list all queries that are long
running or blocked. The following query lists all user queries that
have been running for more than 10 seconds or that are waiting for
resources.

```
db.adminCommand({aggregate: 1,
                 pipeline: [{$currentOp: {}},
                            {$match: {$or: [{secs_running: {$gt: 10}},
                                            {WaitState: {$exists: true}}]}},
                            {$project: {_id:0,
                                        opid: 1,
                                        secs_running: 1,
                                        WaitState: 1,
                                        blockedOn: 1,
                                        command: 1}}],
                 cursor: {}
                });
```

Repeat the preceding query periodically to determine whether the
list of queries changes and to identify the long running or blocked
queries.

If the output document for the query of interest has a
`WaitState` field, it indicates that resource contention
is why the query is running slow or is blocked. The resource
contention could either be due to I/O, internal system tasks, or
other user queries.

Output from this operation looks something like the following (JSON format).

```
{
    "waitedMS" : NumberLong(0),
    "cursor" : {
        "firstBatch" : [
            {
                "opid" : 201,
                "command" : {
                    "aggregate" : ...
                },
                "secs_running" : 208,
                `"WaitState" : "IO"`
            }
        ],
        "id" : NumberLong(0),
        "ns" : "admin.$cmd"
    },
    "ok" : 1
}
```

I/O can be a bottleneck if many queries across different collections are running concurrently on the same instance, or if the instance size is too small for the dataset that the query is running on. If the queries are read-only queries, you can mitigate the former situation by separating the queries for each collection across separate replicas. For concurrent updates across different collections, or when the instance size is too small for the dataset, you can mitigate by scaling up the instance.

If the resource contention is due to other user queries, the
`"blockedOn"` field in the output document will have the
`"opid"` of the query that is affecting this query. Using
the `"opid"` follows the chain of `"WaitState"`
and `"blockedOn"` fields of all the queries to find the
query at the head of the chain.

If the task at the head of the chain is an internal task, the only mitigation in this case would be to terminate the query and rerun it
later.

The following is sample output in which the find query is blocked
on a collection lock that is owned by another task.

```
{
    "inprog" : [
        {
            "client" : "...",
            "desc" : "Conn",
            "active" : true,
            "killPending" : false,
            "opid" : 75,
            "ns" : "...",
            "command" : {
                "find" : "...",
                "filter" : {

                }
            },
            "op" : "query",
            "$db" : "test",
            "secs_running" : 9,
            "microsecs_running" : NumberLong(9449440),
            "threadId" : 24773,
            "clientMetaData" : {
                "application" : {
                   "name" : "MongoDB Shell"
                },
                "driver" : {
                    ...
                },
                "os" : {
                    ...
                }
            },
            `"WaitState" : "CollectionLock",
 "blockedOn" : "INTERNAL"`
        },
        {
            `"desc" : "INTERNAL"`
        },
        {
            "client" : "...",
            ...
            "command" : {
                "currentOp" : 1
            },
            ...
        }
    ],
    "ok" : 1
}
```

If the `"WaitState"` has values `"Latch"`,
`"SystemLock"`, `"BufferLock"`,
`"BackgroundActivity"`, or `"Other"`, the
source of resource contention is internal system tasks. If the
situation continues for a long time, the only mitigation would be to
terminate the query and rerun it later.

## How do I determine why a system suddenly runs slowly?

The following are some common reasons for a system slowing down:

- Excessive resource contention between concurrent queries
- The number of active concurrent queries increasing over
  time
- Internal system tasks such as `"GARBAGE_COLLECTION"`

To monitor the system usage over time, run the following
`"currentOp"` query periodically and output the results
to an external store. The query counts the number of queries and
operations in each namespace in the system. You can then analyze the
system usage results to understand the load on the system and take
appropriate action.

```
db.adminCommand({aggregate: 1,
                 pipeline: [{$currentOp: {allUsers: true, idleConnections: true}},
                            {$group: {_id: {desc: "$desc", ns: "$ns", WaitState: "$WaitState"}, count: {$sum: 1}}}],
                 cursor: {}
                });
```

This query returns an aggregate of all queries running in each
namespace, all the internal system tasks, and the unique number of
wait states (if any) per namespace.

Output from this operation looks something like the following (JSON format).

```
{
    "waitedMS" : NumberLong(0),
    "cursor" : {
        "firstBatch" : [
            {
                "_id" : {
                    "desc" : "Conn",
                    "ns" : "db.test",
                    "WaitState" : "CollectionLock"
                },
               "count" : 2
            },
            {
                "_id" : {
                    "desc" : "Conn",
                    "ns" : "admin.$cmd"
                },
                "count" : 1
            },
            {
                "_id" : {
                    "desc" : "TTLMonitor"
                },
                "count" : 1
            }
        ],
        "id" : NumberLong(0),
        "ns" : "admin.$cmd"
    },
    "ok" : 1
}
```

In the preceding output, two user queries in namespace
`"db.test"` are blocked on collection lock: one query in
the namespace `"admin.$cmd"`, and one internal
`"TTLMonitor"` task.

If the output indicates many queries with blocking wait states,
see [How do I find
and terminate long running or blocked queries?](#user_diagnostics-query_terminating "#user_diagnostics-query_terminating")

## How do I

determine the cause of high CPU utilization on one or more
cluster instances?

The following sections might help you identify the cause of high
instance CPU utilization. Your results can vary depending on the
workload.

- To determine why an instance is suddenly running slowly,
  see [How do I determine why a system suddenly runs slowly?](#user_diagnostics-speed_change "#user_diagnostics-speed_change")
- To identify and terminate long running queries on a
  particular instance, see [How do I find
  and terminate long running or blocked queries?](#user_diagnostics-query_terminating "#user_diagnostics-query_terminating")
- To understand whether a query is progressing, see [How do I know
  when a query is making progress?](#user_diagnostics-query_progressing "#user_diagnostics-query_progressing")
- To determine why a query takes a long time to run, see [How can I see a query
  plan and optimize a query?](#user_diagnostics-query_plan "#user_diagnostics-query_plan")
- To track long-running queries over time, see [Profiling Amazon DocumentDB operations](profiling.md "profiling.md").

Depending on the reason for your high instance CPU utilization,
doing one or more of the following can help.

- If the primary instance exhibits high CPU utilization, but
  the replica instances don't, consider distributing read
  traffic across replicas via client read preference settings
  (for example, `secondaryPreferred`). For more
  information, see [Connecting to Amazon DocumentDB as a replica set](connect-to-replica-set.md "connect-to-replica-set.md").

Using replicas for reads can make better use of the
cluster’s resources by allowing the primary instance to
process more write traffic. Reads from replicas are
eventually consistent.

- If the high CPU utilization is a result of your write
  workload, changing the size of the cluster’s instances to a
  larger instance type increases the number of CPU cores
  available to service the workload. For more information, see [Instances](what-is.md#what-is-db-instances "what-is.md#what-is-db-instances") and [Instance class specifications](db-instance-classes.md#db-instance-class-specs "db-instance-classes.md#db-instance-class-specs").
- If all cluster instances exhibit high CPU utilization, and
  the workload is using replicas for reads, adding more
  replicas to the cluster increases the resources available
  for read traffic. For more information, see [Adding an Amazon DocumentDB instance to a cluster](db-instance-add.md "db-instance-add.md").

## How do I determine

the open cursors on an instance?

When connected to a Amazon DocumentDB instance, you can use the command
`db.runCommand("listCursors")` to list the open cursors on that instance. There is a limit of up to 4,560 active cursors open at any given time on a given Amazon DocumentDB instance, depending on the instance type. It is generally advised to close cursors that are no longer in use because cursors utilize resources on an instance and have an upper limit. See [Amazon DocumentDB Quotas and limits](limits.md "limits.md") for specific limits.

```
db.runCommand("listCursors")
```

## How do I determine the current Amazon DocumentDB engine version?

To determine your current Amazon DocumentDB engine version, run the
following command.

```
db.runCommand({getEngineVersion: 1})
```

Output from this operation looks something like the following (JSON format).

```
{ "engineVersion" : "2.x.x", "ok" : 1 }
```

###### Note

The engine version for Amazon DocumentDB 3.6 is 1.x.x and the engine version for Amazon DocumentDB 4.0 is 2.x.x.

## How do I analyze index usage and identify unused indexes?

To identify the indexes for a given collection, run the following command:

```
db.collection.getIndexes()
```

To analyze how much indexes are being used during operations performed on the collections, the `collStats` and `indexStats` commands can be used.
In order to view the total number of scans performed using indexes (index scans) compared to the number of scans performed without an index (collection scans), run the following command:

```
db.collection.stats()
```

The output for this command includes the following values:

- **`idxScans`** - The number of scans performed on this collection using an index.
- **`collScans`** - The number of scans performed on this collection without using an index.
  These scans would have involved looking over the documents in the collection one at a time.
- **`lastReset`** - The time these counters have been last reset.
  The statistics provided by this command are reset when starting/stopping the cluster or scaling up/down the instance.

A breakdown of how much each index is used can be found in the output of the following command.
It is a best practice to regularly identify and remove unused indexes in order to improve performance and reduce cost, as it eliminates unnecessary compute, storage, and I/Os used to maintain the indexes.

```
db.collection.aggregate([{$indexStats:{}}]).pretty()
```

The output from this command gives the following values for each index created on the collection:

- **`ops`** - The number of operations that used the index.
  If your workload has been running for a sufficiently long time and you are confident that your workload is in a steady state, an `ops` value of zero would indicate that the index is not used at all.
- **`numDocsRead`** - The number of documents read during operations using this index.
- **`since`** - The time since Amazon DocumentDB started collecting stats on index usage, which is typically the value since the last database restart or maintenance action.
- **`size`** - The size of this index in bytes.

The following example is a sample output from running the above command:

```
{
    "name" : "_id_",
    "key" : {
        "_id" : 1
    },
    "host" : "example-host.com:12345",
    "size" : NumberLong(...),
    "accesses" : {
        "ops" : NumberLong(...),
        "docsRead" : NumberLong(...),
        "since" : ISODate("...")
    },
    "cacheStats" : {
        "blksRead" : NumberLong(...),
        "blksHit" : NumberLong(...),
        "hitRatio" : ...
    }
}
{
    "name" : "x_1",
    "key" : {
        "x" : 1
    },
    "host" : "example-host.com:12345",
    "size" : NumberLong(...),
    "accesses" : {
        "ops" : NumberLong(...),
        "docsRead" : NumberLong(...),
        "since" : ISODate("...")
    },
    "cacheStats" : {
        "blksRead" : NumberLong(...),
        "blksHit" : NumberLong(...),
        "hitRatio" : ...
    }
}
```

To determine the overall index size for a collection, run the following command:

```
db.collection.stats()
```

To drop an unused index, run the following command:

```
db.collection.dropIndex("indexName")
```

## How do I

identify missing indexes?

You can use the [Amazon DocumentDB profiler to log slow queries](profiling.md "profiling.md").
A query that appears repeatedly in the slow query log may indicate
that an additional index is required to improve that query's
performance.

You can identify opportunities for helpful indexes by looking for
long running queries that have one or more stages that perform at
least one `COLLSCAN` stage, meaning that the query stage
has to read every document in the collection in order to provide a
response to the query.

The following example shows a query on a collection of taxi rides
that ran on a large collection.

```
db.rides.count({"fare.totalAmount":{$gt:10.0}}))
```

In order to execute this example, the query had to perform a
collection scan (i.e. read every single document in the collection)
since there is no index on the `fare.totalAmount` field.
Output from the Amazon DocumentDB profiler for this query looks something like
the following:

```
{
    ...
    "cursorExhausted": true,
    "nreturned": 0,
    "responseLength": 0,
    "protocol": "op_query",
    "millis": 300679,
    "planSummary": "COLLSCAN",
    "execStats": {
        "stage": "COLLSCAN",
        "nReturned": "0",
        "executionTimeMillisEstimate": "300678.042"
    },
    "client": "172.31.5.63:53878",
    "appName": "MongoDB Shell",
    "user": "example"
}
```

To speed up the query in this example, you want to create an index on
`fare.totalAmount`, as shown below.

```
db.rides.createIndex( {"fare.totalAmount": 1}, {background: true} )
```

###### Note

Indexes created in the foreground (meaning if the
`{background:true}` option was not supplied when creating
the index) take an exclusive write lock, which prevents applications
from writing data to the collection until the index build completes.
Be aware of this potential impact when creating indexes on
production clusters. When creating indexes, we recommend setting
`{background:true}`.

In general, you want to create indexes on fields that have high
cardinality (for example, a large number of unique values). Creating an
index on a field with low cardinality can result in a large index that
is not used. The Amazon DocumentDB query optimizer considers the overall size of
the collection and selectivity of the indexes when creating a query plan.
There are times where you will see the query processor select a
`COLLSCAN` even when an index is present. This happens when
the query processor estimates that utilizing the index will not yield a
performance advantage over scanning the entire collection. If you want
to force the query processor to utilize a particular index, you can use
the `hint()` operator as shown below.

```
db.collection.find().hint("`indexName`")
```

## How do I determine database collection bloat?

Collection bloat occurs when a collection's size becomes larger due to the accumulation of dead or obsolete documents or fragmentation within database pages.
The percentage reported represents the amount of document space that can be used by future documents.
This bloat consumes space in both the buffer cache and storage.
To remove the bloat, collections must be reloaded either through dump/restore or using a migration loop-back and switchover during a maintenance window.

###### Example

Run the following command to determine unused storage for your collection:

```
db.runCommand({collStats:'coll'})
```

The result looks similar to this:

```
{
        "ns" : "test.coll",
        "count" : 7500,
        "size" : 23250,
        "avgObjSize" : 31,
        "storageSize" : 106496,
        "unusedStorageSize" : {
                "unusedBytes" : `16384`,
                "unusedPercent" : `25.12`
        },
        "compression" : {
                "enable" : false
        },
        "capped" : false,
        "nindexes" : 1,
        "totalIndexSize" : 57344,
        "indexSizes" : {
                "_id_" : 57344
        },
        "collScans" : 4,
        "idxScans" : 10000,
        "opCounter" : {
                "numDocsIns" : 1000,
                "numDocsUpd" : 0,
                "numDocsDel" : 250
        },
        "cacheStats" : {
                "collBlksHit" : 3570,
                "collBlksRead" : 8,
                "collHitRatio" : 99.7765,
                "idxBlksHit" : 12293,
                "idxBlksRead" : 6,
                "idxHitRatio" : 99.9513
        },
        "lastReset" : "2024-12-18 00:30:21.552019+00",
        "ok" : 1,
        "operationTime" : Timestamp(1734632375, 1)
}
```

## Summary of useful

queries

The following queries can be useful for monitoring performance and resource utilization in Amazon DocumentDB.

- Use the following command to view statistics about a specific collection, including operation counters, cache statistics, accesses statistics, and size statistics:

```
db.collection.stats()
```

- Use the following command to view statistics about each index created on a collection including the size of the index, index-specific cache statistics, and index usage statistics:

```
db.collection.aggregate([{$indexStats:{}}]).pretty()
```

- Use the following query to list all activity.

```
db.adminCommand({currentOp: 1, $all: 1});
```

- The following code lists all long running or blocked
  queries.

```
db.adminCommand({aggregate: 1,
                 pipeline: [{$currentOp: {}},
                            {$match: {$or: [{secs_running: {$gt: 10}},
                                            {WaitState: {$exists: true}}]}},
                            {$project: {_id:0,
                                        opid: 1,
                                        secs_running: 1,
                                        WaitState: 1,
                                        blockedOn: 1,
                                        command: 1}}],
                 cursor: {}
                });
```

- The following code terminates a query.

```
db.adminCommand({killOp: 1, op: `<opid of running or blocked query>`});
```

- Use the following code to get an aggregated view of the system state.

```
db.adminCommand({aggregate: 1,
                 pipeline: [{$currentOp: {allUsers: true, idleConnections: true}},
                            {$group: {_id: {desc: "$desc", ns: "$ns", WaitState: "$WaitState"}, count: {$sum: 1}}}],
                 cursor: {}
                });
```
