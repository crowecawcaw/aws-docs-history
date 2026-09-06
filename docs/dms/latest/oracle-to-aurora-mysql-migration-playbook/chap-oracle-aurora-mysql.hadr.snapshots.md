

# Oracle Flashback Table and MySQL snapshots
<a name="chap-oracle-aurora-mysql.hadr.snapshots"></a>

With AWS DMS, you can restore databases to a specific point in time using Oracle Flashback Table and MySQL snapshots. Oracle Flashback Table provides a way to view and restore data from a specified time in the past, while MySQL snapshots capture the state of a database at a specific point for backup or replication purposes.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  | N/A | N/A | Storage-level backup managed by Amazon RDS. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.hadr.snapshots.oracle"></a>

Oracle Flashback Table is a data protection feature used to undo changes to a table and rewind it to a previous state, not from the backup. While Flashback table operations are running, the affected tables are locked, but the rest of the database remains available.

If the structure of a table has been changed since the point of restore, the `FLASHBACK` will fail.

Make sure that the row movement is turned on.

The data to restore must be found in the undo, and the database administrator manages the size and retention.

You can restore a table to a System Change Number (SCN), restore point, or timestamp.

### Examples
<a name="chap-oracle-aurora-mysql.hadr.snapshots.oracle.examples"></a>

Flashback a table using SCN (query `V$DATABASE` to obtain the SCN).

```
SELECT CURRENT_SCN FROM V$DATABASE;
FLASHBACK TABLE employees TO SCN 3254648;
```

Flashback a table using a restore point (query `V$RESTORE_POINT` to obtain restore points).

```
SELECT NAME, SCN, TIME FROM V$RESTORE_POINT;
FLASHBACK TABLE employees TO RESTORE POINT employees_year_update;
```

Flashback a table using a timestamp (query `V$PARAMETER` to obtain the `undo_retention` value).

```
SELECT NAME, VALUE/60 MINUTES_RETAINED
FROM V$PARAMETER
WHERE NAME = 'undo_retention';
FLASHBACK TABLE employees TO
TIMESTAMP TO_TIMESTAMP('2017-09-21 09:30:00', 'YYYY-MM-DD HH:MI:SS');
```

For more information, see [Backup and Recovery User Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/index.html) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.hadr.snapshots.mysql"></a>

Snapshots are the primary backup mechanism for Amazon Aurora databases. They are extremely fast and nonintrusive. You can take snapshots using the Amazon RDS Management Console or the AWS CLI. Unlike RMAN, there is no need for incremental backups. You can choose to restore your database to the exact time when a snapshot was taken or to any other point in time.

 Amazon Aurora provides the following types of backups:
+  **Automated backups** — Always enabled on Amazon Aurora. They do not impact database performance.
+  **Manual backups** — You can create a snapshot at any time. There is no performance impact when taking snapshots of an Aurora database. Restoring data from snapshots requires creation of a new instance. Up to 100 manual snapshots are supported for each database.

### Examples
<a name="chap-oracle-aurora-mysql.hadr.snapshots.mysql.examples"></a>

For examples, see [MySQL Snapshots](chap-oracle-aurora-mysql.hadr.flashback.md#chap-oracle-aurora-mysql.hadr.flashback.mysql).

## Summary
<a name="chap-oracle-aurora-mysql.hadr.snapshots.summary"></a>


| Description | Oracle |  Amazon Aurora  | 
| --- | --- | --- | 
| Create a restore point |  <pre>CREATE RESTORE POINT<br />  before_update GUARANTEE<br />  FLASHBACK DATABASE;</pre>  |  <pre>aws rds create-db-cluster-snapshot<br />  --db-cluster-snapshotidentifier Snapshot_name<br />  --db-cluster-identifier Cluster_Name</pre>  | 
| Configure flashback retention period |  <pre>ALTER SYSTEM SET<br />  db_flashback_retention_target=2880;</pre>  | Configure the **Backup retention window** setting using the AWS Management Console or AWS CLI. | 
| Flashback table to a previous restore point |  <pre>shutdown immediate;<br />startup mount;<br />flashback database to<br />  restore point before_update;</pre>  | Create new cluster from a snapshot.<pre>aws rds restore-db-cluster-from-snapshot<br />    --db-cluster-identifier NewCluster<br />    --snapshot-identifier SnapshotToRestore<br />    --engine aurora-mysql</pre><br />Add new instance to the cluster.<pre>aws rds create-db-instance<br />    --region useast-1<br />    --db-subnet-group default<br />    --engine aurora-mysql<br />    --db-cluster-identifier clustername-restore<br />    --db-instanceidentifier newinstance-nodeA<br />    --dbinstance-class db.r4.large</pre><br />Use `mysqldbexport` and `mysql` to copy the table from the restored instance to the original instance. | 
| Flashback table to a previous point in time |  <pre>shutdown immediate;<br />startup mount;<br />FLASHBACK DATABASE TO TIME<br />  "TO_DATE ('01/01/2017','MM/DD/YY')";</pre>  | Create a new cluster from a snapshot and provide a specific point in time.<pre>aws rds restore-db-cluster-to-point-in-time<br />  --db-cluster-identifier clustername-restore<br />  --source-db-cluster-identifier clustername<br />  --restore-to-time 2017-09-19T23:45:00.000Z</pre><br />Add a new instance to the cluster:<pre>aws rds create-db-instance<br />  --region us-east-1<br />  --db-subnetgroup default<br />  --engine aurora-mysql<br />  --db-cluster-identifier clustername-restore<br />  --db-instance-identifier newinstance-nodeA<br />  --db-instance-class db.r4.large</pre><br />Use `mysqldbexport` and `mysql` to copy the table from the restored instance to the original instance. | 

For more information, see [mysqldump — A Database Backup Program](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html) in the *MySQL documentation*, [rds](https://docs.aws.amazon.com/cli/latest/reference/rds/index.html#cli-aws-rds) in the *CLI Command Reference* and [Restoring a DB instance to a specified time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html) and [Restoring from a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html) in the *Amazon RDS user guide*.