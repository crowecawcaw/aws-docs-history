For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Connecting to a Timestream for InfluxDB read

replica DB cluster

A Timestream for InfluxDB read replica DB cluster has two reachable DB instances instead of a single DB
instance. Each connection is handled by a specific DB instance. When you connect to a
read replica DB cluster, the hostname and port that you specify point to a fully
qualified domain name called an _endpoint_.

The primary (writer) endpoint connects to the writer DB instance of the read replica DB cluster, which supports both read and write operations. The reader endpoint connects to the reader DB instance, which support only read operations.

Using endpoints, you can map each connection to the appropriate DB instance based on
your use case. For example, to perform administrative or write statements, you can
connect to whichever DB instance is the writer DB instance. To perform queries, you can
connect to the reader endpoint. For diagnosis or tuning, you can connect to a specific
DB instance endpoint, `/metrics`, to examine details about a specific DB instance.

For information about connecting to a DB instance, see [Connecting to an Amazon Timestream for InfluxDB DB instance](timestream-for-influx-db-connecting.md "timestream-for-influx-db-connecting.md").
For more information about connecting to read replica clusters, see the following topics.

## Types of read replica

cluster endpoints

An endpoint is represented by a unique identifier that contains a host address. Each
Timestream for InfluxDB cluster has:

- A cluster endpoint.
- A cluster read-only endpoint.
- An instance endpoint for each instance in the cluster.

### Cluster endpoint

A _cluster endpoint_ (or _writer
endpoint_) for a read replica cluster connects to the current
writer DB instance for that DB cluster. This endpoint is the only one that can
perform write operations such as:

- InfluxDB-specific administrative commands, e.g., creating,
  modifying, or deleting organizations, users, buckets, tasks, etc.
- Writing data to your database cluster.

You use the cluster endpoint for all write operations on the DB cluster,
including writes, upserts, deletes, and all configuration and administrative
changes.

In addition, you can use the cluster endpoint for read operations, such as
queries.

If the current writer DB instance of a DB cluster fails, the read replica
cluster automatically fails over to one of its replicas, promoting it as the
new writer DB instance. During a failover, the DB cluster continues to serve
connection requests to the cluster endpoint from the new writer DB instance,
with minimal interruption of service. The read replica endpoint that was
promoted to writer will stop serving reads until a new replica is deployed.

The following example illustrates a cluster endpoint for a read replica
cluster:

```
ipvtdwa5se-wmyjrrjko.us-west-2.timestream-influxdb.amazonaws.com
```

### Read-only endpoint

The _read-only endpoint_ connects to any one of the read replica instances in
the cluster. Read replicas will only support read operations, such as Flux or
InfluxQL queries; in other words, all operations executed against the
`/api/v2/query` endpoint for Flux queries or `/api/query`
endpoint for InfluxQL v1-compatible queries. By processing those statements on the reader DB instances, this endpoint reduces the overhead on the writer DB instance. It also helps the cluster to handle a higher number of simultaneous queries.

The following example illustrates a reader endpoint for a read replica
cluster. The read-only intent of a reader endpoint is denoted by the
`-ro` within the cluster endpoint name.

```
ipvtdwa5se-wmyjrrjko-ro.us-west-2.timestream-influxdb.amazonaws.com
```

### Instance endpoint

An _instance endpoint_ connects to a specific DB instance
within a read replica cluster. Each DB instance in a DB cluster has its own
unique instance endpoint. Therefore, there is one instance endpoint for the
current writer DB instance of the DB cluster (the primary), and there is one
instance endpoint for each of the reader DB instances in the DB cluster.

The instance endpoint provides direct control over connections to the DB cluster. This control can help you address scenarios where using the cluster endpoint or reader endpoint might not be appropriate. For example, your client application might require more fine-grained load balancing based on workload type. In this case, you can configure multiple clients to connect to different reader DB instances in a DB cluster to distribute read workloads.

The following example illustrates an instance endpoint for a DB instance in a
read replica cluster:

```
mydbinstance-123456789012.us-east-1.timestream-influxdb.amazonaws.com
```
