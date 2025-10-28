# api-gw-endpoint-type-check

Checks if Amazon API Gateway APIs are of the type specified in the rule parameter `endpointConfigurationType`. The rule returns NON_COMPLIANT if the REST API does not match the endpoint type configured in the rule parameter.

**Identifier:** API_GW_ENDPOINT_TYPE_CHECK

**Resource Types:** AWS::ApiGateway::RestApi

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS Secret - West, Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

endpointConfigurationTypes
Type: String

Comma-separated list of allowed endpointConfigurationTypes. Allowed values are REGIONAL, PRIVATE and EDGE.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
