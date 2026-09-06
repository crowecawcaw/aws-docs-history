

# Scenario Discovery query language reference
<a name="sd-query-language"></a>

## Query workflow
<a name="sd-query-workflow"></a>

Scenario Discovery uses an asynchronous query model with three API operations:
+ **StartQuery** — Submit a SQL query against a workspace. Returns a `queryId` and initial status `SUBMITTED`.
+ **DescribeQuery** — Poll the query status using the `queryId`. Status progresses through: `SUBMITTED` → `RUNNING` → `COMPLETED` (or `FAILED` / `CANCELING` / `CANCELED`).
+ **GetQueryResults** — Retrieve column metadata and paginated result rows once the query is `COMPLETED`. Set `maxResults` to 10,000 for best performance.

You can also use `CancelQuery` to cancel a running query, and `ListQueries` to list queries for a workspace.

### Example workflow
<a name="sd-query-workflow-example"></a>

```
# 1. Start a query
aws iotsitewise start-query \
  --region $REGION \
  --workspace-name "my-workspace" \
  --query-statement "SELECT * FROM raw_time_series LIMIT 10"
# Response: { "queryId": "abc-123", "status": "SUBMITTED" }

# 2. Poll for completion
aws iotsitewise describe-query \
  --region $REGION \
  --workspace-name "my-workspace" \
  --query-id "abc-123"
# Response: { "queryId": "abc-123", "status": "COMPLETED", ... }

# 3. Get results (paginated)
aws iotsitewise get-query-results \
  --region $REGION \
  --workspace-name "my-workspace" \
  --query-id "abc-123" \
  --max-results 10000
# Response: { "columnInfo": [...], "rows": [...], "nextToken": "..." }
```

## Query constraints
<a name="sd-query-constraints"></a>


| Parameter | Constraint | 
| --- | --- | 
| workspaceName | 1–64 characters, pattern ^[a-zA-Z0-9\_-]\+$ | 
| queryStatement | 1–10,240 characters | 
| clientToken | 36–64 characters (optional, for idempotency) | 
| maxResults | Pagination page size for GetQueryResults (recommended: 10,000) | 

## Query statuses
<a name="sd-query-statuses"></a>


| Status | Description | 
| --- | --- | 
| SUBMITTED | Query accepted, waiting to execute | 
| RUNNING | Query is executing | 
| COMPLETED | Query finished successfully — results available | 
| FAILED | Query failed — check error message | 
| CANCELED | Query was canceled by the user | 
| CANCELING | Cancel request received, query is stopping | 

## Reference tables
<a name="sd-query-reference-tables"></a>

Scenario Discovery provides four queryable tables within each workspace. All queries are scoped to the workspace specified in the `StartQuery` request.

### raw\_time\_series
<a name="sd-query-table-raw-time-series"></a>

Contains timestamped telemetry data ingested into the workspace.


| Column | Data Type | Description | 
| --- | --- | --- | 
| dataset\_id | STRING | ID of the dataset containing this data | 
| series\_id | STRING | Timeseries ID (UUID) | 
| alias | STRING | Property alias path (for example, /sensor/temperature) | 
| event\_timestamp | TIMESTAMP | Timestamp of the data point | 
| nanosecond\_offset | INTEGER | Sub-microsecond offset in nanoseconds | 
| version | INTEGER | Data version number | 
| data\_type | STRING | Value type (for example, JSON, DOUBLE, STRING) | 
| string\_value | STRING | String value (when data\_type is STRING) | 
| long\_value | BIGINT | Long integer value | 
| double\_value | DOUBLE | Double precision floating point value | 
| boolean\_value | BOOLEAN | Boolean value | 
| binary\_value | BINARY | Binary value | 
| array\_value | VARIANT | Array value (semi-structured data) | 
| struct\_value | VARIANT | Struct/object value (semi-structured data) | 

### annotations
<a name="sd-query-table-annotations"></a>

Contains OpenLABEL annotation data associated with video or sensor streams. Each row corresponds to the annotation data for a single video frame.


