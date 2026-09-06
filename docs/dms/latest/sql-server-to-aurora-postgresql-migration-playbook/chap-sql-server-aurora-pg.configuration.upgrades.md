

# Configuring upgrades
<a name="chap-sql-server-aurora-pg.configuration.upgrades"></a>

This topic provides reference information on upgrading database instances, comparing the process for Microsoft SQL Server and Amazon Aurora PostgreSQL. You can use this information to plan and execute database upgrades, whether you’re working with on-premises SQL Server or managed Aurora PostgreSQL in the cloud. The guide walks you through the necessary steps for each platform, including prerequisites, upgrade procedures, and post-upgrade tasks.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
| N/A | N/A | N/A | N/A | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.configuration.upgrades.sqlserver"></a>

As a database administrator, from time to time a database upgrade is required. It can be either for security fix, bugs fixes, compliance, or new database features.

You can plan the database upgrade to minimize the database downtime and risk. You can perform an upgrade in-place or migrate to a new installation.

## Upgrade in-place
<a name="chap-sql-server-aurora-pg.configuration.upgrades.sqlserver.process"></a>

With this approach, we are retaining the current hardware and OS version by adding the new SQL Server binaries on the same server and then upgrade the SQL Server instance.

Before upgrading the database engine, review the SQL Server release notes for the intended target release version for any limitations and known issues to help you plan the upgrade.

In general, these will be the steps to perform the upgrade:

 **Prerequisite steps** 
+ Back up all SQL Server database files, so that you can restore them if required.
+ Run the appropriate Database Console Commands (DBCC CHECKDB) on databases to be upgraded to ensure that they are in a consistent state.
+ Ensure to allocate enough disk space for SQL Server components, in addition to user databases.
+ Disable all startup stored procedures as stored procedures processed at startup time might block the upgrade process.
+ Stop all applications, including all services that have SQL Server dependencies.

 **Steps for upgrade** 
+ Install new software.
  + Fix issues raised.
  + Set if you prefer to have automatic updates or not.
  + Select products install to upgrade, this is the new binaries installation.
  + Monitor the progress of downloading, extracting, and installing the Setup files.
+ Specify the instance of SQL Server to upgrade.
  + On the Select Features page, the features to upgrade will be preselected. The prerequisites for the selected features are displayed on the right-hand pane. SQL Server Setup will install the prerequisite that aren’t already installed during the installation step described later in this procedure.
+ Review upgrade plan before the actual upgrade.
+ Monitor installation progress.

 **Post upgrade tasks** 
+ Review summary log file for the installation and other important notes.
+ Register your servers.

### Migrate to a new installation
<a name="chap-sql-server-aurora-pg.configuration.sectionname.sqlserver.migratetoanewinstallation"></a>

This approach maintains the current environment while building a new SQL Server environment. This is usually done when migrating on a new hardware and with a new version of the operating system. In this approach migrate the system objects so that they are same as the existing environment, then migrate the user database either using backup and restore.

For more information, see [Upgrade Database Engine](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-database-engine?view=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.configuration.sectionname.pg"></a>

After migrating your databases to Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL), you will still need to upgrade your database instance from time to time, for the same reasons you have done in the past, new features, bugs and security fixes.

In a managed service like Amazon Relational Database Service, the upgrade process is much easier and simpler compared to the on-premises Oracle process.

To determine the current Aurora PostgreSQL version being used, use the following AWS CLI command:

```
aws rds describe-db-engine-versions --engine aurora-postgresql --query '*[].[EngineVersion]' --output text --region your-AWS-Region
```

This can also be queried from the database, using the following queries:

```
SELECT AURORA_VERSION();

aurora_version
4.0.0

SHOW SERVER_VERSION;

server_version
12.4
```

For all Aurora and PostgreSQL versions mapping, see [Amazon Aurora PostgreSQL releases and engine versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html) in the *User Guide for Aurora*.

 AWS doesn’t apply major version upgrades on Amazon Aurora automatically. Major version upgrades contains new features and functionality which often involves system table and other code changes. These changes may not be backward-compatible with previous versions of the database so application testing are highly recommended.

Applying automatic minor upgrades can be set by configuring the Amazon Relational Database Service (Amazon RDS) instance to allow it.

You can use the following AWS CLI command on Linux to determine the current automatic upgrade minor versions.

```
aws rds describe-db-engine-versions --engine aurora-postgresql | grep -A 1 AutoUpgrade| grep -A 2 true |grep PostgreSQL | sort --unique | sed -e 's/"Description": "//g'
```

If no results are returned, there is no automatic minor version upgrade available and scheduled.

When enabled, the instance will be automatically upgraded during the scheduled maintenance window.

For major upgrades, this is the recommended process:
+ Have a version-compatible parameter group ready. If you are using a custom DB instance or DB cluster parameter group, you have two options:

  1. Specify the default DB instance, DB cluster parameter group, or both for the new DB engine version.

  1. Create your own custom parameter group for the new DB engine version.
