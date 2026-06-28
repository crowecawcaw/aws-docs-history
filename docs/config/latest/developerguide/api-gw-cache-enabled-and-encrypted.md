# api-gw-cache-enabled-and-encrypted

Checks if all methods in Amazon API Gateway stages have cache enabled and cache encrypted. The rule is NON\_COMPLIANT if any method in an Amazon API Gateway stage is not configured to cache or the cache is not encrypted.

**Identifier:** API\_GW\_CACHE\_ENABLED\_AND\_ENCRYPTED

**Resource Types:** AWS::ApiGateway::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
