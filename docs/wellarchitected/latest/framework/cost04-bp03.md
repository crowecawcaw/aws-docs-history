

# COST04-BP03 Optimize services to reduce data transfer costs

 Pricing, service capabilities, and your usage patterns change over time. Optimize data transfer continuously to keep cost proportional to value while preserving performance, reliability, and security. 

 **Desired outcome:** 
+  Your data transfer architecture is reviewed on a regular cadence, not fixed at its original design. 
+  Your data transfer cost stays proportional to the value it delivers as the workload grows. 
+  Your optimization decisions weigh cost against performance, reliability, and security rather than cost alone. 

 **Common anti-patterns:** 
+  Teams treat the data transfer architecture as immutable and never revisit the original design. 
+  Optimization efforts prioritize cost above performance, reliability, and security. 
+  Reviews happen only when a bill spikes, rather than on a schedule. 
+  New network features and pricing changes go unnoticed, so the architecture misses cheaper options. 

 **Benefits of establishing this best practice:** 
+  Data transfer components stay cost-effective as usage patterns change and new services appear. 
+  Cost scales in a manageable way because the design is built for efficiency and reviewed continuously. 
+  Optimization decisions protect performance, reliability, and security because trade-offs are explicit. 
+  Expensive flows are found and addressed before they dominate the bill. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 AWS releases network features, adjusts pricing, and adds Regions continuously. Your traffic patterns shift as the workload changes. Schedule regular reviews and stay current with [networking features](https://aws.amazon.com/blogs/networking-and-content-delivery/), [architectural best practices](https://aws.amazon.com/whitepapers/), and [prescriptive guidance](https://aws.amazon.com/prescriptive-guidance/). 

 The largest flows have the biggest savings potential, so rank flows by current or projected cost and work from the top. 

 Data transfer choices affect resilience and performance. Cross-Region replication costs money and supports disaster recovery. Cross-Availability Zone traffic costs money and provides fault isolation. Treat cost as one input alongside performance, reliability, and security, and make the trade-off explicit. 

 Most data transfer savings come from a few approaches: reduce the volume that crosses charged boundaries, use cheaper paths such as private connectivity, keep traffic within a single Availability Zone, serve repeated content from an edge cache, or move large one-time transfers to dedicated services. 

 You need continuous visibility into usage and cost. [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), [AWS Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html), and [VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) show what traffic flows and over which paths. The [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/cur-data-transfers-charges.html), [AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/create-cost-categories.html), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), and [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) attribute cost to that traffic and alert you to unexpected changes. The AWS Free Tier includes monthly data transfer allowances for internet egress and for content delivery, which can cover low-volume workloads. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish ongoing visibility and a review cadence:** Schedule recurring reviews of data transfer cost and usage, and configure the monitoring services named in the guidance so each review works from current data. Route cost anomalies to the teams that own the affected flows. 

1.  **Prioritize the most costly flows:** Rank data transfer flows by current or projected cost, and review the highest-cost flows first. Direct optimization effort where it changes the bill the most. 

1.  **Share network services across workloads:** Where it does not conflict with resilience or performance requirements, [share network services](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) across multiple workloads so their fixed cost is spread rather than duplicated. 

1.  **Minimize cross-Region data transfer:** Data moved between AWS Regions can cost more than data moved within a Region. Multi-Region transfer usually supports disaster recovery and high availability, so reduce it only where doing so does not weaken those objectives. For more information, see [AWS multi-Region fundamentals](https://docs.aws.amazon.com/wellarchitected/latest/framework/reliability.html). 

1.  **Keep traffic within an Availability Zone where possible:** Data that crosses Availability Zones is charged in both directions, while traffic within a single Availability Zone over private IP addresses is not. Map Availability Zones across accounts to confirm traffic is not crossing zones unintentionally. For more information, see [How can I map Availability Zones across my accounts?](https://repost.aws/knowledge-center/vpc-map-cross-account-availability-zones) 

1.  **Use interface VPC endpoints for private access to services:** [Interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html), provided by [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html), create private connections between your VPC and supported services. They can reduce public data transfer and [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) cost, in exchange for an hourly and per-gigabyte fee. 

1.  **Use gateway endpoints for Amazon S3 and Amazon DynamoDB:** Gateway endpoints provide private access to [Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) and [Amazon DynamoDB](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html) with no additional charge. Use them where their limitations do not conflict with your requirements. 

1.  **Place NAT gateways in the same Availability Zone as their traffic:** [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) provide managed scaling and lower operational cost than a standalone NAT instance. Locating a NAT gateway in the same Availability Zone as the instances it serves avoids cross-zone charges for that traffic. 

1.  **Deliver repeated content from the edge:** [Amazon CloudFront](https://aws.amazon.com/cloudfront/) caches content at edge locations, which lowers latency and reduces egress from your origin resources. Pair it with [caching services](https://aws.amazon.com/caching/aws-caching/) to avoid transferring the same data repeatedly. 

1.  **Choose an appropriate service for large one-time transfers:** For moving large datasets, [AWS DataSync](https://aws.amazon.com/datasync/) automates and accelerates online transfer, and [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) provides secure high-speed physical upload at an AWS location. [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html) remains available to existing Snow customers, but as of November 2025 is no longer offered to new customers. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST04-BP01 Define network and data transfer infrastructure costs](cost04-bp01.md) 
+  [COST04-BP02 Perform data transfer modeling](cost04-bp02.md) 
+  [COST06-BP04 Consider using shared resources](cost06-bp04.md) 
+  [COST09-BP02 Continuously review and optimize the workload](cost09-bp02.md) 

 **Related documents:** 
+  [Building a scalable and secure multi-VPC network infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) 
+  [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) 
+  [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) 
+  [Gateway endpoints for Amazon DynamoDB](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html) 
+  [Data transfer costs in the AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/cur-data-transfers-charges.html) 
+  [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) 
+  [Detecting unusual spend with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) 
+  [Creating cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/create-cost-categories.html) 
+  [Amazon CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/) 

 **Related videos:** 
+  [Monitoring and optimizing your data transfer costs](https://www.youtube.com/watch?v=UjliYz25_qo) 
+  [AWS Cost Optimization Series: CloudFront](https://www.youtube.com/watch?v=k8De2AfAN3k) 
+  [How can I reduce data transfer charges for my NAT gateway?](https://www.youtube.com/watch?v=hq4KtPRezus) 

 **Related examples:** 
+  [How to chargeback shared services: an AWS Transit Gateway example](https://aws.amazon.com/blogs/aws-cloud-financial-management/gs-chargeback-shared-services-an-aws-transit-gateway-example/) 
+  [Understand AWS data transfer details in depth from the Cost and Usage Report using Amazon Athena and Quick](https://aws.amazon.com/blogs/networking-and-content-delivery/understand-aws-data-transfer-details-in-depth-from-cost-and-usage-report-using-athena-query-and-quicksight/) 
+  [Overview of data transfer costs for common architectures](https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/) 
+  [Cost-optimizing your AWS architectures by using Amazon CloudFront features](https://aws.amazon.com/blogs/networking-and-content-delivery/cost-optimizing-your-aws-architectures-by-utilizing-amazon-cloudfront-features/) 
+  [How can I reduce data transfer charges for my NAT gateway?](https://repost.aws/knowledge-center/vpc-reduce-nat-gateway-transfer-costs) 

 **Related services:** 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [AWS caching solutions](https://aws.amazon.com/caching/aws-caching/) 
+  [AWS DataSync](https://aws.amazon.com/datasync/) 
+  [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) 