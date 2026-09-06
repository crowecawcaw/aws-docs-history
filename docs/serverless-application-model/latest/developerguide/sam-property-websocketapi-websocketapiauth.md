

# WebSocketApiAuth
<a name="sam-property-websocketapi-websocketapiauth"></a>

Configure authorization to control access to your Amazon API Gateway WebSocket API.

For more information about configuring access to WebSocket APIs, see [Controlling access to WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-control-access.html) in the *API Gateway Developer Guide*.

## Syntax
<a name="sam-property-websocketapi-websocketapiauth-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-websocketapi-websocketapiauth-syntax.yaml"></a>

```
[AuthArn](#sam-websocketapiauth-autharn): {{String}}
[AuthType](#sam-websocketapiauth-authtype): {{String}}
[IdentitySource](#sam-websocketapiauth-identitysource): {{List}}
[InvokeRole](#sam-websocketapiauth-invokerole): {{String}}
[Name](#sam-websocketapiauth-name): {{String}}
```

## Properties
<a name="sam-property-websocketapi-websocketapiauth-properties"></a>

 `AuthArn`   <a name="sam-websocketapiauth-autharn"></a>
The ARN of the Lambda function to use for authorization. Required when `AuthType` is `CUSTOM`.  
*Type*: String  
*Required*: Conditional  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `AuthType`   <a name="sam-websocketapiauth-authtype"></a>
The type of authorization. Valid values are `NONE`, `AWS_IAM`, or `CUSTOM`.  
+ `NONE` - No authorization
+ `AWS_IAM` - IAM authorization
+ `CUSTOM` - Lambda authorizer
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `IdentitySource`   <a name="sam-websocketapiauth-identitysource"></a>
The identity source for which authorization is requested. For example, `route.request.header.Authorization`.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[IdentitySource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identitysource)` property of an `AWS::ApiGatewayV2::Authorizer` resource.

 `InvokeRole`   <a name="sam-websocketapiauth-invokerole"></a>
The ARN of the IAM role that API Gateway assumes when invoking the authorizer function. If not specified, AWS SAM automatically creates a resource-based permission that allows API Gateway to invoke the authorizer function.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[AuthorizerCredentialsArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizercredentialsarn)` property of an `AWS::ApiGatewayV2::Authorizer` resource.

 `Name`   <a name="sam-websocketapiauth-name"></a>
The name of the authorizer.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-name)` property of an `AWS::ApiGatewayV2::Authorizer` resource.

## Examples
<a name="sam-property-websocketapi-websocketapiauth-examples"></a>

### Lambda Authorizer
<a name="sam-property-websocketapi-websocketapiauth-examples-lambda"></a>

The following example configures a Lambda authorizer for a WebSocket API.

```
Auth:
  AuthType: CUSTOM
  AuthArn: !GetAtt AuthorizerFunction.Arn
  IdentitySource:
    - route.request.header.Authorization
```

### IAM Authorization
<a name="sam-property-websocketapi-websocketapiauth-examples-iam"></a>

The following example configures IAM authorization for a WebSocket API.

```
Auth:
  AuthType: AWS_IAM
```