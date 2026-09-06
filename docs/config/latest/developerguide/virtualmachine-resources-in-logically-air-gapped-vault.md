

# virtualmachine-resources-in-logically-air-gapped-vault
<a name="virtualmachine-resources-in-logically-air-gapped-vault"></a>

Checks if AWS Backup-Gateway VirtualMachines are in a logically air-gapped vault. The rule is NON\_COMPLIANT if an AWS Backup-Gateway VirtualMachines is not in a logically air-gapped vault within the specified time period. 



**Identifier:** VIRTUALMACHINE\_RESOURCES\_IN\_LOGICALLY\_AIR\_GAPPED\_VAULT

**Resource Types:** AWS::BackupGateway::VirtualMachine

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

resourceTags (Optional)Type: String  
Tags of AWS Backup-Gateway VirtualMachines for the rule to check, in JSON format.

resourceId (Optional)Type: String  
ID of AWS Backup-Gateway VirtualMachine for the rule to check.

recoveryPointAgeValue (Optional)Type: intDefault: 1  
Numerical value for maximum allowed age. No more than 2184 for hours, 91 for days.

recoveryPointAgeUnit (Optional)Type: StringDefault: days  
Unit of time for maximum allowed age. Accepted values: 'hours', 'days'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1595c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).