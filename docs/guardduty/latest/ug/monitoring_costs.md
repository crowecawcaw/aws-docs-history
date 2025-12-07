# Monitoring GuardDuty Usage and Estimating Costs

GuardDuty provides usage metrics that track the processing of protection plans data sources logs/events and GuardDuty Runtime monitored VCPUs over time.

In this page:

- [Amazon CloudWatch Usage Metrics](#cloudwatch_usage_metrics "#cloudwatch_usage_metrics")
- [Understanding GuardDuty Usage](#understanding_guardduty_usage "#understanding_guardduty_usage")
- [Estimating GuardDuty cost](#estimating_guardduty_cost "#estimating_guardduty_cost")

## Amazon CloudWatch Usage Metrics

GuardDuty publishes usage metrics to Amazon Amazon CloudWatch, enabling you to:

- Track actual usage over time
- Create custom dashboards and alarms
- Export usage data for cost estimation in AWS Cost Calculator

GuardDuty usage metrics are published based on your account configuration:

- For standalone accounts (not part of an organization), you can view your account usage metrics in Amazon CloudWatch
- For accounts that are part of an organization, metrics are published to the delegated administrator account (organization's GuardDuty administrator), presenting aggregated usage for the entire organization

GuardDuty usage metrics are published in Amazon CloudWatch within 24 hours.

### Metric Details

GuardDuty publishes the following usage metrics `Hourly` to Amazon CloudWatch under the `AWS/GuardDuty` namespace:

|                               |                          |                    |                    |                                                       |
| ----------------------------- | ------------------------ | ------------------ | ------------------ | ----------------------------------------------------- |
| **Protection Plan**           | **Data Source**          | **Metric Name**    | **Unit**           | **Description**                                       |
| Foundational Threat Detection | CloudTrailEvents         | AnalyzedCount      | Count              | Number of CloudTrail management events analyzed       |
| Foundational Threat Detection | VPCFlowLogDNSLogEvents   | AnalyzedBytes      | Bytes              | Volume of VPC flow logs and DNS logs analyzed         |
| S3 Protection                 | S3DataEvents             | AnalyzedCount      | Count              | Number of S3 data events analyzed                     |
| Amazon EKS Protection         | KubernetesAuditLogs      | AnalyzedCount      | Count              | Number of Amazon EKS audit log events analyzed        |
| Lambda Protection             | LambdaNetworkLogs        | AnalyzedBytes      | Bytes              | Volume of Lambda network logs analyzed                |
| Runtime Monitoring            | RuntimeMonitoringEC2     | MonitoredVcpuHours | Count (vCPU-Hours) | EC2 vCPU hours monitored by Runtime Monitoring        |
| Runtime Monitoring            | RuntimeMonitoringEKS     | MonitoredVcpuHours | Count (vCPU-Hours) | Amazon EKS vCPU hours monitored by Runtime Monitoring |
| Runtime Monitoring            | RuntimeMonitoringFargate | MonitoredVcpuHours | Count (vCPU-Hours) | Fargate vCPU hours monitored by Runtime Monitoring    |
| Malware Protection for EC2    | OnDemandEBSSnapshot      | ScannedBytes       | Bytes              | Volume of on-demand EBS snapshot data scanned         |
| Malware Protection for EC2    | OnDemandEBSVolume        | ScannedBytes       | Bytes              | Volume of on-demand EBS volume data scanned           |
| Malware Protection for EC2    | MalwareProtectionEBS     | ScannedBytes       | Bytes              | Volume of EBS data scanned by Malware Protection      |
| Amazon RDS Protection         | RDS                      | MonitoredAcuHours  | Count (ACU-Hours)  | Amazon RDS Aurora Capacity Units monitored            |
| Amazon RDS Protection         | RDSLimitless             | MonitoredAcuHours  | Count (ACU-Hours)  | Amazon RDS Aurora Limitless ACU hours monitored       |
| Amazon RDS Protection         | AuroraScaleout           | MonitoredAcuHours  | Count (ACU-Hours)  | Aurora Scaleout ACU hours monitored                   |
| Amazon RDS Protection         | RDS                      | MonitoredVcpuHours | Count (vCPU-Hours) | Amazon RDS vCPU hours monitored                       |

**Metrics Dimensions**

- Standalone GuardDuty accounts: Metrics include `AccountId, DataSource` dimensions
- Organization-level (Delegated Administrator): Metrics include `DataSource` dimension

### Malware Protection for S3

GuardDuty `Malware Protection for S3` protection plan publishes the following usage metrics to Amazon CloudWatch under the `AWS/GuardDuty/MalwareProtection` namespace:

|                    |          |                                                                                                         |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------- |
| **Metric Name**    | **Unit** | **Description**                                                                                         |
| CompletedScanCount | Count    | The number of S3 object malware scans that completed in a given time frame.                             |
| FailedScanCount    | Count    | The number of S3 object malware scans that failed in a given time frame.                                |
| SkippedScanCount   | Count    | The number of S3 object malware scans that were skipped in a given time frame.                          |
| InfectedScanCount  | Count    | The number of S3 object malware scans that detected potentially malicious object in a given time frame. |
| CompletedScanBytes | Count    | The number of S3 object bytes scanned in a given time frame.                                            |

**Metrics Dimensions**

- All metrics include `Malware Protection Plan Id, Resource Name` dimensions
- SkippedScanCount metric includes `Skipped Reason` as an additional dimension

## Understanding GuardDuty Usage

### GuardDuty Event Processing

When enabled, GuardDuty automatically consumes events and logs directly from the log sources in your selected AWS Region. GuardDuty ingests events from separate, independent data sources to provide comprehensive security value.

###### Important

Your individual service log configuration or filtering rules (for VPC Flow Logs, DNS Logs, CloudTrail Events, S3 Data Events, Kubernetes Audit Logs, and Lambda Network Logs) do not impact the logs/events processed by GuardDuty.

### GuardDuty VPC Flow Logs processing charges for instances monitored by GuardDuty Runtime Monitoring

For instances monitored by GuardDuty Runtime Monitoring (via either EC2 Runtime agent or Amazon EKS Runtime agent), GuardDuty will not charge for VPC Flow Logs processing as long as the agent actively sends [runtime event data](runtime-monitoring-collected-events.md "runtime-monitoring-collected-events.md"). If the agent stops transmitting event data, GuardDuty reverts to charging via VPC Flow Logs.

Enabling Runtime Monitoring decreases VPC Flow Logs usage in GuardDuty Amazon CloudWatch usage metrics. Disabling Runtime Monitoring restores VPC Flow Logs usage.

## Estimating GuardDuty cost

GuardDuty offers a 30-day free trial per AWS account for most protection plans. During this trial period, you can:

- Monitor your actual usage through GuardDuty Usage metrics
- Estimate your monthly costs using AWS Pricing Calculator based on your observed usage patterns

The following protection plans include a 30-day free trial:

- Foundational GuardDuty
- GuardDuty S3 Protection
- GuardDuty Amazon EKS Protection
- GuardDuty Runtime Monitoring
- GuardDuty Amazon RDS Protection
- GuardDuty Lambda Protection
- GuardDuty Malware Protection for EC2 (only for GuardDuty-initiated scans when enabled with Foundational GuardDuty)

### Security Hub Customers

Security Hub offers a simplified pricing model for GuardDuty Threat Detection with its add-on Threat Analytics plan, consolidating metering of multiple GuardDuty DataSources. When using Security Hub Threat Analytics plan (Security Hub with GuardDuty):

- Multiple GuardDuty DataSources are consolidated
- Notably, for simplicity, Amazon EKS Audit Logs events and S3 Data events are converted to GB using a fixed conversion rate

To create Security Hub cost estimate, please refer to [AWS Security Hub Documentation](../../../securityhub.md "../../../securityhub.md").

**Note:** GuardDuty's 30-day free trial status is independent of Security Hub integration. Enabling or disabling Security Hub:

- Does not grant a new free trial if you've already used GuardDuty's trial period
- Does not interrupt or restart an ongoing free trial
- Does not extend existing trial periods
