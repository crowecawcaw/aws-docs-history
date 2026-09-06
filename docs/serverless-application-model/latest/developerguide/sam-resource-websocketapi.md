

# AWS::Serverless::WebSocketApi
<a name="sam-resource-websocketapi"></a>

Creates an Amazon API Gateway WebSocket API, which enables you to create two-way interactive communication applications. WebSocket APIs allow the server to send messages to clients without the client having to request them. For more information, see [Working with WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html) in the *API Gateway Developer Guide*.

We recommend that you use CloudFormation hooks or IAM policies to verify that API Gateway resources have authorizers attached to them to control access to them.

For more information about using CloudFormation hooks, see [Registering hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/registering-hook-python.html) in the *CloudFormation CLI user guide* and the [apigw-enforce-authorizer](https://github.com/aws-cloudformation/aws-cloudformation-samples/tree/main/hooks/python-hooks/apigw-enforce-authorizer/) GitHub repository.

For more information about using IAM policies, see [Require that API routes have authorization](https://docs.aws.amazon.com/apigateway/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-require-authorization) in the *API Gateway Developer Guide*.

**Note**  
When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation resources. For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md).

## Syntax
<a name="sam-resource-websocketapi-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-resource-websocketapi-syntax.yaml"></a>

```
Type: AWS::Serverless::WebSocketApi
Properties:
  [ApiKeySelectionExpression](#sam-websocketapi-apikeyselectionexpression): {{String}}
  [AccessLogSettings](#sam-websocketapi-accesslogsettings): {{[AccessLogSettings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesslogsettings)}}
  [Auth](#sam-websocketapi-auth): {{WebSocketApiAuth}}
  [DefaultRouteSettings](#sam-websocketapi-defaultroutesettings): {{[RouteSettings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings)}}
  [Description](#sam-websocketapi-description): {{String}}
  [DisableExecuteApiEndpoint](#sam-websocketapi-disableexecuteapiendpoint): {{Boolean}}
  [DisableSchemaValidation](#sam-websocketapi-disableschemavalidation): {{Boolean}}
  [Domain](#sam-websocketapi-domain): {{WebSocketApiDomainConfiguration}}
  [IpAddressType](#sam-websocketapi-ipaddresstype): {{String}}
  [Name](#sam-websocketapi-name): {{String}}
  [PropagateTags](#sam-websocketapi-propagatetags): {{Boolean}}
  [Routes](#sam-websocketapi-routes): {{RouteConfiguration}}
  [RouteSelectionExpression](#sam-websocketapi-routeselectionexpression): {{String}}
  [RouteSettings](#sam-websocketapi-routesettings): {{[RouteSettings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings)}}
  [StageName](#sam-websocketapi-stagename): {{String}}
  [StageVariables](#sam-websocketapi-stagevariables): {{[Json](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagevariables)}}
  [Tags](#sam-websocketapi-tags): {{Map}}
```

## Properties
<a name="sam-resource-websocketapi-properties"></a>

 `ApiKeySelectionExpression`   <a name="sam-websocketapi-apikeyselectionexpression"></a>
An API key selection expression. For more information, see [API Key Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions) in the *API Gateway Developer Guide*.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ApiKeySelectionExpression](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-apikeyselectionexpression)` property of an `AWS::ApiGatewayV2::Api` resource.

 `AccessLogSettings`   <a name="sam-websocketapi-accesslogsettings"></a>
The settings for access logging in a stage.  
*Type*: [AccessLogSettings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesslogsettings)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[AccessLogSettings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesslogsettings)` property of an `AWS::ApiGatewayV2::Stage` resource.

 `Auth`   <a name="sam-websocketapi-auth"></a>
