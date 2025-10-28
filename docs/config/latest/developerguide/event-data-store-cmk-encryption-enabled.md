# event-data-store-cmk-encryption-enabled

Checks if AWS Cloud Trail event data stores have customer managed AWS KMS keys enabled. The rule is NON_COMPLIANT if an event data store has disabled customer managed KMS keys. Optionally, you can specify a list of KMS keys for the rule to check.

**Identifier:** EVENT_DATA_STORE_CMK_ENCRYPTION_ENABLED

**Resource Types:** AWS::CloudTrail::EventDataStore

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

kmsKeyArns (Optional)
Type: CSV

Comma-separated list of Amazon Resource Names (ARNs) of AWS KMS keys for the rule to check. If provided, the rule is NON_COMPLIANT if an AWS Cloud Trail event data store is not encrypted with one of these KMS keys.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
