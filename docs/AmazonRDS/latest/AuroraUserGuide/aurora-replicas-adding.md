# Adding Aurora Replicas to a DB cluster

An Aurora DB cluster with replication has one primary DB instance and up to 15 Aurora Replicas. The primary DB
instance supports read and write operations, and performs all data modifications to the cluster volume. Aurora Replicas connect to
the same storage volume as the primary DB instance, but support read operations only. You use Aurora Replicas to offload read
workloads from the primary DB instance. For more information, see [Aurora Replicas](Aurora.md#Aurora.Replication.Replicas "Aurora.md#Aurora.Replication.Replicas").

Amazon Aurora Replicas have the following limitations:

- You can't create an Aurora Replica for an Aurora Serverless v1 DB cluster. Aurora Serverless v1 has a single DB instance that scales
  up and down automatically to support all database read and write operations.

However, you can add reader instances to Aurora Serverless v2 DB clusters. For more information, see [Adding an Aurora Serverless v2 reader](aurora-serverless-v2-administration.md#aurora-serverless-v2-adding-reader "aurora-serverless-v2-administration.md#aurora-serverless-v2-adding-reader").
We recommend that you distribute the primary instance and Aurora Replicas of your Aurora DB cluster
over multiple Availability Zones to improve the availability of your DB
cluster. For more information, see [Region availability](Concepts.md#Aurora.Overview.Availability "Concepts.md#Aurora.Overview.Availability").

To remove an Aurora Replica from an Aurora DB cluster, delete the Aurora Replica by following the
instructions in [Deleting a DB instance from an Aurora DB cluster](USER_DeleteCluster.md#USER_DeleteInstance "USER_DeleteCluster.md#USER_DeleteInstance").

###### Note

Amazon Aurora also supports replication with an external database, such as an RDS DB
instance. The RDS DB instance must be in the same AWS Region as Amazon Aurora. For more
information, see [Replication with Amazon Aurora](Aurora.md "Aurora.md").

You can add Aurora Replicas to a DB cluster using the AWS Management Console, the AWS CLI, or the RDS API.

###### To add an Aurora replica to a DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**,
   and then select the DB cluster where you want to add the new DB instance.
3. Make sure that both the cluster and the primary instance are in the
   **Available** state. If the DB cluster or the primary instance
   are in a transitional state such as **Creating**, you can't
   add a replica.

If the cluster doesn't have a primary instance, create one using the
[create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") AWS CLI command.
This situation can arise if you used the CLI to restore a DB cluster snapshot and then
view the cluster in the AWS Management Console. 4. For **Actions**,
choose **Add reader**.

The **Add reader** page appears. 5. On the **Add reader** page, specify options for your Aurora Replica.
The following table shows settings for an Aurora Replica.

| For this option                | Do this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Availability zone**          | Determine if you want to specify a particular Availability Zone. The list includes only those<br>Availability Zones that are mapped to the DB subnet group that you chose when you created the DB<br>cluster. For more information about Availability Zones, see [Regions and Availability Zones](Concepts.md "Concepts.md").                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Publicly accessible**        | Select `Yes` to give the Aurora Replica a<br>public IP address; otherwise, select `No`.<br>For more information about hiding Aurora Replicas from<br>public access, see [Hiding a DB cluster in a VPC from the internet](USER_VPC.md#USER_VPC.Hiding "USER_VPC.md#USER_VPC.Hiding").                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Encryption**                 | Select `Enable encryption` to enable encryption at rest<br>for this Aurora Replica. For more information, see [Encrypting Amazon Aurora resources](Overview.md "Overview.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **DB instance class**          | Select a DB instance class that defines the processing<br>and memory requirements for the Aurora Replica. For<br>more information about DB instance class options, see<br>[Amazon AuroraDB instance classes](Concepts.md "Concepts.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Aurora replica source**      | Select the identifier of the primary instance to<br>create an Aurora Replica for.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **DB instance identifier**     | Enter a name for the instance that is unique for your<br>account in the AWS Region you selected. You might choose<br>to add some intelligence to the name such as including<br>the AWS Region and DB engine you selected, for example<br>`aurora-read-instance1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Priority**                   | Choose a failover priority for the instance. If you<br>don't select a value, the default is<br>**tier-1**. This priority<br>determines the order in which Aurora Replicas are<br>promoted when recovering from a primary instance<br>failure. For more information, see [Fault tolerance for an Aurora DB cluster](Concepts.md#Aurora.Managing.FaultTolerance "Concepts.md#Aurora.Managing.FaultTolerance").                                                                                                                                                                                                                                                                                                                                                     |
| **Database port**              | The port for an Aurora Replica is the same as the port<br>for the DB cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **DB parameter group**         | Select a parameter group. Aurora has a default<br>parameter group you can use, or you can create your own<br>parameter group. For more information about parameter<br>groups, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Performance Insights**       | The \*_Turn on Performance Insights_<br>• check box is selected by default. The<br>value isn't inherited from the writer instance. For more information, see [Monitoring DB load with Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Enhanced monitoring**        | Choose \*_Enable enhanced monitoring_<br>• to enable gathering<br>metrics in real time for the operating system that your<br>DB cluster runs on. For more information, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.md "USER_Monitoring.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Monitoring Role**            | Only available if **Enhanced<br>Monitoring\*<br>• is set to<br>**Enable enhanced monitoring**. Choose the IAM role that<br>you created to permit Amazon RDS to communicate with<br>Amazon CloudWatch Logs for you, or choose **Default\*<br>• to<br>have RDS create a role for you named<br>`rds-monitoring-role`. For more<br>information, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.md "USER_Monitoring.md").                                                                                                                                                                                                                                                                                                                       |
| **Granularity**                | Only available if **Enhanced<br>Monitoring\*<br>• is set to<br>**Enable enhanced monitoring\*\*. Set the interval, in<br>seconds, between when metrics are collected for your DB<br>cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Auto minor version upgrade** | Select **Enable auto minor version upgrade\*<br>• if you want to enable your<br>Aurora DB cluster to receive minor DB Engine<br>version upgrades automatically when they become<br>available.<br>The **Auto minor version upgrade\*<br>• setting applies to both<br>Aurora PostgreSQL and Aurora MySQL DB clusters. For Aurora MySQL 2.x clusters, this setting upgrades the<br>clusters to a maximum version of 2.07.2.<br>For more information about engine updates for Aurora PostgreSQL, see<br>[Database engine updates for Amazon Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md").<br>For more information about engine updates for Aurora MySQL, see<br>[Database engine updates for Amazon Aurora MySQL](AuroraMySQL.md "AuroraMySQL.md"). |

6. Choose **Add reader** to create the Aurora
   Replica.
   To create an Aurora Replica in your DB cluster, run the
   [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") AWS CLI command.
   Include the name of the DB cluster as the `--db-cluster-identifier` option.
   You can optionally specify an Availability Zone for the Aurora Replica using the
   `--availability-zone` parameter, as shown in the following
   examples.

For example, the following command creates a new MySQL 5.7–compatible Aurora Replica named
`sample-instance-us-west-2a`.

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

The following command creates a new MySQL 5.7–compatible Aurora Replica named
`sample-instance-us-west-2a`.

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

The following command creates a new PostgreSQL-compatible Aurora Replica named
`sample-instance-us-west-2a`.

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

To create an Aurora Replica in your DB cluster, call the
[CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md") operation.
Include the name of the DB cluster as the `DBClusterIdentifier` parameter.
You can optionally specify an Availability Zone for the Aurora Replica using the
`AvailabilityZone` parameter.

For information about Auto Scaling Amazon Aurora with Aurora replicas, see the following sections.

###### Topics

- [Amazon Aurora Auto Scaling with Aurora Replicas](Aurora.Integrating.md "Aurora.Integrating.md")
- [Adding an auto scaling policy to an Amazon Aurora DB cluster](Aurora.Integrating.AutoScaling.md "Aurora.Integrating.AutoScaling.md")
- [Editing an auto scaling policy for an Amazon Aurora DB cluster](Aurora.Integrating.AutoScaling.md "Aurora.Integrating.AutoScaling.md")
- [Deleting an auto scaling policy from your Amazon Aurora DB cluster](Aurora.Integrating.AutoScaling.md "Aurora.Integrating.AutoScaling.md")
