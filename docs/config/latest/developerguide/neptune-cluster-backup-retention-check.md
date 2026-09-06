

# neptune-cluster-backup-retention-check
<a name="neptune-cluster-backup-retention-check"></a>

Checks if an Amazon Neptune DB cluster retention period is set to specific number of days. The rule is NON\_COMPLIANT if the retention period is less than the value specified by the parameter. 



**Identifier:** NEPTUNE\_CLUSTER\_BACKUP\_RETENTION\_CHECK

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

minimumBackupRetentionPeriod (Optional)Type: int  
Minimum days backups should be kept. Valid values 1 to 35, default value is 7. The rule is NON\_COMPLIANT if value is greater than 'backupRetentionPeriod'. The rule is COMPLIANT if value is less than or equal to 'backupRetentionPeriod'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1139c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).