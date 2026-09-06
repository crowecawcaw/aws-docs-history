

# Monitoring GuardDuty Usage and Estimating Costs
<a name="monitoring_costs"></a>

GuardDuty provides usage metrics that track the processing of protection plans data sources logs/events and GuardDuty Runtime monitored VCPUs over time.

In this page:
+ [Amazon CloudWatch Usage Metrics](#cloudwatch_usage_metrics)
+ [Understanding GuardDuty Usage](#understanding_guardduty_usage)
+ [Estimating GuardDuty cost](#estimating_guardduty_cost)

## Amazon CloudWatch Usage Metrics
<a name="cloudwatch_usage_metrics"></a>

GuardDuty publishes usage metrics to Amazon CloudWatch, enabling you to:
+ Track actual usage over time
+ Create custom dashboards and alarms
+ Export usage data for cost estimation in AWS Pricing Calculator

GuardDuty usage metrics are published based on your account configuration:
+ All accounts (standalone, delegated administrator, and member accounts) receive individual account usage metrics in Amazon CloudWatch
+ Delegated administrator accounts additionally receive aggregated usage metrics for the entire organization

GuardDuty usage metrics are published in Amazon CloudWatch within 24 hours.

### Metric Details
<a name="guardduty_metric_details"></a>

GuardDuty publishes the following usage metrics `Hourly` to Amazon CloudWatch under the `AWS/GuardDuty` namespace:


|  |  |  |  |  | 
| --- |--- |--- |--- |--- |
| Protection Plan | Data Source | Metric Name | Unit | Description | 
| Foundational Threat Detection | CloudTrailEvents | AnalyzedCount | Count | Number of CloudTrail management events analyzed | 
| Foundational Threat Detection | VPCFlowLogDNSLogEvents | AnalyzedBytes | Bytes | Volume of VPC flow logs and DNS logs analyzed | 
| EKS Protection | KubernetesAuditLogs | AnalyzedCount | Count | Number of Amazon EKS audit log events analyzed | 
| S3 Protection | S3DataEvents | AnalyzedCount | Count | Number of S3 data events analyzed | 
| Runtime Monitoring | RuntimeMonitoringEC2 | MonitoredVcpuHours | Count (vCPU-Hours) | EC2 vCPU hours monitored by Runtime Monitoring | 
| Runtime Monitoring | RuntimeMonitoringEKS | MonitoredVcpuHours | Count (vCPU-Hours) | Amazon EKS vCPU hours monitored by Runtime Monitoring | 
| Runtime Monitoring | RuntimeMonitoringFargate | MonitoredVcpuHours | Count (vCPU-Hours) | Fargate vCPU hours monitored by Runtime Monitoring | 
| Malware Protection for EC2 | OnDemandEBSSnapshot | ScannedBytes | Bytes | Volume of on-demand EBS snapshot data scanned | 
| Malware Protection for EC2 | OnDemandEBSVolume | ScannedBytes | Bytes | Volume of on-demand EBS volume data scanned | 
| Malware Protection for EC2 | MalwareProtectionEBS | ScannedBytes | Bytes | Volume of EBS data scanned by Malware Protection | 
| RDS Protection | RDS | MonitoredAcuHours | Count (ACU-Hours) | Amazon RDS Aurora Capacity Units monitored | 
| RDS Protection | RDSLimitless | MonitoredAcuHours | Count (ACU-Hours) | Amazon RDS Aurora Limitless ACU hours monitored | 
| RDS Protection | AuroraScaleout | MonitoredAcuHours | Count (ACU-Hours) | Aurora Scaleout ACU hours monitored | 
| RDS Protection | RDS | MonitoredVcpuHours | Count (vCPU-Hours) | Amazon RDS vCPU hours monitored | 
| Lambda Protection | LambdaNetworkLogs | AnalyzedBytes | Bytes | Volume of Lambda network logs analyzed | 
| AI Protection | AIDataEvents | AnalyzedBytes | Bytes | Volume of AI data events analyzed | 

**Metrics Dimensions**
+ All accounts (standalone, delegated administrator, and member accounts): Metrics include the `AccountId` and `DataSource` dimensions.
+ Delegated administrator accounts: Metrics also include aggregated `DataSource` dimensions across all member accounts in the organization.

### Malware Protection for S3
<a name="malware_protection_s3"></a>

GuardDuty `Malware Protection for S3` protection plan publishes the following usage metrics to Amazon CloudWatch under the `AWS/GuardDuty/MalwareProtection` namespace:


|  |  |  | 
| --- |--- |--- |
| Metric Name | Unit | Description | 
| CompletedScanCount | Count | The number of S3 object malware scans that completed in a given time frame. | 
| FailedScanCount | Count | The number of S3 object malware scans that failed in a given time frame. | 
| SkippedScanCount | Count | The number of S3 object malware scans that were skipped in a given time frame. | 
| InfectedScanCount | Count | The number of S3 object malware scans that detected potentially malicious object in a given time frame. | 
| CompletedScanBytes | Count | The number of S3 object bytes scanned in a given time frame. | 

**Metrics Dimensions**
+ All metrics include `Malware Protection Plan Id, Resource Name` dimensions
+ SkippedScanCount metric includes `Skipped Reason` as an additional dimension

## Understanding GuardDuty Usage
<a name="understanding_guardduty_usage"></a>

### GuardDuty Event Processing
<a name="guardduty_event_processing"></a>

When enabled, GuardDuty automatically consumes events and logs directly from the log sources in your selected AWS Region. GuardDuty ingests events from separate, independent data sources to provide comprehensive security value.

**Important**  
Your individual service log configuration or filtering rules (for VPC Flow Logs, DNS Logs, CloudTrail Events, S3 Data Events, Kubernetes Audit Logs, and Lambda Network Logs) do not impact the logs/events processed by GuardDuty.

### GuardDuty VPC Flow Logs processing charges for instances monitored by GuardDuty Runtime Monitoring
<a name="vpc_flow_logs_runtime_monitoring"></a>

For instances monitored by GuardDuty Runtime Monitoring (via either EC2 Runtime agent or Amazon EKS Runtime agent), GuardDuty will not charge for VPC Flow Logs processing as long as the agent actively sends [runtime event data](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-collected-events.html). If the agent stops transmitting event data, GuardDuty reverts to charging via VPC Flow Logs.

Enabling Runtime Monitoring decreases VPC Flow Logs usage in GuardDuty Amazon CloudWatch usage metrics. Disabling Runtime Monitoring restores VPC Flow Logs usage.

## Estimating GuardDuty cost
<a name="estimating_guardduty_cost"></a>

GuardDuty offers a 30-day free trial per AWS account for most protection plans. During this trial period, you can:
+ Monitor your actual usage through GuardDuty Usage metrics
+ Estimate your monthly costs using AWS Pricing Calculator based on your observed usage patterns

The following protection plans include a 30-day free trial:
+ Foundational Threat Detection
+ S3 Protection
+ EKS Protection
+ Runtime Monitoring
+ RDS Protection
+ Lambda Protection
+ AI Protection
+ Malware Protection for EC2 (only for GuardDuty-initiated scans when enabled with Foundational Threat Detection)

### Using AWS Pricing Calculator
<a name="using_pricing_calculator"></a>

You can use the [AWS Pricing Calculator](https://aws.amazon.com/calculator/) to estimate your monthly GuardDuty costs based on your observed usage patterns. To create an estimate for GuardDuty:

1. Open the [AWS Pricing Calculator](https://aws.amazon.com/calculator/).

1. Choose **Create estimate**.

1. On the **Add service** page, search for **Amazon GuardDuty** and choose **Configure**.

1. Select the AWS Region where GuardDuty is enabled.

1. In the **Service settings** section, enter your estimated usage for each protection plan based on the usage metrics observed in Amazon CloudWatch or the GuardDuty console.

1. Choose **Add to my estimate** to view the projected monthly cost.

**Note**  
Some GuardDuty usage metrics are reported in bytes. When entering values in the AWS Pricing Calculator, you may need to convert bytes to the appropriate unit (MB, GB, or TB). Use the following conversions:  
1 MB = 1,048,576 bytes
1 GB = 1,073,741,824 bytes
1 TB = 1,099,511,627,776 bytes

### Security Hub Customers
<a name="security_hub_customers"></a>

Security Hub offers a simplified pricing model for GuardDuty Threat Detection with its add-on Threat Analytics plan, consolidating metering of multiple GuardDuty DataSources. When using Security Hub Threat Analytics plan (Security Hub with GuardDuty):
+ Multiple GuardDuty DataSources are consolidated
+ Notably, for simplicity, Amazon EKS Audit Logs events and S3 Data events are converted to GB using a fixed conversion rate

To create Security Hub cost estimate, please refer to [AWS Security Hub Documentation](https://docs.aws.amazon.com/securityhub/).

**Note:** GuardDuty's 30-day free trial status is independent of Security Hub integration. Enabling or disabling Security Hub:
+ Does not grant a new free trial if you've already used GuardDuty's trial period
+ Does not interrupt or restart an ongoing free trial
+ Does not extend existing trial periods