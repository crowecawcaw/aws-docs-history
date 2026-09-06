

# Handle host replacement and connection stalling
<a name="best-practices-ecs-eks-host-replacement"></a>

When Neptune replaces a host (for example, during maintenance or failover), existing connections to that host become invalid. In containerized environments, this can stall all threads in a container if the client doesn't handle the replacement gracefully.

**Use current client versions**

If you use the Gremlin query language, use a TinkerPop driver version that is compatible with your Neptune engine version (see [Accessing a Neptune graph with Gremlin](access-graph-gremlin.md) for the compatibility table). If you use the Java driver, consider `neptune-gremlin-client` — a wrapper around the TinkerPop Java driver that adds connection management features like endpoint health checking and failover handling. It follows the same version compatibility rules as the underlying TinkerPop driver.

Use `neptune-gremlin-client` version 3.x (or at minimum version 2.0.7), depending on what your Neptune version allows. These newer versions improve resiliency and connection handling.

For openCypher users with the Neo4j driver, close and recreate the `Driver` object when you detect a connection failure during failover. Neptune supports Bolt protocol versions 1 through 4.0. For more information, see [Neptune Best Practices Using openCypher and Bolt](best-practices-opencypher.md).

**Use cluster or reader endpoints**

Don't connect to instance endpoints directly. Use the cluster endpoint for writes and the reader endpoint for reads. If you must use instance endpoints with `neptune-gremlin-client`, enable endpoint health-check filtering through the `/status` API.

**Configure liveness probes with tolerance**

Set your Kubernetes liveness probe `failureThreshold` to at least 30 with a 10-second period (300 seconds total). This prevents Kubernetes from restarting pods during the approximately 5-minute window when Neptune is completing a host replacement.

**Implement retry with backoff**

A single failed request during host replacement shouldn't crash the container. Implement retry logic with exponential backoff on connection failures so that transient errors during replacement resolve without intervention. For guidance on retryable exceptions, see [Neptune transaction exceptions](https://docs.aws.amazon.com/neptune/latest/userguide/transactions-exceptions.html).