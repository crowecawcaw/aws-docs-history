

# SQL query reference
<a name="omni-sql-query-reference"></a>

CloudWatch Omni supports SQL for querying logs and traces. This page covers CloudWatch Omni SQL: the supported syntax and the behaviors that differ from other SQL dialects. To build SQL queries interactively, use Explore. See [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md).

SQL is the same language wherever you write a query in Omni: in Explore, in an alert condition, and through the public API.

**Tables to query**

A query addresses a signal through its table in your space's CloudWatch Dataset. The Dataset is named `default`:


| FROM table | Reads | 
| --- | --- | 
| logs.default | Log records only. | 
| traces.default | Traces only — both application spans and AI agent spans. | 
| default | Logs and traces in one query. Use this when you do not know which signal holds the field you want. | 

Prefer a concrete signal type whenever possible. Such queries are faster because they do not scan other signals' data.

**System fields**

Every row carries system fields alongside the fields your telemetry brought with it: `@timestamp`, `@ingest_time`, and `@telemetry_type` on every signal, and `@message` on log records. The `@entity`, `@data_source_name`, `@data_source_type`, `@data_format`, `@aws.region`, `@aws.account`, `@logGroupId`, `@logGroupName`, `@logStream`, and `@logStreamId` system fields are also supported.

Quote any field name that is not a plain identifier: one with a leading `@`, a dot, or a hyphen. Backticks and double quotes both work:

```
SELECT `@timestamp`, `@message`
FROM "logs.default"
WHERE `@timestamp` BETWEEN NOW() - INTERVAL '1' DAY AND NOW()
LIMIT 500
```

Quoting decides whether Omni reads a token as a column or as text:
+ Backticks and double quotes mark an **identifier**. `` `status` `` and `"status"` both name the column `status`.
+ Single quotes mark a **string literal**. `'ERROR'` is the text `ERROR`.
+ Brackets look up a key inside an attribute map, and the key is always a string literal, so it takes single quotes: `attributes['http.status_code']`.

Because double quotes are an identifier, `WHERE status = "ERROR"` compares the `status` column against a column named `ERROR`, not against the text `ERROR`. Write `WHERE status = 'ERROR'` instead.

Field names are case sensitive: `traceId` and `traceid` are not interchangeable.

**What a wildcard SELECT returns**

Because the Dataset contains records from different sources, each can have a different set of fields. That is why `SELECT *` does not project all fields as columns. It returns two columns representing a full record: `@timestamp` and `@record` — a JSON document holding the fields your telemetry brought with it. System fields are not part of `@record`; select them by name.

```
@timestamp                  | @record
2026-08-26T18:04:11.230Z    | {"request_id":"abc-123","path":"/api/auth/login","status_code":500, ...}
```

Name the fields you want as columns:

```
SELECT 
  request_id, 
  path, 
  status_code
FROM "logs.default"
WHERE `@timestamp` >= NOW() - INTERVAL '15' MINUTE
```

You can filter on a field whether or not you select it, so `WHERE path = '/api/auth/login'` works under `SELECT *`. Only the projection changes, not what you can reference.

`@record` is an output column only. It cannot feed a function, a comparison, `WHERE`, `GROUP BY`, `ORDER BY`, or a join condition. Name the field you want instead.

`@message` is a system field that holds the raw record. It is useful for unstructured records, where Omni cannot extract any columns and `@record` is empty (`{}`).

**Nested attributes**

Read into an attribute map with bracket syntax:

```
SELECT 
  attributes['http.status_code'], 
  resource['attributes']['service.name']
FROM "traces.default"
WHERE `@timestamp` >= NOW() - INTERVAL '1' HOUR
```

Bracket syntax accepts only string literals as the key, so use single quotes for subscript access. Dots within the string literal are allowed when they are part of the key name, for example `'service.name'`.

**Column types**

No schema is required for a Dataset in Omni. Omni SQL identifies the correct type from the query itself and applies it automatically. For example, when a `WHERE` filter compares against a numeric value such as `WHERE latency > 100`, values are cast to the appropriate type.

