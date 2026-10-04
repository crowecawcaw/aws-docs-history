

# Configuration parameters
<a name="aurora-analytics-configuration-parameters"></a>

You can configure analytics behavior and performance using PostgreSQL configuration parameters. You can set these parameters at the session, database, user, or DB cluster parameter group level using standard PostgreSQL commands.

**Topics**
+ [aurora\_analytics.enabled](#aurora-analytics-param-enabled)
+ [aurora\_analytics.query\_mem](#aurora-analytics-param-query-mem)
+ [aurora\_analytics.lowercase\_unquoted\_column\_name](#aurora-analytics-param-lowercase)
+ [aurora\_analytics.skip\_unsupported\_columns](#aurora-analytics-param-skip-unsupported)
+ [aurora\_analytics.enable\_logging](#aurora-analytics-param-enable-logging)
+ [aurora\_analytics.logging\_level](#aurora-analytics-param-logging-level)
+ [aurora\_analytics.track\_detailed\_metrics](#aurora-analytics-param-track-detailed-metrics)

The following table lists all analytics configuration parameters.


**Analytics configuration parameters**  

| Parameter name | Description | Default | Modifiable by | 
| --- | --- | --- | --- | 
| aurora\_analytics.enabled | Enables the aurora\_analytics extension | false | Parameter group | 
| aurora\_analytics.query\_mem | (KB) Sets the maximum memory that a single aurora\_analytics query can use. | Derived (for example, 4GB) | Any user | 
| aurora\_analytics.lowercase\_unquoted\_column\_name | Lowercases unquoted column names when inferring aurora\_analytics foreign table columns. | true | Any user | 
| aurora\_analytics.skip\_unsupported\_columns | Skips columns with unsupported data types or conflicting names when inferring aurora\_analytics foreign table columns. | false | Any user | 
| aurora\_analytics.enable\_logging | Enables logging for aurora\_analytics. | true | rds\_superuser | 
| aurora\_analytics.logging\_level | Sets detailed logging for aurora\_analytics. | WARNING | rds\_superuser | 
| aurora\_analytics.track\_detailed\_metrics | Collects detailed per-query performance metrics for aurora\_analytics. | false | Any user | 

## aurora\_analytics.enabled
<a name="aurora-analytics-param-enabled"></a>

Enables the `aurora_analytics` extension.


**Properties for aurora\_analytics.enabled**  

| Property | Value | 
| --- | --- | 
| Default | false | 
| Valid values | true, false | 
| Type | Boolean | 
| Apply type | Dynamic | 
| Scope | DB cluster parameter group | 

This parameter is the primary switch for the analytics feature. Set it to `true` in your DB cluster parameter group to enable the feature. Because it's a dynamic parameter, the change is applied immediately without a reboot. Once enabled, you can install the extension (`CREATE EXTENSION aurora_analytics`) in each database.

## aurora\_analytics.query\_mem
<a name="aurora-analytics-param-query-mem"></a>

(KB) Sets the maximum memory that a single `aurora_analytics` query can use.


**Properties for aurora\_analytics.query\_mem**  

| Property | Value | 
| --- | --- | 
| Default | Derived from instance memory (for example, 4GB) | 
| Valid values | String with unit (for example, '2GB', '16GB') or integer in kilobytes (kB) | 
| Type | Memory | 
| Context | User-settable | 
| Scope | Session, user, database, parameter group | 

This parameter controls the maximum memory that the analytics execution engine allocates for processing a single query. This memory is used for hash tables, sorting, aggregation buffers, and intermediate results. You can specify the value as a string with a unit suffix (for example, `'4GB'`) or as an integer in kilobytes (kB), where 1 kB is 1024 bytes, following the PostgreSQL memory-unit convention.

When a query's memory usage approaches this limit, the engine spills intermediate results to temporary local storage. Spilling allows the query to complete but with reduced performance.

Aurora derives the default from instance memory, using the smallest of three terms:

```
query_mem = LEAST(
    48 GiB,                                  -- ceiling for the derived default
    DBInstanceClassMemory x 12.5%,           -- lower bound on smaller instances
    DBInstanceClassMemory x 3.125% + 8 GiB   -- lower bound on larger instances
)
```

The following table shows approximate default values by instance class:


**Default query\_mem by instance class**  

| Instance class | Instance memory | Default `query_mem` | 
| --- | --- | --- | 
| db.r8gd.large | 16 GB | \~2 GB | 
| db.r8gd.xlarge | 32 GB | \~4 GB | 
| db.r8gd.2xlarge | 64 GB | \~8 GB | 
| db.r8gd.4xlarge | 128 GB | \~12 GB | 
| db.r8gd.8xlarge | 256 GB | \~16 GB | 
| db.r8gd.16xlarge | 512 GB | \~24 GB | 

These values are approximate because the derivation uses `DBInstanceClassMemory`, which is slightly lower than the instance class's nominal memory.

**Note**  
`SHOW aurora_analytics.query_mem` returns the value you requested, not necessarily the value the engine uses. The effective limit is capped at instance memory minus the memory reserved for the engine's shared structures. Setting a larger value succeeds, but the engine still uses the capped value.

When to increase this value:
+ Queries fail with out-of-memory errors.
+ You run complex aggregations and joins that process millions of rows.
+ Few concurrent analytical sessions are running.

When to decrease this value:
+ Many concurrent users run analytical queries.
+ You observe memory pressure across the DB instance.

Set different limits for different user roles:

```
-- Heavy analytics users
ALTER USER data_scientist SET aurora_analytics.query_mem = '16GB';
-- Light reporting users
ALTER USER dashboard_user SET aurora_analytics.query_mem = '8GB';
```

Use a session-level setting for a specific complex query:

```
SET aurora_analytics.query_mem = '16GB';
SELECT complex_aggregation FROM ft_large_table;
RESET aurora_analytics.query_mem;
```

**Note**  
As a best practice, make sure that `concurrent_sessions x query_mem` doesn't exceed approximately 30% of instance memory.

## aurora\_analytics.lowercase\_unquoted\_column\_name
<a name="aurora-analytics-param-lowercase"></a>

Lowercases unquoted column names when inferring `aurora_analytics` foreign table columns.


**Properties for aurora\_analytics.lowercase\_unquoted\_column\_name**  

| Property | Value | 
| --- | --- | 
| Default | true | 
| Valid values | true, false | 
| Type | Boolean | 
| Context | User-settable | 
| Scope | Session, user, database, parameter group | 

When Aurora PostgreSQL infers the schema of a foreign table (created with empty parentheses), it reads column names from Parquet or Iceberg metadata. Parquet files often contain mixed-case column names such as `OrderDate` or `CustomerID`.

When set to `true` (default), column names are lowercased to follow PostgreSQL's standard unquoted identifier behavior. For example, `OrderDate` becomes `orderdate`.

When set to `false`, mixed-case column names are preserved. You must use double-quoted identifiers to reference them (for example, `SELECT "OrderDate" FROM ft_orders`).

**Note**  
Leave this parameter at `true` (default) for the most natural PostgreSQL experience.

## aurora\_analytics.skip\_unsupported\_columns
<a name="aurora-analytics-param-skip-unsupported"></a>

Skips columns with unsupported data types or conflicting names when inferring `aurora_analytics` foreign table columns.


**Properties for aurora\_analytics.skip\_unsupported\_columns**  

| Property | Value | 
| --- | --- | 
| Default | false | 
| Valid values | true, false | 
| Type | Boolean | 
| Context | User-settable | 
| Scope | Session, user, database, parameter group | 

When set to `false` (default), Aurora PostgreSQL raises an error if it encounters an unsupported column type during schema inference.

When set to `true`, unsupported columns are silently skipped. The foreign table is created with only the supported columns, allowing you to query the remaining data.

Set this parameter to `true` when your source data contains a mix of supported and unsupported column types and you only need a subset of columns.

## aurora\_analytics.enable\_logging
<a name="aurora-analytics-param-enable-logging"></a>

Enables logging for `aurora_analytics`.


**Properties for aurora\_analytics.enable\_logging**  

| Property | Value | 
| --- | --- | 
| Default | true | 
| Valid values | true, false | 
| Type | Boolean | 
| Context | rds\_superuser only | 
| Scope | Session, user, database, parameter group | 

When enabled, the analytics engine writes diagnostic messages to the PostgreSQL error log at the verbosity level specified by `aurora_analytics.logging_level`.

## aurora\_analytics.logging\_level
<a name="aurora-analytics-param-logging-level"></a>

Sets detailed logging for `aurora_analytics`.


**Properties for aurora\_analytics.logging\_level**  

| Property | Value | 
| --- | --- | 
| Default | WARNING | 
| Valid values | DEBUG5, DEBUG4, DEBUG3, DEBUG2, DEBUG1, INFO, NOTICE, WARNING, ERROR, LOG, FATAL, PANIC | 
| Type | Enum | 
| Context | rds\_superuser only | 
| Scope | Session, user, database, parameter group | 

This parameter controls the verbosity of analytics engine messages written to the PostgreSQL error log. Use `DEBUG1` or higher for troubleshooting. Use `WARNING` (default) or `ERROR` for production workloads to minimize log volume.

This parameter requires `aurora_analytics.enable_logging` to be set to `true`.

## aurora\_analytics.track\_detailed\_metrics
<a name="aurora-analytics-param-track-detailed-metrics"></a>

Collects detailed per-query performance metrics for `aurora_analytics`.


**Properties for aurora\_analytics.track\_detailed\_metrics**  

| Property | Value | 
| --- | --- | 
| Default | false | 
| Valid values | true, false | 
| Type | Boolean | 
| Context | User-settable | 
| Scope | Session, user, database, parameter group | 

When enabled, Aurora PostgreSQL collects detailed per-query metrics such as cache hit ratios and data transfer statistics. You can retrieve these metrics using the analytics statistics functions.

Enable this parameter when you need to analyze cache performance or diagnose slow queries. For more information, see [Resource management](aurora-analytics-resource-management.md).