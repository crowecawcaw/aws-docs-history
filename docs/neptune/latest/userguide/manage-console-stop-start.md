# Stopping and starting an Amazon Neptune DB cluster

Stopping and starting Amazon Neptune clusters helps you manage costs for development and test
environments. You can temporarily stop all the DB instances in your cluster, instead of
setting up and tearing down all the DB instances each time that you use the cluster.

###### Topics

- [Overview of stopping and
  starting a Neptune DB cluster](#manage-console-start-stop-overview "#manage-console-start-stop-overview")
- [Stopping a Neptune DB cluster](#manage-console-stopping "#manage-console-stopping")
- [Starting a stopped Neptune DB cluster](#manage-console-start "#manage-console-start")

## Overview of stopping and

starting a Neptune DB cluster

During periods where you don't need a Neptune cluster, you can stop all instances
in that cluster at once. You can start the cluster again anytime you need to use it.
Starting and stopping simplifies the setup and teardown processes for clusters used for
development, testing, or similar activities that don't require continuous availability.
You can accomplish this in the AWS Management Console with a single action, regardless of how many
instances there are in the cluster.

While your DB cluster is stopped, you are charged only for cluster storage, manual
snapshots, and automated backup storage within your specified retention window. You
aren't charged for any DB instance hours.

After seven days, Neptune automatically starts your DB cluster again to make sure
that it doesn't fall behind any required maintenance updates.

To minimize charges for a lightly loaded Neptune cluster, you can stop the cluster
instead of deleting all its read replicas. For clusters with more than one or two instances,
frequently deleting and recreating the DB instances is only practical using the AWS CLI or
Neptune API, and deletions can also be difficult to perform in the right order. For example,
you must delete all read replicas before deleting the primary instance to avoid activating
the failover mechanism.

Don't use starting and stopping if you need to keep your DB cluster running but you want
to reduce capacity. If your cluster is too costly or not very busy, you can delete one or more DB
instances or change your DB instances to use a smaller instance class, but you can't
stop an individual DB instance.

## Stopping a Neptune DB cluster

When you won't be using it for a while, you can stop a running Neptune DB cluster,
and then start it again when you need it. While the cluster is stopped you are charged
for cluster storage, manual snapshots, and automated backup storage within your specified
retention window, but not for DB instance hours.

The stop operation stops all the cluster's read replica instances before stopping the
primary instance, to avoid activating the failover mechanism.

### Stopping a DB cluster using the AWS Management Console

###### To use the AWS Management Console to stop a Neptune cluster

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Databases**,
   and then choose a cluster. You can perform the stop operation from this
   page, or navigate to the details page for the DB cluster that you want
   to stop.
3. In **Actions**, choose
   **Stop**.

### Stopping a DB cluster using the AWS CLI

To stop a DB instance by using the AWS CLI, call the [stop-db-cluster](api-clusters.md#StopDBCluster "api-clusters.md#StopDBCluster")
command, using the `--db-cluster-identifier` parameter to identify the DB
cluster you want to stop.

###### Example

```
aws neptune stop-db-cluster --db-cluster-identifier `mydbcluster`
```

### Stopping a DB cluster using the Neptune management API

To stop a DB instance by using the Neptune management API, call the [StopDBCluster](api-clusters.md#StopDBCluster "api-clusters.md#StopDBCluster") API and use the `DBClusterIdentifier`
parameter to identify the DB cluster you want to stop.

### What can happen while a DB cluster is stopped

- You **can** restore it from
  a snapshot (see [Restoring from a DB Cluster Snapshot](backup-restore-restore-snapshot.md "backup-restore-restore-snapshot.md")).
- You **can't** modify the
  configuration of the DB cluster or any of its DB instances.
- You **can't** add or remove
  DB instances from the cluster.
- You **can't** delete the cluster
  if it still has any associated DB instances.
- In general, you must re-start a stopped DB cluster to
  perform most administrative actions.
- Neptune applies any scheduled maintenance to your stopped
  cluster as soon as it is started again. Remember that after seven days,
  Neptune automatically re-starts a stopped cluster so that it doesn't
  fall too far behind in maintenance status.
- Neptune does not perform any automated backups of a
  stopped DB cluster, because the underlying data cannot change while
  the cluster is stopped.
- Neptune does not extend the backup retention period for the DB cluster
  while it is stopped.

## Starting a stopped Neptune DB cluster

You can only start a Neptune DB cluster that is in the stopped state.
When you start the cluster, all its DB instances become available again.
The cluster retains its configuration settings, such as endpoints, parameter
groups and VPC security groups.

### Starting a stopped DB cluster using the AWS Management Console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Databases**, and then
   choose a cluster. You can perform the start operation from this page, or navigate
   to the details page for that DB cluster and start from there.
3. In **Actions**, choose **Start**.

### Starting a stopped DB cluster using the AWS CLI

To start a stopped DB cluster using the AWS CLI, call the [start-db-cluster](api-clusters.md#StartDBCluster "api-clusters.md#StartDBCluster")
command using the `--db-cluster-identifier` parameter to specify the stopped
DB cluster that you want to start. Provide either the cluster name that you chose when
creating the DB cluster, or use a DB instance name that you chose with `-cluster`
appended to the end of it.

###### Example

```
aws neptune start-db-cluster --db-cluster-identifier `mydbcluster`
```

### Starting a stopped DB cluster using the Neptune management API

To start a Neptune DB cluster by using the Neptune management API, call the
[StartDBCluster](api-clusters.md#StartDBCluster "api-clusters.md#StartDBCluster") API using the `DBCluster`
parameter to specify the stopped DB cluster that you want to start. Provide either the
cluster name that you chose when creating the DB cluster, or use a DB instance name that you
chose, with `-cluster` appended to the end of it.