Configures authorization for controlling access to your WebSocket API. Authorization is applied to the `$connect` route.  
For more information, see [Controlling access to WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-control-access.html) in the *API Gateway Developer Guide*.  
*Type*: [WebSocketApiAuth](sam-property-websocketapi-websocketapiauth.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `DefaultRouteSettings`   <a name="sam-websocketapi-defaultroutesettings"></a>
The default route settings for this WebSocket API. These settings apply to all routes unless overridden by the `RouteSettings` property for certain routes.  
*Type*: [RouteSettings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[DefaultRouteSettings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-defaultroutesettings)` property of an `AWS::ApiGatewayV2::Stage` resource.

 `Description`   <a name="sam-websocketapi-description"></a>
A description of the WebSocket API.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-description)` property of an `AWS::ApiGatewayV2::Api` resource.

 `DisableExecuteApiEndpoint`   <a name="sam-websocketapi-disableexecuteapiendpoint"></a>
Specifies whether clients can invoke your API by using the default `execute-api` endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[DisableExecuteApiEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableexecuteapiendpoint)` property of an `AWS::ApiGatewayV2::Api` resource.

 `DisableSchemaValidation`   <a name="sam-websocketapi-disableschemavalidation"></a>
Avoid validating models when creating a deployment.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[DisableSchemaValidation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableschemavalidation)` property of an `AWS::ApiGatewayV2::Api` resource.

 `Domain`   <a name="sam-websocketapi-domain"></a>
Configures a custom domain for this WebSocket API.  
WebSocket APIs do not support mutual TLS authentication (MTLS). If you specify `MutualTlsAuthentication` or `OwnershipVerificationCertificateArn`, AWS SAM will return an error.
*Type*: [WebSocketApiDomainConfiguration](sam-property-websocketapi-websocketapidomainconfiguration.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `IpAddressType`   <a name="sam-websocketapi-ipaddresstype"></a>
The IP address type for the API. Valid values are `ipv4` for IPv4 only and `dualstack` for IPv4 and IPv6.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[IpAddressType](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-ipaddresstype)` property of an `AWS::ApiGatewayV2::Api` resource.

 `Name`   <a name="sam-websocketapi-name"></a>
A name for the WebSocket API. If you don't specify a name, AWS SAM generates a name for you.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-name)` property of an `AWS::ApiGatewayV2::Api` resource.

 `PropagateTags`   <a name="sam-websocketapi-propagatetags"></a>
If `true`, AWS SAM adds the `Tags` property to the `AWS::ApiGatewayV2::Stage` and `AWS::ApiGatewayV2::DomainName` resources that AWS SAM generates.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `Routes`   <a name="sam-websocketapi-routes"></a>
The route configurations for this WebSocket API. Routes define how messages are routed to Lambda functions. Each route consists of a route key and a Lambda function ARN.  
WebSocket APIs support three predefined routes: `$connect`, `$disconnect`, and `$default`. You can also define custom routes.  
*Type*: [RouteConfiguration](sam-property-websocketapi-routeconfiguration.md)  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `RouteSelectionExpression`   <a name="sam-websocketapi-routeselectionexpression"></a>
The route selection expression for the WebSocket API. For more information, see [Route Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-expressions) in the *API Gateway Developer Guide*.  
A common value is `$request.body.action`, which routes messages based on an `action` field in the message body.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[RouteSelectionExpression](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routeselectionexpression)` property of an `AWS::ApiGatewayV2::Api` resource.

 `RouteSettings`   <a name="sam-websocketapi-routesettings"></a>
The route settings for this WebSocket API. These settings override the `DefaultRouteSettings` for specific routes.  
*Type*: [RouteSettings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[RouteSettings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings)` property of an `AWS::ApiGatewayV2::Stage` resource.

 `StageName`   <a name="sam-websocketapi-stagename"></a>
The name of the API stage. If you don't specify a name, AWS SAM uses `default` as the stage name.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[StageName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagename)` property of an `AWS::ApiGatewayV2::Stage` resource.

 `StageVariables`   <a name="sam-websocketapi-stagevariables"></a>
A map that defines the stage variables. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9-._~:/?#&=,]+`.  
*Type*: [Json](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagevariables)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[StageVariables](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagevariables)` property of an `AWS::ApiGatewayV2::Stage` resource.

 `Tags`   <a name="sam-websocketapi-tags"></a>
A map (string to string) that specifies the tags to be added to this WebSocket API. For details about valid keys and values for tags, see [Resource tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *CloudFormation User Guide*.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Return Values
<a name="sam-resource-websocketapi-return-values"></a>

### Ref
<a name="sam-resource-websocketapi-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the API ID of the underlying `AWS::ApiGatewayV2::Api` resource, for example, `a1bcdef2gh`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html) in the *AWS CloudFormation User Guide*.

## Examples
<a name="sam-resource-websocketapi-examples"></a>

### Simple WebSocket API
<a name="sam-resource-websocketapi-examples-simple"></a>

The following example creates a WebSocket API with three routes.

```
Resources:
  MyWebSocketApi:
    Type: AWS::Serverless::WebSocketApi
    Properties:
      RouteSelectionExpression: $request.body.action
      Routes:
        $connect:
          FunctionArn: !GetAtt ConnectFunction.Arn
        $disconnect:
          FunctionArn: !GetAtt DisconnectFunction.Arn
        sendMessage:
          FunctionArn: !GetAtt SendMessageFunction.Arn

  ConnectFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.connect
      Runtime: nodejs20.x
      CodeUri: ./src

  DisconnectFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.disconnect
      Runtime: nodejs20.x
      CodeUri: ./src

  SendMessageFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.sendMessage
      Runtime: nodejs20.x
      CodeUri: ./src
```

### WebSocket API with Lambda Authorizer
<a name="sam-resource-websocketapi-examples-auth"></a>

The following example creates a WebSocket API with a Lambda authorizer.

```
Resources:
  MyWebSocketApi:
    Type: AWS::Serverless::WebSocketApi
    Properties:
      RouteSelectionExpression: $request.body.action
      Auth:
        AuthType: CUSTOM
        AuthArn: !GetAtt AuthorizerFunction.Arn
        IdentitySource:
          - route.request.header.Authorization
      Routes:
        $connect:
          FunctionArn: !GetAtt ConnectFunction.Arn
        sendMessage:
          FunctionArn: !GetAtt SendMessageFunction.Arn

  AuthorizerFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.authorize
      Runtime: nodejs20.x
      CodeUri: ./src

  ConnectFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.connect
      Runtime: nodejs20.x
      CodeUri: ./src

  SendMessageFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.sendMessage
      Runtime: nodejs20.x
      CodeUri: ./src
```