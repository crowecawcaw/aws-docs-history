# Upgrading

a DB instance engine version

Amazon RDS
provides newer versions of each supported database engine so you can keep your DB
instance
up-to-date. Newer versions can include bug fixes, security enhancements,
and other improvements for the database engine. When
Amazon RDS
supports a new version of a database engine, you can choose how and when to upgrade your database DB
instances.

There are two kinds of upgrades: major version upgrades and
minor version upgrades. In general, a _major engine version upgrade_
can introduce changes that are not compatible with existing applications. In contrast, a
_minor version upgrade_ includes only changes that are backward-compatible with existing
applications.

For Multi-AZ DB clusters, major version upgrades are only supported for
RDS for PostgreSQL. Minor version upgrades are supported for all engines that support Multi-AZ DB clusters. For
more information, see [Upgrading the engine version of a Multi-AZ DB cluster for Amazon RDS](multi-az-db-clusters-upgrading.md "multi-az-db-clusters-upgrading.md").

The version numbering sequence is specific to each database engine.
For example, RDS for MySQL 5.7 and 8.0 are major engine versions and upgrading from any 5.7
version to any 8.0 version is a major version upgrade. RDS for MySQL version 5.7.22 and 5.7.23
are minor versions and upgrading from 5.7.22 to 5.7.23 is a minor version upgrade.

###### Important

You can't modify a DB instance when it is being upgraded. During an upgrade, the
DB instance status is `upgrading`.

For more information about major and minor version upgrades for a
specific DB engine, see the following documentation for your DB engine:

