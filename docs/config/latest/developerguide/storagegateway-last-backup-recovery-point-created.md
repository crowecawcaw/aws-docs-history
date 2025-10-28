# storagegateway-last-backup-recovery-point-created

Checks if a recovery point was created for AWS Storage Gateway volumes. The rule is NON_COMPLIANT if the Storage Gateway volume does not have a corresponding recovery point created within the specified time period.

**Identifier:** STORAGEGATEWAY_LAST_BACKUP_RECOVERY_POINT_CREATED

**Resource Types:** AWS::StorageGateway::Volume

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

resourceTags (Optional)
Type: String

Tags of Storage Gateway volumes for the rule to check, in JSON format `{"tagkey" : "tagValue"}`.

resourceId (Optional)
Type: String

ID of Storage Gateway volume for the rule to check.

recoveryPointAgeValue (Optional)
Type: int
Default: 1

Numerical value for maximum allowed age. No more than 744 for hours, 31 for days.

recoveryPointAgeUnit (Optional)
Type: String
Default: days

Unit of time for maximum allowed age. Accepted values: 'hours', 'days'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
