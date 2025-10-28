# cw-loggroup-retention-period-check

Checks if an Amazon CloudWatch LogGroup retention period is set to greater than 365 days or else a specified retention period. The rule is NON_COMPLIANT if the retention period is less than `MinRetentionTime`, if specified, or else 365 days.

###### Note

If the retention setting is "Never expire" for a log group, the rule is marked as COMPLIANT.

**Identifier:** CW_LOGGROUP_RETENTION_PERIOD_CHECK

**Resource Types:** AWS::Logs::LogGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (UAE) Region

**Parameters:**

LogGroupNames (Optional)
Type: CSV

A comma-separated list of Log Group names to check the retention period.

MinRetentionTime (Optional)
Type: int

Specify the retention time in days. Valid values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653. The default retention period is 365 days.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
