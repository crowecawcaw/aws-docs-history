# Oracle and Aurora for PostgreSQL upgrades

With AWS DMS, you can upgrade your Oracle and Aurora PostgreSQL databases to newer versions with minimal downtime. The Oracle and Aurora PostgreSQL upgrades feature facilitates seamless database upgrades by creating a new database instance with the desired version, migrating data from the old instance, and redirecting applications to the new instance. This capability is crucial for organizations that need to stay current with the latest database software releases for security, performance, and compatibility reasons.

| Feature compatibility | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| --------------------- | ---------------------------------- | ------------------------- | --------------- |
| N/A                   | N/A                                | N/A                       | N/A             |

## Oracle usage

As a Database Administrator, from time to time a database upgrade is required, it can be either for security fix, but, or a new database feature.

The Oracle upgrades are divided into two different types of upgrades, minor and major.

This topic will outline the differences between the procedure to run upgrades on your Oracle databases today and how you will run those upgrades post migrating to Amazon RDS running Aurora.

The regular presentation of Oracle versions is combined of 4 numbers divided by dots (sometimes you will see the fifth number).

Either way, major or minor upgrades, the first step to initiate the processes mentioned above would be to install the new Oracle software on the database server, and of course before upgrading a production database to have an extensive amount of testing with the applications using the database to upgrade.

Oracle 18c introduces Zero-Downtime Database Upgrade to automate database upgrade and potentially eliminate application downtime during this process.

To understand the versions, let us use the following example 11.2.0.4.0.

These digits have the following meaning:

- 11 — is the major database version.
- 2 — is the database maintenance version.
- 0 — application server version.
- 4 — component specific version.
- 0 — platform specific version.

