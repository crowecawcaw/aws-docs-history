

# Removing a DB instance from an active-active cluster
<a name="mysql-active-active-clusters-remove"></a>

When you remove a DB instance from an active-active cluster, it reverts to a standalone DB instance.

**To remove a DB instance from an active-active cluster**

1. Connect to the DB instance in a SQL client, and call the [mysql.rds\_group\_replication\_stop](mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_stop) stored procedure:

   ```
   call mysql.rds_group_replication_stop();
   ```

1. Modify the `group_replication_group_seeds` parameter for the DB instances that will remain in the active-active cluster.

   In the `group_replication_group_seeds` parameter, delete the DB instance that you are removing from the active-active cluster. For more information about setting parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.Modifying.md).

1. Modify the parameters of the DB instance you are removing from the active-active cluster so that it is no longer part of the cluster.

   You can either associate the DB instance with a different parameter group, or modify the parameters in the DB parameter group associated with the DB instance. The parameters to modify include `group_replication_group_name`, `rds.group_replication_enabled`, and `group_replication_group_seeds`. For more information about active-active cluster parameters, see [Required parameter settings for active-active clusters](mysql-active-active-clusters-parameters.md).

   If you modify the parameters in a DB parameter group, make sure the DB parameter group isn't associated with other DB instances in the active-active cluster.

1. Reboot the DB instance you removed from the active-active cluster for the new parameter settings to take effect.

   For instructions, see [Rebooting a DB instance](USER_RebootInstance.md).