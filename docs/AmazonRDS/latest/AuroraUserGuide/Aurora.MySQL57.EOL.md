

# Preparing for Amazon Aurora MySQL-Compatible Edition version 2 end of standard support
<a name="Aurora.MySQL57.EOL"></a>

Amazon Aurora MySQL-Compatible Edition version 2 (with MySQL 5.7 compatibility) is planned to reach the end of standard support on October 31, 2024. We recommend that you upgrade all clusters running Aurora MySQL version 2 to the default Aurora MySQL version 3 (with MySQL 8.0 compatibility) or higher before Aurora MySQL version 2 reaches the end of its standard support period. On October 31, 2024, Amazon RDS will automatically enroll your databases into [Amazon RDS Extended Support](extended-support.md). 

You can find upcoming end-of-support dates for Aurora MySQL major versions in [*Release calendar for Aurora MySQL major versions*](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.release-calendars.html#AuroraMySQL.release-calendars.major).

If you have clusters running Aurora MySQL version 2, you will receive periodic notices with the latest information about how to conduct an upgrade as we get closer to the end of standard support date. We will update this page periodically with the latest information.

## End of standard support timeline
<a name="timeline"></a>

1. Now through October 31, 2024 – You can upgrade clusters from Aurora MySQL version 2 (with MySQL 5.7 compatibility) to Aurora MySQL version 3 (with MySQL 8.0 compatibility).

1. October 31, 2024 – On this date, Aurora MySQL version 2 will reach the end of standard support and Amazon RDS automatically enrolls your clusters into Amazon RDS Extended Support.

We will automatically enroll you in RDS Extended Support. For more information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md).

## Finding clusters affected by this end-of-life process
<a name="find-cluster"></a>

To find clusters affected by this end-of-life process, use the following procedures.

**Important**  
Be sure to perform these instructions in every AWS Region and for each AWS account where your resources are located.

### Console
<a name="aurora-find-mysqlv1-cluster.CON"></a>

**To find an Aurora MySQL version 2 cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1.  In the navigation pane, choose **Databases**.

1.  In the **Filter by databases** box, enter **5.7**.

1. Check for Aurora MySQL in the engine column.

### AWS CLI
<a name="aurora-find-mysqlv1-cluster.CLI"></a>

To find clusters affected by this end-of-life process using the AWS CLI, call the [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) command. You can use the sample script following.

**Example**  

```
aws rds describe-db-clusters --include-share --query 'DBClusters[?(Engine==`aurora-mysql` && contains(EngineVersion,`5.7.mysql_aurora`))].{EngineVersion:EngineVersion, DBClusterIdentifier:DBClusterIdentifier, EngineMode:EngineMode}' --output table --{{region us-east-1}}     
        
        +---------------------------------------------------------------+
        |                      DescribeDBClusters                       |
        +---------------------+---------------+-------------------------+
        |         DBCI        |      EM       |          EV             |
        +---------------------+---------------+-------------------------+
        |    aurora-mysql2    |  provisioned  | 5.7.mysql_aurora.2.11.3 |
        | aurora-serverlessv1 |   serverless  | 5.7.mysql_aurora.2.11.3 |
        +---------------------+---------------+-------------------------+
```

### RDS API
<a name="Aurora-find-mysqlv1-cluster.API"></a>

To find Aurora MySQL DB clusters running Aurora MySQL version 2, use the RDS [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) API operation with the following required parameters: 
+  `DescribeDBClusters`
  + Filters.Filter.N
    + Name
      + engine
    + Values.Value.N
      + ['aurora']

## Amazon RDS Extended Support
<a name="Aurora-RDS-Extended-Support"></a>

You can use Amazon RDS Extended Support over community MySQL 5.7 at no charge until the end of support date, October 31, 2024. On October 31, 2024, Amazon RDS automatically enrolls your databases into RDS Extended Support for Aurora MySQL version 2. RDS Extended Support for Aurora is a paid service that provides up to 28 additional months of support for Aurora MySQL version 2 until the end of RDS Extended Support in February 2027. RDS Extended Support will only be offered for Aurora MySQL minor versions 2.11 and 2.12. To use Amazon Aurora MySQL version 2 past the end of standard support, plan to run your databases on one of these minor versions before October 31, 2024.

For more information about RDS Extended Support, such as charges and other considerations, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md).

## Performing an upgrade
<a name="Aurora-Performing-an-Upgrade"></a>

