# backup-plan-min-frequency-and-min-retention-check

Checks if a backup plan has a backup rule that satisfies the required frequency and retention period. The rule is NON_COMPLIANT if recovery points are not created at least as often as the specified frequency or expire before the specified period.

**Identifier:** BACKUP_PLAN_MIN_FREQUENCY_AND_MIN_RETENTION_CHECK

**Resource Types:** AWS::Backup::BackupPlan

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

requiredFrequencyValue (Optional)
Type: int
Default: 1

Numerical value for required backup frequency. Maximum of 24 for hours, 31 for days.

requiredRetentionDays (Optional)
Type: int
Default: 35

Required retention period in days.

requiredFrequencyUnit (Optional)
Type: String
Default: days

Unit of time for required backup frequency. Accepted values: 'hours', 'days'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
