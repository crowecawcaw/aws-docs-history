

# Migrating tables to S3 Tables
<a name="s3-tables-migrate"></a>

S3 Tables can migrate AWS Glue-registered Apache Hive tables stored as Apache Parquet in Amazon S3 general purpose buckets to managed Apache Iceberg tables in S3 Tables. S3 Tables automatically copy your data to a new table and convert Hive data types to Iceberg types. Small files are combined into larger ones and data is compressed, so your tables are optimized for storage cost and query performance. You don't need to provision or manage any compute, and your source table remains unchanged and fully available for both reads and writes during a migration job. Migration doesn't move your source objects stored in S3 Intelligent-Tiering to the Frequent Access tier or reset their days since last access. You can migrate tables by using the Amazon S3 console, the AWS CLI, the S3 Tables API, or the S3 Tables migration skill.

For more information, see [How to migrate a table to S3 Tables](s3-tables-migrate-how-it-works.md).

## Features
<a name="s3-tables-migrate-features"></a>

**Optimized destination table**  
Migration compresses or recompresses your data and compacts small files, so your destination table is optimized for both storage cost and query performance. You can configure the compression codec, target file size, and snapshot management settings, or use the defaults. For more information, see [Setting up table migration](s3-tables-migrate-setting-up.md).

**Incremental sync before cutover**  
You don't need to stop writes to your source table. After the initial migration is complete, you can sync the table to migrate changes from your source table to keep the destination table current, and minimize cutover downtime.

**Automatic Hive-to-Iceberg conversion**  
Migration maps your Hive schema and partitioning to an Iceberg schema and partition spec. You can either specify a destination schema to choose the columns and data types you want or let migration generate a compatible Iceberg schema based on the AWS Glue-registered schema. The migration policy controls how migration handles any data type or schema mismatches, while also automatically performing predefined data type conversions between compatible Hive and Iceberg types. For more information, see [Migration policy](s3-tables-migrate-how-it-works.md#s3-tables-migrate-migration-policies).

**Migration review, reports, and statistics**  
Migration produces reports and statistics that you can use to review your source table and track progress. Before copying data, the migration job writes compatibility reports that list issues to resolve. By default, the migration job continues automatically after planning. You can choose to pause and review the reports before any data is copied. After the copy, the object migration report shows the result for each source object. You can also check migration statistics at any time to see how a start or sync is progressing. For more information, see [Migration reports and statistics](s3-tables-migrate-reports.md).

For more information about table migration, see the following topics.
+ [How to migrate a table to S3 Tables](s3-tables-migrate-how-it-works.md)
  + [Data type mappings for table migration](s3-tables-migrate-data-type-mappings.md)
  + [Migration reports and statistics](s3-tables-migrate-reports.md)
+ [Setting up table migration](s3-tables-migrate-setting-up.md)
+ [Running a table migration](s3-tables-migrate-running.md)