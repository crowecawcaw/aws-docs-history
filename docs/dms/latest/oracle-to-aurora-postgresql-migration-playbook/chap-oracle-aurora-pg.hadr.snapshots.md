

# Oracle Flashback Table and Amazon Aurora PostgreSQL snapshots
<a name="chap-oracle-aurora-pg.hadr.snapshots"></a>

With AWS DMS, you can migrate databases between different database platforms or versions by capturing consistent data snapshots from the source database and applying them to the target database. Oracle Flashback Table and Amazon Aurora PostgreSQL snapshots provide point-in-time backups of the source database, enabling migration with minimal downtime.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  | N/A | N/A | Storage level backup managed by Amazon RDS. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.hadr.snapshots.ora"></a>

Oracle Flashback Table is a data protection feature used to undo changes to a table and rewind it to a previous state (not from backup). While Flashback table operations are running, the affected tables are locked, but the rest of the database remains available.

If the structure of a table has been changed since the point of restore, the FLASHBACK will fail. Row movement must be enabled.

The data to restore must be found in the undo (dba must manage the size and retention). A table can be restored to an System Change Number (SCN), Restore Point, or Timestamp.

 **Examples** 

Flashback a table using SCN (query V$DATABASE to obtain the SCN).

```
SELECT CURRENT_SCN FROM V$DATABASE;
FLASHBACK TABLE employees TO SCN 3254648;
```

Flashback a table using a Restore Point (query V$RESTORE\_POINT to obtain restore points).

```
SELECT NAME, SCN, TIME FROM V$RESTORE_POINT;
FLASHBACK TABLE employees TO RESTORE POINT employees_year_update;
```

Flashback a table using a Timestamp (query V$PARAMETER to obtain the undo\_retention value).

```
SELECT NAME, VALUE/60 MINUTES_RETAINED
FROM V$PARAMETER
WHERE NAME = 'undo_retention';
FLASHBACK TABLE employees TO
TIMESTAMP TO_TIMESTAMP('2017-09-21 09:30:00', 'YYYY-MM-DD HH:MI:SS');
```

For more information, see [Backup and Recovery User Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/index.html) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.hadr.snapshots.pg"></a>

Snapshots are the primary backup mechanism for Amazon Aurora databases. They are extremely fast and nonintrusive. You can take snapshots using the Amazon RDS Management Console or the AWS CLI. Unlike RMAN, there is no need for incremental backups. You can choose to restore your database to the exact time when a snapshot was taken or to any other point in time.

 Amazon Aurora provides the following types of backups:
+  **Automated Backups** — Always enabled on Amazon Aurora. They do not impact database performance.
+  **Manual Backups** — You can create a snapshot at any time. There is no performance impact when taking snapshots of an Aurora database. Restoring data from snapshots requires creation of a new instance. Up to 100 manual snapshots are supported for each database.

 **Examples** 

For examples, see [PostgreSQL Amazon Aurora Snapshots](chap-oracle-aurora-pg.hadr.flashback.md#chap-oracle-aurora-pg.hadr.flashback.pg).

## Summary
<a name="chap-oracle-aurora-pg.hadr.snapshots.summary"></a>


| Description | Oracle |  Amazon Aurora  | 
| --- | --- | --- | 
| Create a restore point |  <pre>CREATE RESTORE POINT<br />  before_update GUARANTEE<br />  FLASHBACK DATABASE;</pre>  |  <pre>aws rds create-db-cluster-snapshot<br />  --db-cluster-snapshotidentifier Snapshot_name<br />  --db-cluster-identifier Cluster_Name</pre>  | 
| Configure flashback retention period |  <pre>ALTER SYSTEM SET<br />  db_flashback_retention_target=2880;</pre>  | Configure the **Backup retention window** setting using the AWS management console or AWS CLI. | 
| Flashback table to a previous restore point |  <pre>shutdown immediate;<br />startup mount;<br />flashback database to<br />  restore point before_update;</pre>  | Create new cluster from a snapshot.<pre>aws rds restore-db-cluster-from-snapshot<br />  --db-cluster-identifier NewCluster<br />  --snapshot-identifier SnapshotToRestore<br />  --engine aurora-postgresql</pre><br />Add new instance to the cluster.<pre>aws rds create-db-instance<br />  --region us-east-1<br />  --db-subnetgroup default<br />  --engine aurora-postgresql<br />  --db-cluster-identifier clustername-restore<br />  --db-instance-identifier newinstance-nodeA<br />  --db-instance-class db.r4.large</pre><br />Use `pg_dump` and `pg_restore` to copy the table from the restored instance to the original instance. | 
| Flashback table to a previous point in time |  <pre>shutdown immediate;<br />startup mount;<br />FLASHBACK DATABASE TO TIME<br />  "TO_DATE ('01/01/2017','MM/DD/YY')";</pre>  | Create a new cluster from a snapshot and provide a specific point in time.<pre>aws rds restore-db-cluster-to-point-in-time<br />  --db-cluster-identifier clustername-restore<br />  --source-db-cluster-identifier clustername<br />  --restore-to-time 2017-09-19T23:45:00.000Z</pre><br />Add a new instance to the cluster:<pre>aws rds create-db-instance<br />  --region us-east-1<br />  --db-subnetgroup default<br />  --engine aurora-postgresql<br />  --db-cluster-identifier clustername-restore<br />  --db-instance-identifier newinstance-nodeA<br />  --db-instance-class db.r4.large</pre><br />Use `pg_dump` and `pg_restore` to copy the table from the restored instance to the original instance. | 

For more information, see [rds](https://docs.aws.amazon.com/cli/latest/reference/rds/index.html#cli-aws-rds) in the *CLI Command Reference* and [Restoring a DB instance to a specified time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html) and [Restoring from a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html) in the *Amazon RDS user guide*.