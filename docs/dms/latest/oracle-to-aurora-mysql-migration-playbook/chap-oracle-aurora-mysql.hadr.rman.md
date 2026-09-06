

# Oracle Recovery Manager and Amazon RDS snapshots
<a name="chap-oracle-aurora-mysql.hadr.rman"></a>

With AWS DMS, you can migrate data from Oracle databases by using Oracle Recovery Manager (RMAN) backup sets or Amazon RDS snapshots. Oracle Recovery Manager is a utility for backing up, restoring, and recovering Oracle databases. Amazon RDS snapshots capture the entire database instance, including transaction logs, at a specific point in time.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  | N/A | N/A | Storage-level backup managed by Amazon RDS. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.hadr.rman.oracle"></a>

Oracle Recovery Manager (RMAN) is a primary backup and recovery tool in Oracle. It provides its own scripting syntax and can be used to take full or incremental backups of an Oracle database. The following list identifies the types of backups.
+  **Full RMAN backup** — Creates a full backup of an entire database or individual Oracle data files. For example, a level 0 full backup.
+  **Differential incremental RMAN backup** — Performs a backup of all database blocks that have changed from the previous level 0 or 1 backup.
+  **Cumulative incremental RMAN backup** — Perform a backup all of blocks that have changed from the previous level 0 backup.

RMAN supports online backups of an Oracle database if it has been configured to run in Archived Log Mode.

RMAN backs up the following files:
+ Database data files.
+ Database control file.
+ Database parameter file.
+ Database Archived Redo Logs.

### Examples
<a name="chap-oracle-aurora-mysql.hadr.rman.oracle.examples"></a>

Use the RMAN CLI to connect to an Oracle database.

```
export ORACLE_SID=ORCL
rman target=/
```

Perform a full backup of the database and the database archived redo logs.

```
BACKUP DATABASE PLUS ARCHIVELOG;
```

Perform an incremental level 0 or level 1 backup of the database.

```
BACKUP INCREMENTAL LEVEL 0 DATABASE;
BACKUP INCREMENTAL LEVEL 1 DATABASE;
```

Restore a database.

```
RUN {
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
RESTORE DATABASE;
RECOVER DATABASE;
ALTER DATABASE OPEN;
}
```

Restore a specific pluggable database (Oracle 12c).

```
RUN {
ALTER PLUGGABLE DATABASE pdbA, pdbB CLOSE;
RESTORE PLUGGABLE DATABASE pdbA, pdbB;
RECOVER PLUGGABLE DATABASE pdbA, pdbB;
ALTER PLUGGABLE DATABASE pdbA, pdbB OPEN;
}
```

Restore a database to a specific point in time.

```
RUN {
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
SET UNTIL TIME "TO_DATE('20-SEP-2017 21:30:00','DD-MON-YYYY HH24:MI:SS')";
RESTORE DATABASE;
RECOVER DATABASE;
ALTER DATABASE OPEN RESETLOGS;
}
```

List all current database backups created with RMAN.

```
LIST BACKUP OF DATABASE;
```

For more information, see [Backup and Recovery User Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/index.html) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.hadr.rman.mysql"></a>

Snapshots are the primary backup mechanism for Amazon Aurora databases. They are extremely fast and nonintrusive. You can take snapshots using the Amazon RDS Management Console or the AWS CLI. Unlike RMAN, there is no need for incremental backups. You can choose to restore your database to the exact time when a snapshot was taken or to any other point in time.

 Amazon Aurora provides the following types of backups:
+  **Automated backups** — Always enabled on Amazon Aurora. They do not impact database performance.
+  **Manual backups** — You can create a snapshot at any time. There is no performance impact when taking snapshots of an Aurora database. Restoring data from snapshots requires creation of a new instance. Up to 100 manual snapshots are supported for each database.

