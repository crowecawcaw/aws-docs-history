# S3 Storage Lens metrics and dimensions

To send S3 Storage Lens metrics to CloudWatch, you must enable the CloudWatch publishing option within
S3 Storage Lens advanced metrics. After advanced metrics are enabled, you
can use [CloudWatch
dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") to monitor S3 Storage Lens metrics alongside other application metrics
and create a unified view of your operational health. You can use dimensions to filter
your S3 Storage Lens metrics in CloudWatch by organization, account, bucket, storage class, Region,
and metrics configuration ID.

S3 Storage Lens metrics are published to CloudWatch in the account that owns the S3 Storage Lens configuration.
After you enable the CloudWatch publishing option within advanced metrics, you can access account-level and
bucket-level metrics by configuration ID, account, bucket (for bucket-level metrics only), Region, and
storage class in CloudWatch. Prefix-level metrics are not available in CloudWatch.

###### Note

S3 Storage Lens metrics are daily metrics and are published to CloudWatch once per day.
When you query S3 Storage Lens metrics in CloudWatch, the period for the query must be 1 day (86400 seconds). After your daily S3 Storage Lens metrics appear in your S3 Storage Lens dashboard in the
Amazon S3 console, it can take a few hours for these same metrics to appear in CloudWatch. When you enable
the CloudWatch publishing option for S3 Storage Lens metrics for the first time, it can take up to 24
hours for your metrics to publish to CloudWatch.

For more information about S3 Storage Lens metrics and dimensions in CloudWatch, see the
following topics.

###### Topics

- [Metrics](#storage-lens-cloudwatch-metrics "#storage-lens-cloudwatch-metrics")
- [Dimensions](#storage-lens-cloudwatch-dimensions "#storage-lens-cloudwatch-dimensions")

## Metrics

S3 Storage Lens metrics are available as metrics within CloudWatch. S3 Storage Lens metrics are
published to the `AWS/S3/Storage-Lens` namespace. This namespace is only
for S3 Storage Lens metrics. Amazon S3 bucket, request, and replication metrics are published to
the `AWS/S3` namespace.

S3 Storage Lens metrics are published to CloudWatch in the account that owns the S3 Storage Lens configuration.
After you enable the CloudWatch publishing option within advanced metrics, you can access account-level and
bucket-level metrics by configuration ID, account, bucket (for bucket-level metrics only), Region, and
storage class in CloudWatch. Prefix-level metrics are not available in CloudWatch.

In S3 Storage Lens, metrics are aggregated and stored only in the designated home
Region. S3 Storage Lens metrics are also published to CloudWatch in the home Region
that you specify in the S3 Storage Lens configuration.

For a complete list of S3 Storage Lens metrics, including a list of those metrics
available in CloudWatch, see [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").

###### Note

The valid statistic for S3 Storage Lens metrics in CloudWatch is Average.
For more information about statistics in CloudWatch, see [CloudWatch statistics definitions](../../../AmazonCloudWatch/latest/monitoring/Statistics-definitions.md "../../../AmazonCloudWatch/latest/monitoring/Statistics-definitions.md") in the _Amazon CloudWatch User Guide_.

### Granularity of S3 Storage Lens metrics in CloudWatch

S3 Storage Lens offers metrics at organization, account, bucket, and prefix
granularity. S3 Storage Lens publishes organization, account, and bucket-level
S3 Storage Lens metrics to CloudWatch. Prefix-level S3 Storage Lens metrics are not
available in CloudWatch.

For more information about the granularity of S3 Storage Lens metrics available
in CloudWatch, see the following list:

- **Organization** – Metrics
  aggregated across the member accounts in your organization. S3 Storage Lens
  publishes metrics for member accounts to CloudWatch in the management account.
  - **Organization and account** – Metrics
    for the member accounts in your organization.
  - **Organization and bucket**
    – Metrics for Amazon S3 buckets in the member accounts of
    your organization.

- **Account** (Non-organization level)
  – Metrics aggregated across the buckets in your account.
- **Bucket** (Non-organization level)
  – Metrics for a specific bucket. In CloudWatch, S3 Storage Lens publishes
  these metrics to the AWS account that created the S3 Storage Lens
  configuration. S3 Storage Lens publishes these metrics only for
  non-organization configurations.

## Dimensions

When S3 Storage Lens sends data to CloudWatch, dimensions are attached to each metric.
Dimensions are categories that describe the characteristics of metrics. You can use
dimensions to filter the results that CloudWatch returns.

For example, all S3 Storage Lens metrics in CloudWatch have the
`configuration_id` dimension. You can use this dimension to
differentiate between metrics associated with a specific S3 Storage Lens configuration.
The `organization_id` identifies organization-level metrics. For more
information about dimensions in CloudWatch, see [Dimensions](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension") in the _CloudWatch User
Guide_.

Different dimensions are available for S3 Storage Lens metrics depending on the
granularity of the metrics. For example, you can use the
`organization_id` dimension to filter organization-level metrics by
the AWS Organizations ID. However, you can't use this dimension for bucket and account-level
metrics. For more information, see [Filtering metrics using dimensions](storage-lens-cloudwatch-monitoring-cloudwatch.md#storage-lens-cloudwatch-monitoring-cloudwatch-dimensions "storage-lens-cloudwatch-monitoring-cloudwatch.md#storage-lens-cloudwatch-monitoring-cloudwatch-dimensions").

To see which dimensions are available for your S3 Storage Lens configuration, see the
following
table.

| **Dimension**        | **Description**                                                                                | **Bucket** | **Account** | **Organization** | **Organization and bucket** | **Organization and account** |
| -------------------- | ---------------------------------------------------------------------------------------------- | ---------- | ----------- | ---------------- | --------------------------- | ---------------------------- |
| `configuration_id`   | The dashboard name for the S3 Storage Lens configuration reported in the<br>metrics            |            |             |                  |                             |                              |
| `metrics_version`    | The version of the S3 Storage Lens metrics. The metrics version has a fixed value<br>of `1.0`. |            |             |                  |                             |                              |
| `organization_id`    | The AWS Organizations ID for the metrics                                                       |            |             |                  |                             |                              |
| `aws_account_number` | The AWS account that's associated with the metrics                                             |            |             |                  |                             |                              |
| `aws_region`         | The AWS Region for the metrics                                                                 |            |             |                  |                             |                              |
| `bucket_name`        | The name of the S3 bucket that's reported in the metrics                                       |            |             |                  |                             |                              |
| `storage_class`      | The storage class for the bucket that's reported in the<br>metrics                             |            |             |                  |                             |                              |
| `record_type`        | The granularity of the metrics:<br>ORGANIZATION,<br>ACCOUNT, BUCKET                            | BUCKET     | ACCOUNT     | BUCKET           | ACCOUNT                     | ORGANIZATION                 |
