

# Auth
<a name="sam-property-graphqlapi-auth"></a>

Configure authorization for your GraphQL API.

## Syntax
<a name="sam-property-graphqlapi-auth-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-graphqlapi-auth-syntax-yaml"></a>

```
Additional:
- {{AuthProvider}}
LambdaAuthorizer: {{[LambdaAuthorizerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html)}}
OpenIDConnect: {{[OpenIDConnectConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html)}}
Type: {{String}}
UserPool: {{[UserPoolConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html)}}
```

## Properties
<a name="sam-property-graphqlapi-auth-properties"></a>

`Additional`  <a name="sam-graphqlapi-auth-additional"></a>
A list of additional authorization types for your GraphQL API.  
*Type*: List of [ AuthProvider](sam-property-graphqlapi-auth-authprovider.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`LambdaAuthorizer`  <a name="sam-graphqlapi-auth-lambdaauthorizer"></a>
Specify the optional authorization configuration for your Lambda function authorizer. You can configure this optional property when `Type` is specified as `AWS_LAMBDA`.  
*Type*: [ LambdaAuthorizerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ LambdaAuthorizerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html)` property of an `AWS::AppSync::GraphQLApi` resource.

`OpenIDConnect`  <a name="sam-graphqlapi-auth-openidconnect"></a>
Specify the optional authorization configuration for your OpenID Connect compliant service. You can configure this optional property when `Type` is specified as `OPENID_CONNECT`.  
*Type*: [ OpenIDConnectConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-openidconnectconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ OpenIDConnectConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html)` property of an `AWS::AppSync::GraphQLApi` resource.

`Type`  <a name="sam-graphqlapi-auth-type"></a>
The default authorization type between applications and your AWS AppSync GraphQL API.  
For a list and description of allowed values, see [Authorization and authentication](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html) in the *AWS AppSync Developer Guide*.  
When you specify a Lambda authorizer (`AWS_LAMBDA`), AWS SAM creates an AWS Identity and Access Management (IAM) policy to provision permissions between your GraphQL API and Lambda function.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[AuthenticationType](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-authenticationtype)` property of an `AWS::AppSync::GraphQLApi` resource.

`UserPool`  <a name="sam-graphqlapi-auth-userpool"></a>
Specify the optional authorization configuration for using Amazon Cognito user pools. You can configure this optional property when `Type` is specified as `AMAZON_COGNITO_USER_POOLS`.  
*Type*: [ UserPoolConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-userpoolconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ UserPoolConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html)` property of an `AWS::AppSync::GraphQLApi` resource.

## Examples
<a name="sam-property-graphqlapi-auth-examples"></a>

### Configure a default and additional authorization type
<a name="sam-property-graphqlapi-auth-examples-example1"></a>

In this example, we start by configuring a Lambda authorizer as the default authorization type for our GraphQL API.

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

Next, we configure additional authorization types for our GraphQL API by adding the following to our AWS SAM template:

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