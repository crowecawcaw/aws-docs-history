

# query\_executions
<a name="athena-system-table-query-executions"></a>

The `query_executions` system table contains one row for each completed query execution across all workgroups in your account and Region. It includes data equivalent to the `GetQueryExecution` API response, plus additional columns.

Query metadata is written when a query reaches a final state (`SUCCEEDED`, `FAILED`, `CANCELLED`). No data is written while a query is in the `QUEUED` or `RUNNING` state.

## Table location
<a name="athena-system-table-query-executions-location"></a>

System tables are queried like any other S3 Tables. Here is an example of a query using the fully qualified name of the `query_executions` table:

```
SELECT * FROM "s3tablescatalog/aws-athena"."metadata"."query_executions" LIMIT 10
```

## Columns
<a name="athena-system-table-query-executions-columns"></a>

The following table describes the columns in the `query_executions` system table.


| Column | Type | Description | 
| --- | --- | --- | 
| query\_execution\_id | string | Unique identifier for the query execution. | 
| work\_group\_name | string | The Athena workgroup in which the query ran. | 
| account\_id | string | The 12-digit AWS account ID where the query ran. Leading zeros preserved. | 
| region\_name | string | The AWS Region where the query ran (for example, us-east-1). | 
| query\_string | string | The full SQL query text that was submitted (up to 256 KB). Can contain sensitive data such as PII in WHERE clauses or hardcoded credentials. | 
| execution\_parameters | list of string | Ordered list of parameter values supplied to a parameterized query. NULL if the query was not parameterized. | 
| principal\_arn | string | The IAM principal ARN that submitted the query. Examples: arn:aws:iam::123456789012:user/alice, arn:aws:sts::123456789012:assumed-role/DataAnalyst/session. | 
| submission\_date\_time | timestamp with time zone | When the query was submitted (UTC). | 
| completion\_date\_time | timestamp with time zone | When the query reached its final state (UTC). | 
| state\_enum | string | Final execution state: SUCCEEDED, FAILED, or CANCELLED. | 
| error\_category\_enum | int | Error category if query failed: 1 (system error), 2 (user error), 3 (other). NULL if succeeded. | 
| error\_message | string | Error description if query failed. NULL if succeeded. | 
| error\_type\_enum | int | Numeric error type code (0-9999) for finer-grained classification. NULL if succeeded. | 
| error\_retryable | boolean | Whether the error is retryable. true indicates a transient issue. NULL if succeeded. | 
| statement\_type\_enum | string | High-level statement type: DDL, DML, or UTILITY. | 
| statement\_subtype\_enum | string | Specific statement kind: SELECT, CREATE\_TABLE\_AS\_SELECT, INSERT, UNLOAD, CREATE\_TABLE, DROP\_TABLE, and others. | 
| data\_scanned\_size | long | Bytes of source data scanned. Used to calculate cost in Athena engine version 3. Zero for DDL, cached results, and queries that failed before scanning. | 
| dpu\_count | double | DPUs allocated for queries that run in capacity reservations (Athena engine version 3). NULL otherwise. | 
| total\_execution\_duration | long | Total wall-clock time from submission to completion, in milliseconds. | 
| engine\_execution\_duration | long | Time the query engine spent executing, in milliseconds. Excludes queue, planning, and service processing time. | 
| query\_planning\_duration | long | Time spent planning query execution, in milliseconds. High values indicate too many partitions or complex queries. | 
| query\_queue\_time\_duration | long | Time waiting in queue for resources, in milliseconds. High values indicate concurrency quota reached. | 
| service\_pre\_processing\_duration | long | Time for preprocessing before engine submission, in milliseconds. | 
| service\_processing\_duration | long | Time finalizing and publishing results after engine finished, in milliseconds. | 
| tables\_accessed | list of struct (catalog\_name, database\_name, table\_name) | Tables referenced in the SQL text. Captures syntactic references. This column is an array. To flatten it for analysis, use the [UNNEST](flattening-arrays.md) function. | 
| catalog\_name | string | The catalog name optionally provided as part of the QueryExecutionContext of the StartQueryExecution API call. If none is provided, the default catalog name is AwsDataCatalog. Catalog names provided in the query string override the one from the QueryExecutionContext. | 
| database\_name | string | The database name optionally provided as part of the QueryExecutionContext of the StartQueryExecution API call. If none is provided, the default database name is default. Database names provided in the query string override the one from the QueryExecutionContext. | 
| reused\_previous\_result | boolean | Whether this execution reused a cached result. When true, data\_scanned\_size is 0. | 
| result\_reuse\_enabled | boolean | Whether result reuse (caching) was enabled for this query. | 
| result\_reuse\_max\_age\_in\_minutes | int | Desired maximum age in minutes to reuse a previous result. | 
| effective\_engine\_version | string | The engine version that executed the query (for example, Athena engine version 3). | 
| selected\_engine\_version | string | The engine version configured on the workgroup. | 
| managed\_query\_results\_enabled | boolean | Whether Athena managed query results storage was enabled. | 
| result\_s3\_acl\_option\_enum | string | S3 canned ACL for query results. Currently only BUCKET\_OWNER\_FULL\_CONTROL. | 
| result\_encryption\_option\_enum | string | Encryption for query results: SSE\_S3, SSE\_KMS, or CSE\_KMS. NULL if no encryption configured. | 
| result\_kms\_key\_arn | string | KMS key ARN for encrypting query results (when using SSE\_KMS or CSE\_KMS). | 
| result\_expected\_bucket\_owner\_account\_id | string | AWS account ID expected to own the results S3 bucket. | 
| result\_output\_location | string | S3 URI where query results are stored. | 
| schema\_version | string | Version identifier for the system table schema. | 

