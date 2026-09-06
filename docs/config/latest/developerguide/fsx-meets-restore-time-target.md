

# fsx-meets-restore-time-target
<a name="fsx-meets-restore-time-target"></a>

Checks if the restore time of Amazon FSx File Systems meets the specified duration. The rule is NON\_COMPLIANT if LatestRestoreExecutionTimeMinutes of an Amazon FSx File System is greater than maxRestoreTime minutes. 



**Identifier:** FSX\_MEETS\_RESTORE\_TIME\_TARGET

**Resource Types:** AWS::FSx::FileSystem

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

maxRestoreTimeType: int  
Numerical value for the maximum allowed restore runtime.

resourceTags (Optional)Type: String  
Tags of Amazon FSx File Systems for the rule to check, in JSON format.

resourceId (Optional)Type: String  
ID of Amazon FSx File System for the rule to check.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d857c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).