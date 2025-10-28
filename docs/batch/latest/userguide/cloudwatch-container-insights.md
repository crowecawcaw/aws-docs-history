# AWS Batch CloudWatch Container Insights

CloudWatch Container Insights collects, aggregates, and summarizes metrics and logs from your
AWS Batch compute environments and jobs. The metrics include CPU, memory, disk, and network
utilization. You can add these metrics to CloudWatch dashboards.

Operational data is collected as performance log events. These are
entries that use a structured JSON schema that enables high-cardinality data to be ingested and
stored at scale. From this data, CloudWatch creates higher-level aggregated metrics at the compute
environment and job level as CloudWatch metrics. For more information, see [Container Insights Structured Logs for Amazon ECS](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-reference-structured-logs-ECS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-reference-structured-logs-ECS.md") in the
_Amazon CloudWatch User Guide_.

###### Important

CloudWatch Container Insights are charged as custom metrics by CloudWatch. For more information, see
[Amazon CloudWatch Events pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")

###### Topics

- [Turn on Container Insights](cloudwatch-container-insights-working.md "cloudwatch-container-insights-working.md")