## Example queries
<a name="athena-system-table-query-executions-examples"></a>

### Top 10 queries scanning the most data in the past 7 days
<a name="athena-system-table-query-executions-examples-expensive"></a>

```
SELECT
    query_execution_id,
    work_group_name,
    principal_arn,
    data_scanned_size / POWER(1024.0, 3) AS data_scanned_gb,
    total_execution_duration / 1000.0 AS duration_seconds,
    SUBSTR(query_string, 1, 200) AS query_preview
FROM "s3tablescatalog/aws-athena"."metadata"."query_executions"
WHERE submission_date_time >= CURRENT_TIMESTAMP - INTERVAL '7' DAY
    AND state_enum = 'SUCCEEDED'
ORDER BY data_scanned_size DESC
LIMIT 10
```

### Identify who is running queries in a workgroup
<a name="athena-system-table-query-executions-examples-principals"></a>

```
SELECT
    principal_arn,
    COUNT(*) AS query_count,
    SUM(data_scanned_size) / POWER(1024.0, 4) AS total_tb_scanned
FROM "s3tablescatalog/aws-athena"."metadata"."query_executions"
WHERE submission_date_time >= CURRENT_TIMESTAMP - INTERVAL '30' DAY
    AND work_group_name = 'analytics-team'
GROUP BY principal_arn
ORDER BY total_tb_scanned DESC
```

### Most queried tables
<a name="athena-system-table-query-executions-examples-most-queried"></a>

```
SELECT
    t.catalog_name,
    t.database_name,
    t.table_name,
    COUNT(*) AS access_count
FROM "s3tablescatalog/aws-athena"."metadata"."query_executions"
CROSS JOIN UNNEST(tables_accessed) AS t (catalog_name, database_name, table_name)
WHERE submission_date_time >= CURRENT_TIMESTAMP - INTERVAL '30' DAY
GROUP BY t.catalog_name, t.database_name, t.table_name
ORDER BY access_count DESC
LIMIT 20
```

### Query failure patterns
<a name="athena-system-table-query-executions-examples-failures"></a>

```
SELECT
    error_category_enum,
    error_message,
    COUNT(*) AS failure_count,
    COUNT(DISTINCT principal_arn) AS affected_users
FROM "s3tablescatalog/aws-athena"."metadata"."query_executions"
WHERE submission_date_time >= CURRENT_TIMESTAMP - INTERVAL '7' DAY
    AND state_enum = 'FAILED'
GROUP BY error_category_enum, error_message
ORDER BY failure_count DESC
LIMIT 10
```

### Daily data scanned trend by workgroup
<a name="athena-system-table-query-executions-examples-daily-cost"></a>

```
SELECT
    DATE(submission_date_time) AS query_date,
    work_group_name,
    COUNT(*) AS query_count,
    SUM(data_scanned_size) / POWER(1024.0, 4) AS tb_scanned
FROM "s3tablescatalog/aws-athena"."metadata"."query_executions"
WHERE submission_date_time >= CURRENT_TIMESTAMP - INTERVAL '30' DAY
    AND statement_type_enum = 'DML'
GROUP BY DATE(submission_date_time), work_group_name
ORDER BY query_date DESC
```