

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Storage engine FAQ for Amazon Timestream for InfluxDB 3
<a name="faq-storage-engine"></a>

Questions about the upgraded storage engine for InfluxDB 3. For the full description, upgrade steps, and performance guidance, see [Upgraded storage engine for InfluxDB 3](influxdb3-storage-engine.md).

**What is the upgraded storage engine?**  
It is a new storage engine for InfluxDB 3 that changes how data is written, compacted, and read to improve performance and resource predictability for large and complex time series workloads. It persists data in a new columnar file format, the `.pt` format, in place of Apache Parquet. It reached general availability in InfluxDB 3 Enterprise version 3.11.

**Do new clusters use the upgraded engine by default?**  
Yes. New Amazon Timestream for InfluxDB 3 deployments that run InfluxDB 3 Enterprise version 3.11 or later use the upgraded storage engine by default. You do not need to opt in.

**Do I have to upgrade my existing cluster?**  
No. Existing clusters keep running on the Parquet based engine until you choose to upgrade. The upgrade is an opt in action.

**How do I upgrade an existing cluster?**  
Set the `upgradePachaTree` parameter in a custom DB parameter group and apply that parameter group to your cluster. Take a backup first.

**How do I check migration progress?**  
The update workflow can report the cluster as `AVAILABLE` before the background data migration finishes. To track actual progress, query the `system.upgrade_parquet_node` system table, which reports per-node status such as `running` or `completed` along with the files and bytes still to convert. For details, see [Check migration progress](influxdb3-storage-engine.md#influxdb3-storage-engine-check-progress).

**Will performance be affected during the upgrade?**  
It can be. While the cluster converts existing Parquet data and serves live traffic at the same time, you might see higher query latency and increased CPU, memory, and I/O usage until the migration finishes. Queries still return complete results during the upgrade because the cluster merges results from both Parquet and `.pt` data. Plan the upgrade for a period of lower traffic.

**Can I roll back to Parquet after upgrading?**  
No. On Timestream for InfluxDB 3 the upgrade is irreversible and there is no downgrade command. To return to Parquet storage, restore from a backup taken before the upgrade.

**Is my data safe during the upgrade?**  
The migration runs while the cluster stays online and queries continue to return complete results. As with any major change, take a backup before you start so that you have a known good recovery point.

**Does the upgraded engine change how I write or query data?**  
No. Your write and query interfaces are unchanged. The engine changes how data is stored and processed internally, not the APIs you use.

**Did any configuration parameters change?**  
Yes. The upgraded engine adds parameters such as `wal-buffer-size`, `snapshot-size`, and `snapshot-duration`. Changing any parameter is applied through a DB parameter group and restarts the cluster.