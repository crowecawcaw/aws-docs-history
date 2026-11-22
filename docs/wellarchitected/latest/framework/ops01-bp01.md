

# OPS01-BP01 Develop application telemetry

 Application telemetry is the metrics, logs, and traces your workload emits about its own behavior. Without it, you cannot tell whether a release improved or degraded the experience. When telemetry ties technical signals to business outcomes, you see both system health and whether the workload delivers the results the business expects. 

 **Desired outcome:** 
+  Your application emits metrics, logs, and traces across every layer, from infrastructure to business logic. 
+  You can connect a technical signal to the business outcome it affects, because your telemetry is tied to defined key performance indicators (KPIs). 
+  Your telemetry lands in a consistent format and a consolidated location, rather than scattered across disconnected tools. 
+  Your telemetry surfaces anomalies automatically, so you detect degraded behavior before customers report it. 
+  You mask sensitive data in logs before storage, so your telemetry does not become a compliance liability. 

 **Common anti-patterns:** 
+  Teams instrument only part of the stack, leaving gaps where failures go unseen. 
+  Data lands in several disconnected tools, so no one can assemble a complete view of workload health. 
+  Organizations track technical metrics but never define business KPIs, so they cannot tell whether the workload delivers value. 
+  Teams wait for user complaints instead of detecting anomalies in the telemetry they already collect. 
+  Logs capture personally identifiable information in plain text, creating a privacy and compliance exposure. 

 **Benefits of establishing this best practice:** 
+  Data-driven decisions replace guesswork, because operators see how the workload actually behaves. 
+  Issues are detected and resolved faster, which improves availability. 
+  Resource decisions improve, because usage data shows where capacity is wasted or constrained. 
+  Business KPIs reveal problems that technical metrics alone miss, such as a checkout flow that succeeds technically but loses customers. 
+  Consistent instrumentation makes telemetry from new components immediately comparable with the rest of the workload. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Observability refers to three kinds of telemetry: metrics, logs, and traces. Metrics are numeric measurements over time, cheap to store and quick to alert on. Logs are timestamped records of discrete events, rich in detail but expensive at volume. Traces follow a single request across components. High-cardinality metrics and verbose logs raise cost and obscure the signal you need, so decide what each data type must answer before you instrument. 

 A service can return a success code for every request while customers abandon a broken checkout flow. Business KPIs measure outcomes the organization cares about, such as completed orders or sign-ups. A central team sets KPI naming and definition conventions, while the workload owner instruments the application to emit the underlying data. 

 [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) collects metrics and logs from applications and infrastructure in AWS and on-premises environments, and [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) captures and analyzes traces. Both support anomaly detection, which learns a normal baseline from historical data and alerts on deviations, so you avoid hand-tuning static thresholds. [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) builds on this telemetry: it instruments supported application runtimes automatically using OpenTelemetry, collects the RED metrics (rate, errors, and duration) for each service and operation, discovers the dependencies your application calls, and lets you define service level objectives (SLOs) on those metrics or on any CloudWatch metric. For these tools to work across the whole workload, every component must emit and name telemetry consistently. 

 OpenTelemetry provides an open standard for this use case. The CloudWatch agent, an AWS-managed OpenTelemetry collector with CloudWatch components built in, is the recommended collection path. Any OpenTelemetry SDK can send metrics and traces to the agent over OTLP. The agent delivers them to Amazon CloudWatch and AWS X-Ray alongside previously collected logs. Send telemetry directly to the OTLP endpoints only when running an agent is impractical, such as with serverless functions at the edge. 

 You can use [CloudWatch Omni](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-omni.html), the OpenTelemetry-based experience in CloudWatch, to read this telemetry after setting up a domain and space. To read traces, you also must enable [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html) in the account and Region that receives your traces. Omni identifies each service by the service name set by your instrumentation, derives its dependencies from your outbound calls, and reports its RED metrics from span metrics. For upstream OpenTelemetry SDKs, the [CloudWatch plugin for OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-send-application-telemetry.html) generates those span metrics (while the AWS Distro for OpenTelemetry SDK generates its own). Because it stays inert unless a metrics exporter is configured alongside the trace exporter, consider adding both services. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify what to collect:** Decide which metrics, logs, and traces answer real questions about workload health, performance, and behavior. Tie each data source to a question an operator or a business stakeholder needs answered, and leave out data that answers nothing. 

