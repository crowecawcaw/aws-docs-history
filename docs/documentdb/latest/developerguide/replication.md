# Amazon DocumentDB High availability and replication

You can achieve high availability and read scaling in Amazon DocumentDB (with MongoDB compatibility) by using replica instances. A single Amazon DocumentDB cluster supports a single primary instance and up to 15 replica instances. These instances can be distributed across Availability Zones within the cluster's Region. The primary instance accepts read and write traffic, and replica instances accept only read requests.

The cluster volume is made up of multiple copies of the data for the cluster. However, the data in the cluster volume is represented as a single, logical volume to the primary instance and to Amazon DocumentDB replicas in the cluster. Replica instances are eventually consistent. They return query results with minimal replica lag—usually much less than 100 milliseconds after the primary instance has written an update. Replica lag varies depending on the rate of database change. That is, during periods in which a large number of write operations occur for the database, you might see an increase in the replica lag.

## Read scaling

Amazon DocumentDB replicas work well for read scaling because they are fully dedicated to read operations on your cluster volume. Write operations are managed by the primary instance. The cluster volume is shared among all instances in your cluster. Therefore, you don't have to replicate and maintain a copy of the data for each Amazon DocumentDB replica.

## High availability

When you create an Amazon DocumentDB cluster, depending upon the number of Availability Zones in the subnet group (there must be at least two), Amazon DocumentDB provisions instances across the Availability Zones. When you create instances in the cluster, Amazon DocumentDB automatically distributes the instances across the Availability Zones in a subnet group to balance the cluster. This action also prevents all instances from being located in the same Availability Zone.

###### Example

To illustrate the point, consider an example where you create a cluster that has a subnet group with three Availability Zones:
_AZ1_, _AZ2_, and _AZ3_.

When the first instance in the cluster is created, it is the primary instance and is located in one of the Availability Zones. In this example, it's in _AZ1_. The second instance created is a replica instance and is located in one of the other two Availability Zones, say _AZ2_. The third instance created is a replica instance and is located in the remaining Availability Zone, _AZ3_. If you create more instances, they are distributed across the Availability Zones so that you achieve balance in the cluster.

If a failure occurs in the primary instance (AZ1), a failover is triggered, and one of the existing replicas is promoted to primary. When the old primary recovers, it becomes a replica in the same Availability Zone in which it was provisioned (AZ1). When you provision a three-instance cluster, Amazon DocumentDB continues to preserve that three-instance cluster. Amazon DocumentDB automatically handles detection, failover, and recovery of instance failures without any manual intervention.

When Amazon DocumentDB performs a failover and recovers an instance, the recovered instance remains in the Availability Zone in which it was originally provisioned. However, the role of the instance might change from primary to replica. Doing this prevents the scenario in which a series of failovers could result in all instances being in the same Availability Zone.

You can specify Amazon DocumentDB replicas as failover targets. That is, if the primary instance fails, the specified Amazon DocumentDB replica or replica from a tier is promoted to the primary instance. There is a brief interruption during which read and write requests made to the primary instance fail with an exception. If your Amazon DocumentDB cluster doesn't include any Amazon DocumentDB replicas, when the primary instance fails, it is re-created. Promoting an Amazon DocumentDB replica is much faster than re-creating the primary instance.

For high availability scenarios, we recommend that you create one or more Amazon DocumentDB replicas. These replicas should be of the same instance class as the primary instance and in different Availability Zones for your Amazon DocumentDB cluster.

For more information, see the following:

- [Understanding Amazon DocumentDB cluster fault tolerance](db-cluster-fault-tolerance.md "db-cluster-fault-tolerance.md")
- [Amazon DocumentDB Failover](failover.md "failover.md")
  - [Controlling the failover target](failover.md#failover-target_control "failover.md#failover-target_control")

### High availability with global clusters

For high availability across multiple AWS Regions, you can set up [Amazon DocumentDB global clusters](global-clusters.md "global-clusters.md"). Each global cluster spans multiple regions, enabling low latency global reads and disaster recovery from outages across an AWS Region. Amazon DocumentDB automatically handles replicating all data and updates from the primary region to each of the secondary regions.

## Adding replicas

The first instance added to the cluster is the primary instance. Every instance that is added after the first instance is a replica instance. A cluster can have up to 15 replica instances in addition to the primary.

When you create a cluster using the AWS Management Console, a primary instance is automatically created at the same time. To create a replica at the same time as you create the cluster and the primary instance, choose **Create replica in different zone**. For more information, see step 4.d in [Creating an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md"). To add more replicas to an Amazon DocumentDB cluster, see [Adding an Amazon DocumentDB instance to a cluster](db-instance-add.md "db-instance-add.md").

When using the AWS CLI to create your cluster, you must explicitly create your primary and replica instances. For more information, see the "Using the AWS CLI" section in the following topics:

- [Creating an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md")
- [Adding an Amazon DocumentDB instance to a cluster](db-instance-add.md "db-instance-add.md")

## Replication lag

Replication lag is typically 50ms or less. The most common reasons for increased replica lag are:

- A high write rate on the primary that causes the read replicas to fall behind the primary.
- Contention on the read replicas between long running queries (e.g., large sequential scans, aggregation queries) and incoming write replication.
- Very large number of concurrent queries on the read replicas.

To minimize replication lag, try these troubleshooting techniques:

- If you have a high write rate or high CPU utilization, we recommend that you scale up the instances in your cluster.
- If there are long running queries on your read replicas, and very frequent updates to the documents being queried, consider altering your long running queries, or running them against the primary/write replica to avoid contention on the read replicas.
- If there is a very large number of concurrent queries or high CPU utilization only on the read replicas, another option is to scale out the number of read replicas to spread out the workload.
- Because replication lag is a result of high write throughput and long running queries, we recommend troubleshooting the replication lag by utilizing the DBClusterReplicaLagMaximum CW metric in combination with the slow query logger and `WriteThroughput`/`WriteIOPS` metrics.

In general, we recommend that all your replicas are of the same instance type, so that a cluster failover will not cause a degradation in performance.

If you are choosing between scaling up and scaling out (eg. six smaller instances vs three larger instances), we generally recommend trying to scale up first (larger instances) before scaling out, as you will get a larger buffer cache per DB instance.

Proactively, you should set a replication lag alarm and set its threshold to a value that you feel is the upper bound for how far behind (or “stale”) your data on replica instances can be before it starts affecting the functionality of your application. In general, we would advise that the replication lag threshold be exceeded for several data points before alarming, due to transient workloads.

###### Note

In addition, we recommend that you set another alarm for replication lags that exceed 10 seconds. If you surpass this threshold for multiple data points, we recommend that you scale up your instances or reduce your write throughput on the primary instance.
