

# Troubleshooting replication failures due to missing records
<a name="USER_ReadRepl.Troubleshooting.MissingRecords"></a>

When using Amazon RDS for MySQL or MariaDB with binary log replication, you might encounter replication failures where the process halts due to missing records on read replicas. This section explains how to diagnose and resolve these issues.

## Common causes
<a name="USER_ReadRepl.Troubleshooting.MissingRecords.Causes"></a>

A data inconsistency between the source and replica could be caused by one of the following scenarios:
+ Manual data modification on the replica
+ Transactions skipped using `sql_replica_skip_counter` (`sql_slave_skip_counter` prior to MySQL 8.0.26)
+ Missing rows on the replica during initial data sync using migration tools

## Identifying the problem
<a name="USER_ReadRepl.Troubleshooting.MissingRecords.Identifying"></a>

A common indicator of this issue is `Error 1032` with the message `Can't find record`. The following error message appears in the replica's error log:

```
2025-11-04T21:24:11.038899Z 566 [ERROR] [MY-010584] [Repl] Replica SQL for channel '': 
Worker 1 failed executing transaction 'ANONYMOUS' at source log 
mysql-bin-changelog.031523, end_log_pos 899; Could not execute Update_rows event on 
table test_replication.users; Can't find record in 'users', Error_code: 1032; handler 
error HA_ERR_KEY_NOT_FOUND; the event's source log mysql-bin-changelog.031523, 
end_log_pos 899, Error_code: MY-001032
```

**Note**  
The error log format varies between MySQL and MariaDB engines. For information on how to retrieve the logs, see [Viewing and listing database log files](USER_LogAccess.Procedural.Viewing.md).

## Diagnosing the issue
<a name="USER_ReadRepl.Troubleshooting.MissingRecords.Diagnosing"></a>

To diagnose the replication failure:
+ Review the replica error logs to identify where replication stopped. You can use `MY-010584` as the search keyword.
+ Run `SHOW REPLICA STATUS\G` (`SHOW SLAVE STATUS\G` prior to MySQL 8.0.22) on the replica and review the `Last_Error` column:

  ```
  Last_Error: Coordinator stopped because there were error(s) in the worker(s). 
  The most recent failure being: Worker 1 failed executing transaction 'ANONYMOUS' 
  at source log mysql-bin-changelog.031523, end_log_pos 899. See error log and/or 
  performance_schema.replication_applier_status_by_worker table for more details 
  about this failure or others, if any.
  ```
+ Check the binary log file name and position where the replication process stopped on the replica instance. You can find this information in the replica instance's error log.

## Analyzing binary logs
<a name="USER_ReadRepl.Troubleshooting.MissingRecords.BinlogAnalysis"></a>

To investigate a replication failure at a specific transaction, you can use the [`mysqlbinlog`](https://dev.mysql.com/doc/refman/en/mysqlbinlog.html) utility to examine the binary log file. For example, if replication failed at `end_log_pos` position `899` in the binary log file `mysql-bin-changelog.031523`, you can analyze this specific location to identify the cause of the failure.

**Note**  
The `end_log_pos` value indicates the end position of the failing event. In the decoded binary log output, look for the event whose `end_log_pos` matches this value.

Use the `mysqlbinlog` utility to download and examine the relevant binary log. Use the endpoint for the primary instance.

```
$ mysqlbinlog --read-from-remote-server \
--host=<rds-endpoint> \
--port=3306 \
--user=<username> \
--password=<password> \
--base64-output=DECODE-ROWS -vv \
mysql-bin-changelog.031523 > decoded-binlog-file-name
```

**Note**  
The `mysqlbinlog` utility is a native MySQL tool that helps you read and interpret binary log contents. For more information about accessing binary logs on Amazon RDS, see [Accessing MySQL binary logs](USER_LogAccess.MySQL.Binarylog.md).

The binary log from the writer instance shows that the writer instance attempted to update a record with `id=1` in the `test_replication.users` table:

```
#251104 21:13:13 server id 680788197  end_log_pos 899 CRC32 0x89b1e255     Update_rows: table id 101 flags: STMT_END_F
### UPDATE `test_replication`.`users`
### WHERE
###   @1=1 /* INT meta=0 nullable=0 is_null=0 */
###   @2='Test User' /* VARSTRING(400) meta=400 nullable=1 is_null=0 */
###   @3='updated4@example.com' /* VARSTRING(400) meta=400 nullable=1 is_null=0 */
###   @4=1762288260 /* TIMESTAMP(0) meta=0 nullable=1 is_null=0 */
### SET
###   @1=1 /* INT meta=0 nullable=0 is_null=0 */
###   @2='Test User' /* VARSTRING(400) meta=400 nullable=1 is_null=0 */
###   @3='updated5@example.com' /* VARSTRING(400) meta=400 nullable=1 is_null=0 */
###   @4=1762288260 /* TIMESTAMP(0) meta=0 nullable=1 is_null=0 */
# at 899
```

The replica's error logs show that the replica could not execute the `UPDATE` statement because the target record does not exist:

```
Can't find record in 'users', Error_code: 1032; handler error HA_ERR_KEY_NOT_FOUND
```

To verify that the row is missing, check if the specific row exists on the replica:

```
SELECT 1 FROM test_replication.users WHERE id=1;
Empty set (0.00 sec)
```

This output confirms that the `UPDATE` operation from the source DB instance failed to replicate because the target row doesn't exist on the replica.

## Avoiding replication failures
<a name="USER_ReadRepl.Troubleshooting.MissingRecords.Prevention"></a>

We recommend the following best practices to avoid replication inconsistencies:
+ Use GTID-based replication. For more information, see [Using GTID-based replication](mysql-replication-gtid.md).
+ Use `binlog_format` as `ROW` on the primary instance. With `binlog_format` as `MIXED`, there is a chance for replication to hide inconsistencies silently.
+ Configure `read_only` to `1` on the replica instance to prevent unintended row modifications.
+ Set `innodb_flush_log_at_trx_commit` to `1` on the replica instance.
+ Set `sync_binlog` to `1` on the primary instance.
+ Verify table schema parity between the primary and replica.
+ Ensure that replicated tables have primary keys.