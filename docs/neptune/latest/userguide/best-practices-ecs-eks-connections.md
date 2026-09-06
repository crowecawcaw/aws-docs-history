

# Manage connection pools and lifecycle in containerized environments
<a name="best-practices-ecs-eks-connections"></a>

Managing connections to Neptune effectively is essential in containerized environments where containers (pods in Kubernetes) start, stop, and scale frequently. Neptune enforces several WebSocket connection limits:
+ Each instance type has a maximum number of concurrent [WebSocket connections](https://docs.aws.amazon.com/neptune/latest/userguide/limits.html#limits-websockets)
+ Idle connections are closed after 20–25 minutes of inactivity
+ With IAM authentication, connections are force-closed after 10 days regardless of activity (see [WebSocket connection limits](https://docs.aws.amazon.com/neptune/latest/userguide/limits.html#limits-websockets))

Some drivers support periodic keep-alive heartbeats to prevent idle disconnects. For example, the Gremlin Java driver's `keepAliveInterval` sends a periodic ping to the server. Consult your specific driver's configuration options to determine what keep-alive settings are available and how they interact with Neptune's idle timeout.

Understanding these limits helps you design connection handling that works well with container orchestration patterns like rolling deployments, autoscaling, and container recycling. For general guidance on connection management with the Java Gremlin driver, see [Close the client to avoid the connections limit](best-practices-gremlin-java-close-connections.md) and [Create a new connection after failover](best-practices-gremlin-java-new-connection.md).

**Close connections on container shutdown**

Implement a graceful shutdown by adding a `SIGTERM` handler that closes your graph client before the container exits. For example, call Gremlin Java's `cluster.close()`, Gremlin's `driverRemoteConnection.close()` in Go or Python, or Bolt's `driver.close()` for the Neo4j driver. In Kubernetes, use a `preStop` hook to drain connections before `SIGTERM` is sent, especially during rolling updates.

**Note**  
Docker and Amazon ECS only deliver `SIGTERM` to PID 1 in the container. Use the exec form in your Dockerfile (for example, `ENTRYPOINT ["java", "-jar", "app.jar"]` not `ENTRYPOINT java -jar app.jar`) or an init process like `tini` to ensure your application receives the signal.

**Use a single client instance per container**

Creating multiple Gremlin `DriverRemoteConnection` or Bolt `neo4j.Driver` instances in the same container multiplies connection usage. Share a single client instance across all threads in the container. The client objects are thread-safe.

**Size connection pools relative to your fleet**

Set `maxConnectionPoolSize` so that the total connections across all containers don't exceed the Neptune instance connection limit. For example, if you run 20 containers with 8 threads each, calculate the per-container pool size so that 20 × pool size stays within the [instance limit for your instance type](https://docs.aws.amazon.com/neptune/latest/userguide/limits.html#limits-websockets). For more information about configuring connection pool sizes, see [Set `maxInProcessPerConnection` and `maxSimultaneousUsagePerConnection` to the same value](best-practices-gremlin-java-maxes.md).

**Set a connection wait timeout**

In the Java Gremlin driver, configure `maxWaitForConnection` to a reasonable value such as 5–10 seconds. The default is often infinite or very long, which causes threads to hang when the pool is exhausted rather than failing fast with a clear error. Not all language drivers support this setting—check your driver's documentation for the equivalent configuration option.