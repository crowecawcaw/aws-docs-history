

# Adding Aurora Replicas to a DB cluster
<a name="aurora-replicas-adding"></a><a name="create_instance"></a>

An Aurora DB cluster with replication has one primary DB instance and up to 15 Aurora Replicas. The primary DB instance supports read and write operations, and performs all data modifications to the cluster volume. Aurora Replicas connect to the same storage volume as the primary DB instance, but support read operations only. You use Aurora Replicas to offload read workloads from the primary DB instance. For more information, see [Aurora Replicas](Aurora.Replication.md#Aurora.Replication.Replicas). 

Amazon Aurora Replicas have the following limitations:
+ However, you can add reader instances to Aurora serverless DB clusters. For more information, see [Adding an Aurora serverless reader](aurora-serverless-v2-administration.md#aurora-serverless-v2-adding-reader).

We recommend that you distribute the primary instance and Aurora Replicas of your Aurora DB cluster over multiple Availability Zones to improve the availability of your DB cluster. For more information, see [Region availability](Concepts.RegionsAndAvailabilityZones.md#Aurora.Overview.Availability).

To remove an Aurora Replica from an Aurora DB cluster, delete the Aurora Replica by following the instructions in [Deleting a DB instance from an Aurora DB cluster](USER_DeleteCluster.md#USER_DeleteInstance).

**Note**  
Amazon Aurora also supports replication with an external database, such as an RDS DB instance. The RDS DB instance must be in the same AWS Region as Amazon Aurora. For more information, see [Replication with Amazon Aurora](Aurora.Replication.md).

You can add Aurora Replicas to a DB cluster using the AWS Management Console, the AWS CLI, or the RDS API.

## Console
<a name="aurora-replicas-adding.Console"></a>

**To add an Aurora replica to a DB cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then select the DB cluster where you want to add the new DB instance. 

1.  Make sure that both the cluster and the primary instance are in the **Available** state. If the DB cluster or the primary instance are in a transitional state such as **Creating**, you can't add a replica. 

    If the cluster doesn't have a primary instance, create one using the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) AWS CLI command. This situation can arise if you used the CLI to restore a DB cluster snapshot and then view the cluster in the AWS Management Console. 

1. For **Actions**, choose **Add reader**. 

   The **Add reader** page appears.

1. On the **Add reader** page, specify options for your Aurora Replica. The following table shows settings for an Aurora Replica.

<a name="aurora_replica_settings"></a>
<table>
<thead>
  <tr><th>For this option</th><th>Do this</th></tr>
</thead>
<tbody>
  <tr><td> <b>Availability zone</b> </td><td>Determine if you want to specify a particular Availability Zone. The list includes only those Availability Zones that are mapped to the DB subnet group that you chose when you created the DB cluster. For more information about Availability Zones, see <a href="Concepts.RegionsAndAvailabilityZones.md">Regions and Availability Zones</a>.</td></tr>
  <tr><td> <b>Publicly accessible</b> </td><td>Select <code>Yes</code> to give the Aurora Replica a public IP address; otherwise, select <code>No</code>. For more information about hiding Aurora Replicas from public access, see <a href="USER_VPC.WorkingWithRDSInstanceinaVPC.md#USER_VPC.Hiding">Hiding a DB cluster in a VPC from the internet</a>.</td></tr>
  <tr><td> <b>Encryption</b> </td><td>Select <code>Enable encryption</code> to enable encryption at rest for this Aurora Replica. For more information, see <a href="Overview.Encryption.md">Encrypting Amazon Aurora resources</a>.</td></tr>
  <tr><td> <b>DB instance class</b> </td><td>Select a DB instance class that defines the processing and memory requirements for the Aurora Replica. For more information about DB instance class options, see <a href="Concepts.DBInstanceClass.md">Amazon AuroraDB instance classes</a>.</td></tr>
  <tr><td> <b>Aurora replica source</b> </td><td>Select the identifier of the primary instance to create an Aurora Replica for.</td></tr>
  <tr><td> <b>DB instance identifier</b> </td><td>Enter a name for the instance that is unique for your account in the AWS Region you selected. You might choose to add some intelligence to the name such as including the AWS Region and DB engine you selected, for example <b>aurora-read-instance1</b>.</td></tr>
  <tr><td> <b>Priority</b> </td><td>Choose a failover priority for the instance. If you don't select a value, the default is <b>tier-1</b>. This priority determines the order in which Aurora Replicas are promoted when recovering from a primary instance failure. For more information, see <a href="Concepts.AuroraHighAvailability.md#Aurora.Managing.FaultTolerance">Fault tolerance for an Aurora DB cluster</a>.</td></tr>
  <tr><td> <b>Database port</b> </td><td>The port for an Aurora Replica is the same as the port for the DB cluster.</td></tr>
  <tr><td> <b>DB parameter group</b> </td><td>Select a parameter group. Aurora has a default parameter group you can use, or you can create your own parameter group. For more information about parameter groups, see <a href="USER_WorkingWithParamGroups.md">Parameter groups for Amazon Aurora</a>.</td></tr>
  <tr><td><b>Performance Insights</b> </td><td>The <b>Turn on Performance Insights</b> check box is selected by default. The value isn't inherited from the writer instance. For more information, see <a href="USER_PerfInsights.md">Monitoring DB load with Amazon CloudWatch Database Insights on Amazon Aurora</a>.</td></tr>
  <tr><td><b>Enhanced monitoring</b></td><td>Choose <b>Enable enhanced monitoring</b> to enable gathering metrics in real time for the operating system that your DB cluster runs on. For more information, see <a href="USER_Monitoring.OS.md">Monitoring OS metrics with Enhanced Monitoring</a>. </td></tr>
  <tr><td><b>Monitoring Role</b></td><td>Only available if <b>Enhanced Monitoring</b> is set to <b>Enable enhanced monitoring</b>. Choose the IAM role that you created to permit Amazon RDS to communicate with Amazon CloudWatch Logs for you, or choose <b>Default</b> to have RDS create a role for you named <code>rds-monitoring-role</code>. For more information, see <a href="USER_Monitoring.OS.md">Monitoring OS metrics with Enhanced Monitoring</a>. </td></tr>
  <tr><td><b>Granularity</b></td><td>Only available if <b>Enhanced Monitoring</b> is set to <b>Enable enhanced monitoring</b>. Set the interval, in seconds, between when metrics are collected for your DB cluster.</td></tr>
  <tr><td> <b>Auto minor version upgrade</b> </td><td>Select <b>Enable auto minor version upgrade</b> if you want to enable your Aurora DB cluster to receive minor DB Engine version upgrades automatically when they become available.<br />The <b>Auto minor version upgrade</b> setting applies to both Aurora PostgreSQL and Aurora MySQL DB clusters. For Aurora MySQL 2.x clusters, this setting upgrades the clusters to a maximum version of 2.07.2.<br />For more information about engine updates for Aurora PostgreSQL, see <a href="AuroraPostgreSQL.Updates.md">Database engine updates for Amazon Aurora PostgreSQL</a>.<br />For more information about engine updates for Aurora MySQL, see <a href="AuroraMySQL.Updates.md">Database engine updates for Amazon Aurora MySQL</a>.</td></tr>
</tbody>
</table>


1. Choose **Add reader** to create the Aurora Replica.

## AWS CLI
<a name="aurora-replicas-adding.CLI"></a>

To create an Aurora Replica in your DB cluster, run the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) AWS CLI command. Include the name of the DB cluster as the `--db-cluster-identifier` option. You can optionally specify an Availability Zone for the Aurora Replica using the `--availability-zone` parameter, as shown in the following examples.

For example, the following command creates a new MySQL 5.7–compatible Aurora Replica named `sample-instance-us-west-2a`.

For Linux, macOS, or Unix:

```
aws rds create-db-instance --db-instance-identifier sample-instance-us-west-2a \
    --db-cluster-identifier sample-cluster --engine aurora-mysql --db-instance-class db.r5.large \
    --availability-zone us-west-2a
```

For Windows:

```
aws rds create-db-instance --db-instance-identifier sample-instance-us-west-2a ^
    --db-cluster-identifier sample-cluster --engine aurora-mysql --db-instance-class db.r5.large ^
    --availability-zone us-west-2a
```

The following command creates a new MySQL 5.7–compatible Aurora Replica named `sample-instance-us-west-2a`.

For Linux, macOS, or Unix:

```
aws rds create-db-instance --db-instance-identifier sample-instance-us-west-2a \
    --db-cluster-identifier sample-cluster --engine aurora-mysql --db-instance-class db.r5.large \
    --availability-zone us-west-2a
```

For Windows:

```
aws rds create-db-instance --db-instance-identifier sample-instance-us-west-2a ^
    --db-cluster-identifier sample-cluster --engine aurora --db-instance-class db.r5.large ^
    --availability-zone us-west-2a
```

The following command creates a new PostgreSQL-compatible Aurora Replica named `sample-instance-us-west-2a`.

For Linux, macOS, or Unix:

```
aws rds create-db-instance --db-instance-identifier sample-instance-us-west-2a \
    --db-cluster-identifier sample-cluster --engine aurora-postgresql --db-instance-class db.r5.large \
    --availability-zone us-west-2a
```

For Windows:

```
aws rds create-db-instance --db-instance-identifier sample-instance-us-west-2a ^
    --db-cluster-identifier sample-cluster --engine aurora-postgresql --db-instance-class db.r5.large ^
    --availability-zone us-west-2a
```

## RDS API
<a name="aurora-replicas-adding.API"></a>

To create an Aurora Replica in your DB cluster, call the [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) operation. Include the name of the DB cluster as the `DBClusterIdentifier` parameter. You can optionally specify an Availability Zone for the Aurora Replica using the `AvailabilityZone` parameter.

For information about Auto Scaling Amazon Aurora with Aurora replicas, see the following sections.

**Topics**
+ [Amazon Aurora Auto Scaling with Aurora Replicas](Aurora.Integrating.AutoScaling.md)
+ [Adding an auto scaling policy to an Amazon Aurora DB cluster](Aurora.Integrating.AutoScaling.Add.md)
+ [Editing an auto scaling policy for an Amazon Aurora DB cluster](Aurora.Integrating.AutoScaling.Edit.md)
+ [Deleting an auto scaling policy from your Amazon Aurora DB cluster](Aurora.Integrating.AutoScaling.Delete.md)