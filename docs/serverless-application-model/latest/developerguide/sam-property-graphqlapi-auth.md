# Auth

Configure authorization for your GraphQL API.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
Additional:
- `AuthProvider`
LambdaAuthorizer: `LambdaAuthorizerConfig`
OpenIDConnect: `OpenIDConnectConfig`
Type: `String`
UserPool: `UserPoolConfig`
```

## Properties

`Additional`

A list of additional authorization types for your GraphQL API.

_Type_: List of [AuthProvider](sam-property-graphqlapi-auth-authprovider.md "sam-property-graphqlapi-auth-authprovider.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation
equivalent.

`LambdaAuthorizer`

Specify the optional authorization configuration for your Lambda function authorizer. You can configure this
optional property when `Type` is specified as `AWS_LAMBDA`.

_Type_: [LambdaAuthorizerConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-lambdaauthorizerconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-lambdaauthorizerconfig")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `LambdaAuthorizerConfig` property of an `AWS::AppSync::GraphQLApi` resource.

`OpenIDConnect`

Specify the optional authorization configuration for your OpenID Connect compliant service.
You can configure this optional property when `Type` is specified as `OPENID_CONNECT`.

_Type_: [OpenIDConnectConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-openidconnectconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-openidconnectconfig")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `OpenIDConnectConfig` property of an `AWS::AppSync::GraphQLApi` resource.

`Type`

The default authorization type between applications and your AWS AppSync GraphQL API.

For a list and description of allowed values, see [Authorization and
authentication](../../../appsync/latest/devguide/security-authz.md "../../../appsync/latest/devguide/security-authz.md") in the _AWS AppSync Developer Guide_.

When you specify a Lambda authorizer (`AWS_LAMBDA`), AWS SAM creates an
AWS Identity and Access Management (IAM) policy to provision permissions between your GraphQL
API and Lambda function.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`AuthenticationType` property of an
`AWS::AppSync::GraphQLApi` resource.

`UserPool`

Specify the optional authorization configuration for using Amazon Cognito user pools. You can configure this
optional property when `Type` is specified as `AMAZON_COGNITO_USER_POOLS`.

_Type_: [UserPoolConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-userpoolconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-userpoolconfig")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `UserPoolConfig` property of an `AWS::AppSync::GraphQLApi` resource.

## Examples

### Configure a default and additional authorization

type

In this example, we start by configuring a Lambda authorizer as the default authorization type for our
GraphQL API.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyGraphQLAPI:
    Type: AWS::Serverless::GraphQLApi
    Properties:
      Auth:
        Type: AWS_LAMBDA
        LambdaAuthorizer:
          AuthorizerUri: !GetAtt Authorizer1.Arn
          AuthorizerResultTtlInSeconds: 10
          IdentityValidationExpression: hello
```

Next, we configure additional authorization types for our GraphQL API by adding the following to our
AWS SAM template:

```
        Additional:
        - Type: AWS_IAM
        - Type: API_KEY
        - Type: OPENID_CONNECT
          OpenIDConnect:
            AuthTTL: 10
            ClientId: myId
            IatTTL: 10
            Issuer: prod
```

This results in the following AWS SAM template:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyGraphQLAPI:
    Type: AWS::Serverless::GraphQLApi
    Properties:
      Auth:
        Type: AWS_LAMBDA
        LambdaAuthorizer:
          AuthorizerUri: !GetAtt Authorizer1.Arn
          AuthorizerResultTtlInSeconds: 10
          IdentityValidationExpression: hello
        Additional:
        - Type: AWS_IAM
        - Type: API_KEY
        - Type: OPENID_CONNECT
          OpenIDConnect:
            AuthTTL: 10
            ClientId: myId
            IatTTL: 10
            Issuer: prod
```
