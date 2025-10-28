# AuthProvider

Optional authorization configuration for your additional GraphQL API authorization types.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
LambdaAuthorizer: `LambdaAuthorizerConfig`
OpenIDConnect: `OpenIDConnectConfig`
Type: `String`
UserPool: `UserPoolConfig`
```

## Properties

`LambdaAuthorizer`

Specify the optional authorization configuration for your AWS Lambda function authorizer. You can configure this
optional property when `Type` is specified as `AWS_LAMBDA`.

_Type_: [LambdaAuthorizerConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-lambdaauthorizerconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-lambdaauthorizerconfig")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `LambdaAuthorizerConfig` property of an `AWS::AppSync::GraphQLApi` `AdditionalAuthenticationProvider` object.

`OpenIDConnect`

Specify the optional authorization configuration for your OpenID Connect compliant service.
You can configure this optional property when `Type` is specified as `OPENID_CONNECT`.

_Type_: [OpenIDConnectConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-openidconnectconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-openidconnectconfig")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `OpenIDConnectConfig` property of an `AWS::AppSync::GraphQLApi` `AdditionalAuthenticationProvider` object.

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
`AuthenticationType` property of an `AWS::AppSync::GraphQLApi` `AdditionalAuthenticationProvider` object.

`UserPool`

Specify the optional authorization configuration for using Amazon Cognito user pools. You can configure this
optional property when `Type` is specified as `AMAZON_COGNITO_USER_POOLS`.

_Type_: [UserPoolConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-userpoolconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#cfn-appsync-graphqlapi-userpoolconfig")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `UserPoolConfig` property of an `AWS::AppSync::GraphQLApi` `AdditionalAuthenticationProvider` object.