For more information, see [About Oracle Database Release Numbers](https://docs.oracle.com/en/database/oracle/oracle-database/19/upgrd/oracle-database-release-numbers.html#GUID-1E2F3945-C0EE-4EB2-A933-8D1862D8ECE2 "https://docs.oracle.com/en/database/oracle/oracle-database/19/upgrd/oracle-database-release-numbers.html#GUID-1E2F3945-C0EE-4EB2-A933-8D1862D8ECE2") in the _Oracle documentation_.

In Oracle, the users can set the compatibility level of the database to control the features and some behaviors.

This is being done using the `COMPATIBLE` parameter, the value for this parameter can be fetched using the following query.

```
SELECT NAME, VALUE FROM V$PARAMETER WHERE NAME = 'compatible';
```

## Upgrade process

In general, the process for major or minor upgrades is the same, minor version upgrade has less steps but overall the process is very similar.

Major upgrade referring to upgrades of the version number in the Oracle version, in the preceding example "11", the minor upgrade refers to any of the following numbers in the Oracle version, in the preceding example these will be "2.0.4.0".

Major upgrades are mostly being done in order to gain many new useful features being released between those versions, while minor upgrades are focused on bug and security fixes.

You can perform upgrades using the Oracle upgrade tools or manually.

Oracle tools will perform the following steps and might ask for some inputs or fixes from the user during the process.

- **Upgrade operation type** — the user chooses either Oracle database upgrade or move database between Oracle software installations.
- **Database selection** — the user selects the database to upgrade and the Oracle software to use for this database.
- **Prerequisite checks** — Oracle tools will let the use choose what to do with all issues found and their severity.
- **Upgrade options** — Oracle will let the use to pick his practices to do the upgrade, options such as recompilation and parallelism for those, time zone upgrade, statistics gathering, and more.
- **Management options** — the user chooses to connect and configure Oracle management solutions to the database.
- **Move database files** — the user chooses if a data file movement is required to a new devices or path.
- **Network configuration** — Oracle listener configurations.
- **Recovery options** — the user defines Oracle backup solutions or using his own.
- **Summary** — a report of all options that were selected in previous steps to present before the upgrade.
- **Progress** — monitor and present the upgrade status.
- **Results** — a post upgrade summary.

For the manual process, we won’t cover all actions in this topic, as there are many steps and commands to run.

In overall, the preceding steps will be divided into many sub-steps and tasks to run.

For more information, see [Example of Manual Upgrade of Windows Non-CDB Oracle Database 11.2.0.3](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/upgrd/example-manual-upgrade-windows-non-cdb-11203-to-122.html#GUID-30F3DC9C-141A-47DC-9B83-6D0C395E565C "https://docs.oracle.com/en/database/oracle/oracle-database/12.2/upgrd/example-manual-upgrade-windows-non-cdb-11203-to-122.html#GUID-30F3DC9C-141A-47DC-9B83-6D0C395E565C") in the _Oracle documentation_.

## Aurora for PostgreSQL usage

After migrating your databases to Amazon RDS running Aurora for PostgreSQL, you will still need to upgrade your database instances from time to time, for the same reasons you have done in the past, new features, bugs and security fixes.

In a managed service such as Amazon RDS, the upgrade process is much easier and simpler compare to the on-prem Oracle process.

To determine the current Aurora for PostgreSQL version being used, you can use the following AWS CLI command.

```
aws rds describe-db-engine-versions
  --engine aurora-postgresql
  --query '*[].[EngineVersion]'
  --output text
  --region your-AWS-Region
```

This can also be queried from the database, using the following queries.

```
SELECT AURORA_VERSION();

aurora_version
4.0.0

SHOW SERVER_VERSION;

server_version
12.4
```

For Aurora and PostgreSQL versions mapping, see [Amazon Aurora PostgreSQL releases and engine versions](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.md") in the _Amazon RDS user guide_.

AWS doesn’t apply major version upgrades on Amazon RDS and Aurora automatically. Major version upgrades contain new features and functionality which often involves system table and other code changes. These changes may not be backward-compatible with previous versions of the database so application testing is highly recommended.

Applying automatic minor upgrades can be set by configuring the Amazon RDS instance to allow it.

You can use the following AWS CLI command on Linux to determine the current automatic upgrade minor versions.

```
aws rds describe-db-engine-versions
  --engine aurora-postgresql
  | grep -A 1 AutoUpgrade
  | grep -A 2 true
  | grep PostgreSQL
  | sort --unique
  | sed -e 's/"Description":"//g'
```

If no results are returned, there is no automatic minor version upgrade available and scheduled.

When enabled, the instance will be automatically upgraded during the scheduled maintenance window.

For major upgrades, this is the recommended process:

- Have a version-compatible parameter group ready. If you are using a custom DB instance or DB cluster parameter group, you have two options:
  - Specify the default DB instance, DB cluster parameter group, or both for the new DB engine version.
  - Create your own custom parameter group for the new DB engine version.

  If you associate a new DB instance or DB cluster parameter group as a part of the upgrade request, make sure to reboot the database after the upgrade completes to apply the parameters. If a DB instance needs to be rebooted to apply the parameter group changes, the instance’s parameter group status shows pending-reboot. You can view an instance’s parameter group status in the console or by using a CLI command such as `describe-db-instances` or `describe-db-clusters`.

- Check for unsupported usage.
  - Commit or roll back all open prepared transactions before attempting an upgrade. You can use the following query to verify that there are no open prepared transactions on your instance

  ```
  SELECT count(*) FROM pg_catalog.pg_prepared_xacts;
  ```

  - Remove all uses of the `reg*` data types before attempting an upgrade. Except for `regtype` and `regclass`, you can’t upgrade the `reg*` data types. The `pg_upgrade` utility can’t persist this data type, which is used by Amazon Aurora to do the upgrade. To verify that there are no uses of unsupported `reg*` data types, use the following query for each database.

  ```
  SELECT count(*)
    FROM pg_catalog.pg_class c,
    pg_catalog.pg_namespace n,
    pg_catalog.pg_attribute a
      WHERE c.oid = a.attrelid
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

- Perform a backup. The upgrade process creates a DB cluster snapshot of your DB cluster during upgrading. If you also want to do a manual backup before the upgrade process.
- Upgrade `pgRouting` and `postGIS` extensions to the latest available version before performing the major version upgrade. Run the following command for each extension that you use.

```
ALTER EXTENSION PostgreSQL-extension UPDATE TO 'new-version'
```

An upgrade from versions older than 12, requires additional steps. For more information, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.md") in the _Amazon RDS user guide_.

After meeting all preceding prerequisites, you can perform the actual upgrade through the AWS console or AWS CLI.

**AWS Console**

1. Sign in to your AWS console and choose **RDS**.
2. Choose **Databases** and select the database cluster that you want to upgrade.
3. Choose **Modify**.
4. For **DB engine version**, choose the new version.
5. Choose **Continue** and check the summary of modifications.
6. To apply the changes immediately, choose **Apply immediately**. Choosing this option can cause an outage in some cases. For more information, see [Modifying an Amazon Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.md") in the _Amazon RDS user guide_.
7. On the confirmation page, review your changes. If they are correct, choose **Modify cluster** to save your changes. Or choose **Back** to edit your changes or **Cancel** to cancel your changes.

**AWS CLI**

For Linux, macOS, or Unix, use the following query.

```
aws rds modify-db-cluster \
  --db-cluster-identifier mydbcluster \
  --engine-version new_version \
  --allow-major-version-upgrade \
  --no-apply-immediately
```

For Windows, use the following query.

```
aws rds modify-db-cluster ^
  --db-cluster-identifier mydbcluster ^
  --engine-version new_version ^
  --allow-major-version-upgrade ^
  --no-apply-immediately
```

## Summary

| Phase                 | Oracle Step                                         | Aurora for PostgreSQL                                                                                                                                                                               |
| --------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prerequisite          | Install new Oracle software                         | N/A                                                                                                                                                                                                 |
| Prerequisite          | Upgrade operation type                              | N/A                                                                                                                                                                                                 |
| Prerequisite          | Database selection                                  | Select the right Amazon RDS instance                                                                                                                                                                |
| Prerequisite          | Prerequisite checks                                 | 1. Remove all uses of the reg data types.<br>2. Upgrade certain extensions<br>3. Commit or roll back all open prepared transactions<br>`<br>SELECT count(*) FROM pg_catalog.pg_prepared_xacts;<br>` |
| Prerequisite          | Upgrade options                                     | N/A                                                                                                                                                                                                 |
| Prerequisite          | Management options (optional)                       | N/A                                                                                                                                                                                                 |
| Prerequisite          | Move database files (optional)                      | N/A                                                                                                                                                                                                 |
| Prerequisite          | Network configuration (optional)                    | N/A                                                                                                                                                                                                 |
| Prerequisite          | Recovery options                                    | N/A                                                                                                                                                                                                 |
| Prerequisite          | Summary                                             | N/A                                                                                                                                                                                                 |
| Prerequisite          | Perform a database backup                           | Run Amazon RDS instance backup                                                                                                                                                                      |
| Prerequisite          | Stop application and connection                     | Same                                                                                                                                                                                                |
| Run                   | Progress                                            | Review status from the console                                                                                                                                                                      |
| Post-upgrade          | Results                                             | Review status from the console                                                                                                                                                                      |
| Post-upgrade          | Test applications against the new upgraded database | Same                                                                                                                                                                                                |
| Production deployment | Re-run all steps in a production environment        | Same                                                                                                                                                                                                |

For more information, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.md") in the _Amazon RDS user guide_.
