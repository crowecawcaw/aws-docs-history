

# OpenTelemetry Metrics (Recommended)
<a name="metrics-otel-recommended"></a>

OpenTelemetry is an open-source observability framework that provides vendor-agnostic instrumentation for collecting metrics, logs, and traces from your applications. Amazon CloudWatch supports OpenTelemetry natively, enabling you to use community-standard SDKs and collectors to send metrics directly to CloudWatch without vendor lock-in.

With OpenTelemetry metrics in CloudWatch, you get:
+ **No vendor lock-in** – Instrument once with OTel SDKs, send to CloudWatch or any OTel-compatible backend. Switch destinations with a config change, not a code change.
+ **Open-source native metric names** – Use community-standard metric names (for example, `container_cpu_usage_seconds_total` from cAdvisor) instead of proprietary names. Existing PromQL dashboards and runbooks work as-is.
+ **PromQL querying** – Query with the industry-standard Prometheus Query Language. No proprietary query syntax needed.
+ **High cardinality at low cost** – Up to 150 labels per data point with per-GB pricing. No penalty for adding pod names, request IDs, or custom tags.
+ **Unified telemetry pipeline** – The same OTel Collector that collects your metrics can also collect logs and traces, simplifying your observability stack.

**Topics**
+ [CloudWatch OpenTelemetry Metrics](metrics-otel-overview.md)
+ [Publish custom metrics with OpenTelemetry](metrics-otel-send.md)
+ [Query metrics with PromQL](CloudWatch-PromQL.md)
+ [Anomaly detection using PromQL](anomaly_detection_promql.md)
+ [OTel metrics pricing and storage](metrics-otel-pricing.md)
+ [Migrate from Classic to OTel metrics](metrics-otel-migrate.md)
+ [AWS vended metrics in OpenTelemetry format](CloudWatch-OTelEnrichment.md)