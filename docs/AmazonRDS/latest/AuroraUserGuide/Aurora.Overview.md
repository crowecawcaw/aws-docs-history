# Amazon Aurora reliability

Aurora is designed to be reliable, durable, and fault tolerant. You can architect your
Aurora DB cluster to improve availability by doing things such as adding Aurora Replicas and
placing them in different Availability Zones, and also Aurora includes several automatic
features that make it a reliable database solution.

###### Topics

- [Storage auto-repair](#Aurora.Overview.AutoRepair "#Aurora.Overview.AutoRepair")
- [Survivable page cache](#Aurora.Overview.CacheWarming "#Aurora.Overview.CacheWarming")
- [Recovery from unplanned restarts](#Aurora.Overview.RestartRecovery "#Aurora.Overview.RestartRecovery")

## Storage auto-repair

Because Aurora maintains multiple copies of your data in three Availability Zones, the
chance of losing data as a result of a disk failure is greatly minimized. Aurora
automatically detects failures in the disk volumes that make up the cluster volume. When a
segment of a disk volume fails, Aurora immediately repairs the segment. When Aurora repairs
the disk segment, it uses the data in the other volumes that make up the cluster volume to
ensure that the data in the repaired segment is current. As a result, Aurora avoids data loss
and reduces the need to perform a point-in-time restore to recover from a disk failure.

## Survivable page cache

In Aurora, each DB instance's page cache is managed in a separate process from the
database, which allows the page cache to survive independently of the database. (The page
cache is also called the InnoDB _buffer pool_ on Aurora MySQL and the
_buffer cache_ on Aurora PostgreSQL.)

In the unlikely event of a database failure, the page cache remains in memory, which
keeps current data pages "warm" in the page cache when the database restarts. This provides
a performance gain by bypassing the need for the initial queries to execute read I/O
operations to "warm up" the page cache.

For Aurora MySQL, page cache behavior when rebooting and failing over is the
following:

- You can reboot the writer instance without rebooting the reader instances.
  - If the reader instances don't reboot when the writer instance reboots, they
    don't lose their page caches.
  - If the reader instances reboot when the writer instance reboots, they do lose
    their page caches.

- When a reader instance reboots, the page caches on the writer and reader instances
  both survive.
- When the DB cluster fails over, the effect is similar to when a writer instance
  reboots. On the new writer instance (previously the reader instance) the page cache
  survives, but on the reader instance (previously the writer instance), the page cache
  doesn't survive.

For Aurora PostgreSQL, you can use cluster cache management to preserve the page cache of a
designated reader instance that becomes the writer instance after failover. For more
information, see [Fast recovery after failover with
cluster cache management for Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md").

## Recovery from unplanned restarts

Aurora is designed to recover from an unplanned restart almost instantaneously and
continue to serve your application data without the binary log. Aurora recovers
asynchronously on parallel threads, so that your database is open and available immediately
after an unplanned restart.

For more information, see [Fault tolerance for an Aurora DB
cluster](Concepts.md#Aurora.Managing.FaultTolerance "Concepts.md#Aurora.Managing.FaultTolerance") and [Optimizations to reduce database restart time](AuroraMySQL.md#ReducedRestartTime "AuroraMySQL.md#ReducedRestartTime").

The following are considerations for binary logging and unplanned restart recovery on
Aurora MySQL:

- Enabling binary logging on Aurora directly affects the recovery time after an
  unplanned restart, because it forces the DB instance to perform binary log
  recovery.
- The type of binary logging used affects the size and efficiency of logging. For the
  same amount of database activity, some formats log more information than others in the
  binary logs. The following settings for the `binlog_format` parameter result
  in different amounts of log data:

      + `ROW` – The most log data
      + `STATEMENT` – The least log data
      + `MIXED` – A moderate amount of log data that usually provides
       the best combination of data integrity and performance

  The amount of binary log data affects recovery time. If there is more data logged in
  the binary logs, the DB instance must process more data during recovery, which increases
  recovery time.

- To reduce computational overhead and improve recovery times with binary logging, you
  can use enhanced binlog. Enhanced binlog improves the database recovery time by up to
  99%. For more information, see [Setting up enhanced binlog for Aurora MySQL](AuroraMySQL.Enhanced.md "AuroraMySQL.Enhanced.md").
- Aurora does not need the binary logs to replicate data within a DB cluster or to
  perform point-in-time restore (PITR).
- If you don't need the binary log for external replication (or an external binary log
  stream), we recommend that you set the `binlog_format` parameter to
  `OFF` to disable binary logging. Doing so reduces recovery time.

For more information about Aurora binary logging and replication, see [Replication with Amazon Aurora](Aurora.md "Aurora.md"). For more information
about the implications of different MySQL replication types, see [Advantages and
disadvantages of statement-based and row-based replication](https://dev.mysql.com/doc/refman/8.0/en/replication-sbr-rbr.html "https://dev.mysql.com/doc/refman/8.0/en/replication-sbr-rbr.html") in the MySQL
documentation.
