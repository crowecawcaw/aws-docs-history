

# s3-last-backup-recovery-point-created
<a name="s3-last-backup-recovery-point-created"></a>

Checks if a recovery point was created for Amazon Simple Storage Service (Amazon S3). The rule is NON\_COMPLIANT if the Amazon S3 bucket does not have a corresponding recovery point created within the specified time period. 



**Identifier:** S3\_LAST\_BACKUP\_RECOVERY\_POINT\_CREATED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

recoveryPointAgeUnit (Optional)Type: StringDefault: days  
Unit of time for maximum allowed age. Accepted values: 'hours', 'days'.

recoveryPointAgeValue (Optional)Type: intDefault: 1  
Numerical value for maximum allowed age. No more than 744 for hours, 31 for days.

resourceId (Optional)Type: String  
Name of Amazon S3 bucket for the rule to check.

resourceTags (Optional)Type: String  
Tags of Amazon S3 bucket for the rule to check, in JSON format `{"tagkey" : "tagValue"}`.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1455c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).