# ADVSUS02-BP02 Identify redundant infrastructure and unnecessary data movement to reduce usage where possible

Identify and eliminate redundant infrastructure components and
unnecessary data movement within your advertising workloads, as
this can help reduce resource usage, lower the overall carbon
footprint, and improve sustainability-related key performance
indicators (KPIs).

## Implementation guidance

- Audit your advertising workload infrastructure to identify
  any redundant or underutilized resources, such as idle
  instances, oversized instances, or unnecessary data
  replication.
- Analyze data movement patterns and network traffic to
  identify opportunities for reducing data transfers,
  especially over long distances or between regions. Use
  Amazon CloudFront to cache and serve ad files closer to
  consumers.
- Implement auto scaling and right-sizing mechanisms to
  automatically adjust resource allocation based on actual
  workload demands, minimizing over-provisioning. For example,
  with real-time bidding workloads that use Amazon EKS,
  implement a scaling policy that is determined by the number
  of bids being served, which optimizes resource usage.
- Consolidate workloads and data storage where possible,
  reducing the overall infrastructure footprint and associated
  energy consumption. Implement lifecycle policies to remove
  old ad file assets that are no longer needed.
- Establish monitoring and reporting processes to track
  resource utilization, data movement, and sustainability KPIs
  over time, enabling continuous optimization.

## Key AWS services

- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/") (Identify optimization opportunities)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/") (Visualizes and analyzes cost/usage
  data)
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") (Monitors and records resource configurations)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/") (Cache and serve ad files)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") (Logs API calls and events)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/") (Automatically scales resources)
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") (Serverless computing)
- [AWS Data Transfer Cost Estimator](https://calculator.aws/#/createCalculator/DataTransfer "https://calculator.aws/#/createCalculator/DataTransfer") (Estimates data transfer
  costs)
- [Amazon S3 Lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") (Remove unneeded ad assets)
- [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/ "https://aws.amazon.com/well-architected-tool/") (Provides architecture best
  practices)
