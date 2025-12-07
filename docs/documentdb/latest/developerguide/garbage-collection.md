# Garbage collection in Amazon DocumentDB

Amazon DocumentDB implements a multi-version concurrency control (MVCC) database architecture that creates new versions of document and index entries for every update operation.
This architecture provides enables transaction isolation, preventing one transaction's changes from appearing in another.

###### Topics

- [Understanding Garbage collection in Amazon DocumentDB](#understanding-garbage-collection "#understanding-garbage-collection")
- [Garbage collection process](#garbage-collection-process "#garbage-collection-process")
- [Storage architecture and extended storage](#storage-architecture "#storage-architecture")
- [Monitoring garbage collection](#monitoring-garbage-collection "#monitoring-garbage-collection")
- [Example collStats output](#example-collstats-output "#example-collstats-output")
- [Frequently asked questions](#garbage-collection-faq "#garbage-collection-faq")

## Understanding Garbage collection in Amazon DocumentDB

Garbage collection (GC) is an automated background process that maintains optimal system performance and availability in Amazon DocumentDB.
Like many modern databases, Amazon DocumentDB's MVCC architecture creates new document and index versions with each update. Each write operation consumes a unique MVCC ID from a finite counter.
These IDs identify which transaction a document version belongs to and whether it has been committed or rolled back.
Over time, these old versions and their MVCC IDs accumulate, requiring cleanup to prevent performance degradation.

### Functions of garbage collection

Garbage collector serves three essential functions:

- **Reclaims storage space** — It removes obsolete document and index versions that are no longer needed by active queries, freeing space for future write operations.
- **Prevents MVCC ID overflow** — It prevents MVCC ID overflow by managing the finite counter of MVCC IDs.
  Without this management, the counter would eventually reach its limit, forcing the database into a temporary read-only mode until IDs are recycled.
- **Maintains query performance** — It maintains optimal query performance by eliminating dead document versions that would otherwise accumulate and slow down query processing.

## Garbage collection process

The GC process operates per collection and can have multiple processes running concurrently on different collections.
The process consists of four sequential phases:

1. **Identification** — The system identifies document and index versions no longer referenced by active transactions or queries.
2. **Memory loading** — Old documents and index entries are loaded into memory if not already present.
3. **Deletion** — Obsolete versions are permanently deleted to reclaim storage space.
4. **MVCC ID recycling** — The system recycles MVCC IDs from deleted versions for new operations.

When garbage collection completes processing old document versions, it removes the oldest MVCC IDs from the system.
This cleanup is crucial for preventing MVCC ID overflow by recycling MVCC IDs, making them available for new write operations across the cluster.
Without this recycling process, the system would eventually exhaust its finite MVCC ID counter and enter a read-only state.

### Garbage collection scheduling

Garbage collection runs automatically in the background at periodic intervals.
The timing and frequency adjust dynamically based on system load, available resources, write volume, and MVCC ID consumption levels.
During high write activity, the GC process executes more frequently to manage the increased number of document versions.

## Storage architecture and extended storage

Amazon DocumentDB uses a sophisticated storage architecture that separates document storage into two distinct segments:

### Base storage segment

The base storage segment contains the primary document data and metadata. This segment stores:

- Document content that fits within the standard page size (8 KB).
- Document metadata and structure information.
- Primary indexes and their entries.
- Collection-level statistics and configuration.

### Extended storage segment

The extended storage segment utilizes a specialized large document object store designed to handle documents that exceed the standard storage page size. This segment provides:

- **Efficient Large Document Handling** — Documents larger than the base storage threshold are automatically moved to the extended storage segment.
- **Optimized Storage Layout** — The segment uses a different storage format optimized for large objects, reducing fragmentation and improving access patterns.
- **Independent Garbage Collection** — The extended storage segment has its own garbage collection process that can run independently of base storage cleanup.
- **Transparent Access** — Applications access large documents seamlessly without needing to know which storage segment contains the data.

The extended storage segment is particularly beneficial for:

- Collections with documents containing large embedded arrays.
- Documents with extensive nested structures.
- Collections storing binary data or large text fields.
- Applications with mixed document sizes where some documents significantly exceed average size.

## Monitoring garbage collection

### Cluster level metrics

**`AvailableMVCCIds`**

- **Location** — Amazon CloudWatch
- **Description** — A counter that shows the number of remaining write operations available from a maximum limit of 1.8 billion.
  When this counter reaches zero, your cluster enters read-only mode until IDs are reclaimed and recycled.
  The counter decreases with each write operation and increases as garbage collection recycles old MVCC IDs.
- **Recommendation** — Set an alarm when the value falls below 1.3 billion.
  This early warning allows you to take recommended steps discussed later.

**`LongestRunningGCRuntime`**

- **Location** — Amazon CloudWatch
- **Description** — Duration in seconds of the longest active garbage collection process.
  Updates every minute and tracks only active operations, excluding processes that complete within the one-minute window.
- **Recommendation** — Compare with `GCRuntimeStats` historical data to identify abnormal garbage collection behavior, such as extended runtimes during bulk deletions.

### Collection level metrics

**`MVCCIDStats: MvccIdAgeScale`**

- **Location** — Database collStats command
- **Description** — Measures MVCC ID age on a scale of 0 to 1, where 1 indicates the maximum age before a cluster enters a read-only state.
  Use this metric alongside `AvailableMVCCIds` to identify collections containing the oldest MVCC IDs that are aging the cluster.
- **Recommendation** — Maintain values below 0.3 for each collection.

**`GCRuntimeStats`**

- **Location** — Database collStats command
- **Description** — Provides a two-month history of garbage collection metrics, including total runs, average duration, and maximum duration.
  Only includes garbage collection operations lasting more than five minutes to ensure meaningful statistics.

**`StorageSizeStats`**

- **Location** — Database collStats command
- **Description** — Provides detailed breakdown of storage utilization across different storage segments:
  - `storageSegmentBase` — Storage used by the base storage segment for standard documents
  - `storageSegmentExtended` — Storage used by the extended storage segment for large documents

- **Usage** — Helps identify collections with significant large document storage and understand storage distribution patterns.

**`UnusedStorageSize`** (collection level)

- **Location** — Database collStats command
- **Description** — Estimates unused storage space in a collection based on sampled statistics.
  It includes space from deleted documents and empty segments. The metric provides both combined totals and per-segment breakdowns:
  - Combined `unusedBytes` and `unusedPercent` across all storage segments
  - `storageSegmentBase` — Unused space specifically in the base storage segment
  - `storageSegmentExtended` — Unused space specifically in the extended storage segment

**`DocumentFragmentStats`**

- **Location** — Database collStats command
- **Description** — Provides detailed information about document fragments and dead data within collections.
  Document fragments represent the internal storage units used by the database engine, and dead fragments indicate data that is no longer accessible but hasn't been reclaimed yet. This metric includes:
  - `totalDocFragmentsCount` — Total number of document fragments in the collection
  - `deadDocFragmentsCount` — Number of fragments containing dead (inaccessible) data
  - `deadDocFragmentsPercent` — Percentage of fragments that contain dead data
  - `deadDocFragmentBytes` — Estimated bytes consumed by dead document fragments
  - Per-segment breakdown for `storageSegmentBase` and `storageSegmentExtended`

- **Usage** — Monitor this metric to understand the effectiveness of garbage collection and identify collections that may benefit from maintenance operations.
  High percentages of dead fragments indicate that garbage collection may be falling behind or that the collection would benefit from optimization.

### Index level metrics

**`UnusedStorageSize`** (index level)

- **Location** — Database indexStats command
- **Description** — Estimates unused storage space in an index based on sampled statistics.
  It includes space from obsolete index entries and empty segments.
- **Recommendation** — Use the `REINDEX` command to rebuild indexes without downtime and reclaim unused space.
  Refer to Managing Indexes for more details.

## Example collStats output

The following example shows a typical `collStats` output with garbage collection and storage metrics:

```
{
    "ns" : "xid_consumption_test_db.xid_test_collection",
    "MVCCIdStats" : {
        "MVCCIdScale" : 0.03
    },
    "gcRuntimeStats" : {
        "numRuns" : 1,
        "historicalAvgRuntime" : 3295,
        "historicalMaxRuntime" : 3295,
        "lastRuntime" : 3295,
        "lastRuntimeStart" : ISODate("2025-06-24T08:47:14Z")
    },
    "documentFragmentStats" : {
        "totalDocFragmentsCount" : 45000000,
        "deadDocFragmentsCount" : 2250000,
        "deadDocFragmentsPercent" : 5.0,
        "deadDocFragmentBytes" : 98304000,
        "storageSegmentBase" : {
            "totalDocFragmentsCount" : 30000000,
            "deadDocFragmentsCount" : 1500000,
            "deadDocFragmentsPercent" : 5.0,
            "deadDocFragmentBytes" : 65536000
        },
        "storageSegmentExtended" : {
            "totalDocFragmentsCount" : 15000000,
            "deadDocFragmentsCount" : 750000,
            "deadDocFragmentsPercent" : 5.0,
            "deadDocFragmentBytes" : 32768000
        }
    },
    "collScans" : 14,
    "count" : 30000000,
    "size" : 1320000000,
    "avgObjSize" : 44,
    "storageSize" : 6461497344,
    "storageSizeStats" : {
        "storageSegmentBase" : 4307664896,
        "storageSegmentExtended" : 2153832448
    },
    "capped" : false,
    "nindexes" : 2,
    "totalIndexSize" : 9649553408,
    "indexSizes" : {
        "_id_" : 1910661120,
        "c_1" : 7738892288
    },
    "unusedStorageSize" : {
        "unusedBytes" : 4201881600,
        "unusedPercent" : 65.05,
        "storageSegmentBase" : {
            "unusedBytes" : 2801254400,
            "unusedPercent" : 65.05
        },
        "storageSegmentExtended" : {
            "unusedBytes" : 1400627200,
            "unusedPercent" : 65.05
        }
    },
    "cacheStats" : {
        "collBlksHit" : 171659016,
        "collBlksRead" : 754061,
        "collHitRatio" : 99.5627,
        "idxBlksHit" : 692563636,
        "idxBlksRead" : 1177921,
        "idxHitRatio" : 99.8303
    },
    "idxScans" : 41823984,
    "opCounter" : {
        "numDocsIns" : 0,
        "numDocsUpd" : 20911992,
        "numDocsDel" : 0
    },
    "lastReset" : "2025-06-24 05:57:08.219711+00",
    "ok" : 1,
    "operationTime" : Timestamp(1750968826, 1)
}
```

## Frequently asked questions

### How do I identify if garbage collection is not working efficiently?

Monitor these warning signs that indicate inefficient garbage collection:

- **Excessive Collection Bloat** — Steadily increasing `UnusedStorageSize` metrics during heavy writes or bulk deletions, especially with large indexes.
- **High Dead Fragment Percentage** — `DocumentFragmentStats` showing consistently high `deadDocFragmentsPercent` values (above 10-15%).
- **Degraded Query Latency** — Increased query latency due to accumulated dead documents.
- **Extended GC Duration** — Garbage collection operations taking longer than historical averages in `GCRuntimeStats`.
- **Elevated GC Processing** — High `LongestRunningGCRuntime` indicating the garbage collector cannot keep up with system demands.

### Does garbage collection affect my database performance?

Under normal conditions, garbage collection has minimal performance impact. However, when garbage collection falls behind, you may experience:

- Increased storage costs from accumulated dead documents.
- Slower query performance due to obsolete index entries.
- Temporary read-only mode if MVCC IDs are depleted.
- Higher resource usage during intensive collection runs, especially on smaller instances.
- Reduced efficiency in extended storage segment operations for large documents.

### Can I manually trigger garbage collection?

No, garbage collection in Amazon DocumentDB cannot be manually triggered. The system manages garbage collection automatically as part of its internal maintenance operations.

### What alarms should I set as an operational best practice?

We recommend setting up monitoring at both the cluster and collection levels to ensure optimal performance of your Amazon DocumentDB system.

For cluster-level monitoring, start by creating a Amazon CloudWatch alarm for the `AvailableMVCCIds` metric with a threshold of 1.3 billion.
This gives you adequate time to take action before the metric reaches zero, at which point your cluster would enter read-only mode.
Keep in mind that this metric may fluctuate based on your specific usage patterns - some customers see it drop below 1.3 billion and then recover above 1.5 billion as garbage collection completes its work.

It's also important to monitor the `LongestRunningGCRuntime` metric through Amazon CloudWatch.
This metric, along with `GCRuntimeStats`, helps you understand how efficiently garbage collection is performing across your system.

For collection-level monitoring, focus on these key metrics:

- `MvccIdAgeScale` — Watch for increasing values that suggest MVCC IDs are aging and may need attention.
- `GCRuntimeStats` — Identify garbage collection processes taking unusually long or extending over multiple days.
- `DocumentFragmentStats` — Monitor `deadDocFragmentsPercent` values - consistently high percentages (above 10-15%) may indicate garbage collection is falling behind.
- `StorageSizeStats` and `UnusedStorageSize` — Track storage utilization patterns and identify collections with significant unused space in either storage segment.

Collections with frequent write operations need extra attention, as they generate more work for the garbage collector.
We recommend checking these metrics more frequently for collections with heavy write activity to ensure garbage collection keeps up with your workload.

Note that these monitoring recommendations serve as a starting point.
As you become more familiar with your system's behavior, you may want to adjust these thresholds to better match your specific usage patterns and requirements.

### What should I do if my `AvailableMVCCIds` falls below 1.3 billion?

If your `AvailableMVCCIds` metric drops below 1.3 billion, we recommend taking immediate action to prevent your cluster from entering read-only mode.
We recommend first scaling up your instance size to provide the garbage collector with more computing resources.
This is our primary recommendation as it allows your application to continue normal operations while giving the garbage collector the additional power it needs to catch up.

If scaling up alone doesn't improve the situation, we recommend considering a reduction in your write operations.
Use the `MvccIdAgeScale` metric to identify which specific collections contain older MVCC IDs that need attention.
Additionally, monitor `DocumentFragmentStats` to identify collections with high dead fragment percentages that may be contributing to garbage collection inefficiency.

Once you've identified these collections, you may need to temporarily reduce write operations to them to allow garbage collection to catch up.
During the recovery period, we recommend closely monitoring the `AvailableMVCCIds` metric to ensure your actions are having the desired effect.
Your cluster is considered healthy once the `AvailableMVCCIds` value returns to 1.5 billion or higher.

Remember that these steps are preventive measures to help your system recover before it reaches a critical state.
The sooner you take action after seeing the metric drop below 1.3 billion, the more likely you are to avoid any impact to your write operations.
