

# Application traces
<a name="omni-application-traces"></a>

An application trace records one request as it passes through your services and dependencies. A span records one operation within that trace. Use this page to find a request, inspect the operations inside it, and open the related logs or service metrics.

For traces of AI agent runs, see [Agent traces](omni-agent-traces.md).

Available in the Omni web UI only.

**Open application traces**

Choose the entry point that matches what you are investigating:
+ From the launcher, under Application performance monitoring, choose `Traces` to explore requests directly.
+ From the application map, select a service and choose **Analyze traces**.
+ From Services, open a service and choose **Analyze traces**.

Select the time range you want to investigate.

Trace context does not propagate by itself: both sides of each hop must be instrumented. If the next service in a request is not instrumented, the trace stops there.

**Choose traces or spans**

Choose the investigation level that matches your question.

**Traces**

Choose Traces when you want to investigate a complete request.

Use Traces for questions such as:
+ Which requests failed?
+ Which requests were slow?
+ Which trace should you inspect in detail?

The summary above the results shows information such as Total traces and Traces with errors for the selected time range.

**Spans**

Choose Spans when you want to search individual operations across traces.

Use Spans for questions such as:
+ Which DynamoDB.PutItem operations reported errors?
+ Which dependency operations took the longest?
+ Which operations ran in a particular service?
+ Which spans match a status or attribute?

Use Search spans to find an operation by name. Use the status control or Errors filter to narrow the results.

The results show when each span occurred and the operation it represents.

**Investigate a request**

1. Select the relevant time range.

1. Use Traces to find a complete request, or use Spans to find a specific operation.

1. Select a trace to review the operations that occurred during the request.

1. Find the span where an error occurred or where the request spent unexpected time.

1. Open related logs or service metrics when you need more evidence.

For aggregate application topology, see [Monitor applications with the application map](omni-monitor-applications-with-the-application-map.md). For one service's health and telemetry, see [Monitor a service](omni-monitor-a-service.md).

**Inspect a trace**

Select a trace to open its detail view. The trace header shows the trace ID and the number of spans in the trace.

Switch among the available views:
+ Timeline
+ Graph
+ Flame
+ JSON

Use the Timeline view to follow span timing and parent-child relationships.

You can also:
+ Search for a span within the trace.
+ Filter spans by status.
+ Choose Tree to follow parent-child structure.
+ Choose Grouped to organize similar spans together.
+ Use Errors to focus on spans that reported an error.
+ Choose Reset to remove the current trace-detail filters.

Select a span to inspect its details.

**Inspect trace or span details**

Use the Trace and Span controls in the detail view to change the scope of the information shown. Choose Trace to review information about the complete request. Choose Span to review the selected operation.

The span detail can include:
+ Name
+ Span ID
+ Parent ID
+ Trace ID
+ Service
+ Start
+ End
+ Scope
+ Status and duration

Expand the following sections when you need more detail:
+ Span attributes
+ Resource attributes
+ Annotations
+ Raw data

**View logs for a trace**

Logs can provide details that are not present in the trace, such as application messages, exceptions, and business events. From the trace header, choose **Show logs for this trace**. The logs view opens the records associated with the trace when the required correlation information is available.

If no logs appear, confirm that:
+ The application produced logs during the request.
+ Those logs were sent to your space.
+ The selected time range includes the request.
+ The log records contain the trace ID used for correlation.

Where supported by your instrumentation, include span and service context in log records as well, so you can narrow logs to the operation and service under investigation. For telemetry configuration, see [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).

**View metrics for a service**

Choose **Show metrics for this service** to investigate the metrics associated with the service in the current trace context.

Use service metrics to determine whether the problem in the trace occurred alongside a broader change in request volume, latency, errors, or infrastructure behavior.

For service-level monitoring, see [Monitor a service](omni-monitor-a-service.md).

**When trace information is incomplete**

Trace investigation depends on the telemetry your applications send. Use the following checks when information is missing:
+ No traces appear. Confirm the time range and verify that the workload is sending traces.
+ A trace stops at one service. Confirm that the next service is instrumented and propagates trace context.
+ A trace has only one or a few flat spans. Verify that the workload records the internal operations you need to inspect.
+ Related logs do not appear. Confirm log ingestion and trace-ID correlation.
+ Service metrics do not appear. Confirm that the service publishes the required metrics.

**Where to go next**


|  |  | 
| --- |--- |
| To do this | See or choose | 
| Review the service involved in the trace | [Monitor a service](omni-monitor-a-service.md) | 
| See application topology and dependencies | [Monitor applications with the application map](omni-monitor-applications-with-the-application-map.md) | 
| Open logs associated with the request | Show logs for this trace | 
| Examine metrics for the service | Show metrics for this service | 
| Query trace or log records directly | [Explore and query your telemetry](omni-explore-and-query-your-telemetry.md) | 
| Investigate an AI agent run instead | [Agent traces](omni-agent-traces.md) | 