# apigateway-stage-description

Checks if Amazon API Gateway stages have a description. The rule is NON_COMPLIANT if configuration.Description does not exist or is an empty string.

**Identifier:** APIGATEWAY_STAGE_DESCRIPTION

**Resource Types:** AWS::ApiGateway::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
