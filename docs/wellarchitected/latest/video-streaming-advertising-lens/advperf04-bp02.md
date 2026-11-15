

# ADVPERF04-BP02 Consider purpose-built databases for advertising workloads
<a name="advperf04-bp02"></a>

 Purpose-built databases offer low latency and can meet the scaling needs of advertising workloads more efficiently than general-purpose relational databases. Use in-memory databases for sub-millisecond bid path data and OLTP databases for medium-latency transactional workloads. 

 **Desired outcome:** 
+  Your low-latency and medium-latency advertising data workloads run on databases purpose-built for their specific access patterns. 
+  Your workloads deliver consistent performance at scale without forcing you to over-engineer a general-purpose database for requirements it was not designed for. 

 **Common anti-patterns:** 
+  Using a single relational database for both real-time bidding data and transactional campaign management data, which forces a medium-latency OLTP engine to serve sub-millisecond read requirements it can't consistently meet under high concurrency. 
+  Defaulting to general-purpose databases for ad tech workloads without evaluating purpose-built alternatives like Aerospike. 

 **Benefits of establishing this best practice:** 
+  Purpose-built databases avoid the performance compromises that come from fitting advertising workloads into general-purpose engines. They reduce bid response latency and make scaling simpler. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 For low-latency bid path data, three database options align with advertising use cases: 

1.  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) delivers single-digit-millisecond key-value and document lookups at scale, with on-demand capacity that absorbs traffic bursts without pre-provisioning. Use it for high-read, low-write data such as user profile lookups and bid request enrichment where the access pattern is a known key lookup. 

1.  Aerospike is a purpose-built database for ad tech workloads requiring extreme throughput and consistent sub-millisecond latency at scale, particularly for user profile stores and real-time audience data where NVMe-backed local storage avoids network-attached storage latency. Aerospike's hybrid memory architecture stores indexes in DRAM and data on NVMe, which combines in-memory read speed with the durability of persistent storage. 

1.  [Amazon Aurora Global Database](https://aws.amazon.com/rds/aurora/) is appropriate for medium-latency transactional workloads requiring Multi-Region availability. Campaign configuration, advertiser account data, and inventory management records benefit from Aurora's OLTP performance and the ability to replicate data globally with sub-second cross-region lag. Aurora's fast regional failover (under 1 minute recovery time objective) supports campaign management workloads that require high availability. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Use DynamoDB for high-read bid path lookups:** Configure DynamoDB tables for user profile lookups, frequency cap checks, and audience segment membership with appropriate primary key design (user ID as partition key) and secondary indexes for targeting attribute queries. Enable DynamoDB Accelerator (DAX) as an in-memory cache layer to reduce read latency from single-digit milliseconds to microseconds for frequently accessed profiles. 

1.  **Deploy Aerospike on Storage Optimized instances for extreme throughput requirements:** For workloads requiring millions of TPS with sub-millisecond p99 latency (large-scale user profile stores, real-time bidding data stores), deploy Aerospike on I4i instances with locally attached NVMe storage. Configure Aerospike's storage engines to use the NVMe device directly rather than through the operating system's file system for minimum latency. 

1.  **Use Aurora Global Database for Multi-Region campaign management:** For campaign configuration, account data, and inventory records that require transactional consistency and Multi-Region availability, deploy Aurora with Global Database replication. Configure secondary regions as read replicas with custom endpoints for low-latency regional reads. Use Aurora's write forwarding feature to allow writes through secondary regions without requiring application changes. 

1.  **Implement DynamoDB TTL for bid event data:** For bid logs, impression events, and click tracking data that should expire after a retention period (typically 30–90 days), configure DynamoDB TTL to automatically delete expired items without consuming write capacity. This keeps table size predictable and query performance consistent as data accumulates. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF04-BP01 Choose a data management strategy that matches your availability, latency, and access requirements](advperf04-bp01.md) 

 **Related documents:** 
+  [Running Ad Tech Workloads on AWS with Aerospike at Petabyte Scale](https://aws.amazon.com/blogs/industries/running-ad-tech-workloads-on-aws-with-aerospike-at-petabyte-scale/) 
+  [Use Amazon Aurora Global Database to build resilient multi-region applications](https://aws.amazon.com/blogs/database/use-amazon-aurora-global-database-to-build-resilient-multi-region-applications/) 

 **Related services:** 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/) 