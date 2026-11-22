

# Optimizing costs

You pay for the metrics, logs, and traces that the Amazon CloudWatch Observability add-on and Helm chart send to CloudWatch. For OpenTelemetry metrics, each pod and node label that the agent adds as an attribute also adds to the data that you store and query. Use the following settings to send only the telemetry that you need. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) on the AWS website.
+ [Telemetry filters](eks-observability-addon-telemetry-filters.md) – Drop the telemetry of some namespaces, drop metrics by name, and choose which pod and node labels the agent adds.
+ Turn off the features that you don't use, such as the OTLP endpoint (`otlp.enabled`), span metrics (`otlp.spanMetrics.enabled`), or individual OTel Container Insights solutions (`otelContainerInsights.solutions.{{name}}.enabled`). For the features that are on by default, see [Features that are on by default](install-CloudWatch-Observability-EKS-addon.md#install-CloudWatch-Observability-EKS-addon-defaults).

**Topics**
+ [Telemetry filters](eks-observability-addon-telemetry-filters.md)