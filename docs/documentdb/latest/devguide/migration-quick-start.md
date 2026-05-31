# Migrate to Amazon DocumentDB using AWS Database Migration Service (DMS): Quick Start Guide

###### Topics

- [Prepare the DMS source](#migrate-qs-dma-source "#migrate-qs-dma-source")
- [Setup DMS](#migrate-qs-dms-setup "#migrate-qs-dms-setup")
- [Enable DocumentDB compression](#migrate-qs-comp "#migrate-qs-comp")
- [Create a replication task](#migrate-qs-create "#migrate-qs-create")
- [Monitor progress](#migrate-qs-monitor "#migrate-qs-monitor")
- [Additional information](#migrate-qs-info "#migrate-qs-info")

## Prepare the DMS source

See [Enabling change streams](change_streams.md#change_streams-enabling "change_streams.md#change_streams-enabling") to enable DocumentDB change streams or enable the MongoDB Oplog to support DMS Change Data Capture (CDC).

- The DMS source must retain all ongoing changes until DMS full load completes for all included collections.
- DocumentDB change streams are time based. Make sure your `change_stream_log_retention_duration` setting is large enough to cover the time to complete the full load.
- The MongoDB Oplog is a fixed size. Make sure it is sized to hold all operations during full load.

## Setup DMS

Create DMS instance, source, and target endpoints and test each endpoint.

## Enable DocumentDB compression

Enable compression by attaching a custom parameter group to your DocumentDB cluster and updating default_collection_compression parameter to enabled.
See [Managing collection-level document compression](doc-compression.md "doc-compression.md") for more information.

## Create a replication task

1. In the DMS console, in the navigation pane, choose **Migrate or replicate**, then choose **Tasks**.
2. Choose **Create task**.
3. On the **Create task** page, in the **Task configuration** section:
   - Enter a unique and meaningful **Task identifier** (for example, "mongodb-docdb-replication").
   - Choose the source endpoint you created previously in the **Source database endpoint** drop-down menu.
   - Choose the target endpoint you created previously in the **Target database endpoint** drop-down menu.
   - For **Task type**, choose **Migrate and replicate**.

4. In the **Settings** section:
   - For **Task logs**, check the **Turn on CloudWatch** logs box.
   - For **Editing mode** (at the top of the section), choose **JSON editor** and set the following attributes:
     - Set `ParallelApplyThreads` to 5 (under `TargetMetadata`).
       This enables ~1000 insert/update/delete ops per second in CDC.
     - Set `MaxFullLoadSubTasks` to 16 (under `FullLoadSettings`).
       Consider increasing this depending on your instance size.
     - For large collections (over 100 GB), enable auto-partition (under Table Mapping and under the `parallel-load` attribute):
       - "type": "partitions-auto"
       - "number-of-partitions": 16

## Monitor progress

Use the AWS DMS console or create a custom dashboard ([dashboarder tool](https://github.com/awslabs/amazon-documentdb-tools/tree/master/monitoring/docdb-dashboarder "https://github.com/awslabs/amazon-documentdb-tools/tree/master/monitoring/docdb-dashboarder")) to track migration.
Focus on the following metrics:

- **FullLoadThroughputBandwidthTarget** — Measures the network bandwidth (in KB/second) used by DMS when transferring data to the target database during the full load phase of migration.
- **CDCLatencyTarget** — Measures the time delay (in seconds) bewteen when a change occurs in the source database and when that change is applied to the target database.
- **CDCThroughputRowsTarget** — Measures the number of rows per second that DMS is applying to the target database during the ongoing replication phase of migration.

## Additional information

For more information about Amazon DocumentDB and AWS DMS, see:

See for more information.

- [Amazon DocumentDB migration runbook](docdb-migration-runbook.md "docdb-migration-runbook.md")
- [Migrating from MongoDB to Amazon DocumentDB](../../../dms/latest/sbs/chap-mongodb2documentdb.md "../../../dms/latest/sbs/chap-mongodb2documentdb.md")
