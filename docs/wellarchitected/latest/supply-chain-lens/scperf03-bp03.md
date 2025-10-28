# SCPERF03-BP03 Use cache memory to help improve the performance

Cache memory provides improved latency of the application when
accessed outside of the solution-hosted Regions.

**Desired outcome:** Low latency of
the application when accessed outside of designated Regions.

**Benefits of establishing this best
practice:** Better throughput, low latency, reduced power
consumption, improved reliability, and increased scalability.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

While considering using the cache memory for your supply chain
solutions, you can architect the solution to use caching
services to improve performance. Store frequently used data in
memory or bring the data closer to consumers. Many AWS services
offer features for caching or dedicated services including
Amazon ElastiCache, and Amazon File Cache. For example,
frequently accessed inventory data should be stored in cache
memory, with time-to-live (TTL) settings configured to align
with the data's update frequency and usage patterns. In this
case, data caching solutions (Redis Cache or MemoryDB) are
important to quickly access last available data with low latency
(200 milliseconds or less) interval.

### Implementation steps

1. Identify frequently accessed supply chain data that would
   benefit from caching, such as inventory levels, product
   information, and pricing data.
2. Implement Amazon ElastiCache with Redis or Memcached to
   cache frequently accessed data and reduce database load.
3. Configure appropriate TTL settings for cached data based
   on update frequency and business requirements for data
   freshness.
4. Deploy Amazon CloudFront for caching static content and
   API responses to improve global access performance.
5. Implement cache invalidation strategies to maintain data
   consistency when underlying data changes.
6. Monitor cache performance metrics and optimize cache
   configurations to maximize hit rates and minimize latency.
