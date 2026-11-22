

# ADVPERF03-BP02 Use object storage to store and analyze raw data from ad servers, DSPs, and DMPs

 [Amazon S3](https://aws.amazon.com/s3/) can store massive amounts of advertising data while balancing cost and performance. Use object storage to build data lakes and analyze this data, from real-time bid analytics to historical attribution modeling. 

 **Desired outcome:** 
+  Advertising data from raw event logs and campaign assets to ML training datasets and analytics pipelines is stored in Amazon S3 with the right storage class, partitioning strategy, and access configuration for each workload type. 
+  Storage costs scale efficiently with data volume, and performance-critical workloads are not bottlenecked by storage tier mismatches. 
+  S3 Intelligent-Tiering automatically optimizes storage costs for advertising data with variable or unpredictable access patterns. 

 **Common anti-patterns:** 
+  Storing all advertising data under a single S3 prefix regardless of access frequency or performance requirements, which creates request-rate bottlenecks on high-throughput ingestion paths. 
+  Manually managing storage class transitions for large advertising data lakes instead of using automated tiering, so teams pay either unnecessary storage cost or operational overhead. 
+  Not using S3 Transfer Acceleration for long-distance data ingestion from distributed ad servers and DSPs. 

 **Benefits of establishing this best practice:** 
+  Amazon S3 provides virtually unlimited, durable object storage with a tiering model you can use to optimize cost without sacrificing availability. 
+  For advertising workloads that generate large volumes of event data, campaign assets, and model training inputs, matching each data category to the right storage class reduces storage spend while keeping performance-critical paths fast. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising platforms generate multiple categories of data with widely different access patterns and performance requirements. Bid logs and impression events are written continuously. They are read heavily in the hours immediately after generation for pacing and frequency capping, then accessed infrequently for historical analysis. Campaign creative assets are written once during campaign setup and read repeatedly during active delivery, then rarely accessed afterward. ML training datasets are accessed intensively during model training runs, then idle between training cycles. 

 [Amazon S3's tiering model](https://aws.amazon.com/s3/storage-classes/) provides a cost tier for each access pattern. Use S3 Intelligent-Tiering for advertising data lakes where access patterns change over campaign lifecycles. Hot content automatically transitions to lower-cost tiers as the campaign completes, with no lifecycle rules to manage. 

 Amazon S3 request throughput scales with each prefix. A single prefix supporting millions of bid log writes per day can become a throughput bottleneck. Distribute objects across multiple prefixes (by date, campaign ID, or data source) to spread request load and maximize available throughput. 

 Amazon S3 Transfer Acceleration routes uploads through the nearest AWS edge location and onto the AWS backbone network. This reduces the variability and latency of long-distance data transfers for advertising platforms with globally distributed ad servers or DSP integrations. Use it to collect bid logs from European or Asia-Pacific ad infrastructure into a primary US-based analytics data lake. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Partition advertising data across multiple S3 prefixes:** Design prefix hierarchies that distribute request load. For bid log data, use a prefix structure such as bid-logs/year=YYYY/month=MM/day=DD/hour=HH/ to partition by time. For campaign creative assets, partition by campaign ID. This enables partition pruning in [Amazon Athena](https://aws.amazon.com/athena/) queries and limits request rate throttling on a single prefix. 

1.  **Apply S3 Intelligent-Tiering to advertising data with variable access patterns:** Enable S3 Intelligent-Tiering on buckets containing campaign data, audience segments, and historical bid logs where access frequency changes over campaign lifecycles. Configure the optional Archive Access tier (objects not accessed for 90 days) and Deep Archive Access tier (objects not accessed for 180 days) for cost-optimized storage of completed campaign data. 

1.  **Use S3 Express One Zone for performance-critical advertising data:** For model artifacts, temporary creative assets, and intermediate audience processing data that require single-digit-millisecond access from your compute, use S3 Express One Zone directory buckets colocated in the same Availability Zone as your EC2 or ECS workloads (for more detail, see ADVPERF03-BP04). 

1.  **Enable S3 Transfer Acceleration for distributed data ingestion:** For advertising platforms with ad servers, DSPs, or data collectors operating in regions distant from your primary analytics bucket, enable S3 Transfer Acceleration on the destination bucket. Configure your data collection agents to use the <bucket>.s3-accelerate.amazonaws.com endpoint. Measure transfer latency improvement in your specific geographic configuration. Acceleration provides the most benefit for cross-continental transfers. 

1.  **Monitor S3 access and performance:** Use AWS CloudTrail to log S3 API activity for compliance and security auditing. Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) S3 storage metrics to track request counts, error rates, and first-byte latency by bucket and prefix. Enable S3 Storage Lens for organization-wide visibility into storage utilization, activity trends, and cost optimization opportunities across all your advertising data buckets. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF03-BP04 Use single-zone high-performance object storage for latency-sensitive ad serving and model artifact retrieval](advperf03-bp04.md) 

 **Related documents:** 
+  [Getting started with S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-one-zone.html) 
+  [Manage Amazon S3 storage costs granularly and at scale using S3 Intelligent-Tiering](https://aws.amazon.com/blogs/storage/manage-amazon-s3-storage-costs-granularly-and-at-scale-using-s3-intelligent-tiering/) 

 **Related services:** 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 