| Column | Data Type | Description | 
| --- | --- | --- | 
| dataset\_id | STRING | ID of the dataset containing this annotation | 
| series\_id | STRING | Timeseries ID (UUID) | 
| alias | STRING | Property alias path (for example, /annotations/front\_left) | 
| event\_timestamp | TIMESTAMP | Timestamp of the annotation frame | 
| nanosecond\_offset | INTEGER | Sub-microsecond offset in nanoseconds | 
| frame\_id | STRING | Frame identifier | 
| openlabel\_version | STRING | OpenLABEL schema version | 
| streams | VARIANT | Stream metadata (semi-structured) | 
| objects | VARIANT | Detected objects with bounding boxes, types, and attributes (semi-structured) | 
| contexts | VARIANT | Scene context information (semi-structured) | 
| updated\_at | TIMESTAMP | Last update timestamp | 

### dataset
<a name="sd-query-table-dataset"></a>

Contains metadata about datasets in the workspace.


| Column | Data Type | Description | 
| --- | --- | --- | 
| dataset\_id | STRING | Dataset ID (UUID) | 
| dataset\_external\_id | STRING | External identifier | 
| dataset\_type | STRING | Dataset type (for example, SESSION, CURATED) | 
| dataset\_payload | VARIANT | Dataset configuration payload (semi-structured) | 
| dataset\_source | STRING | Dataset source type | 
| name | STRING | Dataset name | 
| description | STRING | Dataset description | 
| version | INTEGER | Dataset version number | 
| created\_at | TIMESTAMP | Creation timestamp | 
| updated\_at | TIMESTAMP | Last update timestamp | 
| metadata | VARIANT | User-defined metadata key-value pairs | 

### datasegment
<a name="sd-query-table-datasegment"></a>

Contains metadata about data segments (timeseries references) within datasets.


| Column | Data Type | Description | 
| --- | --- | --- | 
| source\_dataset\_id | STRING | ID of the source SESSION dataset | 
| dataset\_id | STRING | ID of the dataset this segment belongs to | 
| timeseries\_id | STRING | Timeseries ID (UUID) | 
| start\_time | TIMESTAMP | Segment start timestamp | 
| end\_time | TIMESTAMP | Segment end timestamp | 
| alias | STRING | Property alias path | 
| data\_type | STRING | Data type (for example, VIDEO, ANNOTATION, JSON) | 
| start\_time\_nanosecond\_offset | INTEGER | Sub-microsecond offset in nanoseconds | 
| end\_time\_nanosecond\_offset | INTEGER | Sub-microsecond offset in nanoseconds | 

## Supported data types
<a name="sd-query-data-types"></a>


| Data Type | Description | 
| --- | --- | 
| STRING | A string of maximum length 1024 bytes | 
| INTEGER | A signed 32-bit integer | 
| BIGINT | A signed 64-bit integer | 
| DOUBLE | IEEE 754 double precision floating point | 
| BOOLEAN | true or false | 
| TIMESTAMP | ISO-8601 compliant timestamps | 
| VARIANT | Semi-structured data (JSON objects, arrays). Use variant functions or dot notation to extract values | 
| MAP | Key-value pairs | 

Timestamp formats:

```
TIMESTAMP '2025-12-21 23:59:58.123'
TIMESTAMP '2025-12-21 23:59:58'
TIMESTAMP '2025-12-21'
```

## Supported SQL clauses
<a name="sd-query-sql-clauses"></a>

```
SELECT expression [, ...]
  [ FROM table_name [AS alias] [, ...] ]
  [ WHERE condition ]
  [ GROUP BY expression [, ...] ]
  [ HAVING condition ]
  [ ORDER BY expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST ] [, ...] ]
  [ LIMIT count ]
```


| Clause | Description | 
| --- | --- | 
| SELECT | Columns or expressions to return | 
| FROM | Tables to query. Supports comma-separated tables and explicit JOIN | 
| WHERE | Filter conditions | 
| GROUP BY | Group rows for aggregation | 
| HAVING | Filter groups after aggregation | 
| ORDER BY | Sort results. Use ASC or DESC, with optional NULLS FIRST / NULLS LAST | 
| LIMIT | Limit result count (0 to 2,147,483,647) | 
| JOIN / INNER JOIN | Combine rows from multiple tables | 
| UNION / UNION ALL | Combine results from multiple queries | 
| SUB SELECT | Nested SELECT within WHERE or FROM | 

## Variant functions and dot notation
<a name="sd-query-variant-functions"></a>

Scenario Discovery supports two approaches for working with VARIANT columns (semi-structured JSON data).

### Dot notation (recommended for simple access)
<a name="sd-query-dot-notation"></a>

Use dot notation to access nested fields directly on VARIANT columns:

