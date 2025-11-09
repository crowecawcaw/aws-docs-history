# Modifying an Aurora Serverless v1 DB cluster

###### Important

AWS has [announced the end-of-life date for Aurora Serverless v1: March 31st, 2025](https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon "https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon"). All Aurora Serverless v1 clusters that are
not migrated by March 31, 2025 will be migrated to Aurora Serverless v2 during the maintenance window. If the upgrade fails, Amazon Aurora converts the Serverless v1
cluster to a provisioned cluster with the equivalent engine version during the maintenance window. If applicable, Amazon Aurora will enroll the
converted provisioned cluster in Amazon RDS Extended Support. For more information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

After you configure an Aurora Serverless v1 DB cluster, you can modify certain properties with the AWS Management Console, the AWS CLI, or the
RDS API. Most of the properties you can modify are the same as for other kinds of Aurora clusters.

The most relevant changes for Aurora Serverless v1 are the following:

- [Modifying the scaling configuration](#aurora-serverless.modifying.scaling "#aurora-serverless.modifying.scaling")
- [Upgrading the major version](#aurora-serverless.modifying.upgrade "#aurora-serverless.modifying.upgrade")
- [Converting from Aurora Serverless v1 to
  provisioned](#aurora-serverless.modifying.convert "#aurora-serverless.modifying.convert")

## Modifying the scaling configuration of an Aurora Serverless v1 DB

cluster

You can set the minimum and maximum capacity for the DB cluster. Each capacity unit is equivalent to a specific compute
and memory configuration. Aurora Serverless automatically creates scaling rules for thresholds for CPU utilization,
connections, and available memory. You can also set whether Aurora Serverless pauses the database when there's no
activity and then resumes when activity begins again.

You can set the following specific values for the scaling configuration:

- **Minimum Aurora capacity unit** – Aurora Serverless can reduce capacity down to this
  capacity unit.
- **Maximum Aurora capacity unit** – Aurora Serverless can increase capacity up to this
  capacity unit.
- **Autoscaling timeout and action** – This section specifies how long Aurora
  Serverless waits to find a scaling point before timing out. It also specifies the action to take when a
  capacity modification times out because it can't find a scaling point. Aurora can force the capacity change to
  set the capacity to the specified value as soon as possible. Or, it can roll back the capacity change to cancel it.
  For more information, see [Timeout action for capacity changes](aurora-serverless-v1.md#aurora-serverless.how-it-works.timeout-action "aurora-serverless-v1.md#aurora-serverless.how-it-works.timeout-action").
- **Pause after inactivity** – Use the optional **Scale the capacity to 0 ACUs when
  cluster is idle** setting to scale the database to zero processing capacity while it's inactive. When
  database traffic resumes, Aurora automatically resumes processing capacity and scales to handle the traffic.

###### Note

When you modify the capacity range for an Aurora Serverless DB cluster, the change takes place immediately,
regardless of whether you choose to apply it immediately or during the next scheduled maintenance window.

You can modify the scaling configuration of an Aurora DB cluster with the AWS Management Console.

###### To modify an Aurora Serverless v1 DB cluster

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the Aurora Serverless v1 DB cluster that you want to modify.
4. For **Actions**, choose **Modify cluster**.
5. In the **Capacity settings** section, modify the scaling configuration.
6. Choose **Continue**.
7. On the **Modify DB cluster** page, review your modifications, then choose when to apply
   them.
8. Choose **Modify cluster**.
   To modify the scaling configuration of an Aurora Serverless v1 DB cluster using the AWS CLI, run the
   [modify-db-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster.html") AWS CLI command.
   Specify the `--scaling-configuration` option to configure the minimum capacity, maximum capacity, and automatic
   pause when there are no connections. Valid capacity values include the following:

- Aurora MySQL: `1`, `2`, `4`, `8`, `16`,
  `32`, `64`, `128`, and `256`.
- Aurora PostgreSQL: `2`, `4`, `8`, `16`, `32`,
  `64`, `192`, and `384`.
  In this example, you modify the scaling configuration of an Aurora Serverless v1 DB cluster named
  `sample-cluster`.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier sample-cluster \
    --scaling-configuration MinCapacity=8,MaxCapacity=64,SecondsUntilAutoPause=500,TimeoutAction='ForceApplyCapacityChange',AutoPause=true

```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier sample-cluster ^
    --scaling-configuration MinCapacity=8,MaxCapacity=64,SecondsUntilAutoPause=500,TimeoutAction='ForceApplyCapacityChange',AutoPause=true

```

You can modify the scaling configuration of an Aurora DB cluster with the [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md") API operation. Specify the
`ScalingConfiguration` parameter to configure the minimum capacity, maximum capacity, and automatic
pause when there are no connections. Valid capacity values include the following:

- Aurora MySQL: `1`, `2`, `4`, `8`, `16`,
  `32`, `64`, `128`, and `256`.
- Aurora PostgreSQL: `2`, `4`, `8`, `16`, `32`,
  `64`, `192`, and `384`.

## Upgrading the major version of an Aurora Serverless v1 DB

cluster

###### Important

AWS has [announced the end-of-life date for Aurora Serverless v1: March 31st, 2025](https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon "https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon"). All Aurora Serverless v1 clusters that are
not migrated by March 31, 2025 will be migrated to Aurora Serverless v2 during the maintenance window. If the upgrade fails, Amazon Aurora converts the Serverless v1
cluster to a provisioned cluster with the equivalent engine version during the maintenance window. If applicable, Amazon Aurora will enroll the
converted provisioned cluster in Amazon RDS Extended Support. For more information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

You can upgrade the major version for an Aurora Serverless v1 DB cluster compatible with PostgreSQL 11 to a corresponding
PostgreSQL 13–compatible version.

You can perform an in-place upgrade of an Aurora Serverless v1 DB cluster using the AWS Management Console.

###### To upgrade an Aurora Serverless v1 DB cluster

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the Aurora Serverless v1 DB cluster that you want to upgrade.
4. For **Actions**, choose **Modify cluster**.
5. For **Version**, choose an Aurora PostgreSQL version 13 version number.

The following example shows an in-place upgrade from Aurora PostgreSQL 11.16 to 13.9.

![Upgrading an Aurora Serverless v1 DB cluster using the console](images/sv1-upgrade-apg11-to-13.png)

If you perform a major version upgrade, leave all of the other properties the same. To change any other
properties, do another **Modify** operation after the upgrade finishes. 6. Choose **Continue**. 7. On the **Modify DB cluster** page, review your modifications, then choose when to apply
them. 8. Choose **Modify cluster**.
To perform an in-place upgrade from a PostgreSQL 11–compatible Aurora Serverless v1 DB cluster
to a PostgreSQL 13–compatible one, specify the `--engine-version` parameter with an Aurora PostgreSQL
version 13 version number that's compatible with Aurora Serverless v1. Also include the
`--allow-major-version-upgrade` parameter.

In this example, you modify the major version of a PostgreSQL 11–compatible
Aurora Serverless v1 DB cluster named `sample-cluster`. Doing so performs an in-place upgrade to a
PostgreSQL 13–compatible Aurora Serverless v1 DB cluster.

```
aws rds modify-db-cluster \
    --db-cluster-identifier sample-cluster \
    --engine-version 13.serverless_12 \
    --allow-major-version-upgrade

```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier sample-cluster ^
    --engine-version 13.serverless_12 ^
    --allow-major-version-upgrade

```

To perform an in-place upgrade from a PostgreSQL 11–compatible Aurora Serverless v1 DB cluster
to a PostgreSQL 13–compatible one, specify the `EngineVersion` parameter with an Aurora PostgreSQL
version 13 version number that's compatible with Aurora Serverless v1. Also include the
`AllowMajorVersionUpgrade` parameter.

## Converting an Aurora Serverless v1 DB cluster to provisioned

You can convert an Aurora Serverless v1 DB cluster to a provisioned DB cluster. To perform the conversion, use the AWS CLI or Amazon RDS API to change the DB instance class to **Provisioned**. Use the steps below to modify your DB instance class.

The following example demonstrates how to use the AWS CLI to convert an Aurora Serverless v1 DB cluster to a provisioned cluster.

To convert an Aurora Serverless v1 DB cluster to a provisioned cluster, run the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") AWS CLI command.

The following parameters are required:

- `--db-cluster-identifier` – The Aurora Serverless v1 DB cluster that you're converting to
  provisioned.
- `--engine-mode` – Use the value `provisioned`.
- `--allow-engine-mode-change`
- `--db-cluster-instance-class` – Choose the DB instance class for the provisioned DB
  cluster based on the capacity of the Aurora Serverless v1 DB cluster.
  In this example, you convert an Aurora Serverless v1 DB cluster named `sample-cluster` and use the
  `db.r5.xlarge` DB instance class.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
--db-cluster-identifier `sample-cluster` \
--engine-mode provisioned \
--allow-engine-mode-change \
--db-cluster-instance-class `db.r5.xlarge`
```

For Windows:

```
aws rds modify-db-cluster ^
--db-cluster-identifier `sample-cluster` ^
--engine-mode provisioned ^
--allow-engine-mode-change ^
--db-cluster-instance-class `db.r5.xlarge`
```

The following example demonstrates how to use the Amazon RDS API to convert an Aurora Serverless v1 DB cluster to a provisioned cluster.

To convert an Aurora Serverless v1 DB cluster to a provisioned cluster, use the [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md") API operation.

The following parameters are required:

- `DBClusterIdentifier` – The Aurora Serverless v1 DB cluster that you're converting to
  provisioned.
- `EngineMode` – Use the value `provisioned`.
- `AllowEngineModeChange`
- `DBClusterInstanceClass` – Choose the DB instance class for the provisioned DB cluster
  based on the capacity of the Aurora Serverless v1 DB cluster.

## Considerations when converting from an Aurora Serverless v1 DB cluster to a provisioned cluster

The following considerations apply when an Aurora Serverless v1 DB cluster is converted to a provisioned cluster:

- You can use this conversion as part of upgrading your DB cluster from
  Aurora Serverless v1 to Aurora Serverless v2. For more information, see [Upgrading from an Aurora Serverless v1 cluster to Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.upgrade-from-serverless-v1-procedure "aurora-serverless-v2.md#aurora-serverless-v2.upgrade-from-serverless-v1-procedure").
- The conversion process creates a reader DB instance in the DB cluster, promotes the reader instance to a writer instance,
  and then deletes the original Aurora Serverless v1 instance. When you convert the DB cluster, you can't perform any other
  modifications at the same time, such as changing the DB engine version or DB cluster parameter group. The conversion
  operation is applied immediately, and can't be undone.
- During the conversion, a backup DB cluster snapshot is taken of the DB cluster in case an error occurs. The identifier for
  the DB cluster snapshot has the form `pre-modify-engine-mode-`DB_cluster_identifier`-`timestamp``.
- Aurora uses the current default DB minor engine version for the provisioned DB cluster.
- If you don't provide a DB instance class for your converted DB cluster, Aurora recommends one based on the maximum capacity
  of the original Aurora Serverless v1 DB cluster. The recommended capacity to instance class mappings are shown in the
  following table.

| Serverless maximum capacity (ACUs) | Provisioned DB instance class |
| ---------------------------------- | ----------------------------- |
| 1                                  | db.t3.small                   |
| 2                                  | db.t3.medium                  |
| 4                                  | db.t3.large                   |
| 8                                  | db.r5.large                   |
| 16                                 | db.r5.xlarge                  |
| 32                                 | db.r5.2xlarge                 |
| 64                                 | db.r5.4xlarge                 |
| 128                                | db.r5.8xlarge                 |
| 192                                | db.r5.12xlarge                |
| 256                                | db.r5.16xlarge                |
| 384                                | db.r5.24xlarge                |

###### Note

Depending on the DB instance class you choose, and your database usage, you might see different costs for a
provisioned DB cluster compared to Aurora Serverless v1.

If you convert your Aurora Serverless v1 DB cluster to a burstable (db.t\*) DB instance class, you might incur additional
costs for using the DB cluster. For more information, see [DB instance class types](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").
