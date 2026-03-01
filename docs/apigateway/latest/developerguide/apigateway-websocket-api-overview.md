# Overview of WebSocket APIs in API Gateway

In API Gateway you can create a WebSocket API as a stateful frontend for an AWS service (such
as Lambda or DynamoDB) or for an HTTP endpoint. The WebSocket API invokes your backend based on
the content of the messages it receives from client apps.

Unlike a REST API, which receives and responds to requests, a WebSocket API supports
two-way communication between client apps and your backend. The backend can send callback
messages to connected clients.

In your WebSocket API, incoming JSON messages are directed to backend integrations based
on routes that you configure. (Non-JSON messages are directed to a `$default`
route that you configure.)

A _route_ includes a _route key_, which is the value
that is expected once a _route selection expression_ is evaluated. The
`routeSelectionExpression` is an attribute defined at the API level. It
specifies a JSON property that is expected to be present in the message payload. For more
information about route selection expressions, see [Route selection expressions](websocket-api-develop-routes.md#apigateway-websocket-api-route-selection-expressions "websocket-api-develop-routes.md#apigateway-websocket-api-route-selection-expressions").

For example, if your JSON messages contain an `action` property, and you want
to perform different actions based on this property, your route selection expression might
be `${request.body.action}`. Your routing table would specify which action to
perform by matching the value of the `action` property against the custom route
key values that you have defined in the table.

## Use routes for a WebSocket API

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

For more information about the `$connect` and `$disconnect` routes,
see [Manage connected users and client apps: $connect and $disconnect routes](apigateway-websocket-api-route-keys-connect-disconnect.md "apigateway-websocket-api-route-keys-connect-disconnect.md").

For more information about the `$default` route and custom routes, see [Invoke your backend integration with the $default Route and custom routes in API Gateway](apigateway-websocket-api-routes-integrations.md "apigateway-websocket-api-routes-integrations.md").

## Send data to connected client apps

Backend services can send data to connected client apps. You can send data by doing the following:

- Use an integration to send a response, which is returned to the client by a route
  response that you have defined.
- You can use the `@connections` API to send a POST request. For more
  information, see [Use @connections commands in your backend service](apigateway-how-to-call-websocket-api-connections.md "apigateway-how-to-call-websocket-api-connections.md").

## WebSocket API status codes

API Gateway WebSocket APIs use the following status codes for communication from the
server to client as described in the
[WebSocket Close Code
Number Registry](https://www.iana.org/assignments/websocket/websocket.xhtml#close-code-number "https://www.iana.org/assignments/websocket/websocket.xhtml#close-code-number"):

1001

API Gateway returns this status code when the client is idle for 10 minutes or
reaches the maximum 2 hour connection lifetime.

1003

API Gateway returns this status code when an endpoint receives a binary media type. Binary media types
aren't supported for WebSocket APIs.

1005
API Gateway returns this status code if the client sends a close frame without a closure code.

1006
API Gateway returns this status code if there is an unexpected closure of the connection, such as the TCP connection closed without a WebSocket close frame.

1008

API Gateway returns this status code when an endpoint receives too many requests from a particular client.

1009

API Gateway returns this status code when an endpoint receives a message that is too big for it to
process.

1011
API Gateway returns this status code when there is an internal server error.

1012

API Gateway returns this status code if the service restarts.
