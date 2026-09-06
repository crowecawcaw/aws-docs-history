

# RouteConfiguration
<a name="sam-property-websocketapi-routeconfiguration"></a>

## Syntax
<a name="sam-property-websocketapi-routeconfiguration-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-websocketapi-routeconfiguration-syntax.yaml"></a>

```
[ApiKeyRequired](#sam-routeconfiguration-apikeyrequired): {{Boolean}}
[FunctionArn](#sam-routeconfiguration-functionarn): {{String}}
[IntegrationTimeout](#sam-routeconfiguration-integrationtimeout): {{Integer}}
[ModelSelectionExpression](#sam-routeconfiguration-modelselectionexpression): {{String}}
[OperationName](#sam-routeconfiguration-operationname): {{String}}
[RequestModels](#sam-routeconfiguration-requestmodels): {{Json}}
[RequestParameters](#sam-routeconfiguration-requestparameters): {{Json}}
[RouteResponseSelectionExpression](#sam-routeconfiguration-routeresponseselectionexpression): {{String}}
```

## Properties
<a name="sam-property-websocketapi-routeconfiguration-properties"></a>

 `ApiKeyRequired`   <a name="sam-routeconfiguration-apikeyrequired"></a>
Specifies whether an API key is required for this route.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ApiKeyRequired](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apikeyrequired)` property of an `AWS::ApiGatewayV2::Route` resource.

 `FunctionArn`   <a name="sam-routeconfiguration-functionarn"></a>
The ARN of the Lambda function that handles this route. AWS SAM creates an integration and the necessary permissions for API Gateway to invoke the function.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `IntegrationTimeout`   <a name="sam-routeconfiguration-integrationtimeout"></a>
The timeout for the integration, in milliseconds. The maximum value is 29,000 milliseconds (29 seconds).  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[TimeoutInMillis](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-timeoutinmillis)` property of an `AWS::ApiGatewayV2::Integration` resource.

 `ModelSelectionExpression`   <a name="sam-routeconfiguration-modelselectionexpression"></a>
The model selection expression for the route.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ModelSelectionExpression](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-modelselectionexpression)` property of an `AWS::ApiGatewayV2::Route` resource.

 `OperationName`   <a name="sam-routeconfiguration-operationname"></a>
The operation name for the route.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[OperationName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-operationname)` property of an `AWS::ApiGatewayV2::Route` resource.

 `RequestModels`   <a name="sam-routeconfiguration-requestmodels"></a>
The request models for the route.  
*Type*: Json  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[RequestModels](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestmodels)` property of an `AWS::ApiGatewayV2::Route` resource.

 `RequestParameters`   <a name="sam-routeconfiguration-requestparameters"></a>
The request parameters for the route.  
*Type*: Json  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[RequestParameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestparameters)` property of an `AWS::ApiGatewayV2::Route` resource.

 `RouteResponseSelectionExpression`   <a name="sam-routeconfiguration-routeresponseselectionexpression"></a>
The route response selection expression for the route.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[RouteResponseSelectionExpression](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routeresponseselectionexpression)` property of an `AWS::ApiGatewayV2::Route` resource.

## Examples
<a name="sam-property-websocketapi-routeconfiguration-examples"></a>

### Simple Route
<a name="sam-property-websocketapi-routeconfiguration-examples-simple"></a>

The following example configures a simple route.

```
Routes:
  $connect:
    FunctionArn: !GetAtt ConnectFunction.Arn
  sendMessage:
    FunctionArn: !GetAtt SendMessageFunction.Arn
    OperationName: SendMessage
```