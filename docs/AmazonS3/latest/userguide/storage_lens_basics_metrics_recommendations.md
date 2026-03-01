# Understanding Amazon S3 Storage Lens

###### Important

Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3. Starting January 5, 2023, all new object uploads to Amazon S3 are automatically encrypted at no additional cost and with no impact on performance. The automatic encryption status for S3 bucket default encryption configuration and for new object uploads is available in CloudTrail logs, S3 Inventory, S3 Storage Lens, the Amazon S3 console, and as an additional Amazon S3 API response header in the AWS CLI and AWS SDKs. For more information, see [Default encryption FAQ](default-encryption-faq.md "default-encryption-faq.md").

Amazon S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide
visibility into object-storage usage and activity. You can use S3 Storage Lens metrics to generate
summary insights, such as finding out how much storage you have across your entire organization
or which are the fastest-growing buckets and prefixes. You can also use S3 Storage Lens metrics to
identify cost-optimization opportunities, implement data-protection and security best practices,
and improve the performance of application workloads. For example, you can identify buckets that
don't have S3 Lifecycle rules to expire incomplete multipart uploads that are more than 7 days
old. You can also identify buckets that aren't following data-protection best practices, such as using
S3 Replication or S3 Versioning. S3 Storage Lens also analyzes metrics to deliver contextual
recommendations that you can use to optimize storage costs and apply best practices for
protecting your data.

S3 Storage Lens aggregates your metrics and displays the information in the **Account snapshot** section on the
Amazon S3 console **Buckets** page. S3 Storage Lens also provides an interactive dashboard that you can use to visualize insights and
trends, flag outliers, and receive recommendations for optimizing storage costs and applying data protection best practices. Your dashboard has
drill-down options to generate and visualize insights at the organization, account, AWS Region, storage class, bucket, prefix, or
Storage Lens group level. You can also send a daily metrics report in CSV or Parquet format to a general purpose S3 bucket or export
the metrics directly to an AWS-managed S3 table bucket. You can create and manage S3 Storage Lens dashboards by using the Amazon S3 console,
AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3 REST API.

## S3 Storage Lens concepts and terminology

This section contains the terminology and concepts that are essential for successfully
understanding and using Amazon S3 Storage Lens.

###### Topics

