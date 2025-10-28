# Best practices for Amazon DocumentDB

Learn best practices for working with Amazon DocumentDB (with MongoDB compatibility). This section is continually updated as
new best practices are identified.

###### Topics

- [Basic operational guidelines](#best_practices-operational "#best_practices-operational")
- [Instance sizing](#best_practices-instance_sizing "#best_practices-instance_sizing")
- [Working with indexes](#best_practices-indexes "#best_practices-indexes")
- [Security best practices](#best_practices-security "#best_practices-security")
- [Cost optimization](#best_practices-cost_optimization "#best_practices-cost_optimization")
- [Using metrics to identify performance issues](#best_practices-performance "#best_practices-performance")
- [TTL and time series workloads](#best_practices-ttl_timeseries "#best_practices-ttl_timeseries")
- [Migrations](#best_practices-migrations "#best_practices-migrations")
- [Working with cluster parameter groups](#best_practices-cluster_parameter_groups "#best_practices-cluster_parameter_groups")
- [Aggregation pipeline queries](#best_practices-aggregation_pipeline_queries "#best_practices-aggregation_pipeline_queries")
- [batchInsert and
  batchUpdate](#best_practices-batchinsert_batchupdate "#best_practices-batchinsert_batchupdate")

## Basic operational guidelines

The following are basic operational guidelines that everyone should follow when working
with Amazon DocumentDB. The Amazon DocumentDB Service Level Agreement requires that you follow these
guidelines.

- Deploy a cluster consisting of two or more Amazon DocumentDB instances in two AWS Availability Zones. For production workloads, we recommend deploying a
  cluster consisting of three or more Amazon DocumentDB instances in three Availability
  Zones.
- Use the service within the stated service limits. For more information, see [Amazon DocumentDB Quotas and limits](limits.md "limits.md").
- Monitor your memory, CPU, connections, and storage usage. To help you maintain
  system performance and availability, set up Amazon CloudWatch to notify you when usage
  patterns change or when you approach the capacity of your deployment.
- Scale up your instances when you are approaching capacity limits. Your instances
  should be provisioned with enough compute resources (i.e., RAM, CPU) to accommodate
  unforeseen increases in demand from your applications.
- Set your backup retention period to align with your recovery point objective.
- Test failover for your cluster to understand how long the process takes for your
  use case. For more information, see [Amazon DocumentDB Failover](failover.md "failover.md").
- Connect to your Amazon DocumentDB cluster with the cluster endpoint (see [Amazon DocumentDB endpoints](how-it-works.md#how-it-works.endpoints "how-it-works.md#how-it-works.endpoints")) and in
  replica set mode (see [Connecting to Amazon DocumentDB as a replica set](connect-to-replica-set.md "connect-to-replica-set.md")) to minimize the impact of a failover on
  your application.
- Choose a driver read preference setting that maximizes read scaling while meeting
  your application's read consistency requirements. The `secondaryPreferred`
  read preference enables replica reads and frees up the primary instance to do more
  work. For more information, see [Read preference options](how-it-works.md#durability-consistency-isolation "how-it-works.md#durability-consistency-isolation").
- Design your application to be resilient in the event of network and database
  errors. Use your driver's error mechanism to distinguish between transient errors and
  persistent errors. Retry transient errors using an exponential backoff mechanism when
  appropriate. Ensure that your application considers data consistency when
  implementing retry logic.
- Enable cluster deletion protection for all production clusters, or any cluster
  that has valuable data. Before deleting an Amazon DocumentDB cluster, take a final snapshot. If
  you are deploying resources with AWS CloudFormation, enable termination protection. For more
  information, see [Termination
  protection and deletion protection](quick_start_cfn.md#quick_start_cfn-termination_deletion_protection "quick_start_cfn.md#quick_start_cfn-termination_deletion_protection").
- When creating an Amazon DocumentDB cluster, the `--engine-version` is an optional parameter
  that defaults to the latest major engine version. The current major engine version is
  5.0.0. When new major engine versions are released, the default engine version for
  `--engine-version` will be updated to reflect the last major engine version. As a
  result, for production workloads, and especially those that are dependent on
  scripting, automation, or AWS CloudFormation templates, we recommend that you explicitly specify
  the `--engine-version` to the intended major version.

## Instance sizing

One of the most critical aspects of choosing an instance size in Amazon DocumentDB is the amount
of RAM for your cache. Amazon DocumentDB reserves one-third of the RAM for its own services, meaning
that only two-thirds of the instance RAM is available for the cache. Thus, it is an Amazon DocumentDB
best practice to choose an instance type with enough RAM to fit your working set (i.e.,
data and indexes) in memory. Having properly sized instances will help optimize for overall
performance and potentially minimize I/O cost.

To determine whether your application's working set fits in memory, monitor the
`BufferCacheHitRatio` using Amazon CloudWatch for each instance in a cluster
that is under load.

The `BufferCacheHitRatio` CloudWatch metric measures the percentage of data
and indexes served from an instance’s memory cache (versus the storage volume). Generally
speaking, the value of `BufferCacheHitRatio` should be as high as possible, as
reading data from working set memory is faster and more cost-effective than reading from
the storage volume. While it is desirable to keep `BufferCacheHitRatio` as close
to 100% as possible, the best achievable value will depend on your application’s access
patterns and performance requirements. To maintain the highest possible
`BufferCacheHitRatio`, it is recommended that the instances in your cluster
are provisioned with enough RAM to be able to fit your indexes and working data set in
memory.

If your indexes do not fit into memory, you will see a lower
`BufferCacheHitRatio`. Continually reading from disk incurs additional I/O
costs and is not better than reading from memory. If your
`BufferCacheHitRatio` ratio is lower than expected, scale up the instance
size for your cluster to provide more RAM to fit working set data in memory. If scaling up
the instance class results in a dramatic increase in `BufferCacheHitRatio`, then
your application's working set did not fit in memory. Continue to scale up until
`BufferCacheHitRatio` no longer increases dramatically after a scaling
operation. For information about monitoring an instance's metrics, see [Amazon DocumentDB metrics](cloud_watch.md#cloud_watch-metrics_list "cloud_watch.md#cloud_watch-metrics_list").

Depending on your workload and latency requirements, it may be acceptable for your
application to have higher `BufferCacheHitRatio` values during steady state
usage, but have the `BufferCacheHitRatio` dip periodically as analytic queries
that need to scan an entire collection are run on an instance. These periodic dips in
`BufferCacheHitRatio` may manifest as higher latency for subsequent queries
that need to repopulate the working set data from the storage volume back into the buffer
cache. **We recommend that you test your workloads in a pre-production
environment with a representative production workload first in order to understand the
performance characteristics and `BufferCacheHitRatio` before deploying the
workload to production.**

The `BufferCacheHitRatio` is an instance-specific metric, so different
instances within the same cluster may have different `BufferCacheHitRatio`
values depending on how reads are distributed among the primary and replica instances. If
your operational workload cannot handle periodic increases in latency from repopulating the
working set cache after running analytic queries, you should try to isolate the regular
workload’s buffer cache from that of the analytic queries. You can achieve complete
`BufferCacheHitRatio` isolation by directing operational queries to the
primary instance and analytic queries only to the replica instances. You can also achieve
partial isolation by directing analytic queries to a specific replica instance with the
understanding that some percentage of regular queries will also run on that replica and
could potentially be affected.

Appropriate `BufferCacheHitRatio` values depend on your use case and
application requirements. There is no one best or minimum value for this metric; only you
can decide if the tradeoff from a temporarily lower `BufferCacheHitRatio` is
acceptable from a cost and performance perspective.

## Working with indexes

### Building Indexes

When importing data into Amazon DocumentDB, you should create your indexes before importing
large datasets. You can use the [Amazon DocumentDB Index Tool](https://github.com/awslabs/amazon-documentdb-tools "https://github.com/awslabs/amazon-documentdb-tools")
to extract indexes from a running MongoDB instance or `mongodump`
directory, and create those indexes in an Amazon DocumentDB cluster. For more guidance on
migrations, see [Migrating to Amazon DocumentDB](docdb-migration.md "docdb-migration.md").

### Index selectivity

We recommend that you limit the creation of indexes to fields where the number of
duplicate values is less than 1% of the total number of documents in the collection. As
an example, if your collection contains 100,000 documents, only create indexes on fields
where the same value occurs 1000 times or fewer.

Choosing an index with a high number of unique values (i.e., a high cardinality)
ensures that filter operations return a small number of documents, thereby yielding good
performance during index scans. An example of a high-cardinality index is a unique
index, which guarantees that equality predicates return at most a single document.
Examples of low-cardinality include an index over a Boolean field and an index over day
of the week. Due to their poor performance, low cardinality indexes are unlikely to be
chosen by the database’s query optimizer. At the same time, low cardinality indexes
continue to consume resources such as disk space and I/Os. As a rule of thumb, you
should target indexes on fields where the typical value frequency is 1% of the total
collection size or less.

Additionally, it is recommended to only create indexes on fields that are commonly
utilized as a filter and regularly look for unused indexes. For more information, see
[How do I analyze index usage and identify unused indexes?](user_diagnostics.md#user-diag-index-usage "user_diagnostics.md#user-diag-index-usage").

### Impact of indexes on writing data

While indexes can improve query performance by avoiding the need to scan every
document in a collection, this improvement comes with a tradeoff. For each index on a
collection, every time a document is inserted, updated, or deleted, the database must
update the collection and write the fields to each of the indexes for the collection.
For example, if a collection has nine indexes, the database must perform ten writes
before acknowledging the operation to the client. Thus, each additional index incurs
additional write latency, I/O's, and increase in the overall utilized storage.

Cluster instances need to be appropriately sized to keep all working set memory. This
avoids the need to continuously read index pages from the storage volume, which
negatively impacts performance and generates higher I/O costs. For more information, see
[Instance sizing](#best_practices-instance_sizing "#best_practices-instance_sizing").

For best performance, minimize the number of indexes in your collections, adding only
those indexes necessary to improve performance for common queries. While workloads vary,
a good guideline is to keep the number of indexes per collection to five or
fewer.

### Identifying missing indexes

Identifying missing indexes is a best practice that we recommend performing on a
regular basis. For more information, please see [How do I
identify missing indexes?](user_diagnostics.md#user_diagnostics-identify_missing_indexes "user_diagnostics.md#user_diagnostics-identify_missing_indexes").

### Identifying unused indexes

Identifying and removing unused indexes is a best practice that we recommend
performing on a regular basis. For more information, please see [How do I analyze index usage and identify unused indexes?](user_diagnostics.md#user-diag-index-usage "user_diagnostics.md#user-diag-index-usage").

## Security best practices

For security best practices, you must use AWS Identity and Access Management (IAM) accounts to control access
to Amazon DocumentDB API operations, especially operations that create, modify, or delete Amazon DocumentDB
resources. Such resources include clusters, security groups, and parameter groups. You must
also use IAM to control actions that perform common administrative actions such as
backing up restoring clusters. When creating IAM roles, employ the principle of least
privilege.

- Enforce least privilege with [role-based
  access control](role_based_access_control.md "role_based_access_control.md").
- Assign an individual IAM account to each person who manages Amazon DocumentDB resources. Do
  not use the AWS account root user to manage Amazon DocumentDB resources. Create an IAM user
  for everyone, including yourself.
- Grant each IAM user the minimum set of permissions that are required to perform
  their duties.
- Use IAM groups to effectively manage permissions for multiple users. For more
  information about IAM, see the [IAM User
  Guide](../../../IAM/latest/UserGuide/Welcome.md "../../../IAM/latest/UserGuide/Welcome.md"). For information about IAM best practices, see [IAM
  Best Practices](../../../IAM/latest/UserGuide/IAMBestPractices.md "../../../IAM/latest/UserGuide/IAMBestPractices.md").
- Regularly rotate your IAM credentials.
- Configure AWS Secrets Manager to automatically rotate the secrets
  for Amazon DocumentDB. For more information, see [Rotating Your AWS Secrets Manager Secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") and [Rotating Secrets for Amazon DocumentDB](../../../secretsmanager/latest/userguide/rotating-secrets-documentdb.md "../../../secretsmanager/latest/userguide/rotating-secrets-documentdb.md") in the _AWS Secrets
  Manager User Guide_.
- Grant each Amazon DocumentDB user the minimum set of permissions that are required to
  perform their duties. For more information, see [Database access using Role-Based
  Access Control](role_based_access_control.md "role_based_access_control.md").
- Use Transport Layer Security (TLS) to encrypt your data in transit and AWS KMS to
  encrypt your data at rest.

## Cost optimization

The following best practices can help you manage and minimize your costs when using
Amazon DocumentDB. For pricing information, see [Amazon DocumentDB (with MongoDB compatibility) pricing](https://aws.amazon.com/documentdb/pricing/ "https://aws.amazon.com/documentdb/pricing/") and [Amazon DocumentDB (with MongoDB compatibility) FAQs](https://aws.amazon.com/documentdb/faqs/ "https://aws.amazon.com/documentdb/faqs/").

- Create billing alerts at thresholds of 50 percent and 75 percent of your expected
  bill for the month. For more information about creating billing alerts, see [Creating a Billing Alarm](../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md#creating_billing_alarm_with_wizard "../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md#creating_billing_alarm_with_wizard").
- Amazon DocumentDB's architecture separates storage and compute, so even a single-instance
  cluster is highly durable. The cluster storage volume replicates data six ways across
  three Availability Zones, providing extremely high durability regardless of the
  number of instances in the cluster. A typical production cluster has three or more
  instances to provide high availability. However, you can optimize costs by using a
  single instance development cluster when high availability is not required.
- For development and test scenarios, stop a cluster when it is no longer needed and
  start the cluster when development resumes. For more information, see [Stopping and starting an
  Amazon DocumentDB cluster](db-cluster-stop-start.md "db-cluster-stop-start.md").
- Both TTL and change streams incur I/O's when data is written, read, and deleted.
  If you have enabled these features but are not utilizing them in your application,
  disabling the features can help reduce costs.

## Using metrics to identify performance issues

###### Topics

- [Viewing performance metrics](#best_practices-performance_viewing_metrics "#best_practices-performance_viewing_metrics")
- [Setting a CloudWatch alarm](#best_practices-set_cloudwatch_alarm "#best_practices-set_cloudwatch_alarm")
- [Evaluating performance metrics](#best_practices-performance_evaluating_metrics "#best_practices-performance_evaluating_metrics")
- [Evaluating Amazon DocumentDB instance usage with CloudWatch metrics](#best-practice-evaluating-instance-usage "#best-practice-evaluating-instance-usage")
- [Tuning queries](#best_practices-performance_tuning_queries "#best_practices-performance_tuning_queries")

To identify performance issues caused by insufficient resources and other common
bottlenecks, you can monitor the metrics available for your Amazon DocumentDB cluster.

### Viewing performance metrics

Monitor performance metrics on a regular basis to see the average, maximum, and
minimum values for a variety of time ranges. This helps you identify when performance is
degraded. You can also set Amazon CloudWatch alarms for particular metric thresholds so that you
are alerted if they are reached.

To troubleshoot performance issues, it’s important to understand the baseline
performance of the system. After you set up a new cluster and get it running with a
typical workload, capture the average, maximum, and minimum values of all the
performance metrics at different intervals (for example, 1 hour, 24 hours, 1 week, 2
weeks). This gives you an idea of what is normal. It helps to get comparisons for both
peak and off-peak hours of operation. You can then use this information to identify when
performance is dropping below standard levels.

####

You can view performance metrics using the AWS Management Console or AWS CLI. For more
information, see [Viewing CloudWatch data](cloud_watch.md#cloud_watch-view_data "cloud_watch.md#cloud_watch-view_data").

### Setting a CloudWatch alarm

To set a CloudWatch alarm, see [Using Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.

### Evaluating performance metrics

An instance has several different categories of metrics. How you determine acceptable
values depends on the metric.

###### CPU

- **CPU Utilization** — The percentage of the
  computer processing capacity used.

###### Memory

- **Freeable Memory** — How much RAM is
  available on the instance.
- **Swap Usage** — How much swap space is
  used by the instance, in megabytes.

###### Input/output operations

- **Read IOPS**, **Write
  IOPS** — The average number of disk read or write operations
  per second.
- **Read Latency**, **Write
  Latency** — The average time for a read or write operation in
  milliseconds.
- **Read Throughput**, **Write
  Throughput** — The average number of megabytes read from or
  written to disk per second.
- **Disk Queue Depth** — The number of I/O
  operations that are waiting to be written to or read from disk.

###### Network traffic

- **Network Receive Throughput**, **Network Transmit Throughput** — The rate of network
  traffic to and from the instance in megabytes per second.

###### Database connections

- **DB Connections** — The number of client
  sessions that are connected to the instance.

Generally speaking, acceptable values for performance metrics depend on what your
baseline looks like and what your application is doing. Investigate consistent or
trending variances from your baseline.

The following are recommendations and advice about specific types of metrics:

- **High CPU consumption** — High values for
  CPU consumption might be appropriate, provided that they are in keeping with your
  goals for your application (like throughput or concurrency) and are expected. If
  your CPU consumption is consistently over 80 percent, consider scaling up your
  instances.
- **High RAM consumption** — If your
  `FreeableMemory` metric frequently dips below 10% of the total
  instance memory, consider scaling up your instances. For more information on what
  happens when your DocumentDB instance is experiencing high memory pressure, see
  [Amazon DocumentDB Resource Governance](how-it-works.md#how-it-works.reliability.resource-governance "how-it-works.md#how-it-works.reliability.resource-governance").
- **Swap usage** — This metric should remain
  at or near zero. If your swap usage is significant, consider scaling up your
  instances.
- **Network traffic** — For network traffic,
  talk with your system administrator to understand what the expected throughput is
  for your domain network and internet connection. Investigate network traffic if
  throughput is consistently lower than expected.
- **Database connections** — Consider
  constraining database connections if you see high numbers of user connections
  together with decreases in instance performance and response time. The best number
  of user connections for your instance varies based on your instance class and the
  complexity of the operations being performed. For issues with any performance
  metrics, one of the first things you can do to improve performance is tune the
  most used and most expensive queries to see if that lowers the pressure on system
  resources.

If your queries are tuned and an issue persists, consider upgrading your Amazon DocumentDB
instance class to one with more of the resource (CPU, RAM, disk space, network
bandwidth, I/O capacity) that is related to the issue you're experiencing.

### Evaluating Amazon DocumentDB instance usage with CloudWatch metrics

You can use CloudWatch metrics to watch your instance throughput and discover if your instance class provides sufficient resources for your applications.
For information about your instance class limits, see [Instance limits](limits.md#limits.instance "limits.md#limits.instance") and locate the specifications for your instance class to find your network performance.

If your instance usage is near the instance class limit, then performance may begin to slow.
The CloudWatch metrics can confirm this situation so you can plan to manually scale-up to a larger instance class.

Combine the following CloudWatch metrics values to find out if you are nearing the instance class limit:

- **NetworkThroughput**—The amount of network throughput received and transmitted by the clients for each instance in the Amazon DocumentDB cluster.
  This throughput value doesn't include network traffic between instances in the cluster and the cluster storage volume.
- **StorageNetworkThroughput**—The amount of network throughput received and sent to the Amazon DocumentDB cluster storage volume by each instance in the Amazon DocumentDB cluster.

Add the **NetworkThroughput** to the **StorageNetworkThroughput** to find the network throughput received from and sent to the Amazon DocumentDB cluster storage volume by each instance in your Amazon DocumentDB cluster.
The instance class limit for your instance should be greater than the sum of these two combined metrics.

You can use the following metrics to review additional details of the network traffic from your client applications when sending and receiving:

- **NetworkReceiveThroughput**—The amount of network throughput received from clients by each instance in the Amazon DocumentDB cluster.
  This throughput doesn't include network traffic between instances in the cluster and the cluster storage volume.
- **NetworkTransmitThroughput**—The amount of network throughput sent to clients by each instance in the Amazon DocumentDB cluster.
  This throughput doesn't include network traffic between instances in the cluster and the cluster storage volume.
- **StorageNetworkReceiveThroughput**—The amount of network throughput received from the Amazon DocumentDB cluster storage volume by each instance in the cluster.
- **StorageNetworkTransmitThroughput**—The amount of network throughput sent to the Amazon DocumentDB cluster storage volume by each instance in the cluster.

Add all of these metrics together to evaluate how your network usage compares to the instance class limit.
The instance class limit should be greater than the sum of these combined metrics.

The network limits and CPU utilization by an instance are mutual.
When the network throughput increases, then the CPU utilization also increases.
Monitoring the CPU and network usage provides information about how and why the resources are being exhausted.

To help minimize network usage, you can consider:

- Using a larger instance class.
- Dividing the write requests in batches to reduce overall transactions.
- Directing the read-only workload to a read-only instance.
- Deleting any unused indexes.

### Tuning queries

One of the best ways to improve cluster performance is to tune your most commonly
used and most resource-intensive queries to make them less expensive to run.

You can use the profiler (see [Profiling Amazon DocumentDB operations](profiling.md "profiling.md"))
to log the execution time and details of operations that were performed on your cluster.
Profiler is useful for monitoring the slowest operations on your cluster to help you
improve individual query performance and overall cluster performance.

You can also use the `explain` command to learn how to analyze a query
plan for a particular query. Use this information to modify a query or underlying
collection to improve your query performance (for example, adding an index).

## TTL and time series workloads

Document deletion resulting from TTL index expiry is a best effort process. Documents
are not guaranteed to be deleted within any specific period. Factors like instance size,
instance resource utilization, document size, overall throughput, the number of indexes,
and whether indexes and the working set fit in memory can all affect the timing of when
expired documents are deleted by the TTL process.

When the TTL monitor deletes your documents, each deletion incurs I/O costs, which
increases your bill. If throughput and TTL delete rates increase, you should expect a
higher bill due to increased I/O usage. However, if you do not create a TTL index to delete
documents, but instead segment documents into collections based on time and simply drop
those collections when they are no longer needed, you will not incur any IO costs. This can
be significantly more cost effective than using a TTL index.

For time-series workloads, you can consider creating rolling collections instead of a
TTL index as rolling collections can be a better way to delete data and less I/O
intensive. If you have large collections (especially collections over 1TB) or TTL deletion
I/O costs are a concern, we recommend that you partition documents into collections based
on time, and drop collections when the documents are no longer needed. You can create one
collection per day or one per week, depending on your data ingest rate. While requirements
will vary depending on your application, a good rule of thumb is to have more smaller
collections rather than a few large collections. Dropping these collections does not incur
I/O costs, and can be faster and more cost effective than using a TTL index.

## Migrations

As a best practice, we recommend that when migrating data to Amazon DocumentDB, you first create
your indexes in Amazon DocumentDB before migrating the data. Creating the indexes first can reduce
the overall time and increase the speed of the migration. To do this, you can use the
Amazon DocumentDB [Index Tool](https://github.com/awslabs/amazon-documentdb-tools "https://github.com/awslabs/amazon-documentdb-tools").
For more information on migrations, see the [Amazon DocumentDB migration guide](docdb-migration.md "docdb-migration.md").

We also recommend that before you migrate your production database, it is a best
practice to fully test your application on Amazon DocumentDB, taking into consideration
functionality, performance, operations, and cost.

## Working with cluster parameter groups

We recommend that you try out cluster parameter group changes on a test cluster before
applying the changes to your production clusters. For information about backing up your
cluster, see [Backing up and restoring in Amazon DocumentDB](backup_restore.md "backup_restore.md").

## Aggregation pipeline queries

When creating an aggregation pipeline query with multiple stages and evaluating only a
subset of the data in the query, use the `$match` stage as the first stage or in
the beginning of the pipeline. Using `$match` first will reduce the number of
documents subsequent stages within the aggregation pipeline query will need to process,
thus improving the performance of your query.

## `batchInsert` and

`batchUpdate`

When performing a high rate of concurrent `batchInsert` and/or
`batchUpdate` operations, and the amount of `FreeableMemory`
(CloudWatch Metric) goes to zero on your primary instance, you can either reduce the
concurrency of the batch insert or update workload or, if concurrency of the workload
cannot be reduced, increase the instance size to increase the amount of
`FreeableMemory`.
