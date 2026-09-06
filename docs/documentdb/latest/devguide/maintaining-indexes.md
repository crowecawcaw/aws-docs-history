

# Maintaining indexes
<a name="maintaining-indexes"></a>

## Index bloat
<a name="maintaining-indexes-bloat"></a>

Amazon DocumentDB uses Multi-Version Concurrency Control (MVCC) to manage concurrent transactions. When documents are deleted or updated, their previous versions remain in collections and indexes as "dead" versions. The garbage collection process automatically reclaims space from these dead versions for future operations.

Index bloat occurs when a collection's indexes become larger due to the accumulation of dead or obsolete index entries or fragmentation within the pages. The percentage reported represents the amount of index space that can be used by future index entries. This bloat consumes space in both the buffer cache and storage. If you want to remove the bloat, you will need to rebuild indexes.

**Example:** Run the following command to determine unused storage for your index:

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
        "unusedSizeBytes" : 409600,
        "unusedSizePercent" : 49.51
    }
}
```

You can rebuild indexes without downtime using the reIndex command, which requires a scan of the entire collection. See Index maintenance using reIndex.

## Index maintenance using reIndex
<a name="maintaining-indexes-reindex"></a>

reIndex is a command used to rebuild an index. It is typically used when an index has become corrupted or inefficient. Over time, indexes can accumulate unused space due to many updates, inserts, or deletes, leading to degraded performance. Reindexing helps to remove such unused space and restore the efficiency of the index.

**reIndex guidelines**
+ reIndex is only supported on Amazon DocumentDB 5.0 and above
+ reIndex always runs in the background.
+ Amazon DocumentDB supports reindex of a single index in the background, allowing for multiple workers. The old index is usable by queries when the reIndex process is running.
+ Amazon DocumentDB supports indexing progress report through currentOp. You can see index build stages similar to the Index build stages viewed during index creation. The only difference is that reIndex always has eight stages, regardless if it's unique or not. There's no "building index: sorting keys 2" stage.
+ reIndex can run concurrently with any command except index-related commands on the same collection: createIndexes, dropIndexes, collMod, and renameCollection.
+ reIndex is currently not supported for text, geospatial, vector, and partial indexes.

**reIndex build**

Use the following command to rebuild your index:

```
db.runCommand({ reIndex: "collection-name", index: "index-name"})
```

Optionally, you can also control the number of workers assigned to the rebuild process:

```
db.runCommand({ reIndex: "collection-name", index: "index-name", workers: number })
```

For information specific to managing indexes with Java, see [Index management in Amazon DocumentDB with Java](index-management-java.md).