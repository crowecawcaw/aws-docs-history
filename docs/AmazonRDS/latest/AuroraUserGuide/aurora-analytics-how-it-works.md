

# How it works
<a name="aurora-analytics-how-it-works"></a>

Aurora PostgreSQL runs your analytical queries inside your DB cluster, reading Iceberg and Parquet data directly from Amazon S3, without moving it into Aurora or running a separate system. You point a PostgreSQL foreign table at your data in Amazon S3, Amazon S3 Tables, or the AWS Glue Data Catalog, then query it with standard SQL. The foreign table stores only metadata (schema and location); no data is copied into Aurora.

When your application submits a query that references a foreign table, PostgreSQL parses and plans the query, then delegates execution to DuckDB, the open-source columnar analytical engine embedded directly in the PostgreSQL server.

For Iceberg tables, the engine resolves the corresponding snapshot and its data files through the AWS Glue Data Catalog or Amazon S3 Tables. Using the IAM role attached to your DB cluster, the engine reads only the byte ranges it needs from Amazon S3 or Amazon S3 Tables. Predicate pushdown and column pruning skip row groups and columns your query does not reference. Frequently accessed data is cached on the DB instance's local storage and shared across sessions, allowing repeated queries to be served locally instead of reading from Amazon S3 again. The engine returns results as standard PostgreSQL rows to your application.

Queries that join foreign tables with local Aurora PostgreSQL tables run within a single process and see your session's uncommitted writes, participating in your transactions like any other PostgreSQL query. Your driver, ORM, or BI tool treats a foreign table like any regular Aurora PostgreSQL table.

The following diagram shows an overview of the capability.

![Overview of Aurora PostgreSQL querying Iceberg and Parquet data in a data lake. An application connects to the Aurora PostgreSQL endpoint and runs SQL against foreign tables. The embedded DuckDB analytics engine resolves Iceberg snapshots through the AWS Glue Data Catalog or Amazon S3 Tables, reads data directly from Amazon S3 using the IAM role attached to the DB cluster, caches frequently accessed data on local instance storage, and returns results as standard PostgreSQL rows.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-analytics-overview.png)


## Key concepts
<a name="aurora-analytics-concepts"></a>

The following concepts are central to querying Iceberg and Parquet data in Aurora PostgreSQL.
+ **Foreign tables**: PostgreSQL tables you define that point to your Apache Parquet or Apache Iceberg data in Amazon S3, Amazon S3 Tables, or the AWS Glue Data Catalog. Foreign tables behave like regular PostgreSQL tables, but the underlying data stays in your data lake. For more information, see [Working with foreign tables](aurora-analytics-foreign-tables.md).
+ **Analytics engine**: A columnar analytical engine that executes analytical queries against foreign-table data. Aurora PostgreSQL uses DuckDB, embedded directly in the PostgreSQL server. Because the engine runs in-process with PostgreSQL, there is nothing separate to install or manage.
+ **Query memory**: The working memory the analytics engine uses to run a query, set by the `aurora_analytics.query_mem` parameter. Its default is derived from your instance's memory. For more information, see [Query memory](aurora-analytics-resource-management.md#aurora-analytics-query-memory).
+ **Worker threads**: The CPU parallelism the engine uses to run a query. Aurora scales worker threads automatically from the query's memory budget. For more information, see [Worker threads](aurora-analytics-resource-management.md#aurora-analytics-worker-threads).
+ **Amazon S3 read cache**: A cache of frequently accessed Amazon S3 data on the DB instance's local storage (NVMe or Amazon EBS). The cache is shared across all sessions on the DB instance. For more information, see [On-disk read cache](aurora-analytics-resource-management.md#aurora-analytics-on-disk-read-cache).

## Key capabilities
<a name="aurora-analytics-capabilities"></a>

The following capabilities are supported:

### Data access and formats
<a name="aurora-analytics-capabilities-data-access"></a>
+ Query Apache Parquet and Apache Iceberg data stored in Amazon S3, Amazon S3 Tables, and the AWS Glue Data Catalog. For Iceberg tables managed in external Iceberg REST Catalog-compatible catalogs, use AWS Glue Data Catalog federation.
+ Reference data by Amazon S3 URI, AWS Glue Data Catalog ARN, or Amazon S3 Tables ARN. For AWS Glue Data Catalog locations, the data format is detected automatically from catalog metadata.
+ When you create a foreign table with an empty column list, column names and data types are automatically inferred from the Parquet or Iceberg metadata and mapped to PostgreSQL-compatible types.
+ For Iceberg tables, query the latest snapshot, a specific snapshot by ID, or as of a specific timestamp (time travel).
+ Query data in an AWS Region different from where your Aurora PostgreSQL DB cluster is deployed.

### Query execution and optimization
<a name="aurora-analytics-capabilities-query-execution"></a>
+ Predicate pushdown and column pruning minimize the data read from Amazon S3. `WHERE` filters are applied at the scan, using Parquet and Iceberg statistics to skip row groups and files that cannot match. Only the columns your query references are fetched.
+ Entire query plans, including joins between foreign tables and local PostgreSQL tables, can be pushed to the analytics engine for maximum performance.
+ Supported SQL features include aggregations (`COUNT`, `SUM`, `AVG`), grouping and filtering (`GROUP BY`, `WHERE`, `ORDER BY`), joins between foreign tables and PostgreSQL tables, common table expressions (CTEs), prepared statements (`PREPARE`/`EXECUTE`), and query plan analysis with `EXPLAIN` and `EXPLAIN ANALYZE`.
+ Materialize query results into a PostgreSQL table or materialized view with `CREATE TABLE AS SELECT` and `CREATE MATERIALIZED VIEW AS SELECT`.
+ When a query exceeds its memory budget, intermediate results spill automatically to local storage so that the query completes.

### Monitoring
<a name="aurora-analytics-capabilities-monitoring"></a>
+ Monitor and troubleshoot analytical workloads with the same tools that you use for Aurora PostgreSQL. Amazon CloudWatch reports instance-level cache hit rates, memory usage, disk spills, and Amazon S3 activity.
+ `EXPLAIN` and `EXPLAIN ANALYZE` show which parts of a query run in the analytics engine, along with filter pushdown and column projection. SQL functions report per-query and instance-wide metrics such as cache hits, bytes read from Amazon S3, and bytes spilled to disk.
+ Time spent in the analytics engine is reported through the `Extension:AuroraAnalyticsExecute` wait event. Analytical queries appear in the average active sessions (AAS) chart in Amazon CloudWatch Database Insights and Performance Insights alongside the rest of your PostgreSQL workload.

### Compatibility
<a name="aurora-analytics-capabilities-compatibility"></a>
+ Coexists with other Aurora PostgreSQL extensions in the same database, and works with standard PostgreSQL client tools and utilities.