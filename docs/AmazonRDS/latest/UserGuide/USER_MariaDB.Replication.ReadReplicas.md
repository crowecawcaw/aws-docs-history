# Monitoring MariaDB read replicas

For MariaDB read replicas, you can monitor replication lag in Amazon CloudWatch by viewing
the Amazon RDS `ReplicaLag` metric. The `ReplicaLag` metric reports
the value of the `Seconds_Behind_Master` field of the `SHOW REPLICA
 STATUS` command.

###### Note

Previous versions of MariaDB used `SHOW SLAVE STATUS` instead of
`SHOW REPLICA STATUS`. If you are using a MariaDB version before 10.5,
then use `SHOW SLAVE STATUS`.

Common causes for replication lag for MariaDB are the following:

- A network outage.
- Writing to tables with indexes on a read replica. If the
  `read_only` parameter is not set to 0 on the read replica, it
  can break replication.
- Using a nontransactional storage engine such as MyISAM. Replication
  is only supported for the InnoDB storage engine on MariaDB.
  When the `ReplicaLag` metric reaches 0, the replica has caught up to
  the source DB instance. If the `ReplicaLag` metric returns -1, then
  replication is currently not active. `ReplicaLag` = -1 is equivalent to
  `Seconds_Behind_Master` = `NULL`.
