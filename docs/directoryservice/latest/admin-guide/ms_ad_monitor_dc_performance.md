# Using CloudWatch to monitor the performance of your AWS Managed Microsoft AD domain controllers

AWS Directory Service integrates with Amazon CloudWatch to help provide you with important performance metrics for
each domain controller in your Active Directory. This means that you can monitor domain controller
performance counters, such as CPU and memory utilization. You can also configure alarms and
initiate automated actions to respond to periods of high utilization. For example, you can
configure an alarm for domain controller CPU utilization above 70 percent and create an SNS
topic to notify you when this occurs. You can use this SNS topic to initiate automation, such as
AWS Lambda functions, to increase the number of domain controllers to your Active Directory.

For more information about monitoring your domain controllers, see [Determining when to add domain controllers with CloudWatch metrics](#scaledcs "#scaledcs").

There are fees associated with Amazon CloudWatch. For more information, see [CloudWatch
billing and cost](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_billing.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_billing.md").

###### Important

Domain controller performance metrics with CloudWatch is unavailable in the
Canada West (Calgary) Region.

To enable CloudWatch, see [Enabling Amazon CloudWatch Logs log forwarding for
AWS Managed Microsoft AD](ms_ad_enable_log_forwarding.md "ms_ad_enable_log_forwarding.md").

## Finding domain controllers performance metrics in

CloudWatch

In the Amazon CloudWatch console, metrics for a given service are grouped first by the service's
namespace. You can add metric filters that are subordinate to that namespace. Use the
following procedure to locate the correct namespace and subordinate metric that is required to
set up AWS Managed Microsoft AD domain controller metrics in CloudWatch.

###### To find domain controller metrics in the CloudWatch console

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. From the list of metrics, select the **Directory Service** namespace,
   and then from the list, select the **AWS Managed Microsoft AD** metric.

For instructions on how to set up domain controller metrics using the CloudWatch console, see
[How to automate AWS Managed Microsoft AD scaling based on utilization metrics](https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/ "https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/") in the AWS
Security Blog.

## Determining when to add domain controllers with CloudWatch metrics

Load balancing across all of your domain controllers is important for the resilience and
performance of your Active Directory. To help you optimize the performance of your domain controllers in
AWS Managed Microsoft AD, we recommend that you first monitor important metrics in CloudWatch to form a
baseline. During this process, you analyze your Active Directory over time to identify your average and
peak Active Directory utilization. After determining your baseline, you can monitor these metrics on a
regular basis to help determine when to add a domain controller to your Active Directory.

The following metrics are important to monitor on a regular basis. For a full list of
available domain controller metrics in CloudWatch, see [AWS Managed Microsoft AD performance counters](#performance-counters "#performance-counters").

- Domain controller-specific metrics, such as:
  - Processor
  - Memory
  - Logical Disk
  - Network Interface

- AWS Managed Microsoft AD directory-specific metrics, such as:
  - LDAP searches
  - Binds
  - DNS queries
  - Directory reads
  - Directory writes

For instructions on how to set up domain controller metrics using the CloudWatch console, see
[How to automate AWS Managed Microsoft AD scaling based on utilization metrics](https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/ "https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/") in the AWS
Security Blog. For general information about metrics in CloudWatch, see [Using Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") in the _Amazon CloudWatch User Guide_.

For general information about domain controller planning, see [Capacity planning for Active Directory Domain Services](https://docs.microsoft.com/en-us/windows-server/administration/performance-tuning/role/active-directory-server/capacity-planning-for-active-directory-domain-services "https://docs.microsoft.com/en-us/windows-server/administration/performance-tuning/role/active-directory-server/capacity-planning-for-active-directory-domain-services") on the Microsoft website.

## AWS Managed Microsoft AD performance counters

The following table lists all performance counters available in Amazon CloudWatch for tracking
domain controller and directory performance in AWS Managed Microsoft AD.

| Metric category                              | Metric name               |
| -------------------------------------------- | ------------------------- | ---------------------------------------- |
| Database ==> Instances (NTDSA)               | Database Cache % Hit      |
| I/O Database Reads Average Latency           |                           | I/O Database Reads/sec                   |
| I/O Log Writes Average Latency               |
| DirectoryServices (NTDS)                     | LDAP Bind Time            |
| DRA Pending Replication Operations           |                           | DRA Pending Replication Synchronizations |
| DNS                                          | Recursive Queries/sec     |
| Recursive Query Failure/sec                  |                           | TCP Query Received/sec                   |
| Total Query Received/sec                     |                           | Total Response Sent/sec                  |
| UDP Query Received/sec                       |
| LogicalDisk                                  | Avg. Disk Queue Length    |
| % Free Space                                 |
| Memory                                       | % Committed Bytes in Use  |
| Long-Term Average Standby Cache Lifetime (s) |
| Network Interface                            | Bytes Sent/sec            |
| Bytes Received/sec                           |                           | Current Bandwidth                        |
| NTDS                                         | ATQ Estimated Queue Delay |
| ATQ Request Latency                          |                           | DS Directory Reads/Sec                   |
| DS Directory Searches/Sec                    |                           | DS Directory Writes/Sec                  |
| LDAP Client Sessions                         |                           | LDAP Searches/sec                        |
| LDAP Successful Binds/sec                    |
| Processor                                    | % Processor Time          |
| Security System-Wide Statistics              | Kerberos Authentications  |
| NTLM Authentications                         |