**Note**  
If you associate a new DB instance or DB cluster parameter group as a part of the upgrade request, make sure to reboot the database after the upgrade completes to apply the parameters. If a DB instance needs to be rebooted to apply the parameter group changes, the instance’s parameter group status shows pending-reboot. You can view an instance’s parameter group status in the console or by using a CLI command such as `describe-db-instances` or `describe-db-clusters`.
+ Check for unsupported usage:

  1. Commit or roll back all open prepared transactions before attempting an upgrade. You can use the following query to verify that there are no open prepared transactions on your instance.

     ```
     SELECT count(*) FROM pg_catalog.pg_prepared_xacts;
     ```

  1. Remove all uses of the reg\* data types before attempting an upgrade. Except for `regtype` and `regclass`, you can’t upgrade the reg\* data types. The `pg_upgrade` utility can’t persist this data type, which is used by Amazon Aurora to do the upgrade. To verify that there are no uses of unsupported reg\* data types, use the following query for each database.

     ```
     SELECT count(*) FROM pg_catalog.pg_class c, pg_catalog.pg_namespace n, pg_
     catalog.pg_attribute aWHERE c.oid = a.attrelid
     AND NOT a.attisdropped
     AND a.atttypid IN ('pg_catalog.regproc'::pg_catalog.regtype,
     'pg_catalog.regprocedure'::pg_catalog.regtype,
     'pg_catalog.regoper'::pg_catalog.regtype,
     'pg_catalog.regoperator'::pg_catalog.regtype,
     'pg_catalog.regconfig'::pg_catalog.regtype,
     'pg_catalog.regdictionary'::pg_catalog.regtype)
     AND c.relnamespace = n.oid
     AND n.nspname NOT IN ('pg_catalog', 'information_schema');
     ```
+ Perform a backup. The upgrade process creates a DB cluster snapshot of your DB cluster during upgrading.
+ Upgrade certain extensions to the latest available version before performing the major version upgrade. The extensions to update include the following:

  1. pgRouting

  1. postGIS
+ Run the following command for each extension that you are using.

  ```
  ALTER EXTENSION PostgreSQL-extension UPDATE TO 'new-version'
  ```

If you are upgrading versions older than PostgreSQL 12, there are a few more steps. For more information, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.html) in the *User Guide for Aurora*.

You can perform the actual upgrade through the console or AWS CLI.

 **Console** 

1. Sign in to the AWS Management Console and choose **RDS**.

1. In the navigation pane, choose **Databases**, and then choose the DB cluster that you want to upgrade.

1. Choose **Modify**. The **Modify DB cluster** page appears.

1. For **DB engine version**, choose the new version.

1. Choose **Continue** and check the summary of modifications.

1. To apply the changes immediately, choose **Apply immediately**. Choosing this option can cause an outage in some cases. For more information, see [Modifying an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Modifying.html) in the *User Guide for Aurora*.

1. On the confirmation page, review your changes. If they are correct, choose **Modify Cluster** to save your changes. Or choose **Back** to edit your changes or **Cancel** to cancel your changes.

 ** AWS CLI** 

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
--db-cluster-identifier mydbcluster \
--engine-version new_version \
--allow-major-version-upgrade \
--no-apply-immediately
```

For Microsoft Windows:

```
aws rds modify-db-cluster ^
--db-cluster-identifier mydbcluster ^
--engine-version new_version ^
--allow-major-version-upgrade ^
--no-apply-immediately
```

## Summary
<a name="chap-sql-server-aurora-pg.configuration.sectionname.summary"></a>


| Phase | SQL Server Step |  Aurora PostgreSQL  | 
| --- | --- | --- | 
| Prerequisite | Perform an instance backup. | Run Amazon RDS instance backup. | 
| Prerequisite | DBCC for consistent verification. | N/A | 
| Prerequisite | Validate disk size and free space. | N/A | 
| Prerequisite | Disable all startup stored procedures (if applicable). | N/A | 
| Prerequisite | Stop application and connection. | N/A | 
| Prerequisite | Install new software and fix prerequisites errors raised. |  1.  Remove all uses of the reg\* data types. <br />2.  Upgrade certain extensions. <br />3.  Commit or roll back all open prepared transactions. <pre>SELECT count(*) FROM pg_catalog.pg_prepared_xacts;</pre>   | 
| Prerequisite | Select instances to upgrade. | Select the right Amazon RDS instance. | 
| Prerequisite | Review pre-upgrade summary. | N/A | 
| Runtime | Monitor upgrade progress. | You can review from the console. | 
| Post-upgrade | Results. | You can review from the console. | 
| Post-upgrade | Register server. | N/A | 
| Post-upgrade | Test applications against the new upgraded database. | Test applications against the new upgraded database. | 
| Production deployment | Re-run all steps in a production environment. | Re-run all steps in a production environment. | 

For more information, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.html) in the *User Guide for Aurora*.