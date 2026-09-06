

# api-gw-ssl-enabled
<a name="api-gw-ssl-enabled"></a>

Checks if a REST API stage uses an SSL certificate. The rule is NON\_COMPLIANT if the REST API stage does not have an associated SSL certificate. 

**Note**  
This rule returns `NOT_APPLICABLE` if the [GetIntegration](https://docs.aws.amazon.com/apigateway/latest/api/API_GetIntegration.html) API returns an integration type other than `HTTP` as [type](https://docs.aws.amazon.com/apigateway/latest/api/API_GetIntegration.html#apigw-GetIntegration-response-type). This rule evaluates the SSL certificate configuration in API Gateway stage settings, not the actual deployed state.

**Identifier:** API\_GW\_SSL\_ENABLED

**Resource Types:** AWS::ApiGateway::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Taipei) Region

**Parameters:**

CertificateIDs (Optional)Type: CSV  
Comma-separated list of client certificate IDs configured on a REST API stage.

## AWS CloudFormation template
<a name="w2aac20c16c17b7c83c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).