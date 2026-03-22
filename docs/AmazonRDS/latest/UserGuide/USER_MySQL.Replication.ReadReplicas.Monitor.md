# Monitoring replication lag for MySQL read replicas

For MySQL read replicas, you can monitor replication lag in Amazon CloudWatch by viewing
the Amazon RDS `ReplicaLag` metric. The `ReplicaLag` metric reports
the value of the `Seconds_Behind_Master` field of the `SHOW REPLICA
 STATUS` command.

Common causes for replication lag for MySQL are the following:

- A network outage.
- Writing to tables that have different indexes on a read replica. If the
  `read_only` parameter is set to `0` on the read
  replica, replication can break if the read replica becomes incompatible with
  the source DB instance. After you've performed maintenance tasks on the
  read replica, we recommend that you set the `read_only` parameter
  back to `1`.
- Using a nontransactional storage engine such as MyISAM. Replication
  is only supported for the InnoDB storage engine on MySQL.
  When the `ReplicaLag` metric reaches 0, the replica has caught up to
  the source DB instance. If the `ReplicaLag` metric returns -1, then
  replication is currently not active. `ReplicaLag` = -1 is equivalent to
  `Seconds_Behind_Master` = `NULL`.
