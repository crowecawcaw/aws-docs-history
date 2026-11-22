

# Using the CloudWatch agent for Amazon EKS Container Insights

The CloudWatch agent powers Container Insights on Amazon EKS. You don't install or configure the agent yourself for this use case. Instead, Container Insights on Amazon EKS is deployed through the `amazon-cloudwatch-observability` Amazon EKS add-on, which runs the CloudWatch agent and an OpenTelemetry Collector as a DaemonSet on your cluster. Together they collect infrastructure metrics, container logs, and performance data from the cluster.

There are two configurations of the same add-on:
+ **OTel Container Insights (recommended)** – the actively developed configuration, built on OpenTelemetry. For more information, see [OTel Container Insights (Recommended)](container-insights-eks-otel.md).
+ **Enhanced Container Insights (Classic)** – the earlier configuration of the same add-on. For more information, see [Enhanced Container Insights (Classic)](container-insights-eks-classic.md).

The difference between them is the add-on version and configuration, not a different product.

Because installing the add-on sets up and configures the agent for you, you don't create an agent configuration file for Container Insights on Amazon EKS. To get started, see [Quick start](container-insights-eks-otel-quickstart.md). For instructions on installing the add-on, including the Helm chart option, see [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md).