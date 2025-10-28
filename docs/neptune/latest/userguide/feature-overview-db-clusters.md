# Amazon Neptune DB Clusters and Instances

An Amazon Neptune _DB cluster_ manages access to your data
through queries. A cluster consists of:

- One _primary DB instance._.
- Up to 15 _read-replica DB instances._.
  All the instances in a cluster share the same [underlying
  managed storage volume](feature-overview-storage.md "feature-overview-storage.md"), which is designed for reliability and high availability.

You connect to the DB instances in your DB cluster through [Neptune endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md").

## The primary DB instance in a Neptune DB cluster

The primary DB instance coordinates all write operations to the DB cluster's
underlying storage volume. It also supports read operations.

There can only be one primary DB instance in a Neptune DB cluster. If the primary
instance becomes unavailable, Neptune automatically fails over to one of the
read-replica instances with a priority that you can specify.

## Read-replica DB instances in a Neptune DB cluster

After you create the primary instance for a DB cluster, you can create up to
15 read-replica instances in your DB cluster to support read-only queries.

Neptune read-replica DB instances work well for scaling read capacity because
they are fully dedicated to read operations on your cluster volume. All write operations
are managed by the primary instance. Each read-replica DB instance has its own
endpoint.

Because the cluster storage volume is shared among all instances in a cluster,
all read-replica instances return the same data for query results with very little
replication lag. This lag is usually much less than 100 milliseconds after the primary
instance writes an update, although it can be somewhat longer when the volume of write
operations is very large.

Having one or more read-replica instances available in different Availability Zones can
increase availability, because read-replicas serve as failover targets for the primary
instance. That is, if the primary instance fails, Neptune promotes a read-replica
instance to become the primary instance. When this happens, there is a brief interruption
while the promoted instance is rebooted, during which read and write requests made to
the primary instance fail with an exception.

By contrast, if your DB cluster doesn't include any read-replica instances, your
DB cluster remains unavailable when the primary instance fails until it has been
re-created. Re-creating the primary instance takes considerably longer than
promoting a read-replica.

To ensure high availability, we recommend that you create one or more read-replica
instances that have the same DB instance class as the primary instance and are located
in different Availability Zones than the primary instance. See [Fault tolerance for a Neptune DB cluster](backup-restore-overview-fault-tolerance.md "backup-restore-overview-fault-tolerance.md").

Using the console, you can create a Multi-AZ deployment by simply specifying Multi-AZ when
creating a DB cluster. If a DB cluster is in a single Availability Zone, you can make it a
Multi-AZ DB cluster adding a Neptune replica in a different Availability Zone.

###### Note

You can't create an encrypted read-replica instance for an unencrypted
Neptune DB cluster, or an unencrypted read-replica instance for an encrypted
Neptune DB cluster.

For details on how to create a Neptune read-replica DB instance, see [Creating a Neptune reader instance using the console](manage-console-create-replica.md "manage-console-create-replica.md").

## Sizing DB instances in a Neptune DB cluster

Size the instances in your Neptune DB cluster based on your CPU and memory requirements.
The number of vCPUs on an instance determines the number of query threads that handle incoming
queries. The amount of memory on an instance determines the size of the buffer cache, used for
storing copies of data pages fetched from the underlying storage volume.

Each Neptune DB instance has a number of query threads equal to 2 x number of vCPUs on
that instance. An `r5.4xlarge`, for example, with 16 vCPUs, has
32 query threads, and can therefore process 32 queries concurrently.

Additional queries that arrive while all query threads are occupied are put into a
server-side queue, and processed in a FIFO manner as query threads become available.
This server-side queue can hold approximately 8000 pending requests. Once it's full,
Neptune respond to additional requests with a `ThrottlingException`. You
can monitor the number of pending requests with the `MainRequestQueuePendingRequests`
CloudWatch metric, or by using the [Gremlin query
status endpoint](gremlin-api-status.md "gremlin-api-status.md") with the `includeWaiting` parameter.

Query execution time from a client perspective includes of any time spent in the
queue, in addition to the time taken to actually execute the query.

A sustained concurrent write load that utilizes all the query threads on the primary
DB instance ideally shows 90% or more CPU utilization, which indicates that all the query
threads on the server are actively engaged in doing useful work. However, actual CPU
utilization is often somewhat lower, even under a sustained concurrent write load.
This is usually because query threads are waiting on I/O operations to the underlying
storage volume to complete. Neptune uses quorum writes that make six copies of your
data across three Availability Zones, and four out of those six storage nodes must
acknowledge a write for it to be considered durable. While a query thread waits for
this quorum from the storage volume, it is stalled, which reduces CPU utilization.

If you have a serial write load where you are performing one write after another
and waiting for the first to complete before beginning the next, you can expect the CPU
utilization to be lower still. The exact amount will be a function of the number of
vCPUs and query threads (the more query threads, the less overall CPU per query),
with some reduction caused by waiting for I/O.

For more information about how best to size DB instances, see [Choosing instance types for Amazon Neptune](instance-types.md "instance-types.md"). For the pricing of each
instance-type, please see the [Neptune pricing page](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/").

## Monitoring DB instance performance in Neptune

You can use CloudWatch metrics in Neptune to monitor the performance of your DB instances
and keep track of query latency as observed by the client. See [Using CloudWatch to monitor DB instance
performance in Neptune](cloudwatch-monitoring-instances.md "cloudwatch-monitoring-instances.md").
