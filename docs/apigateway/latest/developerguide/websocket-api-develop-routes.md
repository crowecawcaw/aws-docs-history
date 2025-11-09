# Create routes for WebSocket APIs in API Gateway

In your WebSocket API, incoming JSON messages are directed to backend integrations based
on routes that you configure. (Non-JSON messages are directed to a `$default`
route that you configure.)

A _route_ includes a _route key_, which is the value
that is expected once a _route selection expression_ is evaluated. The
`routeSelectionExpression` is an attribute defined at the API level. It
specifies a JSON property that is expected to be present in the message payload. For more
information about route selection expressions, see [Route selection
expressions](#apigateway-websocket-api-route-selection-expressions "#apigateway-websocket-api-route-selection-expressions").

For example, if your JSON messages contain an `action` property and you want to
perform different actions based on this property, your route selection expression might be
`${request.body.action}`. Your routing table would specify which action to
perform by matching the value of the `action` property against the custom route
key values that you have defined in the table.

There are three predefined routes that can be used: `$connect`,
`$disconnect`, and `$default`. In addition, you can create custom
routes.

- API Gateway calls the `$connect` route when a persistent connection between
  the client and a WebSocket API is being initiated.
- API Gateway calls the `$disconnect` route when the client or the server
  disconnects from the API.
- API Gateway calls a custom route after the route selection expression is evaluated
  against the message if a matching route is found; the match determines which
  integration is invoked.
- API Gateway calls the `$default` route if the route selection expression
  cannot be evaluated against the message or if no matching route is found.

## Route selection

expressions

A _route selection expression_ is evaluated when the service is
selecting the route to follow for an incoming message. The service uses the route whose
`routeKey` exactly matches the evaluated value. If none match and a route
with the `$default` route key exists, that route is selected. If no routes
match the evaluated value and there is no `$default` route, the service
returns an error. For WebSocket-based APIs, the expression should be of the form
`$request.body.`{path_to_body_element}``.

For example, suppose you are sending the following JSON message:

```
{
    "service" : "chat",
    "action" : "join",
    "data" : {
        "room" : "room1234"
   }
}
```

You might want to select your API's behavior based on the `action`
property. In that case, you might define the following route selection
expression:

```
$request.body.action
```

In this example, `request.body` refers to your message's JSON payload, and
`.action` is a [JSONPath](https://goessner.net/articles/JsonPath/ "https://goessner.net/articles/JsonPath/") expression. You can use any JSON path expression after
`request.body`, but keep in mind that the result will be stringified. For
example, if your JSONPath expression returns an array of two elements, that will be
presented as the string `"[item1, item2]"`. For this reason, it's a good
practice to have your expression evaluate to a value and not an array or an
object.

You can simply use a static value, or you can use multiple variables. The following
table shows examples and their evaluated results against the preceding payload.

| Expression                                           | Evaluated result | Description                                                   |
| ---------------------------------------------------- | ---------------- | ------------------------------------------------------------- |
| `$request.body.action`                               | `join`           | An unwrapped variable                                         |
| `${request.body.action}`                             | `join`           | A wrapped variable                                            |
| `${request.body.service}/${request.body.action}`     | `chat`/`join`    | Multiple variables with static values                         |
| `${request.body.action}-${request.body.invalidPath}` | `join-`          | If the JSONPath is not found, the variable is resolved as "". |
| `action`                                             | `action`         | Static value                                                  |
| `\$default`                                          | `$default`       | Static value                                                  |

The evaluated result is used to find a route. If there is a route with a matching
route key, the route is selected to process the message. If no matching route is found,
then API Gateway tries to find the `$default` route if available. If the
`$default` route is not defined, then API Gateway returns an error.

## Set up routes for a WebSocket API in

API Gateway

When you first create a new WebSocket API, there are three predefined routes:
`$connect`, `$disconnect`, and `$default`. You can
create them by using the console, API, or AWS CLI. If desired, you can create custom
routes. For more information, see [Overview of WebSocket APIs in API Gateway](apigateway-websocket-api-overview.md "apigateway-websocket-api-overview.md").

###### Note

In the CLI, you can create routes before or after you create integrations, and you
can reuse the same integration for multiple routes.

#### Create a route using

the API Gateway console

###### To create a route using the API Gateway console

1. Sign in to the API Gateway console, choose the API, and choose
   **Routes**.
2. Choose **Create route**
3. For **Route key**, enter the route key name. You can create the predefined routes (`$connect`,
   `$disconnect`, and `$default`), or a custom route.

###### Note

When you create a custom route, do not use the `$` prefix
in the route key name. This prefix is reserved for predefined
routes. 4. Select and configure the integration type for the route. For more information, see [Set up
a WebSocket API integration request using the API Gateway console](apigateway-websocket-api-integration-requests.md#apigateway-websocket-api-integration-request-using-console "apigateway-websocket-api-integration-requests.md#apigateway-websocket-api-integration-request-using-console").

#### Create a route using

the AWS CLI

The following [create-route](../../../cli/latest/reference/apigatewayv2/create-route.md "../../../cli/latest/reference/apigatewayv2/create-route.md") command creates a route:

```
aws apigatewayv2 --region us-east-1 create-route --api-id aabbccddee --route-key $default
```

The output will look like a following:

```
{
    "ApiKeyRequired": false,
    "AuthorizationType": "NONE",
    "RouteKey": "$default",
    "RouteId": "1122334"
}
```

#### Specify route

request settings for `$connect`

When you set up the `$connect` route for your API, the following
optional settings are available to enable authorization for your API. For more
information, see [The
$connect route](apigateway-websocket-api-route-keys-connect-disconnect.md#apigateway-websocket-api-routes-about-connect "apigateway-websocket-api-route-keys-connect-disconnect.md#apigateway-websocket-api-routes-about-connect").

- **Authorization**: If no authorization is needed, you can
  specify `NONE`. Otherwise, you can specify:
  - `AWS_IAM` to use standard AWS IAM policies to control
    access to your API.
  - `CUSTOM` to implement authorization for an API by
    specifying a Lambda authorizer function that you have previously
    created. The authorizer can reside in your own AWS account or a
    different AWS account. For more information about Lambda authorizers,
    see [Use API Gateway Lambda authorizers](apigateway-use-lambda-authorizer.md "apigateway-use-lambda-authorizer.md").

  ###### Note

  In the API Gateway console, the `CUSTOM` setting is
  visible only after you have set up an authorizer function as
  described in [Configure a Lambda authorizer (console)](configure-api-gateway-lambda-authorization.md#configure-api-gateway-lambda-authorization-with-console "configure-api-gateway-lambda-authorization.md#configure-api-gateway-lambda-authorization-with-console").

###### Important

The **Authorization** setting is applied to the
entire API, not just the `$connect` route. The
`$connect` route protects the other routes, because it is
called on every connection.

- **API key required**: You can optionally require an API
  key for an API's `$connect` route. You can use API keys together
  with usage plans to control and track access to your APIs. For more
  information, see [Usage plans and API keys for REST APIs in API Gateway](api-gateway-api-usage-plans.md "api-gateway-api-usage-plans.md").

#### Set

up the `$connect` route request using the API Gateway console

To set up the `$connect` route request for a WebSocket API using the
API Gateway console:

1. Sign in to the API Gateway console, choose the API, and choose
   **Routes**.
2. Under **Routes**, choose `$connect`, or create a `$connect` route by following [Create a route using
   the API Gateway console](#apigateway-websocket-api-route-using-console "#apigateway-websocket-api-route-using-console").
3. In the **Route request settings** section, choose **Edit**.
4. For **Authorization**, select an authorization type.
5. To require an API for the `$connect` route, select **Require API key**.
6. Choose **Save changes**.
