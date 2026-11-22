

# ADVREL03-BP04 Reserve appropriate capacity of services in the supported regions

 Manage service capacity across multiple Regions. Load-test regularly at five times your baseline RTB traffic to validate capacity requirements. Reserve capacity to handle normal operations, peak loads, and potential disruptions. 

 **Desired outcome:** 
+  Service capacity reservations are sized based on load test results at 5x baseline RTB traffic. 
+  Capacity reservations cover both steady-state operations and anticipated peak events (seasonal campaigns, live events). 
+  Capacity planning accounts for all resource types (compute, network, database connections, and cache memory) to avoid single-layer bottlenecks. 

 **Common anti-patterns:** 
+  Sizing capacity to average load instead of validated peak, which leaves no headroom for seasonal campaigns or live events. 
+  Skipping load testing, so capacity reservations are guesses rather than evidence-based. 
+  Reserving compute but ignoring database connections, cache memory, or network (creating a single-layer bottleneck). 
+  Sizing ElastiCache to average memory and relying on LRU eviction during peaks, so cache-miss storms overload the database tier. 

 **Benefits of establishing this best practice:** 
+  Capacity reservations are sized from load-test evidence at 5x baseline RTB traffic. 
+  Reservations cover both steady state and anticipated peak events, limiting disruption during high-traffic periods. 
+  Planning across all resource types helps avoid single-layer bottlenecks that constrain the whole workload. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Elastic capacity is available only if spare capacity exists when you request it. Under broad regional demand, which a major live event produces across every system serving it, a scaling request can be delayed or declined. The workloads competing for that capacity are often the other advertising systems responding to the same event, so the correlation is structural. A reservation commits capacity to you up to the size of the reservation, and its value is highest when elasticity is least dependable. Treat reservations as one mitigation among several. Diversify instance types across families and sizes to widen the pool a scale-out can draw from. A reservation-only approach only shifts the point of failure, because an exhausted reserved pool also fails. 

 Each capacity type fails differently under load, so one reservation strategy doesn't cover a bid path. Compute shortfall degrades gradually: fewer instances mean higher per-instance load and rising latency, and some bids still return. Database throughput shortfall produces throttling, so requests are rejected rather than slowed. Cache shortfall compounds differently than compute and database shortfalls. A cache sized for the average working set begins evicting under peak load. Each eviction of a live key adds a database read plus a write-back, arriving when the database is most loaded from other sources. High eviction volumes also raise CPU on the cache nodes themselves, so the tier that was absorbing load starts contributing to it. Size cache memory against the hot dataset plus headroom rather than against observed average utilization. 

 You pay for reservations whether the peak arrives, and you must arrange them before capacity is scarce, which means committing on a forecast. Reserving late defeats the purpose, because the shortage being hedged against is already underway. Reserving generously for every event becomes permanent overspend. The judgment is tractable because advertising revenue is concentrated in a small number of known events. Weigh the cost of headroom against the revenue at risk during those windows. 

 A capacity plan is unproven until you produce and test load. The test must raise every tier together because the tiers interact. Compute that scales correctly into a cache that starts evicting produces an unpredictable database bottleneck. Testing tiers separately validates each one and can miss interactions that cause faults. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create On-Demand Capacity Reservations before anticipated peaks:** Use Amazon EC2 On-Demand Capacity Reservations (ODCRs) to pre-reserve EC2 instance capacity in the Availability Zones where your advertising workloads run. Create reservations at least 72 hours before anticipated peak events. Configure instance placement groups so that reserved instances are placed on hardware with low-latency networking for RTB workloads. 

1.  **Right-size DynamoDB provisioned capacity with auto scaling:** Configure DynamoDB provisioned capacity (not on-demand) for tables with predictable traffic patterns. Set target utilization at 70% with auto scaling minimum at 110% of average traffic and maximum at 150% of expected peak. This provides burst capacity for unexpected spikes while keeping costs controlled during normal operation. 

1.  **Size ElastiCache clusters for peak memory requirements:** Calculate peak memory requirements based on: number of unique items in cache × average item size × 120% headroom. Configure ElastiCache cluster nodes with memory capacity to hold the complete hot dataset plus headroom. Avoid relying on LRU eviction during peak traffic: cache misses during peak events cascade to database overload. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP03 Architect for variable demand](advrel01-bp03.md) 
+  [ADVREL03-BP01 Use a full regional deployment for compute resources through Auto Scaling groups and compute container orchestrators](advrel03-bp01.md) 
+  [ADVREL05-BP05 Maintain independent operational readiness in each Region](advrel05-bp05.md) 

 **Related documents:** 
+  [Troubleshoot Amazon EC2 Auto Scaling: EC2 instance launch failures](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-instancelaunchfailure.html) 
+  [Reserve capacity in specific Availability Zones with Capacity Reservations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-ec2-capacity-reservations.html) 
+  [Best practices for sizing your Amazon ElastiCache (Redis OSS) clusters](https://aws.amazon.com/blogs/database/best-practices-for-sizing-your-amazon-elasticache-for-redis-clusters/) 
+  [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) 
+  [What to Consider when Selecting a Region for your Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/) 

 **Related services:** 
+  [Amazon Route 53](https://aws.amazon.com/route53/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 