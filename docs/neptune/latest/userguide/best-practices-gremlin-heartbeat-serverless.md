

# Heartbeat Configuration for Neptune Serverless
<a name="best-practices-gremlin-heartbeat-serverless"></a>

When using Gremlin WebSocket clients with Neptune Serverless, you need to configure the client's ping interval appropriately to maintain stable connections during scaling events. The Gremlin client uses WebSocket connections and sends periodic pings to verify the connection is active. The client expects a response from the server within the ping interval timeframe. If the server doesn't respond, the client automatically closes the connection.

For Neptune **provisioned** instances, we recommend setting the ping interval to **5 seconds**. For Neptune **Serverless clusters**, we recommend setting the ping interval to at least **20 seconds** to accommodate potential delays during scaling operations. This parameter controls how long the client waits between writes to the server before sending a ping to verify the connection is still active.

The configuration of this parameter varies depending on the client implementation:

**Java Client Configuration**

For the Java TinkerPop Gremlin client, configure the `keepAliveInterval` parameter:

```
Cluster.Builder builder = Cluster.build()
    .addContactPoint(endpoint)
    .keepAliveInterval(20000); // Configure ping interval in milliseconds
```

For more details about the Java driver configuration, refer to the [Java TinkerPop documentation](https://tinkerpop.apache.org/docs/current/reference/#gremlin-java-configuration).

**Go Client Configuration**

For the Gremlin Go client, configure the `KeepAliveInterval` parameter:

```
rc, err := driver.NewDriverRemoteConnection(endpoint,
    func(settings *driver.DriverRemoteConnectionSettings) {
        settings.TraversalSource = "g"
        settings.AuthInfo = auth
        settings.KeepAliveInterval = 20 * time.Second // Configure ping interval
        ...
    })
```

For more details about the Go driver configuration, refer to the [Go TinkerPop documentation](https://tinkerpop.apache.org/docs/current/reference/#gremlin-go-configuration).

**JavaScript/Node.js Client Configuration**

For the JavaScript/Node.js Gremlin client, configure the `pingInterval` parameter:

```
const gremlin = require('gremlin');
const DriverRemoteConnection = gremlin.driver.DriverRemoteConnection;

const connection = new DriverRemoteConnection(endpoint, {
    traversalSource: 'g',
    pingInterval: 20000  // Configure ping interval in milliseconds
});
```

For more details about the JavaScript driver configuration, refer to the [JavaScript TinkerPop documentation](https://tinkerpop.apache.org/docs/current/reference/#gremlin-javascript-configuration).

**Python Client Configuration**

For the Python Gremlin client, the ping interval is typically managed at the transport layer. Consult the specific transport implementation documentation for configuration options:

```
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

g = traversal().with_remote(
    DriverRemoteConnection('wss://your-neptune-endpoint:your-neptune-port/gremlin','g',
        transport_factory=lambda: AiohttpTransport(read_timeout=60,
                                                    write_timeout=20,
                                                    heartbeat=20, // Configure heartbeat
                                                    call_from_event_loop=True,
                                                    max_content_length=100*1024*1024,
                                                    ssl_options=ssl.create_default_context(Purpose.CLIENT_AUTH))))
```

For more details about the Python driver configuration, refer to the [Python TinkerPop documentation](https://tinkerpop.apache.org/docs/current/reference/#gremlin-python-configuration).

This configuration ensures your client maintains connection stability during Neptune Serverless scaling events, preventing unnecessary connection closures and improving application reliability.