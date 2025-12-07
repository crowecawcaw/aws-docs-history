# CloudWatch pipelines

A telemetry pipeline collects, processes, and routes data such as logs, metrics, and traces from various sources to different destinations. CloudWatch pipelines provides a
centralized way to collect data from AWS services, third-party applications, and custom sources. The pipeline processes and transforms data using a rich set
of processors, converts data into standard formats like Open Cybersecurity Schema Framework (OCSF), and routes processed data to CloudWatch Logs.

You can collect data from a wide range of sources, including AWS services, third-party
applications, and your own custom sources. This data is then processed and transformed using
processors that can standardize formats, filter unnecessary information, and enrich the data
with additional context. This allows you to convert varied data formats into standardized
schemas such as OCSF, enabling unified analysis across all your data sources.

Throughout the entire pipeline, your data remains protected with transport layer
encryption, ensuring security and compliance requirements are met.

###### Note

When configuring pipelines, remember that pipeline definitions are not encrypted and
should never include sensitive data, such as personally identifiable information
(PII).

Each pipeline consists of three main components:

1. **Source** – Defines where your data comes
   from (AWS services, third-party applications, or custom sources)
2. **Processors** – Optionally, configure how
   your data is transformed, filtered, or enriched

###### Note

Adding processors leads to mutation of the log events and original (raw) logs
are not retained. 3. **Sink** – Specify where your
processed data should be delivered
To get started with CloudWatch pipelines:

1. Sign in to the AWS Management Console
2. Navigate to CloudWatch.
3. Choose **Ingestion** from the navigation panel and then select the **Pipelines** tab.
4. Choose **Create pipeline**.

###### Note

Be aware of the following limits that apply to CloudWatch pipelines

- Maximum number of pipelines per account: 330

      + Up to 300 pipelines for collecting data from CloudWatch Logs
      + Up to 30 pipelines for collecting data from other sources

  CloudWatch pipelines is available in the following AWS
  Regions.

###### Note

Third-party data source collection is available in regions where OpenSearch Ingestion has API endpoints.

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Europe (Stockholm)
- South America (São Paulo)
  For more details, see [Amazon CloudWatch endpoints and quotas](../../../general/latest/gr/cw_region.md "../../../general/latest/gr/cw_region.md") in the
  _AWS General Reference_.

###### Topics

- [Creating pipelines](Creating-pipelines.md "Creating-pipelines.md")
- [Managing pipelines](managing-pipelines.md "managing-pipelines.md")
- [Data sources](data-sources.md "data-sources.md")
- [CloudWatch pipelines processors](pipeline-processors.md "pipeline-processors.md")
- [Sinks](pipeline-sinks.md "pipeline-sinks.md")
- [CloudWatch pipelines IAM policies and permissions](pipeline-iam-reference.md "pipeline-iam-reference.md")
- [CloudWatch pipelines extensions](pipeline-extensions.md "pipeline-extensions.md")
- [Monitoring Pipelines Using CloudWatch Metrics](pipelines-metrics.md "pipelines-metrics.md")
- [Troubleshooting](troubleshooting.md "troubleshooting.md")
