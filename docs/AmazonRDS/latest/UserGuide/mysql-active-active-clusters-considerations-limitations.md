# Limitations and considerations for active-active clusters

Active-active clusters in Amazon RDS offer enhanced availability and scalability by
distributing workloads across multiple instances. However, there are important
limitations and considerations to keep in mind when using this architecture.

The following sections outline key factors such as replication delays, conflict
resolution, resource allocation, and failover behavior. Understanding these
considerations can help ensure optimal performance and reliability in active-active
cluster deployments.

###### Topics

- [Limitations for RDS for MySQL active-active clusters](#mysql-active-active-clusters-limitations "#mysql-active-active-clusters-limitations")
- [Considerations and best practices for RDS for MySQL active-active clusters](#mysql-active-active-clusters-considerations "#mysql-active-active-clusters-considerations")

## Limitations for RDS for MySQL active-active clusters

The following limitations apply to active-active clusters for RDS for MySQL:

- The master user name can't be `rdsgrprepladmin` for DB instances in
  an active-active cluster. This user name is reserved for Group Replication
  connections.
- For DB instances with read replicas in active-active clusters, a prolonged replication status other than
  `Replicating` can cause log files to exceed storage limits. For information about the status
  of read replicas, see [Monitoring read replication](USER_ReadRepl.md "USER_ReadRepl.md").
- Blue/green deployments aren't supported for DB instances in an active-active cluster. For more information, see
  [Using Amazon RDS Blue/Green Deployments for database updates](blue-green-deployments.md "blue-green-deployments.md").
- Kerberos authentication isn't supported for DB instances in an active-active cluster. For more information, see
  [Using Kerberos authentication for Amazon RDS for MySQL](mysql-kerberos.md "mysql-kerberos.md").
- The DB instances in a Multi-AZ DB cluster can't be added to an
  active-active cluster. However, the DB instances in a Multi-AZ DB instance
  deployment can be added to an active-active cluster. For more information,
  see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md").
- Tables that don't have a primary key aren't replicated in an active-active cluster because writes
  are rejected by the Group Replication plugin.
- Non-InnoDB tables aren't replicated in an active-active cluster.
- Active-active clusters don't support concurrent DML and DDL statements on different DB instances
  in the cluster.
- You can't configure an active-active cluster to use single-primary mode for the group's replication mode.
  For this configuration, we recommend using a Multi-AZ DB cluster instead. For more information, see
  [Multi-AZ DB cluster deployments for Amazon RDS](multi-az-db-clusters-concepts.md "multi-az-db-clusters-concepts.md").
- Multi-source replication isn't supported for DB instances in an active-active cluster.
- A cross-Region active-active cluster can't enforce certificate authority (CA)
  verification for Group Replication connections.

## Considerations and best practices for RDS for MySQL active-active clusters

Before you use RDS for MySQL active-active clusters, review the following considerations
and best practices:

- Active-active clusters can't have more than nine DB instances.
- With the Group Replication plugin, you can control the transaction consistency
  guarantees of the active-active cluster. For more information, see [Transaction Consistency Guarantees](https://dev.mysql.com/doc/refman/8.0/en/group-replication-consistency-guarantees.html "https://dev.mysql.com/doc/refman/8.0/en/group-replication-consistency-guarantees.html") in the MySQL
  documentation.
- Conflicts are possible when different DB instances update the same row in an active-active
  cluster. For information about conflicts and conflict resolution, see
  [Group Replication](https://dev.mysql.com/doc/refman/8.0/en/group-replication-summary.html "https://dev.mysql.com/doc/refman/8.0/en/group-replication-summary.html") in the MySQL documentation.
- For fault tolerance, include at least three DB instances in your active-active
  cluster. It is possible to configure an active-active cluster with only one or
  two DB instances, but the cluster won't be fault tolerant. For information about
  fault tolerance, see [Fault-tolerance](https://dev.mysql.com/doc/refman/8.0/en/group-replication-fault-tolerance.html "https://dev.mysql.com/doc/refman/8.0/en/group-replication-fault-tolerance.html") in the MySQL documentation.
- When a DB instance joins an existing active-active cluster and is running the
  same engine version as the lowest engine version in the cluster, the DB instance
  joins in read-write mode.
- When a DB instance joins an existing active-active cluster and is running a
  higher engine version than the lowest engine version in the cluster, the DB
  instance must remain in read-only mode.
- If you enable Group Replication for a DB instance by setting its
  `rds.group_replication_enabled` parameter to `1` in
  the DB parameter group, but replication hasn't started or has failed to start,
  the DB instance is placed in super-read-only mode to prevent data
  inconsistencies. For information about super-read-only mode, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_super_read_only "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_super_read_only").
- You can upgrade a DB instance in an active-active cluster, but the DB instance is read-only until
  all of the other DB instances in the active-active cluster are upgraded to same engine version or
  a higher engine version. When you upgrade a DB instance, the DB instance automatically joins the
  same active-active cluster when the upgrade completes. To avoid an unintended switch to read-only mode for a DB instance,
  disable automatic minor version upgrades for it. For information about upgrading a MySQL DB instance, see
  [Upgrades of the RDS for MySQL DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").
- You can add a DB instance in a Multi-AZ DB instance deployment to an existing
  active-active cluster. You can also convert a Single-AZ DB instance in an
  active-active cluster to a Multi-AZ DB instance deployment. If a primary DB
  instance in a Multi-AZ deployment fails, that primary instance fails over to the
  standby instance. The new primary DB instance automatically joins the same
  cluster after failover completes. For more information about Multi-AZ DB
  instance deployments, see [Multi-AZ DB instance deployments for Amazon RDS](Concepts.md "Concepts.md").
- We recommend that the DB instances in an active-active cluster have different
  time ranges for their maintenance windows. This practice avoids multiple DB
  instances in the cluster going offline for maintenance at the same time. For
  more information, see [Amazon RDS maintenance window](USER_UpgradeDBInstance.md#Concepts.DBMaintenance "USER_UpgradeDBInstance.md#Concepts.DBMaintenance").
- Active-active clusters can use SSL for connections between DB instances. To
  configure SSL connections, set the [group_replication_recovery_use_ssl](https://dev.mysql.com/doc/refman/8.0/en/group-replication-system-variables.html#sysvar_group_replication_recovery_use_ssl "https://dev.mysql.com/doc/refman/8.0/en/group-replication-system-variables.html#sysvar_group_replication_recovery_use_ssl") and [group_replication_ssl_mode](https://dev.mysql.com/doc/refman/8.0/en/group-replication-system-variables.html#sysvar_group_replication_ssl_mode "https://dev.mysql.com/doc/refman/8.0/en/group-replication-system-variables.html#sysvar_group_replication_ssl_mode") parameters. The values for these
  parameters must match for all DB instances in the active-active cluster.

Currently, active-active clusters don't support certificate authority (CA) verification for
connections between AWS Regions. So, the [group_replication_ssl_mode](https://dev.mysql.com/doc/refman/8.0/en/group-replication-system-variables.html#sysvar_group_replication_ssl_mode "https://dev.mysql.com/doc/refman/8.0/en/group-replication-system-variables.html#sysvar_group_replication_ssl_mode") parameter must be set to `DISABLED` (the default) or `REQUIRED`
for cross-Region clusters.

- An RDS for MySQL active-active cluster runs in multi-primary mode. The default
  value of the [group_replication_enforce_update_everywhere_checks](https://dev.mysql.com/doc/refman/8.0/en/group-replication-system-variables.html#sysvar_group_replication_enforce_update_everywhere_checks "https://dev.mysql.com/doc/refman/8.0/en/group-replication-system-variables.html#sysvar_group_replication_enforce_update_everywhere_checks") is
  `ON` and the parameter is static. When this parameter is set to
  `ON`, applications can't insert into a table that has cascading
  foreign key constraints.
- An RDS for MySQL active-active cluster uses the MySQL communication stack for connection security instead of
  XCOM. For more information, see [Communication Stack for Connection Security Management](https://dev.mysql.com/doc/refman/8.0/en/group-replication-connection-security.html "https://dev.mysql.com/doc/refman/8.0/en/group-replication-connection-security.html") in the MySQL documentation.
- When a DB parameter group is associated with a DB instance in an active-active
  cluster, we recommend only associating this DB parameter group with other DB
  instances that are in the cluster.
- Active-active clusters only support RDS for MySQL DB instances. These DB
  instances must be running supported versions of the DB engine.
- When a DB instance in an active-active cluster has an unexpected failure, RDS
  starts recovery of the DB instance automatically. If the DB instance doesn't
  recover, we recommend replacing it with a new DB instance by performing a
  point-in-time recovery with a healthy DB instance in the cluster. For
  instructions, see [Adding a DB instance to an active-active cluster using point-in-time recovery](mysql-active-active-clusters-adding.md#mysql-active-active-clusters-adding-pitr "mysql-active-active-clusters-adding.md#mysql-active-active-clusters-adding-pitr").
- You can delete a DB instance in an active-active cluster without affecting the other DB instances
  in the cluster. For information about deleting a DB instance, see [Deleting a DB instance](USER_DeleteInstance.md "USER_DeleteInstance.md").
- When a DB instance unintentionally leaves an active-active cluster, by default
  the `group_replication_exit_state_action` parameter changes to
  `OFFLINE_MODE`. In this state, the DB instance is
  inaccessible and you must reboot the DB instance to bring it back online and
  to rejoin the cluster. You can change this behavior by modifying the
  `group_replication_exit_state_action` parameter in a custom
  parameter group. By setting the parameter to `READ_ONLY`, when
  the DB instance unintentionally leaves a cluster, it enters a super
  read-only state rather than going offline.
