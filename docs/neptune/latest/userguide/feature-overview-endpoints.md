# Connecting to Amazon Neptune Endpoints

Amazon Neptune uses a cluster of DB instances rather than a single instance. Each
Neptune connection is handled by a specific DB instance. When you connect to a Neptune
cluster, the host name and port that you specify point to an intermediate handler called
an _endpoint_. An endpoint is a URL that contains a
host address and a port. Neptune endpoints use encrypted Transport Layer Security/Secure
Sockets Layer (TLS/SSL) connections.

Neptune uses the endpoint mechanism to abstract these connections so that you
don't have to hardcode the hostnames, or write your own logic for rerouting connections
when some DB instances are unavailable.

Using endpoints, you can map each connection to the appropriate instance or
group of instances, depending on your use case. Custom endpoints let you connect to
subsets of DB instances. The following endpoints are available in a Neptune DB cluster:

## Neptune cluster endpoints

A cluster endpoint is an endpoint for a Neptune DB cluster that connects to the
current primary DB instance for that DB cluster. Each Neptune DB cluster has a cluster
endpoint and one primary DB instance.

The cluster endpoint provides failover support for read/write connections to the DB
cluster. Use the cluster endpoint for all write operations on the DB cluster, including
inserts, updates, deletes, and data definition language (DDL) changes. You can also use
the cluster endpoint for read operations, such as queries.

If the current primary DB instance of a DB cluster fails, Neptune automatically
fails over to a new primary DB instance. During a failover, the DB cluster continues to
serve connection requests to the cluster endpoint from the new primary DB instance, with
minimal interruption of service.

The following example illustrates a cluster endpoint for a Neptune DB
cluster.

`mydbcluster.cluster-123456789012.us-east-1.neptune.amazonaws.com:8182`

## Neptune reader endpoints

A reader endpoint is an endpoint for a Neptune DB cluster that connects to one of
the available Neptune replicas for that DB cluster. Each Neptune DB cluster has a
reader endpoint. If there is more than one Neptune replica, the reader endpoint
directs each connection request to one of the Neptune replicas.

The reader endpoint provides round-robin routing for read-only connections to the DB
cluster. Use the reader endpoint for read operations, such as queries.

You can't use the reader endpoint for write operations unless you have a
single-instance cluster (a cluster with no read-replicas). In that case and that
case only, the reader can be used for write operations as well as read operations.

The reader endpoint round-robin routing works by changing the host that the DNS
entry points to. Each time you resolve the DNS, you get a different IP, and connections
are opened against those IPs. After a connection is established, all the requests for
that connection are sent to the same host. The client must create a new connection and
resolve the DNS record again to get a connection to potentially different read replica.

###### Note

WebSockets connections are often kept alive for long periods. To get different
read replicas, do the following:

- Ensure that your client resolves the DNS entry each time it connects.
- Close the connection and reconnect.

Various client software might resolve DNS in different ways. For example, if your
client resolves DNS and then uses the IP for every connection, it directs all requests
to a single host.

DNS caching for clients or proxies resolves the DNS name to the same endpoint from
the cache. This is a problem for both round robin routing and failover scenarios.

###### Note

Disable any DNS caching settings to force DNS resolution each time.

The DB cluster distributes connection requests to the reader endpoint among
available Neptune replicas. If the DB cluster contains only a primary DB instance, the
reader endpoint serves connection requests from the primary DB instance. If a Neptune
replica is created for that DB cluster, the reader endpoint continues to serve
connection requests to the reader endpoint from the new Neptune replica, with minimal
interruption in service.

The following example illustrates a reader endpoint for a Neptune DB
cluster.

`mydbcluster.cluster-ro-123456789012.us-east-1.neptune.amazonaws.com:8182`

## Neptune instance endpoints

