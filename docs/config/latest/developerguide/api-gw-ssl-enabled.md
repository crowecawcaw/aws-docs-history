# api-gw-ssl-enabled

Checks if a REST API stage uses an SSL certificate. The rule is NON_COMPLIANT if the REST API stage does not have an associated SSL certificate.

###### Note

This rule returns `NOT_APPLICABLE` if the [GetIntegration](../../../apigateway/latest/api/API_GetIntegration.md "../../../apigateway/latest/api/API_GetIntegration.md") API returns `AWS` as [type](../../../apigateway/latest/api/API_GetIntegration.md#apigw-GetIntegration-response-type "../../../apigateway/latest/api/API_GetIntegration.md#apigw-GetIntegration-response-type").

**Identifier:** API_GW_SSL_ENABLED

**Resource Types:** AWS::ApiGateway::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Asia Pacific (Taipei) Region

**Parameters:**

CertificateIDs (Optional)
Type: CSV

Comma-separated list of client certificate IDs configured on a REST API stage.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
