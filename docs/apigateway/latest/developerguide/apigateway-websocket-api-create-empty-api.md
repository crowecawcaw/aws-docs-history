

# Create WebSocket APIs in API Gateway
<a name="apigateway-websocket-api-create-empty-api"></a>

You can create a WebSocket API in the API Gateway console, by using the AWS CLI [create-api](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/create-api.html) command, or by using the `CreateApi` command in an AWS SDK. The following procedures show how to create a new WebSocket API.

**Note**  
WebSocket APIs only support TLS 1.2 and TLS 1.3. Earlier TLS versions are not supported.

## Create a WebSocket API using AWS CLI commands
<a name="apigateway-websocket-api-create-using-awscli"></a>

The following [create-api](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/create-api.html) command creates an API with the `$request.body.action` route selection expression:

```
aws apigatewayv2 --region us-east-1 create-api --name "myWebSocketApi3" --protocol-type WEBSOCKET --route-selection-expression '$request.body.action'
```

The output looks like the following:

```
{
    "ApiKeySelectionExpression": "$request.header.x-api-key",
    "Name": "myWebSocketApi3",
    "CreatedDate": "2018-11-15T06:23:51Z",
    "ProtocolType": "WEBSOCKET",
    "RouteSelectionExpression": "'$request.body.action'",
    "ApiId": "aabbccddee"
}
```

## Create a WebSocket API using the API Gateway console
<a name="apigateway-websocket-api-create-using-console"></a>

You can create a WebSocket API in the console by choosing the WebSocket protocol and giving the API a name.

**Important**  
Once you have created the API, you cannot change the protocol you have chosen for it. There is no way to convert a WebSocket API into a REST API or vice versa.

**To create a WebSocket API using the API Gateway console**

1. Sign in to the API Gateway console and choose **Create API**.

1. Under **WebSocket API**, choose **Build**. Only Regional endpoints are supported.

1. For **API name**, enter the name of your API.

1. For **Route selection expression**, enter a value. For example, `$request.body.action`. 

   For more information about route selection expressions, see [Route selection expressions](websocket-api-develop-routes.md#apigateway-websocket-api-route-selection-expressions).

1. Do one of the following:
   + Choose **Create blank API** to create an API with no routes.
   + Choose **Next** to attach routes to your API.

   You can attach routes after you create your API.