- [Dashboard configuration](#storage_lens_basics_configuration "#storage_lens_basics_configuration")
- [Default dashboard](#storage_lens_basics_default_dashboard "#storage_lens_basics_default_dashboard")
- [Dashboards](#storage_lens_basics_dashboards "#storage_lens_basics_dashboards")
- [Account snapshot](#storage_lens_basics_account_snapshot "#storage_lens_basics_account_snapshot")
- [Metrics export](#storage_lens_basics_metrics_export "#storage_lens_basics_metrics_export")
- [Metrics export destinations](#storage_lens_basics_metrics_export_destinations "#storage_lens_basics_metrics_export_destinations")
- [Home Region](#storage_lens_basics_home_region "#storage_lens_basics_home_region")
- [Retention period](#storage_lens_basics_data_queries "#storage_lens_basics_data_queries")
- [Metrics categories](#storage_lens_basics_metrics_types "#storage_lens_basics_metrics_types")
- [Recommendations](#storage_lens_basics_recommendations "#storage_lens_basics_recommendations")
- [Metrics selection](#storage_lens_basics_metrics_selection "#storage_lens_basics_metrics_selection")
- [Prefix delimiter](#storage_lens_basics_prefix_delimiter "#storage_lens_basics_prefix_delimiter")
- [S3 Storage Lens and AWS Organizations](#storage_lens_basics_organizations "#storage_lens_basics_organizations")

### Dashboard configuration

S3 Storage Lens requires a dashboard configuration that contains the properties required to
aggregate metrics on your behalf for a single dashboard or export. When you create a
configuration, you choose the dashboard name and the home Region, which you can't change
after you create the dashboard. You can optionally add tags and configure a metrics export
in CSV or Parquet format.

In the dashboard configuration, you also define the dashboard scope and the metrics
selection. The scope can include all the storage for your organization account or sections
that are filtered by Region, bucket, and account. When you configure the metrics
selection, you choose between free tier metrics and advanced tier metrics, which you can
upgrade to for an additional charge. With the advanced tier, you can access additional
metrics and features. These features include advanced metric categories, prefix-level
aggregation, contextual recommendations, and Amazon CloudWatch publishing. For information about
S3 Storage Lens pricing, see [Amazon S3
pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

### Default dashboard

The S3 Storage Lens default dashboard on the console is named
**default-account-dashboard**. S3 preconfigures this dashboard to
visualize the summarized insights and trends for your entire account and updates them
daily in the S3 console. You can't modify the configuration scope of the default
dashboard, but you can upgrade the metrics selection from free tier metrics to advanced
tier metrics. You can configure the optional metrics export or even disable the dashboard.
However, you can't delete the default dashboard.

###### Note

If you disable your default dashboard, it's no longer updated. You'll no longer
receive any new daily metrics in your S3 Storage Lens dashboard, your metrics export, or the
account snapshot on the S3 **Buckets** page. If your dashboard uses
advanced metrics, you'll no longer be charged. You can still see historic data in the
dashboard until the 14-day period for data queries expires. This period is 15 months if
you've enabled advanced metrics. To access historic data, you can re-enable the
dashboard within the expiration period.

### Dashboards

You can create additional S3 Storage Lens dashboards and scope them by AWS Regions, S3
buckets, or accounts (for AWS Organizations). When you create or edit a S3 Storage Lens dashboard, you
define your dashboard scope and metrics selection. S3 Storage Lens offers free tier metrics and
advanced tier metrics, which you can upgrade to for an additional charge. With advanced
metrics, you can access additional metrics and features for gaining insight into your
storage. These include advanced metric categories, prefix-level aggregation, contextual
recommendations, and Amazon CloudWatch publishing. For information about S3 Storage Lens pricing, see
[Amazon S3 pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

You can also disable or delete dashboards. If you disable a dashboard, it's no longer
updated, and you will no longer receive any new daily metrics. You can still see historic
data until the 14-day expiration period. If you enabled advanced metrics for that
dashboard, this period is 15 months. To access historic data, you can re-enable the
dashboard within the expiration period.

If you delete your dashboard, you lose all your dashboard configuration settings. You
will no longer receive any new daily metrics, and you also lose access to the historical
data associated with that dashboard. If you want to access the historic data for a deleted
dashboard, you must create another dashboard with the same name in the same home
Region.

###### Note

- You can use S3 Storage Lens to create up to 50 dashboards per home Region.
- Organization-level dashboards can be limited only to a Regional scope.

### Account snapshot

The S3 Storage Lens **Account snapshot** summarizes metrics from your
default dashboard and displays your total storage, object count, and average object size
on the S3 console **Buckets** page. This account snapshot gives you quick
access to insights about your storage without having to leave the
**Buckets** page. The account snapshot also provides one-click access
to your interactive S3 Storage Lens dashboard.

You can use your dashboard to visualize insights and trends, flag outliers, and
receive recommendations for optimizing storage costs and applying data protection best
practices. Your dashboard has drill-down options to generate insights at the organization,
account, bucket, object, or prefix level. You can also send a once-daily metrics export to
an S3 bucket in CSV or Parquet format.

You can't modify the dashboard scope of the **default-account
dashboard** because it's linked to the **Account snapshot**.
However, you can upgrade the metrics selection in your
**default-account-dashboard** from free metrics to paid advanced
metrics. After upgrading, you can then display all requests, bytes uploaded, and bytes
downloaded in the S3 Storage Lens **Account snapshot**.

###### Note

If you disable your default dashboard, your **Account snapshot** is
no longer updated. To continue displaying metrics in the **Account
snapshot**, you can re-enable the
**default-account-dashboard**.

### Metrics export

An S3 Storage Lens metrics export is a file that contains all the metrics identified in your
S3 Storage Lens configuration. This information is generated daily in CSV or
Parquet format and is sent to a general purpose S3 bucket. You can also
export the metrics directly to the `aws-s3` AWS-managed S3 table bucket
making it easy to query using AWS analytics services or third-party tools. You can use
the metrics export for further analysis by using the metrics tool of your choice. The
bucket specified for your metrics export must be in the same Region as your S3 Storage Lens
configuration. You can generate an S3 Storage Lens metrics export from the S3 console by editing
your dashboard configuration. You can also configure a metrics export by using the AWS CLI
and AWS SDKs.

There are two types of metric exports available in Storage Lens:

- Default metrics report – The default metrics
  report in S3 Storage Lens includes free metrics and activity trends across your
  AWS account and aggregates usage metrics for top prefixes.
- Expanded prefixes metrics report – The
  Storage Lens expanded prefixes metrics report provides granular storage and activity
  metrics (such as storage usage, bytes transferred, and request counts by status code)
  at the prefix level for every prefix in your bucket. This report is available as an
  opt-in feature in all AWS Regions, through the advanced pricing tier in your Storage
  Lens dashboard configuration. For information about S3 Storage Lens feature pricing, see
  [Amazon S3 pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

###### Note

Storage Lens only generates metrics for [S3 general
purpose buckets](UsingBucket.md "UsingBucket.md").

### Metrics export destinations

When exporting Storage Lens metrics data, you can choose both an S3 general purpose
bucket or an S3 table bucket as your destination. General purpose buckets provide broad
compatibility with existing tools and applications, offering flexibility to process data
within your account, using your preferred analytics services. This option supports
standard S3 access patterns and integrations for data analysis within individual buckets
in your Region. In contrast, S3 table bucket lets you run immediate queries across
multiple accounts and regions, create custom dashboards with Amazon Quick, and join data with
other AWS services or third-party tools, without the need for additional processing
infrastructure. For example, you can combine Storage Lens metrics with S3 Metadata to
analyze object activity patterns across your organization.

#### S3 general purpose bucket

Exporting Storage Lens metrics to an S3 general purpose bucket offers flexibility
and continuity for storing your Storage Lens data. You can maintain existing workflows
and operational consistency by continuing to use your current infrastructure and
existing extract, transform, and load (ETL) processes, analytics tools, or automated
workflows. General purpose buckets also work with the full range of AWS services and
third-party tools that support standard S3 APIs. This gives you maximum flexibility in
how you process, analyze, or visualize your Storage Lens insights. Additionally, you can
implement S3 lifecycle policies to automatically manage data retention, transitioning
older metrics to lower-cost storage classes or deleting them after specified periods to
optimize costs. Therefore, if operational continuity and workflow flexibility are your
priorities for Storage Lens implementation, then consider choosing an S3 general purpose
bucket for exporting your Storage Lens data. For more information about S3 general
purpose buckets pricing, see [Amazon S3
pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

#### S3 table bucket

When exporting Storage Lens metrics to S3 table bucket, you can easily analyze your
storage usage and activity metrics without building data pipelines. Your metrics are
organized in S3 Tables that are created in an AWS-managed S3 table bucket called
`aws-s3` for optimal query performance, with customizable retention periods
and encryption settings to meet your data management needs. With your metrics in
S3 Tables, you can run queries across multiple accounts and Regions using SQL tools and
AWS analytics services (like Amazon Athena, Amazon Quick, Amazon EMR, and Amazon Redshift) to create custom
dashboards and generate deeper insights. For example, you can join S3 Storage Lens metrics with
S3 Metadata to identify objects in prefixes that aren't showing any recent activity. Any
data stored in an S3 table bucket incurs S3 Tables costs. For more information about
S3 Tables pricing, see [Amazon S3
pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

###### Permissions for metrics export to S3 Tables

To create and work with S3 Storage Lens tables and table buckets, you must have certain
`s3tables` permissions. At a minimum, to configure S3 Storage Lens to
S3 Tables, you must have the following `s3tables` permissions:

- `s3tables:CreateTableBucket` – This permission allows you to
  create an AWS-managed table bucket. All S3 Storage Lens metrics in your account are
  stored in a single AWS-managed table bucket named `aws-s3`.
- `s3tables:PutTableBucketPolicy` – S3 Storage Lens uses this
  permission to set a table bucket policy that allows
  `systemtables.s3.amazonaws.com` access to the bucket so that logs can
  be delivered.

###### Important

If you remove permissions for the service principal
`systemtables.s3.amazonaws.com`, S3 Storage Lens will not be able to update the
S3 tables with data based on your configuration. We recommend adding other access
control policies in addition to the policy already provided, instead of editing the
canned policy that is added when your table bucket is set up.

###### Note

A separate S3 table for each type of metric export is created for each Storage
Lens configuration. If you have multiple Storage Lens configurations in the Region,
separate tables are created for additional configurations. For example, there are
three types of tables available for your S3 table bucket.

### Home Region

The home Region is the AWS Region where all S3 Storage Lens metrics for a given dashboard
configuration are stored. You must choose a home Region when you create your S3 Storage Lens
dashboard configuration. After you choose a home Region, you can't change it. Also, if
you're creating a Storage Lens group, we recommend that you choose the same home Region as
your Storage Lens dashboard.

###### Note

You can choose one of the following Regions as your home Region:

- US East (N. Virginia) – `us-east-1`
- US East (Ohio) – `us-east-2`
- US West (N. California) – `us-west-1`
- US West (Oregon) – `us-west-2`
- Asia Pacific (Mumbai) – `ap-south-1`
- Asia Pacific (Seoul) – `ap-northeast-2`
- Asia Pacific (Singapore) – `ap-southeast-1`
- Asia Pacific (Sydney) – `ap-southeast-2`
- Asia Pacific (Tokyo) – `ap-northeast-1`
- Canada (Central) – `ca-central-1`
- China (Beijing) – `cn-north-1`
- China (Ningxia) – `cn-northwest-1`
- Europe (Frankfurt) – `eu-central-1`
- Europe (Ireland) – `eu-west-1`
- Europe (London) – `eu-west-2`
- Europe (Paris) – `eu-west-3`
- Europe (Stockholm) – `eu-north-1`
- South America (São Paulo) – `sa-east-1`

### Retention period

S3 Storage Lens metrics are retained so that you can see historical trends and compare
differences in your storage and activity over time. You can use Amazon S3 Storage Lens metrics for
queries so that you can see historical trends and compare differences in your storage
usage and activity over time.

All S3 Storage Lens metrics are retained for a period of 15 months. However, metrics are only
available for queries for a specific duration, which depends on your [metrics selection](#storage_lens_basics_metrics_selection "#storage_lens_basics_metrics_selection"). This duration
can't be modified. Free metrics are available for queries for a 14-day period, and
advanced metrics are available for queries for a 15-month period.

### Metrics categories

Within the free and advanced tiers, S3 Storage Lens metrics are organized into categories
that align with key use cases, such as cost optimization and data protection. Free metrics
include summary, cost optimization, data protection, access management, performance, and
event metrics. When you upgrade to advanced metrics, you can enable additional cost
optimization and data protection metrics that you can use to further reduce your S3
storage costs and ensure your data is protected. You can also enable activity metrics and
detailed status-code metrics that you can use to improve the performance of application
workflows.

The following list shows all of the free and advanced metric categories. For a
complete list of the individual metrics included in each category, see [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").

###### Summary metrics

Summary metrics provide general insights about your S3 storage, including your total
storage bytes and object count.

###### Cost optimization metrics

Cost optimization metrics provide insights that you can use to manage and optimize
your storage costs. For example, you can identify buckets that have incomplete multipart
uploads that are more than 7-days old.

With advanced metrics, you can enable advanced cost optimization metrics. These
metrics include S3 Lifecycle rule count metrics that you can use to get per-bucket
expiration and transition S3 Lifecycle rule counts.

###### Data-protection metrics

Data-protection metrics provide insights for data protection features, such as
encryption and S3 Versioning. You can use these metrics to identify buckets that are not
following data protection best practices. For example, you can identify buckets that are
not using default encryption with AWS Key Management Service keys (SSE-KMS) or S3 Versioning.

With advanced metrics, you can enable advanced data protection metrics. These metrics
include per-bucket replication rule count metrics.

###### Access management metrics

Access management metrics provide insights for S3 Object Ownership. You can use
these metrics to see which Object Ownership settings your buckets use.

###### Event metrics

Event metrics provide insights for S3 Event Notifications. With event metrics, you
can see which buckets have S3 Event Notifications configured.

###### Performance metrics

Performance metrics provide insights for S3 Transfer Acceleration. With performance
metrics, you can see which buckets have Transfer Acceleration enabled.

###### Activity metrics (advanced)

If you upgrade your dashboard to the **Advanced tier**, you can
enable activity metrics. Activity metrics provide details about how your storage is
requested (for example, all requests, Get requests, Put requests), bytes uploaded or
downloaded, and errors.

Prefix-level activity metrics can be used to help you determine which prefixes are
being used infrequently, so that you can [transition to a more optimal
storage class using S3 Lifecycle](lifecycle-transition-general-considerations.md "lifecycle-transition-general-considerations.md").

###### Detailed status code metrics (advanced)

If you upgrade your dashboard to the **Advanced tier**, you can
enable detailed status code metrics. Detailed status code metrics provide insights for
HTTP status codes, such as 403 Forbidden and 503 Service Unavailable, that you can use
to troubleshoot access or performance issues. For example, you can look at the **403 Forbidden error count** metric to identify workloads that are
accessing buckets without the correct permissions applied.

Prefix-level detailed status code metrics can be used to gain a better understanding
of the HTTP status code occurrences by prefix. For example, 503 error count metrics enable
you to identify prefixes receiving throttling requests during data ingestion.

###### Advanced cost optimization metrics

Advanced cost optimization metrics provide detailed insights into your S3 lifecycle management configurations to help you optimize storage costs through automated data transitions and deletions. These metrics track the number of lifecycle rules configured across different lifecycle rule types. You can use these metrics to ensure comprehensive lifecycle rule coverage across your buckets and identify opportunities to implement additional cost optimization strategies through automated data management.

###### Advanced data protection metrics

Advanced data protection metrics help you protect your data by providing insights into replication rule counts, SSE-KMS encryption usage, and security vulnerabilities such as unsupported signature and TLS requests. (**Note:** Replication rule count metrics aren't available for prefixes.)

This visibility enables you to ensure proper data redundancy, validate encryption compliance, identify security risks from outdated protocols, troubleshoot replication misconfigurations, and maintain robust data protection strategies at the organization, account, and bucket levels.

###### Advanced performance metrics

Advanced performance metrics reveal how your applications interact with data in S3 and can help identify opportunities to optimize application performance such as inefficient I/O patterns, cross-region access, and unique object access count. Storage Lens advanced performance metrics eliminates the need for expensive custom monitoring tools and enables customers to implement S3 best practices more effectively, particularly benefiting performance sensitive applications such as machine learning training, data analytics, and other high-performance compute workloads.

### Recommendations

S3 Storage Lens provides automated recommendations to help you optimize your storage.
Recommendations are placed contextually alongside relevant metrics in the S3 Storage Lens
dashboard. Historical data is not eligible for recommendations because recommendations are
relevant to what is happening in the most recent period. Recommendations appear only when
they are relevant.

S3 Storage Lens recommendations come in the following forms:

- Suggestions

Suggestions alert you to trends within your storage and activity that might
indicate a storage-cost optimization opportunity or a data protection best practice.
You can use the suggested topics in the _Amazon S3 User Guide_ and the S3 Storage Lens dashboard to drill down for more details
about the specific Regions, buckets, or prefixes.

- Call-outs

Call-outs are recommendations that alert you to interesting anomalies within your
storage and activity over a period that might need further attention or
monitoring.

    + Outlier call-outs


    S3 Storage Lens provides call-outs for metrics that are outliers, based on your
     recent 30-day trend. The outlier is calculated by using a standard score, also
     known as a *z-score*. In this score, the current
     day's metric is subtracted from the average of the last 30 days for that metric.
     The current day's metric is then divided by the standard deviation for that metric
     over the last 30 days. The resulting score is usually between -3 and +3. This
     number represents the number of standard deviations that the current day's metric
     is from the mean.


    S3 Storage Lens considers metrics with a score >2 or <-2 to be outliers because
     they are higher or lower than 95 percent of normally distributed data.
    + Significant change call-outs


    The significant change call-out applies to metrics that are expected to change
     less frequently. Therefore, it's set to a higher sensitivity than the outlier
     calculation, which is typically in the range of +/- 20 percent versus the prior
     day, week, or month.


    Addressing call-outs in your storage and
     activity – If you receive a significant change call-out, it’s
     not necessarily a problem. The call-out could be the result of an anticipated
     change in your storage. For example, you might have recently added a large number
     of new objects, deleted a large number of objects, or made similar planned
     changes.


    If you see a significant change call-out on your dashboard, take note of it
     and determine whether it can be explained by recent circumstances. If not, use the
     S3 Storage Lens dashboard to drill down for more details to understand the specific
     Regions, buckets, or prefixes that are driving the fluctuation.

- Reminders

Reminders provide insights into how Amazon S3 works. They can help you learn more about
ways to use S3 features to reduce storage costs or apply data protection best
practices.

### Metrics selection

S3 Storage Lens offers two metrics selections that you can choose for your dashboard and
export: _free tier_ and _advanced
tier_.

- Free tier

S3 Storage Lens offers free metrics for all dashboards and configurations. Free metrics
contain metrics that are relevant to your storage, such as the number of buckets and
the objects in your account. Free metrics also include use-case based metrics (for
example, cost optimization and data protection metrics) that you can use to
investigate whether your storage is configured according to S3 best practices. All
free tier metrics are collected daily and can be exported to either an S3 general
purpose bucket (CSV or Parquet format) or S3 table bucket
(Parquet format only). Data is available for queries for 14 days in
the Amazon S3 console. For more information about which metrics are available with free
metrics, see the [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").

- Advanced tier

S3 Storage Lens offers free metrics for all dashboards and configurations with the option
to upgrade to advanced metrics. Additional charges apply. For more information, see
[Amazon S3 pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

Advanced tier metrics include all the metrics in free metrics along with
additional metrics, such as advanced data protection and cost optimization metrics,
activity metrics, and detailed status-code metrics. Advanced tier metrics also provide
recommendations to help you optimize your storage. Recommendations are placed
contextually alongside relevant metrics in the dashboard.

Advanced tier includes the following features:

    + Advanced metrics categories – Generate
     additional metrics. For a complete list of advanced metric categories, see [Metrics categories](#storage_lens_basics_metrics_types "#storage_lens_basics_metrics_types"). For a complete list of
     metrics, see the [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").
    + Amazon CloudWatch publishing – Publishes S3 Storage Lens
     metrics to CloudWatch to create a unified view of your operational health in CloudWatch [dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md"). You can also use CloudWatch API operations and features, such as
     alarms and triggered actions, metric math, and anomaly detection, to monitor and
     take action on S3 Storage Lens metrics. For more information, see [Monitor S3 Storage Lens metrics in CloudWatch](storage_lens_view_metrics_cloudwatch.md "storage_lens_view_metrics_cloudwatch.md").
    + Default metrics report – The default
     metrics report in S3 Storage Lens includes free metrics and prefix aggregation
     capabilities for top prefixes for object storage usage and activity trends across
     your AWS accounts. With the default metrics report, you can identify cost
     optimization opportunities at no additional charge beyond standard S3 storage
     costs.
    + Expanded prefixes metrics report – The
     Storage Lens expanded prefixes metrics report provides comprehensive prefix-level
     analytics across your entire S3 storage data, expanding coverage to support up to
     billions of prefixes per bucket.
    + Additional metrics aggregation




    	- Prefix aggregation – Collects
    	 metrics at the [prefix](using-prefixes.md "using-prefixes.md") level. This
    	 setting specifies the prefixes aggregated as part of the default metrics
    	 report, which is displayed in the Storage Lens dashboard. Note that metrics
    	 that are applicable at the prefix level are available with **Prefix aggregation**, except for bucket-level settings
    	 and rule count metrics. Prefix-level metrics don't apply to the expanded
    	 prefixes metrics export and aren't published to CloudWatch.
    	- Storage Lens group aggregation –
    	 Collects metrics at the Storage Lens group level. After you enable the
    	 advanced tier metrics and Storage Lens group aggregation, you can specify
    	 which Storage Lens groups to include or exclude from your Storage Lens
    	 dashboard. At least one Storage Lens group must be specified. Storage Lens
    	 groups that are specified must also reside within the designated home Region
    	 in the dashboard account. Storage Lens group-level metrics are not published
    	 to CloudWatch.

All advanced metrics are collected daily. Data is available for querying for up to
15 months in the Amazon S3 console. For more information about the storage metrics that are
aggregated by S3 Storage Lens, see [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").

### Prefix delimiter

Prefix delimiters determine how Storage Lens counts prefix depth, by separating the
hierarchical levels within object keys. You can only specify a single character to
indicate each level within your prefixes. If the prefix delimiter is undefined, Amazon S3 uses
"`/`" as the default delimiter.

###### Note

When you're updating your Storage Lens dashboard configuration via API, the
_delimiter_ and the updated _prefix delimiter_ must be defined in the same way, or you'll receive an
error. The delimiter only applies to prefix-level metrics that are exported to the
default metrics report. The prefix delimiter applies to all prefixes that are exported
to the expanded prefixes metrics report.

### S3 Storage Lens and AWS Organizations

AWS Organizations is an AWS service that helps you aggregate all of your AWS accounts under
one organization hierarchy. Amazon S3 Storage Lens works with AWS Organizations to provide a single view of
object storage and activity across your Amazon S3 storage.

For more information, see [Using Amazon S3 Storage Lens with AWS Organizations](storage_lens_with_organizations.md "storage_lens_with_organizations.md").

- Trusted access

Using your organization's management account, you must enable trusted access for
S3 Storage Lens to aggregate storage metrics and usage data for all member accounts in your
organization. You can then create dashboards or exports for your organization by using
your management account or by giving delegated administrator access to other accounts
in your organization.

You can disable trusted access for S3 Storage Lens at any time, which stops S3 Storage Lens from
aggregating metrics for your organization.

- Delegated administrator

You can create dashboards and metrics for S3 Storage Lens for your organization by using
your AWS Organizations management account, or by giving _delegated
administrator_ access to other accounts in your organization. You can
deregister delegated administrators at any time. Deregistering a delegated
administrator also automatically stops all organization-level dashboards created by
that delegated administrator from aggregating new storage metrics.

For more information, see [Amazon S3 Storage Lens and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-s3lens.md "../../../organizations/latest/userguide/services-that-can-integrate-s3lens.md") in the _AWS Organizations User Guide_.

#### Amazon S3 Storage Lens service-linked roles

Along with AWS Organizations trusted access, Amazon S3 Storage Lens uses AWS Identity and Access Management (IAM)
service-linked roles. A service-linked role is a unique type of IAM role that's linked
directly to S3 Storage Lens. Service-linked roles are predefined by S3 Storage Lens and include all
the permissions that it requires to collect daily storage and activity metrics from
member accounts in your organization.

For more information, see [Using service-linked roles for Amazon S3 Storage Lens](using-service-linked-roles.md "using-service-linked-roles.md").
