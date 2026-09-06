

# Query running slow
<a name="performance-slow-queries"></a>

## Identification - Spot the problem
<a name="identification-spot-problem"></a>

A slow-running query is one that exceeds the execution time expected for your business requirements. The definition of what constitutes a slow query varies across different workloads. You can identify slow queries through profiler logs or Performance Insights.

1. Enable the profiler if not already enabled. Profiler logs are written to Amazon CloudWatch under the Log Group: `/aws/docdb/<cluster-identifier>/profiler`. Use CloudWatch Logs Insights to query them.

   **Example** CloudWatch log analysis query to get the 10 slowest queries for the ecommerce.products collection:

   ```
   filter ns="ecommerce.products" | sort millis desc | limit 10
   ```

1. Use Performance Insights to identify expensive queries in near real-time. Enable Performance Insights if it is not already enabled.

   1. Open the AWS Console, navigate to Amazon Amazon DocumentDB, then Performance Insights, and select your cluster instance.

   1. Review the DB Load (AAS) timeline and Top queries (by DB load). Expand a query digest to view literal child statements.

   1. Capture the queries that require analysis.
**Note**  
Not all queries in Performance Insights may be inefficient or slow queries.

## Investigate — Gather information
<a name="investigate-gather-information"></a>

1. The profiler provides the query execution plan and key metrics associated with it, including millis, nreturned, and planSummary (index usage):

   ```
   {
       "op": "query",
       "ts": 1721374275673,
       "ns": "test.perf",
       "command": {
           "find": "perf",
           "filter": {
               "threadRunCount": 0
           },
           "$db": "test",
           "lsid": {
               "id": {
                   "$binary": "oO2wEtpgQIK+y9KGByYnsw==",
                   "$type": "4"
               }
           },
           "$readPreference": {
               "mode": "secondaryPreferred"
           }
       },
       "cursorExhausted": true,
       "nreturned": 0,
       "responseLength": 0,
       "protocol": "op_query",
       "millis": 137,
       "planSummary": "IXSCAN",
       "execStats": {
           "stage": "FETCH",
           "nReturned": "0",
           "executionTimeMillisEstimate": "100.346",
           "inputStage": {
               "stage": "IXSCAN",
               "nReturned": "0",
               "executionTimeMillisEstimate": "100.342",
               "indexName": "threadRunCount_1"
           }
       },
       "client": "172.31.6.165:43154",
       "appName": "ProdAppTester14",
       "user": "adminuser"
   }
   ```

   To find the COLLSCAN queries:

   ```
   filter planSummary="COLLSCAN" | sort millis desc | limit 20
   ```

1. Use Performance Insights to analyze query execution trends, such as waits, load, and resource impact (e.g., IOPS or CPU per query) in real time.

   As Performance Insights doesn't provide the query execution plan, capture the query and run explain("executionStats") on the query on your Amazon DocumentDB cluster:

   ```
   db.ecommerce.products.find().explain("executionStats")
   ```

1. Optionally, correlate profiler metrics with Performance Insights data (e.g., match high millis queries in profiler with top queries in Performance Insights).

## Diagnose — Find root cause
<a name="diagnose-find-root-cause"></a>

In this step, diagnose the query plan to identify potential optimizations. Use the following flow - symptom → likely cause:
+ **Symptom:** planSummary: "COLLSCAN"

  **Cause:** Missing or incorrect index.
+ **Symptom:** aggregation slow with $group / $sort

  **Cause:** Aggregation pipeline may be processing too much data in memory.
+ **Symptom:** high latencies while Performance Insights shows DB Load grouped by IO waits, though indexes are utilized (planSummary: "IXSCAN").

  **Cause:** I/O bound queries; indexes or working set exceeds available buffer cache on the instance.
+ **Symptom:** PI shows CPU wait states, high AAS due to few queries

  **Cause:** CPU-bound queries (complex aggregations, $regex).
+ **Symptom:** many slow queries but none show expensive planSummary

  **Cause:** external bottleneck (network, throttling, maintenance tasks, volume of queries).

## Resolve — Fix the issue
<a name="resolve-fix-issue"></a>

When you implement fixes, always validate with explain("executionStats") and monitor Performance Insights DB Load.

1. **planSummary: "COLLSCAN"**
   + Create a targeted index.

     **Example:** For frequent queries that filter by { category, price } and sort by price descending:

     ```
     db.products.createIndex({ category: 1, price: -1 })
     ```

1. **aggregation slow with $group / $sort**
   + Push $match and $project early to reduce documents flowing into $group / $sort.
   + Limit the number of fields early in the pipeline:

     ```
     db.products.explain("executionStats").aggregate([
       { $match: { category: "Electronics", price: { $gt: 0 } } },   // early filter
       { $project: { price: 1, category: 1 } },                     // reduce document size
       { $group: { _id: "$category", avgPrice: { $avg: "$price" } } }
     ])
     ```

1. **high latencies while Performance Insights shows DB Load grouped by IO waits**
   + Validate if BufferCacheHitRatio is low or ReadIOPS on the instance are high. Increase instance memory (upgrade instance class, e.g., r6g.large → r6g.xlarge) or use NVMe instance class.
   + Reduce index footprint.
   + Add read replicas to offload read traffic (use readPreference setting to redirect traffic on replicas if query is tolerant with eventual consistency).

1. **PI shows CPU wait states, high AAS due to few queries**
   + Replace expensive $regex with indexed prefix searches or $text index.
   + Batch writes (insert) to reduce write amplification.

**Note**  
Always test your changes in a lower environment (non-production) before promoting those changes to Production.