1.  **Instrument the application to emit metrics, logs, and traces:** Add instrumentation in application code so each layer produces telemetry, and [instrument your application for tracing](https://docs.aws.amazon.com/xray/latest/devguide/xray-instrumenting-your-app.html) to record how requests move through it. Emit structured logs and named metrics so downstream analysis can parse them consistently. Where the runtime is supported, [enable Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html) to instrument the application automatically before writing custom instrumentation manually. 

1.  **Deploy the CloudWatch agent:** Install the [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) to collect system and application metrics and logs from your workload and its infrastructure. The agent is an AWS-managed OpenTelemetry collector: any OpenTelemetry SDK can [send metrics and traces to it over OTLP](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-OpenTelemetry-metrics.html), which makes it the recommended collection path for OpenTelemetry-instrumented components. 

1.  **Monitor business KPIs:** Instrument the application to emit KPI measurements as OpenTelemetry metrics, so business outcomes flow through the same collection path as the rest of your telemetry. Where a component is not instrumented with OpenTelemetry, publish [custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) directly instead. Monitor for business outcomes to choose KPIs that reflect value delivered, not just requests served. Define the KPIs themselves first, as described in [OPS02-BP01 Develop key performance indicators](ops02-bp01.md). This step instruments the application to emit the data that measures them. 

1.  **Enable anomaly detection for logs and metrics:** Turn on [CloudWatch Logs anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html) and [CloudWatch metrics anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) so unusual behavior is flagged against a learned baseline. Route the resulting alerts to the teams that own the affected components. 

1.  **Mask sensitive log data:** Apply [CloudWatch Logs data protection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) to detect and mask sensitive fields before they are stored or read. This keeps personally identifiable information out of your telemetry pipeline. 

1.  **Standardize collection across the workload:** Agree on shared conventions for metric names, log structure, and trace attributes so data from every component correlates. Uniform instrumentation is what lets you compare and join telemetry across services. Start from the [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) rather than inventing a naming scheme: they define standard names and attributes for common operations, resources, and signals, so your telemetry correlates not only across your own components but with what instrumentation libraries and AWS services already emit. 

1.  **Consolidate across accounts:** Use [Amazon CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) to bring metrics, logs, and alarms from multiple accounts into one view. This shortens response times for issues that span your AWS environment. 

1.  **Analyze and act on the data:** Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/features/) for metric and log analysis and [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) for trace analysis to turn collected telemetry into decisions. Feed what you learn back into which signals you collect and which KPIs you track. With [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html) enabled, spans are stored in OpenTelemetry format in CloudWatch Logs, so every transaction is searchable rather than a sampled subset, and you can query spans using the same semantic-convention attribute names your instrumentation emits. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 
+  [OPS01-BP02 Develop user experience telemetry](ops01-bp02.md) 
+  [OPS01-BP03 Develop dependency telemetry](ops01-bp03.md) 
+  [OPS01-BP04 Develop distributed tracing](ops01-bp04.md) 

 **Related documents:** 
+  [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/) 
+  [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) 
+  [AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) 
+  [Instrumenting distributed systems for operational visibility](https://builder.aws.com/content/3EuxPBdIiiUhB5IK47p3O3fxhy7/instrumenting-distributed-systems-for-operational-visibility) 
+  [AWS Observability Skill Builder course](https://skillbuilder.aws/learn/F1MH4GQSG8/aws-observability/KFYCBWBF3V) 
+  [What's new with Amazon CloudWatch](https://aws.amazon.com/about-aws/) 
+  [OpenTelemetry in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPGettingStarted.html) 
+  [Collect metrics and traces with OpenTelemetry using the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-OpenTelemetry-metrics.html) 
+  [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) 
+  [CloudWatch OpenTelemetry metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-otel-overview.html) 
+  [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html) 
+  [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) 
+  [CloudWatch Omni](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-omni.html) 
+  [Send application telemetry to CloudWatch Omni](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-send-application-telemetry.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Elevate application and generative AI observability (COP326)](https://www.youtube.com/watch?v=vxzq8GthOLs) 

 **Related examples:** 
+  [Application observability and APM with Amazon CloudWatch](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Application observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) 