

# Configure the CloudWatch agent with OpenTelemetry (recommended)

With the OpenTelemetry configuration, the agent sends metrics, logs, and traces to the CloudWatch OpenTelemetry Protocol (OTLP) endpoints. Metrics use OpenTelemetry semantic conventions and keep their labels, and you query them with PromQL. You define this configuration in the `opentelemetry` section of the agent configuration file. For a comparison with the Classic configuration, see [Choose a configuration model for the CloudWatch agent](CloudWatch-Agent-config-model.md).

**Topics**
+ [Create a CloudWatch agent configuration for OpenTelemetry](CloudWatch-Agent-OpenTelemetry-config.md)
+ [CloudWatch agent configuration file: OpenTelemetry section](CloudWatch-Agent-Configuration-File-OpenTelemetrysection.md)
+ [Scrape Prometheus metrics on Amazon EC2 instances](CloudWatch-Agent-PrometheusEC2.md)
+ [Appending OpenTelemetry collector configuration files](CloudWatch-Agent-appending-OpenTelemetry-config-files.md)