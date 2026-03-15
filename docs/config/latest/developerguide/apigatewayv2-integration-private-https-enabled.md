# apigatewayv2-integration-private-https-enabled

Checks if Amazon API Gateway V2 private integration traffic for HTTP APIs uses the HTTPS protocol. The rule is NON_COMPLIANT if configuration.TlsConfig does not exist.

**Identifier:** APIGATEWAYV2_INTEGRATION_PRIVATE_HTTPS_ENABLED

**Resource Types:** AWS::ApiGatewayV2::Integration

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
