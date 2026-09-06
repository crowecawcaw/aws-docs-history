

# efs-resources-in-logically-air-gapped-vault
<a name="efs-resources-in-logically-air-gapped-vault"></a>

Checks if Amazon Elastic File System (Amazon EFS) File Systems are in a logically air-gapped vault. The rule is NON\_COMPLIANT if an Amazon EFS File System is not in a logically air-gapped vault within the specified time period. 



**Identifier:** EFS\_RESOURCES\_IN\_LOGICALLY\_AIR\_GAPPED\_VAULT

**Resource Types:** AWS::EFS::FileSystem

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

resourceTags (Optional)Type: String  
Tags of Amazon EFS File Systems for the rule to check, in JSON format.

resourceId (Optional)Type: String  
ID of EFS File System for the rule to check.

recoveryPointAgeValue (Optional)Type: intDefault: 1  
Numerical value for maximum allowed age. No more than 2184 for hours, 91 for days.

recoveryPointAgeUnit (Optional)Type: StringDefault: days  
Unit of time for maximum allowed age. Accepted values: 'hours', 'days'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d711c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).