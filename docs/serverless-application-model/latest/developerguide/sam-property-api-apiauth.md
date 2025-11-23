# ApiAuth

Configure authorization to control access to your API Gateway API.

For more information and examples for configuring access using AWS SAM see [Control API access with your AWS SAM template](serverless-controlling-access-to-apis.md "serverless-controlling-access-to-apis.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  AddApiKeyRequiredToCorsPreflight: `Boolean`
  AddDefaultAuthorizerToCorsPreflight: `Boolean`
  ApiKeyRequired: `Boolean`
  Authorizers: `CognitoAuthorizer | LambdaTokenAuthorizer | LambdaRequestAuthorizer | AWS_IAM`
  DefaultAuthorizer: `String`
  InvokeRole: `String`
  ResourcePolicy: `ResourcePolicyStatement`
  UsagePlan: `ApiUsagePlan`

```

###### Note

The `Authorizers` property includes `AWS_IAM`, but there is no extra configuration needed for `AWS_IAM`. For an example, see [AWS IAM](#sam-property-api-apiauth--examples--aws_iam "#sam-property-api-apiauth--examples--aws_iam").

## Properties

`AddApiKeyRequiredToCorsPreflight`

If the `ApiKeyRequired` and `Cors` properties are set, then setting `AddApiKeyRequiredToCorsPreflight` will cause the API key to
be added to the `Options` property.

_Type_: Boolean

_Required_: No

_Default_: `True`

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`AddDefaultAuthorizerToCorsPreflight`

If the `DefaultAuthorizer` and `Cors` properties are set, then setting `AddDefaultAuthorizerToCorsPreflight` will cause the default authorizer to be added to the `Options` property in the OpenAPI section.

_Type_: Boolean

_Required_: No

_Default_: True

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`ApiKeyRequired`

If set to true then an API key is required for all API events. For more information about API keys see [Create and Use Usage Plans with API Keys](../../../apigateway/latest/developerguide/api-gateway-api-usage-plans.md "../../../apigateway/latest/developerguide/api-gateway-api-usage-plans.md") in the _API Gateway Developer Guide_.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Authorizers`

The authorizer used to control access to your API Gateway API.

For more information, see [Control API access with your AWS SAM template](serverless-controlling-access-to-apis.md "serverless-controlling-access-to-apis.md").

_Type_: [CognitoAuthorizer](sam-property-api-cognitoauthorizer.md "sam-property-api-cognitoauthorizer.md") | [LambdaTokenAuthorizer](sam-property-api-lambdatokenauthorizer.md "sam-property-api-lambdatokenauthorizer.md") | [LambdaRequestAuthorizer](sam-property-api-lambdarequestauthorizer.md "sam-property-api-lambdarequestauthorizer.md") | AWS_IAM

_Required_: No

_Default_: None

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

_Additional notes_: SAM adds the Authorizers to the OpenApi definition of an Api.

`DefaultAuthorizer`

Specify a default authorizer for an API Gateway API, which will be used for authorizing API calls by default.

###### Note

If the Api EventSource for the function associated with this API is configured to use IAM Permissions, then this property must be set to `AWS_IAM`, otherwise an error will result.

_Type_: String

_Required_: No

_Default_: None

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`InvokeRole`

Sets integration credentials for all resources and methods to this value.

`CALLER_CREDENTIALS` maps to `arn:aws:iam::`:<user>/``, which uses the caller credentials to invoke the endpoint.

_Valid values_: `CALLER_CREDENTIALS`, `NONE`, `IAMRoleArn`

_Type_: String

_Required_: No

_Default_: `CALLER_CREDENTIALS`

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`ResourcePolicy`

Configure Resource Policy for all methods and paths on an API.

_Type_: [ResourcePolicyStatement](sam-property-api-resourcepolicystatement.md "sam-property-api-resourcepolicystatement.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

_Additional notes_: This setting can also be defined on individual `AWS::Serverless::Function` using the [ApiFunctionAuth](sam-property-function-apifunctionauth.md "sam-property-function-apifunctionauth.md"). This is required for APIs with `EndpointConfiguration: PRIVATE`.

`UsagePlan`

Configures a usage plan associated with this API. For more information about usage plans see [Create and Use Usage Plans with API Keys](../../../apigateway/latest/developerguide/api-gateway-api-usage-plans.md "../../../apigateway/latest/developerguide/api-gateway-api-usage-plans.md") in the _API Gateway Developer Guide_.

This AWS SAM property generates three additional CloudFormation resources when this property is set: an [AWS::ApiGateway::UsagePlan](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.md"), an [AWS::ApiGateway::UsagePlanKey](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.md"), and an [AWS::ApiGateway::ApiKey](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.md"). For information about this scenario, see [UsagePlan
property is specified](sam-specification-generated-resources-api.md#sam-specification-generated-resources-api-usage-plan "sam-specification-generated-resources-api.md#sam-specification-generated-resources-api-usage-plan"). For general information about generated CloudFormation resources, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

_Type_: [ApiUsagePlan](sam-property-api-apiusageplan.md "sam-property-api-apiusageplan.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### CognitoAuth

Cognito Auth example

#### YAML

```
Auth:
  Authorizers:
    MyCognitoAuth:
     UserPoolArn:
       Fn::GetAtt:
         - MyUserPool
         - Arn
     AuthType: "COGNITO_USER_POOLS"
  DefaultAuthorizer: MyCognitoAuth
  InvokeRole: CALLER_CREDENTIALS
  AddDefaultAuthorizerToCorsPreflight: false
  ApiKeyRequired: false
  ResourcePolicy:
    CustomStatements: [{
      "Effect": "Allow",
      "Principal": "*",
      "Action": "execute-api:Invoke",
      "Resource": "execute-api:/Prod/GET/pets",
      "Condition": {
          "IpAddress": {
              "aws:SourceIp": "1.2.3.4"
          }
        }
    }]
    IpRangeDenylist:
      - "10.20.30.40"

```

### AWS IAM

AWS IAM example

#### YAML

```
Auth:
  Authorizers: AWS_IAM
```
