# LambdaRequestAuthorizer

Configure a Lambda Authorizer to control access to your API with a Lambda function.

For more information and examples, see [Control API access with your AWS SAM template](serverless-controlling-access-to-apis.md "serverless-controlling-access-to-apis.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
DisableFunctionDefaultPermissions: `Boolean`
FunctionArn: `String`
FunctionInvokeRole: `String`
FunctionPayloadType: `String`
Identity: `LambdaRequestAuthorizationIdentity`

```

## Properties

`DisableFunctionDefaultPermissions`

Specify `true` to prevent AWS SAM from automatically creating an `AWS::Lambda::Permissions`
resource to provision permissions between your `AWS::Serverless::Api` resource and authorizer Lambda
function.

_Default value_: `false`

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`FunctionArn`

Specify the function ARN of the Lambda function which provides authorization for the
API.

###### Note

AWS SAM will automatically create an `AWS::Lambda::Permissions` resource when
`FunctionArn` is specified for `AWS::Serverless::Api`. The
`AWS::Lambda::Permissions` resource provisions permissions between your API and authorizer Lambda
function.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`FunctionInvokeRole`

Adds authorizer credentials to the OpenApi definition of the Lambda
authorizer.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`FunctionPayloadType`

This property can be used to define the type of Lambda Authorizer for an API.

_Valid values_: `TOKEN` or
`REQUEST`

_Type_: String

_Required_: No

_Default_: `TOKEN`

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`Identity`

This property can be used to specify an `IdentitySource` in an incoming
request for an authorizer. This property is only required if the
`FunctionPayloadType` property is set to `REQUEST`.

_Type_: [LambdaRequestAuthorizationIdentity](sam-property-api-lambdarequestauthorizationidentity.md "sam-property-api-lambdarequestauthorizationidentity.md")

_Required_: Conditional

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

## Examples

### LambdaRequestAuth

#### YAML

```
Authorizers:
  MyLambdaRequestAuth:
    FunctionPayloadType: REQUEST
    FunctionArn:
      Fn::GetAtt:
        - MyAuthFunction
        - Arn
    FunctionInvokeRole:
      Fn::GetAtt:
        - LambdaAuthInvokeRole
        - Arn
    Identity:
      Headers:
        - Authorization1

```
