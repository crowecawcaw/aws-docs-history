For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Querying data from Timestream for InfluxDB 3

Amazon Timestream for InfluxDB 3 provides multiple query APIs and protocols to retrieve your time
series data. The platform supports both SQL and InfluxQL query languages through HTTP and Flight
(gRPC) protocols, offering flexibility for different use cases and client preferences.

## Query methods overview

InfluxDB 3 supports the following query methods:

- Native v3 HTTP API – SQL and InfluxQL queries via REST endpoints.
- influxdb3 CLI – Command-line interface for interactive queries.
- Flight+gRPC Protocol – High-performance binary protocol for client libraries.
- v1 Compatibility API – Legacy InfluxQL queries for backward compatibility.

### Using the v3 HTTP query API

The v3 API provides dedicated endpoints for SQL and InfluxQL queries with support for both
GET and POST methods.

#### SQL queries

(`/api/v3/query_sql`)

GET request example:

```
curl --get "https://your-cluster-endpoint:8086/api/v3/query_sql" \
  --header "Authorization: Bearer YOUR_TOKEN" \
  --data-urlencode "db=DATABASE_NAME" \
  --data-urlencode "q=SELECT * FROM home WHERE time >= now() - INTERVAL '1 day'"

```

POST request example (for complex queries):

```
curl "https://your-cluster-endpoint:8086/api/v3/query_sql" \
  --header "Authorization: Bearer YOUR_TOKEN" \
  --json '{
    "db": "DATABASE_NAME",
    "q": "SELECT * FROM home WHERE room = '\''Kitchen'\'' AND temp > 20",
    "format": "jsonl"
  }'

```

#### InfluxQL queries

(`/api/v3/query_influxql`)

For InfluxQL queries do the following:

```
curl --get "https://your-cluster-endpoint:8086/api/v3/query_influxql" \
  --header "Authorization: Bearer YOUR_TOKEN" \
  --data-urlencode "db=DATABASE_NAME" \
  --data-urlencode "q=SELECT mean(temp) FROM home WHERE time >= now() - 1d GROUP BY room"

```

#### Query parameters

You can use the following query parameters:

| **Parameter** | **Description**                                     | **Required**       |
| ------------- | --------------------------------------------------- | ------------------ |
| `db`          | Database name                                       | Yes                |
| `q`           | Query string (SQL or InfluxQL)                      | Yes                |
| `format`      | Response format (json, jsonl, csv, pretty, parquet) | No (default: json) |
| `params`      | Parameters for parameterized queries                | No                 |

#### Using the Influxdb3 CLI

InfluxDB 3 command-line interface (CLI) is invoked with the `influxdb3`
command. It provides an interactive way to query your data with support for multiple output
formats.

The following shows a basic query:

```
influxdb3 query \
  --host "your-cluster-endpoint:8086" \
  --token "YOUR_TOKEN" \
  --database "DATABASE_NAME" \
  "SELECT * FROM home WHERE time >= now() - INTERVAL '1 day'"

```

The following shows a query with different output formats:

```
# JSON output
influxdb3 query \
  --database "DATABASE_NAME" \
  --format json \
  "SELECT * FROM home LIMIT 10"

# CSV output
influxdb3 query \
  --database "DATABASE_NAME" \
  --format csv \
  "SELECT * FROM home LIMIT 10"

# Parquet file output
influxdb3 query \
  --database "DATABASE_NAME" \
  --format parquet \
  --output results.parquet \
  "SELECT * FROM home"

```

The following output formats are supported:

- pretty (default) – Human-readable tabular format.
- json – Standard JSON array.
- jsonl – JSON Lines (streaming-friendly).
- csv – Comma-separated values.
- parquet – Binary columnar format (requires file output).

### Using the v1 compatibility API

For legacy InfluxQL queries, use the `/query` endpoint:

```
curl --get "https://your-cluster-endpoint:8086/query" \
  --header "Authorization: Bearer YOUR_TOKEN" \
  --data-urlencode "db=DATABASE_NAME" \
  --data-urlencode "q=SELECT * FROM home" \
  --data-urlencode "epoch=ms"

```

