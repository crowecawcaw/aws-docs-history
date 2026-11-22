

# FND06-BP01 Configure detailed cost information sources

 Implement centralized cost management and reporting to provide detailed visibility into cloud spending across all accounts and resources in your organization.These reports support granular analysis of costs, automated reporting, and data-driven decision making for cloud financial management. 

 **Desired outcome:** 
+  You have automated collection of detailed cost and usage data across the organization. 
+  You have centralized access to granular cost data that supports various analysis needs. 
+  You have a foundation for advanced cost management capabilities and integrations. 

 **Common anti-patterns:** 
+  Relying solely on consolidated monthly billing data without detailed resource-level information and understanding of amortized cost. 
+  Not implementing consistent data collection standards across accounts. 
+  Lacking automated data processing and analysis capabilities. 
+  Turning on detailed data collection years after cloud adoption starts, losing history that cannot be backfilled. 

 **Benefits of establishing this best practice:** 
+  Improved visibility into cost drivers across the organization. 
+  Improved ability to analyze, optimize, and forecast cloud spending. 
+  Support for advanced cost allocation, showback, and chargeback capabilities. 
+  Support for data-driven financial decisions. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Summary-level billing shows the actual spend, but not which resources, services, or behaviors drove that spending. For optimization, chargeback, and cost anomaly detection, collect detailed, granular data (hourly is ideal) and include resource IDs and tags. AWS does not backfill this data, so if you turn on detailed exports late, the first months of cloud usage remain opaque. 

 Use [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/) to receive AWS Cost and Usage Report (CUR) 2.0 data at monthly, daily, or hourly granularity. CUR 2.0 captures rates, costs, and usage attributes for all chargeable AWS services, along with dimensions such as tags, account IDs, and account names. Three export types are available: *standard data export* delivers a customized table to Amazon S3 on a recurring basis, *cost and usage dashboard* deploys a pre-built AWS Quick dashboard, and *legacy data export* supports the older CUR format during transition. 

 When you include resource IDs, you can trace costs to individual resources. Turn on [split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html) for container workloads running on [Amazon ECS](https://aws.amazon.com/ecs/) or [Amazon EKS](https://aws.amazon.com/eks/). Without it, you can see cluster-level costs but cannot allocate them to the teams and business units consuming the shared compute and memory. With hourly granularity, you can correlate costs with application events and business metrics. These customizations have trade-offs in data volume and cost of storage, but the insights they produce can be worth the overhead depending on your organization's cost management priorities. 

 [AWS Glue](https://aws.amazon.com/glue/) prepares the data for analysis, [Amazon Athena](https://aws.amazon.com/athena/) supports SQL queries against the reports, and [AWS Quick](https://aws.amazon.com/quick/) provides visualization. The [AWS Cloud Intelligence Dashboards](https://docs.aws.amazon.com/solutions/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws/) provide pre-built dashboards for common cost analysis scenarios. 

 To calculate unit economics (cost per transaction, cost per customer, cost per feature), you need application telemetry for the business outcomes those costs produce. Log business metrics at a cadence that matches your cost data (hourly at minimum) so you can correlate them. For guidance on application logging and monitoring, see the [Well-Architected Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/operational-excellence.html). 

**Important**  
 Configure data exports in your management account (or a [designated billing account with the appropriate permissions](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-s3-bucket.html)) so the export captures usage across all member accounts. Exports configured inside a member account capture only that account's activity and miss the rest of the organization. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create data exports:** Create customized exports with the data you want using [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/) and control the schema of your exports. Set up a dedicated [Amazon S3](https://aws.amazon.com/s3/) bucket with appropriate lifecycle policies for cost data storage. AWS Data Exports can automatically create and configure this bucket during setup. 

1.  **Configure the cost and usage report:** Turn on all available cost data dimensions including resource IDs, tags, and usage attributes. Turn on [split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html) for container workloads and shared resources. Pick data compression and format settings that fit your storage and query needs. Set hourly granularity in your data export settings so you can do detailed time-based cost analysis and tie costs to business events. 

1.  **Implement visualization and reporting:** Consider deploying [AWS Cloud Intelligence Dashboards](https://docs.aws.amazon.com/solutions/advanced-cloud-observability-with-cloud-intelligence-dashboards-on-aws/) for immediate visibility. Configure [AWS Quick](https://aws.amazon.com/quick/) with appropriate [IAM roles and permissions](https://docs.aws.amazon.com/quick/latest/userguide/security_iam_service-with-iam.html) for organization-wide access. Create custom dashboards for different stakeholder groups. 

1.  **Establish automated data processing:** Configure [AWS Glue](https://aws.amazon.com/glue/) crawlers to automatically catalog your cost data exports. Set up [Amazon Athena](https://aws.amazon.com/athena/) queries or saved views for common cost analysis patterns. Consider automated alerts for cost anomalies using [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) or custom solutions that query your detailed cost data. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND06-BP02 Standardize cost attribution categories](fnd06-bp02.md) 
+  [FND06-BP03 Configure billing and cost management tools](fnd06-bp03.md) 

 **Related documents:** 
+  [What is AWS Data Exports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) 
+  [AWS Cloud Financial Management](https://aws.amazon.com/aws-cost-management/) 
+  [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) 
+  [Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) 

 **Related examples:** 
+  [Data Exports for AWS Billing and Cost Management and Cost Management](https://aws.amazon.com/blogs/aws-cloud-financial-management/introducing-data-exports-for-billing-and-cost-management/) 
+  [Quick MoM Cost Analysis with Cost Comparison in AWS Cost Explorer](https://aws.amazon.com/blogs/aws-cloud-financial-management/quick-mom-cost-analysis-with-aws-cost-explorers-new-cost-comparison-feature/) 