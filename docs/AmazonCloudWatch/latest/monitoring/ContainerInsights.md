

# Container Insights for Amazon EKS

Use CloudWatch Container Insights to collect, aggregate, and summarize metrics and logs from your containerized applications and microservices. The topics in this section cover Container Insights on Amazon Elastic Kubernetes Service (Amazon EKS), RedHat OpenShift on AWS (ROSA), and Kubernetes on Amazon EC2. Container Insights supports clusters deployed on AWS Fargate.

For Container Insights on Amazon Elastic Container Service (Amazon ECS), see [Container Insights for Amazon ECS](deploy-container-insights-ECS.md).

The default way to set up Container Insights on an Amazon EKS cluster is to install the Amazon CloudWatch Observability Amazon EKS add-on (`amazon-cloudwatch-observability`) or the Amazon CloudWatch Observability Helm chart. Both install the same components: the CloudWatch agent on every node, a cluster-level CloudWatch agent, and the CloudWatch agent operator. The add-on and the chart accept the same configuration values, so a feature that you can turn on with one, you can turn on with the other.
+ Use the Amazon EKS add-on when you manage your cluster with Amazon EKS tools, such as the Amazon EKS console, the AWS CLI, CloudFormation, or eksctl. Amazon EKS installs and updates the add-on for you.
+ Use the Helm chart when you manage your cluster with Helm or a GitOps tool, or when your cluster is a Kubernetes cluster that is not hosted on Amazon EKS. The chart is published in the [aws-observability/helm-charts](https://github.com/aws-observability/helm-charts) repository on the GitHub website.

To install the add-on or the chart, and to see which features are on by default, see [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md). To change its configuration, see [Configuring the add-on and the Helm chart](eks-observability-addon-configure.md).

Container Insights on Amazon EKS comes in two variants. For a comparison, see [Compare Container Insights approaches](container-insights-eks-compare.md).
+ [Enhanced Container Insights (Classic)](container-insights-eks-classic.md) – Sends CloudWatch metrics through embedded metric format. Application Signals (Classic) belongs to this variant.
+ [OTel Container Insights (Recommended)](container-insights-eks-otel.md) – Sends OpenTelemetry metrics that you query with PromQL. The OTLP endpoint, ServiceMonitor and PodMonitor scraping, service identity, the standard telemetry attributes, and the telemetry filters are described under this variant.

CloudWatch automatically collects metrics for many resources, such as CPU, memory, disk, and network. Container Insights also provides diagnostic information, such as container restart failures, to help you isolate issues and resolve them quickly. You can also set CloudWatch alarms on metrics that Container Insights collects.

Container Insights collects data as *performance log events* using [embedded metric format](CloudWatch_Embedded_Metric_Format.md). These performance log events are entries that use a structured JSON schema that enables high-cardinality data to be ingested and stored at scale. From this data, CloudWatch creates aggregated metrics at the cluster, node, pod, task, and service level as CloudWatch metrics. The metrics that Container Insights collects are available in CloudWatch automatic dashboards, and are also viewable in the **Metrics** section of the CloudWatch console. Metrics are not visible until the container tasks have been running for some time.

When you deploy Container Insights, it automatically creates a log group for the performance log events. You don't need to create this log group yourself.

To help you manage your Container Insights costs, CloudWatch does not automatically create all possible metrics from the log data. However, you can view additional metrics and additional levels of granularity by using CloudWatch Logs Insights to analyze the raw performance log events.

With the original version of Container Insights, metrics collected and logs ingested are charged as custom metrics. With Container Insights with enhanced observability for Amazon EKS, Container Insights metrics and logs are charged per observation instead of being charged per metric stored or log ingested. For more information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

For Amazon EKS, OTel Container Insights collects metrics using the OpenTelemetry Protocol (OTLP) and supports PromQL queries. Each metric is enriched with up to 150 labels, including OpenTelemetry semantic convention attributes and Kubernetes pod and node labels. For more information, see [OTel Container Insights (Recommended)](container-insights-eks-otel.md).

In Amazon EKS, RedHat OpenShift on AWS, and Kubernetes, Container Insights uses a containerized version of the CloudWatch agent to discover all of the running containers in a cluster. It then collects performance data at every layer of the performance stack.

Container Insights supports encryption with the AWS KMS key for the logs and metrics that it collects. To enable this encryption, you must manually enable AWS KMS encryption for the log group that receives Container Insights data. This causes Container Insights to encrypt this data using the provided KMS key. Only symmetric keys are supported. Do not use asymmetric KMS keys to encrypt your log groups.

For more information, see [Encrypt Log Data in CloudWatch Logs Using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html).

**Topics**
+ [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md)
+ [Configuring the add-on and the Helm chart](eks-observability-addon-configure.md)
+ [Enhanced Container Insights (Classic)](container-insights-eks-classic.md)
+ [OTel Container Insights (Recommended)](container-insights-eks-otel.md)
+ [Compare Container Insights approaches](container-insights-eks-compare.md)
+ [Migration guides](container-insights-eks-migration-hub.md)
+ [Troubleshooting Container Insights on Amazon EKS](container-insights-eks-troubleshooting.md)
+ [Setting up Container Insights on Red Hat OpenShift on AWS (ROSA)](deploy-container-insights-RedHatOpenShift.md)
+ [Viewing Container Insights metrics](Container-Insights-view-metrics.md)
+ [Metrics collected by Container Insights](Container-Insights-metrics.md)