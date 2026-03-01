# Troubleshooting a MariaDB read replica problem

The replication technologies for MariaDB are asynchronous. Because they are
asynchronous, occasional `BinLogDiskUsage` increases on the source DB
instance and `ReplicaLag` on the read replica are to be expected. For
example, a high volume of write operations to the source DB instance can occur in
parallel. In contrast, write operations to the read replica are serialized using a
single I/O thread, which can lead to a lag between the source instance and read
replica. For more information about read-only replicas in the MariaDB documentation,
go to [Replication overview](http://mariadb.com/kb/en/mariadb/replication-overview/ "http://mariadb.com/kb/en/mariadb/replication-overview/").

You can do several things to reduce the lag between updates to a source DB instance
and the subsequent updates to the read replica, such as the following:

- Sizing a read replica to have a storage size and DB instance class comparable
  to the source DB instance.
- Ensuring that parameter settings in the DB parameter groups used by the source
  DB instance and the read replica are compatible. For more information and an
  example, see the discussion of the `max_allowed_packet` parameter
  later in this section.
  Amazon RDS monitors the replication status of your read replicas and updates the
  `Replication State` field of the read replica instance to
  `Error` if replication stops for any reason. An example might be if
  DML queries run on your read replica conflict with the updates made on the source DB
  instance.

You can review the details of the associated error thrown by the MariaDB engine by
viewing the `Replication Error` field. Events that indicate the status of
the read replica are also generated, including [RDS-EVENT-0045](USER_Events.md#RDS-EVENT-0045 "USER_Events.md#RDS-EVENT-0045"),
[RDS-EVENT-0046](USER_Events.md#RDS-EVENT-0046 "USER_Events.md#RDS-EVENT-0046"), and [RDS-EVENT-0047](USER_Events.md#RDS-EVENT-0047 "USER_Events.md#RDS-EVENT-0047"). For more
information about events and subscribing to events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md"). If a MariaDB error message is returned, review
the error in the [MariaDB error message documentation](http://mariadb.com/kb/en/mariadb/mariadb-error-codes/ "http://mariadb.com/kb/en/mariadb/mariadb-error-codes/").

One common issue that can cause replication errors is when the value for the
`max_allowed_packet` parameter for a read replica is less than the
`max_allowed_packet` parameter for the source DB instance. The
`max_allowed_packet` parameter is a custom parameter that you can set
in a DB parameter group that is used to specify the maximum size of DML code that
can be run on the database. In some cases, the `max_allowed_packet`
parameter value in the DB parameter group associated with a source DB instance is
smaller than the `max_allowed_packet` parameter value in the DB parameter
group associated with the source's read replica. In these cases, the replication
process can throw an error (Packet bigger than 'max_allowed_packet' bytes) and stop
replication. You can fix the error by having the source and read replica use DB
parameter groups with the same `max_allowed_packet` parameter values.

Other common situations that can cause replication errors include the
following:

- Writing to tables on a read replica. If you are creating indexes on a read replica, you need
  to have the `read_only` parameter set to **0** to create the indexes. If you are writing to tables on the
  read replica, it might break replication.
- Using a non-transactional storage engine such as MyISAM. read replicas require
  a transactional storage engine. Replication is only supported for the InnoDB
  storage engine on MariaDB.
- Using unsafe nondeterministic queries such as `SYSDATE()`. For
  more information, see [Determination of safe and unsafe statements in binary logging](https://dev.mysql.com/doc/refman/8.0/en/replication-rbr-safe-unsafe.html "https://dev.mysql.com/doc/refman/8.0/en/replication-rbr-safe-unsafe.html").
  If you decide that you can safely skip an error, you can follow the steps described in
  [Skipping the current replication error for RDS for MySQL](Appendix.MySQL.CommonDBATasks.md "Appendix.MySQL.CommonDBATasks.md"). Otherwise, you can
  delete the read replica and create an instance using the same DB instance identifier
  so that the endpoint remains the same as that of your old read replica. If a
  replication error is fixed, the `Replication State` changes to
  _replicating_.

For MariaDB DB instances, in some cases read replicas can't be switched to the
secondary if some binary log (binlog) events aren't flushed during the failure.
In these cases, manually delete and recreate the read replicas. You can reduce the
chance of this happening by setting the following parameter values:
`sync_binlog=1` and `innodb_flush_log_at_trx_commit=1`.
These settings might reduce performance, so test their impact before implementing
the changes in a production environment.
