# Oracle and Aurora MySQL upgrades

With AWS DMS, you can upgrade your Oracle and Aurora MySQL databases to newer versions with minimal downtime. The Oracle and Aurora MySQL Upgrades feature facilitates seamless database upgrades by creating a new database instance with the desired version, migrating data from the old instance, and redirecting applications to the new instance. This capability is crucial for organizations that need to stay current with the latest database software releases for security, performance, and compatibility reasons.

## Oracle usage

As a Database Administrator, from time to time a database upgrade is required, it can be either for security fix, but, or a new database feature.

The Oracle upgrades are divided into two different types of upgrades, minor and major.

This topic will outline the differences between the procedure to execute upgrades on your Oracle databases today and how you will run those upgrades post migrating to Amazon RDS running Aurora.

The regular presentation of Oracle versions is combined of 4 numbers divided by dots, and sometimes you can see the fifth number.

Either way, major or minor upgrades, the first step to initiate the processes mentioned above would be to install the new Oracle software on the database server, and of course before upgrading a production database to have an extensive amount of testing with the applications using the database to upgrade.

Oracle 18c introduces Zero-Downtime Database Upgrade to automate Database upgrade and potentially eliminate application downtime during this process.

To understand the versions, let us use the following example 11.2.0.4.0. The digits in this example mean the following:

- 11 — The major database version.
- 2 — The database maintenance version.
- 0 — The application server version.
- 4 — The component-specific version.
- 0 — The platform-specific version.

