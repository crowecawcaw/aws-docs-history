# Monitoring your storage activity and usage with

Amazon S3 Storage Lens

Amazon S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide
visibility into object storage and activity. S3 Storage Lens also analyzes metrics to deliver
contextual recommendations that you can use to optimize storage costs and apply best practices
for protecting your data.

You can use S3 Storage Lens metrics to generate summary insights. For example, you can find out how
much storage you have across your entire organization or which are the fastest-growing buckets
and prefixes. You can also use S3 Storage Lens metrics to identify cost optimization opportunities,
implement data protection and access management best practices, and improve the performance of
application workloads. For example, you can identify buckets that don't have S3 Lifecycle rules
set up to expire incomplete multipart uploads that are more than 7 days old. You can also
identify buckets that aren't following data protection best practices, such as using
S3 Replication or S3 Versioning.

S3 Storage Lens aggregates your metrics and displays the information in the **Account snapshot** section on the
Amazon S3 console **Buckets** page. S3 Storage Lens also provides an interactive dashboard that you can use to visualize insights and
trends, flag outliers, and receive recommendations for optimizing storage costs and applying data protection best practices. Your dashboard has
drill-down options to generate and visualize insights at the organization, account, AWS Region, storage class, bucket, prefix, or
Storage Lens group level. You can also send a daily metrics report in CSV or Parquet format to a general purpose S3 bucket or export
the metrics directly to an AWS-managed S3 table bucket.

![The Snapshot for date section in the S3 Storage Lens dashboard.](images/storage-lens-dashboard.png)

## S3 Storage Lens metrics and features

S3 Storage Lens provides an interactive _default dashboard_ that is updated
daily. S3 Storage Lens preconfigures this dashboard to visualize the summarized insights and trends
for your entire account and updates them daily in the S3 console. Metrics from this dashboard
are also summarized in your account snapshot on the **Buckets** page. For
more information, see [Default dashboard](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_default_dashboard "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_default_dashboard").

To create other dashboards and scope them by AWS Regions, S3 buckets, or accounts (for
AWS Organizations), you create an S3 Storage Lens dashboard configuration. You can create and manage S3 Storage Lens
dashboard configurations by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3
REST API. When you create or edit an S3 Storage Lens dashboard, you define your dashboard scope and
metrics selection.

S3 Storage Lens offers free tier metrics and advanced tier metrics, which you can upgrade to for
an additional charge. With the advanced tier, you can access additional metrics and features
for gaining insight into your storage. These features include advanced metric categories,
prefix aggregation, contextual recommendations, expanded prefixes metrics reports, and
Amazon CloudWatch publishing. Prefix aggregation and contextual recommendations are available only in
the Amazon S3 console. For information about S3 Storage Lens pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

###### Metrics categories

