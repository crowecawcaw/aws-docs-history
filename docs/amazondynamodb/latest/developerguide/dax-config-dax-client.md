# Configuring your DAX client

The DAX cluster is an instance-based cluster that can be accessed using various DAX SDKs.
Each SDK provides developers with configurable options, such as requestTimeout and connections,
to meet specific application requirements.

When configuring your DAX client, a crucial
consideration is your client application's scale—specifically, the ratio of client instances
to DAX server instances (which has a maximum of 11). Large client instance fleets can generate
numerous connections to DAX server instances, potentially overwhelming them.
This guide outlines best practices for DAX client configuration.

## Best practices

1. **Client instances** – Implement singleton client
   instances to ensure instance reuse across requests. For implementation
   details, see [Step 4: Run a sample application](DAX.client.md "DAX.client.md").
2. **Request timeouts** – While applications often
   require low request timeouts to ensure minimal latency for upstream systems, setting timeouts too
   low can cause problems. Low timeouts may trigger frequent reconnection to server instances when
   DAX servers experience temporary latency spikes. When a timeout occurs, the DAX client terminates
   the existing server node connection and establishes a new one. Since connection establishment is
   resource-intensive, numerous consecutive connections can overload DAX servers. We recommend the following:
   - Maintaining default request timeout settings.
   - If lower timeouts are necessary, implement separate application threads with lower timeout values
     and include retry mechanisms with exponential back-off.

3. **Connection timeout** – For most applications, we recommend maintaining the
   default connection timeout settings.
4. **Concurrent connections** – Certain SDKs, such as JavaV2, allow adjustment
   of concurrent connections to the DAX server. Key considerations:
   - DAX server instances can handle up to 40,000 concurrent connections.
   - Default settings are suitable for most use cases.
   - Large client instances combined with high concurrent connections may overload servers.
   - Lower concurrent connection values reduce server overload risk.
   - Performance calculation example:
     - Assuming 1ms request latency, each connection can theoretically
       handle 1,000 requests/second.
     - For a 3-node cluster, a single client instance connecting to all nodes
       can process 3,000 requests/second.
     - With 10 connections, the client can handle approximately 30,000 requests/second.

     Recommendation – Begin with lower concurrent connection settings and validate through
     performance testing with expected production workload patterns.
