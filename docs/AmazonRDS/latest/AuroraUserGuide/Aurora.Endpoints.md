# Cluster endpoints for Amazon Aurora

A _cluster endpoint_ (or _writer
endpoint_) for an Aurora DB cluster connects to the current primary DB instance
for that DB cluster. This endpoint is the only one that can perform write operations such as
DDL statements. Because of this, the cluster endpoint is the one that you connect to when
you first set up a cluster or when your cluster only contains a single DB instance.

Each Aurora DB cluster has one cluster endpoint and one primary DB instance.

You use the cluster endpoint for all write operations on the DB cluster, including
inserts, updates, deletes, and DDL changes. You can also use the cluster endpoint for read
operations, such as queries.

The cluster endpoint provides failover support for read/write connections to the DB
cluster. If the current primary DB instance of a DB cluster fails, Aurora automatically fails
over to a new primary DB instance. During a failover, the DB cluster continues to serve
connection requests to the cluster endpoint from the new primary DB instance, with minimal
interruption of service.

The following example illustrates a cluster endpoint for an Aurora MySQL DB
cluster.

```
mydbcluster.cluster-c7tj4example.us-east-1.rds.amazonaws.com:3306
```

Each Aurora cluster has a single built-in cluster endpoint, whose name and other
attributes are managed by Aurora. You can't create, delete, or modify this kind of
endpoint.

You use the cluster endpoint when you administer your cluster, perform extract,
transform, load (ETL) operations, or develop and test applications. The cluster endpoint
connects to the primary instance of the cluster. The primary instance is the only DB
instance where you can create tables and indexes, run `INSERT` statements, and
perform other DDL and DML operations.

The physical IP address pointed to by the cluster endpoint changes when the failover
mechanism promotes a new DB instance to be the read/write primary instance for the cluster.
If you use any form of connection pooling or other multiplexing, be prepared to flush or
reduce the time-to-live for any cached DNS information. Doing so ensures that you don't try
to establish a read/write connection to a DB instance that became unavailable or is now
read-only after a failover.
