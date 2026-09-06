

# efs-last-backup-recovery-point-created
<a name="efs-last-backup-recovery-point-created"></a>

Checks if a recovery point was created for Amazon Elastic File System (Amazon EFS) File Systems. The rule is NON\_COMPLIANT if the Amazon EFS File System does not have a corresponding Recovery Point created within the specified time period. 



**Identifier:** EFS\_LAST\_BACKUP\_RECOVERY\_POINT\_CREATED

**Resource Types:** AWS::EFS::FileSystem

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

resourceTags (Optional)Type: String  
Tags of Amazon EFS File Systems for the rule to check, in JSON format `{"tagkey" : "tagValue"}`.

resourceId (Optional)Type: String  
ID of EFS File System for the rule to check.

recoveryPointAgeValue (Optional)Type: intDefault: 1  
Numerical value for maximum allowed age. No more than 744 for hours, 31 for days.

recoveryPointAgeUnit (Optional)Type: StringDefault: days  
Unit of time for maximum allowed age. Accepted values: 'hours', 'days'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d705c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).