For more information, see [About Oracle Database Release Numbers](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/upgrd/about-oracle-database-release-numbers.html#GUID-1E2F3945-C0EE-4EB2-A933-8D1862D8ECE2 "https://docs.oracle.com/en/database/oracle/oracle-database/12.2/upgrd/about-oracle-database-release-numbers.html#GUID-1E2F3945-C0EE-4EB2-A933-8D1862D8ECE2") in the _Oracle documentation_.

In Oracle, users can set the compatibility level of the database to control the features and some behaviors.

You can do this by using the `COMPATIBLE` parameter. Use the following query to fetch the value for this parameter:

```
SELECT NAME, VALUE FROM V$PARAMETER WHERE NAME = 'compatible';
```

### Upgrade process

In general, the process of major or minor upgrades is the same. Minor version upgrade has less steps but overall the process is similar.

Major upgrade referring to upgrades of the version number in the Oracle version. In the preceding example, the minor upgrade refers to any of the following numbers in the Oracle version that follow the major database version: 2.0.4.0.

Major upgrades are mostly being done in order to gain many new useful features being released between those versions, while minor upgrades are focused on bug and security fixes.

You can upgrade your database version using the Oracle upgrade tools or manually.

Oracle tools perform the following steps and might ask for some inputs or fixes from the user along the process. The upgrade steps are:

- **Upgrade operation type** — the user chooses either to upgrade an Oracle database or move a database between Oracle software installations.
- **Database selection** — the user selects the database to upgrade and the Oracle software to use for this database.
- **Prerequisite checks** — Oracle tools let the user choose what to do with all issues found and their severity.
- **Upgrade options** — Oracle lets the user to pick his practices to do the upgrade, using such options as: recompilation and parallelism for those, time zone upgrade, statistics gathering, and more.
- **Management options** — the user chooses to connect or configure the Oracle management solutions to the database.
- **Move database files** — the user chooses if a data file movement is required to a new devices or path.
- **Network configuration** — Oracle listener configurations.
- **Recovery options** — the user defines Oracle backup solutions or uses his own.
- **Summary** — a report of all options were selected in previous steps to present before the upgrade.
- **Progress** — monitor and present the upgrade status.
- **Results** — a post-upgrade summary.

For the manual process, we won’t cover all actions in this topic, as there are many steps and commands to run.

In overall, the eleven steps mentioned before, will be divided into many sub-steps and tasks to run.

For more information, see [Example of Manual Upgrade of Windows Non-CDB Oracle Database 11.2.0.3](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/upgrd/example-manual-upgrade-windows-non-cdb-11203-to-122.html#GUID-30F3DC9C-141A-47DC-9B83-6D0C395E565C "https://docs.oracle.com/en/database/oracle/oracle-database/12.2/upgrd/example-manual-upgrade-windows-non-cdb-11203-to-122.html#GUID-30F3DC9C-141A-47DC-9B83-6D0C395E565C") in the _Oracle documentation_.

## MySQL usage

After migrating your databases to Amazon Aurora MySQL, make sure that you upgrade your database instance from time to time, for the same reasons you have done it in the past like new features, bugs and security fixes.

In a managed service such as Amazon Relational Database Service, the upgrade process is much easier and simpler compare to the on-prem Oracle process.

To determine the current Aurora for MySQL version being used, you can use the following AWS CLI command:

```
aws rds describe-db-engine-versions --engine aurora-mysql --query '*[].[EngineVersion]' --output text --region your-AWS-Region
```

You can also query this from the database, using the following queries:

```
SELECT AURORA_VERSION();
```

In an Aurora MySQL version number scheme, for example 2.08.1, first digit represents the major version. Aurora MySQL version 1 is compatible with MySQL 5.6 and Aurora MySQL version 2 is compatible with MySQL 5.7. For more information about Aurora and MySQL versions mapping, see [Database engine updates for Amazon Aurora MySQL version 2](../../../AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../../../AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md") in the _Release Notes for Aurora MySQL_.

AWS doesn’t apply major version upgrades on Amazon RDS Aurora automatically. Major version upgrades contains new features and functionality which often involves system table and other code changes. These changes may not be backward-compatible with previous versions of the database so applications testing is highly recommended.

Applying automatic minor upgrades can be set by configuring the Amazon RDS instance to allow it.

You can use the following AWS CLI command on Linux to determine the current automatic upgrade minor versions.

```
aws rds describe-db-engine-versions --output=table --engine mysql --engine-version minor-version --region region
```

###### Note

If the query doesn’t return results, there is no automatic minor version upgrade available and scheduled.

When enabled, the instance will be automatically upgraded during the scheduled maintenance window.

To upgrade your cluster to a compatible cluster, you can do so by running an upgrade process on the cluster itself. This kind of upgrade is an in-place upgrade, in contrast to upgrades that you do by creating a new cluster. The upgrade is relatively fast because it doesn’t require copying all your data to a new cluster volume. In-place upgrade preserves the endpoints and set of DB instances for your cluster.

To verify application compatibility, performance and maintenance procedures for the upgraded cluster, you can perform a simulation of the upgrade by doing the following: \* Clone a cluster. \* Perform an in-place upgrade of the cloned cluster. \* Test applications, performance and so on, using the cloned cluster. \* Resolve any issues, adjust your upgrade plans to account for them. \* Once all the testing looks good, you can perform the in-place upgrade for your production cluster.

For major upgrades, AWS recommends the following flow:

- Check for open XA transactions by running the `XA RECOVER` statement. Commit or rollback the XA transactions before starting the upgrade.
- Check for DDL statements by running the `SHOW PROCESSLIST` statement and looking for `CREATE`, `DROP`, `ALTER`, `RENAME`, and `TRUNCATE` statements in the output. Allow all DDLs to finish before starting the upgrade.
- Check for any uncommitted rows by querying the `INFORMATION_SCHEMA.INNODB_TRX` table. The table contains one row for each transaction. Let the transaction complete or shut down applications that are submitting these changes.

Aurora MySQL performs a major version upgrade in multiple steps. After each step begins, Aurora MySQL records an event. You can monitor the current status and events as they occur on the Events page in the Amazon RDS console.

Aurora performs a series of checks before beginning the upgrade process. If any issues are detected during these checks, resolve the issue identified in the event details and restart the upgrade process.

Aurora takes the cluster offline, performs a similar set of tests as in the previous step. If no new issues are identified, then Aurora moves with the next step. If any issues are detected during these checks, resolve the issue identified in the event details and restart the upgrade process again.

Aurora backups up the MySQL cluster by creating a snapshot of the cluster volume.

Aurora clones the cluster volume. If any issues are encountered during the upgrade, Aurora reverts to the original data from the cloned cluster volume and brings the cluster back online.

Aurora performs a clean shutdown and it rolls back any uncommitted transactions.

Aurora upgrades the engine version. It installs the binary for the new engine version and uses the writer DB instance to upgrade your data to new to MySQL compatible format. During this stage, Aurora modifies the system tables and performs other conversions that affect the data in your cluster volume.

The upgrade process is completed. Aurora records a final event to indicate that the upgrade process completed successfully. Now DB cluster is running the new major version.

Upgrade can be done through the AWS Console or AWS CLI.

## Upgrade using the AWS Management Console

1. Sign in to the AWS Management Console and choose **RDS**.
2. Choose **Databases**, and then choose the DB cluster that you want to upgrade.
3. Choose **Modify**. The **Modify DB cluster page** appears.
4. For **DB engine version**, choose the new version.
5. Choose **Continue** and check the summary of modifications.
6. To apply the changes immediately, choose **Apply immediately**. Choosing this option can cause an outage in some cases. For more information, see [Modifying an Amazon Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md") in the _User Guide for Aurora_.
7. On the confirmation page, review your changes. If they are correct, choose **Modify cluster** to save your changes. Alternatively, choose **Back** to edit your changes or **Cancel** to cancel your changes.

## Upgrade using AWS CLI

To upgrade the major version of an Aurora MySQL DB cluster, use the AWS CLI `modify-db-cluster` command with the following required parameters:

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
--db-cluster-identifier sample-cluster \
--engine aurora-mysql \
--engine-version 5.7.mysql_aurora.2.09.0 \
--allow-major-version-upgrade \
--apply-immediately
```

For Windows:

```
aws rds modify-db-cluster ^
--db-cluster-identifier sample-cluster ^
--engine aurora-mysql ^
--engine-version 5.7.mysql_aurora.2.09.0 ^
--allow-major-version-upgrade ^
--apply-immediately
```

## Summary

| Phase                 | Oracle                                              | Aurora MySQL                                                 |
| --------------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| Prerequisite          | Install new Oracle software                         | N/A                                                          |
| Prerequisite          | Upgrade operation type                              | N/A                                                          |
| Prerequisite          | Database selection                                  | Select the right Amazon Relational Database Service instance |
| Prerequisite          | Prerequisite checks                                 | Commit or rollback uncommitted transactions                  |
| Prerequisite          | Upgrade options                                     | N/A                                                          |
| Prerequisite          | Management options (optional)                       | N/A                                                          |
| Prerequisite          | Move database files (optional)                      | N/A                                                          |
| Prerequisite          | Network configuration (optional)                    | N/A                                                          |
| Prerequisite          | Recovery options                                    | N/A                                                          |
| Prerequisite          | Summary                                             | N/A                                                          |
| Prerequisite          | Perform a database backup                           | Run an Amazon Relational Database Service instance backup    |
| Prerequisite          | Stop application and connection                     | Stop application and connection                              |
| Run                   | Progress                                            | Can be reviewed from the console                             |
| Post-upgrade          | Results                                             | Can be reviewed from the console                             |
| Post-upgrade          | Test applications against the new upgraded database | Test applications against the new upgraded database          |
| Production deployment | Re-run all steps in a production environment        | Re-run all steps in a production environment                 |

For more information, see [Upgrading Amazon Aurora MySQL DB clusters](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.md") in the _User Guide for Aurora_.
