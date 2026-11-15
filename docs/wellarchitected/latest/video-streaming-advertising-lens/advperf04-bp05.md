

# ADVPERF04-BP05 Manage high-volume user profile data
<a name="advperf04-bp05"></a>

 User profile databases are typically large (100 million to 5 billion profiles) and require managing retention, geographic placement, and caching to control storage costs and maintain sub-millisecond bid path performance. 

 **Desired outcome:** 
+  Your user profile store delivers consistent sub-millisecond to single-digit-millisecond read performance at scale. 
+  Retention policies bound storage costs and keep query latency within SLOs as the system scales. 
+  Profile data is stored close to users geographically, and cross-region synchronization is scheduled rather than real-time to minimize transfer costs. 

 **Common anti-patterns:** 
+  Retaining user profile data indefinitely without a defined retention policy, which allows the dataset grow unconstrained until storage costs and query latency degrade. 
+  Replicating user profile data across multiple regions in real time, when a given user is almost never accessed from more than one Region simultaneously. 

 **Benefits of establishing this best practice:** 
+  Bounded retention and local storage of user profiles keeps your database at a manageable size (preserving query latency SLOs as the system scales) while avoiding unnecessary replication costs. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 User profile data has a staleness curve, where behavioral signals older than 30–90 days add less targeting value but still consume storage and inflate query scan times. Use a retention window of 30 days for high-velocity bid path profiles and up to one year for full audience profiles. 

 [Amazon MemoryDB](https://aws.amazon.com/memorydb/) provides durable, in-memory storage with Redis-compatible APIs. Use a cache-aside pattern (check MemoryDB before querying DynamoDB, and populate MemoryDB from DynamoDB on cache misses) to keep the most frequently accessed profiles in memory while DynamoDB stores the full dataset. 

 Advertisers use geotargeting, so where you store profile data affects bid path latency. A user's profile is accessed from the region they are located in for a given ad campaign. Store profiles in the AWS Region closest to where users are located to avoid cross-Region network latency that would add tens of milliseconds to every profile lookup on the bid path. 

 For architectures that require profile data in more than one Region (global campaigns), synchronize profiles on a schedule (once or twice per day). Real-time cross-region replication adds significant data transfer costs with minimal correctness benefit because users are rarely in two geographic locations simultaneously. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure DynamoDB TTL for profile data retention:** Set a TTL attribute on DynamoDB user profile items and configure DynamoDB's TTL feature to automatically expire items after your defined retention window (30–90 days from last update for bid path profiles). TTL deletions don't consume write capacity and incur no charge. Monitor the TimeToLiveDeletedItemCount CloudWatch metric to confirm TTL is deleting expired items at the expected rate. 

1.  **Deploy Amazon MemoryDB as your in-memory user profile cache:** Deploy MemoryDB in the same Availability Zone as your bidder compute. Implement a cache-aside pattern where bid evaluation services check MemoryDB first, populate on miss from DynamoDB, and update MemoryDB on profile writes. Configure MemoryDB eviction policy to evict least-recently-used items as the working set grows, keeping the most frequently accessed profiles in memory. 

1.  **Store user profiles in the Region closest to the user:** Partition your profile storage by user geography (EU users in EU regions, US users in US regions, APAC users in APAC regions). Configure your bidding infrastructure to route profile lookups to the regional store. Avoid the anti-pattern of centralizing all user profiles in a single Region and serving lookups globally over cross-region connections. 

1.  **Implement periodic cross-region synchronization:** For architectures that require profile data in multiple regions for global campaign targeting, implement a scheduled synchronization job ([AWS Step Functions](https://aws.amazon.com/step-functions/) \+ Lambda) that runs once or twice per day, replicating changed profiles to secondary regions. Use DynamoDB Streams to identify changed profiles since the last sync and transfer only the delta to minimize transfer volume. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Observability best practices for Amazon MemoryDB for Valkey](https://docs.aws.amazon.com/memorydb/latest/devguide/best-practices-observability.html) 

 **Related services:** 
+  [Amazon MemoryDB](https://aws.amazon.com/memorydb/) 
+  [Amazon DynamoDB TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) 