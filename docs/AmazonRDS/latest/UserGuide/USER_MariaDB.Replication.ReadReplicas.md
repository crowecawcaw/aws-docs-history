# Configuring delayed replication with MariaDB

You can use delayed replication as a strategy for disaster recovery. With delayed
replication, you specify the minimum amount of time, in seconds, to delay
replication from the source to the read replica. In the event of a disaster, such as
a table deleted unintentionally, you complete the following steps to recover from
the disaster quickly:

- Stop replication to the read replica before the change that caused the disaster
  is sent to it.

To stop replication, use the [mysql.rds_stop_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication "mysql-stored-proc-replicating.md#mysql_rds_stop_replication") stored procedure.

- Promote the read replica to be the new source DB instance by using the
  instructions in [Promoting a read replica to be a standalone
  DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

###### Note

- Delayed replication is supported for MariaDB 10.6 and higher.
- Use stored procedures to configure delayed replication. You can't configure
  delayed replication with the AWS Management Console, the AWS CLI, or the Amazon RDS
  API.
- You can use replication based on global transaction identifiers (GTIDs) in a delayed replication
  configuration.

###### Topics

- [Configuring delayed replication during read replica creation](#USER_MariaDB.Replication.ReadReplicas.DelayReplication.ReplicaCreation "#USER_MariaDB.Replication.ReadReplicas.DelayReplication.ReplicaCreation")
- [Modifying delayed replication for an existing read replica](#USER_MariaDB.Replication.ReadReplicas.DelayReplication.ExistingReplica "#USER_MariaDB.Replication.ReadReplicas.DelayReplication.ExistingReplica")
- [Promoting a read replica](#USER_MariaDB.Replication.ReadReplicas.DelayReplication.Promote "#USER_MariaDB.Replication.ReadReplicas.DelayReplication.Promote")

## Configuring delayed replication during read replica creation

To configure delayed replication for any future read replica created from a DB
instance, run the [mysql.rds_set_configuration](mysql-stored-proc-configuring.md#mysql_rds_set_configuration "mysql-stored-proc-configuring.md#mysql_rds_set_configuration") stored procedure with the
`target delay` parameter.

###### To configure delayed replication during read replica creation

1. Using a MariaDB client, connect to the MariaDB DB instance to be the source for
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

1. Using a MariaDB client, connect to the read replica as the master
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

## Promoting a read replica

After replication is stopped, in a disaster recovery scenario, you can promote
a read replica to be the new source DB instance. For information about promoting
a read replica, see [Promoting a read replica to be a standalone
DB instance](USER_ReadRepl.md "USER_ReadRepl.md").
