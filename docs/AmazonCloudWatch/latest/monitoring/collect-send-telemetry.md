

# Collect and send telemetry
<a name="collect-send-telemetry"></a>

CloudWatch provides multiple methods to collect and send telemetry data from your applications and infrastructure. For new work, use OpenTelemetry. You send OpenTelemetry metrics, logs, and traces to the CloudWatch OTLP endpoints, either from the CloudWatch agent or from an OpenTelemetry collector. For more information, see [OpenTelemetry](CloudWatch-OpenTelemetry-Sections.md).

You can also use the CloudWatch agent to collect metrics, logs, and traces from Amazon EC2 instances and on-premises servers. Separately, embedded metric format generates metrics from structured log data, CloudWatch Pipelines transform and route telemetry at scale, and managed Prometheus collectors discover and scrape Prometheus-compatible metrics from your AWS resources without running an agent.

**Topics**
+ [OpenTelemetry](CloudWatch-OpenTelemetry-Sections.md)
+ [Collect metrics, logs, and traces using the CloudWatch agent](Install-CloudWatch-Agent.md)
+ [Embedding metrics within logs](CloudWatch_Embedded_Metric_Format.md)
+ [CloudWatch pipelines](cloudwatch-pipelines.md)
+ [Amazon CloudWatch managed Prometheus collectors](managed-prometheus-collectors.md)