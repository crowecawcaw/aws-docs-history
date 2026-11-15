

# ADVCOST04-BP02 Consider multi-level caching for user profile data
<a name="advcost04-bp02"></a>

 A caching layer is a cost-effective way to serve user profile data because it reduces read latency and cuts direct database operations. An in-memory cache holds frequently retrieved items and returns them in microseconds. 

 **Desired outcome:** 
+  DAX or ElastiCache serves the majority of user profile reads during bid evaluation, reducing DynamoDB RCU consumption and associated costs. 
+  Cache hit rate exceeds 90% for active bid-path user profiles. 

 **Common anti-patterns:** 
+  Querying DynamoDB directly for every bid request without a caching layer, which pays full RCU costs for repetitive reads of the same user profiles within short time windows. 
+  Implementing a custom caching solution (self-managed Redis or Memcached) when DAX provides the same benefit with DynamoDB API compatibility and no application-layer cache management logic. 
+  Under-sizing the DAX cluster and experiencing cache evictions that reduce hit rates. 
+  Setting cache TTL too high for profile data that changes frequently, so stale targeting data is served and reduces campaign effectiveness. 
+  Deploying a DAX cluster without monitoring cache hit ratios. 

 **Benefits of establishing this best practice:** 
+  Lower DynamoDB RCU consumption for read-heavy profile lookups, which directly reduces database costs. 
+  Microsecond response times for cached items improve bid evaluation speed and auction win rates. 
+  DAX is API-compatible and requires minimal code changes. 
+  Reduced load on DynamoDB tables decreases the risk of throttling during traffic spikes. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Read amplification is the main cost problem in bid-path profile lookups. A single ad auction triggers profile reads for multiple user segments, and auctions fire millions of times per hour. Without a caching layer, every read consumes DynamoDB Read Capacity Units at full price, even when a different bidder thread fetched the same profile milliseconds earlier. The ratio of unique profiles to total reads (the deduplication ratio) determines how much cost a cache can reduce. Workloads with high temporal locality (the same users appearing in multiple concurrent auctions) benefit most. 

 [DynamoDB Accelerator (DAX)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html) is a write-through, read-through cache that sits in front of DynamoDB with full API compatibility for GetItem, BatchGetItem, and Query operations. This compatibility means the application layer doesn't need custom cache-aside logic, invalidation code, or serialization changes. A self-managed [ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) cluster offers more flexibility (custom eviction policies, multi-table aggregation, computed cache entries) but requires the application to own cache population, invalidation, and failure handling. Choose DAX when the access pattern maps directly to DynamoDB item reads. Choose ElastiCache when the cache needs to serve pre-computed or cross-table results that DAX can't express. 

 Profile data changes when users exhibit new behavior (site visits, purchases, and app installs), and targeting accuracy depends on fresh signals. The optimal TTL depends on profile update frequency, which varies by audience segment. High-value retargeting segments update frequently and need shorter TTLs (seconds to low minutes). Broad demographic segments change slowly and tolerate longer TTLs (minutes to hours). 

 Cluster sizing failures can manifest when you under- or over-provision. The working set size, not total table size, determines the right node count and type. The working set is the number of unique profiles accessed within one TTL window. If this set fits in cluster memory, hit rates stay above 90 percent. If it doesn't, evictions spike and cost savings disappear. 

 DAX nodes in a different Availability Zone from the bidder fleet add cross-AZ data transfer charges and an extra network hop of 1 to 2 milliseconds. This matters in a path where total budget is under 10 milliseconds. Co-locating cache nodes with compute also reduces the impact of an Availability Zone failure. If both cache and compute fail together, traffic shifts to another Availability Zone rather than leaving bidders running without their cache layer. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create a DAX cluster co-located with bidder compute:** Deploy DAX nodes in the same Availability Zones as your bidder fleet. Select node type based on your user profile working set size (use R-series for memory-intensive caching). Configure minimum 3 nodes for Multi-AZ high availability. 

1.  **Migrate bidder application to use the DAX client:** Replace the DynamoDB client initialization in your bidder application with the DAX client, specifying the DAX cluster endpoint. DAX is API-compatible. Only client initialization changes. Test cache behavior with TTL configurations that match your targeting data update frequency. 

1.  **Monitor cache hit rate and RCU reduction:** Track ItemCacheHits compared to ItemCacheMisses in CloudWatch. Compare DynamoDB RCU consumption before and after DAX deployment. Target 90%\+ hit rate for active campaign profiles. Adjust TTL settings if hit rate is below target (indicating TTL is too short relative to access frequency). 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Reduce latency and cost in read-heavy applications using Amazon DynamoDB Accelerator](https://aws.amazon.com/blogs/database/reduce-latency-and-cost-in-read-heavy-applications-using-amazon-dynamodb-accelerator/) 

 **Related services:** 
+  [Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodb/dax/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 