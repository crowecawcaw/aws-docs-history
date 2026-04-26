# RouteConfiguration

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
ApiKeyRequired: `Boolean`
FunctionArn: `String`
IntegrationTimeout: `Integer`
ModelSelectionExpression: `String`
OperationName: `String`
RequestModels: `Json`
RequestParameters: `Json`
RouteResponseSelectionExpression: `String`

```

## Properties

`ApiKeyRequired`

Specifies whether an API key is required for this route.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`ApiKeyRequired` property of an
`AWS::ApiGatewayV2::Route` resource.

`FunctionArn`

The ARN of the Lambda function that handles this route. AWS SAM creates an integration and the necessary permissions for API Gateway to invoke the function.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`IntegrationTimeout`

The timeout for the integration, in milliseconds. The maximum value is 29,000 milliseconds (29 seconds).

_Type_: Integer

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`TimeoutInMillis` property of an
`AWS::ApiGatewayV2::Integration` resource.

`ModelSelectionExpression`

The model selection expression for the route.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`ModelSelectionExpression` property of an
`AWS::ApiGatewayV2::Route` resource.

`OperationName`

The operation name for the route.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`OperationName` property of an
`AWS::ApiGatewayV2::Route` resource.

`RequestModels`

The request models for the route.

_Type_: Json

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`RequestModels` property of an
`AWS::ApiGatewayV2::Route` resource.

`RequestParameters`

The request parameters for the route.

_Type_: Json

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`RequestParameters` property of an
`AWS::ApiGatewayV2::Route` resource.

`RouteResponseSelectionExpression`

The route response selection expression for the route.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`RouteResponseSelectionExpression` property of an
`AWS::ApiGatewayV2::Route` resource.

## Examples

### Simple Route

The following example configures a simple route.

```
Routes:
  $connect:
    FunctionArn: !GetAtt ConnectFunction.Arn
  sendMessage:
    FunctionArn: !GetAtt SendMessageFunction.Arn
    OperationName: SendMessage

```
