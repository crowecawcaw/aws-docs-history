# cloudwatch-alarm-settings-check

Checks whether CloudWatch alarms with the given metric name have the specified settings.

**Identifier:** CLOUDWATCH_ALARM_SETTINGS_CHECK

**Resource Types:** AWS::CloudWatch::Alarm

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

metricName
Type: String

The name for the metric associated with the alarm.

period (Optional)
Type: int
Default: 300

The period, in seconds, during which the specified statistic is applied.

statistic (Optional)
Type: String

The statistic for the metric associated with the alarm (for example, 'Average' or 'Sum').

comparisonOperator (Optional)
Type: String

The operation for comparing the specified statistic and threshold (for example, 'GreaterThanThreshold').

threshold (Optional)
Type: int

The value against which the specified statistic is compared.

evaluationPeriods (Optional)
Type: int

The number of periods over which data is compared to the specified threshold.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
