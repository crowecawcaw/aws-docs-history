# OAuth2Authorizer

Definition for an OAuth 2.0 authorizer, also known to as a JSON Web Token (JWT) authorizer.

For more information, see [Controlling access to HTTP APIs with JWT authorizers](../../../apigateway/latest/developerguide/http-api-jwt-authorizer.md "../../../apigateway/latest/developerguide/http-api-jwt-authorizer.md") in the _API Gateway Developer Guide_.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  AuthorizationScopes: `List`
  IdentitySource: `String`
  JwtConfiguration: `Map`

```

## Properties

`AuthorizationScopes`

List of authorization scopes for this authorizer.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`IdentitySource`

Identity source expression for this authorizer.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`JwtConfiguration`

JWT configuration for this authorizer.

This is passed through to the `jwtConfiguration` section of an
`x-amazon-apigateway-authorizer` in the `securitySchemes` section of an OpenAPI
definition.

###### Note

Properties `issuer` and `audience` are case insensitive and can be used either
lowercase as in OpenAPI or uppercase `Issuer` and `Audience` as in
[AWS::ApiGatewayV2::Authorizer](../../../AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.md").

_Type_: Map

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### OAuth 2.0 authorizer

OAuth 2.0 authorizer Example

#### YAML

```
Auth:
  Authorizers:
    OAuth2Authorizer:
      AuthorizationScopes:
        - scope1
      JwtConfiguration:
        issuer: "https://www.example.com/v1/connect/oauth2"
        audience:
          - MyApi
      IdentitySource: "$request.querystring.param"
  DefaultAuthorizer: OAuth2Authorizer

```
