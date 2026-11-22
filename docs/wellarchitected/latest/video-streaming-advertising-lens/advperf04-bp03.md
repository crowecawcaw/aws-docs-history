

# ADVPERF04-BP03 Review your distributed database setup (sharding and replication) for performance, cost, and availability needs

 Evaluate trade-offs between performance, cost, and availability when configuring sharding and replication for advertising databases. Uniform multi-AZ replication for all data categories inflates cross-AZ transfer costs. Oversized database clusters without sharding waste compute for data that doesn't require it. 

 **Desired outcome:** 
+  Your advertising databases scale horizontally through sharding without over-provisioning expensive high-performance instances for your entire dataset. 
+  Replication is scoped to the data and zones that actually require it, so you get the availability your workload needs without paying for redundancy where the risk doesn't justify the cost. 
+  Availability Zone affinity is configured between bidder nodes and database nodes, which avoids cross-AZ data transfer charges for bid path queries. 

 **Common anti-patterns:** 
+  Replicating all data across every Availability Zone by default without evaluating which datasets actually require Multi-AZ durability, which inflates cross-AZ data transfer costs for data where single-AZ availability is acceptable. 
+  Running a monolithic database cluster without sharding, so the entire dataset must fit on high-performance instances even when only a fraction is touched on the latency-sensitive bid path. 

 **Benefits of establishing this best practice:** 
+  With thoughtful sharding and replication design, you can match infrastructure cost to actual workload requirements. 
+  For high-volume advertising databases, cost savings from targeted replication and horizontal sharding can be significant. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Cross-AZ data transfer costs accumulate at advertising scale. Every bid path database query that crosses an Availability Zone boundary incurs $0.01/GB in each direction. At millions of queries per second, even small query payloads generate substantial transfer costs. Availability Zone affinity between bidder compute and database nodes avoids these charges by routing reads to replicas in the same Availability Zone. 

 For Aerospike, the Availability Zone affinity feature removes cross-AZ transfer costs for high-frequency bid-evaluation reads (user profile lookups, frequency cap checks, audience segment membership queries). 

 For advertising user profile stores, sharding by user ID hash distributes lookup load evenly across nodes. Each node handles a fraction of total request volume. You can then provision many appropriately sized instances instead of expensive high-performance instances sized for peak aggregate load. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable Availability Zone affinity in Aerospike for bid path queries:** Configure Aerospike's rack-aware feature and client library to prefer reads from nodes in the same Availability Zone as the bidder application. Verify that bid evaluation traffic isn't crossing Availability Zone boundaries by monitoring VPC Flow Logs for cross-AZ traffic between bidder instances and Aerospike nodes. Measure the reduction in cross-AZ data transfer charges after enabling Availability Zone affinity. 

1.  **Design a sharding strategy based on your access patterns:** For user profile data accessed by user ID, use consistent hashing on the user ID to distribute records evenly across Aerospike nodes. For campaign data accessed by campaign ID, shard by campaign ID range. Document the sharding key for each data category and the expected distribution of access across shards to verify that the shard count is appropriate for your QPS. 

1.  **Apply Multi-AZ replication selectively based on availability requirements:** For data on the critical bid path (user profiles, frequency caps, audience segments), replicate across multiple Availability Zones to maintain availability if a single zone experiences an impairment. For data with lower availability requirements (historical campaign records, batch analytics inputs), consider keeping the primary in a single Availability Zone and using read replicas only where read throughput requires it. Evaluate cross-AZ replication costs against the business impact of unavailability for each data category. 

1.  **Monitor cross-AZ traffic and adjust placement:** Use VPC Flow Logs and [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to identify cross-AZ data transfer charges attributable to database traffic. For database-compute pairs generating significant cross-AZ charges, move the database nodes or compute to colocate them in the same Availability Zone. Update Auto Scaling group placement configurations to maintain Availability Zone alignment as the fleet scales. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Amazon Ads Architecture at Scale, re:Invent 2021](https://www.youtube.com/watch?v=YRbIAmzFxxc) 

 **Related services:** 
+  [Amazon RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/) 
+  [Amazon ElastiCache Multi-AZ](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/AutoFailover.html) 