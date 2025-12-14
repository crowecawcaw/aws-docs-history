# Creating an Aurora Serverless v1 DB cluster

###### Important

AWS has [announced the end-of-life date for Aurora Serverless v1: March 31st, 2025](https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon "https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon"). All Aurora Serverless v1 clusters that are
not migrated by March 31, 2025 will be migrated to Aurora Serverless v2 during the maintenance window. If the upgrade fails, Amazon Aurora converts the Serverless v1
cluster to a provisioned cluster with the equivalent engine version during the maintenance window. If applicable, Amazon Aurora will enroll the
converted provisioned cluster in Amazon RDS Extended Support. For more information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

The following procedure creates an Aurora Serverless v1 cluster without any of your schema objects or data. If
you want to create an Aurora Serverless v1 cluster that's a duplicate of an existing provisioned or
Aurora Serverless v1 cluster, you can perform a snapshot restore or cloning operation instead. For those
details, see [Restoring from a DB cluster snapshot](aurora-restore-snapshot.md "aurora-restore-snapshot.md") and
[Cloning a volume for an Amazon Aurora DB cluster](Aurora.Managing.md "Aurora.Managing.md"). You can't convert an
existing provisioned cluster to Aurora Serverless v1. You also can't convert an existing Aurora Serverless v1
cluster back to a provisioned cluster.

