# Troubleshooting workload issues for Aurora MySQL databases

Database workload can be viewed as reads and writes. With an understanding of "normal" database workload, you can tune queries
and the database server to meet demand as it changes. There are a number of different reasons why performance can change, so the
first step is to understand what has changed.

- Has there been a major or minor version upgrade?

A major version upgrade includes changes to the engine code, particularly in the optimizer, that can change the query
execution plan. When upgrading database versions, especially major versions, it's very important that you analyze the
database workload and tune accordingly. Tuning can involve optimizing and rewriting queries, or adding and updating
parameter settings, depending on the results of testing. Understanding what is causing the impact will allow you to
start focusing on that specific area.

For more information, see [What is new in
MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html "https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html") and [Server and
status variables and options added, deprecated, or removed in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/added-deprecated-removed.html "https://dev.mysql.com/doc/refman/8.0/en/added-deprecated-removed.html") in the MySQL documentation, and
[Comparing Aurora MySQL version 2 and Aurora MySQL version 3](AuroraMySQL.md "AuroraMySQL.md").

- Has there been an increase in data being processed (row counts)?
- Are there more queries running concurrently?
- Are there schema or database changes?
- Have there been code defects or fixes?

###### Contents

- [Instance host metrics](aurora-mysql-troubleshooting-workload.md#ams-workload-instance "aurora-mysql-troubleshooting-workload.md#ams-workload-instance")
  - [CPU usage](aurora-mysql-troubleshooting-workload.md#ams-workload-cpu "aurora-mysql-troubleshooting-workload.md#ams-workload-cpu")
  - [Memory usage](aurora-mysql-troubleshooting-workload.md#ams-workload-instance-memory "aurora-mysql-troubleshooting-workload.md#ams-workload-instance-memory")
  - [Network throughput](aurora-mysql-troubleshooting-workload.md#ams-workload-network "aurora-mysql-troubleshooting-workload.md#ams-workload-network")

- [Database metrics](aurora-mysql-troubleshooting-workload.md#ams-workload-db "aurora-mysql-troubleshooting-workload.md#ams-workload-db")
- [Troubleshooting memory usage issues for Aurora MySQL databases](ams-workload-memory.md "ams-workload-memory.md")
  - [Example 1: Continuous high memory usage](ams-workload-memory.md#ams-workload-memory.example1 "ams-workload-memory.md#ams-workload-memory.example1")
  - [Example 2: Transient memory spikes](ams-workload-memory.md#ams-workload-memory.example2 "ams-workload-memory.md#ams-workload-memory.example2")
  - [Example 3: Freeable memory drops continuously and isn't reclaimed](ams-workload-memory.md#ams-workload-memory.example3 "ams-workload-memory.md#ams-workload-memory.example3")

- [Troubleshooting out-of-memory issues for Aurora MySQL databases](AuroraMySQLOOM.md "AuroraMySQLOOM.md")

## Instance host metrics

Monitor instance host metrics such as CPU, memory, and network activity to help understand whether there has been a
workload change. There are two main concepts for understanding workload changes:

- Utilization – The usage of a device, such as CPU or disk. It can be time-based or capacity-based.
  - Time-based – The amount of time that a resource is busy over a particular observation
    period.
  - Capacity-based – The amount of throughput that a system or component can deliver, as a percentage
    of its capacity.

- Saturation – The degree to which more work is required of a resource than it can process. When
  capacity-based usage reaches 100%, the extra work can't be processed and must be queued.

### CPU usage

You can use the following tools to identify CPU usage and saturation:

- CloudWatch provides the `CPUUtilization` metric. If this reaches 100%, then the instance is saturated.
  However, CloudWatch metrics are averaged over 1 minute, and lack granularity.

For more information on CloudWatch metrics, see [Instance-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances "Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances").

- Enhanced Monitoring provides metrics returned by the operating system `top` command. It shows load averages and
  the following CPU states, with 1-second granularity:

      + `Idle (%)` = Idle time
      + `IRQ (%)` = Software interrupts
      + `Nice (%)` = Nice time for processes with a [niced](https://en.wikipedia.org/wiki/Nice_(Unix) "https://en.wikipedia.org/wiki/Nice_(Unix)") priority.
      + `Steal (%)` = Time spent serving other tenants (virtualization related)
      + `System (%)` = System time
      + `User (%)` = User time
      + `Wait (%)` = I/O wait

  For more information on Enhanced Monitoring metrics, see [OS metrics for Aurora](USER_Monitoring-Available-OS-Metrics.md#USER_Monitoring-Available-OS-Metrics-RDS "USER_Monitoring-Available-OS-Metrics.md#USER_Monitoring-Available-OS-Metrics-RDS").

### Memory usage

If the system is under memory pressure, and resource consumption is reaching
saturation, you should be observing a high degree of page scanning, paging,
swapping, and out-of-memory errors.

You can use the following tools to identify memory usage and
saturation:

CloudWatch provides the `FreeableMemory` metric, that shows how much
memory can be reclaimed by flushing some of the OS caches and the current free
memory.

For more information on CloudWatch metrics, see [Instance-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances "Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances").

Enhanced Monitoring provides the following metrics that can help you identify memory usage
issues:

- `Buffers (KB)` – The amount of memory used for
  buffering I/O requests before writing to the storage device, in
  kilobytes.
- `Cached (KB)` – The amount of memory used for
  caching file system–based I/O.
- `Free (KB)` – The amount of unassigned memory, in
  kilobytes.
- `Swap` – Cached, Free, and Total.

For example, if you see that your DB instance uses `Swap` memory,
then the total amount of memory for your workload is larger than your instance
currently has available. We recommend increasing the size of your DB instance or
tuning your workload to use less memory.

For more information on Enhanced Monitoring metrics, see [OS metrics for Aurora](USER_Monitoring-Available-OS-Metrics.md#USER_Monitoring-Available-OS-Metrics-RDS "USER_Monitoring-Available-OS-Metrics.md#USER_Monitoring-Available-OS-Metrics-RDS").

For more detailed information on using the Performance Schema and
`sys` schema to determine which connections and components are
using memory, see [Troubleshooting memory usage issues for Aurora MySQL databases](ams-workload-memory.md "ams-workload-memory.md").

### Network throughput

CloudWatch provides the following metrics for total network throughput, all averaged over 1 minute:

- `NetworkReceiveThroughput` – The amount of network throughput received from clients by each
  instance in the Aurora DB cluster.
- `NetworkTransmitThroughput` – The amount of network throughput sent to clients by each
  instance in the Aurora DB cluster.
- `NetworkThroughput` – The amount of network throughput both received from and transmitted to
  clients by each instance in the Aurora DB cluster.
- `StorageNetworkReceiveThroughput` – The amount of network throughput received from the
  Aurora storage subsystem by each instance in the DB cluster.
- `StorageNetworkTransmitThroughput` – The amount of network throughput sent to the Aurora
  storage subsystem by each instance in the Aurora DB cluster.
- `StorageNetworkThroughput` – The amount of network throughput received from and sent to the
  Aurora storage subsystem by each instance in the Aurora DB cluster.

For more information on CloudWatch metrics, see [Instance-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances "Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances").

Enhanced Monitoring provides the `network` received (**RX**) and transmitted (**TX**)
graphs, with up to 1-second granularity.

For more information on Enhanced Monitoring metrics, see [OS metrics for Aurora](USER_Monitoring-Available-OS-Metrics.md#USER_Monitoring-Available-OS-Metrics-RDS "USER_Monitoring-Available-OS-Metrics.md#USER_Monitoring-Available-OS-Metrics-RDS").

## Database metrics

Examine the following CloudWatch metrics for workload changes:

- `BlockedTransactions` – The average number of transactions in the database that are blocked per
  second.
- `BufferCacheHitRatio` – The percentage of requests that are served by the buffer cache.
- `CommitThroughput` – The average number of commit operations per second.
- `DatabaseConnections` – The number of client network connections to the database
  instance.
- `Deadlocks` – The average number of deadlocks in the database per second.
- `DMLThroughput` – The average number of inserts, updates, and deletes per second.
- `ResultSetCacheHitRatio` – The percentage of requests
  that are served by the query cache.
- `RollbackSegmentHistoryListLength` – The undo logs that record committed transactions with
  delete-marked records.
- `RowLockTime` – The total time spent acquiring row locks for InnoDB tables.
- `SelectThroughput` – The average number of select queries per second.

For more information on CloudWatch metrics, see [Instance-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances "Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances").

Consider the following questions when examining the workload:

1. Were there recent changes in DB instance class, for example reducing the instance size from 8xlarge to 4xlarge, or
   changing from db.r5 to db.r6?
2. Can you create a clone and reproduce the issue, or is it happening only on that one instance?
3. Is there server resource exhaustion, high CPU or memory exhaustion? If yes, this could mean that additional
   hardware is required.
4. Are one or more queries taking longer?
5. Are the changes caused by an upgrade, especially a major version upgrade? If yes, then compare the pre- and
   post-upgrade metrics.
6. Are there changes in the number of reader DB instances?
7. Have you enabled general, audit, or binary logging? For more information, see [Logging for Aurora MySQL databases](aurora-mysql-troubleshooting-logging.md "aurora-mysql-troubleshooting-logging.md").
8. Did you enable, disable, or change your use of binary log (binlog) replication?
9. Are there any long-running transactions holding large numbers of row locks? Examine the InnoDB history list length
   (HLL) for indications of long-running transactions.

For more information, see [The InnoDB history list length increased
significantly](proactive-insights.md "proactive-insights.md") and the blog post [Why is my SELECT query running slowly
on my Amazon Aurora MySQL DB cluster?](https://repost.aws/knowledge-center/aurora-mysql-slow-select-query "https://repost.aws/knowledge-center/aurora-mysql-slow-select-query").

    1. If a large HLL is caused by a write transaction, it means that `UNDO` logs are accumulating
     (not being cleaned regularly). In a large write transaction, this accumulation can grow quickly. In MySQL,
     `UNDO` is stored in the [SYSTEM tablespace](https://dev.mysql.com/doc/refman/5.7/en/innodb-system-tablespace.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-system-tablespace.html").
     The `SYSTEM` tablespace is not shrinkable. The `UNDO` log might cause the
     `SYSTEM` tablespace to grow to several GB, or even TB. After the purge, release the allocated
     space by taking a logical backup (dump) of the data, then import the dump to a new DB instance.
    2. If a large HLL is caused by a read transaction (long-running query), it can mean that the query is using a
     large amount of temporary space. Release the temporary space by rebooting. Examine Performance Insights DB metrics for any
     changes in the `Temp` section, such as `created_tmp_tables`. For more information, see
     [Monitoring DB load with Performance Insights on Amazon Aurora](USER_PerfInsights.md "USER_PerfInsights.md").

10. Can you split long-running transactions into smaller ones that modify fewer rows?
11. Are there any changes in blocked transactions or increases in deadlocks? Examine Performance Insights DB metrics for any changes
    in status variables in the `Locks` section, such as `innodb_row_lock_time`, `innodb_row_lock_waits`, and `innodb_dead_locks`. Use 1-minute or 5-minute intervals.
12. Are there increased wait events? Examine Performance Insights wait events and wait types using 1-minute or 5-minute intervals.
    Analyze the top wait events and see whether they are correlated to workload changes or database contention. For
    example, `buf_pool mutex` indicates buffer pool contention. For more information, see [Tuning Aurora MySQL with wait events](AuroraMySQL.Managing.Tuning.md "AuroraMySQL.Managing.Tuning.md").
