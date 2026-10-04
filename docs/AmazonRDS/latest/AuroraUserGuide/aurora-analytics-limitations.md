

# Limitations
<a name="aurora-analytics-limitations"></a>

The following limitations apply to foreign tables. For supported engine versions, instance classes, and Regions, see [Querying Apache Iceberg and Parquet data directly in Aurora PostgreSQL](query-iceberg-and-parquet-data.md).

**Topics**
+ [Data modification](#aurora-analytics-limitations-data-modification)
+ [Data format and schema](#aurora-analytics-limitations-data-format)
+ [Query execution](#aurora-analytics-limitations-query-execution)
+ [Infrastructure](#aurora-analytics-limitations-infrastructure)

## Data modification
<a name="aurora-analytics-limitations-data-modification"></a>
+ **Read-only access**: These foreign tables are read-only. `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, and `COPY FROM` operations on foreign tables are not supported. To modify your data, update the source files in Amazon S3 (for Parquet) or update your Iceberg table through AWS Glue or other tools.
+ **Row locking has no effect**: You can include the `FOR UPDATE`, `FOR NO KEY UPDATE`, `FOR SHARE`, and `FOR KEY SHARE` locking clauses in a query, and the query runs and returns rows. This is standard PostgreSQL foreign data wrapper behavior, not specific to this feature.

## Data format and schema
<a name="aurora-analytics-limitations-data-format"></a>
+ **Amazon S3 Multi-Region Access Points not supported**: A foreign table location can be an `s3://` URI, an AWS Glue Data Catalog ARN, or an Amazon S3 Tables ARN. Amazon S3 Multi-Region Access Point (MRAP) ARNs and hostnames are not supported as a foreign table location.
+ **Data type limitations**: Some PostgreSQL data types do not have a supported mapping. `JSONB`, `SERIAL`, array types, network types, range types, geometric types, and `XML` are not supported. For more information, see [Data formats and type mapping](aurora-analytics-type-mapping.md).
+ **Column name length limit**: Column names inferred from Parquet or Iceberg metadata cannot exceed 63 characters (the PostgreSQL `NAMEDATALEN` limit).
+ **Case-insensitive column name collisions**: A foreign table cannot contain two columns whose names differ only in ASCII letter case (for example, `"Foo"` and `"foo"`). If the underlying data contains such columns, rename them in the source data.
+ **Collation restrictions**: Only `C` and `ICU` collations are supported on foreign table column definitions. libc collations (such as `en_US`) and custom collations are not supported on foreign table columns. You can use libc collations at the expression level in queries, but this might reduce pushdown optimization.

## Query execution
<a name="aurora-analytics-limitations-query-execution"></a>
+ **Single-Region data access per query**: You cannot access data from multiple AWS Regions within a single query. All Amazon S3 data accessed in a query must reside in the same Region.
+ **System columns not accessible**: Aurora PostgreSQL does not support PostgreSQL system columns (`ctid`, `xmin`, `xmax`, `cmin`, `cmax`, and `tableoid`) on foreign tables. Referencing one returns the error `[Aurora Analytics] system column is not supported`.

## Infrastructure
<a name="aurora-analytics-limitations-infrastructure"></a>
+ **Cache not persistent across restarts**: The on-disk read cache is cleared when a DB instance restarts or fails over. Subsequent queries re-fetch data from Amazon S3.
+ **Serverless scaling considerations**: With Aurora Serverless v2 deployments, running multiple resource-intensive analytical queries concurrently might exceed the rate at which the DB instance can scale up.