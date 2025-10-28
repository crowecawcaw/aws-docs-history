# Managing logical slot synchronization for RDS for PostgreSQL

Starting in community PostgreSQL 17, a new feature to automatically synchronize
logical replication slots from primary to standby servers has been introduced
through the parameter `sync_replication_slots` or the related function
`pg_sync_replication_slots()`, which manually synchronizes slots on
execution.

These features are available starting with RDS for PostgreSQL 17. A typical setup will
have a primary instance and its [read replica](USER_PostgreSQL.Replication.md "USER_PostgreSQL.Replication.md"), as well
as a logical replication subscriber to the primary.

Ensure the subscription is created with the failover option set to true:

```
CREATE SUBSCRIPTION `subname` CONNECTION 'host=...' PUBLICATION `pubname` WITH (failover = true);
```

This creates a logical slot on the publisher with failover enabled.

```
postgres=> SELECT slot_name, slot_type, failover FROM pg_catalog.pg_replication_slots;
 slot_name | slot_type | failover
-----------+-----------+----------
 subname   | logical   | t
(1 row)
```

By enabling slot synchronization, all of the failover logical replication slots on
the primary are automatically created on the physical standbys and are synced
periodically. Ensure the following values have been set through [parameter
groups](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"):

- `rds.logical_replication` must be `1` to enable
  logical replication
- `hot_standby_feedback` must be `1` on the
  standby
- `rds.logical_slot_sync_dbname` on the standby must be set to a
  valid database name

The parameter's default value is `postgres`. If the logical
publishing instance has the `postgres` database, the default
parameter does not need to be changed.

- `synchronized_standby_slots` on the primary must be set to the
  physical replication slot of the standby intended to be in-sync
- `sync_replication_slots` must be `1` to enable
  automatic synchronization
  With a failover-enabled subscription slot and the above parameter values, when a
  standby is promoted, the subscriber can alter its subscription to this newly
  promoted instance and continue logical replication seamlessly.
