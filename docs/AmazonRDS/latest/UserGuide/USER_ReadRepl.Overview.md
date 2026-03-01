# Differences between read replicas for DB engines

Because Amazon RDS DB engines implement replication differently, there are several significant
differences that you should know about.

## Db2

Replicas for RDS for Db2 have the following features and behaviors:

- **Replication method** – Physical
  replication.
- **Transaction logs purge** – RDS for Db2
  purges the logs from the primary DB instance when the following conditions have
  been met:

      + The logs are at least two hours old.
      + The archive log retention hours setting has passed.
      + RDS for Db2 successfully replicated the logs to all the replica DB
       instances.

  This applies to both same AWS Region DB instances and cross-Region DB
  instances. For information about setting archive log retention hours, see [rdsadmin.set_archive_log_retention](db2-sp-managing-databases.md#db2-sp-set-archive-log-retention "db2-sp-managing-databases.md#db2-sp-set-archive-log-retention").

- **Writable replicas** – A Db2 replica is a
  physical copy, and Db2 doesn't allow for writes in a replica. You can promote
  the replica to make it writable. The promoted replica has the replicated data to
  the point when the request was made to promote it.
- **Backups** – Automatic backups and
  manual snapshots are supported on RDS for Db2 replicas.
- **Parallel replication** – Archive log
  data is always transmitted in parallel from the primary database to all of its
  replicas.
- **Standby state** – The primary use for
  standby replicas is cross-Region disaster recovery. For information, see [Working with replicas for Amazon RDS for Db2](db2-replication.md "db2-replication.md").

## MariaDB and MySQL

Read replicas for RDS for MariaDB and RDS for MySQL have the following features and
behaviors:

- **Replication method** – Logical
  replication.
- **Transaction logs purge** – RDS for MariaDB and
  RDS for MySQL keep any binary logs that haven't been applied.
- **Writable replicas** – You can enable the MariaDB
  or MySQL read replica to be writable.
- **Backups** – Automatic backups and manual
  snapshots are supported on RDS for MariaDB or RDS for MySQL read replicas.
- **Parallel replication** – All supported MariaDB
  and MySQL versions allow for parallel replication threads.
- **Mounted state** – Not supported.

## Oracle

Read replicas for RDS for Oracle have the following features and behaviors:

- **Replication method** – Physical
  replication.
- **Transaction logs purge** – If a primary
  DB instance has no cross-Region read replicas, Amazon RDS for Oracle keeps a minimum of two
  hours of transaction logs on the source DB instance. Logs are purged from the source
  DB instance after two hours or after the archive log retention hours setting has
  passed, whichever is longer. Logs are purged from the read replica after the
  archive log retention hours setting has passed only if they have been
  successfully applied to the database.

In some cases, a primary DB instance might have one or more cross-Region read
replicas. If so, Amazon RDS for Oracle keeps the transaction logs on the source DB instance
until they have been transmitted and applied to all cross-Region read
replicas.

For information about setting archive log retention hours, see [Retaining archived redo logs](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").

- **Writable replicas** – An Oracle read
  replica is a physical copy, and Oracle doesn't allow for writes in a read
  replica. You can promote the read replica to make it writable. The promoted read
  replica has the replicated data to the point when the request was made to
  promote it.
- **Backups** – Automatic backups and
  manual snapshots are supported on RDS for Oracle read replicas.
- **Parallel replication** – Redo log data
  is always transmitted in parallel from the primary database to all of its read
  replicas.
- **Mounted state** – The primary use for
  mounted replicas is cross-Region disaster recovery. An Active Data Guard license
  isn't required for mounted replicas. For more information, see [Working with read replicas for Amazon RDS for Oracle](oracle-read-replicas.md "oracle-read-replicas.md").

## PostgreSQL

Read replicas for RDS for PostgreSQL have the following features and behaviors:

- **Replication method** – Physical
  replication.
- **Transaction logs purge** – PostgreSQL
  has the parameter `wal_keep_segments` that dictates how many write
  ahead log (WAL) files are kept to provide data to the read replicas. The
  parameter value specifies the number of logs to keep.
- **Writable replicas** – A PostgreSQL read
  replica is a physical copy, and PostgreSQL doesn't allow for a read replica
  to be made writable.
- **Backups** – Manual snapshots are
  supported for RDS for PostgreSQL read replicas. Automated backups for read replicas
  are supported for RDS for PostgreSQL 14.1 and higher versions only. You can't turn on
  automated backups for PostgreSQL read replicas for RDS for PostgreSQL versions
  earlier than 14.1. For RDS for PostgreSQL 13 and earlier versions, create a snapshot
  from a read replica if you want a backup of it.
- **Parallel replication** – PostgreSQL has
  a single process handling replication.
- **Mounted state** – Not supported.

## SQL Server

Read replicas for RDS for SQL Server have the following features and behaviors:

- **Replication method** – Physical
  replication.
- **Transaction logs purge** – The Virtual
  Log File (VLF) of the transaction log file on the primary replica can be
  truncated after it is no longer required for the secondary replicas.

The VLF can only be marked as inactive when the log records have been hardened
in the replicas. Regardless of how fast the disk subsystems are in the primary
replica, the transaction log will keep the VLFs until the slowest replica has
hardened it.

- **Writable replicas** – A SQL Server read
  replica is a physical copy and also doesn't allow for writes. You can
  promote the read replica to make it writable. The promoted read replica has the
  replicated data up to the point when the request was made to promote it.
- **Backups** – Automatic backups and manual
  snapshots aren't supported on RDS for SQL Server read replicas.
- **Parallel replication** – Redo log data
  is always transmitted in parallel from the primary database to all of its read
  replicas.
- **Mounted state** – Not supported.
