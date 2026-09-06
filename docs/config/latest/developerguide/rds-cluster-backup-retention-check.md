

# rds-cluster-backup-retention-check
<a name="rds-cluster-backup-retention-check"></a>

Checks if an Amazon RDS cluster automated backup retention period is set to a specific number of days. The rule is NON\_COMPLIANT if the retention period is less than the value specified by the parameter. The default value is 7 days. 



**Identifier:** RDS\_CLUSTER\_BACKUP\_RETENTION\_CHECK

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

minimumBackupRetentionPeriod (Optional)Type: intDefault: 7  
The minimum backup retention period in days for the rule to check. The rule is NON\_COMPLIANT if the backup retention period is less than the value specified in this parameter. Valid values are 1 to 35. The default value is 7.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1223c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).