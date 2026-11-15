

# ADVREL03-BP03 Deploy stateful dependencies across multiple Availability Zones
<a name="advrel03-bp03"></a>

 Deploy databases, caches, and message queues across multiple Availability Zones to match the RTO, RPO, and latency requirements of each advertising component tier. Evaluate trade-offs between single-AZ and multi-AZ deployments for each stateful dependency, with consideration for cost, failover speed, and the bid-response latency budget. 

 **Desired outcome:** 
+  Database configurations match the RTO and RPO requirements of the advertising components they serve. 
+  Failover procedures are automated and tested, not discovered for the first time during a production incident. 
+  The recovery strategy selected (from periodic snapshots to multi-AZ hot standby) is proportional to the business impact of data loss. 
+  Failover for all Tier 1 stateful dependencies completes within the bid response latency budget. 

 **Common anti-patterns:** 
+  Applying one database HA pattern uniformly instead of matching it to each tier's RTO/RPO and business impact. 
+  Enabling multi-AZ everywhere without accounting for cross-AZ data transfer cost on high-volume tables. 
+  Connecting applications to instance endpoints rather than the cluster endpoint, defeating automatic failover. 
+  Assuming failover works without testing it, discovering the actual failover duration for the first time during a production incident. 
+  Storing critical bid state only in local instance storage or single-AZ volumes while assuming compute redundancy is sufficient. 
+  Running caching layers (ElastiCache, Memcached) in single-AZ mode, so a zone failure removes both database failover protection and the cache layer simultaneously. 

 **Benefits of establishing this best practice:** 
+  Database configurations match the RTO and RPO requirements of the components they serve, avoiding over- and under-provisioning. 
+  Automated, tested failover keeps the bid path available during Availability Zone disruptions. 
+  Recovery strategy cost is proportional to the business impact of data loss for each tier. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Treating advertising data stores as one single class can produce availability or over-engineering issues. Tiers exist because data staleness has a different business meaning in each store. A frequency-cap or user-profile store serves the live auction. If it lags or becomes unavailable, the system overserves ads within seconds. Overserving spends already-exhausted budgets and breaches contractual caps. Both the acceptable data loss and the acceptable downtime are therefore measured in seconds to a minute. 

 People can directly edit campaign management data. A trafficker who can't change a line item for ten minutes loses productive time without creating compliance exposure, so minutes of recovery are tolerable. Analytics stores serve no live traffic at all. A warehouse restored hours later reproduces the same reports, so paying for instant recovery there buys nothing. 

 Synchronous multi-AZ replication and globally replicated tables add an ongoing premium. Pay it where a minute of unavailability costs real auction revenue or creates overspend liability, and skip it on data that isn't read by live traffic. 

 Each service bills that premium differently. A Multi-AZ relational deployment roughly doubles instance and storage cost because you pay for the standby. The replication traffic between primary and standby isn't separately billed. A globally replicated table instead multiplies write cost by the number of replica Regions. Each write is billed as a replicated write unit in every Region. No separate cross-Region transfer fee applies. Either way, the cost is ongoing and scales with write volume. 

 Under-protecting Tier 1 becomes visible quickly. Paying Tier 1 prices for Tier 3 data is harder to spot and happens more often, because a default template applied the same deployment everywhere. Multi-Region replication is the next step above multi-AZ in the same trade-off. It protects globally served data against Regional impairment at a higher premium. Only globally read stores (campaign configuration and audience definitions) justify that premium. 

 Replication and failover protect against infrastructure loss. Bad data is a separate problem. A corrupt write, an errant migration, or an application bug replicates to the standby as faithfully as a good write. Failing over then reaches the same damaged data. Point-in-time recovery and snapshots solve that separate problem. Even at the highest tier, pair replication with an independent recovery path. 

 Choose each store's tier jointly with the revenue owners, not the database team alone. Tier placement depends on the business impact of data loss and cannot be automated. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure Aurora Multi-AZ for Tier 1 auction databases:** Deploy Aurora clusters with one writer and one reader replica in a different Availability Zone. Enable automatic failover. Test failover by using AWS FIS to simulate an Availability Zone failure and measuring actual failover duration. Configure application connection strings to use the cluster endpoint (not instance endpoint) so that failover happens automatically without application changes. 

1.  **Configure DynamoDB for high-availability bid path data stores:** For user profile and frequency cap data, use DynamoDB with on-demand capacity and point-in-time recovery enabled. For global campaigns, enable DynamoDB global tables. Set up DynamoDB TTL on bid event records to manage table size and query performance. Configure CloudWatch alarms on DynamoDB throttled requests to detect capacity issues before they affect bid processing. 

1.  **Implement single-AZ database resilience for cost-sensitive Tier 2 components:** For campaign management databases where RPO/RTO requirements permit, implement periodic snapshots (every 15 minutes) plus a read replica in a different Availability Zone. Use the read replica for promotion to primary in case of Availability Zone failure (5–15 minute RTO). Document the promotion procedure and include it in the DR runbook. 

1.  **Use Aurora Global Database for lowest-latency Multi-Region reads:** For advertising data that must be read from multiple regions (campaign configurations, audience segment definitions, brand safety rules), deploy Aurora Global Database with a primary region and 1–2 secondary regions. Measure actual read latency from each Region and verify it meets your bid-path requirements. Configure the secondary regions as read-only endpoints to block accidental writes. 

1.  **Make message queues and caching layers Multi-AZ:** Amazon SQS is inherently Multi-AZ. If using Amazon MSK or self-managed Kafka, confirm brokers span at least 2 Availability Zones with min.insync.replicas=2. Enable ElastiCache for Redis Multi-AZ with automatic failover. Size each Availability Zone's cache to handle the full workload (not just its proportional share) so the surviving Availability Zone can absorb traffic immediately after failover. 

1.  **Remove single-AZ state from the bid path:** Audit the bid pipeline for any state held only in local instance storage, single-AZ EBS volumes, or in-memory process state without external persistence. Migrate critical state to Multi-AZ stores (DynamoDB, ElastiCache Multi-AZ, or replicated EBS with Multi-Attach). 

1.  **Test failover against the bid response latency budget:** Test that database and cache failover completes within your bid response latency budget. RDS Multi-AZ DB instance failover typically takes 60 to 120 seconds (crash recovery on cold standby). Multi-AZ DB cluster deployments (MySQL/PostgreSQL) fail over in under 35 seconds. ElastiCache Multi-AZ failover completes in under 30 seconds. Verify these timings against your bid deadline requirements using AWS FIS experiments. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP04 Design your workloads to withstand failures of individual components](advrel04-bp04.md) 
+  [ADVREL03-BP01 Use a full regional deployment for compute resources through Auto Scaling groups and compute container orchestrators](advrel03-bp01.md) 

 **Related documents:** 
+  [Amazon RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/) 
+  [Using Amazon Aurora Global Database to build resilient multi-Region applications](https://aws.amazon.com/blogs/database/use-amazon-aurora-global-database-to-build-resilient-multi-region-applications/) 

 **Related services:** 
+  [Amazon Aurora](https://aws.amazon.com/rds/aurora/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon RDS](https://aws.amazon.com/rds/) 