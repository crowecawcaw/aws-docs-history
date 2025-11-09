# Preparing for Amazon Aurora MySQL-Compatible Edition version 2 end of

standard support

Amazon Aurora MySQL-Compatible Edition version 2 (with MySQL 5.7 compatibility) is planned to reach the end of
standard support on October 31, 2024. We recommend that you upgrade all clusters running
Aurora MySQL version 2 to the default Aurora MySQL version 3 (with MySQL 8.0 compatibility) or
higher before Aurora MySQL version 2 reaches the end of its standard support period. On
October 31, 2024, Amazon RDS will automatically enroll your databases into [Amazon RDS Extended Support](extended-support.md "extended-support.md"). If you're running Amazon Aurora MySQL version
2 (with MySQL 5.7 compatibility) in an Aurora Serverless version 1 cluster, this doesn't apply
to you. If you want to upgrade your Aurora Serverless version 1 clusters to Aurora MySQL version
3, see [Upgrade path for
Aurora Serverless v1 DB clusters](#Aurora-Upgrade-Serverlessv1-Clusters "#Aurora-Upgrade-Serverlessv1-Clusters").

You can find upcoming end-of-support dates for Aurora MySQL major versions in [_Release calendar for
Aurora MySQL major versions_](../AuroraMySQLReleaseNotes/AuroraMySQL.md#AuroraMySQL.release-calendars.major "../AuroraMySQLReleaseNotes/AuroraMySQL.md#AuroraMySQL.release-calendars.major").

If you have clusters running Aurora MySQL version 2, you will receive periodic notices with
the latest information about how to conduct an upgrade as we get closer to the end of
standard support date. We will update this page periodically with the latest
information.

## End of standard support timeline

1. Now through October 31, 2024 – You can upgrade clusters from Aurora MySQL
   version 2 (with MySQL 5.7 compatibility) to Aurora MySQL version 3 (with MySQL 8.0
   compatibility).
2. October 31, 2024 – On this date, Aurora MySQL version 2 will reach the
   end of standard support and Amazon RDS automatically enrolls your clusters into
   Amazon RDS Extended Support.

We will automatically enroll you in RDS Extended Support.
For more
information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

## Finding clusters affected by this end-of-life process

To find clusters affected by this end-of-life process, use the following
procedures.

###### Important

Be sure to perform these instructions in every AWS Region and for each
AWS account where your resources are located.

###### To find an Aurora MySQL version 2 cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. In the **Filter by databases** box, enter
   **5.7**.
4. Check for Aurora MySQL in the engine column.
   To find clusters affected by this end-of-life process using the AWS CLI, call
   the [describe-db-clusters](../../../cli/latest/reference/rds/describe-db-clusters.md "../../../cli/latest/reference/rds/describe-db-clusters.md") command. You can use the sample script
   following.

```
aws rds describe-db-clusters --include-share --query 'DBClusters[?(Engine==`aurora-mysql` && contains(EngineVersion,`5.7.mysql_aurora`))].{EngineVersion:EngineVersion, DBClusterIdentifier:DBClusterIdentifier, EngineMode:EngineMode}' --output table --`region us-east-1`
       `+---------------------------------------------------------------+
 | DescribeDBClusters |
 +---------------------+---------------+-------------------------+
 | DBCI | EM | EV |
 +---------------------+---------------+-------------------------+
 | aurora-mysql2 | provisioned | 5.7.mysql_aurora.2.11.3 |
 | aurora-serverlessv1 | serverless | 5.7.mysql_aurora.2.11.3 |
 +---------------------+---------------+-------------------------+`

```

To find Aurora MySQL DB clusters running Aurora MySQL version 2, use the RDS
[DescribeDBClusters](../APIReference/API_DescribeDBClusters.md "../APIReference/API_DescribeDBClusters.md") API operation with the following required
parameters:

- `DescribeDBClusters`
  - Filters.Filter.N
    - Name
      - engine

    - Values.Value.N
      - ['aurora']

## Amazon RDS Extended Support

You can use Amazon RDS Extended Support over community MySQL 5.7 at no charge until the end of support
date, October 31, 2024. On October 31, 2024, Amazon RDS automatically enrolls your databases
into RDS Extended Support for Aurora MySQL version 2. RDS Extended Support for Aurora is a paid service that
provides up to 28 additional months of support for Aurora MySQL version 2 until the end of
RDS Extended Support in February 2027. RDS Extended Support will only be offered for Aurora MySQL minor
versions 2.11 and 2.12. To use Amazon Aurora MySQL version 2 past the end of standard
support, plan to run your databases on one of these minor versions before October 31, 2024.

For more information about RDS Extended Support, such as charges and other considerations, see
[Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

## Performing an upgrade

Upgrading between major versions requires more extensive planning and testing than for
a minor version. The process can take substantial time. We want to look at the upgrade
as a three-step process, with activities before the upgrade, for the upgrade, and after
the upgrade.

**Before the upgrade:**

Before the upgrade, we recommend that you check for application compatibility,
performance, maintenance procedures, and similar considerations for the upgraded
cluster, thereby confirming that post-upgrade your applications will work as expected.
Here are five recommendations that will help provide you a better upgrade
experience.

- First, it's critical to understand [How the Aurora MySQL in-place major version upgrade works](AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Sequence "AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Sequence").
- Next, explore the upgrade techniques that are available when [Upgrading from Aurora MySQL version 2 to version 3](AuroraMySQL.Updates.md#AuroraMySQL.Updates.MajorVersionUpgrade.2to3 "AuroraMySQL.Updates.md#AuroraMySQL.Updates.MajorVersionUpgrade.2to3").
- To help you decide the right time and approach to upgrade, you can learn the
  differences between Aurora MySQL version 3 and your current environment with [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](AuroraMySQL.md "AuroraMySQL.md").
- After you've decided on the option that's convenient and works best, try a mock in-place upgrade on a cloned cluster, using [Planning a major version upgrade for an Aurora MySQL cluster](AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Planning "AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Planning").
- Review the [Major version upgrade prechecks for Aurora MySQL](AuroraMySQL.md "AuroraMySQL.md"). The upgrade prechecker can run
  and determine whether your database can be upgraded successfully, and if there are any application incompatibility issues post-upgrade as
  well as performance, maintenance procedures, and similar considerations.
- Not all kinds or versions of Aurora MySQL clusters can use the in-place upgrade mechanism. For more information, see
  [Aurora MySQL major version upgrade paths](AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Compatibility "AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Compatibility").

If you have any questions or concerns, the AWS Support Team is available on the
[community forums](https://repost.aws/ "https://repost.aws/") and [Premium Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

**Doing the upgrade:**

You can use one of the following upgrade techniques. The amount of downtime your
system will experience depends on the technique chosen.

- **Blue/Green Deployments** – For
  situations where the top priority is to reduce application downtime, you can use
  [Amazon RDS Blue/Green Deployments](https://aws.amazon.com/blogs/aws/new-fully-managed-blue-green-deployments-in-amazon-aurora-and-amazon-rds/ "https://aws.amazon.com/blogs/aws/new-fully-managed-blue-green-deployments-in-amazon-aurora-and-amazon-rds/") for performing the major version
  upgrade in provisioned Amazon Aurora DB clusters. A blue/green deployment creates a
  staging environment that copies the production environment. You can make certain
  changes to the Aurora DB cluster in the green (staging) environment without
  affecting production workloads. The switchover typically takes under a minute
  with no data loss. For more information, see [Overview of Amazon Aurora Blue/Green Deployments](blue-green-deployments-overview.md "blue-green-deployments-overview.md"). This minimizes downtime,
  but requires you to run additional resources while performing the
  upgrade.
- **In-place upgrades** – You can perform an
  [in-place upgrade](AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Sequence "AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Sequence") where
  Aurora automatically performs a precheck process for you, takes the cluster
  offline, backs up your cluster, performs the upgrade, and puts your cluster back
  online. An in-place major version upgrade can be performed in a few clicks, and
  doesn't involve other coordination or failovers with other clusters, but does
  involve downtime. For more information, see [How to perform an in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md")
- **Snapshot restore** – You can upgrade
  your Aurora MySQL version 2 cluster by restoring from an Aurora MySQL version 2
  snapshot into an Aurora MySQL version 3 cluster. To do this, you should follow the
  process for taking a snapshot and [restoring](aurora-restore-snapshot.md "aurora-restore-snapshot.md") from it. This process involves database interruption
  because you're restoring from a snapshot.

**After the upgrade:**

After the upgrade, you need to closely monitor your system (application and database)
and make fine-tuning changes if necessary. Following the pre-upgrade steps closely will
minimize the required changes needed. For more information, see [Troubleshooting Amazon Aurora MySQL database performance](aurora-mysql-troubleshooting.md "aurora-mysql-troubleshooting.md").

To learn more about the methods, planning, testing, and troubleshooting of Aurora MySQL
major version upgrades, be sure to thoroughly read [Upgrading the major version of an Amazon Aurora MySQL DB cluster](AuroraMySQL.Updates.md "AuroraMySQL.Updates.md"), including [Troubleshooting for Aurora MySQL in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md"). Also, note that some
instance types aren't supported for Aurora MySQL version 3. For more information, see
[Amazon Aurora DB instance classes](Concepts.md "Concepts.md").

## Upgrade path for

Aurora Serverless v1 DB clusters

Upgrading between major versions requires more extensive planning and testing than for
a minor version. The process can take substantial time. We want to look at the upgrade
as a three-step process, with activities before the upgrade, for the upgrade, and after
the upgrade.

Aurora MySQL version 2 (with MySQL 5.7 compatibility) will continue to receive standard
support for Aurora Serverless v1 clusters.

If you want to upgrade to Amazon Aurora MySQL 3 (with MySQL 8.0 compatibility) and
continue running Aurora Serverless, you can use Amazon Aurora Serverless v2. To understand the
differences between Aurora Serverless v1 and Aurora Serverless v2, see [Comparison of Aurora Serverless v2 and Aurora Serverless v1](aurora-serverless-v2.md#aurora-serverless.comparison "aurora-serverless-v2.md#aurora-serverless.comparison").

**Upgrade to Aurora Serverless v2:** You can upgrade an
Aurora Serverless v1 cluster to Aurora Serverless v2. For more information, see [Upgrading from an Aurora Serverless v1 cluster to Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.upgrade-from-serverless-v1-procedure "aurora-serverless-v2.md#aurora-serverless-v2.upgrade-from-serverless-v1-procedure").
