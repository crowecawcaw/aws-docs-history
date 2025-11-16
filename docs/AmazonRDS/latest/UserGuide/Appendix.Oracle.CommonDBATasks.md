# Enabling and

disabling block change tracking

Block changing tracking records changed blocks in a tracking file. This technique
can improve the performance of RMAN incremental backups. For more information, see [Using Block Change Tracking to Improve Incremental Backup Performance](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/backing-up-database.html#GUID-4E1F605A-76A7-48D0-9D9B-7343B4327E2A "https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/backing-up-database.html#GUID-4E1F605A-76A7-48D0-9D9B-7343B4327E2A")
in the Oracle Database documentation.

RMAN features aren't supported in a read replica. However, as part of your high
availability strategy, you might choose to enable block tracking in a read-only
replica using the procedure
`rdsadmin.rdsadmin_rman_util.enable_block_change_tracking`. If you
promote this read-only replica to a source DB instance, block change tracking is enabled
for the new source instance. Thus, your instance can benefit from fast incremental
backups.

Block change tracking procedures are supported in Enterprise Edition only for the
following DB engine versions:

- Oracle Database 21c (21.0.0)
- Oracle Database 19c (19.0.0)

###### Note

In a single-tenant CDB, the following operations work, but no customer-visible
mechanism can detect the current status of the operations. See also [Limitations of RDS for Oracle
CDBs](Oracle.Concepts.md#Oracle.Concepts.single-tenant-limitations "Oracle.Concepts.md#Oracle.Concepts.single-tenant-limitations").

To enable block change tracking for a DB instance, use the Amazon RDS procedure
`rdsadmin.rdsadmin_rman_util.enable_block_change_tracking`. To
disable block change tracking, use `disable_block_change_tracking`. These
procedures take no parameters.

To determine whether block change tracking is enabled for your DB instance, run
the following query.

```
SELECT STATUS, FILENAME FROM V$BLOCK_CHANGE_TRACKING;
```

The following example enables block change tracking for a DB instance.

```
EXEC rdsadmin.rdsadmin_rman_util.enable_block_change_tracking;
```

The following example disables block change tracking for a DB instance.

```
EXEC rdsadmin.rdsadmin_rman_util.disable_block_change_tracking;
```
