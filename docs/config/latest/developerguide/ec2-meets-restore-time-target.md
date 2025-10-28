# ec2-meets-restore-time-target

Checks if the restore time of Amazon Elastic Compute Cloud (Amazon EC2) instances meets the specified duration. The rule is NON_COMPLIANT if LatestRestoreExecutionTimeMinutes of an Amazon EC2 instance is greater than maxRestoreTime minutes.

**Identifier:** EC2_MEETS_RESTORE_TIME_TARGET

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

maxRestoreTime
Type: int

Numerical value for the maximum allowed restore runtime.

resourceTags (Optional)
Type: String

Tags of Amazon EC2 instances for the rule to check, in JSON format.

resourceId (Optional)
Type: String

ID of Amazon EC2 instance for the rule to check.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
