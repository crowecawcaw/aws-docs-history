# stats

Use `stats` to create visualizations of your log data such as
bar charts, line charts, and stacked area charts. This helps you more
efficiently identify patterns in your log data. CloudWatch Logs Insights generates
visualizations for queries that use the `stats` function and one
or more aggregation functions.

For example, the following query in a Route 53 log group returns
visualizations showing the distribution of Route 53 records per hour, by query
type.

```
stats count(*) by queryType, bin(1h)
```

All such queries can produce bar charts. If your query uses the
`bin()` function to group the data by one field over time,
you can also see line charts and stacked area charts.

The following time units and abbreviations are supported with the
`bin` function. For all units and abbreviations that include
more than one character, adding s to pluralize is supported. So both
`hr` and `hrs` work to specify hours.

- `millisecond`
  `ms`
  `msec`
- `second`
  `s`
  `sec`
- `minute`
  `m`
  `min`
- `hour`
  `h`
  `hr`
- `day`
  `d`
- `week`
  `w`
- `month`
  `mo`
  `mon`
- `quarter`
  `q`
  `qtr`
- `year`
  `y`
  `yr`

###### Topics

- [Visualize time
  series data](#CWL_Insights-Visualizing-TimeSeries "#CWL_Insights-Visualizing-TimeSeries")
- [Visualize log data
  grouped by fields](#CWL_Insights-Visualizing-ByFields "#CWL_Insights-Visualizing-ByFields")
- [Use multiple stats
  commands in a single query](#CWL_QuerySyntax-stats-multi "#CWL_QuerySyntax-stats-multi")
- [Functions to use with
  stats](#CWL_QuerySyntax-stats-functions "#CWL_QuerySyntax-stats-functions")

## Visualize time

series data

Time series visualizations work for queries with the following
characteristics:

- The query contains one or more aggregation functions. For more
  information, see [Aggregation Functions in the Stats Command](#CWL_Insights_Aggregation_Functions "#CWL_Insights_Aggregation_Functions").
- The query uses the `bin()` function to group the
  data by one field.

These queries can produce line charts, stacked area charts, bar
charts, and pie charts.

**Examples**

For a complete tutorial, see [Tutorial: Run a
query that produces a time series visualization](CWL_AnalyzeLogData_VisualizationQuery.md "CWL_AnalyzeLogData_VisualizationQuery.md").

Here are more example queries that work for time series
visualization.

The following query generates a visualization of the average values of
the `myfield1` field, with a data point created every five
minutes. Each data point is the aggregation of the averages of the
`myfield1` values from the logs from the previous five
minutes.

```
stats avg(myfield1) by bin(5m)
```

The following query generates a visualization of three values based on
different fields, with a data point created every five minutes. The
visualization is generated because the query contains aggregate
functions and uses `bin()` as the grouping field.

```
stats avg(myfield1), min(myfield2), max(myfield3) by bin(5m)
```

**Line chart and stacked area chart
restrictions**

Queries that aggregate log entry information but don't use the
`bin()` function can generate bar charts. However, the
queries cannot generate line charts or stacked area charts. For more
information about these types of queries, see [Visualize log data
grouped by fields](#CWL_Insights-Visualizing-ByFields "#CWL_Insights-Visualizing-ByFields").

## Visualize log data

grouped by fields

You can produce bar charts for queries that use the `stats`
function and one or more aggregation functions. For more information,
see [Aggregation Functions in the Stats Command](#CWL_Insights_Aggregation_Functions "#CWL_Insights_Aggregation_Functions").

To see the visualization, run your query. Then choose the
**Visualization** tab, select the arrow next to
**Line**, and choose **Bar**.
Visualizations are limited to up to 100 bars in the bar chart.

**Examples**

For a complete tutorial, see [Tutorial: Run a
query that produces a visualization grouped by log fields](CWL_AnalyzeLogData_VisualizationFieldQuery.md "CWL_AnalyzeLogData_VisualizationFieldQuery.md"). The
following paragraphs include more example queries for visualization by
fields.

The following VPC flow log query finds the average number of bytes
transferred per session for each destination address.

```
stats avg(bytes) by dstAddr
```

You can also produce a chart that includes more than one bar for each
resulting value. For example, the following VPC flow log query finds the
average and maximum number of bytes transferred per session for each
destination address.

```
stats avg(bytes), max(bytes) by dstAddr
```

The following query finds the number of Amazon Route 53 query logs for each
query type.

```
stats count(*) by queryType
```

## Use multiple stats

commands in a single query

You can use as many as two `stats` commands in a single
query. This enables you to perform an additional aggregation on the
output of the first aggregation.

**Example: Query with two `stats`
commands**

For example, the following query first find the total traffic volume
in 5-minute bins, then calculates the highest, lowest, and average
traffic volume among those 5-minute bins.

````
FIELDS strlen(@message) AS message_length
| STATS sum(message_length)/1024/1024 as logs_mb BY bin(5m)
| STATS max(logs_mb) AS peak_ingest_mb, min(logs_mb) AS min_ingest_mb, avg(logs_mb) AS avg_ingest_mb ``` **Example: Combine multiple stats commands with other functions such as `filter`, `fields`, `bin`** You can combine two `stats` commands with other commands such as `filter` and `fields` in a single query. For example, the following query finds the number of distinct IP addresses in sessions and finds the number of sessions by client platform, filters those IP addresses, and then finally finds the average of session requests per client platform. ``` STATS count_distinct(client_ip) AS session_ips, count(*) AS requests BY session_id, client_platform
| FILTER session_ips > 1
| STATS count(*) AS multiple_ip_sessions, sum(requests) / count(*) AS avg_session_requests BY client_platform ``` You can use `bin` and `dateceil` functions in queries with multiple `stats` commands. For example, the following query first combines messages into 5-minute blocks, then aggregates those 5-minute blocks into 10-minute blocks and calculates the highest, lowest, and average traffic volumes within each 10-minute block. ``` FIELDS strlen(@message) AS message_length
| STATS sum(message_length) / 1024 / 1024 AS logs_mb BY BIN(5m) as @t
| STATS max(logs_mb) AS peak_ingest_mb, min(logs_mb) AS min_ingest_mb, avg(logs_mb) AS avg_ingest_mb BY dateceil(@t, 10m) ``` **Notes and limitations** A query can have a maximum of two `stats` commands. This quota can't be changed. If you use a `sort` or `limit` command, it must appear after the second `stats` command. If it is before the second `stats` command, the query is not valid. When a query has two `stats` commands, the partial results from the query do not begin displaying until the first `stats` aggregation is complete. In the second `stats` command in a single query, you can refer only to fields that are defined in the first `stats` command. For example, the following query is not valid because the `@message` field won't be available after the first `stats` aggregation. ``` FIELDS @message
| STATS SUM(Fault) by Operation # You can only reference `SUM(Fault)` or Operation at this point
| STATS MAX(strlen(@message)) AS MaxMessageSize # Invalid reference to @message ``` Any fields that you reference after the first `stats` command must be defined in that first `stats` command. ``` STATS sum(x) as sum_x by y, z
| STATS max(sum_x) as max_x by z # You can only reference `max(sum_x)`, max_x or z at this point ``` ###### Important The `bin` function always implicitly uses the `@timestamp` field. This means that you can't use `bin` in the second `stats` command without using the first `stats` command to propagate the `timestamp` field. For example, the following query is not valid. ``` FIELDS strlen(@message) AS message_length
| STATS sum(message_length) AS ingested_bytes BY @logStream
| STATS avg(ingested_bytes) BY bin(5m) # Invalid reference to @timestamp field ``` Instead, define the `@timestamp` field in the first `stats` command, and then you can use it with `dateceil` in the second `stats` command as in the following example. ``` FIELDS strlen(@message) AS message_length
| STATS sum(message_length) AS ingested_bytes, max(@timestamp) as @t BY @logStream
| STATS avg(ingested_bytes) BY dateceil(@t, 5m) ``` ## Functions to use with stats CloudWatch Logs Insights supports both stats aggregation functions and stats non-aggregation functions. Use statsaggregation functions in the `stats` command and as arguments for other functions.
| Function | Result type | Description |
| --- | --- | --- |
| `avg(fieldName: NumericLogField)` | number | The average of the values in the specified field. |
| `count()` `count(fieldName: LogField)` | number | Counts the log events. `count()` (or `count(*)`) counts all events returned by the query, while `count(fieldName)` counts all records that include the specified field name. |
| `count_distinct(fieldName: LogField)` | number | Returns the number of unique values for the field. If the field has very high cardinality (contains many unique values), the value returned by `count_distinct` is just an approximation. |
| `max(fieldName: LogField)` | LogFieldValue | The maximum of the values for this log field in the queried logs. |
| `min(fieldName: LogField)` | LogFieldValue | The minimum of the values for this log field in the queried logs. |
| `pct(fieldName: LogFieldValue, percent: number)` | LogFieldValue | A percentile indicates the relative standing of a value in a dataset. For example, `pct(@duration, 95)` returns the `@duration` value at which 95 percent of the values of `@duration` are lower than this value, and 5 percent are higher than this value. |
| `stddev(fieldName: NumericLogField)` | number | The standard deviation of the values in the specified field. |
| `sum(fieldName: NumericLogField)` | number | The sum of the values in the specified field. | **Stats non-aggregation functions** Use non-aggregation functions in the `stats` command and as arguments for other functions.
| Function | Result type | Description |
| --- | --- | --- |
| `earliest(fieldName: LogField)` | LogField | Returns the value of `fieldName` from the log event that has the earliest timestamp in the queried logs. |
| `latest(fieldName: LogField)` | LogField | Returns the value of `fieldName` from the log event that has the latest timestamp in the queried logs. |
| `sortsFirst(fieldName: LogField)` | LogField | Returns the value of `fieldName` that sorts first in the queried logs. |
| `sortsLast(fieldName: LogField)` | LogField | Returns the value of `fieldName` that sorts last in the queried logs. |
````
