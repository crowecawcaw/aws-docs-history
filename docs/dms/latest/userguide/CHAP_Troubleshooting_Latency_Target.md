# Troubleshooting target latency issues

This section contains scenarios that can contribute to target latency.

###### Topics

- [Indexing issues](#CHAP_Troubleshooting_Latency_Target_Indexing "#CHAP_Troubleshooting_Latency_Target_Indexing")
- [SORTER message in task log](#CHAP_Troubleshooting_Latency_Target_Sorter "#CHAP_Troubleshooting_Latency_Target_Sorter")
- [Database locking](#CHAP_Troubleshooting_Latency_Target_Locking "#CHAP_Troubleshooting_Latency_Target_Locking")
- [Slow LOB lookups](#CHAP_Troubleshooting_Latency_Target_LOB "#CHAP_Troubleshooting_Latency_Target_LOB")
- [Multi-AZ, audit logging and backups](#CHAP_Troubleshooting_Latency_Target_MultiAZ "#CHAP_Troubleshooting_Latency_Target_MultiAZ")

## Indexing issues

During the CDC phase, AWS DMS replicates changes on the source by executing DML statements (insert, update, and delete)
on the target. For heterogenous migrations using DMS, differences in index optimizations on the source
and target can cause writes to the target to take longer. This results in target latency and performance issues.

To troubleshoot indexing issues, do the following. The procedures for these steps vary for different database engines.

- Monitor the query time for your target database. Comparing the query execution time on the target and source can
  indicate which indexes need optimization.
- Enable logging for slow-running queries.

To fix indexing issues for long-running replications, do the following:

- Tune the indexes on your source and target databases
  so that the query execution time is similar on the source and the target.
- Compare the secondary indexes used in DML queries for the source and the target.
  Make sure that DML performance on the target is comparable to or better than the source DML performance.

Note that the procedure for optimizing indexes is specific to your database engine.
There is no DMS feature for tuning source and target indexes.

## SORTER message in task log

If a target endpoint can't keep up with the volume of changes that AWS DMS writes to it, the
task caches the changes on the replication instance. If the cache grows larger than an internal threshold,
the task stops reading further changes from the source. DMS does this to prevent the replication instance from
running out of storage, or the task being stuck while reading a large volume of pending events.

To troubleshoot this issue, check the CloudWatch logs for a message similar to either of the following:

```
[SORTER ]I: Reading from source is paused. Total disk usage exceeded the limit 90% (sorter_transaction.c:110)
[SORTER ]I: Reading from source is paused. Total storage used by swap files exceeded the limit 1048576000 bytes  (sorter_transaction.c:110)

```

If your logs contain a message similar to the first message, disable any trace logging for the task, and
increase the replication instance storage. For information about increasing replication instance storage, see
[Modifying a replication instance](CHAP_ReplicationInstance.md "CHAP_ReplicationInstance.md").

If your logs contain a message similar to the second message, do the following:

- Move tables with numerous transactions or long running DML operations to a separate task,
  if they don’t have any dependencies on other tables in the task.
- Increase the `MemoryLimitTotal` and `MemoryKeepTime` settings to
  hold the transaction for a longer duration in memory. This won't help if the latency is sustained,
  but it can help keep latency down during short bursts of transactional volume. For information about
  these task settings, see [Change processing tuning settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").
- Evaluate if you can use batch apply for your transaction by setting `BatchApplyEnabled`
  to `true`. For information about the `BatchApplyEnabled` setting, see
  [Target
  metadata task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").

## Database locking

If an application accesses a database that AWS DMS is using as a replication target,
the application may lock a table that DMS is trying to access. This creates a lock contention.
Since DMS writes changes to the target database in the order they occurred on the source, delays to writing
to one table due to lock contentions create delays to writing to all tables.

To troubleshoot this issue, query the target database to check if a lock contention is blocking DMS write transactions.
If the target database is blocking DMS write transactions, do one or more of the following:

- Restructure your queries to commit changes more frequently.
- Modify your lock timeout settings.
- Partition your tables to minimize lock contentions.

Note that the procedure for optimizing lock contentions is specific to your database engine.
There is no DMS feature for tuning lock contentions.

## Slow LOB lookups

When AWS DMS replicates a large object (LOB) column, it performs a lookup on the source just before
writing changes to the target. This lookup normally doesn't cause any latency on the target, but if the source database
delays the lookup due to locking, target latency may spike.

This issue is normally difficult to diagnose. To troubleshoot this issue, enable detailed debugging on the task logs, and compare the timestamps
of the DMS LOB lookup calls. For information about enabling detailed
debugging, see [Viewing and managing AWS DMS task logs](CHAP_Monitoring.md#CHAP_Monitoring.ManagingLogs "CHAP_Monitoring.md#CHAP_Monitoring.ManagingLogs").

To fix this issue, try the following:

- Improve the SELECT query performance on the source database.
- Tune the DMS LOB settings. For information about tuning the LOB settings, see
  [Migrating large binary objects (LOBs)](CHAP_BestPractices.md#CHAP_BestPractices.LOBS "CHAP_BestPractices.md#CHAP_BestPractices.LOBS").

## Multi-AZ, audit logging and backups

For Amazon RDS targets, target latency can increase during the following:

- Backups
- After enabling multiple availability zones (multi-AZ)
- After enabling database logging, such as audit or slow query logs.

These issues are normally difficult to diagnose. To troubleshoot these issues, monitor latency for
periodic spikes during Amazon RDS maintenance windows or periods of heavy database loads.

To fix these issues, try the following:

- If possible, during short term migration, disable multi-AZ, backups, or logging.
- Reschedule your maintenance windows for periods of low activity.
