# Troubleshooting indexes

The following topics address what to do if your index or
background index build fails.

###### Topics

- [Index build
  fails](#troubleshooting.index-build-fails "#troubleshooting.index-build-fails")
- [Background index build latency issues and fails](#troubleshooting.background-index-build-fails "#troubleshooting.background-index-build-fails")
- [Database index bloat](#troubleshooting-database-bloat "#troubleshooting-database-bloat")

## Index build

fails

Amazon DocumentDB utilizes local storage on an instance as part of the
index creation process. You can monitor this disk usage using
the **FreeLocalStorage** CloudWatch metric
(`CloudWatch -> Metrics -> DocDB -> Instance Metrics`).
When an index build consumes all of the local disk and fails,
you will receive an error. When migrating data to Amazon DocumentDB, we
encourage you to create indexes first and then insert the data.
For more information on migration strategies and creating
indexes, see [Migrating to Amazon DocumentDB](docdb-migration.md "docdb-migration.md")
in the Amazon DocumentDB documentation and the blog: [Migrate from MongoDB to Amazon DocumentDB using the offline method](https://aws.amazon.com/blogs/database/migrate-from-mongodb-to-amazon-documentdb-using-the-offline-method/ "https://aws.amazon.com/blogs/database/migrate-from-mongodb-to-amazon-documentdb-using-the-offline-method/").

When creating indexes on an existing cluster, if the index
build is taking longer than expected or is failing, we recommend
that you scale up the instance to create the index then, after
the index is created, scale back down. Amazon DocumentDB enables you to
quickly scale instance sizes in minutes using the AWS Management Console or
the AWS CLI. For more information, see [Managing instance classes](db-instance-classes.md "db-instance-classes.md"). With per-second
instance pricing, you only pay for the resource you use up to
the second.

##

Background index build latency issues and fails

Background index builds in Amazon DocumentDB do not start until all queries on the primary instance that started before the index build was initiated complete executing.
If there is a long running query, background index builds will block until the query finishes and thus can take longer than expected to complete.
This is true even if collections are empty.

Foreground index builds do not exhibit the same blocking behavior.
Instead, foreground index builds take an exclusive lock on the collection until the index build is completed.
Thus, to create indexes on empty collection and to avoid blocking on any long running queries, we suggest using foreground index builds.

###### Note

Amazon DocumentDB allows only one background index build to occur on a collection at any given time.
If DDL (Data Definition Language) operations such as `createIndex()` or`dropIndex()` occur on the same collection during a background index build, the background index build fails.

## Database index bloat

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
See [Index maintenance using reIndex](managing-indexes.md#reIndex "managing-indexes.md#reIndex").
