

# OPS02-BP05 Regularly analyze workload traces

 A trace shows the path a request takes through your workload. Trace analysis looks at these paths at the scale of your entire architecture. While metrics quantify changes and logs record what each component did, traces show how the parts of your workload behaved together: which service added latency, which dependency returned an error, and which interaction pattern is drifting. 

 **Desired outcome:** 
+  You analyze your trace data on a defined cadence, not only when an incident forces you to. 
+  You find slow and failing request paths in your trace data before users report them. 
+  Your trace analysis reads the RED metrics (rate, errors, duration) derived from traces, not only individual timelines. 
+  Your traces connect to the logs and client-side telemetry behind them, so one analysis explains a request from frontend to backend. 

 **Common anti-patterns:** 
+  Traces are collected but overlooked, and analysis relies on logs and metrics alone. 
+  Trace data is not correlated with the logs recorded during the same request. 
+  The RED metrics derived from traces go unread per service and dependency. 
+  Analysis only ever inspects single traces, so patterns across thousands of requests stay invisible. 

 **Benefits of establishing this best practice:** 
+  Troubleshooting improves and mean time to resolution falls, because the failing service is found rather than guessed. 
+  Dependencies and their impact on the request path become visible and quantified. 
+  Performance issues are identified and corrected swiftly, including the ones only some requests experience. 
+  Trace-derived metrics inform decisions about where optimization effort pays back. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 This practice assumes traces exist (for detail on instrumenting and collecting traces, see [OPS01-BP04 Develop distributed tracing](ops01-bp04.md)). The cadence and baseline discipline come from [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md). Trace analysis joins that same review and does not need its own schedule. Traces answer questions metrics and logs cannot: where in the request path the workload is slow, for which requests, and why. 

 Trace analysis needs both a close view of single requests and a wide view across many. The wide view starts with the RED metrics derived from traces: request rate, errors, and duration per service and dependency. Drift in those aggregates tells you which service's traces are worth opening. From there, work from the service to its slowest operations, from the operations to the requests in the tail, and from a tail request to the exact call that put it there. 

 Store spans as structured data so you can query them precisely. Which checkout requests over five seconds touched the payment service yesterday? Which customers hit the failing dependency? Does the latency follow a specific attribute your instrumentation emits? Query every transaction to measure who is affected and by how much. Use OpenTelemetry's [trace semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/trace/) as the attribute vocabulary (as described in [OPS01-BP01 Develop application telemetry](ops01-bp01.md)). The same query works across services regardless of which SDK produced the span, because attribute names are standardized. 

 Include client-side traces from real users and synthetic canaries alongside backend traces, so client-experienced latency ties to the backend call that caused it. Correlate traces with logs: the trace locates the failing service, and the logs recorded during that request explain it. Extend the analysis view across every account the workload runs in, so one investigation follows a request from the frontend to the log line. 

 Enable [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html) as the trace-analysis entry point. You get per-service views of the RED metrics derived from trace data, dependency breakdowns, and the correlated traces for each. The [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) console remains the trace backend's own analysis surface, and its insights feature raises anomalies automatically. AI assistants extend the same reading: CloudWatch investigations correlates trace data with related telemetry when something needs explaining, AWS DevOps Agent reviews it proactively, and MCP servers make trace data available to AI agents from wherever they work. 

 When a traced workload is an AI agent, a trace that completed quickly and without errors can still contain a well-formed response that is wrong. In this scenario, CloudWatch Omni scores agent responses with your chosen [evaluators](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-agents-evaluate.html) on a sample of production traffic or on demand against a dataset, and then shows the scores on the trace next to its latency, errors, and token usage. You can read these scores as one more trace-derived signal in your workload review. For more detail on evaluation as a discipline, see [AGENTOPS06 Testing, evaluation, and validation frameworks](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06.html). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Start from the service views:** With Application Signals enabled, begin each review on the [Services page](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services-page.html): compare each service's RED metrics and dependency latencies against your baseline, and open the [service detail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceDetail.html) to reach the traces behind a drifting number. The trace-derived aggregates decide where deeper trace reading is worth the time. 