```
-- Access nested struct fields
SELECT t.struct_value.observation.state.max_speed
FROM raw_time_series t
LIMIT 10

-- Filter on nested values
SELECT DISTINCT t.dataset_id, t.series_id, t.event_timestamp
FROM raw_time_series t
WHERE CAST(t.struct_value.observation.state.max_speed AS INT) > 0

-- Access annotation context fields
SELECT a.contexts.road_type, a.contexts.weather
FROM annotations a
LIMIT 10
```

### variant\_extract
<a name="sd-query-variant-extract"></a>

Extracts a value from a variant object by key name. Returns a VARIANT that you can further access or cast.

Signature: `variant_extract(variant_expr, key)`

```
SELECT
    variant_extract(obj, 'object_type'),
    variant_extract(obj, 'object_name'),
    variant_extract_nested(obj, 'attributes.confidence')
FROM annotations a,
UNNEST(CAST(a.objects AS VARIANT ARRAY)) AS t(obj)
WHERE a.dataset_id = 'my-dataset-id'
LIMIT 50
```

### variant\_extract\_nested
<a name="sd-query-variant-extract-nested"></a>

Extracts a nested value using a dot-separated path string. The second parameter must be a string literal.

Signature: `variant_extract_nested(variant_expr, 'dotted.path.key')`

```
SELECT
    variant_extract(obj, 'object_type'),
    variant_extract_nested(obj, 'attributes.confidence')
FROM annotations a,
UNNEST(CAST(a.objects AS VARIANT ARRAY)) AS t(obj)
WHERE a.dataset_id = 'my-dataset-id'
    AND CAST(variant_extract_nested(obj, 'attributes.confidence') AS DOUBLE) >= 0.7
LIMIT 50
```

### to\_json
<a name="sd-query-to-json"></a>

Converts a variant value to a JSON string.

Signature: `to_json(variant_expr)`

```
SELECT to_json(a.objects) FROM annotations a LIMIT 5
```

### UNNEST for arrays
<a name="sd-query-unnest"></a>

Use UNNEST to expand VARIANT arrays into rows:

```
SELECT
    a.dataset_id,
    a.series_id,
    a.frame_id,
    a.event_timestamp,
    variant_extract(obj, 'object_type'),
    variant_extract(obj, 'object_name'),
    variant_extract_nested(obj, 'attributes.confidence')
FROM annotations a,
UNNEST(CAST(a.objects AS VARIANT ARRAY)) AS t(obj)
WHERE a.dataset_id = 'my-dataset-id'
    AND CAST(variant_extract_nested(obj, 'attributes.confidence') AS DOUBLE) >= 0.7
ORDER BY a.dataset_id
LIMIT 50
```

## Operators and functions
<a name="sd-query-operators-functions"></a>

### Logical operators
<a name="sd-query-logical-operators"></a>


| Operator | Description | 
| --- | --- | 
| AND | Both conditions must be true | 
| OR | Either condition must be true | 
| NOT | Negates a condition | 

### Comparison operators
<a name="sd-query-comparison-operators"></a>


| Operator | Description | 
| --- | --- | 
| = | Equal to | 
| <> or \!= | Not equal to | 
| < | Less than | 
| > | Greater than | 
| <= | Less than or equal to | 
| >= | Greater than or equal to | 
| BETWEEN | Within a range (inclusive) | 
| IN | Matches any value in a list | 
| LIKE | Pattern matching with % and \_ wildcards | 
| IS NULL / IS NOT NULL | Null checks | 

### Aggregate functions
<a name="sd-query-aggregate-functions"></a>


| Function | Description | 
| --- | --- | 
| COUNT(\*) / COUNT(expr) | Count rows | 
| SUM(expr) | Sum of values | 
| AVG(expr) | Average of values | 
| MIN(expr) | Minimum value | 
| MAX(expr) | Maximum value | 

### Type conversion
<a name="sd-query-type-conversion"></a>


| Function | Description | 
| --- | --- | 
| CAST(expr AS type) | Convert a value to the specified type | 

## Example queries
<a name="sd-query-examples"></a>

### Basic telemetry queries
<a name="sd-query-examples-telemetry"></a>

List all telemetry data (limited):

```
SELECT * FROM raw_time_series LIMIT 10
```

Filter by time range:

```
SELECT alias, event_timestamp, double_value
FROM raw_time_series
WHERE event_timestamp > TIMESTAMP '2025-01-01 00:00:00'
  AND event_timestamp < TIMESTAMP '2025-01-02 00:00:00'
LIMIT 100
```

