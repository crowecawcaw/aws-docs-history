# lambda-function-log-format-json

Checks if AWS Lambda functions have the log format set to JSON for more control and better readability. The rule is NON_COMPLIANT if configuration.loggingConfig.logFormat is not 'JSON'.

**Identifier:** LAMBDA_FUNCTION_LOG_FORMAT_JSON

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
