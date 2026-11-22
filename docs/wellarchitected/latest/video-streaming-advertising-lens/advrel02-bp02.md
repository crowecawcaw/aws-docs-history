

# ADVREL02-BP02 Implement a caching strategy

 A caching strategy improves system reliability and performance. Evaluate different caching levels (from client-side to server-side) and explore various caching solutions including ElastiCache, third-party databases, and CDNs for optimizing ad payload delivery and reducing backend load. 

 **Desired outcome:** 
+  Frequently accessed advertising data (user profiles, frequency caps, audience segments, and creative metadata) is served from cache, reducing bid path latency and database load. 
+  Cache warm-up strategies help avoid cold-start latency spikes during traffic bursts. 
+  CDN caching for ad creative payloads reduces origin load and improves viewer experience globally. 

 **Common anti-patterns:** 
+  No caching layer: every bid request triggers a database lookup for user profile data, creating a bottleneck at the database tier during traffic spikes. 
+  Setting TTLs that are too long for frequently updated data (frequency caps), which allows stale data to affect campaign delivery accuracy. 
+  Not pre-warming caches before known high-traffic events, so cache-miss storms hit at event start. 

 **Benefits of establishing this best practice:** 
+  Reduced database load enables higher bid throughput without proportionally scaling database infrastructure. 
+  Lower bid path latency improves auction response times and bid win rates. 
+  CDN caching improves ad creative load times for viewers regardless of geographic location. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Caching can be applied at in client-side caching of user profiles, server-side caching for bid enhancement, and CDN caching for ad creative payloads. For server-side caching, use Amazon ElastiCache (Redis OSS) or Memcached. Third-party databases such as Aerospike, Cassandra, and ScyllaDB serve user profile data that requires sub-millisecond access with high consistency. 

 Cache ad creative payloads on a CDN such as Amazon CloudFront to reduce origin load and lower delivery latency for viewers. For SGAI and SSAI workflows, pre-populate CDN caches with pre-transcoded creatives before ad breaks begin to protect fill rates and viewer experience. 

 For frequency capping data that must stay consistent across multiple auction servers, use ElastiCache with a short TTL (30 seconds to 2 minutes) to balance consistency with performance. Stricter consistency requirements, such as preventing over-delivery within a single session, might require a durable store with synchronous replication. 

 Amazon API Gateway provides a built-in caching layer for API responses. For targeting data that changes infrequently, such as audience segment definitions and campaign flight dates, API Gateway caching reduces calls to backend segment management services. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify cacheable data categories and appropriate TTLs:** Audit bid-path data access patterns and classify data by: update frequency (user profile behavior: 5-minute TTL, audience segment definitions: 15-minute TTL, creative metadata: 1-hour TTL, campaign flight rules: 5-minute TTL) and consistency requirement (frequency caps: 30-second TTL, targeting segments: 5-minute TTL). Document cache keys, eviction policies, and fallback behavior for cache misses. 

1.  **Deploy ElastiCache Redis clusters colocated with bidder compute:** Deploy Redis clusters in the same Availability Zones as your bidding compute, using cluster mode enabled for horizontal scaling. Configure read replicas in each Availability Zone for read-heavy workloads. Set maxmemory-policy to allkeys-lru for ad targeting data where evicting less-recently-used entries is acceptable. Monitor cache hit rate per data category through CloudWatch: target 95%\+ for user profile lookups. 

1.  **Implement cache pre-warming for known traffic events:** Before high-traffic advertising events (live events, campaign launches), pre-populate caches with the targeting data and user profiles likely to be accessed. Use a Lambda function that queries your profile store for the most active user segments and writes them to ElastiCache 10 minutes before the event starts. This helps avoid cold-start database storms at event initialization. 

1.  **Configure CDN caching for ad creative payloads:** Deploy CloudFront distributions for ad creative assets with TTLs aligned to campaign flight dates (use Cache-Control: max-age headers set to the campaign end date). Enable CloudFront Origin Shield to consolidate origin requests. For SSAI and SGAI workflows, configure pre-transcoded creative warm-up by issuing cache-priming requests through Lambda to prime edge caches before ad breaks begin in the programming schedule. 

1.  **Monitor cache effectiveness and tune TTLs:** Create CloudWatch dashboards showing cache hit rates, eviction rates, and connection count per ElastiCache cluster. Configure alarms on cache hit rate dropping below 90% (indicates TTL is too short or cache size is insufficient). Monthly, review TTL settings against data update frequency to optimize the trade-off between staleness and database load. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP04 Design your workloads to withstand failures of individual components](advrel04-bp04.md) 
+  [ADVREL03-BP03 Deploy stateful dependencies across multiple Availability Zones](advrel03-bp03.md) 

 **Related documents:** 
+  [Amazon ElastiCache Memcached](https://aws.amazon.com/elasticache/memcached/) 
+  [Caching for high-volume workloads with Amazon ElastiCache](https://aws.amazon.com/tutorials/purpose-built-databases/elasticache/) 

 **Related services:** 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 