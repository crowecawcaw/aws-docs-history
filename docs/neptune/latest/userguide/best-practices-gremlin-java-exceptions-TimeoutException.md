# Troubleshooting

`java.util.concurrent.TimeoutException`

The Gremlin Java client throws a `java.util.concurrent.TimeoutException`
when a Gremlin request times out at the client itself while waiting for a slot in one
of the WebSocket connections to become available. This timeout duration is controlled
by the `maxWaitForConnection` client-side configurable parameter.

###### Note

Because requests that time out at the client are never sent to the server,
they aren't reflected in any of the metrics captured at the server, such as
`GremlinRequestsPerSec`.

This kind of timeout is generally caused in one of two ways:

- **The server actually reached maximum capacity.**
  If this is the case, the queue on the server fills up, which you can detect by
  monitoring the [MainRequestQueuePendingRequests](cw-metrics.md#cw-metrics-available "cw-metrics.md#cw-metrics-available")
  CloudWatch metric. The number of parallel queries that the server can handle depends on
  its instance size.

If the `MainRequestQueuePendingRequests` metric doesn't show a
build-up of pending requests on the server, then the server can handle more requests
and the timeout is being caused by client-side throttling.

- **Client throttling of requests.**
  This can generally be fixed by changing client configuration settings.

The maximum number of parallel requests that the client can send can be roughly
estimated as follows:

```
maxParallelQueries = maxConnectionPoolSize * Max( maxSimultaneousUsagePerConnection, maxInProcessPerConnection )
```

Sending more than `maxParallelQueries` to the client causes
`java.util.concurrent.TimeoutException` exceptions. You can generally
fix this in several ways:

    + *Increase the connection timeout duration.*
     If latency is not crucial for your application, increase the client's
     `maxWaitForConnection` setting. The client then waits longer before
     it times out, which in turn can increase latency.
    + *Increase the maximum requests per connection.*
     This allows more requests to be sent using the same WebSocket connection.
     Do this by increasing the client's `maxSimultaneousUsagePerConnection`
     and `maxInProcessPerConnection` settings. These settings
     should generally have the same value.
    + *Increase the number of connections in the connection pool.*
     Do this by increasing the client's `maxConnectionPoolSize` setting.
     The cost is increased resource consumption, because each connection uses memory
     and an operating-system file descriptor, and requires an SSL and WebSocket
     handshake during initialization.
