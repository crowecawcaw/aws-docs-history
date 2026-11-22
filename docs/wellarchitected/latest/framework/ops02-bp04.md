

# OPS02-BP04 Regularly analyze workload logs

 Logs are the most detailed telemetry a workload produces, recording every request, error, and component decision. At production volume, no human being is reading logs line by line. Regular log analysis uses queries and machine assistance to extract patterns and answers from that detail. 

 **Desired outcome:** 
+  You analyze your logs on a defined cadence, not only when an incident forces you to. 
+  You know the frequent patterns in your logs, so a new error signature stands out on sight. 
+  When you troubleshoot, you find the log events that explain a symptom quickly, wherever in the workload they were written. 
+  You set each log group's retention and storage class to match the value you get from analyzing it. 

 **Common anti-patterns:** 
+  Logs are collected diligently but only read after a critical issue has already surfaced. 
+  Teams search logs manually and eyeball, leaving the query, pattern, and anomaly tools unused. 
+  Every log group is retained indefinitely in full-price storage regardless of how it is used. 
+  Analysis stops at account boundaries, so behavior that spans accounts goes unread. 

 **Benefits of establishing this best practice:** 
+  Operational bottlenecks and security threats surface proactively, before they become incidents. 
+  Machine assistance reads the volume a human cannot, so unusual events are seen rather than missed. 
+  Debugging accelerates because the log detail behind a symptom is one query away. 
+  Log spend stays proportionate to value instead of growing with volume by default. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A metric shows that something changed, a trace shows where in the request path it happened, and the logs show the reason, such as the error text, the input that triggered the error, and the state the component recorded. Analyze logs on the same cadence and against the same baselines defined in [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md). 

 A workload can produce millions of log events an hour. Use queries and machine analysis instead of reading them manually. Pattern analysis condenses those millions of events into a short list of recurring shapes you can review. Comparing patterns between time ranges shows what changed after a deployment or at the start of an incident. Anomaly detection runs continuously between reviews, learning each log group's normal output and flagging what does not fit. 

 When a query matches more events than a person can read, [generate a natural language summary of the query results](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Results-Summary.html) directly in Log Analytics. Amazon CloudWatch investigations and AWS DevOps Agent read log data when correlating a problem. AI agents can also gather log data through the [Model Context Protocol servers for AWS](https://github.com/awslabs/mcp). These assistants work best on structured, well-classified, queryable logs. 

 Some questions need more than one log group to answer. A request that touches several services leaves entries across several log groups, so correlate them by joining log groups on shared fields such as a request ID. CloudWatch Logs Insights supports [joins](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Join.html) across log groups and [subqueries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Subqueries.html) that filter one log group by what is found in another. Index the fields you join and filter on most to keep queries fast and reduce the volume scanned. 

 With [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) enabled, spans are stored as structured logs in CloudWatch Logs and can be queried alongside application logs from the same request. Analyzing trace data itself is covered in [OPS02-BP05 Regularly analyze workload traces](ops02-bp05.md). 

 [OpenTelemetry treats logs as one of its three signals](https://opentelemetry.io/docs/concepts/signals/logs/), and its logging bridges attach to your existing logging frameworks, injecting trace and span context into each record. Logs built this way correlate with traces by default, and the fields you join and filter on are already structured — queries do not need to parse them out of free text. For instrumentation details, see [OPS01-BP01 Develop application telemetry](ops01-bp01.md). 

 Amazon's practice, described in [Instrumenting distributed systems for operational visibility](https://builder.aws.com/content/3EuxPBdIiiUhB5IK47p3O3fxhy7/instrumenting-distributed-systems-for-operational-visibility), is one structured log entry per unit of work. A request or a message produces a single record carrying its properties, every counter, and every timer, so a failed request is one log entry to find. Debugging output goes to separate log groups, so request-log analysis works on one consistent format. Metrics remain their own OpenTelemetry signal. The request log holds the same measurements per request, so when a metric moves, the detail that explains it is already in the logs. Where a component emits no metrics, derive them from its logs with metric filters. 

 Match each log group's storage class and retention to how it is used: logs you alarm on need full capability, logs kept for occasional queries can use a lower-cost class, and logs nobody has queried in a year might not need their current retention. 

 [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) holds the log groups, runs the queries, learns the patterns, and connects log signals to the metrics and alarms in the rest of your observability practice. [Log Analytics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogAnalytics.html) is the default console for this work. It combines queries, real-time streaming, and top-contributor analysis in one place, with saved parameterized queries, facets for exploring results, and query generation from natural language. 

 For workloads instrumented with OpenTelemetry, [CloudWatch Omni](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-explore-and-query-your-telemetry.html) queries the same logs with SQL, drafted from a plain language question if you prefer. From a trace's detail view, you can [open the log records that carry that trace ID](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-application-traces.html). This works only when each log record contains the trace ID, which can be injected using the previously described logging bridge. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Bring logs where analysis happens:** Confirm the workload's components send logs to [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html), and enable [cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) where the workload spans accounts, so one query can read the whole footprint. The collection and structure of these logs is developed in [OPS01-BP01 Develop application telemetry](ops01-bp01.md). 

1.  **Enable log anomaly detection:** Create [log anomaly detectors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html) on the log groups that matter, so unusual patterns are flagged as they appear rather than waiting for the next review. When an anomaly points at a broader problem, you can start a [CloudWatch investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) to correlate it with related telemetry and recent changes. 

1.  **Query logs instead of reading them:** Work in [Log Analytics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogAnalytics.html) to extract answers from log data with [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) queries, written for you from a natural-language prompt or manually. When a query's results are still more than a person can read, [generate a natural language summary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Results-Summary.html) of them. Review [pattern analysis](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Patterns.html) to see recurring event shapes at a glance, and [compare time ranges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Compare.html) to isolate what changed after a deployment or at incident onset. For analysis beyond what queries express, enable the [S3 Tables Integration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/s3-tables-integration.html) so your logs are also available as managed Apache Iceberg tables, queryable in place by Amazon Athena, Amazon Redshift, or any Iceberg-compatible engine, and correlatable with data that lives outside CloudWatch. 

1.  **Correlate across log groups:** Answer request-path questions by [joining log groups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Join.html) on shared fields such as request IDs, and use [subqueries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Subqueries.html) to filter one group by what you find in another. [Create field indexes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html) on the fields you join and filter on most, to speed queries and cut the volume they scan. 

1.  **Watch live when it matters:** Use [Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html) to stream log events in real time during deployments and incident response, when waiting for the next query cycle is too slow. 

1.  **Turn recurring log signals into metrics:** Create [metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) for the log events you keep querying for, so they become metrics you can chart and alarm on. Counting each distinct error reason separately keeps the resulting error metrics readable instead of noisy. Use [Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) to rank the top contributors inside high-cardinality fields such as caller IPs or user agents. 

1.  **Let assistants read at scale:** When a flagged anomaly or a deviating metric needs explaining, start a [CloudWatch investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) from it, so related telemetry, the logs included, is correlated into a hypothesis of the probable cause. Use [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) to read operational signals, including log data, proactively between reviews, surfacing concerning trends with prioritized improvements. AI agents can also gather log data on request through the [CloudWatch MCP server](https://github.com/awslabs/mcp/tree/main/src/cloudwatch-mcp-server), and whatever the source of a result set too large to read, [generate a natural language summary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Results-Summary.html) of it. Route machine findings to the teams that own the affected components, and confirm them against the patterns and baselines this practice maintains. 

1.  **Match storage to analytical value:** Assign the [Infrequent Access log class](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html) to log groups you keep for occasional analysis rather than alerting, and set retention per log group based on how far back its analysis reaches. Revisit these choices as usage changes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md) 
+  [OPS02-BP05 Regularly analyze workload traces](ops02-bp05.md) 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 
+  [OPS01-BP01 Develop application telemetry](ops01-bp01.md) 

 **Related documents:** 
+  [Instrumenting distributed systems for operational visibility](https://builder.aws.com/content/3EuxPBdIiiUhB5IK47p3O3fxhy7/instrumenting-distributed-systems-for-operational-visibility) 
+  [Analyzing log data with CloudWatch Log Analytics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogAnalytics.html) 
+  [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) 
+  [Log anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html) 
+  [Create field indexes to improve query performance and reduce scan volume](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html) 
+  [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html) 
+  [Metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) 
+  [Using Contributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) 
+  [Generate a natural language summary from query results](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Results-Summary.html) 
+  [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) 
+  [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/) 
+  [CloudWatch MCP server](https://github.com/awslabs/mcp/tree/main/src/cloudwatch-mcp-server) 
+  [CloudWatch Omni: Explore and query your telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-explore-and-query-your-telemetry.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - What's new with Amazon CloudWatch (COP363)](https://www.youtube.com/watch?v=MQmNzKZsx44) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US/intro) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 