# Accessing MemoryDB

Each MemoryDB cluster endpoint contains an address and a port. This cluster endpoint supports the Valkey and Redis OSS Cluster protocol to allow clients to discover the specific roles, ip addresses and slots for each node in the cluster. When a primary node fails and a replica is promoted in its place, you can connect to cluster endpoint to discover the new primary using the Valkey or Redis OSS Cluster protocol.

You need to connect to the cluster endpoint to discover node endpoints using **cluster nodes** or **cluster slots** command. After discovering the right node for a key, you can connect directly to the node for read/write requests. A Valkey or Redis OSS client can use the cluster endpoint to automatically connect to the correct node.

To troubleshoot specific nodes in a cluster,
you can also use node-specific endpoints, but these are not necessary for normal usage.

To find a cluster's endpoint, see the following:

- [Finding the Endpoint for a MemoryDB Cluster (AWS CLI)](endpoints.md#endpoints.find.cli "endpoints.md#endpoints.find.cli")
- [Finding the Endpoint for a MemoryDB Cluster (MemoryDB API)](endpoints.md#endpoints.find.api "endpoints.md#endpoints.find.api")
  For connecting to nodes or clusters, see [Connecting to MemoryDB nodes using
  redis-cli](getting-started.md#connect-tls "getting-started.md#connect-tls").
