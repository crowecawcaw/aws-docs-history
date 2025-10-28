# Overall best practices

Below you can find information about best practices for using the Valkey, Memcached, and Redis OSS interfaces within ElastiCache.

- **Use cluster-mode enabled configurations** –
  Cluster-mode enabled allows the cache to scale horizontally to achieve higher storage
  and throughput than a cluster-mode disabled configuration. ElastiCache serverless is only available
  in a cluster-mode enabled configuration.
- **Use long-lived connections** – Creating
  a new connection is expensive, and takes time and CPU resources from the cache. Reuse
  connections when possible (e.g. with connection pooling) to amortize this cost over many
  commands.
- **Read from replicas** – If you are using
  ElastiCache serverless or have provisioned read replicas (node-based clusters), direct reads to
  replicas to achieve better scalability and/or lower latency. Reads from replicas are eventually
  consistent with the primary.

In a node-based cluster, avoid directing read requests to a single read replica since reads may
not be available temporarily if the node fails. Either configure your
client to direct read requests to at least two read replicas, or direct reads to a single replica and the primary.

In ElastiCache serverless, reading from the replica port (6380) will
direct reads to the client's local availability zone when possible, reducing retrieval latency. It will automatically
fall back to the other nodes during failures.

- **Avoid expensive commands** – Avoid running any
  computationally and I/O intensive operations, such as the `KEYS` and
  `SMEMBERS` commands. We suggest this approach because these
  operations increase the load on the cluster and have an impact on the
  performance of the cluster. Instead, use the `SCAN` and
  `SSCAN` commands.
- **Follow Lua best practices** – Avoid long running Lua
  scripts, and always declare keys used in Lua scripts up front. We recommend this
  approach to determine that the Lua script is not using cross slot commands.
  Ensure that the keys used in Lua scripts belong to the same slot.
- **Use sharded pub/sub** – When using Valkey or Redis OSS to support pub/sub workloads
  with high throughput, we recommend you use [sharded pub/sub](https://valkey.io/topics/pubsub/ "https://valkey.io/topics/pubsub/")
  (available with Valkey, and with Redis OSS 7 or later). Traditional pub/sub in cluster-mode enabled clusters broadcasts messages to all nodes in
  the cluster, which can result in high `EngineCPUUtilization`. Note that in ElastiCache serverless, traditional
  pub/sub commands internally use sharded pub/sub commands.

###### Topics
