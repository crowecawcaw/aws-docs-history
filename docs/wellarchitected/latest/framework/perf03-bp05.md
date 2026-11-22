

# PERF03-BP05 Implement data access patterns that utilize caching

 You don't need to fetch frequently accessed data from its primary store on every request. A cache keeps a copy closer to the reader, so repeated reads return faster and the primary store carries less load. Caching helps only when the access pattern suits it. 

 **Desired outcome:** 
+  Your caching strategy matches your workload's access patterns. 
+  You cache data that is read often and changes rarely. 
+  You have a cache invalidation strategy that balances freshness against load on the primary store. 
+  You monitor cache efficiency and treat the cache as recoverable, not durable. 

 **Common anti-patterns:** 
+  Teams cache data that changes frequently. 
+  Teams rely on cached data as if it were durably stored and always available. 
+  Teams ignore the consistency of their cached data. 
+  Teams do not monitor the efficiency of their caching implementation. 
+  Teams key the cache on caller identity when most callers share the same value, which lowers the hit rate. 

 **Benefits of establishing this best practice:** 
+  Read latency and throughput improve for frequently accessed data. 
+  The primary data store carries less load, which frees capacity. 
+  User experience improves because hot data returns quickly. 
+  Costs fall because you scale the primary store less aggressively. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A cache stores data so repeat requests return faster or cost less. If the cache evicts entries or restarts, you rebuild the data by repeating a calculation or fetching from the primary store. Treat the cache as an accelerator. 

 Caching happens at more than one level, and each level trades latency against consistency. *Client-side caching* stores results inside the application or service that makes the query. It gives the lowest latency because the data is local to the reader. A client can keep serving some queries when the primary store is unavailable. The cost appears when many clients cache independently. They duplicate storage and drift out of sync, so one client can return a value that another updated a minute ago. *Remote caching* solves that drift by placing a shared cache between the clients and the primary store. Every client checks the same remote cache, which gives consistent responses and scales storage independently of the clients. The trade is an extra network hop, which raises latency compared with a local hit. Many workloads combine the two caches in a multi-level scheme. They serve hot data from a local cache and fall back to a remote cache before touching the primary store. 

 An invalidation strategy governs how stale a read can be. A time-to-live (TTL) scheme expires entries after a fixed interval, which is simple but can serve stale data. Event-based invalidation removes entries when the source changes, which keeps data fresh but requires the source to signal changes. Version-based schemes attach a version to each entry so readers can detect staleness. The right choice depends on how much staleness the workload tolerates. Plan for cache warming so a cold cache after a restart does not overload the primary store. Decide between write-through and write-behind patterns based on whether writes must be immediately readable. 

 Caching a bad candidate wastes memory and can make performance worse. Data that changes on nearly every read thrashes the cache, producing constant invalidation and low hit rates. The signal to watch is the *cache hit rate*, the share of requests served from cache. A rate below roughly 80 percent usually means the cache is too small or the access pattern does not benefit from caching. Add client resilience such as connection retries, exponential backoff, timeouts, and connection pooling so that a slow or unavailable cache degrades gracefully. AWS supports these patterns with [Amazon ElastiCache](https://aws.amazon.com/elasticache/) and [API caching in Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html). 

 Base cache key granularity on how the data varies, not on who asks for it. A key that includes a caller or account identifier creates one entry per caller, even when most callers resolve to the same value. This lowers the cache hit rate and sends avoidable load to the primary store. Key the shared case on the dimension that determines the value, such as resource type, and handle caller-specific cases on a separate path. Use a shared key only when the value is identical for every caller, so you never serve one caller's data to another. Review your keys as traffic changes. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify what to cache:** Find databases, APIs, and network services with heavy read workloads, a high read-to-write ratio, predictable access patterns, or high cost to scale. These are the candidates where a cache returns the most benefit. See [database caching](https://aws.amazon.com/caching/database-caching/) and [API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html). 

1.  **Choose a caching strategy that fits the access pattern:** Select client-side caching, remote caching, or a multi-level combination based on your latency and consistency needs, using [caching strategies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html) and [AWS caching solutions](https://aws.amazon.com/caching/aws-caching/) as references. Follow [caching best practices](https://aws.amazon.com/caching/best-practices/) for your data store. 

1.  **Configure cache invalidation and warming:** Choose a TTL, event-based, or version-based invalidation scheme that balances data freshness against load on the primary store. Plan cache warming and pre-population, and decide between write-through and write-behind patterns based on whether writes must be immediately readable. 

1.  **Implement client resilience:** Enable connection retries, exponential backoff, client-side timeouts, and connection pooling so that a slow or unavailable cache degrades gracefully. 

1.  **Monitor cache efficiency:** Track the cache hit rate with a goal of 80 percent or higher, and treat lower values as a signal that the cache is undersized or the access pattern does not benefit from caching. For example, use [the ElastiCache metrics reference](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.WhichShouldIMonitor.html). 

1.  **Add replication for read scaling and availability:** Use [data replication](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.Redis.Groups.html) to offload reads across multiple cache instances and improve both read performance and availability. 

1.  **Review cache key granularity:** Compare your cache keys with real traffic. Where most callers resolve to the same value, cache that case on a broader key, and keep caller-specific or access-controlled data on a separate path. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF03-BP04 Implement strategies to improve query performance in data store](perf03-bp04.md) 
+  [PERF03-BP02 Evaluate available configuration options for data store](perf03-bp02.md) 
+  [PERF03-BP01 Use a purpose-built data store that best supports your data access and storage requirements](perf03-bp01.md) 

 **Related documents:** 
+  [Using the Amazon ElastiCache Well-Architected Lens](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WellArchitechtedLens.html) 
+  [Caching challenges and strategies](https://builder.aws.com/content/3K9TeXp6strMiJ4vhakpRD7BQWO/caching-challenges-and-strategies) 
+  [ElastiCache best practices and caching strategies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.html) 

 **Related services:** 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodbaccelerator/) 