## Authentication options for the v3 HTTP Query API

- Bearer token: `Authorization: Bearer TOKEN`
- Basic auth: `--user "any:TOKEN"`
- Query parameter: `?p=TOKEN`

## Response formats for the v3 HTTP Query API

- JSON (default)
- CSV (with `Accept: application/csv` header)

## SQL Query Examples

The following shows a basic query:

```
-- Select specific fields with time filter
SELECT temp, humidity, room
FROM home
WHERE time >= now() - INTERVAL '7 days'
  AND room = 'Kitchen'
ORDER BY time DESC

-- Show all tables in database
SHOW TABLES

-- Show columns in a table
SHOW COLUMNS FROM home

```

The following shows aggregation queries:

```
-- Aggregate by tags
SELECT
  room,
  AVG(temp) as avg_temp,
  MAX(humidity) as max_humidity
FROM home
WHERE time >= now() - INTERVAL '24 hours'
GROUP BY room

-- Time-based aggregation using DATE_BIN
SELECT
  DATE_BIN(INTERVAL '1 hour', time) as time,
  AVG(temp) as avg_temp,
  COUNT(*) as reading_count
FROM home
GROUP BY 1
ORDER BY time DESC

```

The following shows advanced SQL features:

```
-- Parameterized queries (via API)
SELECT * FROM home
WHERE room = $room
  AND temp > $min_temp
  AND time >= $start_time

-- Gap filling with interpolation
SELECT
  date_bin_gapfill(INTERVAL '5 minutes', time) as time,
  room,
  interpolate(avg(temp)) as temp
FROM home
WHERE time >= '2025-01-01T00:00:00Z'
  AND time <= '2025-01-01T12:00:00Z'
GROUP BY 1, room

-- Type casting
SELECT
  temp::INTEGER as temp_int,
  CAST(humidity AS VARCHAR) as humidity_str
FROM home

```

The following shows InfluxQL query examples:

```
-- Basic query with time filter
SELECT * FROM home WHERE time >= now() - 1d

-- Aggregation with GROUP BY time
SELECT MEAN(temp), MAX(humidity)
FROM home
WHERE time >= now() - 7d
GROUP BY time(1h), room

-- Using selector functions
SELECT FIRST(temp), LAST(temp)
FROM home
WHERE time >= now() - 1h
GROUP BY room

```

The following shows how to query system tables to understand your database structure and
monitor performance:

```
-- View all tables with schema information
SELECT * FROM information_schema.tables

-- View column details for a specific table
SELECT * FROM information_schema.columns
WHERE table_name = 'home'

-- Monitor recent queries
SELECT * FROM system.queries
ORDER BY issue_time DESC
LIMIT 10

-- Check cache configurations
SELECT * FROM system.last_caches
SELECT * FROM system.distinct_caches

```

## Query performance best practices

- **Use Time Filters**: Always include time range filters to limit
  data scanned.
- **Leverage Indexes**: Design queries to use tag filters
  effectively.
- **Choose Appropriate Output Format**:
  - Use jsonl for streaming large results.
  - Use parquet for data export and analytics.
  - Use csv for spreadsheet compatibility.

- **Optimize Aggregations**: Use DATE_BIN for time-based grouping.
- **Use Parameterized Queries**: Prevent injection attacks and
  improve reusability.
- **Monitor Query Performance**: Check the system.queries table for
  slow queries.

## Client library query support

InfluxDB 3 client libraries use the Flight+gRPC protocol for optimal performance. The
following Python code shows an example of this.

```
from influxdb3 import InfluxDBClient3

client = InfluxDBClient3(
    host="your-cluster-endpoint:8086",
    token="YOUR_TOKEN",
    database="DATABASE_NAME"
)

# SQL query
sql_result = client.query("SELECT * FROM home WHERE room = 'Kitchen'")

# InfluxQL query
influxql_result = client.query(
    "SELECT MEAN(temp) FROM home WHERE time >= now() - 1h GROUP BY room",
    language="influxql"
)

```