1.  **Set objectives on the RED metrics:** Create [service level objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) on the services and operations that matter most, using the same RED metrics the service views read: Application Signals offers the duration and errors it already collects, as latency and availability, for ready-made service level indicators. It tracks attainment against the goal you set and can alarm on error-budget burn rate, so a fast burn interrupts you instead of waiting for the next review. Those alarms, for an objective at risk or already breached, can be [configured to create investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-configure-alarms.html) automatically, so the correlation work starts before you arrive. The SLO dashboard answers each review's first question, whether the workload is meeting its objectives, at a glance. 

1.  **Query spans across every transaction:** With [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) enabled, spans are stored in OpenTelemetry format in CloudWatch Logs, so you can [search and analyze them](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-search-analyze-spans.html) with the attribute names your instrumentation emits. Quantify the tail: how many requests, which users, which shared attribute. In CloudWatch Omni, the same spans are queryable with SQL from [Explore](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-explore-and-query-your-telemetry.html), including a lookup of one trace ID across every application and agent that handled it. 

1.  **Let anomalies find you between reviews:** Enable [X-Ray insights](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-insights.html) so anomalies in trace data, such as rising fault rates or latency, are raised automatically with their probable root cause and a timeline. Review open insights as part of the cadence, and use [groups](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-groups.html) to scope insights to the request paths that matter most. 

1.  **Explore patterns interactively:** Use [X-Ray Analytics](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-analytics.html) to compare trace sets against each other, such as the slow tail against the healthy baseline, and identify the attributes that distinguish them. Filter into the latency distribution rather than averaging over it. 

1.  **Correlate traces with logs:** Enable [trace to log correlation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application-Signals-TraceLogCorrelation.html) so the log events recorded during a traced request are reachable from the trace itself. The trace locates the failing service. The correlated logs explain it. 

1.  **Include the client's view:** Analyze traces that begin at [real users](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) and [synthetic canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) alongside backend traces, so client-experienced latency is attributed to the backend call that caused it, and regressions are caught by canaries before users meet them. Developing this telemetry is covered in [OPS01-BP02 Develop user experience telemetry](ops01-bp02.md). 

1.  **Let assistants read at scale:** When an SLO metric or a flagged anomaly needs explaining, start a [CloudWatch investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-CreateInvestigation-SLO.html) from it, so trace data is correlated with related telemetry and recent changes into a hypothesis of the probable cause. Use [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) to review operational signals, trace data included, proactively between reviews. AI agents can also analyze the same data from wherever they work through the [Application Signals MCP server](https://github.com/awslabs/mcp/tree/main/src/cloudwatch-applicationsignals-mcp-server), which reads service health, SLO compliance, and the spans behind them. Route machine findings to the teams that own the affected components, and confirm them against the baselines this practice maintains. 

1.  **Span the whole footprint:** Configure [Transaction Search across accounts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-cross-account-observability.html) with CloudWatch cross-account observability, so trace analysis follows requests wherever the workload runs instead of stopping at an account boundary. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS01-BP04 Develop distributed tracing](ops01-bp04.md) 
+  [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md) 
+  [OPS02-BP04 Regularly analyze workload logs](ops02-bp04.md) 
+  [OPS01-BP02 Develop user experience telemetry](ops01-bp02.md) 

 **Related documents:** 
+  [OpenTelemetry trace semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/trace/) 
+  [Service level objectives (SLOs)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) 
+  [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) 
+  [Searching and analyzing spans](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-search-analyze-spans.html) 
+  [Detecting anomalies in traces with X-Ray insights](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-insights.html) 
+  [Exploring trace data with X-Ray Analytics](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-analytics.html) 
+  [Enable trace to log correlation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application-Signals-TraceLogCorrelation.html) 
+  [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) 
+  [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/) 
+  [Application Signals MCP server](https://github.com/awslabs/mcp/tree/main/src/cloudwatch-applicationsignals-mcp-server) 
+  [CloudWatch Omni: Explore and query your telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-explore-and-query-your-telemetry.html) 
+  [CloudWatch Omni: Evaluate agent quality](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-agents-evaluate.html) 
+  [AWS Well-Architected Agentic AI Lens: Testing, evaluation, and validation frameworks](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Observability for AI Agents and Traditional Workloads (COP335)](https://www.youtube.com/watch?v=oYpCvqZk9SQ) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US/intro) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) 