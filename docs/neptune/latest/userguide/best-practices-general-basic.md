# Amazon Neptune basic operational guidelines

The following are basic operational guidelines that you should follow when working with
Neptune.

- Understand Neptune DB instances so that you can size them appropriately
  for your performance and use-case requirements. See [Amazon Neptune DB Clusters and Instances](feature-overview-db-clusters.md "feature-overview-db-clusters.md").
- Monitor your CPU and memory usage. This helps you know when to migrate to a DB instance
  class with greater CPU or memory capacity to achieve the query performance that you require.
  You can set up Amazon CloudWatch to notify you when usage patterns change or when you approach the
  capacity of your deployment. Doing so can help you maintain system performance and
  availability. See [Monitoring instances](feature-overview-db-clusters.md#feature-overview-monitoring-instances "feature-overview-db-clusters.md#feature-overview-monitoring-instances") and [Monitoring Neptune](monitoring.md "monitoring.md") for details.

Because Neptune has its own memory manager, it is normal to see relatively
low memory usage even when CPU usage is high. Encountering out-of-memory exceptions
when executing queries is the best indicator that you need to increase freeable
memory.

- Enable automatic backups and set the backup window to occur at
  a convenient time.
- Test failover for your DB instance to understand how long the process takes for your use
  case. It also helps ensure that the application that accesses your DB instance can
  automatically connect to the new DB instance after failover.
- If possible, run your client and Neptune cluster in the same region and VPC,
  because cross-region connections with VPC peering can introduce delays in query
  response times. For single-digit millisecond query responses, it is necessary to
  keep the client and the Neptune cluster in the same region and VPC.
- When you create a read-replica instance, it should be at least as
  large as the primary writer instance. This helps keep replication lag in check, and avoids
  replica restarts. See [Avoid different instance classes in a cluster](#best-practices-loader-heterogeneous-instances "#best-practices-loader-heterogeneous-instances").
- Before upgrading to a new major engine version, be sure to test your
  application on it before you upgrade. You can do this by cloning your DB
  cluster so that the clone cluster runs the new engine version, and then
  test your application on the clone.
- To facilitate failovers, all instances should ideally be the same
  size.

###### Topics

- [Amazon Neptune security best practices](best-practices-general-security.md "best-practices-general-security.md")
- [Avoid different instance classes in a cluster](#best-practices-loader-heterogeneous-instances "#best-practices-loader-heterogeneous-instances")
- [Avoid repeated restarts during bulk loading](#best-practices-loader-repeated-restarts "#best-practices-loader-repeated-restarts")
- [Enable the OSGP Index if you have a large number of predicates](#best-practices-general-predicates "#best-practices-general-predicates")
- [Avoid long-running transactions where possible](#best-practices-general-long-running-transactions "#best-practices-general-long-running-transactions")
- [Best practices for using Neptune metrics](best-practices-general-metrics.md "best-practices-general-metrics.md")
- [Best practices for tuning Neptune queries](#best-practices-general-tuning "#best-practices-general-tuning")
- [Load balancing across read replicas](#best-practices-general-loadbalance "#best-practices-general-loadbalance")
- [Loading faster using a temporary larger
  instance](#best-practices-loader-tempinstance "#best-practices-loader-tempinstance")
- [Resize your writer instance by failing over to a read-replica](#best-practices-resize-instance "#best-practices-resize-instance")
- [Retry upload after data prefetch task interrupted error](#load-api-reference-status-interrupted "#load-api-reference-status-interrupted")

## Avoid different instance classes in a cluster

When your DB cluster contains instances of different classes, problems can occur over
time. The most common problem is that a small reader instance can get into a cycle of
repeated restarts because of replication lag. If a reader node has a weaker DB instance
class configuration than that of a writer DB instance, the volume of changes can be too
big for the reader to catch up.

###### Important

To avoid repeated restarts caused by replication lag, configure your
DB cluster so that all instances have the same instance class (size).

You can see the lag between the writer instance (the primary) and the readers in
your DB cluster using the `ClusterReplicaLag` metric in Amazon CloudWatch.
The `VolumeWriteIOPs` metric also lets you detect bursts of write activity in
your cluster that can create replication lag.

## Avoid repeated restarts during bulk loading

If you experience a cycle of repeated read-replica restarts because of
replication lag during a bulk load, your replicas are likely unable to keep up
with the writer in your DB cluster.

Either scale the readers to be larger than the writer, or temporarily remove
them during the bulk load and then recreate them after it completes.

## Enable the OSGP Index if you have a large number of predicates

If your data model contains a large number of distinct predicates (more than thousand
in most cases), you may experience reduced performance and higher operational costs.

If this is the case, you can improve performance by enabling the [OSGP index](feature-overview-storage-indexing.md#feature-overview-storage-indexing-osgp "feature-overview-storage-indexing.md#feature-overview-storage-indexing-osgp").
See [The OSGP index](features-lab-mode.md#features-lab-mode-features-osgp-index "features-lab-mode.md#features-lab-mode-features-osgp-index").

## Avoid long-running transactions where possible

Long-running transactions, either read-only or read-write, can cause unexpected
problems of the following kinds:

A long-running transaction on a reader instance or on a writer instance with
concurrent writes can result in a large accumulation of different versions of data.
This can introduce higher latencies for read queries that filter out a large
portion of their results.

In some cases, the accumulated versions over hours can cause new writes to be
throttled.

A long-running read-write transaction with many writes can also cause issues
if the instance restarts. If an instance restarts from a maintenance event or a
crash, all uncommitted writes are rolled back. Such undo operations typically
run in the background and do not block the instance from coming back up, but
any new writes that conflict with the operations being rolled back then fail.

For example, if the same query is retried after the connection was severed
in the previous run might fail when the instance is restarted.

The time needed for undo operations is proportional to the size of the
changes involved.

## Best practices for tuning Neptune queries

One of the best ways to improve Neptune performance is to tune your most commonly
used and most resource-intensive queries to make them less expensive to run.

For information about how to tune Gremlin queries, see [Gremlin query hints](gremlin-query-hints.md "gremlin-query-hints.md") and [Tuning Gremlin queries](gremlin-traversal-tuning.md "gremlin-traversal-tuning.md") . For information about how to tune
SPARQL queries, see [SPARQL query hints](sparql-query-hints.md "sparql-query-hints.md").

## Load balancing across read replicas

The reader endpoint round-robin routing works by changing the host that the DNS entry
points to. The client must create a new connection and resolve the DNS record to get a
connection to a new read replica, because WebSocket connections are often kept alive for
long periods.

To get different read replicas for successive requests, ensure that your client resolves
the DNS entry each time it connects. This may require closing the connection and reconnecting
to the reader endpoint.

You can also load balance requests across read replicas by connecting to instance
endpoints explicitly.

## Loading faster using a temporary larger

instance

Your load performance increases with larger instance sizes. If you're not using a large
instance type, but you want increased load speeds, you can use a larger instance to load and
then delete it.

###### Note

The following procedure is for a new cluster. If you have an existing cluster, you can
add a new larger instance and then promote it to a primary DB instance.

###### To load data using a larger instance size

1. Create a cluster with a single `r5.12xlarge` instance. This instance
   is the primary DB instance.
2. Create one or more read replicas of the same size (`r5.12xlarge`).

You can create the read replicas in a smaller size, but if they are not large
enough to keep up with writes made by the primary instance, they may have to restart
frequently. The resulting downtime reduces performance dramatically. 3. In the bulk loader command, include `“parallelism” : “OVERSUBSCRIBE”`
to tell Neptune to use all available CPU resources for loading (see [Neptune Loader Request Parameters](load-api-reference-load.md#load-api-reference-load-parameters "load-api-reference-load.md#load-api-reference-load-parameters")). The load operation will then
proceed as fast as I/O permits, which generally requires 60-70% of CPU resources. 4. Load your data using the Neptune loader. The load job runs on the primary DB
instance. 5. After the data is finished loading, be sure to scale all the instances in
the cluster down to the same instance type to avoid additional charges and repeated
restart problems (see [Avoid different instance sizes](#best-practices-loader-heterogeneous-instances "#best-practices-loader-heterogeneous-instances")).

## Resize your writer instance by failing over to a read-replica

The best way to resize an instance in your DB cluster, including the writer instance,
is to create or modify a read-replica instance so that it has the size your want, and then
deliberately fail over to that read-replica. The downtime seen by your application is
only the time required to change the writer's IP address, which should be around 3 to 5 seconds.

The Neptune management API that you use to fail over the current writer instance to
a read-replica instance deliberately is [FailoverDBCluster](api-clusters.md#FailoverDBCluster "api-clusters.md#FailoverDBCluster"). If you are using the Gremlin Java client,
you may need to create a new Client object after the failover to pick up the new IP address,
as mentioned [here](best-practices-gremlin-java-new-connection.md "best-practices-gremlin-java-new-connection.md").

Make sure to change all your instances to the same size so that you avoid a cycle of
repeated restarts, as mentioned below.

## Retry upload after data prefetch task interrupted error

When you are loading data into Neptune using the bulk loader, a `LOAD_FAILED`
status may occasionally result, with a `PARSING_ERROR` and `Data prefetch
 task interrupted` message reported in response to a request for detailed information,
like this:

```
"errorLogs" : [
  {
    "errorCode" : "PARSING_ERROR",
    "errorMessage" : "Data prefetch task interrupted: Data prefetch task for 11467 failed",
    "fileName" : "s3://amzn-s3-demo-bucket/`some-source-file`",
    "recordNum" : 0
  }
]
```

If you encounter this error, just retry the bulk upload request again.

The error occurs when there was a temporary interruption that was typically
not caused by your request or your data, and it can usually be resolved by
running the bulk upload request again.

If you are using default settings, namely `"mode":"AUTO"`, and
`"failOnError":"TRUE"`, the loader skips the files that it already
successfully loaded and resumes loading files it had not yet loaded when the
interruption occurred.
