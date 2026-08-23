# kinesis-stream-backup-retention-check

Checks if an Amazon Kinesis Data Stream has its data record retention period set to a specific number of hours. The rule is NON\_COMPLIANT if the property `RetentionPeriodHours` is set to a value less than the value specified by the parameter.

**Identifier:** KINESIS\_STREAM\_BACKUP\_RETENTION\_CHECK

**Resource Types:** AWS::Kinesis::Stream

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Israel (Tel Aviv), Canada West (Calgary) Region

**Parameters:**

minimumBackupRetentionPeriod (Optional)
Type: String

Minimum hours data records should be retained. Valid values are 24 to 8760, default value is 168.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