**Note**  
In Amazon Relational Database Service (Amazon RDS) for MySQL version 8.0.21, you can turn on or off the redo logging option using the `ALTER INSTANCE {ENABLE|DISABLE} INNODB REDO_LOG` syntax. This functionality is intended for loading data into a new MySQL instance. Turning off the redo logging option helps speed up data loading by avoiding redo log writes. The new `INNODB_REDO_LOG_ENABLE` privilege permits turning on and turning off the redo logging option. The new `Innodb_redo_log_enabled` status variable permits monitoring redo logging status. For more information, see [Disabling Redo Logging](https://dev.mysql.com/doc/refman/8.0/en/innodb-redo-log.html#innodb-disable-redo-logging) in the *MySQL documentation*.

### Examples
<a name="chap-oracle-aurora-mysql.hadr.rman.mysql.examples"></a>

For examples, see [MySQL Snapshots](chap-oracle-aurora-mysql.hadr.flashback.md#chap-oracle-aurora-mysql.hadr.flashback.mysql).

## Summary
<a name="chap-oracle-aurora-mysql.hadr.rman.summary"></a>


| Description | Oracle |  Amazon Aurora  | 
| --- | --- | --- | 
| Scheduled backups | Create the `DBMS_SCHEDULER` job that will run your RMAN script on a scheduled basis. | Automatic | 
| Manual full database backups |  <pre>BACKUP DATABASE PLUS ARCHIVELOG;</pre>  | Use Amazon RDS dashboard or the AWS CLI command to take a snapshot on the cluster.<pre>aws rds create-db-cluster-snapshot<br />  --dbcluster-snapshot-identifier Snapshot_name<br />  --db-cluster-identifier Cluster_Name</pre> | 
| Restore database |  <pre>RUN<br />{<br />SHUTDOWN IMMEDIATE;<br />STARTUP MOUNT;<br />RESTORE DATABASE;<br />RECOVER DATABASE;<br />ALTER DATABASE OPEN;<br />}</pre>  | Create new cluster from a cluster snapshot.<pre>aws rds restore-db-cluster-from-snapshot<br />  --db-cluster-identifier NewCluster<br />  --snapshotidentifier SnapshotToRestore<br />  --engine aurora-mysql</pre><br />Add a new instance to the new/restored cluster.<pre>aws rds create-db-instance<br />  --region useast-1<br />  --db-subnet-group default<br />  --engine aurora-mysql<br />  --db-cluster-identifier clustername-restore<br />  --db-instance-identifier newinstance-nodeA<br />  --db-instance-class db.r4.large</pre> | 
| Incremental differential |  <pre>BACKUP INCREMENTAL LEVEL 0<br />DATABASE;<br />BACKUP INCREMENTAL LEVEL 1<br />DATABASE;</pre>  | N/A | 
| Incremental cumulative |  <pre>BACKUP INCREMENTAL LEVEL 0<br />CUMULATIVE DATABASE;<br />BACKUP INCREMENTAL LEVEL 1<br />CUMULATIVE DATABASE;</pre>  | N/A | 
| Restore a database to a specific point in time |  <pre>RUN {<br />  SHUTDOWN IMMEDIATE;<br />  STARTUP MOUNT;<br />  SET UNTIL TIME "TO_DATE(<br />    '19-SEP-2017 23:45:00',<br />    'DD-MON-YYYY HH24:MI:SS')";<br />  RESTORE DATABASE;<br />  RECOVER DATABASE;<br />  ALTER DATABASE<br />  OPEN RESETLOGS;<br />}</pre>  | Create a new cluster from a cluster snapshot by given custom time to restore.<pre>aws rds restore-db-cluster-to-point-in-time<br />  --db-cluster-identifier clustername-restore<br />  --source-db-cluster-identifier clustername<br />  --restore-to-time 2017-09-19T23:45:00.000Z</pre><br />Add a new instance to the new or restored cluster.<pre>aws rds create-db-instance<br />  --region useast-1<br />  --db-subnet-group default<br />  --engine aurora-mysql<br />  --db-cluster-identifier clustername-restore<br />  --db-instance-identifier newinstance-nodeA<br />  --db-instance-class db.r4.large</pre> | 
| Backup database archive logs |  <pre>BACKUP ARCHIVELOG ALL;</pre>  | N/A | 
| Delete old database archive logs |  <pre>CROSSCHECK BACKUP;<br />DELETE EXPIRED BACKUP;</pre>  | N/A | 
| Restore a single pluggable database (12c) |  <pre>RUN {<br />  ALTER PLUGGABLE DATABASE pdb1, pdb2 CLOSE;<br />  RESTORE PLUGGABLE DATABASE pdb1, pdb2;<br />  RECOVER PLUGGABLE DATABASE pdb1, pdb2;<br />  ALTER PLUGGABLE DATABASE pdb1, pdb2<br />  OPEN;<br />}</pre>  | Create new cluster from a cluster snapshot.<pre>aws rds restore-db-cluster-from-snapshot<br />  --db-cluster-identifier NewCluster<br />  --snapshotidentifier SnapshotToRestore<br />  --engine aurora-mysql</pre><br />Add a new instance to the new or restored cluster.<pre>aws rds create-db-instance<br />  --region useast-1<br />  --db-subnet-group default<br />  --engine aurora-mysql<br />  --db-cluster-identifier clustername-restore<br />  --db-instance-identifier newinstance-nodeA<br />  --db-instance-class db.r4.large</pre><br />Use mysqldump and mysql to copy the database to the original instance.<pre>mysqldump --column-statistics=0<br />    DATABASE_TO_RESTORE<br />    -h RESTORED_INSTANCE_ENDPOINT<br />    -P 3306 -u USER_NAME<br />    -p > /local_path/backup-file.sql</pre><pre>mysql DB_NAME<br />    -h MYSQL_INSTANCE_ENDPOINT<br />    -P 3306 -u USER_NAME<br />    -p < /local_path/backup-file.sql</pre> In Amazon RDS for MySQL version 8.0, make sure that the `column_statistics` flag set to 0 if you use binaries when running the mysqldump.  | 

For more information, see [mysqldump — A Database Backup Program](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html) in the *MySQL documentation*, [rds](https://docs.aws.amazon.com/cli/latest/reference/rds/index.html#cli-aws-rds) in the *CLI Command Reference*, [Restoring a DB instance to a specified time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html) and [Restoring from a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html) in the *Amazon RDS user guide*.