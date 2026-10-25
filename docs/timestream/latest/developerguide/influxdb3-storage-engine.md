

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Upgraded storage engine for InfluxDB 3
<a name="influxdb3-storage-engine"></a>

 Amazon Timestream for InfluxDB 3 now includes an upgraded storage engine that improves write, compaction, and query performance for large and complex time series workloads. The upgraded engine reached general availability in InfluxDB 3 Enterprise version 3.11. It changes how data is written, compacted, and read, and it is designed to deliver lower query latency and more predictable resource usage for high cardinality tables, wide and sparse schemas, and query heavy access patterns. Data persisted by the upgraded engine uses a new columnar file format, the `.pt` format, in place of Apache Parquet. 

 How the engine is selected depends on whether your cluster is new or already running: 
+ **New deployments** use the upgraded storage engine by default. DB clusters that run InfluxDB 3 Enterprise version 3.11 or later select it automatically, and you do not need to set any parameter to opt in.
+ **Existing clusters**, including any DB cluster created before InfluxDB 3 Enterprise version 3.11, continue to run on the Parquet based engine until you opt in to an upgrade. The upgrade runs in place on your existing cluster.

**Important**  
 On Timestream for InfluxDB 3, upgrading an existing cluster to the upgraded storage engine is a one way change. There is no command to downgrade a cluster back to the Parquet based engine. If you need to return to Parquet storage, restore from a backup that you took before the upgrade. Review the rest of this page, and test on a non production cluster, before you upgrade a production cluster. 

## What the upgraded engine improves
<a name="influxdb3-storage-engine-benefits"></a>

 The upgraded storage engine is built for heavier and more complex time series workloads. It provides: 
+ **Lower query latency** for single series and point lookups.
+ **More predictable resource usage**, with bounded CPU and memory during persistence and compaction.
+ **Support for wide and sparse schemas**, including tables with very large column counts and dynamic schema evolution.
+ **A time series optimized file format** (`.pt`) that applies type specific compression to timestamps, floats, and strings.

 The size of these improvements depends on your workload. Clusters with high cardinality data, wide and sparse schemas, or query heavy access patterns benefit the most. 

## New deployments
<a name="influxdb3-storage-engine-new-deployments"></a>

 When you create a new Timestream for InfluxDB 3 cluster that runs InfluxDB 3 Enterprise version 3.11 or later, the cluster uses the upgraded storage engine by default. No parameter group setting is required to enable it, and no migration step is involved because the cluster has no prior Parquet data to convert. 

## Upgrade an existing cluster
<a name="influxdb3-storage-engine-upgrade-existing"></a>

 Existing clusters stay on the Parquet based engine until you choose to upgrade. The upgrade is an opt in action that you apply through a DB parameter group. When the parameter is applied, the cluster begins migrating its existing Parquet data to the upgraded engine in place. 

 You opt in by setting the `upgradePachaTree` parameter in a custom DB parameter group and applying that parameter group to your cluster. 

**Note**  
 Take a backup of your cluster before you start the upgrade. On Timestream for InfluxDB 3 the upgrade cannot be reversed, so a backup taken before the upgrade is your path back to Parquet storage if you need it. 

## What to expect during the upgrade
<a name="influxdb3-storage-engine-during-upgrade"></a>

 The migration runs while your cluster stays online. During the upgrade, the cluster reads from both the existing Parquet data and the new `.pt` data and merges the results, so queries continue to return complete results while data is being converted. 

 Because the cluster is converting existing data and serving live traffic at the same time, **query and write performance can be affected during the upgrade**. You might see higher query latency and increased CPU, memory, and I/O usage until the migration finishes. Plan the upgrade for a period of lower traffic, and avoid starting it at the same time as other heavy operations such as large backfills. 

 How long the migration takes depends on the volume of existing data the cluster has to convert, so larger clusters take longer to finish. The cluster stays available throughout. We recommend that you upgrade a non production cluster first, monitor query latency and resource metrics in CloudWatch during the migration, and start the upgrade during a period of lower traffic. 

 After the migration finishes, the cluster serves all queries from the upgraded engine, and you should see its steady state benefits, such as lower query latency and more predictable CPU and memory use. 

## Check migration progress
<a name="influxdb3-storage-engine-check-progress"></a>

 When you upgrade an existing cluster, the update workflow can report the cluster as `AVAILABLE` before the data migration has finished. The migration continues in the background after the workflow completes, so an `AVAILABLE` status does not mean the migration is done. To see the actual progress, query the `system.upgrade_parquet_node` system table, which reports migration status for each node in the cluster. 

```
SELECT * FROM system.upgrade_parquet_node
```

 Each node reports its own status. Ingest nodes migrate their write path, and the compactor node converts the stored data, so the per-node conversion counts appear on the compactor. The following example shows a cluster where migration has finished on every node: 

```
node_id    mode        status      conversion_remaining    conversion_bytes_remaining
node-1     ingest      completed   n/a                     n/a
node-2     ingest      completed   n/a                     n/a
node-3     compactor   completed   0                       0
```

 While a migration is in progress, `status` shows `running` and the `conversion_remaining` and `conversion_bytes_remaining` values decrease as data is converted, which you can use to estimate time to completion. The table reports the following columns: 


| Column | Description | 
| --- | --- | 
| status | Migration state of the node: pending, running, completed, or failed. | 
| mode | The node role: ingest or compactor. | 
| conversion\_completed, conversion\_remaining | Number of files already migrated versus files still to migrate. | 
| conversion\_bytes\_remaining | Remaining bytes to migrate. Useful for estimating time to completion. | 
| conversion\_failed | Number of files that failed to convert. | 
| stalled, stalled\_since, last\_progress\_at | Stall detection. Indicates whether progress has stopped and when progress was last made. | 
| import\_windows\_completed, import\_window\_count | Progress through the time-window batches that the migration processes. | 

## Returning to Parquet storage
<a name="influxdb3-storage-engine-reversibility"></a>

 On Timestream for InfluxDB 3, migrating a cluster to the upgraded storage engine is irreversible. There is no downgrade command. If you need to return to Parquet storage, restore from a backup that you took before the upgrade. For backup and restore steps, see [Customer-managed backup and restore](influxdb3-customer-managed-backup-restore.md). 

## Parameter changes
<a name="influxdb3-storage-engine-parameter-changes"></a>

 The upgraded storage engine introduces new tuning parameters for its write ahead log and snapshot behavior. 

### New parameters
<a name="influxdb3-storage-engine-new-parameters"></a>

 The upgraded engine adds configuration parameters for its write ahead log and snapshot behavior. The following parameters and their engine defaults apply to the upgraded engine: 
+ `wal-buffer-size`: Maximum in memory write ahead log buffer before a flush is triggered. Engine default 15MB.
+ `snapshot-size`: Maximum size of the active snapshot bucket before it is rotated. Engine default 250MB.
+ `snapshot-duration`: Time based snapshot rotation trigger. Engine default 10s.

**Note**  
 You set these parameters through a DB parameter group. As with every parameter change on Timestream for InfluxDB 3, applying a new or updated parameter group restarts the cluster, so your cluster is briefly unavailable while the change takes effect. Plan parameter changes for a period of lower traffic. For more information, see [Parameter Groups for DB Clusters in Amazon Timestream](parameter-groups.md). 