## Compare SQL and InfluxQL query capabilities

The following table compares SQL and InfluxQL query capabilities:

| **Feature**               | **SQL**                | **InfluxQL**      |
| ------------------------- | ---------------------- | ----------------- |
| **Joins**                 | Supported              | Not supported     |
| **Window Functions**      | Full support           | Limited           |
| **Subqueries**            | Supported              | Not supported     |
| **Time Functions**        | `DATE_BIN`, `INTERVAL` | `time()` grouping |
| **Parameterized Queries** | Native support         | Not supported     |
| **Gap Filling**           | `date_bin_gapfill()`   | `fill()` function |

By understanding these query capabilities and choosing the appropriate method for your use
case, you can efficiently retrieve and analyze your time-series data from Timestream for InfluxDB 3.

SQL advantages:

- Full-featured SQL implementation with support for complex queries.
- Support for joins, unions, and window functions.
- Familiar syntax for users with SQL background.
- More extensive analytical capabilities.

InfluxQL advantages:

- Designed specifically for time-series data.
- Simpler syntax for common time-series operations.
- Backward compatibility for users migrating from InfluxDB v1.
- Specialized time-series functions.

## Query optimization features

InfluxDB 3 offers several optimization features to improve query performance for specific
use cases. These features leverage in-memory caching and custom indexing strategies to deliver
sub-millisecond response times for frequently accessed data patterns.

### Last Value Cache (LVC)

The Last Value Cache (LVC) stores the most recent N values for specified fields in memory,
enabling sub-10ms response times for queries that need the latest data points. This feature is
available in both Core and Enterprise editions.

#### How LVC works

The LVC maintains an in-memory table of the most recent values for each unique
combination of key columns (typically tags). For example, with sensor data:

```
Table: home
├── Tags: room, wall
└── Fields: temp, humidity, co

LVC Configuration:
- Key columns: room, wall
- Value columns: temp, humidity, co
- Count: 4 (last 4 values)

```

The cache stores:

| **room**    | **wall** | **temp** | **humidity** | **co** | **time**             |
| ----------- | -------- | -------- | ------------ | ------ | -------------------- |
| Kitchen     | east     | 22.7     | 36.5         | 26     | 2025-01-26T20:00:00Z |
| Kitchen     | east     | 22.7     | 36.0         | 9      | 2025-01-26T17:00:00Z |
| Kitchen     | east     | 22.7     | 36.2         | 3      | 2025-01-26T15:00:00Z |
| Kitchen     | east     | 22.7     | 36.1         | 0      | 2025-01-26T10:00:00Z |
| Living Room | north    | 22.2     | 36.4         | 17     | 2025-01-26T20:00:00Z |
| ...         | ...      | ...      | ...          | ...    | ...                  |

#### Create an LVC

Use the following command to create an LVC:

```
influxdb3 create last_cache \
  --database DATABASE_NAME \
  --token YOUR_TOKEN \
  --table home \
  --key-columns room,wall \
  --value-columns temp,hum,co \
  --count 5 \
  --ttl 30mins \
  homeLastCache

```

#### Query the LVC

Use the following command to query an LVC:

```
-- Query the last cached values
SELECT * FROM last_cache('home', 'homeLastCache')

-- Filter specific series
SELECT * FROM last_cache('home', 'homeLastCache')
WHERE room = 'Kitchen'

```

#### LVC best practices

- Manage Cardinality: Only include essential tags as key columns to minimize memory
  usage.
- Optimize Value Count: Balance between query needs and memory consumption.
- Consider TTL: Set appropriate time-to-live for cache entries.
- Monitor Memory: Cache size = (key_column_cardinality × count × value_columns).

### Distinct Value Cache (DVC)

The Distinct Value Cache (DVC) maintains unique values for specified columns in memory,
accelerating metadata queries to under 30ms response times. Available in both Core and
Enterprise editions.