A Dataset may contain records from different sources with different fields. The same field name may appear with different types. For example, `status` may hold enumeration values in some records (`OK`, `ERROR`) and numeric values in others (0, 1). In such cases, Omni selects the most appropriate type to execute the query correctly.

In ambiguous cases, use the `CAST` operator.

**Time filtering**

The time range you select in Explore automatically applies to your query. You can also bound time in the query text with a `@timestamp` condition, using `BETWEEN` or comparison operators, and `NOW()` with `INTERVAL` arithmetic. A `@timestamp` condition in the query takes precedence over the range selected in Explore. Other timestamp functions are also supported.

**In a join, bound each table separately.** A condition on one side does not constrain the other, so a join with a single bound reads the whole retention window on the unbounded side:

```
SELECT a.request_id, a.path, b.user_id
FROM "logs.default" a
JOIN "logs.default" b ON a.request_id = b.request_id
WHERE a.`@timestamp` >= NOW() - INTERVAL '1' HOUR
  AND a.`@timestamp` <= NOW()
  AND b.`@timestamp` >= NOW() - INTERVAL '1' HOUR
  AND b.`@timestamp` <= NOW()
```

**Discover fields**

Wrap any query in `EXPLAIN (ANALYZE_FIELDS)` to get one row per field observed in the rows that query selects, instead of the data rows:

```
EXPLAIN (ANALYZE_FIELDS) 
SELECT * 
FROM "logs.default"
WHERE `@timestamp` >= NOW() - INTERVAL '1' HOUR
LIMIT 500
```

Your conditions, time bounds, and `LIMIT` all apply, so you can ask which fields appear on one service's error logs in the last hour rather than which fields exist anywhere. [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md) covers how the Browse panel runs this for you.

`EXPLAIN (ANALYZE_FIELDS)` is not billed or metered: it samples a bounded slice of your data, so you can run it freely to explore a Dataset's fields.

**Supported and unsupported syntax**

CloudWatch Omni SQL supports the constructs this page demonstrates — `SELECT` with `WHERE`, `GROUP BY`, `ORDER BY`, and `LIMIT`, joins, and aggregate functions with `FILTER` — as well as window functions, `UNION` and `UNION ALL`, and `CAST`. `EXPLAIN (ANALYZE_FIELDS)` is the only supported form of `EXPLAIN`.

The engine rejects unsupported statements before they run, returning an unsupported-statement error rather than an empty result, so you can distinguish a rejected query from one that matched nothing.

**Examples**

**Slowest agent runs in the last hour.** Each span's duration is the difference between its `startTimeUnixNano` and `endTimeUnixNano`, and the agent's name comes from its resource attributes:

```
SELECT 
  resource['attributes']['service.name'] AS agent, 
  `@timestamp`, 
  (endTimeUnixNano - startTimeUnixNano) AS duration_ns
FROM traces.default
WHERE `@timestamp` >= NOW() - INTERVAL '1' HOUR
ORDER BY duration_ns DESC
LIMIT 20
```

**Error rate by service.** Counting over a grouped select:

```
SELECT resource['attributes']['service.name'] AS service,
       COUNT(*) AS spans,
       COUNT(*) FILTER (WHERE status['code'] IN ('2', 'ERROR')) AS errors
FROM traces.default
WHERE `@timestamp` >= NOW() - INTERVAL '1' HOUR
GROUP BY resource['attributes']['service.name']
ORDER BY errors DESC
```

**One request across an application and an agent.** Both carry the same trace ID when context propagates:

```
SELECT * 
FROM "traces.default"
WHERE 
  `@timestamp` >= NOW() - INTERVAL '1' HOUR 
  AND traceId = '<trace-id>'
```

**Next steps**
+ To build a query interactively, see [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md).
+ To alert on a query result, see [Alerts](omni-alerts.md).
+ To put a query on a dashboard, see [Dashboards](omni-dashboards.md).