# API Gateway WebSocket APIs

A WebSocket API in API Gateway is a collection of WebSocket routes that are integrated with
backend HTTP endpoints, Lambda functions, or other AWS services. You can use API Gateway features
to help you with all aspects of the API lifecycle, from creation through monitoring your
production APIs.

API Gateway WebSocket APIs are bidirectional. A client can send messages to a service, and
services can independently send messages to clients. This bidirectional behavior enables
richer client/service interactions because services can push data to clients without
requiring clients to make an explicit request. WebSocket APIs are often used in real-time
applications such as chat applications, collaboration platforms, multiplayer games, and
financial trading platforms.

For an example app to get started with, see
[Tutorial: Create a WebSocket chat app with a WebSocket API, Lambda and
DynamoDB](websocket-api-chat-app.md "websocket-api-chat-app.md").

In this section, you can learn how to develop, publish, protect, and
monitor your WebSocket APIs using API Gateway.

###### Topics

- [Overview of WebSocket APIs in API Gateway](apigateway-websocket-api-overview.md "apigateway-websocket-api-overview.md")
- [Develop WebSocket APIs in API Gateway](websocket-api-develop.md "websocket-api-develop.md")
- [Publish WebSocket APIs for customers to invoke](websocket-api-publish.md "websocket-api-publish.md")
- [Protect your WebSocket APIs in API Gateway](websocket-api-protect.md "websocket-api-protect.md")
- [Monitor WebSocket APIs in API Gateway](websocket-api-monitor.md "websocket-api-monitor.md")
