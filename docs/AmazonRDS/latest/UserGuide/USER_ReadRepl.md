# Troubleshooting a MySQL read replica problem

For MySQL DB instances, in some cases read replicas present replication errors or data
inconsistencies (or both) between the read replica and its source DB instance. This problem
occurs when some binary log (binlog) events or InnoDB redo logs aren't flushed
during a failure of the read replica or the source DB instance. In these cases,
manually delete and recreate the read replicas. You can reduce the chance of this
happening by setting the following parameter values: `sync_binlog=1` and
`innodb_flush_log_at_trx_commit=1`. These settings might reduce performance, so
test their impact before implementing the changes in a production environment.

###### Warning

In the parameter group associated with the source DB instance, we recommend keeping these parameter values:
`sync_binlog=1` and `innodb_flush_log_at_trx_commit=1`. These parameters are dynamic. If you
don't want to use these settings, we recommend temporarily setting those values before executing any operation on the
source DB instance that might cause it to restart. These operations include, but are not limited to, rebooting,
rebooting with failover, upgrading the database version, and changing the DB instance class or its storage. The same
recommendation applies to creating new read replicas for the source DB instance.

Failure to follow this guidance increases the risk of read replicas presenting replication errors or data
inconsistencies (or both) between the read replica and its source DB instance.

The replication technologies for MySQL are asynchronous. Because they are
asynchronous, occasional `BinLogDiskUsage` increases on the source DB
instance and `ReplicaLag` on the read replica are to be expected. For
example, a high volume of write operations to the source DB instance can occur in
parallel. In contrast, write operations to the read replica are serialized using a
single I/O thread, which can lead to a lag between the source instance and read
replica. For more information about read-only replicas in the MySQL documentation,
see [Replication implementation details](https://dev.mysql.com/doc/refman/8.0/en/replication-implementation-details.html "https://dev.mysql.com/doc/refman/8.0/en/replication-implementation-details.html").

You can do several things to reduce the lag between updates to a source DB
instance and the subsequent updates to the read replica, such as the
following:

- Sizing a read replica to have a storage size and DB instance class
  comparable to the source DB instance.
- Ensuring that parameter settings in the DB parameter groups used by the
  source DB instance and the read replica are compatible. For more information
  and an example, see the discussion of the `max_allowed_packet`
  parameter later in this section.
  Amazon RDS monitors the replication status of your read replicas and updates the
  `Replication State` field of the read replica instance to
  `Error` if replication stops for any reason. An example might be if
  DML queries run on your read replica conflict with the updates made on the source DB
  instance.

You can review the details of the associated error thrown by the MySQL engine by
viewing the `Replication Error` field. Events that indicate the status of
the read replica are also generated, including [RDS-EVENT-0045](USER_Events.md#RDS-EVENT-0045 "USER_Events.md#RDS-EVENT-0045"),
[RDS-EVENT-0046](USER_Events.md#RDS-EVENT-0046 "USER_Events.md#RDS-EVENT-0046"), and [RDS-EVENT-0047](USER_Events.md#RDS-EVENT-0047 "USER_Events.md#RDS-EVENT-0047"). For more
information about events and subscribing to events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md"). If a MySQL error message is returned, review the
error number in the [MySQL
error message documentation](https://dev.mysql.com/doc/mysql-errors/8.0/en/server-error-reference.html "https://dev.mysql.com/doc/mysql-errors/8.0/en/server-error-reference.html").

One common issue that can cause replication errors is when the value for the
`max_allowed_packet` parameter for a read replica is less than the
`max_allowed_packet` parameter for the source DB instance. The
`max_allowed_packet` parameter is a custom parameter that you can set
in a DB parameter group. You use `max_allowed_packet` to specify the
maximum size of DML code that can be run on the database. In some cases, the
`max_allowed_packet` value in the DB parameter group associated with
a read replica is smaller than the `max_allowed_packet` value in
the DB parameter group associated with the source DB instance. In these cases,
the replication process can throw the error `Packet bigger than
 'max_allowed_packet' bytes` and stop replication. To fix the error, have
the source DB instance and read replica use DB parameter groups with the same
`max_allowed_packet` parameter values.

Other common situations that can cause replication errors include the
following:

- Writing to tables on a read replica. In some cases, you might create indexes on a read replica
  that are different from the indexes on the source DB instance. If you do,
  set the `read_only` parameter to `0` to create the
  indexes. If you write to tables on the read replica, it might break
  replication if the read replica becomes incompatible with the source DB
  instance. After you perform maintenance tasks on the read replica, we
  recommend that you set the `read_only` parameter back to
  `1`.
- Using a non-transactional storage engine such as MyISAM. Read replicas require
  a transactional storage engine. Replication is only supported for the InnoDB
  storage engine on MySQL.
- Using unsafe nondeterministic queries such as `SYSDATE()`. For
  more information, see [Determination of safe and unsafe statements in binary logging](https://dev.mysql.com/doc/refman/8.0/en/replication-rbr-safe-unsafe.html "https://dev.mysql.com/doc/refman/8.0/en/replication-rbr-safe-unsafe.html").
  If you decide that you can safely skip an error, you can follow the steps
  described in the section [Skipping the current
  replication error for RDS for MySQL](Appendix.MySQL.CommonDBATasks.md "Appendix.MySQL.CommonDBATasks.md"). Otherwise, you can
  first delete the read replica. Then you create an instance using the same DB
  instance identifier so that the endpoint remains the same as that of your old read
  replica. If a replication error is fixed, the `Replication State` changes
  to _replicating_.
