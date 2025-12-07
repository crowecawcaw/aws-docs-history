# Restoring an Aurora Serverless v1 DB cluster

###### Important

AWS has [announced the end-of-life date for Aurora Serverless v1: March 31st, 2025](https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon "https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon"). All Aurora Serverless v1 clusters that are
not migrated by March 31, 2025 will be migrated to Aurora Serverless v2 during the maintenance window. If the upgrade fails, Amazon Aurora converts the Serverless v1
cluster to a provisioned cluster with the equivalent engine version during the maintenance window. If applicable, Amazon Aurora will enroll the
converted provisioned cluster in Amazon RDS Extended Support. For more information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

You can configure an Aurora Serverless v1 DB cluster when you restore a provisioned DB cluster snapshot with the
the AWS CLI or the RDS API.

When you restore a snapshot to an Aurora Serverless v1 DB cluster, you can set the following specific values:

- **Minimum Aurora capacity unit** – Aurora Serverless v1 can reduce capacity down to
  this capacity unit.
- **Maximum Aurora capacity unit** – Aurora Serverless v1 can increase capacity up to
  this capacity unit.
- **Timeout action** – The action to take when a capacity modification times out
  because it can't find a scaling point. Aurora Serverless v1 DB cluster can force your DB cluster to the
  new capacity settings if set the **Force scaling the capacity to the specified values...** option. Or, it can roll back the capacity change to cancel it if you don't choose the
  option. For more information, see
  [Timeout action for capacity changes](aurora-serverless-v1.md#aurora-serverless.how-it-works.timeout-action "aurora-serverless-v1.md#aurora-serverless.how-it-works.timeout-action").
- **Pause after inactivity** – The amount of time with no database traffic to scale
  to zero processing capacity. When database traffic resumes, Aurora automatically resumes processing
  capacity and scales to handle the traffic.

For general information about restoring a DB cluster from a snapshot, see
[Restoring from a DB cluster snapshot](aurora-restore-snapshot.md "aurora-restore-snapshot.md").

You can configure an Aurora Serverless DB cluster when you restore a provisioned DB
cluster snapshot with the AWS Management Console, the AWS CLI, or the RDS API.

When you restore a snapshot to an Aurora Serverless DB cluster, you can set the following specific values:

- **Minimum Aurora capacity unit** – Aurora Serverless can reduce
  capacity down to this capacity unit.
- **Maximum Aurora capacity unit** – Aurora Serverless can increase
  capacity up to this capacity unit.
- **Timeout action** – The action to take when a
  capacity modification times out because it can't find a scaling point.
  Aurora Serverless v1 DB cluster can force your DB cluster to the new capacity settings if set the
  **Force scaling the capacity to the specified values...** option.
  Or, it can roll back the capacity change to cancel it if you don't choose the option. For
  more information, see [Timeout action for capacity changes](aurora-serverless-v1.md#aurora-serverless.how-it-works.timeout-action "aurora-serverless-v1.md#aurora-serverless.how-it-works.timeout-action").
- **Pause after inactivity** – The amount of time with
  no database traffic to scale to zero processing capacity. When database traffic
  resumes, Aurora automatically resumes processing capacity and scales to handle
  the traffic.

###### Note

The version of the DB cluster snapshot must be compatible with Aurora Serverless v1. For the list of supported versions, see
[Aurora Serverless v1](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

To restore a snapshot to an Aurora Serverless v1 cluster with MySQL 5.7 compatibility, include the following
additional parameters:

- `--engine **aurora-mysql**`
- `--engine-version **5.7**`

The `--engine` and `--engine-version` parameters let you create a MySQL
5.7-compatible Aurora Serverless v1 cluster from a MySQL 5.6-compatible Aurora or Aurora Serverless v1
snapshot. The following example restores a snapshot from a MySQL 5.6-compatible cluster named
`mydbclustersnapshot` to a MySQL 5.7-compatible Aurora Serverless v1 cluster named
`mynewdbcluster`.

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-from-snapshot \
    --db-cluster-identifier `mynewdbcluster` \
    --snapshot-identifier `mydbclustersnapshot` \
    --engine-mode serverless \
    --engine aurora-mysql \
    --engine-version 5.7
```

For Windows:

```
aws rds restore-db-cluster-from-snapshot ^
    --db-instance-identifier `mynewdbcluster` ^
    --db-snapshot-identifier `mydbclustersnapshot` ^
    --engine aurora-mysql ^
    --engine-version 5.7
```

You can optionally specify the `--scaling-configuration` option to configure the minimum
capacity, maximum capacity, and automatic pause when there are no connections. Valid capacity values
include the following:

- Aurora MySQL: `1`, `2`, `4`, `8`, `16`,
  `32`, `64`, `128`, and `256`.
- Aurora PostgreSQL: `2`, `4`, `8`, `16`, `32`,
  `64`, `192`, and `384`.

In the following example, you restore from a previously created DB cluster snapshot named
`mydbclustersnapshot` to a new DB cluster named
`mynewdbcluster`. You set the `--scaling-configuration` so that the
new Aurora Serverless v1 DB cluster can scale from 8 ACUs to 64 ACUs (Aurora capacity units) as needed to
process the workload. After processing completes and after 1000 seconds with no connections to support,
the cluster shuts down until connection requests prompt it to restart.

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-from-snapshot \
    --db-cluster-identifier `mynewdbcluster` \
    --snapshot-identifier `mydbclustersnapshot` \
    --engine-mode serverless --scaling-configuration MinCapacity=8,MaxCapacity=64,TimeoutAction='ForceApplyCapacityChange',SecondsUntilAutoPause=1000,AutoPause=true
```

For Windows:

```
aws rds restore-db-cluster-from-snapshot ^
    --db-instance-identifier `mynewdbcluster` ^
    --db-snapshot-identifier `mydbclustersnapshot` ^
    --engine-mode serverless --scaling-configuration MinCapacity=8,MaxCapacity=64,TimeoutAction='ForceApplyCapacityChange',SecondsUntilAutoPause=1000,AutoPause=true
```

To configure an Aurora Serverless v1 DB cluster when you restore from a DB cluster using the RDS API, run
the [RestoreDBClusterFromSnapshot](../APIReference/API_RestoreDBClusterFromSnapshot.md "../APIReference/API_RestoreDBClusterFromSnapshot.md")
operation and specify `serverless` for the `EngineMode` parameter.

You can optionally specify the `ScalingConfiguration` parameter to configure the minimum
capacity, maximum capacity, and automatic pause when there are no connections. Valid capacity values
include the following:

- Aurora MySQL: `1`, `2`, `4`, `8`, `16`,
  `32`, `64`, `128`, and `256`.
- Aurora PostgreSQL: `2`, `4`, `8`, `16`, `32`,
  `64`, `192`, and `384`.
