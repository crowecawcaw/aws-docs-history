For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Aurora/RDS Postgres as a target

This section explains ingesting the S3 staged time-series data into Amazon RDS/Aurora PostgreSQL. The ingestion process will primarily focus on the CSV files generated from Timestream's export tool to ingest into Postgres. We recommend designing the PostgreSQL schema and table with proper indexing strategies for time-based queries. Use any ETL processes to transform Timestream's specialized structures into relational tables optimized for your specific requirements. When migrating Timestream data to a relational database, structure your schema with a timestamp column as the primary time index, measurement identifier columns derived from Timestream's measure_name, and dimension columns from Timestream's dimensions and your actual measures. Create strategic indexes on time ranges and frequently queried dimension combinations to optimize performance during data transformation and loading process. When migrating time-series data to PostgreSQL, proper instance sizing is critical for maintaining query performance at scale. Consider your expected data volume, query complexity, and concurrency requirements when selecting an instance class, with particular attention to memory allocation for time-series aggregation workloads. For datasets exceeding tens of millions of rows, leverage [PostgreSQL's native partitioning capabilities](../../../AmazonRDS/latest/UserGuide/PostgreSQL_Partitions.md "../../../AmazonRDS/latest/UserGuide/PostgreSQL_Partitions.md") and advanced indexing strategies to optimize for time-series access patterns.

We recommend performing functional and performance testing to choose the right instance and [tuning your PostgreSQL database](../../../AmazonRDS/latest/UserGuide/PostgreSQL.md "../../../AmazonRDS/latest/UserGuide/PostgreSQL.md") to address any performance bottlenecks. Performing rigorous data integrity checks through sample query comparisons between your source Timestream database and target system is critical to ensure migration success and maintain query correctness. By executing identical queries against both systems and comparing results — including record counts, aggregations, and outlier values — you can identify any discrepancies that might indicate transformation errors, data loss, or semantic differences in query interpretation. This verification process validates that your data maintains its analytical value post-migration, builds confidence in the new system among stakeholders who rely on these insights, helps identify any necessary query adjustments to accommodate syntax or functional differences between platforms, and establishes a quantifiable baseline for determining when the migration can be considered complete and successful. Without these systematic checks, subtle data inconsistencies might remain undetected, potentially leading to incorrect business decisions or undermining confidence in the entire migration project.

## Ingestion

We recommend using [AWSDatabase Migration Service (DMS)](../../../dms/latest/userguide/Welcome.md "../../../dms/latest/userguide/Welcome.md") with [source as S3](../../../dms/latest/userguide/CHAP_Source.md "../../../dms/latest/userguide/CHAP_Source.md") (both CSV and Parquet are supported) with [PostgreSQL](../../../dms/latest/userguide/CHAP_Target.md "../../../dms/latest/userguide/CHAP_Target.md") as the target. For scenarios where AWS DMS may not be suitable for your specific requirements, we provide a supplementary Python-based utility ([PostgreSQL CSV Ingestion Tool](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/targets/rds_for_postgresql/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/targets/rds_for_postgresql/README.md")) for migrating CSV data from S3 to PostgreSQL.

### Overview of PostgreSQL CSV ingestion tool

The PostgreSQL CSV Ingestion Tool, is a high-performance utility designed to efficiently load CSV files into PostgreSQL databases. It leverages multi-threading and connection pooling to process multiple files in parallel, significantly reducing data loading time. We recommend to running this script using an EC2 instance. Consider using instance types optimized for network operations, such as C5N.

#### Key features

- Multi-threaded Processing: Loads multiple CSV files simultaneously.
- Connection Pooling: Efficiently manages database connections.
- Automatic Column Detection: Dynamically extracts column names from CSV headers.
- Retry Logic: Handles transient errors with exponential backoff.
- File Management; Moves processed files to a designated directory so retrying is resuming but not restarting.
- Comprehensive Logging: Detailed logs for monitoring and troubleshooting.
- Error Notifications: Optional SNS notifications for failures.
- Secure Credentials: Retrieves database passwords from AWS Secrets Manager.

_Prerequisites and installation_

See prerequisites and installation in the [PostgreSQL CSV Ingestion Tool Readme](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/targets/rds_for_postgresql/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/liveanalytics_migration_scripts/targets/rds_for_postgresql/README.md") in GitHub.

_Usage_

```
python copy_postgres.py \
    --database 'postgres_testing' \
    --table 'demolarge_restored' \
    --csv-files-dir '/data/csv_files/*partition*/*.csv' \
    --host database-1.cluster-xxxxxxxx.us-east-1.rds.amazonaws.com \
    --secret-arn 'arn:aws:secretsmanager:<region>:<account_id>:secret:rds!cluster-xxxxx-xx-xx-xx-xxxxxxxx-xxxxx' \
    --sns-topic-arn 'arn:aws:sns:<region>:<account_id>:<topic_name>'
```

_Validation_

You can use DynamoDB for exported rows or logs generated by Timestream's export tool and compare against rows ingested from PostgreSQL Ingestion automation logs. You can do select counts against the source and target tables with the consistent export and import time, if the data is being continuously ingested during the migration process the counts will vary so the recommendation is to compare rows exported and rows important from logging.

_Cleanup_

- Cleanup unloaded data that was created as part of Timestream for LiveAnalytics export tool.
- Delete downloaded data and logs on EC2 to reclaim the space.
- Delete DynamoDB table if used for logging as part of Timestream for LiveAnalytics export tool.