An instance endpoint is an endpoint for a DB instance in a Neptune DB cluster that
connects to that specific DB instance. Each DB instance in a DB cluster, regardless of
instance type, has its own unique instance endpoint. So, there is one instance endpoint
for the current primary DB instance of the DB cluster. There is also one instance
endpoint for each of the Neptune replicas in the DB cluster.

The instance endpoint provides direct control over connections to the DB cluster,
for scenarios where using the cluster endpoint or reader endpoint might not be
appropriate. For example, your client application might require fine-grained load
balancing based on workload type. In this case, you can configure multiple clients to
connect to different Neptune replicas in a DB cluster to distribute read
workloads.

The following example illustrates an instance endpoint for a DB instance in a
Neptune DB cluster.

`mydbinstance.123456789012.us-east-1.neptune.amazonaws.com:8182`

## Neptune custom endpoints

A custom endpoint for a Neptune cluster represents a set
of DB instances that you choose. When you connect to the endpoint, Neptune chooses
one of the instances in the group to handle the connection. You define which instances
this endpoint refers to, and you decide what purpose the endpoint serves.

A Neptune DB cluster has no custom endpoints until you create one, and you can
create up to five custom endpoints for each provisioned Neptune cluster.

The custom endpoint provides load-balanced database connections based on criteria
other than the read-only or read/write capability of the DB instances. Because the
connection can go to any DB instance associated with the endpoint, make sure that
all the instances within that group share the same performance and memory capacity
characteristics. When you use custom endpoints, you typically don't use the reader
endpoint for that cluster.

This feature is intended for advanced users with specialized kinds of workloads
where it isn't practical to keep all the Neptune Replicas in the cluster identical.
With custom endpoints, you can adjust the capacity of the DB instances used with each
connection.

For example, if you define several custom endpoints that connect to groups of
instances with different instance classes, you can then direct users with different
performance needs to the endpoints that best suit their use cases.

The following example illustrates a custom endpoint for a DB instance in a Neptune
DB cluster:

`myendpoint.cluster-custom-123456789012.us-east-1.neptune.amazonaws.com:8182`

See [Working with custom endpoints](feature-custom-endpoint-membership.md "feature-custom-endpoint-membership.md") for more information.

## Neptune endpoint considerations

Consider the following when working with Neptune endpoints:

- Before using an instance endpoint to connect to a specific DB instance in a DB
  cluster, consider using the cluster endpoint or reader endpoint for the DB cluster
  instead.

The cluster endpoint and reader endpoint provide support for high-availability
scenarios. If the primary DB instance of a DB cluster fails, Neptune automatically
fails over to a new primary DB instance. It does so by either promoting an existing
Neptune replica to a new primary DB instance or creating a new primary DB instance. If
a failover occurs, you can use the cluster endpoint to reconnect to the newly promoted
or created primary DB instance, or use the reader endpoint to reconnect to one of the
other Neptune replicas in the DB cluster.

If you don't take this approach, you can still make sure that you're connecting
to the right DB instance in the DB cluster for the intended operation. To do so, you can
manually or programmatically discover the resulting set of available DB instances in the
DB cluster and confirm their instance types after failover, before using the instance
endpoint of a specific DB instance.

For more information about failovers, see [Fault tolerance for a Neptune DB cluster](backup-restore-overview-fault-tolerance.md "backup-restore-overview-fault-tolerance.md").

- The reader endpoint only directs connections to available Neptune replicas in a
  Neptune DB cluster. It does not direct specific queries.

###### Important

Neptune does not load balance.

If you want to load balance queries to distribute the read workload for a DB
cluster, you must manage that in your application. You must use instance endpoints to
connect directly to Neptune replicas to balance the load.

- The reader endpoint round-robin routing works by changing the host that the DNS
  entry points to. The client must create a new connection and resolve the DNS record
  again to get a connection to a potentially new read replica.
- During a failover, the reader endpoint might direct connections to the new primary
  DB instance of a DB cluster for a short time, when a Neptune replica is promoted to
  the new primary DB instance.
