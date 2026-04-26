# WebSocketApiAuth

Configure authorization to control access to your Amazon API Gateway WebSocket API.

For more information about configuring access to WebSocket APIs, see [Controlling access to WebSocket APIs](../../../apigateway/latest/developerguide/apigateway-websocket-api-control-access.md "../../../apigateway/latest/developerguide/apigateway-websocket-api-control-access.md") in the _API Gateway Developer Guide_.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
AuthArn: `String`
AuthType: `String`
IdentitySource: `List`
InvokeRole: `String`
Name: `String`

```

## Properties

`AuthArn`

The ARN of the Lambda function to use for authorization. Required when `AuthType` is `CUSTOM`.

_Type_: String

_Required_: Conditional

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`AuthType`

The type of authorization. Valid values are `NONE`, `AWS_IAM`, or `CUSTOM`.

- `NONE` - No authorization
- `AWS_IAM` - IAM authorization
- `CUSTOM` - Lambda authorizer

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`IdentitySource`

The identity source for which authorization is requested. For example, `route.request.header.Authorization`.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`IdentitySource` property of an
`AWS::ApiGatewayV2::Authorizer` resource.

`InvokeRole`

The ARN of the IAM role that API Gateway assumes when invoking the authorizer function. If not specified, AWS SAM automatically creates a resource-based permission that allows API Gateway to invoke the authorizer function.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`AuthorizerCredentialsArn` property of an
`AWS::ApiGatewayV2::Authorizer` resource.

`Name`

The name of the authorizer.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an
`AWS::ApiGatewayV2::Authorizer` resource.

## Examples

### Lambda Authorizer

The following example configures a Lambda authorizer for a WebSocket API.

```
Auth:
  AuthType: CUSTOM
  AuthArn: !GetAtt AuthorizerFunction.Arn
  IdentitySource:
    - route.request.header.Authorization

```

### IAM Authorization

The following example configures IAM authorization for a WebSocket API.

```
Auth:
  AuthType: AWS_IAM

```
