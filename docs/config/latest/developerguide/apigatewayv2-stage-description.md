# apigatewayv2-stage-description

Checks if Amazon API Gateway V2 stages have a description. The rule is NON\_COMPLIANT if configuration.Description does not exist or is an empty string.

**Identifier:** APIGATEWAYV2\_STAGE\_DESCRIPTION

**Resource Types:** AWS::ApiGatewayV2::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
