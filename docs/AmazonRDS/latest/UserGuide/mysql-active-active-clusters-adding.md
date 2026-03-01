# Adding a DB instance to an active-active cluster

You can add a DB instance to an Amazon RDS for MySQL active-active cluster by restoring a DB
snapshot or by restoring a DB instance to a point in time. An active-active cluster can
include up to nine DB instances.

When you recover a DB instance to a point in time, it usually includes more recent transactions than a DB
instance that was restored from a DB snapshot. When the DB instance has more recent transactions, fewer transactions
need to be applied when you start replication. So, using point-in-time recovery to add a DB instance to a cluster
is usually faster than restoring from a DB snapshot.

###### Topics

- [Adding a DB instance to an active-active cluster using point-in-time recovery](#mysql-active-active-clusters-adding-pitr "#mysql-active-active-clusters-adding-pitr")
- [Adding a DB instance to an active-active cluster using a DB snapshot](#mysql-active-active-clusters-adding-snapshot "#mysql-active-active-clusters-adding-snapshot")

## Adding a DB instance to an active-active cluster using point-in-time recovery

You can add a DB instance to an active-active cluster by performing point-in-time recovery on a DB instance in the cluster.

For information about recovering a DB instance to a point in time in a different AWS Region, see
[Replicating automated backups to another AWS Region](USER_ReplicateBackups.md "USER_ReplicateBackups.md").

###### To add a DB instance to an active-active cluster using point-in-time recovery

1. Create a new DB instance by performing point-in-time recovery on a DB instance in the active-active cluster.

You can perform point-in-time recovery on any DB instance in the cluster to create the new DB instance.
For instructions, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

###### Important

During point-in-time-recovery, associate the new DB instance with a DB
parameter group that has the active-active cluster parameters set.
Otherwise, Group Replication won't start on the new DB instance. For
information about the parameters and the required setting for each one,
see [Required parameter settings for active-active clusters](mysql-active-active-clusters-parameters.md "mysql-active-active-clusters-parameters.md").

###### Tip

If you take a snapshot of the DB instance before you start
point-in-time recovery, you might be able to reduce the amount of time
required to apply transactions on the new DB instance. 2. Add the DB instance to the `group_replication_group_seeds` parameter in each DB parameter group
associated with a DB instance in the active-active cluster, including the DB parameter group that you
associated with the new DB instance.

For more information about setting parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 3. In a SQL client, connect to the new DB instance, and call the [mysql.rds_group_replication_set_recovery_channel](mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_set_recovery_channel "mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_set_recovery_channel") stored procedure. Replace
`group_replication_user_password` with the password for the `rdsgrprepladmin` user.

```
call mysql.rds_group_replication_set_recovery_channel('`group_replication_user_password`');
```

4. Using the SQL client, call the [mysql.rds_group_replication_start](mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_start "mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_start") stored procedure to start replication:

```
call mysql.rds_group_replication_start(0);
```

## Adding a DB instance to an active-active cluster using a DB snapshot

You can add a DB instance to an active-active cluster by creating a DB snapshot of a DB instance in the cluster and then
restoring the DB snapshot.

For information about copying a snapshot to a different AWS Region, see [Considerations for cross-Region snapshot copying](USER_CopySnapshot.md#USER_CopySnapshot.AcrossRegions "USER_CopySnapshot.md#USER_CopySnapshot.AcrossRegions").

###### To add a DB instance to an active-active cluster using a DB snapshot

1. Create a DB snapshot of a DB instance in the active-active cluster.

You can create a DB snapshot of any DB instance in the cluster. For instructions, see
[Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md"). 2. Restore a DB instance from the DB snapshot.

During the snapshot restore operation, associate the new DB instance with a DB parameter group that
has the active-active cluster parameters set. For information about the parameters and the required setting for each one,
see [Required parameter settings for active-active clusters](mysql-active-active-clusters-parameters.md "mysql-active-active-clusters-parameters.md").

For information about restoring a DB instance from a DB snapshot, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md"). 3. Add the DB instance to the `group_replication_group_seeds` parameter in each DB parameter group
associated with a DB instance in the active-active cluster, including the DB parameter group that you
associated with the new DB instance.

For more information about setting parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 4. In a SQL client, connect to the new DB instance, and call the [mysql.rds_group_replication_set_recovery_channel](mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_set_recovery_channel "mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_set_recovery_channel") stored procedure. Replace
`group_replication_user_password` with the password for the `rdsgrprepladmin` user.

```
call mysql.rds_group_replication_set_recovery_channel('`group_replication_user_password`');
```

5. Using the SQL client, call the [mysql.rds_group_replication_start](mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_start "mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_start") stored procedure to start replication:

```
call mysql.rds_group_replication_start(0);
```
