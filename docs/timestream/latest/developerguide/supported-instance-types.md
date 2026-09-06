

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Supported Instance Types and Specifications
<a name="supported-instance-types"></a>

The following table lists all supported instance types for Amazon Timestream, along with their hardware specifications. These specifications are critical for determining the optimal parameter group values for your workload.


**Supported Instance Types**  

| Instance Type | vCPUs | Memory (GiB) | Memory (Bytes) | Use Case Profile | 
| --- | --- | --- | --- | --- | 
| db.influx.medium | 1 | 8 | 8,589,934,592 | Dev/test, low-volume workloads | 
| db.influx.large | 2 | 16 | 17,179,869,184 | Light production, small datasets | 
| db.influx.xlarge | 4 | 32 | 34,359,738,368 | Small production workloads | 
| db.influx.2xlarge | 8 | 64 | 68,719,476,736 | Medium production workloads | 
| db.influx.4xlarge | 16 | 128 | 137,438,953,472 | Large production workloads | 
| db.influx.8xlarge | 32 | 256 | 274,877,906,944 | High-throughput production | 
| db.influx.12xlarge | 48 | 384 | 412,316,860,416 | Heavy analytics workloads | 
| db.influx.16xlarge | 64 | 512 | 549,755,813,888 | Maximum r7g capacity | 
| db.influx.24xlarge | 96 | 768 | 824,633,720,832 | Extreme-scale workloads | 

The following table provides recommended parameter values for each instance size. Parameters not listed use the same default across all sizes. For detailed explanations, see [Detailed Parameter Reference](detailed-parameter-reference.md).


**Recommended Parameter Values by Instance Size**  

| Parameter | Medium | Large | XLarge | 2XLarge | 4XLarge | 8XLarge | 12XLarge | 16XLarge | 24XLarge | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| num-datafusion-threads | 1 | 2 | 4 | 8 | 16 | 32 | 48 | 64 | 96 | 
| num-io-threads | 1 | 2 | 4 | 8 | 16 | 32 | 48 | 64 | 96 | 
| datafusion-max-parquet-fanout | 250–500 | 500 | 500–1K | 1K | 1K–2K | 2K–5K | 5K–10K | 5K–10K | 5K–10K | 
| query-file-limit | 100–200 | 200–300 | 300–432 | 432 | 432–600 | 600–800 | 800–1024 | 800–1024 | 1024 | 
| query-log-size | 500 | 1K | 1K | 1K–2K | 2K–5K | 2K–5K | 2K–5K | 2K–5K | 2K–5K | 
| exec-mem-pool-bytes | 20% | 20% | 20% | 20% | 20% | 20% | 20% | 20% | 20% | 
| force-snapshot-mem-threshold | 30% | 30% | 30% | 30% | 30% | 30% | 30% | 30% | 30% | 
| parquet-mem-cache-size | 15% | 20% | 20% | 20% | 25% | 25% | 25% | 25% | 25% | 
| wal-max-write-buffer-size | 50K–100K | 100K | 100K–200K | 200K–300K | 300K–500K | 500K–700K | 500K–800K | 700K–1M | 800K–1M | 
| wal-snapshot-size | 300 | 300 | 300 | 300 | 300 | 300 | 300 | 300 | 300 | 
| compaction-max-num-files-per-plan (Ent.) | 500 | 500 | 500 | 500–1K | 1K–2K | 2K–5K | 5K | 5K–10K | 5K–10K | 
| table-index-cache-concurrency-limit | 8–16 | 16–20 | 20 | 20–24 | 24–32 | 32–48 | 48–64 | 48–64 | 64–100 | 
| max-http-request-size | 5 MiB | 10 MiB | 10 MiB | 10–16 MiB | 10–16 MiB | 10–16 MiB | 10–16 MiB | 10–16 MiB | 10–16 MiB | 

**Note:** Parameters not listed in this table (such as `datafusion-use-cached-parquet-loader`, `disable-parquet-mem-cache`, `parquet-mem-cache-prune-interval`, `compaction-multipliers`, `compaction-row-limit`, cache eviction intervals, and others) use the same recommended default value across all instance sizes. See [Detailed Parameter Reference](detailed-parameter-reference.md) for their defaults.

**Note:** Parameters not listed in the table above use the same recommended default value across all instance sizes. See [Detailed Parameter Reference](detailed-parameter-reference.md) for their defaults.