Upgrading between major versions requires more extensive planning and testing than for a minor version. The process can take substantial time. We want to look at the upgrade as a three-step process, with activities before the upgrade, for the upgrade, and after the upgrade.

**Before the upgrade:**

Before the upgrade, we recommend that you check for application compatibility, performance, maintenance procedures, and similar considerations for the upgraded cluster, thereby confirming that post-upgrade your applications will work as expected. Here are five recommendations that will help provide you a better upgrade experience.
+ First, it's critical to understand [How the Aurora MySQL in-place major version upgrade works](AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Sequence).
+ Next, explore the upgrade techniques that are available when [Upgrading from Aurora MySQL version 2 to version 3](AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Updates.MajorVersionUpgrade.2to3).
+ To help you decide the right time and approach to upgrade, you can learn the differences between Aurora MySQL version 3 and your current environment with [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](AuroraMySQL.Compare-v2-v3.md). 
+ After you've decided on the option that's convenient and works best, try a mock in-place upgrade on a cloned cluster, using [Planning a major version upgrade for an Aurora MySQL cluster](AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Planning).
+ Review the [Major version upgrade prechecks for Aurora MySQL](AuroraMySQL.upgrade-prechecks.md). The upgrade prechecker can run and determine whether your database can be upgraded successfully, and if there are any application incompatibility issues post-upgrade as well as performance, maintenance procedures, and similar considerations.
+ Not all kinds or versions of Aurora MySQL clusters can use the in-place upgrade mechanism. For more information, see [Aurora MySQL major version upgrade paths](AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Compatibility).

If you have any questions or concerns, the AWS Support Team is available on the [community forums](https://repost.aws/) and [Premium Support](https://aws.amazon.com/premiumsupport/).

**Doing the upgrade:**

You can use one of the following upgrade techniques. The amount of downtime your system will experience depends on the technique chosen.
+ **Blue/Green Deployments** – For situations where the top priority is to reduce application downtime, you can use [Amazon RDS Blue/Green Deployments](https://aws.amazon.com/blogs/aws/new-fully-managed-blue-green-deployments-in-amazon-aurora-and-amazon-rds/) for performing the major version upgrade in provisioned Amazon Aurora DB clusters. A blue/green deployment creates a staging environment that copies the production environment. You can make certain changes to the Aurora DB cluster in the green (staging) environment without affecting production workloads. The switchover typically takes under a minute with no data loss. For more information, see [Overview of Amazon Aurora Blue/Green Deployments](blue-green-deployments-overview.md). This minimizes downtime, but requires you to run additional resources while performing the upgrade.
+ **In-place upgrades** – You can perform an [in-place upgrade](AuroraMySQL.Updates.MajorVersionUpgrade.md#AuroraMySQL.Upgrading.Sequence) where Aurora automatically performs a precheck process for you, takes the cluster offline, backs up your cluster, performs the upgrade, and puts your cluster back online. An in-place major version upgrade can be performed in a few clicks, and doesn't involve other coordination or failovers with other clusters, but does involve downtime. For more information, see [How to perform an in-place upgrade](AuroraMySQL.Upgrading.Procedure.md)
+ **Snapshot restore** – You can upgrade your Aurora MySQL version 2 cluster by restoring from an Aurora MySQL version 2 snapshot into an Aurora MySQL version 3 cluster. To do this, you should follow the process for taking a snapshot and [restoring](aurora-restore-snapshot.md) from it. This process involves database interruption because you're restoring from a snapshot.

**After the upgrade:**

After the upgrade, you need to closely monitor your system (application and database) and make fine-tuning changes if necessary. Following the pre-upgrade steps closely will minimize the required changes needed. For more information, see [Troubleshooting Amazon Aurora MySQL database performance](aurora-mysql-troubleshooting.md).

To learn more about the methods, planning, testing, and troubleshooting of Aurora MySQL major version upgrades, be sure to thoroughly read [Upgrading the major version of an Amazon Aurora MySQL DB cluster](AuroraMySQL.Updates.MajorVersionUpgrade.md), including [Troubleshooting for Aurora MySQL in-place upgrade](AuroraMySQL.Upgrading.Troubleshooting.md). Also, note that some instance types aren't supported for Aurora MySQL version 3. For more information, see [Amazon AuroraDB instance classes](Concepts.DBInstanceClass.md).