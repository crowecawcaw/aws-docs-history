

# CloudWatch Omni SQL query syntax

This page describes how to compose a CloudWatch Omni SQL query and the clauses and commands you can use in it. For information about tables, system fields, quoting, column types, and time filtering, see [SQL query reference](omni-sql-query-reference.md). For information about query limits, see [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md).

## Example data
<a name="omni-sql-query-syntax-example-data"></a>

The examples on this page assume that your telemetry contains records like the following.

**Log example** (`logs.default`)

```json
{
  "request_id": "abc-123",
  "path": "/api/auth/login",
  "status_code": 500,
  "latency_ms": 182.4,
  "user_id": "u-1042",
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736"
}
```

**Trace example** (`traces.default`)

```json
{
  "traceId": "5b8efff798038103d269b633813fc60c",
  "spanId": "eee19b7ec3c1b174",
  "name": "invoke_agent weather_agent",
  "kind": "INTERNAL",
  "startTimeUnixNano": 1792519316000000000,
  "endTimeUnixNano": 1792519318450000000,
  "resource": { "attributes": { "service.name": "weather-agent" } },
  "attributes": { "gen_ai.operation.name": "invoke_agent", "gen_ai.agent.name": "weather_agent" }
}
```

## Composing a query
<a name="omni-sql-query-syntax-composing-a-query"></a>

A CloudWatch Omni query is a single SQL statement with an optional trailing semicolon. CloudWatch Omni rejects a request that contains more than one statement.

When you run a query with the `StartTelemetryQuery` API, bound `@timestamp` with both a start and an end. In Explore, the time range you select fills in a missing bound.

To add a comment, use `--` for the rest of a line or `/* ... */` for a block. The hash character (`#`) does not start a comment.

The following example uses both comment styles.

```sql
/* Most recent login requests */
SELECT `@timestamp`, request_id, status_code
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW() -- time bound
  AND path = '/api/auth/login'
ORDER BY `@timestamp` DESC
LIMIT 50
```

## Clauses and commands
<a name="omni-sql-query-syntax-clauses-and-commands"></a>

The following table describes each clause and command. Every clause and command on this page works on all three CloudWatch Omni tables: `logs.default`, `traces.default`, and `default`.


| Clause or command | Description | 
| --- | --- | 
| WITH | Defines a common table expression (CTE), a named subquery that the main query can read from. | 
| TABLESAMPLE | Follows a table name and scans a portion of the table's data, selected by percentage of the time range (PERCENT) or by data volume (MAX\_VOLUME). | 
| JOIN | Combines rows from two tables, or from one table with itself. Supports [INNER] JOIN, LEFT JOIN, RIGHT JOIN, and FULL [OUTER] JOIN on a matching condition, and CROSS JOIN, which pairs every row on one side with every row on the other. Bound @timestamp on each side. | 
| WHERE | Keeps only the rows that match a condition. Supports comparison operators, AND, OR, NOT, IN, BETWEEN, LIKE, ILIKE (case-insensitive LIKE), IS NULL, and the \~ regular expression match. | 
| IN (subquery) | Keeps rows whose value appears in the result of a subquery. | 
| EXISTS (subquery) | Keeps rows for which a subquery returns at least one row. Use NOT EXISTS to keep rows for which it returns none. | 
| Scalar subquery | Uses the single value that a subquery returns in an expression, such as latency\_ms > (SELECT avg(latency\_ms) FROM ...). | 
| GROUP BY | Groups rows that share values so you can aggregate them. Accepts expressions or column positions such as GROUP BY 1. | 
| Aggregate functions with FILTER | Computes one value over a group of rows. Add FILTER (WHERE ...) after any aggregate function to include only some rows. | 
| HAVING | Keeps only the groups that match a condition on an aggregate. | 
| Window functions | Computes a value for each row from a set of related rows, called a window. Define the window with OVER (PARTITION BY ... ORDER BY ...) and, optionally, a frame, which limits the window to a range of rows around the current row. | 
| QUALIFY | Keeps only the rows that match a condition on a window function. | 
| ORDER BY | Sorts results with ASC or DESC. Use NULLS FIRST or NULLS LAST to choose where null values go. | 
| LIMIT and OFFSET | Caps the number of rows returned and, with OFFSET, skips rows first. | 
| UNION, UNION ALL, INTERSECT, EXCEPT | Combines the results of two queries. UNION ALL keeps duplicate rows. The others remove them. | 
| CASE | Returns the value for the first condition that is true. | 
| CAST, TRY\_CAST, :: | Converts a value to another type. TRY\_CAST returns null instead of failing the query when a value cannot be converted. | 
| EXPLAIN (ANALYZE\_FIELDS) | Returns a description of each field in the rows the query selects, with its types and sample values, instead of the rows themselves. Not billed. | 
| EXPLAIN (ESTIMATE [QUICK\|ACCURATE]) | Returns an estimate of the bytes the query would scan, in an estimated\_bytes column, instead of running the query. QUICK, the default, returns an estimate sooner. ACCURATE checks more detailed statistics and returns an estimate closer to the actual bytes scanned, but takes longer. Not billed. | 
| Other operators and functions | CloudWatch Omni also supports string, regular expression, math, conditional, date and time, aggregate, window, array and struct, JSON, IP address, and hash and encoding functions. See [Operators and functions](omni-sql-operators-and-functions.md) and [Hash and encoding functions](omni-sql-hash-and-encoding-functions.md). | 

**Example – Count failing traces with WITH**

```sql
WITH errors AS (
  SELECT traceId
  FROM "logs.default"
  WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
    AND status_code >= 500
)
SELECT COUNT(DISTINCT traceId) AS failing_traces
FROM errors
```

**Example – Sample the most recent 5 GB of the last 30 days with TABLESAMPLE**

```sql
SELECT `@timestamp`, request_id, status_code
FROM "logs.default" TABLESAMPLE (5G MAX_VOLUME, BIAS LATEST)
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '30' DAY AND NOW()
  AND status_code >= 500
LIMIT 1000
```

**Example – Count errors and distinct users per path with FILTER and HAVING**

```sql
SELECT path,
       COUNT(*) AS requests,
       COUNT(*) FILTER (WHERE status_code >= 500) AS errors,
       COUNT(DISTINCT user_id) AS users
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
GROUP BY path
HAVING COUNT(*) > 100
ORDER BY errors DESC
```

**Example – Compare log and trace record counts with UNION ALL**

```sql
SELECT 'logs' AS signal, COUNT(*) AS records
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
UNION ALL
SELECT 'traces' AS signal, COUNT(*) AS records
FROM "traces.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
```

**Example – Find paths seen in the last hour but not in the 23 hours before it with EXCEPT**

```sql
SELECT path
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
EXCEPT
SELECT path
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' DAY AND NOW() - INTERVAL '1' HOUR
```

**Example – Discover the fields on agent spans**

```sql
EXPLAIN (ANALYZE_FIELDS)
SELECT *
FROM "traces.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' HOUR AND NOW()
  AND name LIKE 'invoke_agent%'
```

The result has one row for `@timestamp` and one for `@record`. The `@record` row's description lists the fields inside `@record`.