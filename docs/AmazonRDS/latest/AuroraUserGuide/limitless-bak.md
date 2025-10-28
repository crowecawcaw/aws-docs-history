# Backing up and restoring Aurora PostgreSQL Limitless Database

You can back up and restore a DB cluster that uses Aurora PostgreSQL Limitless Database.

###### Contents

- [Backing up a DB cluster that uses Aurora PostgreSQL Limitless Database](limitless-bak.md#limitless-backup "limitless-bak.md#limitless-backup")
  - [Creating a DB cluster snapshot](limitless-bak.md#limitless-backup-snapshot "limitless-bak.md#limitless-backup-snapshot")

- [Restoring a DB cluster that uses Aurora PostgreSQL Limitless Database](limitless-bak.md#limitless-restore "limitless-bak.md#limitless-restore")
  - [Restoring a DB cluster from a DB snapshot](limitless-bak.md#limitless-restore-snapshot "limitless-bak.md#limitless-restore-snapshot")
  - [Restoring a DB cluster using point-in-time recovery](limitless-bak.md#limitless-restore-pitr "limitless-bak.md#limitless-restore-pitr")

- [PostgreSQL backup and restore utilities not supported](limitless-bak.md#limitless-backup-utilities "limitless-bak.md#limitless-backup-utilities")

## Backing up a DB cluster that uses Aurora PostgreSQL Limitless Database

Backing up a DB cluster with Aurora PostgreSQL Limitless Database has similarities and differences in functionality compared to backing up a standard Aurora DB cluster.

- When you take a manual DB cluster snapshot of an Aurora DB cluster that uses Limitless Database, the snapshot includes data from the DB shard
  group.
- Continuous backups include data from the DB shard group.
- Automated daily snapshots include data from the DB shard group.
- Copying DB cluster snapshots is supported. For more information, see [DB cluster snapshot copying](aurora-copy-snapshot.md "aurora-copy-snapshot.md").
- Sharing DB cluster snapshots is supported. For more information, see [Sharing a DB cluster snapshot](aurora-share-snapshot.md "aurora-share-snapshot.md").
- You can't use the `pg_dump` or `pg_dumpall` utility to back up databases in the DB shard
  group.
- Taking final snapshots when deleting DB clusters is supported for Aurora PostgreSQL Limitless Database.
- Retaining automated backups when deleting DB clusters isn't supported for
  Aurora PostgreSQL Limitless Database.

### Creating a DB cluster snapshot

You create an Aurora PostgreSQL Limitless Database DB cluster snapshot in the same way as for a standard Aurora DB cluster, as shown in the following
AWS CLI example:

```
aws rds create-db-cluster-snapshot \
    --db-cluster-identifier `my-db-cluster` \
    --db-cluster-snapshot-identifier `my-db-cluster-snapshot`
```

For more information on backing up DB clusters, see [Overview of backing up and restoring an Aurora DB
cluster](Aurora.Managing.md "Aurora.Managing.md").

## Restoring a DB cluster that uses Aurora PostgreSQL Limitless Database

Restoring a DB cluster with Aurora PostgreSQL Limitless Database has similarities and differences in functionality compared to restoring a standard Aurora DB cluster.

- You can restore a Limitless Database DB cluster only from a source DB cluster that uses a DB engine version compatible with Limitless Database, such as
  `16.4-limitless`.
- When you restore a DB cluster from a manual snapshot of a DB cluster that uses Limitless Database, the entire DB cluster storage is restored.
  This includes the storage of the DB shard group.

You must create a DB shard group to access the storage for your Limitless Database.

- You can restore a DB cluster using point-in-time recovery (PITR) to any point within the retention period. The restored DB cluster
  includes the storage of the DB shard group.

You must create a DB shard group to access the storage for your Limitless Database.

- PITR isn't supported for deleted Aurora PostgreSQL Limitless Database DB clusters.
- When you restore a DB cluster from an automated daily snapshot, the storage for the DB shard group is also restored.
- When you restore an Aurora PostgreSQL Limitless Database DB cluster, you must enable Enhanced Monitoring and Performance Insights. Make sure to include the Performance Insights KMS key ID.

After you restore an Aurora PostgreSQL Limitless Database DB cluster, make sure to verify its functionality by running your queries on it.

### Restoring a DB cluster from a DB snapshot

The following AWS CLI examples show how to restore an Aurora PostgreSQL Limitless Database DB cluster from a DB cluster snapshot.

You must use the `16.4-limitless` DB engine version.

###### To restore a Limitless Database DB cluster from a DB cluster snapshot

1. Restore the DB cluster:

```
aws rds restore-db-cluster-from-snapshot \
    --db-cluster-identifier `my-new-db-cluster` \
    --snapshot-identifier `my-db-cluster-snapshot` \
    --engine aurora-postgresql \
    --engine-version 16.4-limitless \
    --enable-performance-insights \
    --performance-insights-retention-period `31` \
    --performance-insights-kms-key-id arn:aws:kms:us-east-1:`123456789012`:key/`1234abcd-12ab-34cd-56ef-1234567890ab` \
    --monitoring-interval `5` \
    --monitoring-role-arn arn:aws:iam::`123456789012`:role/`EMrole`
```

2. Create the DB shard group:

```
aws rds create-db-shard-group \
    --db-cluster-identifier my-new-db-cluster \
    --db-shard-group-identifier `my-new-DB-shard-group` \
    --max-acu `1000`
```

For more information, see [Adding a DB shard group to an existing Aurora PostgreSQL Limitless Database DB cluster](limitless-shard-add.md "limitless-shard-add.md").

For more information on restoring Aurora DB clusters from DB cluster snapshots, see
[Restoring from a DB cluster snapshot](aurora-restore-snapshot.md "aurora-restore-snapshot.md").

### Restoring a DB cluster using point-in-time recovery

The following AWS CLI examples show how to restore an Aurora PostgreSQL Limitless Database DB cluster using point-in-time recovery (PITR).

###### To restore a Limitless Database DB cluster using PITR

1. Restore the DB cluster:

```
aws rds restore-db-cluster-to-point-in-time \
    --source-db-cluster-identifier `my-db-cluster` \
    --db-cluster-identifier `my-new-db-cluster` \
    --use-latest-restorable-time \
    --enable-performance-insights \
    --performance-insights-retention-period `31` \
    --performance-insights-kms-key-id arn:aws:kms:us-east-1:`123456789012`:key/`1234abcd-12ab-34cd-56ef-1234567890ab` \
    --monitoring-interval `5` \
    --monitoring-role-arn arn:aws:iam::`123456789012`:role/`EMrole`
```

2. Create the DB shard group:

```
aws rds create-db-shard-group \
    --db-cluster-identifier my-new-db-cluster \
    --db-shard-group-identifier `my-new-DB-shard-group` \
    --max-acu `1000`
```

For more information, see [Adding a DB shard group to an existing Aurora PostgreSQL Limitless Database DB cluster](limitless-shard-add.md "limitless-shard-add.md").

For more information on PITR, see [Restoring a DB cluster to a specified time](aurora-pitr.md "aurora-pitr.md").

## PostgreSQL backup and restore utilities not supported

The following PostgreSQL utilities aren't supported for either the primary DB cluster or the DB shard group:

- `pg_dump`
- `pg_dumpall`
- `pg_restore`

While you might be able to use them by open source binaries or alternative methods, doing so could yield inconsistent
results.
