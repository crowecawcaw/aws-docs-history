For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Endpoints and connectivity for Timestream for InfluxDB 3

Amazon Timestream for InfluxDB 3 provides multiple endpoints to connect to your cluster, allowing
for flexible access patterns based on your application needs.

## Endpoint types

### Cluster endpoint

The cluster endpoint (or primary endpoint) provides access to the writer nodes in your
cluster. This endpoint:

- Supports both read and write operations.
- Automatically routes traffic to available writer nodes.
- Is the only endpoint that can perform write operations.
- Should be used for administrative operations and data ingestion.

Example
format: `clusterid-wmyjrrjko.timestream-influxdb-alpha.us-west-2.on.aws`

### Reader endpoint

The reader endpoint connects to the reader nodes in your cluster. This endpoint:

- Supports read-only operations (queries).
- Automatically distributes read traffic across all available reader nodes.
- Helps offload query workload from writer nodes.
- Is ideal for reporting and dashboard applications.

Example
format: `clusterid-wmyjrrjko-ro.timestream-influxdb-alpha.us-west-2.on.aws`

### Node-specific endpoints

In addition to the cluster endpoints, you can connect directly to specific nodes within
your cluster:

- Provides direct access to individual nodes for diagnostics or specific workloads.
- Allows for fine-grained control over connection routing.
- Useful for troubleshooting or when you need to isolate specific operations.
- **Important**: During any issue or failover scenario,
  node-specific endpoints will be temporarily unavailable while the node recovers or is
  replaced.

Example format: `nodeid-wmyjrrjko.timestream-influxdb-alpha.us-west-2.on.aws`

### Traffic distribution

When using cluster-level endpoints (writer/reader and reader endpoints), the traffic
distribution system automatically:

- Distributes traffic to active nodes based on:
  - Node health and availability.
  - Current workload on each node.
  - Node role (writer/reader).

- **Makes specific node unavailability transparent to clients** by
  automatically routing traffic away from unhealthy or unavailable nodes.
- Provides seamless failover without requiring client-side configuration changes.
- Ensures continuous service availability even during maintenance or unexpected node
  failures.

This automatic traffic distribution provides:

- **High availability**: Client connections remain uninterrupted
  even when individual nodes become unavailable.
- **Load balancing**: Traffic is distributed across available
  nodes for optimal performance.
- **Fault tolerance**: Automatic failover ensures minimal impact
  during node failures.
- **Simplified connection management**: Applications don't need to
  handle node-level failures.

### Connection best practices

For optimal performance and reliability:

- **Use cluster-level endpoints for production workloads**: The
  writer/reader and reader endpoints provide automatic failover and transparent handling of
  node unavailability.
- Use the writer/reader endpoint for write operations and administrative tasks.
- Use the reader endpoint for read-heavy applications like dashboards and reports.
- **Avoid node-specific endpoints for critical applications**:
  These endpoints will be unavailable during failover scenarios and don't provide automatic
  traffic redistribution.
- Reserve node-specific endpoints for diagnostics, troubleshooting, or when you need to
  isolate specific operations.
- Implement connection pooling in your applications to efficiently manage connections.
- Configure appropriate timeouts and retry logic in your client applications.

By leveraging the cluster-level endpoints and their automatic traffic distribution
capabilities, you can ensure your applications maintain continuous connectivity and optimal
performance even during node-level failures or maintenance events.
