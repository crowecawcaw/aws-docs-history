# cloudwatch-alarm-settings-check

Checks whether CloudWatch alarms with the given metric name have the specified settings.

**Identifier:** CLOUDWATCH_ALARM_SETTINGS_CHECK

**Resource Types:** AWS::CloudWatch::Alarm

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

metricName
Type: String

The name for the metric associated with the alarm.

threshold (Optional)
Type: int

The value against which the specified statistic is compared.

evaluationPeriods (Optional)
Type: int

The number of periods over which data is compared to the specified threshold.

period (Optional)
Type: int
Default: 300

The period, in seconds, during which the specified statistic is applied.

comparisonOperator (Optional)
Type: String

The operation for comparing the specified statistic and threshold (for example, 'GreaterThanThreshold').

statistic (Optional)
Type: String

The statistic for the metric associated with the alarm (for example, 'Average' or 'Sum').

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
