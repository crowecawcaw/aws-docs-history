# Stopping Group Replication on a DB instance in an active-active cluster

You can stop Group Replication on a DB instance in an active-active
cluster. When you stop Group Replication, the DB instance is placed in super-read-only
mode until replication is restarted or that DB instance is removed from the
active-active cluster. For information about super-read-only mode, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_super_read_only "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_super_read_only").

###### To stop Group Replication temporarily for an active-active cluster

1. Connect to a DB instance in the active-active cluster using a SQL client.

For more information about connecting to an RDS for MySQL DB instance, see
[Connecting to your MySQL DB instance](USER_ConnectToInstance.md "USER_ConnectToInstance.md"). 2. In the SQL client, call the [mysql.rds_group_replication_stop](mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_stop "mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_stop") stored procedure:

```
call mysql.rds_group_replication_stop();
```