When you create an Aurora Serverless v1 DB cluster, you can set the minimum and maximum capacity for the
cluster. A capacity unit is equivalent to a specific compute and memory configuration. Aurora Serverless v1
creates scaling rules for thresholds for CPU utilization, connections, and available memory and seamlessly
scales to a range of capacity units as needed for your applications. For more information see
[Aurora Serverless v1 architecture](aurora-serverless-v1.md#aurora-serverless.architecture "aurora-serverless-v1.md#aurora-serverless.architecture").

You can set the following specific values for your Aurora Serverless v1 DB cluster:

- **Minimum Aurora capacity unit** – Aurora Serverless v1 can reduce capacity down to
  this capacity unit.
- **Maximum Aurora capacity unit** – Aurora Serverless v1 can increase capacity up to
  this capacity unit.

You can also choose the following optional scaling configuration options:

- **Force scaling the capacity to the specified values when the timeout is reached**
  – You can choose this setting if you want Aurora Serverless v1 to force Aurora Serverless v1 to scale
  even if it can't find a scaling point before it times out. If you want Aurora Serverless v1 to cancel
  capacity changes if it can't find a scaling point, don't choose this setting. For more
  information, see
  [Timeout action for capacity changes](aurora-serverless-v1.md#aurora-serverless.how-it-works.timeout-action "aurora-serverless-v1.md#aurora-serverless.how-it-works.timeout-action").
- **Pause compute capacity after consecutive minutes of inactivity** – You can
  choose this setting if you want Aurora Serverless v1 to scale to zero when there's no activity on your
  DB cluster for an amount of time you specify. With this setting enabled, your Aurora Serverless v1 DB
  cluster automatically resumes processing and scales to the necessary capacity to handle the workload when
  database traffic resumes. To learn more, see
  [Pause and resume for Aurora Serverless v1](aurora-serverless-v1.md#aurora-serverless.how-it-works.pause-resume "aurora-serverless-v1.md#aurora-serverless.how-it-works.pause-resume").

Before you can create an Aurora Serverless v1 DB cluster, you need an AWS account. You also need to have
completed the setup tasks for working with Amazon Aurora. For more information, see
[Setting up your environment for Amazon Aurora](CHAP_SettingUp_Aurora.md "CHAP_SettingUp_Aurora.md"). You also need to complete other
preliminary steps for creating any Aurora DB cluster. To learn more, see
[Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

Aurora Serverless v1 is available in certain AWS Regions and for specific Aurora MySQL and Aurora PostgreSQL
versions only. For more information, see
[Aurora Serverless v1](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

###### Note

The cluster volume for an Aurora Serverless v1 cluster is always encrypted. When you create your
Aurora Serverless v1 DB cluster, you can't turn off encryption, but you can choose to use your own
encryption key. With Aurora Serverless v2, you can choose whether to encrypt the cluster volume.

You can create an Aurora Serverless v1 DB cluster with the AWS CLI or the RDS API.

###### Note

If you receive the following error message when trying to create your cluster, your account needs additional permissions.

`Unable to create the resource. Verify that you have permission to create service linked role. Otherwise wait and try
 again later.`

See [Using service-linked roles for
Amazon Aurora](UsingWithRDS.IAM.md "UsingWithRDS.IAM.md") for more
information.

You can't directly connect to the DB instance on your Aurora Serverless v1 DB cluster. To connect to your
Aurora Serverless v1 DB cluster, you use the database endpoint. You can find the endpoint for your Aurora Serverless v1 DB cluster
on the **Connectivity & security** tab for your cluster in the AWS Management Console. For more information, see [Connecting to an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

To create a new Aurora Serverless v1 DB cluster with the AWS CLI, run the
[create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md") command and specify
`serverless` for the `--engine-mode` option.

You can optionally specify the `--scaling-configuration` option to configure the minimum
capacity, maximum capacity, and automatic pause when there are no connections.

The following command examples create a new Serverless DB cluster by setting the
`--engine-mode` option to `serverless`. The examples also specify
values for the `--scaling-configuration` option.

### Example for Aurora MySQL

The following command creates a new Aurora MySQL–compatible Serverless DB cluster. Valid capacity values for
Aurora MySQL are `1`, `2`, `4`, `8`, `16`, `32`,
`64`, `128`, and `256`.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster --db-cluster-identifier `sample-cluster` \
    --engine aurora-mysql --engine-version 5.7.mysql_aurora.2.11.4 \
    --engine-mode serverless \
    --scaling-configuration MinCapacity=4,MaxCapacity=32,SecondsUntilAutoPause=1000,AutoPause=true \
    --master-username `username` --master-user-password `password`
```

For Windows:

```
aws rds create-db-cluster --db-cluster-identifier `sample-cluster` ^
    --engine aurora-mysql --engine-version 5.7.mysql_aurora.2.11.4 ^
    --engine-mode serverless ^
    --scaling-configuration MinCapacity=4,MaxCapacity=32,SecondsUntilAutoPause=1000,AutoPause=true ^
    --master-username `username` --master-user-password `password`
```

### Example for Aurora PostgreSQL

The following command creates a new PostgreSQL 13.9–compatible Serverless DB cluster. Valid capacity values for
Aurora PostgreSQL are `2`, `4`, `8`, `16`, `32`, `64`,
`192`, and `384`.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster --db-cluster-identifier `sample-cluster` \
    --engine aurora-postgresql --engine-version 13.9 \
    --engine-mode serverless \
    --scaling-configuration MinCapacity=8,MaxCapacity=64,SecondsUntilAutoPause=1000,AutoPause=true \
    --master-username `username` --master-user-password `password`
```

For Windows:

```
aws rds create-db-cluster --db-cluster-identifier `sample-cluster` ^
    --engine aurora-postgresql --engine-version 13.9 ^
    --engine-mode serverless ^
    --scaling-configuration MinCapacity=8,MaxCapacity=64,SecondsUntilAutoPause=1000,AutoPause=true ^
    --master-username `username` --master-user-password `password`
```

To create a new Aurora Serverless v1 DB cluster with the RDS API, run the
[CreateDBCluster](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md") operation and specify
`serverless` for the `EngineMode` parameter.

You can optionally specify the `ScalingConfiguration` parameter to configure the minimum
capacity, maximum capacity, and automatic pause when there are no connections. Valid capacity values
include the following:

- Aurora MySQL: `1`, `2`, `4`, `8`, `16`,
  `32`, `64`, `128`, and `256`.
- Aurora PostgreSQL: `2`, `4`, `8`, `16`, `32`,
  `64`, `192`, and `384`.
