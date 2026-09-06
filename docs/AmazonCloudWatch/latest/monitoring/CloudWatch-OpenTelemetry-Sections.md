

# OpenTelemetry
<a name="CloudWatch-OpenTelemetry-Sections"></a>

**Tip**  
To learn more about OpenTelemetry on CloudWatch, check out the [Cloud Operations Enablement workshop and event series](https://aws-experience.com/amer/smb/events/series/Cloud-Operations-Enablement).

OpenTelemetry is an open-source observability framework that provides vendor-agnostic instrumentation for collecting metrics, logs, and traces from your applications. Amazon CloudWatch supports OpenTelemetry natively across all three signal types: metrics queryable with PromQL for flexible and scalable analytics, logs searchable with Logs Insights, and traces explorable with [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html). Because all three signals share a common data model with consistent attributes, you can correlate across metrics, logs, and traces to move from detection to root cause faster. OpenTelemetry metrics carry rich semantic labels and support higher granularity than traditional CloudWatch metrics, enabling precise filtering, aggregation, and analysis across your applications and infrastructure.

CloudWatch supports OpenTelemetry metrics, allowing you to send custom OTel metrics directly to CloudWatch and query them using PromQL alongside AWS vended metrics from over 70 services. You can use PromQL to build dashboards, set CloudWatch Alarms, and explore metrics in Query Studio, the native PromQL console experience. OTel logs sent to CloudWatch are available in Logs Insights for interactive querying and in LiveTail for real-time streaming.

For application performance monitoring, CloudWatch [Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Intro.html) provides a unified, application-centric view of your services and dependencies. Application Signals uses OTLP traces to help you monitor application health, triage issues, and identify the impact on end users. With Transaction Search, you can explore OTLP spans interactively, find transactions using attributes such as customer identifiers or order numbers, correlate transactions to business events such as failed payments, and trace interactions between application components to establish root cause.

![OpenTelemetry overview.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/OpenTelemetry.png)


**Topics**
+ [OTLP Endpoints](CloudWatch-OTLPEndpoint.md)
+ [Getting started](CloudWatch-OTLPGettingStarted.md)
+ [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md)
+ [Troubleshooting](CloudWatch-OTLPTroubleshooting.md)