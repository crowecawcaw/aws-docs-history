# AWS::Serverless::WebSocketApi

Creates an Amazon API Gateway WebSocket API, which enables you to create two-way interactive communication applications. WebSocket APIs allow the server to send messages to clients without the client having to request them. For more information, see [Working with WebSocket APIs](../../../apigateway/latest/developerguide/apigateway-websocket-api.md "../../../apigateway/latest/developerguide/apigateway-websocket-api.md") in the _API Gateway Developer Guide_.

We recommend that you use CloudFormation hooks or IAM policies to verify that API Gateway resources have
authorizers attached to them to control access to them.

For more information about using CloudFormation hooks, see [Registering hooks](../../../cloudformation-cli/latest/userguide/registering-hook-python.md "../../../cloudformation-cli/latest/userguide/registering-hook-python.md") in the _CloudFormation CLI user guide_ and
the [apigw-enforce-authorizer](https://github.com/aws-cloudformation/aws-cloudformation-samples/tree/main/hooks/python-hooks/apigw-enforce-authorizer/ "https://github.com/aws-cloudformation/aws-cloudformation-samples/tree/main/hooks/python-hooks/apigw-enforce-authorizer/") GitHub repository.

For more information about using IAM policies, see [Require that API routes have authorization](../../../apigateway/latest/developerguide/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-require-authorization "../../../apigateway/latest/developerguide/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-require-authorization") in the _API Gateway Developer Guide_.

###### Note

When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation resources.
For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
Type: AWS::Serverless::WebSocketApi
Properties:
  ApiKeySelectionExpression: `String`
  AccessLogSettings: `AccessLogSettings`
  Auth: `WebSocketApiAuth`
  DefaultRouteSettings: `RouteSettings`
  Description: `String`
  DisableExecuteApiEndpoint: `Boolean`
  DisableSchemaValidation: `Boolean`
  Domain: `WebSocketApiDomainConfiguration`
  IpAddressType: `String`
  Name: `String`
  PropagateTags: `Boolean`
  Routes: `RouteConfiguration`
  RouteSelectionExpression: `String`
  RouteSettings: `RouteSettings`
  StageName: `String`
  StageVariables: `Json`
  Tags: `Map`

```

## Properties

`ApiKeySelectionExpression`

An API key selection expression. For more information, see [API Key Selection Expressions](../../../apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.md#apigateway-websocket-api-apikey-selection-expressions "../../../apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.md#apigateway-websocket-api-apikey-selection-expressions") in the _API Gateway Developer Guide_.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`ApiKeySelectionExpression` property of an
`AWS::ApiGatewayV2::Api` resource.

`AccessLogSettings`

The settings for access logging in a stage.

_Type_: [AccessLogSettings](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-accesslogsettings "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-accesslogsettings")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`AccessLogSettings` property of an
`AWS::ApiGatewayV2::Stage` resource.

`Auth`

Configures authorization for controlling access to your WebSocket API. Authorization is applied to the `$connect` route.

For more information, see [Controlling access to WebSocket APIs](../../../apigateway/latest/developerguide/apigateway-websocket-api-control-access.md "../../../apigateway/latest/developerguide/apigateway-websocket-api-control-access.md") in the _API Gateway Developer Guide_.

_Type_: [WebSocketApiAuth](sam-property-websocketapi-websocketapiauth.md "sam-property-websocketapi-websocketapiauth.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`DefaultRouteSettings`

The default route settings for this WebSocket API. These settings apply to all routes
unless overridden by the `RouteSettings` property for certain routes.

_Type_: [RouteSettings](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-routesettings "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-routesettings")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`DefaultRouteSettings` property of an `AWS::ApiGatewayV2::Stage`
resource.

`Description`

A description of the WebSocket API.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Description` property of an
`AWS::ApiGatewayV2::Api` resource.

`DisableExecuteApiEndpoint`

Specifies whether clients can invoke your API by using the default
`execute-api` endpoint. To require that clients use a custom domain name to
invoke your API, disable the default endpoint.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`DisableExecuteApiEndpoint` property of an
`AWS::ApiGatewayV2::Api` resource.

`DisableSchemaValidation`

Avoid validating models when creating a deployment.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`DisableSchemaValidation` property of an
`AWS::ApiGatewayV2::Api` resource.

`Domain`

Configures a custom domain for this WebSocket API.

###### Note

WebSocket APIs do not support mutual TLS authentication (MTLS). If you specify `MutualTlsAuthentication` or `OwnershipVerificationCertificateArn`, AWS SAM will return an error.

_Type_: [WebSocketApiDomainConfiguration](sam-property-websocketapi-websocketapidomainconfiguration.md "sam-property-websocketapi-websocketapidomainconfiguration.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`IpAddressType`

The IP address type for the API. Valid values are `ipv4` for IPv4 only and `dualstack` for IPv4 and IPv6.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`IpAddressType` property of an
`AWS::ApiGatewayV2::Api` resource.

`Name`

A name for the WebSocket API. If you don't specify a name, AWS SAM generates a name for you.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::ApiGatewayV2::Api`
resource.

`PropagateTags`

If `true`, AWS SAM adds the `Tags` property to the
`AWS::ApiGatewayV2::Stage` and `AWS::ApiGatewayV2::DomainName`
resources that AWS SAM generates.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`Routes`

The route configurations for this WebSocket API. Routes define how messages are routed to Lambda functions. Each route consists of a route key and a Lambda function ARN.

WebSocket APIs support three predefined routes: `$connect`, `$disconnect`, and `$default`. You can also define custom routes.

_Type_: [RouteConfiguration](sam-property-websocketapi-routeconfiguration.md "sam-property-websocketapi-routeconfiguration.md")

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`RouteSelectionExpression`

The route selection expression for the WebSocket API. For more information, see [Route Selection Expressions](../../../apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.md#apigateway-websocket-api-route-selection-expressions "../../../apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.md#apigateway-websocket-api-route-selection-expressions") in the _API Gateway Developer Guide_.

A common value is `$request.body.action`, which routes messages based on an `action` field in the message body.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`RouteSelectionExpression` property of an
`AWS::ApiGatewayV2::Api` resource.

`RouteSettings`

The route settings for this WebSocket API. These settings override the
`DefaultRouteSettings` for specific routes.

_Type_: [RouteSettings](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-routesettings "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-routesettings")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`RouteSettings` property of an `AWS::ApiGatewayV2::Stage`
resource.

`StageName`

The name of the API stage. If you don't specify a name, AWS SAM uses `default` as the stage name.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`StageName` property of an `AWS::ApiGatewayV2::Stage`
resource.

`StageVariables`

A map that defines the stage variables. Variable names can have alphanumeric and
underscore characters, and the values must match `[A-Za-z0-9-._~:/?#&=,]+`.

_Type_: [Json](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-stagevariables "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.md#cfn-apigatewayv2-stage-stagevariables")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`StageVariables` property of an `AWS::ApiGatewayV2::Stage`
resource.

`Tags`

A map (string to string) that specifies the tags to be added to this WebSocket API. For details about valid keys and values for tags, see [Resource tag](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md") in the
_CloudFormation User Guide_.

_Type_: Map

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref`
function, `Ref` returns the API ID of the underlying
`AWS::ApiGatewayV2::Api` resource, for example, `a1bcdef2gh`.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

## Examples

### Simple WebSocket API

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
