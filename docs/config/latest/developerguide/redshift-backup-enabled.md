# redshift-backup-enabled

Checks that Amazon Redshift automated snapshots are enabled for clusters.
The rule is NON_COMPLIANT if the value for `automatedSnapshotRetentionPeriod` is greater than `MaxRetentionPeriod` or
less than `MinRetentionPeriod` or the value is 0.

**Identifier:** REDSHIFT_BACKUP_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), AWS Secret - West, Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

MinRetentionPeriod (Optional)
Type: int

Minimum value for the retention period. Minimum value is 1.

MaxRetentionPeriod (Optional)
Type: int

Maximum value for the retention period. Maximum value is 35.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
