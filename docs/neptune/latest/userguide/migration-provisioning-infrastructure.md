# Provisioning infrastructure when migrating from Neo4j to Neptune

Amazon Neptune clusters are built to scale in three dimensions: storage, write capacity,
and read capacity. The sections below discuss specific options to consider when migrating.

## Provisioning storage

The storage for any Neptune cluster is automatically provisioned, without any
administrative overhead on your part. It resizes dynamically in 10 GB chunks as the
storage needs of the cluster increase. As a result, there is no need to estimate
and provision or over-provision storage to handle future data growth.

## Provisioning write capacity

Neptune provides a single writer instance that can be scaled vertically to any
instance size available on the [Neptune
pricing page](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/"). When reading and writing data to a writer instance, all
transactions are ACID compliant, with data isolation as defined in [Transaction Isolation Levels in Neptune](transactions-neptune.md "transactions-neptune.md").

Choosing an optimal size for a writer instance requires running load tests to
determine the optimal instance size for your workload. Any instance within Neptune
can be resized at any time by [modifying
the DB instance class](manage-console-instances-modify.md "manage-console-instances-modify.md"). You can estimate a starting instance size based on
concurrency and average query latency as described below in [Estimating optimal instance size when provisioning your cluster](#migration-provisioning-instance-sizing "#migration-provisioning-instance-sizing").

## Provisioning read capacity

Neptune is built to scale read-replica instances both horizontally, by adding
up to 15 of them within a cluster (or more in a [Neptune
global database](neptune-global-database.md "neptune-global-database.md")), and vertically to any instance size available on the [Neptune pricing page](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/"). All Neptune
read-replica instances uses the same underlying storage volume, enabling transparent
replication of data with minimal lag.

In addition to enabling horizontal scaling of read requests within a Neptune
cluster, read replicas also act as failover targets for the writer instance
to enable high availability. See [Amazon Neptune basic operational guidelines](best-practices-general-basic.md "best-practices-general-basic.md") for suggestions about how to
determine the appropriate number and placement of read replicas in your cluster.

For applications where connectivity and workload are unpredictable, Neptune
also supports [an auto-scaling feature](manage-console-autoscaling.md "manage-console-autoscaling.md")
that can automatically adjust the number of Neptune replicas based on criteria that
you specify.

To determine an optimal size and number of read replica instances requires running
load tests to determine the characteristics of the read workload they must support.
Any instance within Neptune can be resized at any time by [modifying the DB instance class](manage-console-instances-modify.md "manage-console-instances-modify.md").
You can estimate a starting instance size based on concurrency and average query
latency, as described in the [next
section](#migration-provisioning-instance-sizing "#migration-provisioning-instance-sizing").

## Use Neptune Serverless to scale

reader and writer instances automatically as needed

While it is often helpful to be able to estimate the compute capacity that your
anticipated workloads will require, you can configure the [Neptune
Serverless](neptune-serverless.md "neptune-serverless.md") feature to scale read and write capacity up and down automatically.
This can help you meet peak requirements while also scaling back automatically
when demand decreases.

## Estimating optimal instance size when provisioning your cluster

Estimation of optimal instance size requires knowing the average query latency
in Neptune, when your workload is running, as well as the number of concurrent
queries being processed. A rough estimate of instance size can be calculated as the
average query latency multiplied by the number of concurrent queries. This gives you
the average number of concurrent threads needed to handle the workload.

Each vCPU in a Neptune instance can support two concurrent query threads,
so dividing the threads by 2 provides the number of vCPUs required, which can
then be correlated to the appropriate instance size on the [Neptune pricing page](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/").
For example:

```
Average Query Latency:         30ms (0.03s)
Number of concurrent queries:  1000/second

Number of threads needed:      0.03 x 1000 = 30 threads
Number of vCPUs needed:        30 / 2 = 15 vCPUs
```

Correlating this to the number of vCPUs in an instance, we see that we get
a rough estimate that a `r5.4xlarge` would be the recommended instance
to try for this workload. This estimate is rough and only meant to provide initial
guidance on instance-size selection. Any application should go through a
right-sizing exercise to determine the appropriate number and type(s) of
instances that are appropriate for the workload.

Memory requirements should also be taken into account, as well as processing
requirements. Neptune is most performant when the data being accessed by queries
is available in the main-memory buffer pool cache. Provisioning sufficient memory
can also reduce I/O costs significantly.

Additional details and guidance on sizing of instances in a Neptune
cluster can be found on the [Sizing DB instances in a Neptune DB cluster](feature-overview-db-clusters.md#feature-overview-sizing-instances "feature-overview-db-clusters.md#feature-overview-sizing-instances") page.
