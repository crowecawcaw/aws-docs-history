# Stopping and starting an Amazon Aurora DB cluster

Stopping and starting Aurora DB clusters helps you manage costs for development and test
environments. You can temporarily stop all the DB instances in your cluster, instead of
setting up and tearing down all the DB instances each time that you use the cluster.

###### Topics

- [Overview of stopping and starting an Aurora DB
  cluster](#aurora-cluster-start-stop-overview "#aurora-cluster-start-stop-overview")
- [Limitations for stopping and starting Aurora DB clusters](#aurora-cluster-stop-limitations "#aurora-cluster-stop-limitations")
- [Stopping an Aurora DB cluster](#aurora-cluster-stop "#aurora-cluster-stop")
- [Possible operations while an Aurora DB cluster is
  stopped](#aurora-cluster-stopped "#aurora-cluster-stopped")
- [Starting an Aurora DB cluster](#aurora-cluster-start "#aurora-cluster-start")

## Overview of stopping and starting an Aurora DB

cluster

During periods where you don't need an Aurora DB cluster, you can stop all instances in that
cluster at once. You can start the cluster again anytime you need to use it. Starting
and stopping simplifies the setup and teardown processes for clusters used for
development, testing, or similar activities that don't require continuous availability.
You can perform all the AWS Management Console procedures involved with only a single action,
regardless of how many instances are in the cluster.

While your DB cluster is stopped, you're charged only for cluster storage, manual snapshots,
and automated backup storage within your specified retention window. You aren't charged
for any DB instance hours.

###### Important

You can stop a DB cluster for up to seven days. If you don't manually start your DB
cluster after seven days, your DB cluster is automatically started so that it
doesn't fall behind any required maintenance updates.

To minimize charges for a lightly loaded Aurora cluster, you can stop the cluster instead of
deleting all of its Aurora Replicas. For clusters with more than one or two instances,
frequently deleting and recreating the DB instances is only practical using the AWS CLI or
Amazon RDS API. Such a sequence of operations can also be difficult to perform in the right
order, for example to delete all Aurora Replicas before deleting the primary instance to
avoid activating the failover mechanism.

Don't use starting and stopping if you need to keep your DB cluster running but it has more
capacity than you need. If your cluster is too costly or not very busy, delete one or
more DB instances or change all your DB instances to a small instance class. You
can't stop an individual Aurora DB instance.

The time to stop your DB cluster varies depending on factors such as DB instance classes, network
state, DB engine type, and database state. The process can take several minutes. The Amazon RDS
service performs the following actions:

- Shuts down the database engine processes.
- Shuts down the RDS platform processes.
- Terminates the underlying Amazon EC2 instances.

The time to restart your DB cluster varies depending on factors such as database size,
DB instance classes, network state, DB engine type, and the database state when the cluster was
shut down. The startup process can take minutes to hours, but usually takes several
minutes. We recommend that you consider the variability in startup time when creating
your availability plan.

To start the DB cluster, the service performs actions such as the following:

- Provisions the underlying Amazon EC2 instances.
- Starts the RDS platform processes.
- Starts the database engine processes.
- Recovers the DB instances (recovery occurs even after a normal shutdown).

## Limitations for stopping and starting Aurora DB clusters

Some Aurora clusters can't be stopped and started:

- You can only stop and start a cluster that's part of an [Aurora global database](aurora-global-database.md "aurora-global-database.md") if it's the only cluster in the global database.
- You can't stop and start a cluster that has a cross-Region read replica.
- You can't stop and start a cluster that is part of a [blue/green deployment](blue-green-deployments.md "blue-green-deployments.md").
- You can't stop and start an [Aurora Serverless v1 cluster](aurora-serverless.md "aurora-serverless.md").
  With [Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md"), you can stop and start the cluster.

## Stopping an Aurora DB cluster

To use an Aurora DB cluster or perform administration, you always begin with a running Aurora
DB cluster, then stop the cluster, and then start the cluster again. While your cluster
is stopped, you are charged for cluster storage, manual snapshots, and automated backup
storage within your specified retention window, but not for DB instance hours.

The stop operation stops the Aurora Replica instances first, then the primary instance, to
avoid activating the failover mechanism.

###### To stop an Aurora cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose a cluster.
   You can perform the stop operation from this page, or navigate to the
   details page for the DB cluster that you want to stop.
3. For **Actions**, choose **Stop temporarily**.
4. In the **Stop DB cluster temporarily** window, select the
   acknowledgement that the DB cluster will restart automatically after 7 days.
5. Choose **Stop temporarily** to stop the DB cluster,
   or choose **Cancel** to cancel the operation.
   To stop a DB instance by using the AWS CLI, call the
   [stop-db-cluster](../../../cli/latest/reference/rds/stop-db-cluster.md "../../../cli/latest/reference/rds/stop-db-cluster.md") command
   with the following parameters:

- `--db-cluster-identifier` –
  the name of the Aurora cluster.

```
aws rds stop-db-cluster --db-cluster-identifier `mydbcluster`

```

To stop a DB instance by using the Amazon RDS API,
call the
[StopDBCluster](../APIReference/API_StopDBCluster.md "../APIReference/API_StopDBCluster.md") operation
with the following parameter:

- `DBClusterIdentifier` –
  the name of the Aurora cluster.

## Possible operations while an Aurora DB cluster is

stopped

While an Aurora cluster is stopped, you can do a point-in-time restore to any point within
your specified automated backup retention window. For details about doing a
point-in-time restore, see [Restoring data](Aurora.Managing.md#Aurora.Managing.Backups.Restore "Aurora.Managing.md#Aurora.Managing.Backups.Restore").

You can't modify the configuration of an Aurora DB cluster, or any of its DB instances,
while the cluster is stopped. You also can't add or remove DB instances from the
cluster, or delete the cluster if it still has any associated DB instances. You must
start the cluster before performing any such administrative actions.

Stopping a DB cluster removes pending actions, except for the DB cluster parameter group or for the DB parameter groups of the
DB cluster instances.

Aurora applies any scheduled maintenance to your stopped cluster after it's started
again. Remember that after seven days, Aurora automatically starts any stopped clusters
so that they don't fall too far behind in their maintenance status.

Aurora also doesn't perform any automated backups, because the underlying data can't
change while the cluster is stopped. Aurora doesn't extend the backup retention period
while the cluster is stopped.

## Starting an Aurora DB cluster

You always start an Aurora DB cluster beginning with an Aurora cluster that is already in the stopped state. When you start the
cluster, all its DB instances become available again. The cluster keeps its configuration settings such as endpoints, parameter
groups, and VPC security groups.

Starting your DB cluster usually takes several minutes.

###### To start an Aurora cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose a cluster.
   You can perform the start operation from this page, or navigate to the
   details page for the DB cluster that you want to start.
3. For **Actions**, choose **Start**.
   To start a DB cluster by using the AWS CLI, call the [start-db-cluster](../../../cli/latest/reference/rds/start-db-cluster.md "../../../cli/latest/reference/rds/start-db-cluster.md")
   command with the following parameters:

- `--db-cluster-identifier` – the name of the Aurora cluster. This name is
  either a specific cluster identifier you chose when creating the
  cluster, or the DB instance identifier you chose with
  `-cluster` appended to the end.

```
aws rds start-db-cluster --db-cluster-identifier `mydbcluster`

```

To start an Aurora DB cluster by using the Amazon RDS API, call the [StartDBCluster](../APIReference/API_StartDBCluster.md "../APIReference/API_StartDBCluster.md") operation
with the following parameter:

- `DBCluster` – the name of the Aurora cluster. This name is either a
  specific cluster identifier you chose when creating the cluster, or the
  DB instance identifier you chose with `-cluster` appended to
  the end.
