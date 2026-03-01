# Restoring an RDS Custom for SQL Server instance to a point in time

You can restore a DB instance to a specific point in time (PITR), creating a new DB instance. To support PITR, your DB
instances must have backup retention enabled.

The latest restorable time for an RDS Custom for SQL Server DB instance depends on several factors, but is typically within 5 minutes of the
current time. To see the latest restorable time for a DB instance, use the AWS CLI [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") command and look at the value returned in
the `LatestRestorableTime` field for the DB instance. To see the latest restorable time for each DB instance in the
Amazon RDS console, choose **Automated backups**.

You can restore to any point in time within your backup retention period. To see the earliest restorable time for each DB
instance, choose **Automated backups** in the Amazon RDS console.

For general information about PITR, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

###### Topics

- [PITR considerations for RDS Custom for SQL Server](#custom-backup.pitr.sqlserver "#custom-backup.pitr.sqlserver")
- [Number of databases eligible for PITR per instance class type](#custom-backup.pitr.sqlserver.eligiblecountperinstance "#custom-backup.pitr.sqlserver.eligiblecountperinstance")
- [Making databases ineligible for PITR](#custom-backup.pitr.sqlserver.ineligible "#custom-backup.pitr.sqlserver.ineligible")
- [Transaction logs in Amazon S3](#custom-backup.pitr.sqlserver.tlogs "#custom-backup.pitr.sqlserver.tlogs")
- [PITR Restore using the AWS Management Console, the AWS CLI, or the RDS API.](#custom-backup.pitr-sqs-concli "#custom-backup.pitr-sqs-concli")

## PITR considerations for RDS Custom for SQL Server

In RDS Custom for SQL Server, PITR differs in the following important ways from PITR in Amazon RDS:

- PITR only restores the databases in the DB instance. It doesn't restore the operating system or files on the
  C: drive.
- For an RDS Custom for SQL Server DB instance, a database is backed up automatically and is eligible for PITR only under the
  following conditions:
  - The database is online.
  - Its recovery model is set to `FULL`.
  - It's writable.
  - It has its physical files on the D: drive.
  - It's not listed in the `rds_pitr_blocked_databases` table. For more information, see [Making databases ineligible for PITR](#custom-backup.pitr.sqlserver.ineligible "#custom-backup.pitr.sqlserver.ineligible").

- The databases eligible for PITR are determined by the order of their database ID. RDS Custom for SQL Server allows up to 5,000 databases per DB instance.
  However, the maximum number of databases restored by a PITR operation for an RDS Custom for SQL Server DB instance is dependent on the instance class type.
  For more information, see [Number of databases eligible for PITR per instance class type](#custom-backup.pitr.sqlserver.eligiblecountperinstance "#custom-backup.pitr.sqlserver.eligiblecountperinstance").

Other databases that aren't part of PITR can be restored from DB snapshots, including the automated snapshot backups
used for PITR.

- Adding a new database, renaming a database, or restoring a database that
  is eligible for PITR initiates a snapshot of the DB instance.
- The maximum number of databases eligible for PITR changes when the database instance goes through a scale compute
  operation, depending on the target instance class type. If the instance is scaled up, allowing more databases on the
  instance to be eligible for PITR, a new snapshot is taken.
- Restored databases have the same name as in the source DB instance. You can't specify a different name.
- `AWSRDSCustomSQLServerIamRolePolicy` requires access to other AWS services. For more information, see [Add an access policy to AWSRDSCustomSQLServerInstanceRole](custom-setup-sqlserver.md#custom-setup-sqlserver.iam.add-policy "custom-setup-sqlserver.md#custom-setup-sqlserver.iam.add-policy").
- Time zone changes aren't supported for RDS Custom for SQL Server. If you change the operating system or DB instance time zone,
  PITR (and other automation) doesn't work.

## Number of databases eligible for PITR per instance class type

The following table shows the maximum number of databases eligible for PITR based on instance class type.

| Instance class type              | Maximum number of PITR eligible databases |
| -------------------------------- | ----------------------------------------- |
| db.\*.large                      | 100                                       |
| db.\*.xlarge to db.\*.2xlarge    | 150                                       |
| db.\*.4xlarge to db.\*.8xlarge   | 300                                       |
| db.\*.12xlarge to db.\*.16xlarge | 600                                       |
| db.\*.24xlarge, db.\*32xlarge    | 1000                                      |

`*` _Represents different instance class types._

The maximum number of databases eligible for PITR on a DB instance depends on the instance class type. The number ranges
from 100 on the smallest to 1000 on the largest instance class types supported by RDS Custom for SQL Server.
SQL server system databases `(master, model, msdb, tempdb)`, aren't included in this limit. When a DB instance is scaled up or down,
depending on the target instance class type, RDS Custom will automatically update the number of database eligible for PITR.
RDS Custom for SQL Server will send `RDS-EVENT-0352` when the maximum number of databases eligible for PITR changes on a DB instance.
For more information, see [Custom engine version events](USER_Events.md#USER_Events.Messages.CEV "USER_Events.md#USER_Events.Messages.CEV").

###### Note

PITR support for greater than 100 databases is only available on DB instances created after August 26, 2023. For instances created before
August 26, 2023, the maximum number of databases eligible for PITR is 100, regardless of the instance class.
To enable PITR support for more than 100 databases on DB instances created before August 26, 2023,
you can perform the following action:

- Upgrade the DB engine version to 15.00.4322.2.v1 or higher

During a PITR operation, RDS Custom will restore all of the databases that were part of PITR on
source DB instance at restore time. Once the target DB instance has completed restore operations, if backup retention is enabled,
the DB instance will start backing up based on the maximum number of databases eligible for PITR on target DB instance.

For example, if your DB instance runs on a `db.*.xlarge` that has 200 databases:

1. RDS Custom for SQL Server will choose the first 150 databases, ordered by their database ID, for PITR backup.
2. You modify the instance to scale up to db.\*.4xlarge.
3. Once the scale compute operation is completed, RDS Custom for SQL Server will choose the first 300 databases, ordered by their database ID, for PITR backup.
   Each one of the 200 databases that satisfy the PITR requirement conditions will now be eligible for PITR.
4. You now modify the instance to scale down back to db.\*.xlarge.
5. Once the scale compute operation is completed, RDS Custom for SQL Server will again select the first 150 databases, ordered by their database ID, for PITR backup.

## Making databases ineligible for PITR

You can choose to exclude individual databases from PITR. To do this, put their
`database_id` values into a `rds_pitr_blocked_databases` table. Use the following SQL script
to create the table.

###### To create the rds_pitr_blocked_databases table

- Run the following SQL script.

```
create table msdb..rds_pitr_blocked_databases
(
database_id INT NOT NULL,
database_name SYSNAME NOT NULL,
db_entry_updated_date datetime NOT NULL DEFAULT GETDATE(),
db_entry_updated_by SYSNAME NOT NULL DEFAULT CURRENT_USER,
PRIMARY KEY (database_id)
);

```

For the list of eligible and ineligible databases, see the
`RI.End` file in the
`RDSCustomForSQLServer/Instances/`DB_instance_resource_ID`/TransactionLogMetadata`
directory in the Amazon S3 bucket
`do-not-delete-rds-custom-`$ACCOUNT_ID`-`$REGION`-`unique_identifier``.
 For more information about the `RI.End` file, see [Transaction logs in Amazon S3](#custom-backup.pitr.sqlserver.tlogs "#custom-backup.pitr.sqlserver.tlogs").

You can also determine the list of eligible databases for PITR using the following SQL script.
Set the `@limit` variable to the maximum number of databases on eligible for PITR for the instance class. For more
information, see [Number of databases eligible for PITR per instance class type](#custom-backup.pitr.sqlserver.eligiblecountperinstance "#custom-backup.pitr.sqlserver.eligiblecountperinstance").

###### To determine the list of eligible databases for PITR on a DB instance class

- Run the following SQL script.

```
DECLARE @Limit INT;
SET @Limit = (insert-database-instance-limit-here);

USE msdb;
IF (EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND  TABLE_NAME = 'rds_pitr_blocked_databases'))
    WITH TABLE0 AS (
        SELECT hdrs.database_id as DatabaseId, sdb.name as DatabaseName, 'ALWAYS_ON_NOT_WRITABLE_REPLICA' as Reason, NULL as DatabaseNameOnPitrTable
        FROM sys.dm_hadr_database_replica_states hdrs
        INNER JOIN sys.databases sdb ON sdb.database_id = hdrs.database_id
        WHERE (hdrs.is_local = 1 AND hdrs.is_primary_replica = 0)
        OR (sys.fn_hadr_is_primary_replica (sdb.name) = 1 AND DATABASEPROPERTYEX (sdb.name, 'Updateability') = 'READ_ONLY')
    ),
    TABLE1 as (
            SELECT dbs.database_id as DatabaseId, sysdbs.name as DatabaseName, 'OPTOUT' as Reason,
            CASE WHEN dbs.database_name = sysdbs.name THEN NULL ELSE dbs.database_name END AS DatabaseNameOnPitrTable
            FROM msdb.dbo.rds_pitr_blocked_databases dbs
            INNER JOIN sys.databases sysdbs ON dbs.database_id = sysdbs.database_id
            WHERE sysdbs.database_id > 4
            ),
    TABLE2 as (
            SELECT
            db.name AS DatabaseName,
            db.create_date AS CreateDate,
            db.state_desc AS DatabaseState,
            db.database_id AS DatabaseId,
            rs.database_guid AS DatabaseGuid,
            rs.last_log_backup_lsn AS LastLogBackupLSN,
            rs.recovery_fork_guid RecoveryForkGuid,
            rs.first_recovery_fork_guid AS FirstRecoveryForkGuid,
            db.recovery_model_desc AS RecoveryModel,
            db.is_auto_close_on AS IsAutoClose,
            db.is_read_only as IsReadOnly,
            NEWID() as FileName,
            CASE WHEN(db.state_desc = 'ONLINE'
                    AND db.recovery_model_desc != 'SIMPLE'
                    AND((db.is_auto_close_on = 0 and db.collation_name IS NOT NULL) OR db.is_auto_close_on = 1))
                    AND db.is_read_only != 1
                    AND db.user_access = 0
                    AND db.source_database_id IS NULL
                    AND db.is_in_standby != 1
                    THEN 1 ELSE 0 END AS IsPartOfSnapshot,
            CASE WHEN db.source_database_id IS NULL THEN 0 ELSE 1 END AS IsDatabaseSnapshot
            FROM sys.databases db
            INNER JOIN sys.database_recovery_status rs
            ON db.database_id = rs.database_id
            WHERE DB_NAME(db.database_id) NOT IN('tempdb') AND
            db.database_id NOT IN (SELECT DISTINCT DatabaseId FROM TABLE1) AND
            db.database_id NOT IN (SELECT DISTINCT DatabaseId FROM TABLE0)
        ),
        TABLE3 as(
            Select @Limit+count(DatabaseName) as TotalNumberOfDatabases from TABLE2 where TABLE2.IsPartOfSnapshot=1 and DatabaseName in ('master','model','msdb')
        )
        SELECT TOP(SELECT TotalNumberOfDatabases from TABLE3)  DatabaseName,CreateDate,DatabaseState,DatabaseId from TABLE2 where TABLE2.IsPartOfSnapshot=1
        ORDER BY TABLE2.DatabaseID ASC
ELSE
    WITH TABLE0 AS (
        SELECT hdrs.database_id as DatabaseId, sdb.name as DatabaseName, 'ALWAYS_ON_NOT_WRITABLE_REPLICA' as Reason, NULL as DatabaseNameOnPitrTable
        FROM sys.dm_hadr_database_replica_states hdrs
        INNER JOIN sys.databases sdb ON sdb.database_id = hdrs.database_id
        WHERE (hdrs.is_local = 1 AND hdrs.is_primary_replica = 0)
        OR (sys.fn_hadr_is_primary_replica (sdb.name) = 1 AND DATABASEPROPERTYEX (sdb.name, 'Updateability') = 'READ_ONLY')
    ),
    TABLE1 as (
            SELECT
            db.name AS DatabaseName,
            db.create_date AS CreateDate,
            db.state_desc AS DatabaseState,
            db.database_id AS DatabaseId,
            rs.database_guid AS DatabaseGuid,
            rs.last_log_backup_lsn AS LastLogBackupLSN,
            rs.recovery_fork_guid RecoveryForkGuid,
            rs.first_recovery_fork_guid AS FirstRecoveryForkGuid,
            db.recovery_model_desc AS RecoveryModel,
            db.is_auto_close_on AS IsAutoClose,
            db.is_read_only as IsReadOnly,
            NEWID() as FileName,
            CASE WHEN(db.state_desc = 'ONLINE'
                    AND db.recovery_model_desc != 'SIMPLE'
                    AND((db.is_auto_close_on = 0 and db.collation_name IS NOT NULL) OR db.is_auto_close_on = 1))
                    AND db.is_read_only != 1
                    AND db.user_access = 0
                    AND db.source_database_id IS NULL
                    AND db.is_in_standby != 1
                    THEN 1 ELSE 0 END AS IsPartOfSnapshot,
            CASE WHEN db.source_database_id IS NULL THEN 0 ELSE 1 END AS IsDatabaseSnapshot
            FROM sys.databases db
            INNER JOIN sys.database_recovery_status rs
            ON db.database_id = rs.database_id
            WHERE DB_NAME(db.database_id) NOT IN('tempdb') AND
            db.database_id NOT IN (SELECT DISTINCT DatabaseId FROM TABLE0)
        ),
        TABLE2 as(
            SELECT @Limit+count(DatabaseName) as TotalNumberOfDatabases from TABLE1 where TABLE1.IsPartOfSnapshot=1 and DatabaseName in ('master','model','msdb')
        )
        select top(select TotalNumberOfDatabases from TABLE2)  DatabaseName,CreateDate,DatabaseState,DatabaseId from TABLE1 where TABLE1.IsPartOfSnapshot=1
        ORDER BY TABLE1.DatabaseID ASC

```

###### Note

The databases that are only symbolic links are also excluded from databases eligible for PITR operations.
The above query doesn’t filter based on this criteria.

## Transaction logs in Amazon S3

The backup retention period determines whether transaction logs for RDS Custom for SQL Server DB instances are automatically extracted
and uploaded to Amazon S3. A nonzero value means that automatic backups are created, and that the RDS Custom agent uploads the
transaction logs to S3 every 5 minutes.

Transaction log files on S3 are encrypted at rest using the AWS KMS key
that you provided when you created your DB instance. For more information, see
[Protecting data using server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in
the _Amazon Simple Storage Service User Guide_.

The transaction logs for each database are uploaded to an S3 bucket named
`do-not-delete-rds-custom-`$ACCOUNT_ID`-`$REGION`-`unique_identifier``.
 The `RDSCustomForSQLServer/Instances/`DB_instance_resource_ID`` directory in
the S3 bucket contains two subdirectories:

- `TransactionLogs` – Contains the transaction logs for each database and their
  respective metadata.

The transaction log file name follows the pattern
``yyyyMMddHHmm`.`database_id`.`timestamp``,
for example:

```
202110202230.11.1634769287
```

The same file name with the suffix `_metadata` contains information about the transaction log
such as log sequence numbers, database name, and
`RdsChunkCount`. `RdsChunkCount` determines
how many physical files represent a single transaction log file. You
might see files with suffixes `_0001`,
`_0002`, and so on, which mean the physical
chunks of a transaction log file. If you want to use a chunked
transaction log file, make sure to merge the chunks after downloading
them.

Consider a scenario where you have the following files:

    + `202110202230.11.1634769287`
    + `202110202230.11.1634769287_0001`
    + `202110202230.11.1634769287_0002`
    + `202110202230.11.1634769287_metadata`

The `RdsChunkCount` is `3`. The order for merging the files is the following: `202110202230.11.1634769287`, `202110202230.11.1634769287_0001`, `202110202230.11.1634769287_0002`.

- `TransactionLogMetadata` – Contains metadata information about each iteration of
  transaction log extraction.

The `RI.End` file contains information for all databases that had their transaction logs
extracted, and all databases that exist but didn't have their transaction logs extracted. The
`RI.End` file name follows the pattern
``yyyyMMddHHmm`.RI.End.`timestamp``,
for example:

```
202110202230.RI.End.1634769281
```

## PITR Restore using the AWS Management Console, the AWS CLI, or the RDS API.

You can restore an RDS Custom for SQL Server DB instance to a point in time using the AWS Management Console, the AWS CLI, or the RDS API.

###### To restore an RDS Custom DB instance to a specified time

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Automated backups**.
3. Choose the RDS Custom DB instance that you want to restore.
4. For **Actions**, choose **Restore to point in time**.

The **Restore to point in time** window appears. 5. Choose **Latest restorable time** to restore to the latest possible time, or choose
**Custom** to choose a time.

If you chose **Custom**, enter the date and time to which you want to restore the
instance.

Times are shown in your local time zone, which is indicated by an offset from Coordinated Universal Time
(UTC). For example, UTC-5 is Eastern Standard Time/Central Daylight Time. 6. For **DB instance identifier**, enter the name of the target restored RDS Custom DB
instance. The name must be unique. 7. Choose other options as needed, such as DB instance class. 8. Choose **Restore to point in time**.
You restore a DB instance to a specified time by using the [restore-db-instance-to-point-in-time](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md")
AWS CLI command to create a new RDS Custom DB instance.

Use one of the following options to specify the backup to restore from:

- `--source-db-instance-identifier `mysourcedbinstance``
- `--source-dbi-resource-id `dbinstanceresourceID``
- `--source-db-instance-automated-backups-arn `backupARN``The`custom-iam-instance-profile` option is required.

The following example restores `my-custom-db-instance` to a new DB instance
named `my-restored-custom-db-instance`, as of the specified time.

###### Example

For Linux, macOS, or Unix:

```
aws rds restore-db-instance-to-point-in-time \
    --source-db-instance-identifier `my-custom-db-instance`\
    --target-db-instance-identifier `my-restored-custom-db-instance` \
    --custom-iam-instance-profile `AWSRDSCustomInstanceProfileForRdsCustomInstance` \
    --restore-time `2022-10-14T23:45:00.000Z`
```

For Windows:

```
aws rds restore-db-instance-to-point-in-time ^
    --source-db-instance-identifier `my-custom-db-instance` ^
    --target-db-instance-identifier `my-restored-custom-db-instance` ^
    --custom-iam-instance-profile `AWSRDSCustomInstanceProfileForRdsCustomInstance` ^
    --restore-time `2022-10-14T23:45:00.000Z`
```
