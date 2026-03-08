# Backup and restore design

This topic provides reference content comparing backup and recovery features between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can gain insight into how these two database systems handle critical data protection tasks.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                         | Key differences                           |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| Four star feature compatibility | No automation                      | [Backup](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.backup "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.backup") | Amazon RDS manages storage-level backups. |

## SQL Server Usage

The term _backup_ refers to both the process of copying data and to the resulting set of data created by the processes that copy data for safekeeping and disaster recovery. Backup processes copy SQL Server data and transaction logs to media such as tapes, network shares, cloud storage, or local files. You can then copy these backups back to the database using a _restore_ process.

SQL Server uses files, or filegroups, to create backups for an individual database or subset of a database. Table backups aren’t supported.

When a database uses the `FULL` recovery model, transaction logs also need to be backed up. Use transaction logs to back up only database changes since the last full backup and provide a mechanism for point-in-time restore operations.

Recovery model is a database-level setting that controls transaction log management. The three available recovery models are `SIMPLE`, `FULL`, and `BULK LOGGED`. For more information, see [Recovery Models (SQL Server)](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server?view=sql-server-ver15") in the _SQL Server documentation_.

The SQL Server `RESTORE` process copies data and log pages from a previously created backup back to the database. It then triggers a recovery process that rolls forward all committed transactions not yet flushed to the data pages when the backup took place. It also rolls back all uncommitted transactions written to the data files.

SQL Server supports the following types of backups:

- **Copy-only backups** are independent of the standard chain of SQL Server backups. They are typically used as one-off backups for special use cases and don’t interrupt normal backup operations.
- **Data backups** copy data files and the transaction log section of the activity during the backup. A data backup may contain the whole database (Database Backup) or part of the database. The parts can be a partial backup or a file or filegroup.
- **A database backup** is a data backup representing the entire database at the point in time when the backup process finished.
- **A differential backup** is a data backup containing only the data structures (extents) modified since the last full backup. A differential backup is dependent on the previous full backup and can’t be used alone.
- **A full backup** is a data backup containing a Database Backup and the transaction log records of the activity during the backup process.
- **Transaction log backups** don’t contain data pages. They contain the log pages for all transaction activity since the last Full Backup or the previous transaction log backup.
- **File backups** consist of one or more files or filegroups.

SQL Server also supports media families and media sets that you can use to mirror and stripe backup devices. For more information, see [Media Sets, Media Families, and Backup Sets](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/media-sets-media-families-and-backup-sets-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/media-sets-media-families-and-backup-sets-sql-server?view=sql-server-ver15") in the _SQL Server documentation_.

SQL Server 2008 Enterprise edition and later versions support backup compression. Backup compression provides the benefit of a smaller backup file footprint, less I/O consumption, and less network traffic at the expense of increased CPU utilization for running the compression algorithm. For more information, see [Backup Compression](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-compression-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-compression-sql-server?view=sql-server-ver15") in the _SQL Server documentation_.

A database backed up in the `SIMPLE` recovery mode can only be restored from a full or differential backup. For `FULL` and `BULK LOGGED` recovery models, transaction log backups can be restored also to minimize potential data loss.

Restoring a database involves maintaining a correct sequence of individual backup restores. For example, a typical restore operation may include the following steps:

1. Restore the most recent full backup.
2. Restore the most recent differential backup.
3. Restore a set of uninterrupted transaction log backups, in order.
4. Recover the database.

For large databases, a full restore, or a complete database restore, from a full database backup isn’t always a practical solution. SQL Server supports data file restore that restores and recovers a set of files and a single data page restore, except for databases that use the `SIMPLE` recovery model.

### Syntax

The following code examples demonstrate the backup syntax.

```
Backing Up a Whole Database
BACKUP DATABASE <Database Name> [ <Files / Filegroups> ] [ READ_WRITE_FILEGROUPS ]
    TO <Backup Devices>
    [ <MIRROR TO Clause> ]
    [ WITH [DIFFERENTIAL ]
    [ <Option List> ][;]
```

```
BACKUP LOG <Database Name>
    TO <Backup Devices>
    [ <MIRROR TO clause> ]
    [ WITH <Option List> ][;]
```

```
<Option List> =
COPY_ONLY | {COMPRESSION | NO_COMPRESSION } | DESCRIPTION = <Description>
| NAME = <Backup Set Name> | CREDENTIAL | ENCRYPTION | FILE_SNAPSHOT | { EXPIREDATE =
<Expiration Date> | RETAINDAYS = <Retention> }
{ NOINIT | INIT } | { NOSKIP | SKIP } | { NOFORMAT | FORMAT } |
{ NO_CHECKSUM | CHECKSUM } | { STOP_ON_ERROR | CONTINUE_AFTER_ERROR }
{ NORECOVERY | STANDBY = <Undo File for Log Shipping> } | NO_TRUNCATE
ENCRYPTION ( ALGORITHM = <Algorithm> | SERVER CERTIFICATE = <Certificate> | SERVER
ASYMMETRIC KEY = <Key> );
```

The following code examples demonstrate the restore syntax.

```
RESTORE DATABASE <Database Name> [ <Files / Filegroups> ] | PAGE = <Page ID>
FROM <Backup Devices>
[ WITH [ RECOVERY | NORECOVERY | STANDBY = <Undo File for Log Shipping> } ]
[, <Option List>]
[;]
```

```
RESTORE LOG <Database Name> [ <Files / Filegroups> ] | PAGE = <Page ID>
[ FROM <Backup Devices>
[ WITH [ RECOVERY | NORECOVERY | STANDBY = <Undo File for Log Shipping> } ]
[, <Option List>]
[;]
```

```
<Option List> =
MOVE <File to Location>
| REPLACE | RESTART | RESTRICTED_USER | CREDENTIAL
| FILE = <File Number> | PASSWORD = <Password>
| { CHECKSUM | NO_CHECKSUM } | { STOP_ON_ERROR | CONTINUE_AFTER_ERROR }
| KEEP_REPLICATION | KEEP_CDC
| { STOPAT = <Stop Time>
| STOPATMARK = <Log Sequence Number>
| STOPBEFOREMARK = <Log Sequence Number>
```

### Examples

Perform a full compressed database backup.

```
BACKUP DATABASE MyDatabase TO DISK='C:\Backups\MyDatabase\FullBackup.bak'
WITH COMPRESSION;
```

Perform a log backup.

```
BACKUP DATABASE MyDatabase TO DISK='C:\Backups\MyDatabase\LogBackup.bak'
WITH COMPRESSION;
```

Perform a partial differential backup.

```
BACKUP DATABASE MyDatabase
    FILEGROUP = 'FileGroup1',
    FILEGROUP = 'FileGroup2'
    TO DISK='C:\Backups\MyDatabase\DB1.bak'
    WITH DIFFERENTIAL;
```

Restore a database to a point in time.

```
RESTORE DATABASE MyDatabase
    FROM DISK='C:\Backups\MyDatabase\FullBackup.bak'
    WITH NORECOVERY;

RESTORE LOG AdventureWorks2012
    FROM DISK='C:\Backups\MyDatabase\LogBackup.bak'
    WITH NORECOVERY, STOPAT = '20180401 10:35:00';

RESTORE DATABASE AdventureWorks2012 WITH RECOVERY;
```

For more information, see [Backup Overview](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-overview-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-overview-sql-server?view=sql-server-ver15") and [Restore and Recovery Overview](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-and-recovery-overview-sql-server?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-and-recovery-overview-sql-server?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) continuously backs up all cluster volumes and retains restore data for the duration of the backup retention period. The backups are incremental and can be used to restore the cluster to any point in time within the backup retention period. You can specify a backup retention period from one to 35 days when creating or modifying a database cluster. Backups incur no performance impact and don’t cause service interruptions.

Additionally, you can manually trigger data snapshots in a cluster volume that can be saved beyond the retention period. You can use Snapshots to create new database clusters.

###### Note

Manual snapshots incur storage charges for Amazon Relational Database Service (Amazon RDS).

###### Note

Starting from Amazon RDS 8.0.21, you can turn on and turn off redo logging using the `ALTER INSTANCE {ENABLE|DISABLE} INNODB REDO_LOG` syntax. This functionality is intended for loading data into a new MySQL instance. Disabling redo logging helps speed up data loading by avoiding redo log writes. The new `INNODB_REDO_LOG_ENABLE` privilege permits enabling and disabling redo logging. The new `Innodb_redo_log_enabled` status variable permits monitoring redo logging status. For more information, see [Disabling Redo Logging](https://dev.mysql.com/doc/refman/8.0/en/innodb-redo-log.html#innodb-disable-redo-logging "https://dev.mysql.com/doc/refman/8.0/en/innodb-redo-log.html#innodb-disable-redo-logging") in the _MySQL documentation_.

### Restoring Data

You can recover databases from Amazon Aurora automatically retained data or from a manually saved snapshot. Using the automatically retained data significantly reduces the need to take frequent snapshots and maintain Recovery Point Objective (RPO) policies.

The Amazon RDS console displays the available time frame for restoring database instances in the Latest Restorable Time and Earliest Restorable Time fields. The Latest Restorable Time is typically within the last five minutes. The Earliest Restorable Time is the end of the backup retention period.

###### Note

The Latest Restorable Time and Earliest Restorable Time fields display when a database cluster restore has been completed. Both display NULL until the restore process completes.

### Restoring Database Backups from Amazon S3

You can now restore MySQL 5.7 backups stored on Amazon S3 to Amazon Aurora MySQL-Compatible Edition and Amazon RDS for MySQL.

If you are migrating a MySQL 5.5, 5.6, or 5.7 database to Amazon Aurora MySQL-Compatible Edition or Amazon RDS for MySQL, you can copy database backups to an Amazon S3 bucket and restore them for a faster migration. Both full and incremental backups of your database can be restored. Restoring backups can be considerably quicker than moving data using the mysqldump utility, which replays SQL statements to recreate the database.

For more information, see [Restoring a backup into a MySQL DB instance](../../../AmazonRDS/latest/UserGuide/MySQL.Procedural.md "../../../AmazonRDS/latest/UserGuide/MySQL.Procedural.md") in the _Amazon Relational Database Service User Guide_.

### Backtracking an Aurora DB Cluster

With Amazon Aurora with MySQL compatibility, you can backtrack a DB cluster to a specific time, without restoring data from a backup.

Backtracking rewinds the DB cluster to the time you specify. Backtracking isn’t a replacement for backing up your DB cluster so that you can restore it to a point in time. However, backtracking provides the following advantages over traditional backup and restore:

- You can easily undo mistakes. If you mistakenly perform a destructive action, such as a DELETE without a WHERE clause, you can backtrack the DB cluster to a time before the destructive action with minimal interruption of service.
- You can backtrack a DB cluster quickly. Restoring a DB cluster to a point in time launches a new DB cluster and restores it from backup data or a DB cluster snapshot, which can take hours. Backtracking a DB cluster doesn’t require a new DB cluster and rewinds the DB cluster in minutes.
- You can explore earlier data changes. You can repeatedly backtrack a DB cluster back and forth in time to help determine when a particular data change occurred. For example, you can backtrack a DB cluster three hours and then backtrack forward in time one hour. In this case, the backtrack time is two hours before the original time.

For additional information, see [Backtracking an Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.md") in the _User Guide for Aurora_.

### Database Cloning

Database cloning is a fast and cost-effective way to create copies of a database. You can create multiple clones from a single DB cluster and additional clones can be created from existing clones. When first created, a cloned database requires only minimal additional storage space.

Database cloning uses a copy-on-write protocol. Data is copied only when it changes either on the source or cloned database.

Data cloning is useful for avoiding impacts on production databases. For example:

- Testing schema or parameter group modifications.
- Isolating intensive workloads. For example, exporting large amounts of data and running high resource consuming queries.
- Development and testing with a copy of a production database.

### Copying and Sharing Snapshots

You can copy and share database snapshots within the same AWS Region, across AWS Regions, and across AWS accounts. Snapshot sharing provides an authorized AWS account with access to snapshots. Authorized users can restore a snapshot from its current location without first copying it.

Copying an automated snapshot to another AWS account requires two steps:

1. Create a manual snapshot from the automated snapshot.
2. Copy the manual snapshot to another account.

### Backup Storage

In all Amazon RDS regions, backup storage is the collection of both automated and manual snapshots for all database instances and clusters. The size of this storage is the sum of all individual instance snapshots.

When an Aurora MySQL database instance is deleted, all automated backups of that database instance are also deleted. However, Amazon RDS provides the option to create a final snapshot before deleting a database instance. This final snapshot is retained as a manual snapshot. Manual snapshots aren’t automatically deleted.

### The Backup Retention Period

Retention periods for Aurora MySQL DB cluster backups are configured when creating a cluster. If not explicitly set, the default retention is one day when using the Amazon RDS API or the AWS CLI. The retention period is seven days if using the AWS Console. You can modify the backup retention period at any time with a value between one and 35 days.

### Disabling Automated Backups

You can’t turn off automated backups on Aurora MySQL. The backup retention period for Aurora MySQL is managed by the database cluster.

### Saving Data from an Amazon Aurora MySQL Database to Amazon S3

Aurora MySQL supports a proprietary syntax for dumping and loading data directly from and to an Amazon S3 bucket.

You can use the `SELECT …​ INTO OUTFILE S3` statement to export data out of Aurora MySQL. Also, you can use the `LOAD DATA FROM S3` statement for loading data directly from Amazon S3 text files.

###### Note

This integration enables very efficient dumps since there is no need for an intermediate client application to handle the data export, import, and save.

The syntax for the `SELECT …​ INTO OUTFILE S3` statement is shown following:

```
SELECT
    [ALL | DISTINCT | DISTINCTROW ]
        [HIGH_PRIORITY]
        [STRAIGHT_JOIN]
        [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
        [SQL_CACHE | SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
    select_expr [, select_expr ...]
    [FROM table_references
        [PARTITION partition_list]
    [WHERE where_condition]
    [GROUP BY {col_name | expr | position}
        [ASC | DESC], ... [WITH ROLLUP]]
    [HAVING where_condition]
    [ORDER BY {col_name | expr | position}
        [ASC | DESC], ...]
    [LIMIT {[offset,] row_count | row_count OFFSET offset}]
    [PROCEDURE procedure_name(argument_list)]
INTO OUTFILE S3 'S3-URI'
[CHARACTER SET charset_name]
    [export_options]
    [MANIFEST {ON | OFF}]
    [OVERWRITE {ON | OFF}]

export_options:
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]
```

The syntax for the `LOAD DATA FROM S3` statement is shown following:

```
LOAD DATA FROM S3 [FILE | PREFIX | MANIFEST] 'S3-URI'
    [REPLACE | IGNORE]
    INTO TABLE tbl_name
    [PARTITION (partition_name,...)]
    [CHARACTER SET charset_name]
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]
    [IGNORE number {LINES | ROWS}]
    [(col_name_or_user_var,...)]
    [SET col_name = expr,...]
```

For more information, see [Loading data into an Amazon Aurora MySQL DB cluster from text files in an Amazon S3 bucket](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md") in the _User Guide for Aurora_.

As you can see from the syntax, Aurora MySQL offers various options for easy control of saving and loading data directly from an SQL statement without needing to configure options or external services.

The `MANIFEST` option of the export allows you to create an accompanying JSON file that lists the text files created by the `SELECT …​ INTO OUTFILE S3` statement. Later, the `LOAD DATA FROM S3` statement can use this manifest to load the data files back into the database tables.

### Migration Considerations

Migrating from a self-managed backup policy to a Platform as a Service (PaaS) environment such as Aurora MySQL is a complete paradigm shift. You no longer need to worry about transaction logs, file groups, disks running out of space, and purging old backups.

Amazon RDS provides guaranteed continuous backup with point-in-time restore up to 35 days.

Managing an SQL Server backup policy with similar RTO and RPO is a challenging task. With Aurora MySQL, all you need to do set is the retention period and take manual snapshots for special use cases.

### Considerations for Exporting Data to Amazon S3

By default, each file created in an Amazon S3 bucket as a result of the export has a maximal size of 6 GB. The system rolls over to a new file once this limit is exceeded. However, Aurora MySQL guarantees that rows will not span multiple files, and therefore slight variations from this max size are possible.

The `SELECT …​ INTO OUTFILE S3` statement is an atomic transaction. Large or complicated `SELECT` statements may take a significant amount of time to complete. In the event of an error, the statement rolls back and should be ran again. However, if some of the data has already been uploaded to the Amazon S3 bucket, it isn’t deleted as part of the rollback and you can use a differential approach to upload only the remaining data.

###### Note

For exports larger than 25 GB, AWS recommends to split the `SELECT …​ INTO OUTFILE S3` statement into multiple, smaller batches.

Metadata, such as table schema or file metadata, isn’t uploaded by Aurora MySQL to Amazon S3.

### Example — Change the Retention Policy to Seven Days

The following walkthrough describes how to change Aurora MySQL DB cluster retention settings from one day to seven days using the Amazon RDS console.

1. Log in to your [Management Console](https://eu-central-1.console.aws.amazon.com/rds/home?#databases: "https://eu-central-1.console.aws.amazon.com/rds/home?#databases:"), choose **Amazon RDS** , and then choose **Databases**.
2. Choose the relevant DB identifier.
3. Verify the current automatic backup settings.
4. Select the database instance with the writer role and choose **Modify**.
5. Scroll down to the **Backup** section. Select **7 Days** from the list.
6. Choose **Continue**, review the summary, select if to use scheduled maintenance window or to apply immediate and choose **Modify DB instance**.

For more information, see [Maintenance Plans](chap-sql-server-aurora-mysql.management.md "chap-sql-server-aurora-mysql.management.md").

### Exporting Data to Amazon S3

For a detailed example with all the necessary preliminary steps required to export data from Aurora MySQL to an Amazon S3 bucket, see [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3 bucket](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md") in the _User Guide for Aurora_.

## Summary

| Feature                      | SQL Server                                            | Aurora MySQL                                              | Comments                                                                                                                                                                                                                                  |
| ---------------------------- | ----------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| Recovery model               | `SIMPLE`, `BULK LOGGED`, `FULL`                       | N/A                                                       | The functionality of Aurora MySQL backups is equivalent to the `FULL` recovery model.                                                                                                                                                     |
| Backup database              | `BACKUP DATABASE`                                     | Automatic and continuous                                  |                                                                                                                                                                                                                                           |
| Partial backup               | ```<br>BACKUP DATABASE<br>...<br>FILE= ...            | <br>FILEGROUP = ...<br>```                                | N/A                                                                                                                                                                                                                                       |     |
| Log backup                   | `BACKUP LOG`                                          | N/A                                                       | Backup is at the storage level.                                                                                                                                                                                                           |
| Differential Backups         | `<br>BACKUP DATABASE<br>...<br>WITH DIFFERENTIAL<br>` | N/A                                                       |                                                                                                                                                                                                                                           |
| Database snapshots           | `<br>BACKUP DATABASE<br>...<br>WITH COPY_ONLY<br>`    | Amazon RDS console or API                                 | The terminology is inconsistent between SQL Server and Aurora MySQL. A database snapshot in SQL Server is similar to database cloning in Aurora MySQL. Aurora MySQL database snapshots are similar to a `COPY_ONLY` backup in SQL Server. |
| Database clones              | `<br>CREATE<br>DATABASE...<br>AS SNAPSHOT OF...<br>`  |                                                           | The terminology is inconsistent between SQL Server and Aurora MySQL. A database snapshot in SQL Server is similar to database cloning in Aurora MySQL. Aurora MySQL database snapshots are similar to a `COPY_ONLY` backup in SQL Server. |
| Point in time restore        | ```<br>RESTORE DATABASE                               | LOG ... WITH<br>STOPAT...<br>```                          | Any point within the retention period using the Amazon RDS console or API                                                                                                                                                                 |     |
| Partial restore              | ```<br>RESTORE DATABASE...<br>FILE= ...               | <br>FILEGROUP = ...<br>```                                | N/A                                                                                                                                                                                                                                       |     |
| Export and import table data | DTS, SSIS, BCP, linked servers to files               | `<br>SELECT INTO ... OUTFILE S3<br>LOAD DATA FROM S3<br>` |                                                                                                                                                                                                                                           |

For more information, see [Overview of backing up and restoring an Aurora DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.md") and [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3 bucket](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md") in the _User Guide for Aurora_.
