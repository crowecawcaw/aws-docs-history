

# Embedding metrics within logs
<a name="CloudWatch_Embedded_Metric_Format"></a>

The CloudWatch embedded metric format allows you to generate custom metrics asynchronously in the form of logs written to CloudWatch Logs. You can embed custom metrics alongside detailed log event data, and CloudWatch automatically extracts the custom metrics so that you can visualize and alarm on them, for real-time incident detection. Additionally, the detailed log events associated with the extracted metrics can be queried using CloudWatch Logs Insights to provide deep insights into the root causes of operational events. 

**Note**  
OpenTelemetry (OTLP) metrics are the recommended path for ingesting metrics into CloudWatch. For most new workloads, publish custom metrics to the CloudWatch OTLP endpoint, for example by using the CloudWatch agent. For more information, see [Publish custom metrics with OpenTelemetry](metrics-otel-send.md).

Both embedded metric format and OpenTelemetry metrics let you publish custom metrics to CloudWatch, but they suit different needs. OpenTelemetry metrics are the better choice for most new workloads. Embedded metric format is best when you need a metric and its originating log event to stay together.

Use **OpenTelemetry (OTLP) metrics** when:
+ You are building new workloads and want the recommended, actively developed ingestion path.
+ You want to query with PromQL and reuse existing Grafana dashboards.
+ You need high-cardinality labels such as pod names, custom tags, or OpenTelemetry semantic-convention attributes. OpenTelemetry metrics support up to 150 labels per data point and handle high cardinality, but they are not suited to very high cardinality values such as per-request IDs.
+ You are instrumenting containerized applications on Amazon ECS or Amazon EKS, or you already use OpenTelemetry, Container Insights with OpenTelemetry, or CloudWatch Application Signals.

Use **embedded metric format** when:
+ You want to emit a metric and keep the detailed, high-cardinality log event it came from, so you can alarm on the metric and later investigate the underlying logs with CloudWatch Logs Insights.
+ You are running on Lambda or other ephemeral compute, where writing structured logs to standard output is the simplest way to publish metrics without running a separate collector or agent.
+ You already have embedded metric format instrumentation in place.

Embedded metric format helps you generate actionable custom metrics from ephemeral compute such as Lambda functions. By using the embedded metric format to send logs from these ephemeral resources, you can now easily create custom metrics without having to instrument or maintain separate code, while gaining powerful analytical capabilities on your log data.

No setup is required to use the embedded metric format. Either structure your logs by following the [Embedded metric format specification](CloudWatch_Embedded_Metric_Format_Specification.md), or generate them using our client libraries and send them to CloudWatch Logs using the [PutLogEvents API](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html) or the [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.html). 

To generate metrics from logs with embedded metric format, you need the `logs:PutLogEvents` permission but you don't need to also have the `cloudwatch:PutMetricData` permission.

Charges are incurred for logs ingestion and archival, and custom metrics that are generated. For more information, see [Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing).

**Note**  
Be careful when configuring your metric extraction as it impacts your custom metric usage and corresponding bill. If you unintentionally create metrics based on high-cardinality dimensions (such as `requestId`), the embedded metric format will by design create a custom metric corresponding to each unique dimension combination. For more information, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension).

**Note**  
Embedded metric format ensures at least one time delivery of metrics extracted from log events, while duplicate metric values may occasionally occur.

 The following topics describe how to publish logs using the embedded metric format, view your metrics and logs in the console, and set alarms on metrics created with the embedded metric format. 

**Topics**
+ [Publishing logs with the embedded metric format](CloudWatch_Embedded_Metric_Format_Generation.md)
+ [Viewing your metrics and logs in the console](CloudWatch_Embedded_Metric_Format_View.md)
+ [Setting alarms on metrics created with the embedded metric format](CloudWatch_Embedded_Metric_Format_Alarms.md)