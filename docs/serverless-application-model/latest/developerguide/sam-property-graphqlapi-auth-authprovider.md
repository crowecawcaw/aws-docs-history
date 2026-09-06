

# AuthProvider
<a name="sam-property-graphqlapi-auth-authprovider"></a>

Optional authorization configuration for your additional GraphQL API authorization types.

## Syntax
<a name="sam-property-graphqlapi-auth-authprovider-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-graphqlapi-auth-authprovider-syntax-yaml"></a>

```
LambdaAuthorizer: {{[LambdaAuthorizerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html)}}
OpenIDConnect: {{[OpenIDConnectConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html)}}
Type: {{String}}
UserPool: {{[UserPoolConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html)}}
```

## Properties
<a name="sam-property-graphqlapi-auth-authprovider-properties"></a>

`LambdaAuthorizer`  <a name="sam-graphqlapi-auth-authprovider-lambdaauthorizer"></a>
Specify the optional authorization configuration for your AWS Lambda function authorizer. You can configure this optional property when `Type` is specified as `AWS_LAMBDA`.  
*Type*: [ LambdaAuthorizerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-lambdaauthorizerconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ LambdaAuthorizerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html)` property of an `AWS::AppSync::GraphQLApi` `[ AdditionalAuthenticationProvider](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html)` object.

`OpenIDConnect`  <a name="sam-graphqlapi-auth-authprovider-openidconnect"></a>
Specify the optional authorization configuration for your OpenID Connect compliant service. You can configure this optional property when `Type` is specified as `OPENID_CONNECT`.  
*Type*: [ OpenIDConnectConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-openidconnectconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ OpenIDConnectConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html)` property of an `AWS::AppSync::GraphQLApi` `[ AdditionalAuthenticationProvider](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html)` object.

`Type`  <a name="sam-graphqlapi-auth-authprovider-type"></a>
The default authorization type between applications and your AWS AppSync GraphQL API.  
For a list and description of allowed values, see [Authorization and authentication](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html) in the *AWS AppSync Developer Guide*.  
When you specify a Lambda authorizer (`AWS_LAMBDA`), AWS SAM creates an AWS Identity and Access Management (IAM) policy to provision permissions between your GraphQL API and Lambda function.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[ AuthenticationType](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-authenticationtype)` property of an `AWS::AppSync::GraphQLApi` `[ AdditionalAuthenticationProvider](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html)` object.

`UserPool`  <a name="sam-graphqlapi-auth-authprovider-userpool"></a>
Specify the optional authorization configuration for using Amazon Cognito user pools. You can configure this optional property when `Type` is specified as `AMAZON_COGNITO_USER_POOLS`.  
*Type*: [ UserPoolConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-userpoolconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ UserPoolConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html)` property of an `AWS::AppSync::GraphQLApi` `[ AdditionalAuthenticationProvider](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html)` object.