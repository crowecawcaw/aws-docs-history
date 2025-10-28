# `AWS-EnableCWAlarm`

**Description**

The `AWS-EnableCWAlarm` runbook creates Amazon CloudWatch (CloudWatch) alarms for AWS resources in your AWS account that do not already have one. CloudWatch alarms are created for the following AWS resources:

- Amazon Elastic Compute Cloud (Amazon EC2) instances
- Amazon Elastic Block Store (Amazon EBS) volumes
- Amazon Simple Storage Service (Amazon S3) buckets
- Amazon Relational Database Service (Amazon RDS) clusters
  [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCWAlarm "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCWAlarm")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- ComparisonOperator

Type: String

Valid values: GreaterThanOrEqualToThreshold | GreaterThanThreshold | GreaterThanUpperThreshold | LessThanLowerOrGreaterThanUpperThreshol | LessThanLowerThreshold | LessThanOrEqualToThreshold | LessThanThreshold

Description: (Required) The arithmetic operation to use when comparing the specified statistic and threshold.

- MetricName

Type: String

Description: (Required) The name for the metric associated with the alarm.

- Period

Type: Integer

Valid values: 10 | 30 | 60 | A multiple of 60

Description: (Required) The period, in seconds, over which the statistic is applied.

- ResourceARNs

Type: StringList

Description: (Required) A comma separated list of ARNs of the resources to create a CloudWatch alarm for

- Statistic

Type: String

Valid values: Average | Maximum | Minimum | SampleCount | Sum

Description: (Required) The statistic for the metric associated with the alarm.

- Threshold

Type: Integer

Description: (Required) The value to compare with the specified statistic.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudwatch:PutMetricAlarm`
  **Document Steps**

- `aws:executeScript` - Creates a CloudWatch alarm according to the values specified in the runbook parameters for the resources you specify in the `ResourceARNs` parameter .
  **Outputs**

EnableCWAlarm.FailedResources: A maplist of resource ARNs for which a CloudWatch alarm was not created and the reason for the failure.

EnableCWAlarm.SuccessfulResources: A list of resource ARNs for which a CloudWatch alarm was successfully created.
