# Close the client to avoid the connections limit

It is important to close the client when you are finished with it to ensure that
the WebSocket connections are closed by the server and all resources associated with
the connections are released. This happens automatically if you close the cluster using
`Cluster.close( )`, because `client.close( )` is then called
internally.

If the client is not closed properly, Neptune terminates all idle WebSocket
connections after 20 to 25 minutes. However, if you don't explicitly close WebSocket
connections when you're done with them and the number of live connections reaches
the [WebSocket concurrent connection limit](limits.md#limits-websockets "limits.md#limits-websockets"),
additional connections are then refused with an HTTP `429`
error code. At that point, you must restart the Neptune instance to close the
connections.

The advice to call `cluster.close()` does not apply to Java AWS Lambda
functions. See [Managing Gremlin WebSocket connections in AWS Lambda functions](lambda-functions-websocket-connections.md "lambda-functions-websocket-connections.md") for details.