Within the free and advanced tiers, metrics are organized into categories that align
with key use cases, such as cost optimization and data protection. Free metrics include
summary, cost optimization, data protection, access management, performance, and event
metrics. When you upgrade to the advanced tier, you can enable advanced cost optimization
and data protection metrics. You can use these advanced metrics to further reduce your S3
storage costs and improve your data protection stance. You can also enable activity metrics
and detailed status-code metrics to improve the performance of application workloads that
are accessing your S3 buckets. For more information about the free and advanced metrics
categories, see [Metrics selection](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection").

You can assess your storage based on S3 best practices, such as analyzing the percentage
of your buckets that have encryption or S3 Object Lock or S3 Versioning enabled. You can also
identify potential cost-savings opportunities. For example, you can use S3 Lifecycle rule count
metrics to identify buckets that are missing lifecycle expiration or transition rules. You can
also analyze your request activity per bucket to find buckets where objects could be
transitioned to a lower-cost storage class. For more information, see [Amazon S3 Storage Lens metrics use cases](storage-lens-use-cases.md "storage-lens-use-cases.md").

Metrics export

###### Default metrics report

The default metrics report in S3 Storage Lens includes free metrics and advanced tier metrics
covering object storage usage and activity trends across your AWS accounts. The report
includes prefix aggregation for prefixes whose objects comprise at least 1% of the total
data stored in the bucket, and supports up to 10 levels of prefix depth. The report can be
exported daily in CSV or Parquet format to an S3 general purpose bucket. The
report can also be sent to an AWS-managed S3 table bucket (with name `aws-s3`)
making it easy to query using AWS analytics services or third-party tools.

With the default metrics report, you can identify cost optimization opportunities like
buckets without S3 Lifecycle rules for incomplete multipart uploads and buckets not following
data protection best practices such as S3 Replication or S3 Versioning. The default metrics
report also provides contextual recommendations for optimizing storage costs and applying data
protection best practices, at no additional charge beyond standard S3 storage costs.

###### Expanded prefixes metrics report

The Storage Lens expanded prefixes metrics report provides comprehensive prefix-level
analytics across your entire S3 storage data, expanding coverage to support billions of
prefixes in your bucket. This report delivers metrics for all prefixes in your buckets,
including storage usage, bytes transferred, request counts by status code, and data
protection compliance metrics, which you can export daily in CSV or Parquet
format to S3 general purpose bucket. You can also export the metrics directly to the
`aws-s3` AWS-managed S3 table bucket.

###### Note

The report processes metrics for prefixes up to 50 levels deep and excludes prefix-level
metrics for any bucket where the prefix and storage class combinations exceed twice the
object count.

With the expanded prefixes metrics report, you can identify performance optimization
opportunities, such as high error rates, small objects, or sub-optimal request patterns,
across billions of prefixes in your bucket. Unlike the default metrics report, the expanded
prefixes metrics report delivers metrics for granular prefixes in your bucket. For example,
you can identify prefixes with large numbers of objects of size less than 128KB to quickly
isolate such datasets for compaction that will improve application performance. This report is
available in all AWS Regions as an opt-in feature in the Storage Lens advanced tier
dashboard configuration.

Metrics publishing

###### Amazon CloudWatch publishing

You can publish S3 Storage Lens usage and activity metrics to Amazon CloudWatch to create a unified view
of your operational health in CloudWatch [dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").
You can also use CloudWatch features, such as alarms and triggered actions, metric math, and
anomaly detection, to monitor and take action on S3 Storage Lens metrics. In addition, CloudWatch API
operations enable applications, including third-party providers, to access your S3 Storage Lens
metrics. The CloudWatch publishing option is available for dashboards that are upgraded to the
S3 Storage Lens advanced tier. For more information about support for S3 Storage Lens metrics in CloudWatch, see
[Monitor S3 Storage Lens metrics in
CloudWatch](storage_lens_view_metrics_cloudwatch.md "storage_lens_view_metrics_cloudwatch.md").

For more information about using S3 Storage Lens, see the following topics.

###### Topics

- [Understanding
  Amazon S3 Storage Lens](storage_lens_basics_metrics_recommendations.md "storage_lens_basics_metrics_recommendations.md")
- [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md")
- [Setting Amazon S3 Storage Lens permissions](storage_lens_iam_permissions.md "storage_lens_iam_permissions.md")
- [Table naming for S3 Storage Lens export to S3 Tables](storage_lens_s3_tables_naming.md "storage_lens_s3_tables_naming.md")
- [Working with Amazon S3 Storage Lens by using the console and API](S3LensExamples.md "S3LensExamples.md")
- [Viewing metrics with Amazon S3 Storage Lens](storage_lens_view_metrics.md "storage_lens_view_metrics.md")
- [Using Amazon S3 Storage Lens with AWS Organizations](storage_lens_with_organizations.md "storage_lens_with_organizations.md")
- [Working with S3 Storage Lens groups to filter and aggregate metrics](storage-lens-groups-overview.md "storage-lens-groups-overview.md")
