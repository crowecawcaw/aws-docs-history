# Performing a minor

version upgrade

You can use the following methods to upgrade the minor version of a DB cluster or to patch
a DB cluster:

###### Topics

- [Before performing a
  minor version upgrade](#USER_UpgradeDBInstance.PostgreSQL.BeforeMinor "#USER_UpgradeDBInstance.PostgreSQL.BeforeMinor")
- [How to perform minor
  version upgrades and apply patches](#USER_UpgradeDBInstance.PostgreSQL.Minor "#USER_UpgradeDBInstance.PostgreSQL.Minor")
- [Minor release upgrades
  and zero-downtime patching](#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp "#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp")
- [Limitations of zero-downtime patching](#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp.limitations "#USER_UpgradeDBInstance.PostgreSQL.Minor.zdp.limitations")
- [Upgrading the Aurora PostgreSQL
  engine to a new minor version](#USER_UpgradeDBInstance.MinorUpgrade "#USER_UpgradeDBInstance.MinorUpgrade")

## Before performing a

minor version upgrade

We recommend that you perform the following actions to reduce the downtime during
a minor version upgrade:

- The Aurora DB cluster maintenance should be performed during a period of low
  traffic. Use Performance Insights to identify these time periods in order to
  configure the maintenance windows correctly. For more information on
  Performance Insights, see [Monitoring DB
  load with Performance Insights on Amazon RDS](../UserGuide/USER_PerfInsights.md "../UserGuide/USER_PerfInsights.md"). For more information on
  DB cluster maintenance window, [Adjusting the preferred DB cluster
  maintenance window](USER_UpgradeDBInstance.md#AdjustingTheMaintenanceWindow.Aurora "USER_UpgradeDBInstance.md#AdjustingTheMaintenanceWindow.Aurora").
- Use AWS SDKs that support exponential backoff and jitter as a best
  practice. For more information, see [Exponential Backoff And Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ "https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/").

## How to perform minor

version upgrades and apply patches

Minor version upgrades and patches become available in AWS Regions only after
rigorous testing. Before releasing upgrades and patches, Aurora PostgreSQL tests to
ensure that known security issues, bugs, and other issues that emerge after the
release of the minor community version don't disrupt Aurora PostgreSQL fleet
stability.

If you turn on **Enable auto minor version upgrade**,
Aurora PostgreSQL periodically upgrades your DB cluster during your specified maintenance
window. Make sure that the **Enable auto minor version upgrade**
option is turned on for all instances in your Aurora PostgreSQL DB cluster. For information
on how to set **Auto minor version upgrade**, and how the setting
works when applied at the cluster and instance levels, see [Automatic minor version upgrades for Aurora
DB clusters](USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU "USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU").

Check the value of the **Enable auto minor version upgrade**
option for all your Aurora PostgreSQL DB clusters by using the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md")
AWS CLI command as follows.

```
aws rds describe-db-instances \
  --query '*[].{DBClusterIdentifier:DBClusterIdentifier,DBInstanceIdentifier:DBInstanceIdentifier,AutoMinorVersionUpgrade:AutoMinorVersionUpgrade}'
```

This query returns a list of all Aurora DB clusters and their instances with a
`true` or `false` value for the status of the
`AutoMinorVersionUpgrade` setting. The command assumes that you have
your AWS CLI configured to target your default AWS Region.

For more information about the AmVU option and how to modify your Aurora DB cluster to
use it, see [Automatic minor version upgrades for Aurora
DB clusters](USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU "USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU").

You can upgrade your Aurora PostgreSQL DB clusters to new minor versions either by
responding to maintenance tasks, or by modifying the cluster to use the new version.

You can identify any available upgrades or patches for your Aurora PostgreSQL DB
clusters by using the RDS console and opening the
**Recommendations** menu. There, you can find a list of various
maintenance issues such as **Old minor versions**. Depending on
your production environment, you can choose to **Schedule** the
upgrade or take immediate action, by choosing **Apply now**, as
shown following.

![Console image showing Recommendation to upgrade to a newer minor version.](images/apg-maintenance-upgrade-minor.png)

To learn more about how to maintain an Aurora DB cluster, including how to manually
apply patches and minor version upgrades, see [Maintaining an Amazon Aurora DB cluster](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

## Minor release upgrades

and zero-downtime patching

Upgrading an Aurora PostgreSQL DB cluster involves the possibility of an outage. During the
upgrade process, the database is shut down as it's being upgraded. If you start
the upgrade while the database is busy, you lose all connections and transactions
that the DB cluster is processing. If you wait until the database is idle to perform the
upgrade, you might have to wait a long time.

The zero-downtime patching (ZDP) feature improves the upgrading process. With ZDP,
both minor version upgrades and patches can be applied with minimal impact to your
Aurora PostgreSQL DB cluster. ZDP is used when applying patches or newer minor version
upgrades to Aurora PostgreSQL versions and other higher releases of these minor versions
and newer major versions. That is, upgrading to new minor versions from any of these
releases onward uses ZDP.

The following table shows the Aurora PostgreSQL versions and DB instance classes where
ZDP is available:

| Version                   | db.r\<br>• instance classes | db.t\<br>• instance classes | db.x\<br>• instance classes | db.serverless instance class |
| ------------------------- | --------------------------- | --------------------------- | --------------------------- | ---------------------------- |
| 10.21 and higher versions | Yes                         | Yes                         | Yes                         | N/A                          |
| 11.16 and higher versions | Yes                         | Yes                         | Yes                         | N/A                          |
| 11.17 and higher versions | Yes                         | Yes                         | Yes                         | N/A                          |
| 12.11 and higher versions | Yes                         | Yes                         | Yes                         | N/A                          |
| 12.12 and higher versions | Yes                         | Yes                         | Yes                         | N/A                          |
| 13.7 and higher versions  | Yes                         | Yes                         | Yes                         | N/A                          |
| 13.8 and higher versions  | Yes                         | Yes                         | Yes                         | Yes                          |
| 14.3 and higher versions  | Yes                         | Yes                         | Yes                         | N/A                          |
| 14.4 and higher versions  | Yes                         | Yes                         | Yes                         | N/A                          |
| 14.5 and higher versions  | Yes                         | Yes                         | Yes                         | Yes                          |
| 15.3 and higher versions  | Yes                         | Yes                         | Yes                         | Yes                          |
| 16.1 and higher versions  | Yes                         | Yes                         | Yes                         | Yes                          |

During the upgrade process using ZDP, the database engine looks for a quiet point
to pause all new transactions. This action safeguards the database during patches
and upgrades. To make sure that your applications run smoothly with paused
transactions, we recommend integrating retry logic into your code. This approach
ensures that the system can manage any brief downtime without failing and can retry
the new transactions after the upgrade.

When ZDP completes successfully, application sessions are maintained except for
those with dropped connections, and the database engine restarts while the upgrade
is still in progress. Although the database engine restart can cause a temporary
drop in throughput, this typically lasts only for a few seconds or at most,
approximately one minute.

In some cases, zero-downtime patching (ZDP) might not succeed. For example,
parameter changes that are in a `pending` state on your Aurora PostgreSQL DB
cluster or its instances interfere with ZDP.

You can find metrics and events for ZDP operations in **Events**
page in the console. The events include the start of the ZDP upgrade and completion
of the upgrade. In this event you can find how long the process took, and the
numbers of preserved and dropped connections that occurred during the restart. You
can find details in your database error log.

## Limitations of zero-downtime patching

The following limitations apply to zero-downtime patching:

- ZDP tries to preserve current client connections to your Aurora PostgreSQL
  writer instance throughout the Aurora PostgreSQL upgrade process. However, in
  the following cases, connections will be dropped for ZDP to complete:
  - Long running query or transactions are in progress.
  - Data definition language (DDL) statements are running.
  - Temporary tables or table locks are in use.
  - All sessions are listening on notification channels.
  - A cursor in ‘WITH HOLD’ status is in use.
  - TLSv1.1 connections are in use. Starting with Aurora PostgreSQL
    versions later than 16.1, 15.3, 14.8, 13.11, 12.15, and 11.20, ZDP
    is supported with TLSv1.3 connections.

- ZDP isn't supported in the following cases:
  - When Aurora PostgreSQL DB clusters are configured as
    Aurora Serverless v1.
  - During the upgrade of any Aurora reader instances.
  - During the upgrade of any Aurora reader instances that are part of
    an Aurora Global Database cluster in a secondary Region.
  - During OS patches and OS upgrades.

## Upgrading the Aurora PostgreSQL

engine to a new minor version

You can upgrade your Aurora PostgreSQL DB cluster to a new minor version by using the
console, the AWS CLI, or the RDS API. Before performing the upgrade, we recommend that
you follow the same best practice that we recommend for major version upgrades. As
with new major versions, new minor versions can also have optimizer improvements,
such as fixes, that can cause query plan regressions. To ensure plan stability, we
recommend that you use the Query Plan Management (QPM) extension as detailed in
[Ensuring plan stability after a major version upgrade](AuroraPostgreSQL.Optimize.md#AuroraPostgreSQL.Optimize.BestPractice.MajorVersionUpgrade "AuroraPostgreSQL.Optimize.md#AuroraPostgreSQL.Optimize.BestPractice.MajorVersionUpgrade").

###### To upgrade the engine version of your Aurora PostgreSQL DB

cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and
   then choose the DB cluster that you want to upgrade.
3. Choose **Modify**. The **Modify DB
   cluster** page appears.
4. For **Engine version**, choose the new
   version.
5. Choose **Continue** and check the summary of
   modifications.
6. To apply the changes immediately, choose **Apply
   immediately**. Choosing this option can cause an outage
   in some cases. For more information, see [Modifying an Amazon Aurora DB cluster](Aurora.md "Aurora.md").
7. On the confirmation page, review your changes. If they are
   correct, choose **Modify Cluster** to save your
   changes.

Or choose **Back** to edit your changes or
**Cancel** to cancel your changes.
To upgrade the engine version of a DB cluster, use the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md")
AWS CLI command with the following parameters:

- `--db-cluster-identifier` – The name of your
  Aurora PostgreSQL DB cluster.
- `--engine-version` – The version number of the
  database engine to upgrade to. For information about valid engine
  versions, use the AWS CLI [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") command.
- `--no-apply-immediately` – Apply changes during
  the next maintenance window. To apply changes immediately, use
  `--apply-immediately` instead.
  For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier `mydbcluster` \
    --engine-version `new_version` \
    --no-apply-immediately
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier `mydbcluster` ^
    --engine-version `new_version` ^
    --no-apply-immediately
```

To upgrade the engine version of a DB cluster, use the [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md")
operation. Specify the following parameters:

- `DBClusterIdentifier` – The name of the DB
  cluster, for example
  `mydbcluster`.
- `EngineVersion` – The version number of the
  database engine to upgrade to. For information about valid engine
  versions, use the [DescribeDBEngineVersions](../APIReference/API_DescribeDBEngineVersions.md "../APIReference/API_DescribeDBEngineVersions.md") operation.
- `ApplyImmediately` – Whether to apply changes
  immediately or during the next maintenance window. To apply changes
  immediately, set the value to `true`. To apply changes
  during the next maintenance window, set the value to
  `false`.
