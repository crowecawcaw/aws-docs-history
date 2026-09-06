

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Detailed Parameter Reference
<a name="detailed-parameter-reference"></a>

The following parameters are available for InfluxDB 3 parameter groups. Most parameters apply to both Core and Enterprise editions. Parameters marked **Enterprise only** are not available in Core.

**Note**  
**Parameters that must not change after initial setup:** The parameters `gen1-duration`, `compaction-gen2-duration`, `compaction-multipliers`, and `gen1-lookback-duration` are persisted in the catalog. Changing them after the cluster's first start causes silent data divergence (deduplication failures, incorrect generation durations). Set these at cluster creation time only. When cloning parameter groups, these values must be copied unchanged.


**Parameter Summary by Edition**  

| Parameter | Category | Edition | 
| --- | --- | --- | 
| num-datafusion-threads | Query Execution | Core, Enterprise | 
| num-io-threads | Query Execution | Core, Enterprise | 
| datafusion-max-parquet-fanout | Query Execution | Core, Enterprise | 
| datafusion-use-cached-parquet-loader | Query Execution | Core, Enterprise | 
| datafusion-config | Query Execution | Core, Enterprise | 
| query-file-limit | Query Execution | Core, Enterprise | 
| query-log-size | Query Execution | Core, Enterprise | 
| exec-mem-pool-bytes | Memory Management | Core, Enterprise | 
| force-snapshot-mem-threshold | Memory Management | Core, Enterprise | 
| parquet-mem-cache-size | Memory Management | Core, Enterprise | 
| disable-parquet-mem-cache | Memory Management | Core, Enterprise | 
| parquet-mem-cache-prune-interval | Memory Management | Core, Enterprise | 
| parquet-mem-cache-prune-percentage | Memory Management | Core, Enterprise | 
| parquet-mem-cache-query-path-duration | Memory Management | Core, Enterprise | 
| preemptive-cache-age | Memory Management | Core, Enterprise | 
| wal-max-write-buffer-size | WAL Configuration | Core, Enterprise | 
| wal-snapshot-size | WAL Configuration | Core, Enterprise | 
| snapshotted-wal-files-to-keep | WAL Configuration | Core, Enterprise | 
| compaction-check-interval | Compaction | Enterprise only | 
| compaction-cleanup-wait | Compaction | Enterprise only | 
| compaction-gen2-duration | Compaction | Enterprise only | 
| compaction-max-num-files-per-plan | Compaction | Enterprise only | 
| compaction-multipliers | Compaction | Enterprise only | 
| compaction-row-limit | Compaction | Enterprise only | 
| gen1-duration | Data Lifecycle | Core, Enterprise | 
| gen1-lookback-duration | Data Lifecycle | Core, Enterprise | 
| delete-grace-period | Data Lifecycle | Core, Enterprise | 
| hard-delete-default-duration | Data Lifecycle | Core, Enterprise | 
| retention-check-interval | Data Lifecycle | Core, Enterprise | 
| distinct-cache-eviction-interval | Caching | Core, Enterprise | 
| distinct-value-cache-disable-from-history | Caching | Enterprise only | 
| last-cache-eviction-interval | Caching | Core, Enterprise | 
| last-value-cache-disable-from-history | Caching | Enterprise only | 
| table-index-cache-concurrency-limit | Table Index Cache | Core, Enterprise | 
| table-index-cache-max-entries | Table Index Cache | Core, Enterprise | 
| max-http-request-size | HTTP and Network | Core, Enterprise | 
| log-filter | Logging | Core, Enterprise | 
| catalog-sync-interval | Catalog and Replication | Enterprise only | 
| replication-interval | Catalog and Replication | Enterprise only | 