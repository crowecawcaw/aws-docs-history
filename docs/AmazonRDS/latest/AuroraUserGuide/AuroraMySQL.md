# Upgrading the major version of an Amazon Aurora MySQL DB cluster

In an Aurora MySQL version number such as 3.04.1, the 3 represents the major version. Aurora MySQL version 2 is compatible with MySQL 5.7. Aurora MySQL
version 3 is compatible with MySQL 8.0.

Upgrading between major versions requires more extensive planning and testing than for a minor version. The process can take substantial time. After the
upgrade is finished, you also might have followup work to do. For example, this might occur because of differences in SQL compatibility or the way certain
MySQL-related features work. Or it might occur because of differing parameter settings between the old and new versions.

###### Contents

- [Upgrading from Aurora MySQL version 2 to version 3](AuroraMySQL.Updates.md#AuroraMySQL.Updates.MajorVersionUpgrade.2to3 "AuroraMySQL.Updates.md#AuroraMySQL.Updates.MajorVersionUpgrade.2to3")
- [Aurora MySQL major version upgrade paths](AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Compatibility "AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Compatibility")
- [How the Aurora MySQL in-place major version upgrade works](AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Sequence "AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Sequence")
- [Planning a major version upgrade for an Aurora MySQL cluster](AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Planning "AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Planning")
  - [Simulating the upgrade by cloning
    your DB cluster](AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Planning.clone "AuroraMySQL.Updates.md#AuroraMySQL.Upgrading.Planning.clone")
  - [Blue/Green Deployments](AuroraMySQL.Updates.md#AuroraMySQL.UpgradingMajor.BlueGreen "AuroraMySQL.Updates.md#AuroraMySQL.UpgradingMajor.BlueGreen")

- [Major version upgrade prechecks for Aurora MySQL](AuroraMySQL.md "AuroraMySQL.md")
  - [Precheck process for Aurora MySQL](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.process "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.process")
  - [Precheck log format for Aurora MySQL](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.log-format "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.log-format")
  - [Precheck log output examples for Aurora MySQL](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.log-examples "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.log-examples")
  - [Precheck performance for Aurora MySQL](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.performance "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.performance")
  - [Summary of Community MySQL upgrade prechecks](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.community "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.community")
  - [Summary of Aurora MySQL upgrade prechecks](AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.ams "AuroraMySQL.md#AuroraMySQL.upgrade-prechecks.ams")
  - [Precheck descriptions reference for Aurora MySQL](AuroraMySQL.upgrade-prechecks.md "AuroraMySQL.upgrade-prechecks.md")
    - [Errors](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors")
      - [MySQL prechecks that report errors](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.mysql "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.mysql")
      - [Aurora MySQL prechecks that report errors](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.aurora "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-errors.aurora")

    - [Warnings](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings")
      - [MySQL prechecks that report warnings](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.mysql "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.mysql")
      - [Aurora MySQL prechecks that report warnings](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.aurora "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-warnings.aurora")

    - [Notices](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-notices "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-notices")
    - [Errors, warnings, or notices](AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-all "AuroraMySQL.upgrade-prechecks.md#precheck-descriptions-all")

- [How to perform an in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md")
  - [How in-place upgrades affect the parameter groups for a cluster](AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.ParamGroups "AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.ParamGroups")
  - [Changes to cluster properties between Aurora MySQL versions](AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.Attrs "AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.Attrs")
  - [In-place major upgrades for global databases](AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.GlobalDB "AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.GlobalDB")
  - [In-place upgrades for DB clusters with cross-Region read replicas](AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.XRRR "AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.XRRR")

- [Aurora MySQL in-place upgrade tutorial](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md")
- [Finding the reasons for Aurora MySQL major version upgrade failures](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md")
- [Troubleshooting for Aurora MySQL in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md")
- [Post-upgrade cleanup for Aurora MySQL version 3](AuroraMySQL.md "AuroraMySQL.md")
  - [Spatial indexes](AuroraMySQL.md#AuroraMySQL.mysql80-spatial "AuroraMySQL.md#AuroraMySQL.mysql80-spatial")

## Upgrading from Aurora MySQL version 2 to version 3

If you have a MySQL 5.7–compatible cluster and want to upgrade it to a
MySQL–8.0 compatible cluster, you can do so by running an upgrade process on the
cluster itself. This kind of upgrade is an _in-place upgrade_, in contrast
to upgrades that you do by creating a new cluster. This technique keeps the same endpoint and
other characteristics of the cluster. The upgrade is relatively fast because it doesn't
require copying all your data to a new cluster volume. This stability helps to minimize any
configuration changes in your applications. It also helps to reduce the amount of testing for
the upgraded cluster. This is because the number of DB instances and their instance classes
all stay the same.

The in-place upgrade mechanism involves shutting down your DB cluster while the operation takes place. Aurora performs a clean
shutdown and completes outstanding operations such as transaction rollback and undo purge. For more information, see
[How the Aurora MySQL in-place major version upgrade works](#AuroraMySQL.Upgrading.Sequence "#AuroraMySQL.Upgrading.Sequence").

The in-place upgrade method is convenient, because it is simple to perform and minimizes
configuration changes to associated applications. For example, an in-place upgrade preserves
the endpoints and set of DB instances for your cluster. However, the time needed for an
in-place upgrade can vary depending on the properties of your schema and how busy the cluster
is. Thus, depending on the needs for your cluster, you can choose among the upgrade
techniques:

- [In-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md")
- [Blue/Green
  Deployment](#AuroraMySQL.UpgradingMajor.BlueGreen "#AuroraMySQL.UpgradingMajor.BlueGreen")
- [Snapshot restore](aurora-restore-snapshot.md "aurora-restore-snapshot.md")

###### Note

If you use the AWS CLI or RDS API for the snapshot restore upgrade method, you must
run a subsequent operation to create a writer DB instance in the restored DB
cluster.

For general information about Aurora MySQL version 3 and its new features, see [Aurora MySQL version 3 compatible with MySQL 8.0](AuroraMySQL.md "AuroraMySQL.md").

For details about planning an upgrade, see [Planning a major version upgrade for an Aurora MySQL cluster](#AuroraMySQL.Upgrading.Planning "#AuroraMySQL.Upgrading.Planning") and [How to perform an in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md").

## Aurora MySQL major version upgrade paths

Not all kinds or versions of Aurora MySQL clusters can use the in-place upgrade mechanism. You can learn the appropriate upgrade path for each
Aurora MySQL cluster by consulting the following table.

| Type of Aurora MySQL DB cluster                      | Can it use in-place upgrade? | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Aurora MySQL provisioned cluster, version 2          | Yes                          | In-place upgrade is supported for MySQL 5.7–compatible Aurora MySQL clusters.<br>For information about upgrading to Aurora MySQL version 3, see [Planning a major version upgrade for an Aurora MySQL cluster](#AuroraMySQL.Upgrading.Planning "#AuroraMySQL.Upgrading.Planning") and [How to perform an in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Aurora MySQL provisioned cluster, version 3          | Not applicable               | Use a minor version upgrade procedure to upgrade between Aurora MySQL version 3 versions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Aurora Serverless v1 cluster                         | Not applicable               | Aurora Serverless v1 is supported for Aurora MySQL only on version 2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Aurora Serverless v2 cluster                         | Not applicable               | Aurora Serverless v2 is supported for Aurora MySQL only on version 3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Cluster in an Aurora global database                 | Yes                          | To upgrade Aurora MySQL from version 2 to version 3, follow the [procedure for doing an<br>in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md") for clusters in an Aurora global database. Perform the upgrade on the global cluster. Aurora upgrades the primary<br>cluster and all the secondary clusters in the global database at the same time.<br>If you use the AWS CLI or RDS API, call the `modify-global-cluster` command or `ModifyGlobalCluster` operation instead<br>of `modify-db-cluster` or `ModifyDBCluster`.<br>You can perform an in-place upgrade from Aurora MySQL version 2 to version 3 only if the `lower_case_table_names` parameter is<br>set to default and you reboot your global database. For more information, see [Major version upgrades](aurora-global-database-upgrade.md#aurora-global-database-upgrade.major "aurora-global-database-upgrade.md#aurora-global-database-upgrade.major"). |
| Parallel query cluster                               | Yes                          | You can perform an in-place upgrade.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Cluster that is the target of binary log replication | Maybe                        | If the binary log replication is from an Aurora MySQL cluster, you can perform an in-place upgrade. You can't perform the upgrade if the<br>binary log replication is from an RDS for MySQL or an on-premises MySQL DB instance. In that case, you can upgrade using the snapshot restore<br>mechanism.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Cluster with zero DB instances                       | No                           | Using the AWS CLI or the RDS API, you can create an Aurora MySQL cluster without any attached DB instances. In the same way, you can also remove<br>all DB instances from an Aurora MySQL cluster while leaving the data in the cluster volume intact. While a cluster has zero DB instances, you<br>can't perform an in-place upgrade.<br>The upgrade mechanism requires a writer instance in the cluster to perform conversions on the system tables, data files, and so on. In this<br>case, use the AWS CLI or the RDS API to create a writer instance for the cluster. Then you can perform an in-place upgrade.                                                                                                                                                                                                                                                                                                                          |
| Cluster with backtrack enabled                       | Yes                          | You can perform an in-place upgrade for an Aurora MySQL cluster that uses the Backtrack feature. However, after the upgrade, you can't<br>backtrack the cluster to a time before the upgrade.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## How the Aurora MySQL in-place major version upgrade works

Aurora MySQL performs a major version upgrade as a multistage process. You can check the current status of an upgrade. Some of the upgrade steps also
provide progress information. As each stage begins, Aurora MySQL records an event. You can examine events as they occur on the **Events**
page in the RDS console. For more information about working with events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").

###### Important

Once the process begins, it runs until the upgrade either succeeds or fails. You can't cancel the upgrade while it's underway. If the
upgrade fails, Aurora rolls back all the changes and your cluster has the same engine version, metadata, and so on as before.

The upgrade process consists of these stages:

1. Aurora performs a series of [prechecks](AuroraMySQL.md "AuroraMySQL.md") before beginning the upgrade process. Your cluster
   keeps running while Aurora does these checks. For example, the cluster can't have any XA transactions in the prepared state or be processing any
   data definition language (DDL) statements. For example, you might need to shut down applications that are submitting certain kinds of SQL statements.
   Or you might simply wait until certain long-running statements are finished. Then try the upgrade again. Some checks test for conditions that
   don't prevent the upgrade but might make the upgrade take a long time.

If Aurora detects that any required conditions aren't met, modify the conditions identified in the event details. Follow the guidance in
[Troubleshooting for Aurora MySQL in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md"). If Aurora detects conditions that
might cause a slow upgrade, plan to monitor the upgrade over an extended period. 2. Aurora takes your cluster offline. Then Aurora performs a similar set of tests as in the previous stage, to confirm that no new issues arose during
the shutdown process. If Aurora detects any conditions at this point that would prevent the upgrade, Aurora cancels the upgrade and brings the cluster
back online. In this case, confirm when the conditions no longer apply and start the upgrade again. 3. Aurora creates a snapshot of your cluster volume. Suppose that you discover compatibility or other kinds of issues after the upgrade is finished.
Or suppose that you want to perform testing using both the original and upgraded clusters. In such cases, you can restore from this snapshot to create
a new cluster with the original engine version and the original data.

###### Tip

This snapshot is a manual snapshot. However, Aurora can create it and continue with the upgrade process even if you have reached your quota for
manual snapshots. This snapshot remains permanently (if needed) until you delete it. After you finish all post-upgrade testing, you can delete this
snapshot to minimize storage charges. 4. Aurora clones your cluster volume. Cloning is a fast operation that doesn't involve copying the actual table data. If Aurora encounters an
issue during the upgrade, it reverts to the original data from the cloned cluster volume and brings the cluster back online. The temporary cloned
volume during the upgrade isn't subject to the usual limit on the number of clones for a single cluster volume. 5. Aurora performs a clean shutdown for the writer DB instance. During the clean shutdown, progress events are recorded every 15 minutes for the
following operations. You can examine events as they occur on the **Events** page in the RDS console.

    * Aurora purges the undo records for old versions of rows.
    * Aurora rolls back any uncommitted transactions.

6. Aurora upgrades the engine version on the writer DB instance:
   - Aurora installs the binary for the new engine version on the writer DB instance.
   - Aurora uses the writer DB instance to upgrade your data to MySQL 5.7-compatible format. During this stage, Aurora modifies the system tables
     and performs other conversions that affect the data in your cluster volume. In particular, Aurora upgrades the partition metadata in the system
     tables to be compatible with the MySQL 5.7 partition format. This stage can take a long time if the tables in your cluster have a large number of
     partitions.

   If any errors occur during this stage, you can find the details in the MySQL error logs. After this stage starts, if the upgrade process
   fails for any reason, Aurora restores the original data from the cloned cluster volume.

7. Aurora upgrades the engine version on the reader DB instances.
8. The upgrade process is completed. Aurora records a final event to indicate that the upgrade process completed successfully. Now your DB cluster is
   running the new major version.

## Planning a major version upgrade for an Aurora MySQL cluster

To help you decide the right time and approach to upgrade, you can learn the differences
between Aurora MySQL version 3 and your current environment:

- If you're converting from RDS for MySQL 8.0 or MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](AuroraMySQL.md "AuroraMySQL.md").
- If you're upgrading from Aurora MySQL version 2, RDS for MySQL 5.7, or community MySQL
  5.7, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](AuroraMySQL.md "AuroraMySQL.md").
- Create new MySQL 8.0-compatible versions of any custom parameter groups. Apply any
  necessary custom parameter values to the new parameter groups. Consult [Parameter changes for Aurora MySQL version 3](AuroraMySQL.md#AuroraMySQL.mysql80-parameter-changes "AuroraMySQL.md#AuroraMySQL.mysql80-parameter-changes") to learn about parameter
  changes.
- Review your Aurora MySQL version 2 database schema and object definitions for the usage
  of new reserved keywords introduced in MySQL 8.0 Community Edition. Do so before you
  upgrade. For more information, see [MySQL 8.0 New Keywords and Reserved Words](https://dev.mysql.com/doc/mysqld-version-reference/en/keywords-8-0.html#keywords-new-in-8-0 "https://dev.mysql.com/doc/mysqld-version-reference/en/keywords-8-0.html#keywords-new-in-8-0") in the MySQL documentation.

You can also find more MySQL-specific upgrade considerations and tips in [Changes in
MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html "https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html") in the _MySQL Reference Manual_. For example, you can
use the command `mysqlcheck --check-upgrade` to analyze your existing Aurora MySQL
databases and identify potential upgrade issues.

###### Note

We recommend using larger DB instance classes when upgrading to Aurora MySQL version 3
using the in-place upgrade or snapshot restore technique. Examples are db.r5.24xlarge and
db.r6g.16xlarge. This helps the upgrade process to complete faster by using the majority of
available CPU capacity on the DB instance. You can change to the DB instance class that you
want after the major version upgrade is complete.

After you finish the upgrade itself, you can follow the post-upgrade procedures in [Post-upgrade cleanup for Aurora MySQL version 3](AuroraMySQL.md "AuroraMySQL.md"). Finally, test your application's functionality and performance.

If you're converting from RDS from MySQL or community MySQL, follow the migration
procedure explained in [Migrating data to an Amazon Aurora MySQL DB cluster](AuroraMySQL.md "AuroraMySQL.md"). In some cases, you might use binary log replication
to synchronize your data with an Aurora MySQL version 3 cluster as part of the migration. If so,
the source system must run a version that's compatible with your target DB
cluster.

To make sure that your applications and administration procedures work smoothly after
upgrading a cluster between major versions, do some advance planning and preparation. To see
what sorts of management code to update for your AWS CLI scripts or RDS API–based
applications, see [How in-place upgrades affect the parameter groups for a cluster](AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.ParamGroups "AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.ParamGroups"). Also see [Changes to cluster properties between Aurora MySQL versions](AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.Attrs "AuroraMySQL.Upgrading.md#AuroraMySQL.Upgrading.Attrs").

To learn what issues that you might encounter during the upgrade, see [Troubleshooting for Aurora MySQL in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md"). For issues that might cause the
upgrade to take a long time, you can test those conditions in advance and correct them.

###### Note

An in-place upgrade involves shutting down your DB cluster while the operation takes
place. Aurora MySQL performs a clean shutdown and completes outstanding operations such as
undo purge. An upgrade might take a long time if there many undo records to purge. We
recommend performing the upgrade only after the history list length (HLL) is low. A
generally acceptable value for the HLL is 100,000 or less. For more information, see this
[blog post](https://aws.amazon.com/blogs/database/amazon-aurora-mysql-version-2-with-mysql-5-7-compatibility-to-version-3-with-mysql-8-0-compatibility-upgrade-checklist-part-2 "https://aws.amazon.com/blogs/database/amazon-aurora-mysql-version-2-with-mysql-5-7-compatibility-to-version-3-with-mysql-8-0-compatibility-upgrade-checklist-part-2").

### Simulating the upgrade by cloning

your DB cluster

You can check application compatibility, performance, maintenance procedures, and
similar considerations for the upgraded cluster. To do so, you can perform a simulation of
the upgrade before doing the real upgrade. This technique can be especially useful for
production clusters. Here, it's important to minimize downtime and have the upgraded
cluster ready to go as soon as the upgrade has finished.

Use the following steps:

1. Create a clone of the original cluster. Follow the procedure in [Cloning a volume for an Amazon Aurora DB cluster](Aurora.Managing.md "Aurora.Managing.md").
2. Set up a similar set of writer and reader DB instances as in the original
   cluster.
3. Perform an in-place upgrade of the cloned cluster. Follow the procedure in [How to perform an in-place upgrade](AuroraMySQL.Upgrading.md "AuroraMySQL.Upgrading.md").

Start the upgrade immediately after creating the clone. That way, the cluster volume
is still identical to the state of the original cluster. If the clone sits idle before
you do the upgrade, Aurora performs database cleanup processes in the background. In that
case, the upgrade of the clone isn't an accurate simulation of upgrading the
original cluster. 4. Test application compatibility, performance, administration procedures, and so on,
using the cloned cluster. 5. If you encounter any issues, adjust your upgrade plans to account for them. For
example, adapt any application code to be compatible with the feature set of the higher
version. Estimate how long the upgrade is likely to take based on the amount of data in
your cluster. You might also choose to schedule the upgrade for a time when the cluster
isn't busy. 6. After you're satisfied that your applications and workload work properly with the
test cluster, you can perform the in-place upgrade for your production cluster. 7. Work to minimize the total downtime of your cluster during a major version upgrade.
To do so, make sure that the workload on the cluster is low or zero at the time of the
upgrade. In particular, make sure that there are no long running transactions in
progress when you start the upgrade.

### Blue/Green Deployments

In some situations, your top priority is to perform an immediate switchover from the old cluster to an upgraded one. In such situations, you can use
a multistep process that runs the old and new clusters side-by-side. Here, you replicate data from the old cluster to the new one until you are ready
for the new cluster to take over. For details, see [Using Amazon Aurora Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").
