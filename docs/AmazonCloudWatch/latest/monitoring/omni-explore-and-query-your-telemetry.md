

# Explore and query your telemetry
<a name="omni-explore-and-query-your-telemetry"></a>

Explore is where you query your telemetry directly. For how telemetry reaches your space, see [Send telemetry to CloudWatch Omni](omni-send-telemetry.md). Everything in your space (logs, metrics, and traces) is queryable from one surface, so an investigation can move from a chart into the raw records behind it without changing tools. The other web UI views answer predetermined questions; Explore answers the questions you write yourself.

**Note**  
You query in two languages, split by signal: **CloudWatch Omni SQL** for logs and traces, and **PromQL** (Prometheus Query Language) for metrics. The split holds everywhere you write a query in Omni. An alert condition uses the same two languages (see [Alerts](omni-alerts.md)), and when the Omni agent writes a query for you, it is one you can open and run here (see [Ask the Omni agent](omni-ask-the-omni-agent.md)).

**Run your first query**

1. In the navigation, choose **Explore logs** or **Explore metrics**.

![](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/omni-explore-navigation.png)


1. Choose a telemetry source: **Logs**, **Metrics**, or **Traces**. The navigation entry sets the initial source, and you can switch to any of the three here. The editor opens with a runnable starter query for the source you choose.

1. Write the query in **Builder**, the query editor's guided composer, or switch the **Builder / Code** toggle to enter the query text directly. Builder shows sections for a SQL query, and a tree of metrics, labels, and functions for PromQL.

1. (Optional) Expand the fields on the Browse panel, and select a combination of values to apply as predicates for a targeted query.

1. Read the results below the editor: a table for logs and traces, with a histogram of the result distribution above it, and a line chart for metrics. You can switch the visualization and adjust its options.

You can also describe what you want in natural language and let Omni draft the query for you, then edit and run it like any other. For what the Omni agent can do beyond query drafting, see [Ask the Omni agent](omni-ask-the-omni-agent.md).

**Query logs and traces with SQL**

A SQL query addresses a signal through its table name: `"logs.default"`, `"traces.default"`. Each result row also carries system fields: `@timestamp` for time filtering, and `@record`, a JSON document holding the fully parsed telemetry record. Quote system field names in backticks:

```
SELECT `@timestamp`, `@record`
FROM "logs.default"
WHERE `@timestamp` BETWEEN now() - INTERVAL '1' DAY AND now()
LIMIT 500
```

By default, the time range you select in Explore applies to your query. You can also bound time explicitly with a `@timestamp` condition, as shown in the preceding example.

Both logs and traces are stored in the same Dataset, so a single query can cover both. Running a query against the `"default"` Dataset looks up a trace by ID across multiple applications and agents.

```
SELECT `@timestamp`, `@record`
FROM "default"
WHERE traceId = '<trace-id>'
LIMIT 100
```

For how application and agent traces relate, see [Monitor a service](omni-monitor-a-service.md).

For the language itself (supported syntax, case sensitivity, bounding time across a join, and unsupported syntax), see [SQL query reference](omni-sql-query-reference.md).

**Query metrics with PromQL**

For the language and how CloudWatch metrics support it, see [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html) and [Running PromQL queries in Query Studio](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL-QueryStudio.html) in the Amazon CloudWatch User Guide. **Builder** composes the expression — pick a metric, narrow by label values, and apply functions — or switch to **Code** and write the expression directly. In the Browse panel you can select label values before choosing a metric, and the metric list narrows to the metrics that carry them.

**Discover fields**

Fields differ across sources. For whichever signal you are querying (logs or traces), the Browse panel aggregates fields from all sources of that type, so you see every field in your current signal in one place. The field list and each field's values narrow to the rows matching your current query, so selecting a value tightens the query and the field list together.

For metrics, the Browse panel lists metrics and their labels instead of fields, and you can select label values to narrow the metric list.

To ask the same question in the query text instead, see [SQL query reference](omni-sql-query-reference.md).

**Work with results**

In the results table, you can resize, reorder, and hide columns, filter the rows, highlight keywords, and export the results. For metrics, you can adjust the chart's legend and display options, and you can change the visualization type for any result.

**CloudWatch Omni SQL limits**
+ If you do not set `LIMIT`, results are capped at 10,000 rows. Set an explicit `LIMIT` for a known row count, up to a maximum of 100,000.
+ Results are paginated: each page returns up to 1,000 rows; page through the rest with the next-page token (`nextToken` on the API).
+ A query string can be up to 64,000 characters.
+ A query times out after 60 minutes.

**Act on what you find**
+ **Alert on it.** An Omni alert takes a query as its condition, in the same two languages. You can start an alert directly from the query you ran. See [Alerts](omni-alerts.md).
+ **Keep it on a dashboard.** Save the view so the query and its visualization become a shared panel. See [Dashboards](omni-dashboards.md).
+ **Hand it to the agent.** Ask the Omni agent to investigate what the query surfaced. See [Ask the Omni agent](omni-ask-the-omni-agent.md).
+ **Automate it.** Run the same query from your own tooling through the public API, on a schedule or as part of a workflow.