

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Migrating to Amazon Timestream for InfluxDB 3
<a name="migration-to-influxdb3"></a>

Amazon Timestream for InfluxDB 3 Enterprise is the recommended migration target for most LiveAnalytics workloads. It provides standard SQL and InfluxQL query support, unlimited cardinality, multi-node scaling, and a built-in Python processing engine.

## Key differences from LiveAnalytics
<a name="influxdb3-migration-key-differences"></a>


| Feature | LiveAnalytics | InfluxDB 3 Enterprise | 
| --- | --- | --- | 
| Architecture | Serverless, fully managed | Instance-based clusters (db.influx.\* family) | 
| Storage | Automatic memory \+ magnetic tiers | Amazon S3 object storage (Apache Parquet) | 
| Query language | Custom Timestream SQL dialect | Standard SQL \+ InfluxQL | 
| Write protocol | AWS SDK (WriteRecords API) | Line Protocol over HTTPS (port 443) | 
| Scaling | Automatic | Manual: choose instance size \+ node count | 
| Cardinality | Automatic partitioning | Unlimited (no series key index) | 
| Processing | Scheduled queries | Built-in Python processing engine (plugins, triggers) | 
| Auth model | IAM for data-plane | Token-based authentication (Admin Token at provisioning) | 
| Pricing | Per-write, per-query, per-GB stored | Per-instance-hour \+ included Amazon S3 I/O \+ InfluxData license (Marketplace) | 
| Availability SLA | 99.99% | 99.9% (multi-node, multi-AZ) | 
| Regions | 10 regions (frozen) | 19\+ regions (expanding) | 

## Instance types available
<a name="influxdb3-migration-instance-types"></a>


| Instance | vCPUs | Memory | 
| --- | --- | --- | 
| db.influx.large | 2 | 8 GB | 
| db.influx.xlarge | 4 | 16 GB | 
| db.influx.2xlarge | 8 | 32 GB | 
| db.influx.4xlarge | 16 | 64 GB | 
| db.influx.8xlarge | 32 | 128 GB | 
| db.influx.12xlarge | 48 | 192 GB | 

## Editions
<a name="influxdb3-migration-editions"></a>

InfluxDB 3 Core  
Single-node, open-source engine, no license fee. Good for development, testing, and smaller workloads.

InfluxDB 3 Enterprise  
Multi-node clusters (up to 15 nodes), InfluxData Marketplace license required. Recommended for production workloads at scale. Supports configurable node modes (INGEST, QUERY, COMPACT, PROCESS, or ALL).

## Feature mapping
<a name="influxdb3-migration-feature-mapping"></a>


| LiveAnalytics feature | InfluxDB 3 equivalent | 
| --- | --- | 
| Scheduled Queries (downsampling) | Processing Engine scheduled triggers (Python plugins) | 
| Memory Store (recent data) | WAL buffer \+ Last Value Cache | 
| Magnetic Store (historical data) | Amazon S3 Parquet files (compacted) | 
| Multi-measure records | Multiple fields per line protocol point | 
| Dimension-based partitioning | Tag-based automatic partitioning | 
| UNLOAD to Amazon S3 | Export API (table-level Parquet export) | 
| Cross-region replication | Not available (use multi-AZ within region) | 
| AWS Backup integration | Automated backups (snapshot-based) | 
| VPC Endpoints | Private clusters deployed in customer VPC | 
| AWS KMS encryption | Encryption at rest (AWS managed keys; CMK support available) | 

## Steps to migrate from LiveAnalytics to InfluxDB 3
<a name="influxdb3-migration-steps"></a>

1. **Assess your workload:** Identify write throughput (records/sec), query patterns (point queries vs. aggregations), cardinality, and data retention needs. If using Scheduled Queries in LiveAnalytics, plan to replace with InfluxDB 3 Processing Engine plugins.

1. **Provision your InfluxDB 3 cluster:** Choose Core (single-node) or Enterprise (multi-node) based on throughput needs. Create via AWS Console, AWS CLI, or CloudFormation. Select instance size based on write throughput and query concurrency.

1. **Update write path:** LiveAnalytics uses the `WriteRecords` API (AWS SDK). InfluxDB 3 uses **Line Protocol** over HTTPS. Update Telegraf outputs, application code, or IoT Rules to write via Line Protocol to the cluster endpoint. Batch writes with 5,000–10,000 points per batch, sorted by tag keys alphabetically.

1. **Update query path:** LiveAnalytics custom SQL maps to InfluxDB 3 standard SQL with key differences: use `time` column directly (no `measure_value::double` pattern), use `WHERE time > now() - INTERVAL '1 hour'` instead of `ago()`. Use Flight SQL (port 443) for programmatic access or InfluxQL for Grafana dashboards.

1. **Migrate historical data:** Export from LiveAnalytics using `UNLOAD` to Amazon S3 (Parquet or CSV). Import into InfluxDB 3 using Line Protocol writes. For the export step, follow the instructions in [Exporting Timestream data to Amazon S3](export-timestream-data.md). Bulk import from Parquet files is on the roadmap for a future release.

1. **Update monitoring:** Replace LiveAnalytics CloudWatch metrics with InfluxDB 3 CloudWatch metrics (`CPUUtilization`, `MemoryUtilization`, `S3ObjectStorageBytes`). Additional metrics are available via the `/metrics` Prometheus endpoint on the cluster.

1. **Update networking and auth:** LiveAnalytics uses IAM for data-plane auth. InfluxDB 3 uses **token-based auth** (Admin Token created at cluster provisioning). IAM-based data-plane auth for InfluxDB 3 is not yet available. The cluster must be deployed in a VPC with appropriate security groups.

## Additional resources
<a name="influxdb3-migration-resources"></a>
+ [Getting started with InfluxDB 3](https://docs.aws.amazon.com/timestream/latest/developerguide/influxdb3.html)
+ [InfluxDB 3 DB Clusters](https://docs.aws.amazon.com/timestream/latest/developerguide/influxdb3-managing-clusters.html)
+ [InfluxDB 3 Processing Engine](https://docs.influxdata.com/influxdb3/enterprise/process-data/)
+ [Line Protocol Reference](https://docs.influxdata.com/influxdb3/enterprise/reference/line-protocol/)
+ [SQL Reference for InfluxDB 3](https://docs.influxdata.com/influxdb3/enterprise/reference/sql/)