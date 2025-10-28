# Importing data considerations

for MariaDB

The following content contains technical information related to loading data into
MariaDB. This content is aimed at users who are familiar with the MariaDB server
architecture.

## Binary logging

Enabling binary logging reduces data load performance and requires up to four
times additional disk space compared to disabled logging. The transaction size used
to load the data directly affects system performance and disk space
needs—larger transactions require more resources.

## Transaction

size

Transaction size influences the following aspects of MariaDB data loads:

- Resource consumption
- Disk space utilization
- Resume process
- Time to recover
- Input format (flat files or SQL)

This section describes how transaction size affects binary logging and makes the
case for disabling binary logging during large data loads. You can enable and
disable binary logging by setting the Amazon RDS automated backup retention period.
Non-zero values enable binary logging, and zero disables it. For more information,
see [Backup retention period](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").

This section also describes the impact of large transactions on InnoDB and why
it's important to keep transaction sizes small.

### Small

transactions

For small transactions, binary logging doubles the number of disk writes
required to load the data. This effect can severely degrade performance for
other database sessions and increase the time required to load the data. The
degradation experienced depends in part on the following factors:

- Upload rate
- Other database activity taking place during the load
- Capacity of your Amazon RDS DB instance

The binary logs also consume disk space roughly equal to the amount of data
loaded until the logs are backed up and removed. Amazon RDS minimizes this by
frequently backing up and removing binary logs.

### Large

transactions

For large transactions, binary logging triples IOPS and disk usage for the
following reasons:

- The binary log cache stores transaction data temporarily on
  disk.
- This cache grows with the transaction size, which consumes disk
  space.
- When the transaction (commit or rollback) completes, the system copies
  the cache to the binary log.

This process creates three copies of the data:

- The original data
- The cache on disk
- The final binary log entry

Each write operation incurs additional IO, further impacting
performance.

Because of this, binary logging requires triple the disk space compared to
disabled logging. For example, loading 10 GiB of data as a single transaction
creates three copies:

- 10 GiB for the table data
- 10 GiB for the binary log cache
- 10 GiB for the binary log file

The total temporary disk space required is 30 GiB.

Important disk space considerations:

- The cache file persists until either the session ends or a new
  transaction creates another cache.
- The binary log remains until it's backed up, potentially holding 20
  GiB (cache and log) for an extended period.

If you use `LOAD DATA LOCAL INFILE` to load the data, data recovery
creates a fourth copy in case the database has to be recovered from a backup
made before the load. During recovery, MariaDB extracts the data from the binary
log into a flat file. MariaDB then runs `LOAD DATA LOCAL INFILE`.
Building on the preceding example, this recovery requires a total temporary disk
space of 40 GiB, or 10 GiB each for table, cache, log, and local file. Without
at least 40 GiB of free disk space, recovery fails.

### Optimizing large data loads

For large data loads, disable binary logging to reduce overhead and disk space
requirements. You can disable binary logging by setting the backup retention
period to 0. After loading completes, restore the backup retention period to the
appropriate non-zero value. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md") and [Backup retention period](USER_ModifyInstance.md "USER_ModifyInstance.md") in the
settings table.

###### Note

If the DB instance is a source DB instance for read replicas, then you
can't set the backup retention period to 0.

Before loading the data, we recommend that you create a DB snapshot. For more
information, see [Managing manual backups](USER_ManagingManualBackups.md "USER_ManagingManualBackups.md").

## InnoDB

The following information about undo logging and recovery options supports keeping
InnoDB transactions small to optimize database performance.

### Understanding InnoDB undo logging

Undo is a logging mechanism that enables transaction rollback and supports
multi-version concurrency control (MVCC).

For MariaDB 10.11 and lower versions, undo logs are stored in the InnoDB
system tablespace (usually ibdata1) and are retained until the purge thread
removes them. As a result, large data load transactions can cause the system
tablespace to become quite large and consume disk space that you can't reclaim
unless you recreate the database.

For all MariaDB versions, the purge thread must wait to remove any undo logs
until the oldest active transaction either commits or rolls back. If the
database is processing other transactions during the load, their undo logs also
accumulate and can't be removed, even if the transactions commit and no other
transaction needs the undo logs for MVCC. In this situation, all
transactions—including read-only transactions—slow down. This slowdown occurs
because all transactions access all rows that any transaction—not just the load
transaction—changes. In effect, transactions must scan through undo logs that
long-running load transactions prevented from being purged during an undo log
cleanup. This affects performance for any operation accessing modified rows.

### InnoDB

transaction recovery options

Although InnoDB optimizes commit operations, large transaction rollbacks are
slow. For faster recovery, perform a point-in-time recovery or restore a DB
snapshot. For more information, see [Point-in-time recovery](USER_PIT.md "USER_PIT.md") and [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").

## Data import

formats

MariaDB supports two data import formats: flat files and SQL. Review the
information about each format to determine the best option for your needs.

### Flat files

For small transactions, load flat files with `LOAD DATA LOCAL
 INFILE`. This data import format can provide the following benefits
over using SQL:

- Less network traffic
- Lower data transmission costs
- Decreased database processing overhead
- Faster processing

`LOAD DATA LOCAL INFILE` loads the entire flat file as one
transaction. Keep the size of the individual files small for the following
advantages:

- **Resume capability** – You can
  keep track of which files have been loaded. If a problem arises during
  the load, you can pick up where you left off. You might need to
  retransmit some data to Amazon RDS, but with small files, the amount
  retransmitted is minimal.
- **Parallel data loading** – If you
  have sufficient IOPS and network bandwidth for a single file load,
  loading in parallel could save time.
- **Load rate control** – If your
  data load has a negative impact on other processes, you can control the
  load rate by increasing the interval between files.

Large transactions reduce the benefits of using `LOAD DATA LOCAL
 INFILE` to import data. When you can't break a large amount of data
into smaller files, consider using SQL.

### SQL

SQL has one main advantage over flat files: you can easily keep transaction
sizes small. However, SQL can take significantly longer to load than flat files.
Also, after a failure, it can be difficult to determine where to resume—you
can't restart mariadb-dump files. If a failure occurs while loading mariadb-dump
file, you must modify or replace the file before the load can resume. Or,
alternatively, after you correct the cause of the failure, you can restore to
the point in time before the load and resend the file. For more information, see
[Point-in-time recovery](USER_PIT.md "USER_PIT.md").

## Using Amazon RDS DB

snapshots for database checkpoints

If you load data over long durations—such as hours or days—without
binary logging, use DB snapshots to provide periodic checkpoints for data safety.
Each DB snapshot creates a consistent copy of your database instance that serves as
a recovery point during system failures or data corruption events. Because DB
snapshots are fast, frequent checkpointing has minimal impact on load performance.
You can delete previous DB snapshots without impacting database durability or
recovery capabilities. For more information about DB snapshots, see [Managing manual backups](USER_ManagingManualBackups.md "USER_ManagingManualBackups.md").

## Reducing database

load times

The following items are additional tips to reduce load times:

- Create all secondary indexes before loading data into MariaDB databases.
  Unlike other database systems, MariaDB rebuilds the entire table when adding
  or modifying secondary indexes. This process creates a new table with index
  changes, copies all data, and drops the original table.
- Load data in primary key order. For InnoDB tables, this can reduce load
  times by 75%–80% and reduce data file size by 50%.
- Disable foreign key constraints by setting `foreign_key_checks`
  to `0`. This is often required for flat files loaded with
  `LOAD DATA LOCAL INFILE`. For any load, disabling foreign key
  checks accelerates data loading. After loading completes, re-enable
  constraints by setting `foreign_key_checks` to `1` and
  verify the data.
- Load data in parallel unless approaching a resource limit. To enable
  concurrent loading across multiple table segments, use partitioned tables
  when appropriate.
- To reduce SQL execution overhead, combine multiple `INSERT`
  statements into single multi-value `INSERT` operations.
  `mariadb-dump` implements this optimization automatically.
- Reduce InnoDB log IO operations by setting
  `innodb_flush_log_at_trx_commit` to `0`. After
  loading completes, restore `innodb_flush_log_at_trx_commit` to
  `1`.

###### Warning

Setting `innodb_flush_log_at_trx_commit` to `0`
causes InnoDB to flush its logs every second instead of at each commit.
This setting increases performance but can risk transaction loss during
system failures.

- If you are loading data into a DB instance that doesn't have read
  replicas, set `sync_binlog` to `0`. After loading
  completes, restore `sync_binlog parameter`to
  `1`.
- Load data into a Single-AZ DB instance before converting the DB instance
  to a Multi-AZ deployment. If the DB instance already uses a Multi-AZ deployment, we don't
  recommend switching to a Single-AZ deployment for data loading. Doing so
  only provides marginal improvements
