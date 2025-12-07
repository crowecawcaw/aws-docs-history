# Reader endpoints for Amazon Aurora

A _reader endpoint_ for an Aurora DB cluster provides
connection-balancing support for read-only connections to the DB cluster. Use the reader
endpoint for read operations, such as queries. By processing those statements on the
read-only Aurora Replicas, this endpoint reduces the overhead on the primary instance. It
also helps the cluster to scale the capacity to handle simultaneous `SELECT`
queries, proportional to the number of Aurora Replicas in the cluster. Each Aurora DB cluster
has one reader endpoint.

If the cluster contains one or more Aurora Replicas, the reader endpoint balances each
connection request among the Aurora Replicas. In that case, you can only perform read-only
statements such as `SELECT` in that session. If the cluster only contains a
primary instance and no Aurora Replicas, the reader endpoint connects to the primary
instance. In that case, you can perform write operations through the endpoint.

The following example illustrates a reader endpoint for an Aurora MySQL DB cluster.

```
mydbcluster.cluster-ro-c7tj4example.us-east-1.rds.amazonaws.com:3306
```

You use the reader endpoint for read-only connections for your Aurora cluster. This
endpoint uses a connection-balancing mechanism to help your cluster handle a query-intensive
workload. The reader endpoint is the endpoint that you supply to applications that do
reporting or other read-only operations on the cluster.

The reader endpoint balances connections to available Aurora Replicas in an Aurora DB
cluster. It doesn't balance individual queries. If you want to balance each query to
distribute the read workload for a DB cluster, open a new connection to the reader endpoint
for each query.

Each Aurora cluster has a single built-in reader endpoint, whose name and other
attributes are managed by Aurora. You can't create, delete, or modify this kind of
endpoint.

If your cluster contains only a primary target (instance or DB shard group) and no Aurora Replicas, the reader
endpoint connects to the primary instance. In that case, you can perform write operations
through this endpoint.

###### Tip

Through RDS Proxy, you can create additional read-only endpoints for an Aurora cluster.
These endpoints perform the same kind of connection-balancing as the Aurora reader
endpoint. Applications can reconnect more quickly to the proxy endpoints than the Aurora
reader endpoint if reader instances become unavailable. The proxy endpoints can also take
advantage of other proxy features such as multiplexing. For more information, see [Using reader endpoints with Aurora clusters](rds-proxy-endpoints.md#rds-proxy-endpoints-reader "rds-proxy-endpoints.md#rds-proxy-endpoints-reader").
