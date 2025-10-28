# virtualmachine-last-backup-recovery-point-created

Checks if a recovery point was created for AWS Backup-Gateway VirtualMachines. The rule is NON_COMPLIANT if an AWS Backup-Gateway VirtualMachines does not have a corresponding recovery point created within the specified time period.

**Identifier:** VIRTUALMACHINE_LAST_BACKUP_RECOVERY_POINT_CREATED

**Resource Types:** AWS::BackupGateway::VirtualMachine

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

resourceTags (Optional)
Type: String

Tags of AWS Backup-Gateway VirtualMachines for the rule to check, in JSON format `{"tagkey" : "tagValue"}`.

resourceId (Optional)
Type: String

ID of AWS Backup-Gateway VirtualMachine for the rule to check.

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
