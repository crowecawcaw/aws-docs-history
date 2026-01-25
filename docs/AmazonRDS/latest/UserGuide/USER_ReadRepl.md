# Monitoring read replication

You can monitor the status of a read replica in several ways. The Amazon RDS console shows the
status of a read replica in the **Replication** section of the
**Connectivity & security** tab in the read replica details. To
view the details for a read replica, choose the name of the read replica in the list of
DB instances in the Amazon RDS console.

![Read replica status](images/ReadReplicaStatus.png)
You can also see the status of a read replica using the AWS CLI
`describe-db-instances` command or the Amazon RDS API
`DescribeDBInstances` operation.

The status of a read replica can be one of the following:

- **replicating** – The read
  replica is replicating successfully.
- **replication degraded** (SQL Server and
  PostgreSQL only) – Replicas are receiving data from the primary
  instance, but one or more databases might be not getting updates. This can occur,
  for example, when a replica is in the process of setting up newly created databases.
  It can also occur when unsupported DDL or large object changes are made in the blue
  environment of a blue/green deployment.

The status doesn't transition from `replication degraded` to
`error`, unless an error occurs during the degraded state.

- **error** – An error has
  occurred with the replication. Check the **Replication Error**
  field in the Amazon RDS console or the event log to determine the exact error. For more
  information about troubleshooting a replication error, see [Troubleshooting a MySQL read replica problem](USER_ReadRepl.md "USER_ReadRepl.md").
- **terminated** (MariaDB, MySQL, or
  PostgreSQL only) – Replication is terminated. This occurs if
  replication is stopped for more than 30 consecutive days, either manually or due to
  a replication error. In this case, Amazon RDS terminates replication between the primary
  DB instance and all read replicas. Amazon RDS does this to prevent increased storage
  requirements on the source DB instance and long failover times.

Broken replication can affect storage because the logs can grow in size and number
due to the high volume of errors messages being written to the log. Broken
replication can also affect failure recovery due to the time Amazon RDS requires to
maintain and process the large number of logs during recovery.

- **terminated** (Oracle only)
  – Replication is terminated. This occurs if replication is stopped for more
  than 8 hours because there isn't enough storage remaining on the read replica. In
  this case, Amazon RDS terminates replication between the primary DB instance and the affected
  read replica. This status is a terminal state, and the read replica must be
  re-created.
- **stopped** (MariaDB or MySQL
  only) – Replication has stopped because of a customer-initiated
  request.
- **replication stop point set** (MySQL
  only) – A customer-initiated stop point was set using the [mysql.rds_start_replication_until](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until") stored procedure and the
  replication is in progress.
- **replication stop point reached** (MySQL
  only) – A customer-initiated stop point was set using the [mysql.rds_start_replication_until](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until") stored procedure and
  replication is stopped because the stop point was reached.
  You can see where a DB instance is being replicated and if so, check its replication status. On
  the **Databases** page in the RDS console, it shows
  **Primary** in the **Role** column. Choose its DB instance
  name. On its detail page, on the **Connectivity &
  security** tab, its replication status is under **Replication**.

## Monitoring replication lag

You can monitor replication lag in Amazon CloudWatch by viewing the Amazon RDS
`ReplicaLag` metric.

For Db2, the `ReplicaLag`
metric is the maximum lag of databases that have fallen behind, in seconds. For example,
if two databases lag 5 seconds and 10 seconds, respectively, then
`ReplicaLag` is 10 seconds. Databases without available High Availability
Disaster Recovery (HADR) statuses aren't included in the calculation.

For MariaDB and MySQL, the `ReplicaLag` metric reports the value of the
`Seconds_Behind_Master` field of the `SHOW REPLICA STATUS`
command. Common causes for replication lag for MySQL and MariaDB are the
following:

- A network outage.
- Writing to tables with indexes on a read replica. If the
  `read_only` parameter is not set to 0 on the read replica, it can
  break replication.
- Using a nontransactional storage engine such as MyISAM. Replication is only
  supported for the InnoDB storage engine on MySQL and the XtraDB storage engine
  on MariaDB.

###### Note

Previous versions of MariaDB used `SHOW SLAVE STATUS` instead of
`SHOW REPLICA STATUS`. If you are using a MariaDB version lower than
10.5, then use `SHOW SLAVE STATUS`.

When the `ReplicaLag` metric reaches 0, the replica has caught up to the
primary DB instance. If the `ReplicaLag` metric returns `-1`, then
replication is currently not active. `ReplicaLag = -1` is equivalent to
`Seconds_Behind_Master = NULL`.

For Oracle, the `ReplicaLag` metric is the sum of the `Apply
 Lag` value and the difference between the current time and the apply lag's
`DATUM_TIME` value. The `DATUM_TIME` value is the last time
the read replica received data from its source DB instance. For more information, see [V$DATAGUARD_STATS](https://docs.oracle.com/database/121/REFRN/GUID-B346DD88-3F5E-4F16-9DEE-2FDE62B1ABF7.htm#REFRN30413 "https://docs.oracle.com/database/121/REFRN/GUID-B346DD88-3F5E-4F16-9DEE-2FDE62B1ABF7.htm#REFRN30413") in the Oracle documentation.

For SQL Server, the `ReplicaLag` metric is the maximum lag of databases
that have fallen behind, in seconds. For example, if you have two databases that lag 5
seconds and 10 seconds, respectively, then `ReplicaLag` is 10 seconds. The
`ReplicaLag` metric returns the value of the following query.

```
SELECT MAX(secondary_lag_seconds) max_lag FROM sys.dm_hadr_database_replica_states;
```

For more information, see [secondary_lag_seconds](https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-hadr-database-replica-states-transact-sql "https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-hadr-database-replica-states-transact-sql") in the Microsoft documentation.

`ReplicaLag` returns `-1` if RDS can't determine the lag,
such as during replica setup, or when the read replica is in the `error`
state.

###### Note

New databases aren't included in the lag calculation until they are
accessible on the read replica.

For PostgreSQL, the `ReplicaLag` metric returns the value of the following
query.

```
SELECT extract(epoch from now() - pg_last_xact_replay_timestamp()) AS reader_lag
```

PostgreSQL versions 9.5.2 and later use physical replication slots to manage write
ahead log (WAL) retention on the source instance. For each cross-Region read replica
instance, Amazon RDS creates a physical replication slot and associates it with the instance.
Two Amazon CloudWatch metrics, `Oldest Replication Slot Lag` and `Transaction
 Logs Disk Usage`, show how far behind the most lagging replica is in terms of
WAL data received and how much storage is being used for WAL data. The `Transaction
 Logs Disk Usage` value can substantially increase when a cross-Region read
replica is lagging significantly.

For more information about monitoring a DB instance with CloudWatch, see [Monitoring Amazon RDS metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
