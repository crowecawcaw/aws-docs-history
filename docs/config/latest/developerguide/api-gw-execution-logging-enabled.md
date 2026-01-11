# api-gw-execution-logging-enabled

Checks if all methods in Amazon API Gateway stages have logging enabled. The rule is NON_COMPLIANT if logging is not enabled, or if `loggingLevel` is neither ERROR nor INFO.

**Identifier:** API_GW_EXECUTION_LOGGING_ENABLED

**Resource Types:** AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei) Region

**Parameters:**

loggingLevel (Optional)
Type: String
Default: ERROR,INFO

Comma-separated list of specific logging levels (for example, ERROR, INFO or ERROR,INFO).

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
