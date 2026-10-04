

# SQL functions reference
<a name="aurora-analytics-sql-functions-reference"></a>

These functions let you inspect analytics query performance, resource usage, and cache state, and manage foreign table definitions. Before you use them, install the extension. Run `CREATE EXTENSION aurora_analytics` in each database where you want to use analytics.

**Topics**
+ [aurora\_analytics\_stat\_statements()](#aurora-analytics-func-stat-statements)
+ [aurora\_analytics\_stat\_resource\_usage()](#aurora-analytics-func-stat-resource-usage)
+ [aurora\_analytics\_instance\_metrics()](#aurora-analytics-func-instance-metrics)
+ [aurora\_analytics\_cache\_size()](#aurora-analytics-func-cache-size)
+ [aurora\_analytics\_clear\_cache()](#aurora-analytics-func-clear-cache)
+ [aurora\_analytics\_refresh\_foreign\_table()](#aurora-analytics-func-refresh-foreign-table)
+ [aurora\_analytics\_available\_features()](#aurora-analytics-func-available-features)
+ [aurora\_analytics\_stats\_duckdb\_memory()](#aurora-analytics-func-stats-duckdb-memory)
+ [aurora\_analytics\_remote\_tables()](#aurora-analytics-func-remote-tables)
+ [aurora\_analytics\_iceberg\_snapshots()](#aurora-analytics-func-iceberg-snapshots)
+ [aurora\_analytics\_iceberg\_metadata()](#aurora-analytics-func-iceberg-metadata)
+ [aurora\_analytics\_iceberg\_raw\_metadata()](#aurora-analytics-func-iceberg-raw-metadata)

The following table summarizes the analytics SQL functions.


**Analytics SQL functions**  

| Function | Scope | What it answers | 
| --- | --- | --- | 
| aurora\_analytics\_stat\_statements() | Per normalized query, cumulative | Which queries read from Amazon S3 versus cache, spill to disk, or spend the most CPU. | 
| aurora\_analytics\_stat\_resource\_usage() | Per backend, live | Which backend is consuming memory, worker threads, and spill space right now. | 
| aurora\_analytics\_instance\_metrics() | Whole instance, cumulative since engine start | How much Amazon S3 request and cache activity the instance has done since the engine started. | 
| aurora\_analytics\_cache\_size() | Whole instance, current | The current on-disk read cache size. | 
| aurora\_analytics\_clear\_cache() | Whole instance | Clears the on-disk read cache to free local storage. | 
| aurora\_analytics\_refresh\_foreign\_table() | Per foreign table | Re-infers a foreign table's schema in place from the current source metadata. | 
| aurora\_analytics\_available\_features() | Whole instance, current | Which operators, functions, and types are eligible for analytics engine pushdown. | 
| aurora\_analytics\_stats\_duckdb\_memory() | Per backend, live | How the analytics engine is allocating memory across internal categories for the current backend, and what is spilling to disk. | 
| aurora\_analytics\_remote\_tables() | Per remote catalog and schema | Which tables exist in a remote Amazon S3 Tables namespace or AWS Glue database, and their storage locations. | 
| aurora\_analytics\_iceberg\_snapshots() | Per foreign table | Which Iceberg snapshots exist for a foreign table, for time-travel queries. | 
| aurora\_analytics\_iceberg\_metadata() | Per foreign table | Which Iceberg manifests and data files back a foreign table. | 
| aurora\_analytics\_iceberg\_raw\_metadata() | Per foreign table | The raw Iceberg metadata.json for a foreign table, for debugging or non-standard fields. | 

**Note**  
The diagnostic functions report all byte columns as raw bytes. Wrap these columns in `pg_size_pretty()` for readable output.

## aurora\_analytics\_stat\_statements()
<a name="aurora-analytics-func-stat-statements"></a>

```
aurora_analytics_stat_statements()
```

Returns cumulative analytics performance statistics for each normalized query. Use this function to find which queries read from Amazon S3 rather than from cache, which queries spill to disk, and which queries spend the most CPU time.

**Note**  
By default, this function returns statistics only for the queries that your own role ran. Members of the `rds_superuser` role see statistics for all queries.

The following table describes the return columns.


**Return columns for aurora\_analytics\_stat\_statements()**  

| Column | Type | Description | 
| --- | --- | --- | 
| calls | bigint | The number of times the normalized query ran. | 
| analytics\_cache\_hit\_bytes | bigint | The number of bytes served from the on-disk read cache. | 
| analytics\_remote\_read\_bytes | bigint | The number of bytes read remotely from Amazon S3. | 
| analytics\_total\_disk\_spill | bigint | The number of bytes spilled to temporary local disk storage. | 
| analytics\_total\_cpu\_time | double precision | The total CPU time, in milliseconds, spent running the query. | 
| analytics\_total\_thread\_wait\_time | double precision | The total time, in milliseconds, that worker threads spent waiting. | 

The function also returns the normalized query text for each row.

The following example lists queries that read data, sorted by remote reads from Amazon S3.

```
SELECT calls,
       pg_size_pretty(analytics_cache_hit_bytes) AS cache_hits,
       pg_size_pretty(analytics_remote_read_bytes) AS s3_reads,
       pg_size_pretty(analytics_total_disk_spill) AS spill,
       round(analytics_total_cpu_time::numeric, 2) AS cpu_ms
FROM aurora_analytics_stat_statements()
WHERE analytics_cache_hit_bytes > 0 OR analytics_remote_read_bytes > 0
ORDER BY analytics_remote_read_bytes DESC;
```

Interpret the results as follows.
+ `analytics_cache_hit_bytes` much greater than `analytics_remote_read_bytes` means the cache is warm and most reads are local.
+ `analytics_remote_read_bytes` much greater than `analytics_cache_hit_bytes` means the cache is cold or the working set is too large to fit in the cache.
+ `analytics_total_disk_spill` greater than 0 means the query is spilling to disk because of memory pressure.

For guidance on interpreting these statistics and tuning your workload, see [Monitoring and troubleshooting](aurora-analytics-monitoring-troubleshooting.md) and [Resource management](aurora-analytics-resource-management.md).

## aurora\_analytics\_stat\_resource\_usage()
<a name="aurora-analytics-func-stat-resource-usage"></a>

```
aurora_analytics_stat_resource_usage()
```

Returns a live snapshot of analytics resource usage for each backend. Use this function to find which backend is consuming memory, worker threads, and spill space right now.

The following table describes the return columns.


**Return columns for aurora\_analytics\_stat\_resource\_usage()**  

| Column | Type | Description | 
| --- | --- | --- | 
| pid | integer | The process ID of the backend. | 
| current\_memory\_usage | bigint | The number of bytes of memory that the backend is currently using. | 
| active\_threads | integer | The number of worker threads that the backend is currently running. | 
| disk\_spill\_size | bigint | The number of bytes that the backend has currently spilled to temporary local disk storage. | 

**Note**  
Join `pid` to `pg_stat_activity` to see which query each backend is running.

The following example lists backends that are using memory, sorted by memory usage.

```
SELECT pid,
       pg_size_pretty(current_memory_usage) AS mem_used,
       active_threads,
       pg_size_pretty(disk_spill_size) AS spill
FROM aurora_analytics_stat_resource_usage()
WHERE current_memory_usage > 0
ORDER BY current_memory_usage DESC;
```

## aurora\_analytics\_instance\_metrics()
<a name="aurora-analytics-func-instance-metrics"></a>

```
aurora_analytics_instance_metrics()
```

Returns cumulative analytics metrics for the whole instance since the engine started. Use this function to see how much Amazon S3 request and cache activity the instance has done. The counters reset if the engine restarts.

The following table describes the return columns.


**Return columns for aurora\_analytics\_instance\_metrics()**  

| Column | Type | Description | 
| --- | --- | --- | 
| s3\_head\_request\_count | bigint | The number of HEAD requests that the instance has made to Amazon S3. | 
| s3\_get\_request\_count | bigint | The number of GET requests that the instance has made to Amazon S3. | 
| s3\_cache\_hit\_bytes | bigint | The number of bytes served from the on-disk read cache. | 
| s3\_remote\_read\_bytes | bigint | The number of bytes read remotely from Amazon S3. | 

The following example returns the instance-wide request and cache metrics.

```
SELECT s3_head_request_count,
       s3_get_request_count,
       pg_size_pretty(s3_cache_hit_bytes) AS cache_hit,
       pg_size_pretty(s3_remote_read_bytes) AS s3_read
FROM aurora_analytics_instance_metrics();
```

## aurora\_analytics\_cache\_size()
<a name="aurora-analytics-func-cache-size"></a>

```
aurora_analytics_cache_size()
```

Returns a single `bigint` value that represents the current size, in bytes, of the on-disk read cache for the whole instance. Because the function returns raw bytes, wrap it in `pg_size_pretty()` for readable output.

The following example returns the current cache size.

```
SELECT pg_size_pretty(aurora_analytics_cache_size()) AS cache_size;
```

## aurora\_analytics\_clear\_cache()
<a name="aurora-analytics-func-clear-cache"></a>

```
aurora_analytics_clear_cache()
```

Clears the on-disk read cache for the whole instance to free local storage. After you clear the cache, subsequent queries re-fetch data from Amazon S3.

**Note**  
This function requires the `rds_superuser` role.

The following example clears the read cache.

```
SELECT aurora_analytics_clear_cache();
```

## aurora\_analytics\_refresh\_foreign\_table()
<a name="aurora-analytics-func-refresh-foreign-table"></a>

```
aurora_analytics_refresh_foreign_table(table_name regclass, apply_changes boolean)
```

Re-infers a foreign table's schema in place from the current source metadata, keeping the table definition in sync with the underlying Amazon S3 data. The first argument, `table_name`, is the name or OID of the foreign table. The second argument, `apply_changes`, is a required positional boolean that controls whether the function previews or applies the changes. The function returns a `boolean` value that is `true` on success.
+ `apply_changes = false` performs a dry run and reports what would change without modifying the table.
+ `apply_changes = true` applies the schema changes to the table.

Permission: foreign table owner or `rds_superuser`.

The following example first previews the changes and then applies them.

```
-- Preview the changes
SELECT aurora_analytics_refresh_foreign_table('ft_orders', false);

-- Apply the changes
SELECT aurora_analytics_refresh_foreign_table('ft_orders', true);
```

## aurora\_analytics\_available\_features()
<a name="aurora-analytics-func-available-features"></a>

```
aurora_analytics_available_features()
```

Lists the PostgreSQL operators, functions, and types that the analytics engine supports for vectorized execution pushdown. Use this function to determine which SQL constructs can be pushed down and executed natively rather than falling back to PostgreSQL.

This function takes no arguments.

The following table describes the return columns.


**Return columns for aurora\_analytics\_available\_features()**  

| Column | Type | Description | 
| --- | --- | --- | 
| feature\_type | text | The kind of catalog object: operator, function, or type. | 
| oid | oid | The OID of the operator, function, or type in the corresponding pg\_catalog table. | 
| description | text | Restrictions on the construct's pushdown support, or NULL if unrestricted. | 

Permission: all users.

**Note**  
A query is eligible for full pushdown only when every operator, function, and type it references appears in this function's output with no restricting description. Otherwise, the query falls back to table-scan pushdown.

The following example lists the supported types that have pushdown restrictions.

```
SELECT t.typname, f.description
FROM aurora_analytics_available_features() f
JOIN pg_type t ON f.oid = t.oid
WHERE f.feature_type = 'type' AND f.description IS NOT NULL
ORDER BY t.typname;
```

## aurora\_analytics\_stats\_duckdb\_memory()
<a name="aurora-analytics-func-stats-duckdb-memory"></a>

```
aurora_analytics_stats_duckdb_memory()
```

Reports memory usage and temporary storage usage per internal memory category for the current backend. Use this function to understand how the analytics engine allocates memory across internal components during query execution.

This function takes no arguments.

The following table describes the return columns.


**Return columns for aurora\_analytics\_stats\_duckdb\_memory()**  

| Column | Type | Description | 
| --- | --- | --- | 
| tag | text | The internal memory category label (for example, BASE\_TABLE, HASH\_TABLE). | 
| memory\_usage\_bytes | int8 | The amount of memory currently allocated for this category, in bytes. | 
| temporary\_storage\_bytes | int8 | The amount of data for this category spilled to temporary on-disk storage, in bytes. | 

Permission: all users.

**Note**  
This function reports memory usage for the current backend session only. A non-zero `temporary_storage_bytes` value indicates that the analytics engine is spilling data to disk for that category, which can affect query performance.

The following example returns the memory usage for the current backend.

```
SELECT * FROM aurora_analytics_stats_duckdb_memory();
```

## aurora\_analytics\_remote\_tables()
<a name="aurora-analytics-func-remote-tables"></a>

```
aurora_analytics_remote_tables(catalog text, schema_name text)
```

Discovers the tables available in a remote catalog (an AWS Glue database or an Amazon S3 Tables namespace) and returns their names and storage locations.

This function takes the following arguments.
+ `catalog`: An AWS Glue Data Catalog ARN or Amazon S3 Tables bucket ARN. This is the same catalog value that you use in `IMPORT FOREIGN SCHEMA`.
+ `schema_name`: The name of the schema (AWS Glue database or Amazon S3 Tables namespace) within the catalog. This is the same schema name that you use in `IMPORT FOREIGN SCHEMA`.

The following table describes the return columns.


**Return columns for aurora\_analytics\_remote\_tables()**  

| Column | Type | Description | 
| --- | --- | --- | 
| table\_name | text | The name of the table in the remote schema. | 
| location | text | The AWS Glue table ARN or Amazon S3 Tables table ARN. | 

Permission: `USAGE` privilege on the foreign server.

The following example lists the tables in a remote catalog and schema.

```
SELECT * FROM aurora_analytics_remote_tables('arn:aws:glue:us-east-1:123456789012:catalog', 'my_database');
```

## aurora\_analytics\_iceberg\_snapshots()
<a name="aurora-analytics-func-iceberg-snapshots"></a>

```
aurora_analytics_iceberg_snapshots(table_name regclass)
```

Lists all available Iceberg snapshots for a foreign table. Use this function to discover which snapshots exist before you set the `snapshot` option for time-travel queries.

This function takes one argument, `table_name`, which is the name or OID of an Iceberg foreign table.

The following table describes the return columns.


**Return columns for aurora\_analytics\_iceberg\_snapshots()**  

| Column | Type | Description | 
| --- | --- | --- | 
| sequence\_number | int8 | The Iceberg sequence number for this snapshot. | 
| snapshot\_id | int8 | The snapshot ID. Use this value with the snapshot foreign table option. | 
| timestamp\_ms | timestamp | The timestamp when the snapshot was created. | 
| manifest\_list | text | The path to the manifest list file for this snapshot. | 

Permission: foreign table owner or `rds_superuser`. `SELECT` on the table alone is not sufficient.

The following example lists the five most recent snapshots for a foreign table.

```
SELECT sequence_number, snapshot_id, timestamp_ms
FROM aurora_analytics_iceberg_snapshots('ft_transactions')
ORDER BY sequence_number DESC
LIMIT 5;
```

## aurora\_analytics\_iceberg\_metadata()
<a name="aurora-analytics-func-iceberg-metadata"></a>

```
aurora_analytics_iceberg_metadata(table_name regclass)
```

Lists the Iceberg manifest entries and data files for a foreign table. Use this function for debugging, understanding table layout, or inspecting which data files back a table.

This function takes one argument, `table_name`, which is the name or OID of an Iceberg foreign table.

The following table describes the return columns.


**Return columns for aurora\_analytics\_iceberg\_metadata()**  

| Column | Type | Description | 
| --- | --- | --- | 
| manifest\_path | text | The path to the manifest file. | 
| manifest\_sequence\_number | int8 | The sequence number of the manifest. | 
| manifest\_content | text | The content type of the manifest (data or deletes). | 
| status | text | The status of the entry (existing, added, deleted). | 
| content | text | The content type (data or equality-deletes). | 
| file\_path | text | The full Amazon S3 path of the data file. | 
| file\_format | text | The file format (Parquet, ORC, Avro). | 
| record\_count | int8 | The number of records in this data file. | 

Permission: foreign table owner or `rds_superuser`. `SELECT` on the table alone is not sufficient.

The following example lists the five largest existing data files for a foreign table.

```
SELECT file_path, file_format, record_count, status
FROM aurora_analytics_iceberg_metadata('ft_transactions')
WHERE status = 'EXISTING'
ORDER BY record_count DESC
LIMIT 5;
```

## aurora\_analytics\_iceberg\_raw\_metadata()
<a name="aurora-analytics-func-iceberg-raw-metadata"></a>

```
aurora_analytics_iceberg_raw_metadata(table_name regclass)
```

Returns the raw `metadata.json` of an Iceberg foreign table as a single JSON value. Use this function for debugging or reading non-standard metadata fields that `aurora_analytics_iceberg_snapshots` and `aurora_analytics_iceberg_metadata` don't expose, such as table properties, partition specs, or sort orders.

This function takes one argument, `table_name`, which is the name or OID of an Iceberg foreign table.

This function returns a single `json` value that contains the complete Iceberg `metadata.json` content.

Permission: foreign table owner or `rds_superuser`. `SELECT` on the table alone is not sufficient.

**Note**  
Use PostgreSQL JSON operators to extract specific fields from the result.

The following example returns the raw Iceberg metadata for a foreign table.

```
SELECT aurora_analytics_iceberg_raw_metadata('ft_transactions');
```