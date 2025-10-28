# CognitoAuthorizationIdentity

This property can be used to specify an IdentitySource in an incoming request for an authorizer. For more information about IdentitySource see the [ApiGateway Authorizer OpenApi extension](../../../apigateway/latest/developerguide/api-gateway-swagger-extensions-authorizer.md "../../../apigateway/latest/developerguide/api-gateway-swagger-extensions-authorizer.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Header: `String`
  ReauthorizeEvery: `Integer`
  ValidationExpression: `String`

```

## Properties

`Header`

Specify the header name for Authorization in the OpenApi definition.

_Type_: String

_Required_: No

_Default_: Authorization

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`ReauthorizeEvery`

The time-to-live (TTL) period, in seconds, that specifies how long API Gateway caches authorizer results. If you specify a value greater than 0, API Gateway caches the authorizer responses. By default, API Gateway sets this property to 300. The maximum value is 3600, or 1 hour.

_Type_: Integer

_Required_: No

_Default_: 300

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`ValidationExpression`

Specify a validation expression for validating the incoming Identity

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

## Examples

### CognitoAuthIdentity

#### YAML

```
Identity:
  Header: MyCustomAuthHeader
  ValidationExpression: Bearer.*
  ReauthorizeEvery: 30

```
