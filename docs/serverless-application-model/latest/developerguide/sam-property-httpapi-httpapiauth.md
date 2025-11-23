# HttpApiAuth

Configure authorization to control access to your Amazon API Gateway HTTP API.

For more information about configuring access to HTTP APIs, see [Controlling and managing access to an HTTP API in API Gateway](../../../apigateway/latest/developerguide/http-api-access-control.md "../../../apigateway/latest/developerguide/http-api-access-control.md") in the _API Gateway Developer Guide_.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Authorizers: `OAuth2Authorizer | LambdaAuthorizer`
  DefaultAuthorizer: `String`
  EnableIamAuthorizer: `Boolean`

```

## Properties

`Authorizers`

The authorizer used to control access to your API Gateway API.

_Type_: [OAuth2Authorizer](sam-property-httpapi-oauth2authorizer.md "sam-property-httpapi-oauth2authorizer.md") | [LambdaAuthorizer](sam-property-httpapi-lambdaauthorizer.md "sam-property-httpapi-lambdaauthorizer.md")

_Required_: No

_Default_: None

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

_Additional notes_: AWS SAM adds the authorizers to the OpenAPI definition.

`DefaultAuthorizer`

Specify the default authorizer to use for authorizing API calls to your API Gateway API. You can specify `AWS_IAM` as a default authorizer if `EnableIamAuthorizer` is set to `true`. Otherwise, specify an authorizer that you've defined in `Authorizers`.

_Type_: String

_Required_: No

_Default_: None

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`EnableIamAuthorizer`

Specify whether to use IAM authorization for the API route.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### OAuth 2.0 Authorizer

OAuth 2.0 authorizer example

#### YAML

```
Auth:
  Authorizers:
    OAuth2Authorizer:
      AuthorizationScopes:
        - scope1
        - scope2
      JwtConfiguration:
        issuer: "https://www.example.com/v1/connect/oauth2"
        audience:
          - MyApi
      IdentitySource: "$request.querystring.param"
  DefaultAuthorizer: OAuth2Authorizer

```

### IAM authorizer

IAM authorizer example

#### YAML

```
Auth:
  EnableIamAuthorizer: true
  DefaultAuthorizer: AWS_IAM

```
