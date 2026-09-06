

# backup-recovery-point-minimum-retention-check
<a name="backup-recovery-point-minimum-retention-check"></a>

Checks if a recovery point expires no earlier than after the specified period. The rule is NON\_COMPLIANT if the recovery point has a retention point that is less than the required retention period. 



**Identifier:** BACKUP\_RECOVERY\_POINT\_MINIMUM\_RETENTION\_CHECK

**Resource Types:** AWS::Backup::RecoveryPoint

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

requiredRetentionDays (Optional)Type: intDefault: 35  
Required retention period in days.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d253c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).