# Renaming a DB instance in an active-active cluster

You can change the name of a DB instance in an active-active cluster. To rename more than one DB instance in an
active-active cluster, do so one DB instance at a time. So, rename one DB instance and rejoin it to the cluster
before you rename the next DB instance.

###### To rename a DB instance in an active-active cluster

1. Connect to the DB instance in a SQL client, and call the [mysql.rds_group_replication_stop](mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_stop "mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_stop") stored procedure:

```
call mysql.rds_group_replication_stop();
```

2. Rename the DB instance by following the instructions in [Renaming a DB instance](USER_RenameInstance.md "USER_RenameInstance.md").
3. Modify the `group_replication_group_seeds` parameter in each DB parameter group associated with
   a DB instance in the active-active cluster.

In the parameter setting, replace the old DB instance endpoint with the new DB instance endpoint.
For more information about setting parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 4. Connect to the DB instance in a SQL client, and call the [mysql.rds_group_replication_start](mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_start "mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_start") stored procedure:

```
call mysql.rds_group_replication_start(0);
```
