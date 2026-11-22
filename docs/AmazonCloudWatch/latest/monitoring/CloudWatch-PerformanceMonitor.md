

# Using Performance Monitor

Performance Monitor monitors the traffic of the VPCs that you select to determine whether the AWS network is causing issues for your workloads. Performance Monitor measures network degradation across paths between Availability Zones, across Regions, and to AWS services such as Amazon S3 and Amazon DynamoDB.

Performance Monitor uses an impact score, which maps to an impact level of None, Low, Medium, or High, to help you quickly identify which network paths are experiencing degradation.

You can view network performance information for paths in a single account. Or, to view performance information for multiple accounts in an organization, configure Performance Monitor with AWS Organizations and sign in with a management account or delegated administrator account.

Performance Monitor is intended for network operators and application developers who want visibility into AWS network health affecting their workloads. In the Performance Monitor console in Amazon CloudWatch, you can see impact scores and latency data for network paths grouped by Availability Zone pairs, with the ability to drill down into subnet-level flows. You can create monitors for specific VPCs that you want to track over time.

Using a monitor, you can quickly visualize which network paths are experiencing degradation, review latency trends, and understand the blast radius of network events.

Performance Monitor offers two complementary views of network health:
+ **Infrastructure Performance** – Shows AWS backbone network health between AWS Regions and Availability Zones, independent of any specific VPC. Use it to check whether general AWS network performance is affecting your applications. You can also use it to compare Regions before you deploy new workloads.
+ **Monitors** – Track the network paths that your VPC traffic uses. Create a monitor for the VPCs that you want to track. You can then follow impact scores and latency for those paths over time.

For more information about Infrastructure Performance, see [Monitor the AWS backbone with Infrastructure Performance](CloudWatch-PerformanceMonitor-infrastructure-performance.md).

**Topics**
+ [What is Performance Monitor?](CloudWatch-PerformanceMonitor-What-is.md)
+ [Get started](CloudWatch-PerformanceMonitor-get-started.md)
+ [API operations](CloudWatch-PerformanceMonitor-API-operations.md)
+ [Examples with the AWS CLI](CloudWatch-PerformanceMonitor-CLI.md)
+ [Initialize Performance Monitor](CloudWatch-PerformanceMonitor-initialize.md)
+ [Monitor network paths](CloudWatch-PerformanceMonitor-paths.md)
+ [Delete scope](CloudWatch-PerformanceMonitor-scope-delete.md)
+ [View CloudWatch metrics](CloudWatch-PerformanceMonitor-cw-metrics.md)
+ [Create alarms](CloudWatch-PerformanceMonitor-create-alarm.md)
+ [CloudTrail](CloudWatch-PerformanceMonitor-monitoring-overview.md)
+ [Troubleshoot issues](CloudWatch-PerformanceMonitor-troubleshooting.md)
+ [Security](CloudWatch-PerformanceMonitor-security.md)
+ [Infrastructure Performance](CloudWatch-PerformanceMonitor-infrastructure-performance.md)