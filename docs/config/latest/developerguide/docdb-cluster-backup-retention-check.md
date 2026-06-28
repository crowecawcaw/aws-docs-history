# docdb-cluster-backup-retention-check

Checks if an Amazon Document DB cluster retention period is set to specific number of days. The rule is NON\_COMPLIANT if the retention period is less than the value specified by the parameter.

**Identifier:** DOCDB\_CLUSTER\_BACKUP\_RETENTION\_CHECK

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Europe (Milan), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central), China (Ningxia) Region

**Parameters:**

minimumBackupRetentionPeriod (Optional)
Type: int

Minimum days backups should be kept. Valid values 1 to 35, default value is 7. This rule is NON\_COMPLIANT if value is greater than 'backupRetentionPeriod'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