Aggregate telemetry values:

```
SELECT
    alias,
    COUNT(*) AS data_points,
    AVG(double_value) AS avg_value,
    MAX(double_value) AS max_value,
    MIN(double_value) AS min_value
FROM raw_time_series
GROUP BY alias
ORDER BY data_points DESC
```

Query struct telemetry using dot notation:

```
SELECT DISTINCT t.dataset_id, t.series_id, t.event_timestamp
FROM raw_time_series t
WHERE CAST(t.struct_value.observation.state.max_speed AS INT) > 0
```

### Annotation queries
<a name="sd-query-examples-annotations"></a>

List annotations for a dataset:

```
SELECT dataset_id, series_id, frame_id, event_timestamp
FROM annotations
WHERE dataset_id = 'my-dataset-id'
ORDER BY event_timestamp
LIMIT 100
```

Extract detected objects with confidence filtering:

```
SELECT
    a.dataset_id,
    a.series_id,
    a.frame_id,
    a.event_timestamp,
    variant_extract(obj, 'object_type'),
    variant_extract(obj, 'object_name'),
    variant_extract_nested(obj, 'attributes.confidence')
FROM annotations a,
UNNEST(CAST(a.objects AS VARIANT ARRAY)) AS t(obj)
WHERE a.dataset_id = 'my-dataset-id'
    AND CAST(variant_extract_nested(obj, 'attributes.confidence') AS DOUBLE) >= 0.7
ORDER BY a.event_timestamp
LIMIT 50
```

Query annotation contexts using dot notation:

```
SELECT
    a.dataset_id,
    a.frame_id,
    a.contexts.road_type,
    a.contexts.weather,
    a.contexts.time_of_day
FROM annotations a
WHERE a.dataset_id = 'my-dataset-id'
LIMIT 100
```

### Dataset and data segment queries
<a name="sd-query-examples-datasets"></a>

List all datasets:

```
SELECT dataset_id, name, dataset_type, version, created_at
FROM dataset
ORDER BY created_at DESC
```

List data segments for a dataset:

```
SELECT source_dataset_id, dataset_id, timeseries_id, alias, data_type, start_time, end_time
FROM datasegment
WHERE dataset_id = 'my-dataset-id'
```

Count data segments by type:

```
SELECT data_type, COUNT(*) AS segment_count
FROM datasegment
GROUP BY data_type
```

### Cross-table queries
<a name="sd-query-examples-cross-table"></a>

Find telemetry data for a specific dataset's segments:

```
SELECT t.alias, t.event_timestamp, t.double_value
FROM raw_time_series t, datasegment ds
WHERE t.dataset_id = ds.dataset_id
  AND t.series_id = ds.timeseries_id
  AND ds.data_type = 'JSON'
LIMIT 100
```

## Troubleshooting
<a name="sd-query-troubleshooting"></a>

### ValidationException on StartQuery
<a name="sd-query-ts-validation"></a>
+ Verify your `queryStatement` is valid SQL and under 10,240 characters.
+ Verify `workspaceName` matches pattern `^[a-zA-Z0-9_-]+$`.
+ Check that table and column names are valid (see reference tables).

### Query stuck in RUNNING
<a name="sd-query-ts-stuck"></a>
+ Use `CancelQuery` if the query is taking too long.
+ Queries timeout automatically after 15 minutes.

### ResourceNotFoundException on GetQueryResults
<a name="sd-query-ts-not-found"></a>
+ Verify the `queryId` exists and belongs to the specified workspace.
+ Query IDs are scoped to the account and workspace.

### Query returns FAILED
<a name="sd-query-ts-failed"></a>
+ Use `DescribeQuery` to check the `completedAt` timestamp and error details.
+ Common causes: invalid SQL syntax, referencing non-existent columns, type mismatches in CAST expressions.

### Empty results
<a name="sd-query-ts-empty"></a>
+ Verify data has been ingested into the workspace (use `list-time-series` to check).
+ Verify the query is marked as `COMPLETED` through `DescribeQuery`.
+ Check that your WHERE clause time range matches the ingested data's timestamps.
+ Ensure you are querying the correct workspace.

### Slow pagination
<a name="sd-query-ts-slow"></a>
+ Set `maxResults` to 10,000 in `GetQueryResults` for optimal performance.
+ Use `nextToken` to paginate through large result sets.