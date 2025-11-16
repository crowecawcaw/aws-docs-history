# Garbage collection in Amazon DocumentDB

Amazon DocumentDB implements a multi-version concurrency control (MVCC) database architecture that creates new versions of document and index entries for every update operation.
This architecture provides read isolation by allowing read queries to use versioned documents without taking locks.

###### Topics

- [Understanding Garbage Collection in Amazon DocumentDB](#understanding-garbage-collection "#understanding-garbage-collection")
- [Garbage collection process](#garbage-collection-process "#garbage-collection-process")
- [Monitoring garbage collection](#monitoring-garbage-collection "#monitoring-garbage-collection")
- [Example collStats output](#collStats-output "#collStats-output")
- [Frequently asked questions](#w5aac49c15c15 "#w5aac49c15c15")

## Understanding Garbage Collection in Amazon DocumentDB

Garbage collection (GC) is an automated background process that maintains optimal system performance and availability in Amazon DocumentDB.
Unlike traditional databases that overwrite data in place, Amazon DocumentDB’s MVCC architecture creates new versions of documents and index entries with each update operation.
Every write operation that results in a new document version consumes a unique MVCC ID from a finite counter, making efficient cleanup essential.
Over time, these old versions accumulate and must be cleaned up to prevent performance degradation.

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

## Monitoring garbage collection

### Cluster level metrics

**`AvailableMVCCIds`**

- **Location** — Amazon CloudWatch
- **Description** — A counter that shows the number of remaining write operations available before reaching zero.
  When this counter reaches zero, your cluster enters read-only mode until IDs are reclaimed and recycled.
  The counter decreases with each write operation and increases as garbage collection recycles old MVCC IDs.
- **Recommendation** — Set an alarm when the value falls below 1.3 billion.
  This early warning allows you to take recommended steps discussed later.

**`LongestActiveGCRuntime`**

- **Location** — Amazon CloudWatch
- **Description** — Duration in seconds of the longest active garbage collection process.
  Updates every minute and tracks only active operations, excluding processes that complete within the one-minute window.
- **Recommendation** —

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

**`UnusedStorageSize`** (collection level)

- **Location** — Database collStats command
- **Description** — Estimates unused storage space in a collection based on sampled statistics.
  It includes space from deleted documents and empty segments.

### Index level metrics

**`UnusedStorageSize`** (index level)

- **Location** — Database indexStats command
- **Description** — Estimates unused storage space in an index based on sampled statistics.
  It includes space from obsolete index entries and empty segments.
- **Recommendation** — Use the `reIndex` command to rebuild indexes without downtime and reclaim unused space.
  Refer to Managing Indexes for more details.

## Example `collStats` output

```
{
    "ns": "xid_consumption_test_db.xid_test_collection",
    "MVCCIdStats": {
        "MVCCIdScale": 0.03
    },
    "gcRuntimeStats": {
        "numRuns": 1,
        "historicalAvgRuntime": 3295,
        "historicalMaxRuntime": 3295,
        "lastRuntime": 3295,
        "lastRuntimeStart": ISODate("2025-06-24T08:47:14Z")
    },
    "collScans": 14,
    "count": 30000000,
    "size": 1320000000,
    "avgObjSize": 44,
    "storageSize": 6461497344,
    "capped": false,
    "nindexes": 2,
    "totalIndexSize": 9649553408,
    "indexSizes": {
        "_id_": 1910661120,
        "c_1": 7738892288
    },
    "unusedStorageSize": {
        "unusedBytes": 4201881600,
        "unusedPercent": 65.05
    },
    "cacheStats": {
        "collBlksHit": 171659016,
        "collBlksRead": 754061,
        "collHitRatio": 99.5627,
        "idxBlksHit": 692563636,
        "idxBlksRead": 1177921,
        "idxHitRatio": 99.8303
    },
    "idxScans": 41823984,
    "opCounter": {
        "numDocsIns": 0,
        "numDocsUpd": 20911992,
        "numDocsDel": 0
    },
    "lastReset": "2025-06-24 05:57:08.219711+00",
    "ok": 1,
    "operationTime": Timestamp(1750968826, 1)
}
```

## Frequently asked questions

###### Topics

- [How do I identify if garbage collection is not working efficiently?](#w5aac49c15c15b5 "#w5aac49c15c15b5")
- [Does garbage collection affect my database performance?](#w5aac49c15c15b7 "#w5aac49c15c15b7")
- [Can I manually trigger garbage collection?](#w5aac49c15c15b9 "#w5aac49c15c15b9")
- [What alarms should I set as an operational best practice?](#w5aac49c15c15c11 "#w5aac49c15c15c11")
- [What should I do if my AvailableMVCCId falls below 1.3 billion?](#w5aac49c15c15c13 "#w5aac49c15c15c13")

### How do I identify if garbage collection is not working efficiently?

Monitor these warning signs that indicate inefficient garbage collection:

- **Excessive collection bloat** — Steadily increasing `UnusedStorageSize` metrics during heavy writes or bulk deletions, especially with large indexes
- **Degraded query latency** — Increased query latency due to accumulated dead documents
- **Extended GC duration** — Garbage collection operations taking longer than historical averages in `GCRuntimeStats`
- **Elevated GC processing** — High `LongestActiveGCRuntime` indicating the garbage collector cannot keep up with system demands

### Does garbage collection affect my database performance?

Under normal conditions, garbage collection has minimal performance impact.
However, when garbage collection falls behind, you may experience:

- increased storage costs from accumulated dead documents.
- slower query performance due to obsolete index entries.
- temporary read-only mode if MVCC IDs are depleted.
- higher resource usage during intensive collection runs, especially on smaller instances.

### Can I manually trigger garbage collection?

No, garbage collection in Amazon DocumentDB cannot be manually triggered.
The system manages garbage collection automatically as part of its internal maintenance operations.

### What alarms should I set as an operational best practice?

We recommend setting up monitoring at both the cluster and collection levels to ensure optimal performance of your Amazon DocumentDB system.

**For cluster-level monitoring**

Start by creating a CloudWatch alarm for the `AvailableMVCCId` metric with a threshold of 1.3 billion.
This gives you adequate time to take action before the metric reaches zero, at which point your cluster would enter read-only mode.
Keep in mind that this metric may fluctuate based on your specific usage patterns.
Some customers see it drop below 1.3 billion and then recover above 1.5 billion as garbage collection completes its work.

It's also important to monitor the `LongestActiveGCRuntime` metric through CloudWatch.
This metric, along with `GCRuntimeStats`, helps you understand how efficiently garbage collection is performing across your system.

**For collection-level monitoring**

Focus on two key metrics.
First, we recommend watching the `MvccIdAgeScale` value for each collection.
Increasing values suggest that MVCC IDs are aging and may need attention.
Second, monitor `GCRuntimeStats` to identify any garbage collection processes that are taking unusually long or extending over multiple days.
Collections with frequent write operations need extra attention, as they generate more work for the garbage collector.
We recommend checking these metrics more frequently for collections with heavy write activity to ensure garbage collection keeps up with your workload.

Note that these monitoring recommendations serve as a starting point.
As you become more familiar with your system's behavior, you may want to adjust these thresholds to better match your specific usage patterns and requirements.

### What should I do if my `AvailableMVCCId` falls below 1.3 billion?

If your `AvailableMVCCId` metric drops below 1.3 billion, we recommend taking immediate action to prevent your cluster from entering read-only mode.
We recommend first scaling up your instance size to provide the garbage collector with more computing resources.
This allows your application to continue normal operations while giving the garbage collector the additional power it needs to catch up.

If scaling up alone doesn't improve the situation, we recommend considering a reduction in your write operations.
Use the `MvccIdAgeScale` metric to identify which specific collections contain older MVCC IDs that need attention.
Once you've identified these collections, you may need to temporarily reduce write operations to them to allow garbage collection to catch up.
During the recovery period, we recommend closely monitoring the `AvailableMVCCId` metric to ensure your actions are having the desired effect.
Your cluster is considered healthy once the `AvailableMVCCId` value returns to 1.5 billion or higher.

Remember that these steps are preventive measures to help your system recover before it reaches a critical state.
The sooner you take action after seeing the metric drop below 1.3 billion, the more likely you are to avoid any impact to your write operations.
