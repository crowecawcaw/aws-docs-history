

# CloudWatch pipelines
<a name="cloudwatch-pipelines"></a>

CloudWatch pipelines is a fully managed data collector that ingests, transforms, and routes telemetry data—including logs and metrics—from AWS services, third-party applications, and custom sources to CloudWatch. Built-in processors let you enrich, filter, and standardize logs into formats like OCSF—without managing infrastructure or third-party tools. For metrics, CloudWatch pipelines processes and enriches OpenTelemetry (OTel) metrics inline during ingestion into CloudWatch.

CloudWatch pipelines is fully integrated with the [logs management experience](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/data-source-discovery-management.html), enabling you to consistently process and enrich log data across related log groups through data-source and data-type specification. This unlocks use cases such as:
+ **Automatic log categorization** – Logs processed through pipelines are automatically tagged with data source information, enabling service-centric discovery and querying across your infrastructure
+ **Expanding third-party support** – Aggregate and normalize logs from a growing library of third-party sources for unified analytics and compliance

For metrics, CloudWatch pipelines enables the following use cases:
+ **Enrichment** – Add business context such as team, cost center, or environment to metrics from sources you cannot modify
+ **Cost optimization** – Strip high-cardinality attributes to reduce storage costs
+ **Standardization** – Rename metrics and attributes to enforce naming conventions

Output from pipelines is fully compatible with CloudWatch Logs features including Logs Insights queries, Logs Anomaly Detection, and Live Tail. CloudWatch pipelines works with both Standard and Infrequent Access log classes and is backwards compatible with Log Transformers.

For metrics pipelines, processed metrics are fully queryable through PromQL in Query Studio and compatible with CloudWatch Alarms and Anomaly Detection.

To get started with CloudWatch pipelines, visit [pipelines within the CloudWatch ingestion page](https://console.aws.amazon.com/cloudwatch/home?#/telemetry-config:pipelines?useCase=All) in the CloudWatch console.

**Note**  
Be aware of the following limits that apply to CloudWatch pipelines  
Logs pipelines per account: 330  
Up to 300 pipelines for collecting data from CloudWatch Logs
Up to 30 pipelines for collecting data from other sources 
Metrics pipelines per account: up to 300
Up to 20 processors per pipeline (logs and metrics)
Metrics pipelines supported ingestion path: OTLP only

## Pipeline components
<a name="pipeline-components"></a>

Each pipeline consists of the following components:
+ **Source** – Defines where data originates from (Amazon S3 buckets, CloudWatch Logs, CloudWatch Metrics (OTel), third-party integration). Each pipeline must have exactly one source. Metrics pipelines process OTel metrics on the OTLP ingestion path.
+ **Processors** (optional) – Transform, parse, and enrich telemetry data as it flows through the pipeline. Processors are applied sequentially in the order they are defined. Metrics pipelines support a distinct set of processors optimized for OTel metric attributes.
+ **Sink** – Defines the destination where processed data is sent. Supported sink types include `cloudwatch_logs` and `cloudwatch_metrics`. Each pipeline must have exactly one sink.
+ **Extensions** (optional) – Provide additional functionality such as AWS Secrets Manager integration for credential management.

Throughout the entire pipeline, your data remains protected with transport layer encryption so that your data meets security and compliance requirements.

**Note**  
Pipeline definitions are not encrypted with customer-provided keys and must never include sensitive data, such as passwords, API keys, or personally identifiable information (PII).

**Note**  
Adding processors leads to mutation of the log events and original (raw) logs are not retained.

## Pricing
<a name="pipeline-pricing"></a>

CloudWatch pipelines is included with CloudWatch Logs at no additional cost. Standard log ingestion rates based on log class (vended or custom) and storage class (Standard or Infrequent Access) still apply. Metering occurs at time of first ingestion into CloudWatch. CloudWatch Logs sources are metered before pipeline processing. Third-party and S3 bucket sources are classified as Custom logs and metered after processing. For pricing details, see [CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

For metrics pipelines, standard CloudWatch OTel metrics ingestion and storage charges apply. There is no additional charge for pipeline processing.

## Region availability
<a name="pipeline-region-availability"></a>

CloudWatch pipelines is available in the following AWS Regions:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (N. California)
+ US West (Oregon)
+ Africa (Cape Town)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Jakarta)
+ Asia Pacific (Malaysia)
+ Asia Pacific (Melbourne)
+ Asia Pacific (Mumbai)
+ Asia Pacific (New Zealand)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Taipei)
+ Asia Pacific (Thailand)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Canada West (Calgary)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Milan)
+ Europe (Paris)
+ Europe (Spain)
+ Europe (Stockholm)
+ Europe (Zurich)
+ Israel (Tel Aviv)
+ Mexico (Central)
+ South America (São Paulo)

**Note**  
Third-party data source collection is available in regions where [OpenSearch Ingestion has API endpoints](https://docs.aws.amazon.com/general/latest/gr/opensearch-service.html).

For more details, see [Amazon CloudWatch endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cw_region.html) in the *AWS General Reference*.