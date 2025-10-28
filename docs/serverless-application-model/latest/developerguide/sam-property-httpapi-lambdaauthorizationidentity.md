# LambdaAuthorizationIdentity

Use property can be used to specify an IdentitySource in an incoming request for a Lambda authorizer. For more information about identity sources, see [Identity sources](../../../apigateway/latest/developerguide/http-api-lambda-authorizer.md#http-api-lambda-authorizer.identity-sources "../../../apigateway/latest/developerguide/http-api-lambda-authorizer.md#http-api-lambda-authorizer.identity-sources") in the _API Gateway Developer Guide_.

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

Converts the given context strings to a list of mapping expressions in the format `$context.contextString`.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Headers`

Converts the headers to a list of mapping expressions in the format `$request.header.name`.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`QueryStrings`

Converts the given query strings to a list of mapping expressions in the format `$request.querystring.queryString`.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`ReauthorizeEvery`

The time-to-live (TTL) period, in seconds, that specifies how long API Gateway caches authorizer results. If you specify a value greater than 0, API Gateway caches the authorizer responses. The maximum value is 3600, or 1 hour.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`StageVariables`

Converts the given stage variables to a list of mapping expressions in the format `$stageVariables.stageVariable`.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

## Examples

### LambdaRequestIdentity

Lambda request identity example

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
