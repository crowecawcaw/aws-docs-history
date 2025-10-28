# appsync-cache-ct-encryption-in-transit

Checks if an AWS AppSync API cache has encryption in transit enabled. The rule is NON_COMPLIANT if 'TransitEncryptionEnabled' is false.

**Identifier:** APPSYNC_CACHE_CT_ENCRYPTION_IN_TRANSIT

**Resource Types:** AWS::AppSync::ApiCache

**Trigger type:** Configuration changes

**AWS Region:** Only available in Middle East (Bahrain), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
