# Create AWS service

integrations for HTTP APIs in API Gateway

You can integrate your HTTP API with AWS services by using _first-class
integrations_. A first-class integration connects an HTTP API route to an
AWS service API. When a client invokes a route that's backed by a first-class integration,
API Gateway invokes an AWS service API for you. For example, you can use first-class integrations
to send a message to an Amazon Simple Queue Service queue, or to start an AWS Step Functions state machine. For
supported service actions, see [Integration subtype reference](http-api-develop-integrations-aws-services-reference.md "http-api-develop-integrations-aws-services-reference.md").

## Mapping

request parameters

First-class integrations have required and optional parameters. You must configure all
required parameters to create an integration. You can use static values or map
parameters that are dynamically evaluated at runtime. For a full list of supported
integrations and parameters, see [Integration subtype reference](http-api-develop-integrations-aws-services-reference.md "http-api-develop-integrations-aws-services-reference.md").

The following table describes the supported mapping request parameters.

| Type                     | Example                        | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------ | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Header value             | $request.header.`name`         | Header names are case-insensitive. API Gateway combines multiple header values<br>with commas, for example `"header1":<br>"value1,value2"`.                                                                                                                                                                                                                                                                                                                   |
| Query string value       | $request.querystring.`name`    | Query string names are case-sensitive. API Gateway combines multiple values with<br>commas, for example `"querystring1":<br>"Value1,Value2"`.                                                                                                                                                                                                                                                                                                                 |
| Path parameter           | $request.path.`name`           | The value of a path parameter in the request. For example if the<br>route is `/pets/{petId}`, you can map the `petId`<br>parameter from the request with<br>`$request.path.petId`.                                                                                                                                                                                                                                                                            |
| Request body passthrough | $request.body                  | API Gateway passes the entire request body through.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Request body             | $request.body.`name`           | A [JSON path expression](https://goessner.net/articles/JsonPath/index.html#e2 "https://goessner.net/articles/JsonPath/index.html#e2"). Recursive descent<br>(`$request.body..`name``)<br>and filter expressions<br>(`?(`expression`)`) aren't<br>supported.<br>NoteWhen you specify a JSON path, API Gateway truncates the request body at 100 KB and then applies the<br>selection expression. To send payloads larger than 100 KB, specify `$request.body`. |
| Context variable         | $context.`variableName`        | The value of a supported [context variable](http-api-logging-variables.md "http-api-logging-variables.md").                                                                                                                                                                                                                                                                                                                                                   |
| Stage variable           | $stageVariables.`variableName` | The value of a [stage<br>variable](http-api-stages.md "http-api-stages.md").                                                                                                                                                                                                                                                                                                                                                                                  |
| Static value             | `string`                       | A constant value.                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Create a

first-class integration

Before you create a first-class integration, you must create an IAM role that grants
API Gateway permissions to invoke the AWS service action that you're integrating with. To
learn more, see [Creating a role for an
AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

To create a first-class integration, choose a supported AWS service action, such as
`SQS-SendMessage`, configure the request parameters, and provide a role
that grants API Gateway permissions to invoke the integrated AWS service API. Depending on
the integration subtype, different request parameters are required. To learn more, see
[Integration subtype reference](http-api-develop-integrations-aws-services-reference.md "http-api-develop-integrations-aws-services-reference.md").

The following
[create-integration](../../../cli/latest/reference/apigatewayv2/create-integration.md "../../../cli/latest/reference/apigatewayv2/create-integration.md") command creates an integration that sends an Amazon SQS message:

```
aws apigatewayv2 create-integration \
    --api-id abcdef123 \
    --integration-subtype SQS-SendMessage \
    --integration-type AWS_PROXY \
    --payload-format-version 1.0 \
    --credentials-arn arn:aws:iam::123456789012:role/apigateway-sqs \
    --request-parameters '{"QueueUrl": "$request.header.queueUrl", "MessageBody": "$request.body.message"}'
```

## Create a

first-class integration using CloudFormation

The following example shows an CloudFormation snippet that creates a `/{source}/{detailType}` route with a first-class integration with Amazon EventBridge.

The
`Source` parameter is mapped to the `{source}` path parameter, the `DetailType` is mapped to the `{DetailType}` path parameter, and the `Detail` parameter is mapped to the request body.

The snippet does not show the event bus or the IAM role that grants API Gateway permissions to invoke the `PutEvents` action.

```
Route:
    Type: AWS::ApiGatewayV2::Route
    Properties:
      ApiId: !Ref HttpApi
      AuthorizationType: None
      RouteKey: 'POST /{source}/{detailType}'
      Target: !Join
        - /
        - - integrations
          - !Ref Integration
  Integration:
    Type: AWS::ApiGatewayV2::Integration
    Properties:
      ApiId: !Ref HttpApi
      IntegrationType: AWS_PROXY
      IntegrationSubtype: EventBridge-PutEvents
      CredentialsArn: !GetAtt EventBridgeRole.Arn
      RequestParameters:
        Source: $request.path.source
        DetailType: $request.path.detailType
        Detail: $request.body
        EventBusName: !GetAtt EventBus.Arn
      PayloadFormatVersion: "1.0"
```
