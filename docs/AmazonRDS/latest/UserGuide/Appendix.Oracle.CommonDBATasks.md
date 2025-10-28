# Prerequisites for

RMAN backups

Before backing up your database using the `rdsadmin.rdsadmin_rman_util`
package, make sure that you meet the following prerequisites:

- Make sure that your RDS for Oracle database is in `ARCHIVELOG` mode.
  To enable this mode, set the backup retention period to a non-zero
  value.
- When backing up archived redo logs or performing a full or incremental
  backup that includes archived redo logs, and when backing up the database,
  make sure that redo log retention is set to a nonzero value. Archived redo
  logs are required to make database files consistent during recovery. For
  more information, see [Retaining archived
  redo logs](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").
- Make sure that your DB instance has sufficient free space to hold the backups.
  When back up your database, you specify an Oracle directory object as a
  parameter in the procedure call. RMAN places the files in the specified
  directory. You can use default directories, such as
  `DATA_PUMP_DIR`, or create a new directory. For more
  information, see [Creating and
  dropping directories in the main data storage space](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.NewDirectories "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.NewDirectories").

You can monitor the current free space in an RDS for Oracle instance using
the CloudWatch metric `FreeStorageSpace`. We recommend that your free
space exceeds the current size of the database, though RMAN backs up only
formatted blocks and supports compression.
