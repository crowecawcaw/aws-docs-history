# db-instance-backup-enabled

Checks if RDS DB instances have backups enabled. Optionally, the rule checks the backup retention period and the backup window.

**Identifier:** DB_INSTANCE_BACKUP_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

backupRetentionMinimum (Optional)
Type: int

Minimum retention period for backups.

backupRetentionPeriod (Optional)
Type: int

Retention period for backups.

checkReadReplicas (Optional)
Type: boolean

Checks whether RDS DB instances have backups enabled for read replicas.

preferredBackupWindow (Optional)
Type: String

Time range in which backups are created.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
