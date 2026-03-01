# Configuring delayed replication with RDS for PostgreSQL

## Overview and Benefits

The delayed replication feature in RDS for PostgreSQL allows you to intentionally delay the
replication of data changes from your primary database to one or more standby (read
replica) servers. This provides valuable protection against data corruption, accidental
data loss, or erroneous transactions that could otherwise be immediately propagated to
all replicas.

Delayed replication is supported in the following RDS for PostgreSQL versions:

- 14.19 and higher 14 versions
- 15.14 and higher 15 versions
- 16.10 and higher 16 versions
- 17.6 and higher 17 versions

By introducing a time lag in the replication process, you gain a window of opportunity
to detect and respond to data-related incidents before they affect your entire DB cluster.
Key benefits of delayed replication include the following:

- Allows you to recover from accidental deletions, updates, or other logical
  mistakes.
- Provides a buffer against the spread of corrupted data across your
  DB cluster.
- Offers an additional recovery point option to complement your traditional
  backup strategies.
- Allows you to configure the delay period based on your organization's specific
  needs and risk tolerance.

## Enabling and Configuring Delayed Replication

To enable delayed replication on an RDS for PostgreSQL read replica, follow these
steps:

###### Note

For cascaded read replicas, use the same `recovery_min_apply_delay`
parameter and steps described below.

###### To enable delayed replication

1. Create a new custom parameter group or modify an existing one. For more
   information, see [DB parameter groups for Amazon RDS DB instances](USER_WorkingWithDBInstanceParamGroups.md "USER_WorkingWithDBInstanceParamGroups.md").
2. In the parameter group, configure the `recovery_min_apply_delay`
   parameter:
   - Set the value to the desired delay in milliseconds. For example,
     3600000 for a 1-hour delay.
   - Allowed range: 0 to 86400000 ms (0 to 24 hours)
   - Default: 0

3. Apply the parameter group to the read replica instance you want to configure
   for delayed replication.
4. Reboot the read replica instance for the changes to take effect.

###### Note

The `recovery_min_apply_delay` parameter is dynamic. If you
modify an existing parameter group that's already attached to the instance,
the changes take effect immediately without requiring a reboot. However,
when applying a new parameter group to the instance, you must reboot for the
changes to take effect.

## Managing Delayed Replication Recovery

Delayed replication is particularly useful in scenarios where traditional
point-in-time recovery methods may be insufficient or too time-consuming.

During the delayed replication period, you can use the following PostgreSQL functions
to manage the recovery process:

- `pg_wal_replay_pause()`: Request to pause the recovery process on
  the delayed replica.
- `pg_wal_replay_resume()`: Restart the recovery process if it was
  previously paused.
- `pg_is_wal_replay_paused()`: Check if the recovery process is
  currently paused.
- `pg_get_wal_replay_pause_state()`: Get the current state of the
  recovery process (not paused, pause requested, or paused).

Users with the `rds_superuser` role have EXECUTE privileges on
`pg_wal_replay_pause()` and `pg_wal_replay_resume()`. If other
database users need access to these functions, you must grant them the
`rds_superuser` role. For more information about the
`rds_superuser` role, see [Understanding the rds_superuser role](Appendix.PostgreSQL.CommonDBATasks.Roles.md "Appendix.PostgreSQL.CommonDBATasks.Roles.md").

Access to other functions like `pg_is_wal_replay_paused()` and
`pg_get_wal_replay_pause_state()` doesn't require the
`rds_superuser` role.

You can use the following recovery target parameters to precisely control the point in
time to which the delayed replica is recovered. These parameters are static and require
a database reboot to apply changes:

- recovery_target
- recovery_target_lsn
- recovery_target_name
- recovery_target_time
- recovery_target_xid
- recovery_target_inclusive

###### Important

You can specify only one recovery target parameter at a time. Configuring multiple
recovery target parameters in the configuration file results in an error.

## Planning considerations

Consider the following when planning delayed replication with RDS for PostgreSQL:

- During the automatic rotation of `rdsrepladmin` credentials (which
  occurs every 90 days), delayed read replicas may temporarily enter a
  `REPLICATION_ERROR` state. If the delayed replica has sufficient
  WAL logs to maintain the configured delay, it may pause WAL receiver process,
  causing WAL accumulation on the source. You should monitor the replication
  status on the replica and the storage consumption on the source to avoid hitting
  storage-full.
- When delayed read replicas encounter system events (such as reboot or
  restart), they enter a `REPLICATION_ERROR` state where the WAL
  receiver process remains inactive until the configured delay period expires.
  This behavior can cause WAL accumulation on the source instance, potentially
  leading to storage exhaustion. Consider the following preventive
  measures:
  - Configure CloudWatch alarms to monitor storage utilization on source
    instances.
  - Enable storage auto-scaling to handle unexpected WAL growth.
  - Set the `max_slot_wal_keep_size` parameter on the source
    instance to limit WAL retention per replication slot.
  - Monitor replication lag and slot status regularly.

- Longer delays increase WAL logs on replicas, consuming more storage. Monitor
  storage space using CloudWatch alarms, enable auto-scaling, or catch up replicas
  when needed.
- When promoting a delayed read replica, the
  `recovery_min_apply_delay` parameter is not honored, and all
  pending WAL records are immediately applied.
- The `recovery_min_apply_delay` parameter is independent on each
  level of a cascading replication setup. Setting a delay on a replica does not
  add to the delay of any cascaded replicas.

For more information, see the [RDS for PostgreSQL Read Replicas
documentation](USER_ReadRepl.md "USER_ReadRepl.md") and the [RDS for PostgreSQL Disaster Recovery documentation](USER_PostgreSQL.md "USER_PostgreSQL.md").

## Understanding limitations

The delayed replication feature for Amazon RDS for PostgreSQL has the following limitations:

- Blue/Green deployments have the following limitations when configuring delayed
  replication:
  - **Green source instance** — The
    `recovery_min_apply_delay parameter` is disregarded, even
    if configured in the parameter group. Any delay settings on the green
    source instance do not take effect.
  - **Green replica instance** — The
    `recovery_min_apply_delay parameter` is fully supported
    and applied to the PostgreSQL configuration file. Delay settings
    function as expected during the switchover workflow.
  - RDS Blue/Green deployments for major version upgrades

- During major version upgrades, any delayed read replicas will be
  automatically terminated to allow the source instance to proceed with
  the upgrade process in order to ensure minimal downtime. After the
  source instance completed the upgrade, you must manually recreate the
  delayed replicas.
- Delayed replication is not compatible with the following features.
  - RDS for PostgreSQL Logical Replication
  - RDS for PostgreSQL Multi-AZ Clusters (including both inbound and outbound
    replication)
  - Aurora PostgreSQL
