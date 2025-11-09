# Managing Amazon DocumentDB indexes

###### Topics

- [Amazon DocumentDB index creation](#index-creation "#index-creation")
- [Maintaining Amazon DocumentDB indexes](#maintaining-indexes "#maintaining-indexes")

## Amazon DocumentDB index creation

Building indexes in Amazon DocumentDB requires a number of decisions to be made:

- How quickly does it need to be completed?
- Can the collection be inaccessible while the build is occurring?
- How much of an instances compute power can be allocated to the build?
- What type of index should be created?

This section helps you answer these questions and provides the commands and monitoring examples to create and Amazon DocumentDB index on your instance-based cluster collection.

### Guidelines

The following guidelines include basic limits and configuration tradeoffs when creating new indexes:

- **Amazon DocumentDB version support** - While single worker indexing is supported on all Amazon DocumentDB versions, multiple worker indexing is supported only on Amazon DocumentDB versions 4.0 and 5.0.
- **Performance trade-off** - Increasing the number of workers in the index creation process increases CPU utilization and read IO on the primary instance of your Amazon DocumentDB database.
  The resources needed to create a new index will not be available to your running workload.
- **Elastic clusters** - Parallel indexing is not supported on Amazon DocumentDB elastic clusters.
- **Maximum workers** - The maximum number of workers you can configure depends on the size of your primary instance in your database cluster.
  It is half the total number of vCPUs on the primary instance of your database cluster.
  For example, you can run a maximum of 32 workers on a db.r6g.16xlarge instance that has 64 vCPUs.

###### Note

Parallel workers are not supported on 2xlarge instance classes and lower.

- **Minimum workers** - The minimum number of workers you can configure is one.
  The default setting for index creation on instance-based clusters is two workers.
  However, you can reduce the number of workers to one by using the “worker threads” option.
  This will run the process with a single worker.
- **Index compression** - Amazon DocumentDB doesn't support index compression.
  Data sizes for indexes might be larger than when you use other options.
- **Indexing multiple collections** - Half the vCPUs on your database cluster's primary instance can be used for configured workers performing index creation on multiple collections.
- **Index types** - See [this blog post](https://aws.amazon.com/blogs/database/how-to-index-on-amazon-documentdb-with-mongodb-compatibility/ "https://aws.amazon.com/blogs/database/how-to-index-on-amazon-documentdb-with-mongodb-compatibility/") for a complete explanation of supported index types on Amazon DocumentDB.

### Getting started

To start index creation on a collection, use the `createIndexes` command.
By default, the command will run two parallel workers that increases the speed of the index creation process by two times.

For example, the following command process demonstrates how to create an index for the “user_name” field in a document and increase the indexing process speed to four workers:

1. Create indexes using two parallel workers on the cluster:

```
db.runCommand({"createIndexes":"test","indexes":[{"key": {"user_name":1}, "name":"username_idx"}]})
```

2. To optimize the speed of the index creation process, you can specify the number of workers by using the “worker threads” option (`"workers":<number>`) in the `db.runCommand createIndexes` command.

Increase the speed of the process to four parallel workers:

```
db.runCommand({"createIndexes":"test","indexes":[{"key": {"user_name":1}, "name":"username_idx", "workers":4}]})
```

###### Note

The higher the number of workers, the faster the index creation progresses.
However, the higher the number of workers increases, the higher the load increases on the vCPUs and read IO of your primary instance.
Ensure that your cluster is sufficiently provisioned to handle the increased burden without degrading other workloads.

### Indexing progress status

The index creation process works by initializing, scanning collections, sorting keys, and, finally, inserting keys by way of an index builder.
The process has up to six stages when you run it in the foreground, and up to nine stages when you run it in the background.
You can view status metrics such as percentage completion, total number of scanned storage blocks, sorted keys, and inserted keys on stage by stage basis.

Monitor the progress on the indexing process by using the `db.currentOp()` command in the mongo shell.
A 100% completion of the last stage shows that all the indexes have been successfully created:

```
db.currentOp({"command.createIndexes": { $exists : true } })
```

###### Note

Viewing the indexing progress status is only supported on Amazon DocumentDB 5.0.

#### Index build types

The four types of index builds are:

- **Foreground** — The foreground index build blocks all other database operations until the index is created.
  The Amazon DocumentDB foreground build is comprised of five stages.
- **Foreground (unique)** — Single document (unique) foreground index builds block other database operations like regular foreground builds.
  Unlike the basic foreground build, the unique build uses an additional stage (sorting keys 2) to look for duplicate keys.
  The foreground (unique) build is comprised of six stages.
- **Background** — The background index build allows other database operations to run in the foreground while the index is being created.
  The Amazon DocumentDB background build is comprised of eight stages.
- **Background (unique)** — Single document (unique) background index builds allow other database operations to run in the foreground while the index is being created.
  Unlike the basic background build, the unique build uses an additional stage (sorting keys 2) to look for duplicate keys.
  The background (unique) build is comprised of nine stages.

#### Index build stages

| Stage                               | Foreground | Foreground (unique) | Background | Background (unique) |
| ----------------------------------- | ---------- | ------------------- | ---------- | ------------------- |
| Initializing                        | 1          | 1                   | 1          | 1                   |
| building index: initializing        | 2          | 2                   | 2          | 2                   |
| building index: scanning collection | 3          | 3                   | 3          | 3                   |
| building index: sorting keys 1      | 4          | 4                   | 4          | 4                   |
| building index: sorting keys 2      |            | 5                   |            | 5                   |
| building index: inserting keys      | 5          | 6                   | 5          | 6                   |
| validating: scanning index          |            |                     | 6          | 7                   |
| validating: sorting tuples          |            |                     | 7          | 8                   |
| validating: scanning collection     |            |                     | 8          | 9                   |

- **initializing** - createIndex is preparing the index builder.
  This phase should be very brief.
- **building index: initializing** - The index builder is preparing to create the index.
  This phase should be very brief.
- **building index: scanning collection** - The index builder is performing a collection scan to collect index keys.
  The unit of measure is “blocks”.

###### Note

If more than one worker is configured for the index build, it is displayed in this stage.
The “scanning collection” stage is the only stage that uses multiple workers during the index build process.
All other stages will display a single worker.

- **building index: sorting keys 1** - The index builder is sorting the collected index keys. The unit of measure is “keys”.
- **building index: sorting keys 2** - The index builder is sorting the collected index keys that correspond to dead tuples.
  This phase only exists for unique index building. The unit of measure is “keys”.
- **building index: inserting keys** - The index builder is inserting index keys into the new index.
  The unit of measure is “keys”.
- **validating: scanning index** - createIndex is scanning the index to find keys that need to be validated.
  The unit of measure is “blocks”.
- **validating: sorting tuples** - createIndex is sorting the output of the index scanning phase.
- **validating: scanning collection** - createIndex is scanning the collection to validate the index keys found in the previous two phases.
  The unit of measure is “blocks”.

#### Index build output example

In the output example below (foreground index build), the status of the index creation is shown.
The “msg” field summarizes the build progress by indicating the stage and the completion percentage of the build.
The “workers” field indicates the number of workers used during that stage of the index build.
The “progress” field shows the actual numbers used to calculate the percentage of completion.

###### Note

The “currentIndexBuildName”, “msg”, and “progress” fields are not supported on Amazon DocumentDB version 4.0.

```
{
    "inprog" : [{
    …
        "command": {
            "createIndexes": "test",
            "indexes": [{
                "v": 2,
                "key": {
                    "user_name": 1
                },
                "name": "user_name_1"
            }],
            "lsid": {
                "id": UUID(“094d0fba-8f41-4373-82c3-7c4c7b5ff13b”)
            },
            "$db": "test"
        },
        "currentIndexBuildName": user_name_1,
        "msg": "Index Build: building index number_1, stage 6/6 building index: 656860/1003520 (keys) 65%",
        "workers": 1,
        "progress": {
            "done": 656861,
            "total": 1003520
        },
    …
    ],

    "ok" : 1
}
```

## Maintaining Amazon DocumentDB indexes

###### Topics

- [Index bloat](#db-index-bloat "#db-index-bloat")
- [Index maintenance using reIndex](#reIndex "#reIndex")

### Index bloat

Amazon DocumentDB uses Multi-Version Concurrency Control (MVCC) to manage concurrent transactions.
When documents are deleted or updated, their previous versions remain in collections and indexes as "dead" versions.
The garbage collection process automatically reclaims space from these dead versions for future operations.

Index bloat occurs when a collection's indexes become larger due to the accumulation of dead or obsolete index entries or fragmentation within the pages.
The percentage reported represents the amount of index space that can be used by future index entries.
This bloat consumes space in both the buffer cache and storage.
If you want to remove the bloat, you will need to rebuild indexes.

###### Example

Run the following command to determine unused storage for your index:

```
db.coll.aggregate({$indexStats:{}});
```

The result looks similar to this:

```
{
    "name" : "_id_",
    "key" : {
        "_id" : 1
    },
    "host" : "devbox-test.localhost.a2z.com:27317",
    "size" : NumberLong(827392),
    "accesses" : {
        "ops" : NumberLong(40000),
        "docsRead" : NumberLong(46049),
        "since" : ISODate("2025-04-03T21:44:51.251Z")
    },
    "cacheStats" : {
        "blksRead" : NumberLong(264),
        "blksHit" : NumberLong(140190),
        "hitRatio" : 99.8121
    },
    "unusedStorageSize" : {
        "unusedSizeBytes" : `409600`,
        "unusedSizePercent" : `49.51`
    }
}
```

You can rebuild indexes without downtime using the `reIndex` command, which requires a scan of the entire collection.
See [Index maintenance using reIndex](#reIndex "#reIndex").

### Index maintenance using `reIndex`

`reIndex` is a command used to rebuild an index.
It is typically used when an index has become corrupted or inefficient.
Over time, indexes can accumulate unused space due to many updates, inserts, or deletes, leading to degraded performance.
Reindexing helps to remove such unused space and restore the efficiency of the index.

#### `reIndex` guidelines

- `reIndex` is only supported on Amazon DocumentDB 5.0.
- Amazon DocumentDB supports `reindex` of a single index in the background, allowing for multiple workers.
  The old index is usable by queries when the `reIndex` process is running.
- Amazon DocumentDB supports indexing progress report through `currentOp`.
  You can see index build stages similar to the [Index build stages](#index-build-stages "#index-build-stages") viewed during index creation.
  The only difference is that `reIndex` always has eight stages, regardless if it’s unique or not.
  There’s no “building index: sorting keys 2” stage.
- `reIndex` can run concurrently with any command except index-related commands on the same collection: `createIndexes`, `dropIndexes`, `collMod`, and `renameCollection`.
- `reIndex` is currently not supported for text, geospatial, vector, and partial indexes.

##### `reIndex` build

Use the following command to rebuild your index:

```
db.runCommand({ reIndex: "`collection-name`", index: "`index-name`"})
```

Optionally, you can also control the number of workers assigned to the rebuild process:

```
db.runCommand({ reIndex: "`collection-name`", index: "`index-name`", workers: `number` })
```
