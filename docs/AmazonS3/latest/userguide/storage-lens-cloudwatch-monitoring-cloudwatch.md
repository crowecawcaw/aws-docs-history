# Working with S3 Storage Lens metrics in CloudWatch

You can publish S3 Storage Lens metrics to Amazon CloudWatch to create a unified view of your
operational health in [CloudWatch
dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md"). You can also use CloudWatch features, such as alarms and triggered
actions, metric math, and anomaly detection, to monitor and take action on S3 Storage Lens
metrics. In addition, CloudWatch API operations enable applications, including third-party
providers, to access your S3 Storage Lens metrics. For more information about CloudWatch features,
see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md").

You can enable the CloudWatch publishing option for new or existing dashboard configurations
by using the Amazon S3 console, Amazon S3 REST APIs, AWS CLI, and AWS SDKs. The CloudWatch publishing
option is available for dashboards that are upgraded to S3 Storage Lens advanced metrics and
recommendations. For S3 Storage Lens advanced metrics and recommendations pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"). No additional CloudWatch metrics
publishing charges apply; however, other CloudWatch charges, such as dashboards, alarms, and
API calls, do apply. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

S3 Storage Lens metrics are published to CloudWatch in the account that owns the S3 Storage Lens configuration.
After you enable the CloudWatch publishing option within advanced metrics and recommendations,
you can access organization, account, and bucket-level metrics in CloudWatch.
Prefix-level metrics are not available in CloudWatch.

###### Note

S3 Storage Lens metrics are daily metrics and are published to CloudWatch once per day.
When you query S3 Storage Lens metrics in CloudWatch, the period for the query must be 1 day (86400 seconds). After your daily S3 Storage Lens metrics appear in your S3 Storage Lens dashboard in the
Amazon S3 console, it can take a few hours for these same metrics to appear in CloudWatch. When you enable
the CloudWatch publishing option for S3 Storage Lens metrics for the first time, it can take up to 24
hours for your metrics to publish to CloudWatch.

Currently, S3 Storage Lens metrics cannot be consumed through CloudWatch streams.

For more information about working with S3 Storage Lens metrics in CloudWatch, see the
following topics.

###### Topics

- [Working with CloudWatch dashboards](#storage-lens-cloudwatch-monitoring-cloudwatch-dashboards "#storage-lens-cloudwatch-monitoring-cloudwatch-dashboards")
- [Setting alarms, triggering actions, and using anomaly detection](#storage-lens-cloudwatch-monitoring-cloudwatch-alarms "#storage-lens-cloudwatch-monitoring-cloudwatch-alarms")
- [Filtering metrics using dimensions](#storage-lens-cloudwatch-monitoring-cloudwatch-dimensions "#storage-lens-cloudwatch-monitoring-cloudwatch-dimensions")
- [Calculating new metrics with metric math](#storage-lens-cloudwatch-monitoring-cloudwatch-metric-math "#storage-lens-cloudwatch-monitoring-cloudwatch-metric-math")
- [Using search expressions in graphs](#storage-lens-cloudwatch-monitoring-cloudwatch-search-expressions "#storage-lens-cloudwatch-monitoring-cloudwatch-search-expressions")

## Working with CloudWatch dashboards

You can use CloudWatch dashboards to monitor S3 Storage Lens metrics alongside other
application metrics and create a unified view of your operational health. Dashboards
are customizable home pages in the CloudWatch console that you can use to monitor
your resources in a single view.

CloudWatch has broad permissions control that doesn't support limiting access to a
specific set of metrics or dimensions. Users in your account or organization who
have access to CloudWatch will have access to metrics for all S3 Storage Lens configurations
where the CloudWatch support option is enabled. You can't manage permissions for specific
dashboards as you can in S3 Storage Lens. For more information about CloudWatch permissions, see
[Managing access permissions to your CloudWatch resources](../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md "../../../AmazonCloudWatch/latest/monitoring/iam-access-control-overview-cw.md") in the _Amazon CloudWatch User Guide_.

For more information about using CloudWatch dashboards and configuring
permissions, see [Using Amazon CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") and [Sharing CloudWatch dashboards](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.md") in the _Amazon CloudWatch User Guide_.

## Setting alarms, triggering actions, and using anomaly detection

You can configure CloudWatch alarms that watch S3 Storage Lens metrics in CloudWatch and take action
when a threshold is breached. For example, you can configure an alarm that sends an
Amazon SNS notification when the **Incomplete Multipart Upload Bytes**
metric exceeds 1 GB for three consecutive days.

You can also enable anomaly detection to continuously analyze your S3 Storage Lens
metrics, determine normal baselines, and surface anomalies. You can create an
anomaly detection alarm based on a metric's expected value. For example, you can
monitor anomalies for the **Object Lock Enabled Bytes** metric to
detect unauthorized removal of Object Lock settings.

For more information and examples, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") and [Creating an alarm from a metric on a graph](../../../AmazonCloudWatch/latest/monitoring/create_alarm_metric_graph.md "../../../AmazonCloudWatch/latest/monitoring/create_alarm_metric_graph.md") in the _Amazon CloudWatch User Guide_.

## Filtering metrics using dimensions

You can use dimensions to filter S3 Storage Lens metrics in the CloudWatch console. For
example, you can filter by `configuration_id`,
`aws_account_number`, `aws_region`,
`bucket_name`, and more.

S3 Storage Lens supports multiple dashboard configurations per account. This means that
different configurations can include the same bucket. When these metrics are
published to CloudWatch, the bucket will have duplicate metrics within CloudWatch. To view
metrics only for a specific S3 Storage Lens configuration in CloudWatch, you can use the
`configuration_id` dimension. When you filter by
`configuration_id`, you see only the metrics that are associated with
the configuration that you identify.

For more information about filtering by configuration ID, see [Searching for available metrics](../../../AmazonCloudWatch/latest/monitoring/finding_metrics_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/finding_metrics_with_cloudwatch.md") in the _Amazon CloudWatch User Guide_.

## Calculating new metrics with metric math

You can use metric math to query multiple S3 Storage Lens metrics and use math
expressions to create new time series based on these metrics. For example, you can
create a new metric for unencrypted objects by subtracting Encrypted Objects from
Object Count. You can also create a metric to get the average object size by
dividing `StorageBytes` by `ObjectCount` or the number bytes
accessed on one day by dividing `BytesDownloaded` by
`StorageBytes`.

For more information, see [Using metric
math](../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md "../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md") in the _Amazon CloudWatch User Guide_.

## Using search expressions in graphs

With S3 Storage Lens metrics, you can create a search expression. For example, you can
create a search expression for all metrics that are named **IncompleteMultipartUploadStorageBytes** and add `SUM` to
the expression. With this search expression, you can see your total incomplete
multipart upload bytes across all dimensions of your storage in a single
metric.

This example shows the syntax that you would use to create a search expression for
all metrics named **IncompleteMultipartUploadStorageBytes**.

```
SUM(SEARCH('{AWS/S3/Storage-Lens,aws_account_number,aws_region,configuration_id,metrics_version,record_type,storage_class} MetricName="IncompleteMultipartUploadStorageBytes"', 'Average',86400))
```

For more information about this syntax, see [CloudWatch
search expression syntax](../../../AmazonCloudWatch/latest/monitoring/search-expression-syntax.md "../../../AmazonCloudWatch/latest/monitoring/search-expression-syntax.md") in the _Amazon CloudWatch User Guide_. To create a CloudWatch graph with a search expression,
see [Creating
a CloudWatch graph with a search expression](../../../AmazonCloudWatch/latest/monitoring/create-search-expression.md "../../../AmazonCloudWatch/latest/monitoring/create-search-expression.md")in the _Amazon CloudWatch User Guide_.
