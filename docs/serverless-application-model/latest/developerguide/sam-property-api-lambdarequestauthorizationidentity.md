# LambdaRequestAuthorizationIdentity

This property can be used to specify an IdentitySource in an incoming request for an authorizer. For more information about IdentitySource see the [ApiGateway Authorizer OpenApi extension](../../../apigateway/latest/developerguide/api-gateway-swagger-extensions-authorizer.md "../../../apigateway/latest/developerguide/api-gateway-swagger-extensions-authorizer.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Context: `List`
  Headers: `List`
  QueryStrings: `List`
  ReauthorizeEvery: `Integer`
  StageVariables: `List`

```

## Properties

`Context`

Converts the given context strings to the mapping expressions of format `context.contextString`.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Headers`

Converts the headers to comma-separated string of mapping expressions of format `method.request.header.name`.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`QueryStrings`

Converts the given query strings to comma-separated string of mapping expressions of format `method.request.querystring.queryString`.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`ReauthorizeEvery`

The time-to-live (TTL) period, in seconds, that specifies how long API Gateway caches authorizer results. If you specify a value greater than 0, API Gateway caches the authorizer responses. By default, API Gateway sets this property to 300. The maximum value is 3600, or 1 hour.

_Type_: Integer

_Required_: No

_Default_: 300

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`StageVariables`

Converts the given stage variables to comma-separated string of mapping expressions of format `stageVariables.stageVariable`.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### LambdaRequestIdentity

#### YAML

```
Identity:
  QueryStrings:
    - auth
  Headers:
    - Authorization
  StageVariables:
    - VARIABLE
  Context:
    - authcontext
  ReauthorizeEvery: 100

```
