# Functional differences: Amazon DocumentDB and MongoDB

The following are the functional differences between Amazon DocumentDB (with MongoDB compatibility) and
MongoDB.

###### Topics

- [Functional benefits of Amazon DocumentDB](#functional-differences.functional-benefits "#functional-differences.functional-benefits")
- [Updated functional differences](#functional-differences.updated-functional-differences "#functional-differences.updated-functional-differences")
- [Functional differences with MongoDB](#functional-differences.with-mongodb "#functional-differences.with-mongodb")

## Functional benefits of Amazon DocumentDB

### Implicit transactions

In Amazon DocumentDB, all CRUD statements (`findAndModify`, `update`, `insert`, `delete`) guarantee atomicity and consistency, even for operations that modify multiple documents.
With the launch of Amazon DocumentDB 4.0, explicit transactions that provide ACID properties for multi-statement and multi-collection operations are now supported.
For more on using transactions in Amazon DocumentDB, please see [Transactions in Amazon DocumentDB](transactions.md "transactions.md").

The following are examples of operations in Amazon DocumentDB
that modify multiple documents that satisfy both atomic and
consistent behaviors.

```
db.miles.update(
    { "credit_card": { $eq: true } },
    { $mul: { "flight_miles.$[]": NumberInt(2) } },
    { multi: true }
)

```

```
db.miles.updateMany(
    { "credit_card": { $eq: true } },
    { $mul: { "flight_miles.$[]": NumberInt(2) } }
)

```

```
db.runCommand({
  update: "miles",
  updates: [
    {
      q: { "credit_card": { $eq: true } },
      u: { $mul: { "flight_miles.$[]": NumberInt(2) } },
      multi: true
    }
  ]
})

```

```
db.products.deleteMany({
  "cost": { $gt: 30.00 }
})

```

```
db.runCommand({
  delete: "products",
  deletes: [{ q: { "cost": { $gt: 30.00 } }, limit: 0 }]
})

```

The individual operations that compose bulk operations such as
`updateMany` and `deleteMany` are atomic but
the entirety of the bulk operation is not atomic. For example, the
entirety of the `insertMany` operation is atomic if the
individual insert operations execute successfully without error. If
an error is encountered with an `insertMany` operation,
each individual insert statement within the `insertMany`
operation will execute as an atomic operation. If you require ACID properties for `insertMany`, `updateMany`, and `deleteMany` operations, it is recommended to use a transaction.

## Updated functional differences

Amazon DocumentDB continues to improve compatibility with MongoDB by working
backwards from the capabilities our customers ask us to build. This
section contains the functional differences that we have removed in
Amazon DocumentDB to make migrations and building applications easier for our
customers.

###### Topics

- [Array indexing](#functional-differences.array-indexing "#functional-differences.array-indexing")
- [Multi-key indexes](#functional-differences.multi-key-indexes "#functional-differences.multi-key-indexes")
- [Null characters in strings](#functional-differences.strings "#functional-differences.strings")
- [Role-based access control](#functional-differences.role_based_access_control "#functional-differences.role_based_access_control")
- [$regex indexing](#functional-differences.regex-indexing "#functional-differences.regex-indexing")
- [Projection for nested documents](#functional-differences.nested-docs "#functional-differences.nested-docs")

### Array indexing

As of April 23, 2020, Amazon DocumentDB now supports the ability to index arrays that are greater than 2,048 bytes. The limit for an individual item in an array still remains as 2,048 bytes, which is consistent with MongoDB.

If you are creating a new index, no action is needed to take
advantage of the improved functionality. If you have an existing
index, you can take advantage of the improved functionality by
dropping the index and then recreating it. The current index version
with the improved capabilities is `"v" : 3`.

###### Note

For production clusters, the dropping of the index may have an
impact on your application performance. We recommend that you
first test and proceed with caution when making changes to a
production system. In addition, the time it will take to recreate
the index will be a function of the overall data size of the
collection.

You can query for the version of your indexes using the following
command.

```
db.collection.getIndexes()
```

Output from this operation looks something like the following. In this output, the version of the index is `"v" : 3`, which is the most current index version.

```
[
    {
        "v" : 3,
        "key" : {
        "_id" : 1
        },
        "name" : "_id_",
        "ns" : "test.test"
    }
]
```

### Multi-key indexes

As of April 23, 2020, Amazon DocumentDB now supports the ability to create
a compound index with multiple keys in the same array.

If you are creating a new index, no action is needed to take advantage of the improved functionality. If you have an existing index, you can take advantage of the improved functionality by dropping the index and then recreating it. The current index version with the improved capabilities is `"v" : 3`.

###### Note

For production clusters, the dropping of the index may have an
impact on your application performance. We recommend that you
first test and proceed with caution when making changes to a
production system. In addition, the time it will take to recreate
the index will be a function of the overall data size of the
collection.

You can query for the version of your indexes using the following command.

```
db.collection.getIndexes()
```

Output from this operation looks something like the following. In this output, the version of the index is `"v" : 3`, which is the most current index version.

```
[
    {
        "v" : 3,
        "key" : {
            "_id" : 1
        },
        "name" : "_id_",
        "ns" : "test.test"
    }
]

```

### Null characters in strings

As of June 22, 2020, Amazon DocumentDB now supports null characters
( `'\0'` ) in strings.

### Role-based access control

As of March 26, 2020, Amazon DocumentDB supports role-based access control
(RBAC) for built-in roles. To learn more, see [Role-Based Access
Control](role_based_access_control.md "role_based_access_control.md").

### `$regex` indexing

As of June 22, 2020, Amazon DocumentDB now supports the ability for `$regex` operators to utilize an index.

To utilize an index with the `$regex` operator, you must use the `hint()` command. When using `hint()`, you must specify the name of the field you are applying the `$regex` on. For example, if you have an index on field `product` with the index name as `p_1`, `db.foo.find({product: /^x.*/}).hint({product:1})` will utilize the `p_1` index, but `db.foo.find({product: /^x.*/}).hint(“p_1”)` will not utilize the index. You can verify if an index is chosen by utilizing the `explain()` command or using the profiler for logging slow queries. For example, `db.foo.find({product: /^x.*/}).hint(“p_1”).explain()`.

###### Note

The `hint()` method can only be used with one index at a time.

The use of an index for a `$regex` query is optimized for regex queries that utilize a prefix and do not specify the `i`, `m`, or `o` regex options.

When using an index with `$regex`, it is recommended that you create an index on highly selective fields where the number of duplicate values is less than 1% of the total number of documents in the collection. As an example, if your collection contains 100,000 documents, only create indexes on fields where the same value occurs 1000 times or fewer.

### Projection for nested documents

There is a functional difference with `$project` operator between Amazon DocumentDB and MongoDB in version 3.6 that has been resolved in Amazon DocumentDB 4.0 but will remain unsupported in Amazon DocumentDB 3.6.

Amazon DocumentDB 3.6 only considers the first field in a nested document when applying a projection whereas MongoDB 3.6 will parse subdocuments and apply the projection to each sub document as well.

For example: if the projection is `“a.b.c”: 1`, then the behavior works as expect in both Amazon DocumentDB and MongoDB. However, if the projection is `{a:{b:{c:1}}}` then Amazon DocumentDB 3.6 will only apply the projection to `a` and not `b` or `c`. In Amazon DocumentDB 4.0, the projection `{a:{b:{c:1}}}` will be applied to `a`, `b`, and `c`.

## Functional differences with MongoDB

###### Topics

- [$vectorSearch operator](#functional-differences.vector-search "#functional-differences.vector-search")
- [OpCountersCommand](#functional-differences.op-counter "#functional-differences.op-counter")
- [Admin databases and collections](#functional-differences.admin-databases "#functional-differences.admin-databases")
- [cursormaxTimeMS](#functional-differences.cursormaxTimeMS "#functional-differences.cursormaxTimeMS")
- [explain()](#functional-differences.explain "#functional-differences.explain")
- [Index builds](#functional-differences.background-indexes "#functional-differences.background-indexes")
- [Lookup with empty key in path](#functional-differences.lookup-empty "#functional-differences.lookup-empty")
- [MongoDB APIs, operations, and data types](#functional-differences.mongo-apis "#functional-differences.mongo-apis")
- [mongodump and mongorestore utilities](#functional-differences.mongodump-mongorestore "#functional-differences.mongodump-mongorestore")
- [Result ordering](#functional-differences.result-ordering "#functional-differences.result-ordering")
- [Retryable writes](#functional-differences.retryable-writes "#functional-differences.retryable-writes")
- [Sparse index](#functional-differences.sparse-index "#functional-differences.sparse-index")
- [Using $elemMatch within an $all expression](#functional-differences.elemMatch "#functional-differences.elemMatch")
- [Dollar($) and dot(.) in field names](#functional-differences-dollardot "#functional-differences-dollardot")
- [$lookup](#functional-differences.lookup "#functional-differences.lookup")
- [$natural and reverse sorting](#functional-differences.natural "#functional-differences.natural")

### `$vectorSearch` operator

Amazon DocumentDB does not support `$vectorSearch` as an independent operator.
Instead we support, `vectorSearch` inside the `$search` operator.
For more information, see [Vector search for Amazon DocumentDB](vector-search.md "vector-search.md").

### `OpCountersCommand`

Amazon DocumentDB's `OpCountersCommand` behavior deviates from MongoDB's `opcounters.command` as follows:

- MongoDB's `opcounters.command` counts all commands except insert, update, and delete while Amazon DocumentDB's `OpCountersCommand` also excludes the `find` command.
- Amazon DocumentDB counts some internal commands toward the `OpCountersCommand`.

### Admin databases and collections

Amazon DocumentDB does not support the admin or local database nor MongoDB
`system.*` or `startup_log` collections
respectively.

### `cursormaxTimeMS`

In Amazon DocumentDB, `cursor.maxTimeMS` resets the counter for each `getMore` request.
Thus, if a 3000MS `maxTimeMS` is specified, the query takes 2800MS, and each subsequent `getMore` request takes 300MS, then the cursor will not timeout.
The cursor will only timeout when a single operations, either the query or an individual `getMore` request, takes more than the specified `maxTimeMS`.
Further, the sweeper that checks cursor execution time runs at a five (5) minute granularity.

### explain()

Amazon DocumentDB emulates the MongoDB 3.6, 4.0, and 5.0 APIs on a purpose-built database
engine that utilizes a distributed, fault-tolerant, self-healing
storage system. As a result, query plans and the output of
`explain()` may differ between Amazon DocumentDB and MongoDB.
Customers who want control over their query plan can use the
`$hint` operator to enforce selection of a preferred
index.

### Index builds

Amazon DocumentDB allows only one index build to occur on a collection at
any given time. Either in the foreground or the background. If operations such as
`createIndex()` or `dropIndex()` occur on the
same collection when an index build is currently in progress, the
newly attempted operation will fail.

By default, index builds in Amazon DocumentDB and MongoDB version 4.0 occur in the foreground. MongoDB version 4.2, and later ignores the background index build option if specified to
createIndexes or its shell helpers `createIndex()` and `createIndexes()`.

A Time to Live (TTL) index starts expiring documents after the
index build is completed.

### Lookup with empty key in path

When you look up with a key that includes empty string as part of the path (e.g. `x.`, `x..b`), and the object has an empty string key path (e.g. `{"x" : [ { "" : 10 }, { "b" : 20 } ]}`) inside an array, Amazon DocumentDB will return different results than if you were to run the same look up in MongoDB.

In MongoDB, the empty key path look up within array works as expected when the empty string key is not at the end of path look up. However, when the empty string key is at the end of path look up, it does not look into the array.

However in Amazon DocumentDB, only the first element within the array is read, because `getArrayIndexFromKeyString` converts empty string to `0`, so string key look up is treated as array index look up.

### MongoDB APIs, operations, and data types

Amazon DocumentDB is compatible with the MongoDB 3.6, 4.0, and 5.0 APIs. For an up-to-date
list of supported functionality, see [Supported MongoDB APIs, operations, and data types in Amazon DocumentDB](mongo-apis.md "mongo-apis.md").

### `mongodump` and `mongorestore` utilities

Amazon DocumentDB does not support an admin database and thus does not dump
or restore the admin database when using the `mongodump`
or `mongorestore` utilities. When you create a new
database in Amazon DocumentDB using `mongorestore`, you need to
re-create the user roles in addition to the restore operation.

###### Note

We recommend MongoDB Database Tools up to and including version 100.6.1 for Amazon DocumentDB.
You can access the MongoDB Database Tools downloads [here](https://www.mongodb.com/download-center/database-tools/releases/archive "https://www.mongodb.com/download-center/database-tools/releases/archive").

### Result ordering

Amazon DocumentDB does not guarantee implicit result sort ordering of result
sets. To ensure the ordering of a result set, explicitly specify a
sort order using `sort()`.

The following example sorts the items in the inventory collection
in descending order based on the stock field.

```
db.inventory.find().sort({ stock: -1 })

```

When using the `$sort` aggregation stage, the sort order is not preserved unless the `$sort` stage is the last stage in the aggregation pipeline. When using the `$sort` aggregation stage in combination with the `$group` aggregation stage, the `$sort` aggregation stage is only applied to the `$first` and `$last` accumulators. In Amazon DocumentDB 4.0, support was added for `$push` to respect sort order from the previous `$sort` stage.

### Retryable writes

Starting with MongoDB 4.2 compatible drivers, retryable writes are
enabled by default. However, Amazon DocumentDB does not currently support
retryable writes. The functional difference will manifest itself in
an error message similar to the following.

```
{"ok":0,"errmsg":"Unrecognized field: 'txnNumber'","code":9,"name":"MongoError"}
```

Retryable writes can be disabled via the connection string (for example, `MongoClient("mongodb://my.mongodb.cluster/db?retryWrites=false")`) or the MongoClient constructor’s keyword argument (for example, `MongoClient("mongodb://my.mongodb.cluster/db", retryWrites=False)`).

The following is a Python example that disables retryable writes in the connection string.

```
client = pymongo.MongoClient('mongodb://`<username>`:`<password>`@docdb-2019-03-17-16-49-12.cluster-ccuszbx3pn5e.us-east-1.docdb.amazonaws.com:27017/?replicaSet=rs0',w='majority',j=True,retryWrites=False)
```

### Sparse index

To use a sparse index that you have created in a query, you must use the `$exists` clause on the fields that cover the index. If you omit `$exists`, Amazon DocumentDB will not use the sparse index.

The following is an example.

```
db.inventory.count({ "stock": { $exists: true }})
```

For sparse, multi-key indexes, Amazon DocumentDB does not support a unique key constraint if the look up of a document results in a set of values and only a subset of the indexed fields is missing. For example, `createIndex({"a.b" : 1 }, { unique : true, sparse :true })` is not supported, given the input of `"a" : [ { "b" : 2 }, { "c" : 1 } ]`, as `"a.c"` is stored in the index.

### Using `$elemMatch` within an `$all` expression

Amazon DocumentDB does not currently support the use of the
`$elemMatch` operator within an `$all`
expression. As a workaround, you can use the `$and`
operator with `$elemMatch` as follows.

Original operation:

```
db.col.find({
  qty: {
    $all: [
      { "$elemMatch": { part: "xyz", qty: { $lt: 11 } } },
      { "$elemMatch": { num: 40, size: "XL" } }
    ]
  }
})

```

Updated operation:

```
db.col.find({
  $and: [
    { qty: { "$elemMatch": { part: "xyz", qty: { $lt: 11 } } } },
    { qty: { "$elemMatch": { qty: 40, size: "XL" } } }
  ]
})

```

### Dollar($) and dot(.) in field names

Amazon DocumentDB does not support querying Dollar($) prefixed fields in $in, $nin and $all in nested objects.
For example, the following query is not valid in Amazon DocumentDB:

```
coll.find({"field": {"$all": [{ "$a": 1 }]}})
```

### `$lookup`

Amazon DocumentDB supports the ability to do equality matches (for example, left outer join) and also supports uncorrelated subqueries, but does not support correlated subqueries.

#### Utilizing an index with `$lookup`

You can now utilize an index with the `$lookup` stage operator.
Based on your use case, there are multiple indexing algorithms that you can use to optimize for performance.
This section will explain the different indexing algorithms for `$lookup` and help you choose the best one for your workload.

By default, Amazon DocumentDB will utilize the hash algorithm when `allowDiskUse:false` is used and sort merge when `allowDiskUse:true` is used.

###### Note

The `allowDiskUse` option is currently not supported for the `find` command.
The option is only supported as part of aggregation.
We recommend using the aggregation framework with `allowDiskUse:true` to handle large queries that might exceed memory limits.

For some use cases, it may be desirable to force the query optimizer to use a different algorithm.
Below are the different indexing algorithms that the `$lookup` aggregation operator can use:

- **Nested loop**: A nested loop plan is typically beneficial for a workload if the foreign collection is <1 GB and the field in the foreign collection has an index.
  If the nested loop algorithm is being used, the explain plan will show the stage as `NESTED_LOOP_LOOKUP`.
- **Sort merge**: A sort merge plan is typically beneficial for a workload if the foreign collection does not have an index on the field used in lookup and the working dataset doesn’t fit in memory.
  If the sort merge algorithm is being used, the explain plan will show the stage as `SORT_LOOKUP`.
- **Hash**: A hash plan is typically beneficial for a workload if the foreign collection is < 1 GB and the working dataset fits in memory.
  If the hash algorithm is being used, the explain plan will show the stage as `HASH_LOOKUP`.

You can identify the indexing algorithm that is being used for the `$lookup` operator by using `explain` on the query. Below is an example:

```

db.localCollection.explain().aggregate(
   [
      {
         $lookup:
            {
               from: "foreignCollection",
               localField: "a",
               foreignField: "b",
               as: "joined"
            }
      }
   ]
)

output
{
    "queryPlanner" : {
        "plannerVersion" : 1,
        "namespace" : "test.localCollection",
        "winningPlan" : {
            "stage" : "SUBSCAN",
            "inputStage" : {
                "stage" : "SORT_AGGREGATE",
                "inputStage" : {
                    "stage" : "SORT",
                    "inputStage" : {
                        "stage" : "NESTED_LOOP_LOOKUP",
                        "inputStages" : [
                            {
                                "stage" : "COLLSCAN"
                            },
                            {
                                "stage" : "FETCH",
                                "inputStage" : {
                                    "stage" : "COLLSCAN"
                                }
                            }
                        ]
                    }
                }
            }
        }
    },
    "serverInfo" : {
        "host" : "devbox-test",
        "port" : 27317,
        "version" : "3.6.0"
    },
    "ok" : 1
}

```

As an alternative to using the `explain()` method, you can use the profiler to review the algorithm that is being utilized with your use of the `$lookup` operator. For more information on the profiler, please see [Profiling Amazon DocumentDB operations](profiling.md "profiling.md").

#### Using a `planHint`

If you wish to force the query optimizer to use a different indexing algorithm with `$lookup`, you can use a `planHint`.
To do that, use the comment in the aggregation stage options to force a different plan.
Below is an example of the syntax for the comment:

```
comment : {
    comment :  "<string>",
    lookupStage : { planHint : "SORT" | "HASH" | "NESTED_LOOP" }
}
```

Below is an example of using the `planHint` to force the query optimizer to use the `HASH` indexing algorithm:

```

db.foo.aggregate(
   [
      {
         $lookup:
            {
               from: "foo",
               localField: "_id",
               foreignField: "_id",
               as: "joined"
            },
      }
   ]
),
{
   comment : "{ \"lookupStage\" : { \"planHint\": \"HASH\" }}"

```

To test which algorithm is best for your workload, you can use the `executionStats` parameter of the `explain` method to measure the execution time of the `$lookup` stage while modifying the indexing algorithm (i.e., `HASH`/`SORT`/`NESTED_LOOP`).

The following example shows how to use `executionStats` to measure the execution time of the `$lookup` stage using the `SORT` algorithm.

```

db.foo.explain("executionStats").aggregate(
   [
      {
         $lookup:
            {
               from: "foo",
               localField: "_id",
               foreignField: "_id",
               as: "joined"
            },
      }
   ]
),
{
   comment : "{ \"lookupStage\" : { \"planHint\": \"SORT\" }}"
```

### `$natural` and reverse sorting

Amazon DocumentDB supports `$natural` for forward collection scans only. Reverse
collection scans (`{$natural: -1}`) will lead to a
`MongoServerError`.
