# SQL Server Endpoint Troubleshooting

This section contains replication scenarios specific to SQL Server. To determine what changes to replicate
from SQL server AWS DMS reads the transaction logs, and runs periodic scans on the source database. Replication
latency usually results from SQL Server throttling these scans because of resource constraints. It can also result
from a significant increase in the number of events written to the transaction log in a short time.

###### Topics

- [Index rebuilds](#CHAP_Troubleshooting_Latency_Source_SQLServer_Indexrebuilds "#CHAP_Troubleshooting_Latency_Source_SQLServer_Indexrebuilds")
- [Large transactions](#CHAP_Troubleshooting_Latency_Source_SQLServer_Largetransactions "#CHAP_Troubleshooting_Latency_Source_SQLServer_Largetransactions")
- [Misconfigured MS-CDC polling interval for Amazon RDS SQL Server](#CHAP_Troubleshooting_Latency_Source_SQLServer_MisconfiguredCDC "#CHAP_Troubleshooting_Latency_Source_SQLServer_MisconfiguredCDC")
- [Multiple CDC tasks replicating from the same source database](#CHAP_Troubleshooting_Latency_Source_SQLServer_MultipleCDC "#CHAP_Troubleshooting_Latency_Source_SQLServer_MultipleCDC")
- [Transaction log
  backup processing for RDS for SQL Server](#CHAP_Troubleshooting_Latency_Source_SQLServer_backup "#CHAP_Troubleshooting_Latency_Source_SQLServer_backup")

## Index rebuilds

When SQL Server rebuilds a large index, it uses a single transaction. This generates a lot of events, and can
use up a large amount of log space if SQL Server rebuilds several indexes at once. When this happens, you can
expect brief replication spikes. If your SQL Server source has sustained log spikes, check the following:

- First, check the time period of the latency spikes using either the `CDCLatencySource`
  and `CDCLatencySource` CloudWatch metrics, or by checking Throughput Monitoring messages in the task logs.
  For information about CloudWatch metrics for AWS DMS, see
  [Replication task metrics](CHAP_Monitoring.md#CHAP_Monitoring.Metrics.Task "CHAP_Monitoring.md#CHAP_Monitoring.Metrics.Task").
- Check if the size of the active transaction logs or log backups increased during the latency spike.
  Also check if a maintenance job or a rebuild ran during that time.
  For information about checking transaction log size, see
  [Monitor log space use](https://learn.microsoft.com/en-us/sql/relational-databases/logs/manage-the-size-of-the-transaction-log-file?view=sql-server-ver16#MonitorSpaceUse "https://learn.microsoft.com/en-us/sql/relational-databases/logs/manage-the-size-of-the-transaction-log-file?view=sql-server-ver16#MonitorSpaceUse") in the
  [SQL Server technical documentation](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16").
- Verify that your maintenance plan follows SQL server best practices. For information about SQL server
  maintenance best practices, see
  [Index maintenance strategy](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes?view=sql-server-ver16#index-maintenance-strategy "https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes?view=sql-server-ver16#index-maintenance-strategy") in the
  [SQL Server technical documentation](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16").

To fix latency issues during index rebuilds, try the following:

- Use the `BULK_LOGGED` recovery model for offline rebuilds to reduce the events a task has to process.
- If possible, stop the task during index rebuilds. Or, try to schedule index rebuilds during non-peak hours to mitigate the impact
  of a latency spike.
- Try to identify resource bottlenecks that are slowing DMS reads, such as
  disk latency or I/O throughput, and address them.

## Large transactions

Transactions with a lot of events, or long-running transactions, cause the transaction log to grow.
This causes DMS reads to take longer, resulting in latency. This is similar to the effect index rebuilds have
on replication performance.

You may have difficulty identifying this issue if you're not familiar with the typical workload on the source
database. To troubleshoot this issue, do the following:

- First, identify the time that latency spiked using either the `ReadThroughput`
  and `WriteThroughput` CloudWatch metrics, or by checking Throughput Monitoring messages
  in the task logs.
- Check if there are any long-running queries on the source database during the latency spike. For information
  about long-running queries, see
  [Troubleshoot slow-running queries in SQL Server](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/performance/troubleshoot-slow-running-queries "https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/performance/troubleshoot-slow-running-queries") in the [SQL Server technical documentation](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16").
- Check if the size of the active transaction logs or the log backups has increased. For more information, see
  [Monitor log space use](https://learn.microsoft.com/en-us/sql/relational-databases/logs/manage-the-size-of-the-transaction-log-file?view=sql-server-ver16#MonitorSpaceUse "https://learn.microsoft.com/en-us/sql/relational-databases/logs/manage-the-size-of-the-transaction-log-file?view=sql-server-ver16#MonitorSpaceUse") in the [SQL Server technical documentation](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16").

To fix this issue, do one of the following:

- The best fix is to restructure your transactions on the application side so that they complete quickly.
- If you can't restructure your transactions, a short-term workaround is to check for resource bottlenecks
  such as disk waits or CPU contention. If you find bottlenecks in your source database, you can reduce latency by increasing
  disk, CPU, and memory resources for source database. This reduces contention for system resources, allowing DMS queries
  to complete faster.

## Misconfigured MS-CDC polling interval for Amazon RDS SQL Server

A misconfigured polling interval setting on Amazon RDS instances can cause the transaction log to grow.
This is because replication prevents log truncation. While tasks that are running might continue
replicating with minimal latency, stopping and resuming tasks, or starting CDC-only tasks,
can cause task failures. These are due to timeouts while scanning the large transaction log.

To troubleshoot a misconfigured polling interval, do the following:

- Check if the active transaction log size is increasing, and if log usage is close to 100 percent.
  For more information, see
  [Monitor log space use](https://learn.microsoft.com/en-us/sql/relational-databases/logs/manage-the-size-of-the-transaction-log-file?view=sql-server-ver16#MonitorSpaceUse "https://learn.microsoft.com/en-us/sql/relational-databases/logs/manage-the-size-of-the-transaction-log-file?view=sql-server-ver16#MonitorSpaceUse") in the [SQL Server technical documentation](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16").
- Check if log truncation is delayed with a `log_reuse_wait_desc value` of
  `REPLICATION`. For more information, see
  [The Transaction Log (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver16#FactorsThatDelayTruncation "https://learn.microsoft.com/en-us/sql/relational-databases/logs/the-transaction-log-sql-server?view=sql-server-ver16#FactorsThatDelayTruncation") in the [SQL Server technical documentation](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16").

If you find issues with any of the items in the previous list, tune the MS-CDC polling interval. For information
about tuning the polling interval, see [Recommended settings
when using RDS for SQL Server as a source for AWS DMS](CHAP_Source.SQLServer.md#CHAP_Source.SQLServer.Configuration.Settings "CHAP_Source.SQLServer.md#CHAP_Source.SQLServer.Configuration.Settings").

## Multiple CDC tasks replicating from the same source database

During the full load phase, we recommend splitting tables across tasks to improve performance, to separate
dependent tables logically, and to mitigate the impact of a task failure. However,
during the CDC phase, we recommend consolidating tasks to minimize DMS scans. During the CDC phase, each DMS task
scans the transaction logs for new events several times a minute. Since each
task runs independently, every task scans each transaction log individually. This increases disk and CPU
usage on the source SQL Server database. As a result, a large number of tasks running in parallel can cause
SQL Server to throttle DMS reads, leading to increased latency.

You may have difficulty identifying this issue if muliple tasks start gradually. The most common symptom of this
issue is most task scans starting to take longer. This leads to higher latency for these scans.
SQL Server prioritizes a few of the task scans, so a few of the tasks show normal latency.
To troubleshoot this issue, check the `CDCLatencySource` metric for all of your tasks. If some of the tasks have an increasing
`CDCLatencySource`, while a few tasks have a low `CDCLatencySource`, it is likely
that SQL Server is throttling your DMS reads for some of your tasks.

If SQL Server is throttling your task reads during CDC, consolidate your tasks to minimize the number of DMS scans.
The maximum number of tasks that can connect to your source database without creating contention depends on factors such as the
source database capacity, the rate of transaction log growth, or the number of tables. To determine the ideal number
of tasks for your replication scenario, test replication in a test environment similar to your production environment.

## Transaction log

backup processing for RDS for SQL Server

AWS DMS 3.5.3 and above support replicating from RDS for SQL Server log backups. Replicating events
from the backup logs on RDS instances is slower than replicating events from the active
transaction log. This is because DMS requests access to backups serially to ensure that it maintains the
transaction sequence, and to minimize the risk of the Amazon RDS instance storage filling up. Moreover, at the
Amazon RDS end, the time taken to make the backups available to DMS varies depending on the size of the log
backup, and the load on the RDS for SQL Server instance.

Because of these constraints, we recommend that you set the ECA `ActivateSafeguard` to
`true`. This ensures that transactions are not backed up while the DMS task is reading
from the active transaction log. This setting also prevents Amazon RDS archiving transactions in the active log
when DMS is reading transactions from the backup, thereby eliminating the possibility that DMS cannot catch
up to the active log. Note that this may cause the active log size to grow while the task is catching up.
Ensure that your instance has enough storage to keep the instance from running out of space.

For a CDC-only task replicating from RDS for SQL Server sources, use the use of native CDC start position over native CDC start time
if possible. This is because DMS relies on system tables to identify the starting point for the native start position,
rather than scanning individual log backups when you specify a native start time.
