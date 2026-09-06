

# db-instance-backup-enabled
<a name="db-instance-backup-enabled"></a>

Checks if RDS DB instances have backups enabled. Optionally, the rule checks the backup retention period and the backup window.



**Identifier:** DB\_INSTANCE\_BACKUP\_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

backupRetentionMinimum (Optional)Type: int  
Minimum retention period for backups.

backupRetentionPeriod (Optional)Type: int  
Retention period for backups.

checkReadReplicas (Optional)Type: boolean  
Checks whether RDS DB instances have backups enabled for read replicas.

preferredBackupWindow (Optional)Type: String  
Time range in which backups are created.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d451c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).