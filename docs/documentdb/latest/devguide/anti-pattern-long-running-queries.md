

# Long running queries
<a name="anti-pattern-long-running-queries"></a>

## Overview
<a name="long-queries-overview"></a>

Long-running queries can cascade into cluster-wide performance issues. These queries can interfere with Amazon DocumentDB's Multi-Version Concurrency Control (MVCC) garbage collection process, leading to accumulation of old versioned documents and degraded performance across the cluster. Amazon DocumentDB implements a 2-hour server-side timeout as a safety mechanism to limit runaway queries from consuming resources indefinitely.

**What are Long running queries:**
+ Queries that execute for extended periods (typically > 30 minutes)
+ Open cursors that remain active for hours (2 hours time-out won't be applicable if the cursor is active)

## Impact on the cluster
<a name="long-queries-impact"></a>

**Long running queries can interfere with Garbage collection Process**
+ **Old Versions Accumulate**: Garbage collector cannot reclaim old document versions
+ **Collection and Index Bloat**: Collection and Index entries accumulate over time, bloat increases and which can result in more storage cost.
+ **CPU and Memory Pressure**: CPU and memory pressure increases due to inefficient processing of increased number old document versions, index entries, and transaction IDs.

Long Running Query → Blocks GC → Storage Growth → CPU and Memory Pressure → More Long Queries

## Monitor and detect
<a name="long-queries-monitoring"></a>

**1. To find long running queries, use the currentOp command.**

```
// To find a query running for more than 30 mins
db.adminCommand({
    aggregate: 1,
    pipeline: [
        {$currentOp: {}},
        {$match: 
            {$or: 
                [{secs_running: {$gt: 1800}},
                 {WaitState: {$exists: true}}]}}],
    cursor: {}
});
```

**2. To find cursors which are active for more than 30 minutes**

```
// To find cursor which is running more than 30 mins
db.adminCommand({
    "currentOp": true,
    "active": true,
    "$all": true
}).inprog.filter(function(op) {
    return op.desc == "Cursor" && 
           op.secs_running > 1800 && 
           op.active == true;
}).sort((a, b) => b.microsecs_running - a.microsecs_running)
```

**3. Monitoring Garbage collector progress through CloudWatch**

`LongestRunningGCProcess`— Duration in seconds of the longest active garbage collection process. Updates every minute and tracks only active operations, excluding processes that complete within the one-minute window.

`AvailableMVCCIds` -A counter that shows the number of remaining write operations available before reaching zero. When this counter reaches zero, your cluster enters read-only mode until IDs are reclaimed and recycled. The counter decreases with each write operation and increases as garbage collection recycles old MVCC IDs.

**Note**  
Lower MVCC IDs and extended garbage collection duration are not exclusively attributed to long-running queries. Write-intensive workloads on resource-constrained instances can also result in reduced MVCC ID availability and prolonged garbage collection cycles.

## Remediation strategies
<a name="long-queries-remediation"></a>
+ Implement query time-outs in the application
+ Do not keep the cursors alive for longer durations
+ Optimize the queries for better performance.
+ Prefer batching of write operations