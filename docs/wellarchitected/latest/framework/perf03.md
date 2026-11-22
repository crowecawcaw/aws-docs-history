

# Data management

 The right data management solution for a workload depends on the shape of the data and how the workload uses it: the data type, whether access is random or sequential, the throughput and latency it demands, how often data is read and updated, and the durability and availability it requires. No single storage technology serves all of these well, so a one-size-fits-all choice forces trade-offs that degrade performance and raise cost. 

 This capability covers how a workload selects and manages data stores for performance: matching each dataset to a purpose-built store, tuning store configuration to the access pattern, measuring store behavior against a baseline, and using query optimization and caching to keep data fast as volume and demand grow. 


|  PERF03: How do you select and manage data stores to meet performance requirements?  | 
| --- | 
|  [PERF03-BP01 Use a purpose-built data store that best supports your data access and storage requirements](perf03-bp01.md)  | 
|  [PERF03-BP02 Evaluate available configuration options for data store](perf03-bp02.md)  | 
|  [PERF03-BP03 Collect and record data store performance metrics](perf03-bp03.md)  | 
|  [PERF03-BP04 Implement strategies to improve query performance in data store](perf03-bp04.md)  | 
|  [PERF03-BP05 Implement data access patterns that utilize caching](perf03-bp05.md)  | 

## Capability intent
<a name="perf03-intent"></a>
+  Each dataset runs on a store matched to its structure, access pattern, and durability needs, rather than forced onto a single default engine. 
+  Store configuration is tuned to the workload's read, write, and consistency requirements, and validated against representative load before it carries production traffic. 
+  Data store behavior is measured continuously against a known baseline that covers both system resources and store-level access patterns. 
+  Data layout, indexing, and query structure keep the store efficient as data grows, guided by execution plans and regular maintenance. 
+  Frequently read data is served from a cache closer to the reader, with an invalidation strategy that balances freshness against load on the primary store. 
+  Data store decisions are recorded, owned, and revisited as access patterns and data volumes change. 

## Common issues to watch for
<a name="perf03-issues"></a>
+  A single database engine serves every dataset, so workloads that need a different store pay in latency, throughput, and cost for capabilities they cannot use. 
+  Data stores run on default settings, so read offloading, write scaling, tiering, and connection handling stay unconfigured until load exposes the gap. 
+  No performance baseline exists, so teams cannot tell whether current latency is normal or degraded, and problems are diagnosed only after users report them. 
+  Metrics cover host resources but not store-level access patterns, so lock contention, slow queries, and hot partitions stay hidden behind healthy-looking CPU. 
+  Queries run against unpartitioned data, missing indexes, or stale statistics, so full scans and poor execution plans create bottlenecks that grow with data volume. 
+  Caches hold frequently changing data or are treated as durable storage, so hit rates stay low and an eviction or restart overloads the primary store. 