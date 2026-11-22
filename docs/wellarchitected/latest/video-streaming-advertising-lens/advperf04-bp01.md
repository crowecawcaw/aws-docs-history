

# ADVPERF04-BP01 Choose a data management strategy that matches your availability, latency, and access requirements

 Advertising workloads need a data management strategy that matches each datastore to the requirements of its data. When you choose a datastore because of familiarity rather than based on your workload requirements, you risk degraded performance for latency-sensitive workloads and wasted cost on overprovisioned storage. 

 **Desired outcome:** 
+  Every datastore in your advertising stack is selected based on a clear understanding of the latency tier, availability requirements, and access patterns of the data it holds. 
+  Real-time bidding data, audience segmentation data, and historical reporting data each land in a service optimized for their specific characteristics. 
+  Datastore selection is validated against availability requirements in addition to latency. 

 **Common anti-patterns:** 
+  Using a single database technology across all advertising data categories regardless of their latency profile, so low-latency real-time bidding data and high-latency historical reporting data compete for the same resources. 
+  Storing millisecond-sensitive bid request data in a batch-oriented analytics store, or paying for high-performance storage for data that is only queried weekly. 

 **Benefits of establishing this best practice:** 
+  Matching each data category to the right AWS data service reduces latency on the critical bid path, lowers storage costs by right-sizing each tier, and simplifies operations by using purpose-built services. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising data falls into three latency tiers, each with a different class of datastore: 

1.  **Low-latency data (real-time, sub-millisecond to single-digit milliseconds):** This data must be processed within milliseconds to support ad delivery, real-time bidding, and tracking of user interactions. It includes bid requests and responses, user device and location data, ad impression requests, and real-time campaign performance signals (clicks, impressions, and conversions). Datastores must deliver predictable low-latency reads and writes under high concurrency. Use [Amazon ElastiCache](https://aws.amazon.com/elasticache/) (Redis or Memcached) for sub-millisecond in-memory access, and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) for single-digit-millisecond key-value lookups at scale. 

1.  **Medium-latency data (near real-time to batch, minutes to hours):** This data supports audience targeting, campaign optimization, and attribution analysis. It tolerates processing delays of minutes to hours and is typically updated on a rolling basis. It includes user behavioral data, audience segmentation, campaign optimization metrics, and attribution data. Use [Amazon Aurora](https://aws.amazon.com/rds/aurora/) or [Amazon RDS](https://aws.amazon.com/rds/) for relational audience and campaign data that requires transactional consistency, and on-demand DynamoDB for variable access patterns. 

1.  **High-latency data (batch or offline, hours to days):** This data supports analysis, reporting, and long-term decision-making. It includes historical campaign performance, detailed analytics, third-party data from DMPs, and ad creative assets. Use [Amazon S3](https://aws.amazon.com/s3/) for durable cost-optimized storage, and [Amazon Redshift](https://aws.amazon.com/redshift/) or [Amazon Athena](https://aws.amazon.com/athena/) for large-scale analytics and reporting queries over historical datasets. 

 Availability requirements also constrain datastore selection. Low-latency bid path data requires multi-AZ deployment with automatic failover, so a single-AZ datastore is unsuitable regardless of its latency. Historical analytics data can tolerate single-AZ deployment with snapshot-based recovery when cost is a constraint. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Categorize all advertising data by latency tier:** Create a data inventory that classifies each data category as low-latency (bid path), medium-latency (audience and campaign), or high-latency (analytics and reporting). Document the access pattern (read-heavy, write-heavy, mixed), expected QPS at peak, required response time, and retention period for each category. 

1.  **Map each data category to an AWS data service:** For low-latency bid path data, evaluate ElastiCache for sub-millisecond access and DynamoDB for single-digit-millisecond key-value lookups. For medium-latency audience and campaign data, evaluate Aurora or RDS for relational consistency. For high-latency analytics, use S3 plus Athena or Redshift. Document the selection rationale for each mapping. 

1.  **Validate datastore selection against availability requirements:** For each data category, confirm that the chosen datastore's replication, failover, and backup capabilities meet your availability requirements. Bid path data in DynamoDB requires multi-AZ global tables if your architecture spans regions. Aurora requires Multi-AZ deployment for production bid management databases. Match the datastore's availability tier to the business impact of the data category. 

1.  **Validate latency against your bid response budget:** For any datastore used in the bid evaluation path, measure actual p99 read latency under your expected production load (using load testing, not published specifications). Confirm that the datastore's p99 latency fits within the fraction of the total bid response budget allocated to data access, typically no more than 5–10 ms for the combined data access operations in a bid evaluation cycle. 

1.  **Review and update datastore selections annually:** As AWS releases new services and capabilities (new DynamoDB table classes, new ElastiCache features, new Aurora configurations), review your datastore selections against current AWS services. What was the best option 18 months ago may have been superseded by a newer service that better matches your workload requirements. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF04-BP02 Consider purpose-built databases for advertising workloads](advperf04-bp02.md) 
+  [ADVPERF03-BP04 Use single-zone high-performance object storage for latency-sensitive ad serving and model artifact retrieval](advperf03-bp04.md) 

 **Related documents:** 
+  [Amazon DynamoDB: Ad tech use cases and design patterns](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-use-cases-adtech.html) 
+  [Architecture III: Picking the Right Data Store for Your Workload](https://aws.amazon.com/blogs/startups/how-to-pick-the-right-data-store-for-your-workload-1/) 

 **Related services:** 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon Aurora](https://aws.amazon.com/rds/aurora/) 