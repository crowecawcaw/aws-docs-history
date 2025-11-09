# lambda-function-description

Checks if AWS Lambda functions have a description. The rule is NON_COMPLIANT if configuration.description does not exist or is an empty string.

**Identifier:** LAMBDA_FUNCTION_DESCRIPTION

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
