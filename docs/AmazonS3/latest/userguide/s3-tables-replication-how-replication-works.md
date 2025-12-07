# How S3 Tables replication

works

S3 Tables replication creates read-only replicas of your Apache Iceberg tables across Regions
and AWS accounts. Replica tables are maintained automatically by the S3 Tables service and
contain the complete data, metadata, and snapshot history from your source table, making them
queryable using any Iceberg-compatible engine for analytics and time-travel operations.

When you configure replication for a table, S3 Tables:

- Creates a read-only replica table in each destination table bucket with the same name and
  namespace as the source table.
- Backfills the replica with the latest state of the source table
- Monitors the source table for new updates
- Commits all updates to replicas in the same order as the source to maintain
  consistency
  For more information, see the following sections.

###### Topics

- [What is replicated](#s3-tables-replication-what-is-replicated "#s3-tables-replication-what-is-replicated")
- [How data is replicated](#s3-tables-replication-how-data-replicated "#s3-tables-replication-how-data-replicated")
- [Snapshot replication](#s3-tables-replication-snapshot-replication "#s3-tables-replication-snapshot-replication")
- [Considerations and
  limitations](#s3-tables-replication-considerations-limitations "#s3-tables-replication-considerations-limitations")

## What is replicated

The following table components are replicated:

- Table snapshots – All snapshots, including compacted
  snapshots, are replicated in chronological order, maintaining parent-child relationships and
  sequence numbers from the source table. This ensures that replica tables provide the same
  time-travel capabilities as source tables.
- Table data – All data files referenced by table
  snapshots are replicated to the destination Region. This includes:
  - Metadata files – Table metadata.json files, manifests, manifest lists, partition statistics and table statistics.
  - Delete files – All delete files are replicated to
    maintain data accuracy in replica tables.
  - Data files – All data files referenced by
    manifests are replicated.

- Table metadata – Complete metadata replication,
  including schema information (current and historical), partition specifications, sort orders,
  and table properties.
  - Schema Information – All table schemas are
    replicated, including the current schema and historical schema versions. This ensures that
    queries against replica tables use the correct column definitions, data types, and field
    mappings. The replication process maintains schema evolution history, allowing time travel
    queries to work correctly on replica tables.
  - Partition Specifications – Current and historical
    partition specifications are replicated, ensuring replica tables maintain the same
    partitioning strategy as source tables.
  - Sort Orders – Table sort orders are replicated to
    maintain query performance optimizations.

## How data is replicated

Replication determines a valid state for replica tables by comparing Apache Iceberg table
metadata between the source and replica tables. Replication processes metadata in
three categories to update your replica table.

### For table metadata

For versioned metadata fields, replication merges values from the source table into the replica table's arrays for the following fields:

- `snapshots` – Merges all snapshots from the source table into the
  replica table's snapshots array by snapshot-id.
- `snapshot-log` – Merges snapshot logs from the source table into the
  replica table's snapshot-log array, sorted by timestamp and snapshot-id.
- `sort-orders` – Merges sort order definitions from the source table
  into the replica table's sort-orders array by order-id.
- `partition-specs` – Merges partition specifications from the source
  table into the replica table's partition-specs array by spec-id.

### For table configuration

For fields that represent table configuration, replication copies values directly from the
source table:

- `properties`
- `partition-statistics`
- `statistics`

Current table state is also transferred from the source table:

- `current-snapshot-id`
- `current-schema-id`
- `last-column-id`
- `last-partition-id`
- `last-sequence-number`
- `default-sort-order-id`
- `next-row-id` (Iceberg V3)
- `encryption-keys` (Iceberg V3)

### Replica-specific state

The following fields are calculated from merged data and updated for the replica
table:

- `location` is updated during replication to point to the correct file location
  in the replica table bucket, ensuring that all file references are valid in the destination
  environment.
- `metadata-log` contains all destination metadata filenames and is updated after every successful replication with the current metadata filename.
- All file paths are modified to point to the replica table locations.

## Snapshot replication

S3 Tables replication maintains complete snapshot history across Regions by replicating all
table snapshots in the same commit order as the source table. The parent-child relationships from
the source table are preserved in the replica table.

### Snapshot retention

You can configure a custom snapshot retention period for your replicated tables that
differs from the retention period of the source. This means that even if snapshots are expired
and no longer available in the source table, they can be preserved in replicas.

For example, if your source table has a 30-day snapshot retention period but your replica
table is configured with a 90-day retention period, the replica will maintain snapshots from the
previous two months that are no longer available in the source table.

Snapshots that you manually expired at the source table are also preserved in the replica
table. For example, if you expired snapshots from February at the source table using a Spark
procedure, you can still time travel to the snapshots in the replica table.

## Considerations and

limitations

The following considerations apply to replicated tables:

- S3 Tables replicates both Iceberg V2 and V3 tables. However, replication of upgraded
  tables (V2 → V3) is not supported.
- Metadata files larger than 500MB are not supported.
- While table updates are typically replicated within minutes, replication can take longer
  depending on the size of the table update to be replicated, for example, when replication
  starts backfilling.
- Tables with tags or branches are not supported.
- Replication is not supported for Amazon S3 Metadata tables or other AWS-generated system
  tables.
- All table snapshots, including compacted snapshots, are replicated from the source table.
  As a result, compaction is not supported on replica tables.
