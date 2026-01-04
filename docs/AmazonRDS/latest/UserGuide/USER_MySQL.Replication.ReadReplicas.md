# Configuring delayed replication with MySQL

You can use delayed replication as a strategy for disaster recovery. With delayed
replication, you specify the minimum amount of time, in seconds, to delay
replication from the source to the read replica. In the event of a disaster, such as
a table deleted unintentionally, you complete the following steps to recover from
the disaster quickly:

- Stop replication to the read replica before the change that caused the disaster
  is sent to it.

Use the [mysql.rds_stop_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication "mysql-stored-proc-replicating.md#mysql_rds_stop_replication") stored
procedure to stop replication.

- Start replication and specify that replication stops automatically at a log file location.

You specify a location just before the disaster using the
[mysql.rds_start_replication_until](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until")
stored procedure.

- Promote the read replica to be the new source DB instance by using the
  instructions in [Promoting a read replica to be a standalone
  DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

###### Note

- On RDS for MySQL 8.4, delayed replication is supported for MySQL 8.4.3 and
  higher. On RDS for MySQL 8.0, delayed replication is supported for MySQL
  8.0.28 and higher. On RDS for MySQL 5.7, delayed replication is supported
  for MySQL 5.7.44 and higher.
- Use stored procedures to configure delayed replication. You can't configure
  delayed replication with the AWS Management Console, the AWS CLI, or the Amazon RDS
  API.
- You can use replication based on global transaction identifiers (GTIDs) in
  a delayed replication configuration for the following versions:

      + RDS for MySQL version 5.7.44 and higher 5.7 versions
      + RDS for MySQL version 8.0.28 and higher 8.0 versions
      + RDS for MySQL version 8.4.3 and higher 8.4 versions

  If you use GTID-based replication, use the [mysql.rds_start_replication_until_gtid](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid") stored
  procedure instead of the [mysql.rds_start_replication_until](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until") stored
  procedure. For more information about GTID-based replication, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

###### Topics

- [Configuring delayed replication during read replica creation](#USER_MySQL.Replication.ReadReplicas.DelayReplication.ReplicaCreation "#USER_MySQL.Replication.ReadReplicas.DelayReplication.ReplicaCreation")
- [Modifying delayed replication for an existing read replica](#USER_MySQL.Replication.ReadReplicas.DelayReplication.ExistingReplica "#USER_MySQL.Replication.ReadReplicas.DelayReplication.ExistingReplica")
- [Setting a location to stop replication to a read replica](#USER_MySQL.Replication.ReadReplicas.DelayReplication.StartUntil "#USER_MySQL.Replication.ReadReplicas.DelayReplication.StartUntil")
- [Promoting a read replica](#USER_MySQL.Replication.ReadReplicas.DelayReplication.Promote "#USER_MySQL.Replication.ReadReplicas.DelayReplication.Promote")

## Configuring delayed replication during read replica creation

To configure delayed replication for any future read replica created from a DB
instance, run the [mysql.rds_set_configuration](mysql-stored-proc-configuring.md#mysql_rds_set_configuration "mysql-stored-proc-configuring.md#mysql_rds_set_configuration") stored procedure with the
`target delay` parameter.

###### To configure delayed replication during read replica creation

1. Using a MySQL client, connect to the MySQL DB instance to be the source for
   read replicas as the master user.
2. Run the [mysql.rds_set_configuration](mysql-stored-proc-configuring.md#mysql_rds_set_configuration "mysql-stored-proc-configuring.md#mysql_rds_set_configuration") stored procedure with the `target delay` parameter.

For example, run the following stored procedure to specify that replication
is delayed by at least one hour (3,600 seconds) for any read replica
created from the current DB instance.

```
call mysql.rds_set_configuration('target delay', 3600);
```

###### Note

After running this stored procedure, any read replica you create using
the AWS CLI or Amazon RDS API is configured with replication delayed by the
specified number of seconds.

## Modifying delayed replication for an existing read replica

To modify delayed replication for an existing read replica, run the [mysql.rds_set_source_delay](mysql-stored-proc-replicating.md#mysql_rds_set_source_delay "mysql-stored-proc-replicating.md#mysql_rds_set_source_delay") stored procedure.

###### To modify delayed replication for an existing read replica

1. Using a MySQL client, connect to the read replica as the master
   user.
2. Use the [mysql.rds_stop_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication "mysql-stored-proc-replicating.md#mysql_rds_stop_replication") stored
   procedure to stop replication.
3. Run the [mysql.rds_set_source_delay](mysql-stored-proc-replicating.md#mysql_rds_set_source_delay "mysql-stored-proc-replicating.md#mysql_rds_set_source_delay") stored procedure.

For example, run the following stored procedure to specify that replication
to the read replica is delayed by at least one hour (3600
seconds).

```
call mysql.rds_set_source_delay(3600);
```

4. Use the [mysql.rds_start_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication") stored
   procedure to start replication.

## Setting a location to stop replication to a read replica

After stopping replication to the read replica, you can start replication and then
stop it at a specified binary log file location using the [mysql.rds_start_replication_until](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until") stored procedure.

###### To start replication to a read replica and stop replication at a specific

location

1. Using a MySQL client, connect to the source MySQL DB instance as the master user.
2. Run the [mysql.rds_start_replication_until](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until") stored procedure.

The following example initiates replication and replicates changes until it reaches location `120` in the
`mysql-bin-changelog.000777` binary log file. In a disaster recovery scenario, assume that location `120`
is just before the disaster.

```
call mysql.rds_start_replication_until(
  'mysql-bin-changelog.000777',
  120);

```

Replication stops automatically when the stop point is reached. The following RDS event is generated:
`Replication has been stopped since the replica reached the stop point specified by the 
 rds_start_replication_until stored procedure`.

## Promoting a read replica

After replication is stopped, in a disaster recovery scenario, you can
promote a read replica to be the new source DB instance. For information about
promoting a read replica, see [Promoting a read replica to be a standalone
DB instance](USER_ReadRepl.md "USER_ReadRepl.md").
