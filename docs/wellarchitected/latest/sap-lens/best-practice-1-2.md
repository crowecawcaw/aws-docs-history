# Best Practice 1.2 – Implement

infrastructure monitoring for SAP

Set up your infrastructure monitoring to provide information about supporting services
that are used to keep your SAP application running and supporting your users. Some examples
include CPU and memory utilization, storage and filesystem usage and performance (IOPS and
throughput), and network throughput. Include any dependent foundational services used by
SAP, such as on-premises Active Directory services, DNS, and third-party tools, such as high
availability (HA) and backup software. Evaluate AWS tools and SAP-specific tools from the
AWS Marketplace that can help correlate and visualize this information, such as DataDog,
Splunk, DynaTrace, and Avantra. Use this information to identify trends and determine when a
corrective action is required.

**Suggestion 1.2.1 - Implement CloudWatch metrics and alarms for
services supporting SAP**

Implement Amazon CloudWatch detailed monitoring metrics and thresholds with alarms for
all of your SAP systems. These metrics and alarms should include monitoring for common
problems which can affect SAP system availability and performance. Common infrastructure
monitoring areas focus on Amazon Elastic Compute Cloud (EC2) instances, Amazon Elastic
Block Storage (Amazon EBS) volumes, and Elastic Load Balancing (ELB).

Common monitoring items include the following:

- Amazon EC2 high CPU utilization
- Amazon EC2 high memory utilization
- Amazon EBS storage paging
- Amazon EBS storage throughput
- Amazon EBS storage IOPS
- Amazon EBS storage space free and volumes full %
- Amazon EC2 network saturation
- ELB/ALB health and target group health
  Base your alarm thresholds on healthy patterns of historical production usage of your
  system. Continually review and tweak your alarm thresholds to prevent problems.

Review the following resources to get started:

- SAP on AWS Blog: [Serverless Monitoring for SAP NetWeaver](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/")
- SAP on AWS Blog: [Serverless Monitoring for SAP HANA](https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/ "https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/")
- AWS Documentation: [Create a CloudWatch Custom Metric](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md")
- AWS Documentation: [Create a CloudWatch Dashboard](../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md")
- AWS Documentation: [Using CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")

**Suggestion 1.2.2 - Implement AWS service quota monitoring for SAP
services**

Implement a monitoring tool, such as Amazon CloudWatch, or other process to keep track of your
[AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") for required SAP resources in your landscape. Amazon EBS and
Amazon EC2 instance quotas are the most common quotas to affect a SAP workload.

For EC2 instance quotas, consider that SAP landscapes can often use a mix of Amazon EC2
instance types and that some types have a different [On-Demand service quota](../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md#ec2-on-demand-instances-limits "../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md#ec2-on-demand-instances-limits"). For example, the `x*` and `u*`
(High Memory) EC2 instance types have a different service quota that is separate from the
combined quota for standard types like `c6`, `m6`, and `r6`
instance families.

When planning new or scaling existing workloads, verify that your service quotas will
support this and engage Support if a quota increase is required.

- AWS Blog: [AWS Systems Manager Automation now enables monitoring of service usage quota in
  Amazon CloudWatch](https://aws.amazon.com/about-aws/whats-new/2022/01/aws-systems-manager-automation-usage-quota-amazon-cloudwatch/ "https://aws.amazon.com/about-aws/whats-new/2022/01/aws-systems-manager-automation-usage-quota-amazon-cloudwatch/")
- AWS Documentation: [Service
  Quotas - AWS General Reference](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
- AWS Documentation: [On-Demand Instances - Amazon Elastic Compute Cloud Service Quotas](../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md#ec2-on-demand-instances-limits "../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md#ec2-on-demand-instances-limits")
- AWS Documentation: [Requesting a quota increase - Service Quotas](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md")
