# CloudWatch pipelines

CloudWatch pipelines is a fully managed data collector that ingests, transforms, and routes log data
from AWS services, third-party applications, and custom sources to CloudWatch. Built-in
processors let you enrich, filter, and standardize logs into formats like OCSF—without
managing infrastructure or third-party tools.

CloudWatch pipelines is fully integrated with the [logs management
experience](../logs/data-source-discovery-management.md "../logs/data-source-discovery-management.md"), enabling you to consistently process and enrich log data across related
log groups via data-source and data-type specification. This unlocks use cases such as:

- **Automatic log categorization** – Logs processed
  through pipelines are automatically tagged with data source information, enabling
  service-centric discovery and querying across your infrastructure
- **Expanding third-party support** – Aggregate
  and normalize logs from a growing library of third-party sources for unified
  analytics and compliance
  Output from pipelines is fully compatible with CloudWatch Logs features including Logs Insights
  queries, Logs Anomaly Detection, and Live Tail. CloudWatch pipelines works with both Standard and
  Infrequent Access log classes and is backwards compatible with Log Transformers.

To get started with CloudWatch pipelines, visit [pipelines
within the CloudWatch ingestion page](https://console.aws.amazon.com/cloudwatch/home?#/telemetry-config:pipelines?useCase=All "https://console.aws.amazon.com/cloudwatch/home?#/telemetry-config:pipelines?useCase=All") in the CloudWatch console.

###### Note

Be aware of the following limits that apply to CloudWatch pipelines

- Maximum number of pipelines per account: 330
  - Up to 300 pipelines for collecting data from CloudWatch Logs
  - Up to 30 pipelines for collecting data from other sources

## Pipeline components

Each pipeline consists of the following components:

- **Source** – Defines where data originates
  from (Amazon S3 buckets, CloudWatch Logs, third-party integration). Each pipeline must have
  exactly one source.
- **Processors** (optional) – Transform, parse,
  and enrich log data as it flows through the pipeline. Processors are applied
  sequentially in the order they are defined.
- **Sink** – Defines the destination where
  processed log data is sent. Each pipeline must have exactly one sink.
- **Extensions** (optional) – Provide additional
  functionality such as AWS Secrets Manager integration for credential management.

Throughout the entire pipeline, your data remains protected with transport layer
encryption, ensuring security and compliance requirements are met.

###### Note

Pipeline definitions are not encrypted and should never include sensitive data,
such as personally identifiable information (PII).

###### Note

Adding processors leads to mutation of the log events and original (raw) logs
are not retained.

## Pricing

CloudWatch pipelines is included with CloudWatch Logs at no additional cost. Standard log ingestion rates
based on log class (vended or custom) and storage class (Standard or Infrequent Access)
still apply. Metering occurs at time of first ingestion into CloudWatch. CloudWatch Logs sources are
metered before pipeline processing. Third-party and S3 bucket sources are classified
as Custom logs and metered after processing. For pricing details, see [CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

## Region availability

CloudWatch pipelines is available in the following AWS Regions:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Hong Kong)
- Asia Pacific (Malaysia)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Thailand)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Europe (Spain)
- Europe (Stockholm)
- South America (São Paulo)

###### Note

Third-party data source collection is available in regions where [OpenSearch Ingestion has API endpoints](../../../general/latest/gr/opensearch-service.md "../../../general/latest/gr/opensearch-service.md").

For more details, see [Amazon CloudWatch endpoints and quotas](../../../general/latest/gr/cw_region.md "../../../general/latest/gr/cw_region.md") in the
_AWS General Reference_.

###### Topics
