

# Install the CloudWatch agent on Amazon EKS

On Amazon EKS, you don't install the CloudWatch agent with the Amazon EC2 or manual methods. Instead, install it through the `amazon-cloudwatch-observability` Amazon EKS add-on, or the add-on's Helm chart. The add-on runs the CloudWatch agent and an OpenTelemetry collector as a DaemonSet, and by default it turns on Container Insights and CloudWatch Application Signals.

To get started quickly, see [Quick start](container-insights-eks-otel-quickstart.md).

To install the add-on, including the Helm chart option, see [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md).

For how the agent powers Container Insights on Amazon EKS, see [Using the CloudWatch agent for Amazon EKS Container Insights](CloudWatch-Agent-container-insights-eks.md).

To receive OTLP data from your applications through the agent on Amazon EKS, you must use add-on version 6.6.0 or later and supply the agent `opentelemetry` and `otlp` configuration to the add-on. The add-on doesn't turn on the OTLP receiver by default. For more information, see [Amazon CloudWatch agent](CloudWatch-OTLPCloudWatchAgent.md).