- [Upgrades of the MariaDB DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
- [Upgrades of the Microsoft SQL Server DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
- [Upgrades of the RDS for MySQL DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
- [Upgrading the RDS for Oracle DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
- [Upgrades of the RDS for PostgreSQL DB
  engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
  For major version upgrades, you must manually modify the DB engine
  version through the AWS Management Console, AWS CLI, or RDS API. For minor version upgrades, you can
  manually modify the engine version, or you can choose to enable the **Auto minor version upgrade** option.

###### Note

Database engine upgrades require downtime. You can minimize the downtime required for
DB instance
upgrade by using a blue/green deployment. For more information,
see [Using Amazon RDS Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

###### Topics

- [Manually upgrading the engine version](#USER_UpgradeDBInstance.Upgrading.Manual "#USER_UpgradeDBInstance.Upgrading.Manual")
- [Automatically upgrading the minor engine version](#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades "#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades")

## Manually upgrading the engine version

To manually upgrade the engine version of a DB instance, you can use the AWS Management Console,
the AWS CLI, or the RDS API.

###### To upgrade the engine version of a DB instance by using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then
   choose the DB instance that you want to upgrade.
3. Choose **Modify**.
   The **Modify DB instance** page appears.
4. For **DB engine version**, choose the new version.
5. Choose **Continue** and check the summary of modifications.
6. Decide when to schedule your upgrade:
   - To put the changes into the pending modifications queue,
     choose **Apply during the next scheduled maintenance
     window**. During the next maintenance window, RDS
     applies any pending changes in the queue.
   - To apply the changes immediately, choose **Apply
     immediately**. Choosing this option can cause an
     outage in some cases. For more information, see [Using the schedule modifications
     setting](USER_ModifyInstance.md "USER_ModifyInstance.md").

7. On the confirmation page, review your changes.
   If they are correct, choose **Modify DB instance**
   to save your changes.

Alternatively, choose **Back** to edit your changes,
or choose **Cancel** to cancel your changes.
To upgrade the engine version of a DB instance,
use the CLI [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command.
Specify the following parameters:

- `--db-instance-identifier` –
  the name of the DB instance.
- `--engine-version` –
  the version number of the database engine to upgrade to.

For information about valid engine versions, use the AWS CLI [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") command.

- `--allow-major-version-upgrade` – to upgrade the
  major version.
- `--no-apply-immediately` – to apply changes during the
  next maintenance window. To apply changes immediately, use
  `--apply-immediately`.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --engine-version `new_version` \
    --allow-major-version-upgrade \
    --no-apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --engine-version `new_version` ^
    --allow-major-version-upgrade ^
    --no-apply-immediately
```

To upgrade the engine version of a DB instance,
use the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") action.
Specify the following parameters:

- `DBInstanceIdentifier` – the name of the DB instance,
  for example `mydbinstance`.
- `EngineVersion` – the version number of the database
  engine to upgrade to. For information about valid engine versions, use
  the [DescribeDBEngineVersions](../APIReference/API_DescribeDBEngineVersions.md "../APIReference/API_DescribeDBEngineVersions.md") operation.
- `AllowMajorVersionUpgrade` – whether to allow a major
  version upgrade. To do so, set the value to `true`.
- `ApplyImmediately` – whether to apply changes
  immediately or during the next maintenance window. To apply changes
  immediately, set the value to
  `true`. To apply changes
  during the next maintenance window, set the value to
  `false`.

## Automatically upgrading the minor engine version

Automatic minor version upgrades periodically update your
database to recent database engine versions. However, the upgrade might
not always include the latest database engine version. If you need to
keep your databases on specific versions at particular times,
we recommend that you manually upgrade to the database versions that
you need according to your required schedule.
In cases of critical security issues or when a version reaches its end-of-support date,
Amazon RDS
might apply a minor version upgrade even if you haven't enabled the **Auto minor version upgrade**
option. For more information, see the upgrade documentation for your specific database engine.

- [Automatic minor
  version upgrades for RDS for PostgreSQL](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md")
- [Automatic minor version upgrades for RDS for MySQL](USER_UpgradeDBInstance.MySQL.md "USER_UpgradeDBInstance.MySQL.md")
- [Automatic minor version upgrades for RDS for MariaDB](USER_UpgradeDBInstance.MariaDB.md "USER_UpgradeDBInstance.MariaDB.md")
- [Oracle minor version upgrades](USER_UpgradeDBInstance.Oracle.md "USER_UpgradeDBInstance.Oracle.md")
- [Upgrades of the Microsoft SQL Server DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
- [Db2 on Amazon RDS versions](Db2.Concepts.md "Db2.Concepts.md")

###### Topics

- [How automatic minor
  version upgrades work](#USER_UpgradeDBInstance.Upgrading.scheduled "#USER_UpgradeDBInstance.Upgrading.scheduled")
- [Turning on
  automatic minor version upgrades](#USER_UpgradeDBInstance.Upgrading.turning-on-automatic "#USER_UpgradeDBInstance.Upgrading.turning-on-automatic")
- [Determining the
  availability of maintenance updates](#USER_UpgradeDBInstance.Upgrading.availability "#USER_UpgradeDBInstance.Upgrading.availability")
- [Finding automatic minor
  version upgrade targets](#USER_UpgradeDBInstance.Upgrading.targets "#USER_UpgradeDBInstance.Upgrading.targets")

### How automatic minor

version upgrades work

The _upgrade target_ is the DB engine
version to which Amazon RDS upgrades your database. A minor engine
version is designated as the upgrade target when the following conditions are
met:

- The database is running a minor version of the DB engine that is lower than
  the target minor engine version.

You can find the current engine version for your DB instance by looking on the
**Configuration** tab of the database details page or
running the CLI command `describe-db-instances`.

- The database has automatic minor version upgrade enabled.

RDS schedules the upgrade to run automatically in the maintenance window. During
the upgrade, RDS does the following:

1. Runs a system precheck to make sure the database is healthy and ready to
   be upgraded
2. Upgrades the DB engine to the target minor engine version
3. Runs post-upgrade checks
4. Marks the database upgrade as complete

Automatic upgrades incur downtime. The length of the downtime depends on various
factors, including the DB engine type and the size of the database.

### Turning on

automatic minor version upgrades

You can control whether auto minor version upgrade is enabled for a DB instance when you
perform the following tasks:

- [Creating a DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md")
- [Modifying a
  DB instance](Overview.DBInstance.md "Overview.DBInstance.md")
- [Creating a read replica](USER_ReadRepl.md "USER_ReadRepl.md")
- [Restoring a DB instance from a snapshot](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md")
- [Restoring a DB instance to a
  specific time](USER_PIT.md "USER_PIT.md")
- [Importing a DB instance from
  Amazon S3](MySQL.Procedural.md "MySQL.Procedural.md") (for a MySQL backup on Amazon S3)

When you perform these tasks, you can control whether auto minor version upgrade
is enabled for the DB instance in the following ways:

- Using the console, set the **Auto minor version upgrade**
  option.
- Using the AWS CLI, set the
  `--auto-minor-version-upgrade|--no-auto-minor-version-upgrade`
  option.
- Using the RDS API, set the `AutoMinorVersionUpgrade`
  parameter.

### Determining the

availability of maintenance updates

To determine whether a maintenance update, such as a DB engine version upgrade, is
available for your DB instance, you can use the console, AWS CLI, or RDS API.
You can also upgrade the DB engine version manually and adjust the maintenance window.
For more information, see [Maintaining a DB instance](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

### Finding automatic minor

version upgrade targets

You can use the following AWS CLI command to determine the current automatic minor
upgrade target version for a specified minor DB engine version in a specific
AWS Region. You can find the possible `--engine` values for this
command in the description for the `Engine` parameter in [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md").

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
--engine `engine` \
--engine-version `minor-version` \
--region `region` \
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" \
--output text
```

For Windows:

```
aws rds describe-db-engine-versions ^
--engine `engine` ^
--engine-version `minor-version` ^
--region `region` ^
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" ^
--output text
```

For example, the following AWS CLI command determines the automatic minor upgrade
target for MySQL minor version 8.0.11 in the US East (Ohio) AWS Region
(us-east-2).

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
--engine mysql \
--engine-version 8.0.11 \
--region us-east-2 \
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" \
--output table
```

For Windows:

```
aws rds describe-db-engine-versions ^
--engine mysql ^
--engine-version 8.0.11 ^
--region us-east-2 ^
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" ^
--output table
```

Your output is similar to the following.

```
----------------------------------
|    DescribeDBEngineVersions    |
+--------------+-----------------+
|  AutoUpgrade |  EngineVersion  |
+--------------+-----------------+
|  False       |  8.0.15         |
|  False       |  8.0.16         |
|  False       |  8.0.17         |
|  False       |  8.0.19         |
|  False       |  8.0.20         |
|  False       |  8.0.21         |
**| True | 8.0.23 |**
|  False       |  8.0.25         |
+--------------+-----------------+
```

In this example, the `AutoUpgrade` value is `True` for MySQL
version 8.0.23. So, the automatic minor upgrade target is MySQL version 8.0.23,
which is highlighted in the output.

###### Important

If you plan to migrate an RDS for PostgreSQL DB instance to an Aurora PostgreSQL DB cluster
soon, we strongly recommend that you turn off auto minor version upgrades for
the DB instance early during planning. Migration to Aurora PostgreSQL might be delayed if
the RDS for PostgreSQL version isn't yet supported by Aurora PostgreSQL. For
information about Aurora PostgreSQL versions, see [Engine versions for Amazon Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.Updates.md "../AuroraUserGuide/AuroraPostgreSQL.Updates.md").
