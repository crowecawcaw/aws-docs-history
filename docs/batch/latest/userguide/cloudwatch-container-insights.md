# AWS Batch CloudWatch Container Insights

CloudWatch Container Insights collects, aggregates, and summarizes metrics and logs from your
AWS Batch compute environments and jobs. The metrics include CPU, memory, disk, and network
utilization. You can add these metrics to CloudWatch dashboards.

CloudWatch Container Insights collects operational data as performance log events. These are
entries that use a structured JSON schema that enables high-cardinality data to be ingested and
stored at scale. From this data, CloudWatch creates higher-level aggregated metrics at the compute
environment and job level as CloudWatch metrics. For more information, see [Container Insights Structured Logs for Amazon ECS](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-reference-structured-logs-ECS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-reference-structured-logs-ECS.md") in the
_Amazon CloudWatch User Guide_.

###### Important

CloudWatch Container Insights are charged as custom metrics by CloudWatch. For more information, see
[Amazon CloudWatch Events pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

You can enable Container Insights when you create a compute environment or update an existing
compute environment. Container Insights supports three modes:

- **Enabled** – Collects cluster-level and service-level
  metrics including CPU, memory, network, and disk utilization.
- **Enhanced** – Provides all standard metrics plus
  additional per-container metrics and resource observability at the job level.
- **Disabled** – Explicitly turns off Container Insights,
  overriding any Amazon ECS account-level default.

###### Note

Container Insights is only supported for Amazon ECS-based compute environments (managed Amazon EC2,
managed Fargate, and unmanaged Amazon ECS). Amazon EKS-based compute environments are not supported.
For Amazon EKS observability, use the CloudWatch Observability add-on. For more information, see
[Setting up
the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-addon.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-setup-EKS-addon.md") in the
_Amazon CloudWatch User Guide_.

###### Topics

- [Default behavior](cloudwatch-container-insights-default-behavior.md "cloudwatch-container-insights-default-behavior.md")
- [IAM permissions for Container Insights](cloudwatch-container-insights-iam-permissions.md "cloudwatch-container-insights-iam-permissions.md")
- [Turn on Container Insights](cloudwatch-container-insights-working.md "cloudwatch-container-insights-working.md")
- [Turn off Container Insights](cloudwatch-container-insights-disable.md "cloudwatch-container-insights-disable.md")
- [Container Insights metrics](cloudwatch-container-insights-metrics.md "cloudwatch-container-insights-metrics.md")
