# LambdaTokenAuthorizer

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
Identity: `LambdaTokenAuthorizationIdentity`
```

## Properties

`DisableFunctionDefaultPermissions`

Specify `true` to prevent AWS SAM from automatically creating an `AWS::Lambda::Permissions`
resource to provision permissions between your `AWS::Serverless::Api` resource and authorizer Lambda
function.

_Default value_: `false`

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

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

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`FunctionInvokeRole`

Adds authorizer credentials to the OpenApi definition of the Lambda
authorizer.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`FunctionPayloadType`

This property can be used to define the type of Lambda Authorizer for an Api.

_Valid values_: `TOKEN` or
`REQUEST`

_Type_: String

_Required_: No

_Default_: `TOKEN`

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`Identity`

This property can be used to specify an `IdentitySource` in an incoming
request for an authorizer. This property is only required if the
`FunctionPayloadType` property is set to `REQUEST`.

_Type_: [LambdaTokenAuthorizationIdentity](sam-property-api-lambdatokenauthorizationidentity.md "sam-property-api-lambdatokenauthorizationidentity.md")

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

## Examples

### LambdaTokenAuth

#### YAML

```
Authorizers:
  MyLambdaTokenAuth:
    FunctionArn:
      Fn::GetAtt:
        - MyAuthFunction
        - Arn
    Identity:
      Header: MyCustomAuthHeader # OPTIONAL; Default: 'Authorization'
      ValidationExpression: mycustomauthexpression # OPTIONAL
      ReauthorizeEvery: 20 # OPTIONAL; Service Default: 300

```

### BasicLambdaTokenAuth

#### YAML

```
Authorizers:
  MyLambdaTokenAuth:
    FunctionArn:
      Fn::GetAtt:
        - MyAuthFunction
        - Arn

```
