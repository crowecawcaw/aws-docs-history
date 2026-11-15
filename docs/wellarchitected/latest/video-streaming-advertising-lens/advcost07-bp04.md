

# ADVCOST07-BP04 Use serverless pricing engines that scale with transaction volume
<a name="advcost07-bp04"></a>

 You pay continual hosting costs for linear TV pricing engines used only during upfront season, even though the workload is episodic. Serverless pricing engines reduce idle compute costs during off-peak periods. 

 **Desired outcome:** 
+  Episodic linear pricing logic runs on AWS Lambda (scales to zero between upfront season). 
+  Ongoing digital bid floor optimization runs on Fargate with auto-scaling. 
+  Frequently requested pricing data is cached in ElastiCache, reducing compute per pricing request. 

 **Common anti-patterns:** 
+  Running dedicated persistent compute infrastructure for linear TV pricing engines that are heavily utilized only during upfront season (May) and scatter negotiations, so around-the-clock hosting costs accrue for workloads that are episodic and idle for the majority of the year. 
+  Maintaining separate pricing services for linear (rate card, makegood, and scatter calculations) and digital (bid floor optimization, dynamic pricing) that can't share infrastructure, caching layers, or operational tooling, which duplicates deployment, monitoring, and maintenance overhead for systems with the same architectural pattern. 
+  Provisioning digital bid floor optimization infrastructure for peak traffic volume rather than using auto-scaling, so excess capacity keeps charging during off-peak hours when request volume drops but the infrastructure remains fully provisioned. 
+  Recalculating identical rate card prices on every request without caching, which consumes compute for repeated lookups of pricing data that changes infrequently (daily or weekly) while being queried thousands of times between updates. 
+  Exposing separate pricing APIs for linear and digital buying models to downstream systems, so callers must implement format-specific integration logic and cross-system yield optimization is limited when comparing linear and digital pricing in a unified context. 

 **Benefits of establishing this best practice:** 
+  Reduce idle compute costs during off-peak periods (linear pricing is episodic, concentrated in upfront season) 
+  Pay per pricing calculation rather than per hour of provisioned capacity 
+  Handle demand spikes during upfront season without pre-provisioning 
+  Unified pricing service enables cross-system yield optimization 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising pricing engines calculate rates for inventory across buying models, such as linear rate cards, scatter pricing, makegood valuations, and digital bid floor optimization. These workloads have different temporal profiles. Linear pricing is episodic, with intense activity concentrated during upfront season (typically May in US markets) and scatter negotiation periods, then near-zero utilization for the remaining 9\+ months. Digital bid floor optimization runs continuously because programmatic auctions execute around the clock, though volume still varies between peak viewing hours and overnight lulls. 

 If you run both workload types on persistent provisioned infrastructure, you pay the same hourly rate whether the system is processing thousands of pricing calculations or sitting idle. The cost waste is most acute for linear pricing: dedicated servers running year-round for a workload that peaks during a few weeks. Episodic workloads suit per-invocation pricing (pay only when a calculation runs). Ongoing-but-variable workloads suit auto-scaling containers (scale down during low-volume periods, scale up during peaks). 

 Redundant computation is a second source of waste. Rate card prices change infrequently (daily or weekly updates) but are queried thousands of times between updates. Caching pricing results in a shared layer reduces this redundancy. Pricing data has a known refresh cadence, so time-based expiry aligned to the update frequency handles staleness without complex invalidation logic. 

 Both linear and digital pricing systems share an architectural pattern where they receive a pricing request, look up relevant parameters, apply calculation logic, and return a result. Separate deployments for each buying model duplicate deployment pipelines, monitoring dashboards, and on-call responsibilities. A unified pricing service with type-specific calculation logic behind a common API reduces this operational overhead and supports cross-system yield comparisons (what is the same audience segment worth in linear compared to digital?) that separate systems can't provide. 

 Serverless pricing with [Lambda](https://aws.amazon.com/lambda/) introduces cold start latency. For linear pricing consumed by human sales teams during negotiations, cold starts of a few hundred milliseconds are imperceptible. For digital bid floor optimization integrated into real-time auction flows, cold starts might violate latency SLAs. Use Lambda for episodic linear pricing and [Fargate](https://aws.amazon.com/fargate/) with auto-scaling for ongoing digital. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Profile pricing engine usage patterns:** Analyze CloudWatch metrics to quantify CPU utilization across the year. Identify periods of near-zero utilization (linear pricing outside upfront season) compared to ongoing moderate utilization (digital bid floor optimization). 

1.  **Migrate episodic linear pricing to Lambda:** Package linear rate card generation and scatter pricing logic as Lambda functions behind API Gateway. Lambda's pay-per-invocation pricing reduces idle costs during the 9\+ months of low activity. 

1.  **Deploy ongoing digital pricing on Fargate with auto-scaling:** Run digital bid floor optimization as an ECS Fargate service with Application Auto Scaling. Scale down during overnight hours when bid volume is minimal. 

1.  **Deploy shared ElastiCache for pricing data:** Create shared ElastiCache instances serving both linear and digital pricing engines. Cache rate card data (changes daily or weekly) and bid floor calculations (changes based on demand). This reduces redundant compute for identical pricing lookups. 

## Resources
<a name="resources"></a>

 **Related services:** 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [AWS Fargate](https://aws.amazon.com/fargate/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 