#### How DVC works

The DVC stores all unique combinations of values for specified columns, perfect for
queries that need to list available tag values or metadata.

Example cache for location data:

| **country**    | **county**    | **city** |
| -------------- | ------------- | -------- |
| Austria        | Salzburg      | Salzburg |
| Austria        | Vienna        | Vienna   |
| Belgium        | Antwerp       | Antwerp  |
| Belgium        | West Flanders | Bruges   |
| Czech Republic | Prague        | Prague   |

#### Create a DVC

Use the following command to create a DVC:

```
influxdb3 create distinct_cache \
  --database DATABASE_NAME \
  --token YOUR_TOKEN \
  --table wind_data \
  --columns country,county,city \
  --max-cardinality 10000 \
  --max-age 24h \
  windDistinctCache

```

#### Query the DVC

Use the following command to query a DVC:

```
-- Get all distinct values
SELECT * FROM distinct_cache('wind_data', 'windDistinctCache')

-- Get distinct countries
SELECT DISTINCT country
FROM distinct_cache('wind_data', 'windDistinctCache')

```

#### DVC best practices

- Set Cardinality Limits: Define maximum unique value combinations to control memory.
- Configure Max Age: Remove stale values automatically.
- Cache Strategic Columns: Focus on columns frequently used in metadata queries.
- Monitor Cache Size: Higher cardinality means that more memory is required.

### File indexes available in Enterprise only

**Available in Enterprise Edition only.** File indexes allow
customization of how data is indexed in storage, significantly improving single-series query
performance.

#### Default vs. custom indexing

Default Indexing: InfluxDB indexes on all tags plus time. 

Custom Indexing: Index only on columns relevant to your queries.

Example optimization:

```
Schema columns: country, state_province, county, city, postal_code
Query patterns: Always filter by country, state_province, city
Custom index: time, country, state_province, city (skip county, postal_code)

```

The following shows how to create a custom file index

```
influxdb3 create file_index \
  --database DATABASE_NAME \
  --token YOUR_TOKEN \
  --table wind_data \
  country,state_province,city

```

The following shows how to delete a file index:

```
influxdb3 delete file_index \
  --database DATABASE_NAME \
  --token YOUR_TOKEN \
  --table wind_data

```

#### File index considerations

- Compaction Required: Indexes are built during data compaction (gen2+).
- String Columns Only: Can index both tags and string fields.
- Query Pattern Analysis: Analyze your workload before creating custom indexes.
- Single-Series Optimization: Most beneficial for queries targeting specific series.

### Managing cache information

View cache configurations and statistics using system tables:

```
-- View Last Value Caches
SELECT * FROM system.last_caches

-- View Distinct Value Caches
SELECT * FROM system.distinct_caches

-- Check cache memory usage
SELECT
  cache_name,
  table_name,
  key_columns,
  value_count,
  memory_size_bytes
FROM system.last_caches

```

### Performance optimization strategy

Choose the right optimization features based on your query patterns:

| **Query Pattern**        | **Recommended Feature**   | **Expected Performance** |
| ------------------------ | ------------------------- | ------------------------ |
| Latest values per series | Last Value Cache          | <10ms                    |
| Available tag values     | Distinct Value Cache      | <30ms                    |
| Single-series queries    | File Indexes (Enterprise) | Significant improvement  |
| Time-range aggregations  | Standard indexes          | Baseline performance     |

### Memory and resource considerations

**Cache memory formula:**

- LVC: memory = key_cardinality × value_count × value_columns × data_size
- DVC: memory = distinct_combinations × column_count × data_size

**Best practices:**

- Start with small caches and monitor memory usage
- Use TTL settings to limit cache growth
- Only cache frequently queried data
- Monitor cache hit rates through system tables
- For Enterprise: Combine caches with custom file indexes for optimal performance

By leveraging these optimization features appropriately, you can achieve significant
performance improvements for specific query patterns while managing resource consumption
effectively.
