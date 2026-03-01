# Setting up PostgreSQL logical replication with Multi-AZ DB clusters for Amazon RDS

By using PostgreSQL logical replication with your Multi-AZ DB cluster, you can replicate
and synchronize individual tables rather than the entire database instance. Logical
replication uses a publish and subscribe model to replicate changes from a source to one or
more recipients. It works by using change records from the PostgreSQL write-ahead log (WAL).
For more information, see [Performing logical replication for Amazon RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.md "PostgreSQL.Concepts.General.FeatureSupport.md").

When you create a new logical replication slot on the writer DB instance of a Multi-AZ DB cluster, the slot is
asynchronously copied to each reader DB instance in the cluster. The slots on the reader DB instances
are continuously synchronized with those on the writer DB instance.

Logical replication is supported for Multi-AZ DB clusters running RDS for PostgreSQL
version 14.8-R2 and higher, and 15.3-R2 and higher.

###### Note

In addition to the native PostgreSQL logical replication feature, Multi-AZ DB clusters running RDS for PostgreSQL
also support the `pglogical` extension.

For more information about PostgreSQL logical replication, see [Logical
replication](https://www.postgresql.org/docs/current/logical-replication.html "https://www.postgresql.org/docs/current/logical-replication.html") in the PostgreSQL documentation.

###### Topics

- [Prerequisites](#multi-az-db-clusters-logical-replication-prereqs "#multi-az-db-clusters-logical-replication-prereqs")
- [Setting up logical replication](#multi-az-db-clusters-logical-replication "#multi-az-db-clusters-logical-replication")
- [Limitations and recommendations](#multi-az-db-clusters-logical-replication-limitations "#multi-az-db-clusters-logical-replication-limitations")

## Prerequisites

To configure PostgreSQL logical replication for Multi-AZ DB clusters, you must meet the following
prerequisites.

- Your user account must be a member of the `rds_superuser` group and have
  `rds_superuser` privileges. For more information, see [Understanding PostgreSQL roles and permissions](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md").
- Your Multi-AZ DB cluster must be associated with a custom DB cluster parameter
  group so that you can configure the parameter values described in the following
  procedure. For more information, see [Working with DB cluster parameter groups for Multi-AZ DB clusters](USER_WorkingWithDBClusterParamGroups.md "USER_WorkingWithDBClusterParamGroups.md").

## Setting up logical replication

To set up logical replication for a Multi-AZ DB cluster, you enable specific
parameters within the associated DB cluster parameter group, then create logical
replication slots.

###### Note

Starting with PostgreSQL version 16, you can use reader DB instances of the Multi-AZ DB cluster for logical
replication.

###### To set up logical replication for an RDS for PostgreSQL Multi-AZ DB cluster

1.  Open the custom DB cluster parameter group associated with your RDS for PostgreSQL Multi-AZ DB cluster.
2.  In the **Parameters** search field, locate the
    `rds.logical_replication` static parameter and set its value to
    `1`. This parameter change can increase WAL generation, so enable
    it only when you’re using logical slots.
3.  As part of this change, configure the following DB cluster parameters.

        * `max_wal_senders`
        * `max_replication_slots`
        * `max_connections`

    Depending on your expected usage, you might also need to change the values of
    the following parameters. However, in many cases, the default values are
    sufficient.

        * `max_logical_replication_workers`
        * `max_sync_workers_per_subscription`

4.  Reboot the Multi-AZ DB cluster for the parameter values to take effect. For
    instructions, see [Rebooting a Multi-AZ DB cluster and reader DB instances for Amazon RDS](multi-az-db-clusters-concepts-rebooting.md "multi-az-db-clusters-concepts-rebooting.md").
5.  Create a logical replication slot on the writer DB instance of the Multi-AZ DB cluster as explained in [Working with logical replication slots](PostgreSQL.Concepts.General.FeatureSupport.md#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplicationSlots "PostgreSQL.Concepts.General.FeatureSupport.md#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplicationSlots"). This process requires that you specify a decoding plugin. Currently,
    RDS for PostgreSQL supports the `test_decoding`, `wal2json`,
    and `pgoutput` plugins that ship with PostgreSQL.

The slot is asynchronously copied to each reader DB instance in the cluster. 6. Verify the state of the slot on all reader DB instances of the Multi-AZ DB cluster. To do so, inspect the
`pg_replication_slots` view on all reader DB instances and make sure
that the `confirmed_flush_lsn` state is making progress while the
application is actively consuming logical changes.

The following commands demonstrate how to inspect the replication state on the reader
DB instances.

```
% psql -h test-postgres-instance-2.abcdefabcdef.us-west-2.rds.amazonaws.com

postgres=> select slot_name, slot_type, confirmed_flush_lsn from pg_replication_slots;
  slot_name   | slot_type | confirmed_flush_lsn
--------------+-----------+---------------------
 logical_slot | logical   | 32/**`D0001700`**
(1 row)

postgres=> select slot_name, slot_type, confirmed_flush_lsn from pg_replication_slots;
  slot_name   | slot_type | confirmed_flush_lsn
--------------+-----------+---------------------
 logical_slot | logical   | 32/**`D8003628`**
(1 row)

% psql -h test-postgres-instance-3.abcdefabcdef.us-west-2.rds.amazonaws.com

postgres=> select slot_name, slot_type, confirmed_flush_lsn from pg_replication_slots;
  slot_name   | slot_type | confirmed_flush_lsn
--------------+-----------+---------------------
 logical_slot | logical   | 32/**`D0001700`**
(1 row)

postgres=> select slot_name, slot_type, confirmed_flush_lsn from pg_replication_slots;
  slot_name   | slot_type | confirmed_flush_lsn
--------------+-----------+---------------------
 logical_slot | logical   | 32/**`D8003628`**
(1 row)
```

After you complete your replication tasks, stop the replication process, drop replication
slots, and turn off logical replication. To turn off logical replication, modify your
DB cluster parameter group and set the value of `rds.logical_replication` back to
`0`. Reboot the cluster for the parameter change to take effect.

## Limitations and recommendations

The following limitations and recommendations apply to using logical replication with Multi-AZ DB clusters
running PostgreSQL version 16:

- You can use only writer DB instances to create or drop logical replication slots. For example,
  the `CREATE SUBSCRIPTION` command must use the cluster writer
  endpoint in the host connection string.
- You must use the cluster writer endpoint during any table synchronization or
  resynchronization. For example, you can use the following commands to
  resynchronize a newly added table:

```
`Postgres=>`ALTER SUBSCRIPTION `subscription-name` CONNECTION host=`writer-endpoint`
`Postgres=>`ALTER SUBSCRIPTION `subscription-name` REFRESH PUBLICATION
```

- You must wait for table synchronization to complete before using the reader DB instances for
  logical replication. You can use the `pg_subscription_rel` catalog table to monitor table
  synchronization. Table synchronization is complete when the
  `srsubstate` column is set to ready (`r`).
- We recommend using instance endpoints for the logical replication connection once initial
  table synchronization is complete. The following command reduces load on the
  writer DB instance by offloading replication to one of the reader DB instances:

```
`Postgres=>`ALTER SUBSCRIPTION `subscription-name` CONNECTION host=`reader-instance-endpoint`
```

You can't use the same slot on more than one DB instance at a time. When two or more
applications are replicating logical changes from different DB instances in the
cluster, some changes might be lost due to a cluster failover or network issue.
In these situations, you can use instance endpoints for logical replication in
the host connection string. The other application using the same configuration
will show the following error message:

```
replication slot `slot_name` is already active for PID `x` providing immediate feedback.
```

- While using the `pglogical` extension, you can only use the cluster writer
  endpoint. The extension has known limitations that can create unused logical
  replication slots during table synchronization. Stale replication slots reserve
  write-ahead log (WAL) files and can lead to disk space problems.
