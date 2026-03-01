# Viewing S3 Storage Lens metrics on the dashboards

In the Amazon S3 console, S3 Storage Lens provides an interactive default dashboard that you can use to
visualize insights and trends in your data. You can also use this dashboard to flag outliers and
receive recommendations for optimizing storage costs and applying data-protection best
practices. Your dashboard has drill-down options to generate insights at the account, bucket,
AWS Region, prefix, or Storage Lens group level. If you've enabled S3 Storage Lens to work with
AWS Organizations, you can also generate insights at the organization level (such as data for all
accounts that are part of your AWS Organizations hierarchy). The dashboard always loads for the latest
date that has metrics available.

The S3 Storage Lens default dashboard on the console is named
**default-account-dashboard**. Amazon S3 pre-configures this dashboard to
visualize the summarized insights and trends for your entire account and updates them daily in
the S3 console. You can't modify the configuration scope of the default dashboard, but you can
upgrade the metrics selection from the free metrics to the paid advanced metrics and
recommendations. With advanced metrics and recommendations, you can access additional metrics
and features. These features include advanced metric categories, prefix-level aggregation,
contextual recommendations, and Amazon CloudWatch publishing.

You can disable the default dashboard, but you can't delete it. If you disable your default
dashboard, it is no longer updated. You also will no longer receive any new daily metrics in
S3 Storage Lens or in the **Account snapshot** section on the
**Buckets** page. You can still see historic data in the default dashboard
until the 14-day period for data queries expires. This period is 15 months if you've enabled
advanced metrics and recommendations. To access this data, you can re-enable the default
dashboard within the expiration period.

You can create additional S3 Storage Lens dashboards and scope them by AWS Regions, S3 buckets,
or accounts. You can also scope your dashboards by organization if you've enabled Storage Lens
to work with AWS Organizations. When you create or edit an S3 Storage Lens dashboard, you define your dashboard
scope and metrics selection.

You can disable or delete any additional dashboards that you create.

- If you disable a dashboard, it is no longer updated, and you will no longer receive any
  new daily metrics. You can still see historic data for free metrics until the 14-day
  expiration period. If you enabled advanced metrics and recommendations for that dashboard,
  this period is 15 months. To access this data, you can re-enable the dashboard within the
  expiration period.
- If you delete your dashboard, you lose all your dashboard configuration settings. You
  will no longer receive any new daily metrics, and you also lose access to the historical
  data associated with that dashboard. If you want to access the historic data for a deleted
  dashboard, you must create another dashboard with the same name in the same home
  Region.

###### Topics

- [Viewing an Amazon S3 Storage Lens dashboard](#storage_lens_console_viewing "#storage_lens_console_viewing")
- [Understanding your S3 Storage Lens dashboard](#storage_lens_console_viewing_dashboard "#storage_lens_console_viewing_dashboard")

## Viewing an Amazon S3 Storage Lens dashboard

The following procedure shows how to view an S3 Storage Lens dashboard in the S3 console. For
use-case based walkthroughs that show how to use your dashboard to optimize costs, implement
best practices, and improve the performance of applications that access your S3 buckets, see
[Amazon S3 Storage Lens metrics use cases](storage-lens-use-cases.md "storage-lens-use-cases.md").

###### Note

You can't use your account's root user credentials to view Amazon S3 Storage Lens dashboards. To
access S3 Storage Lens dashboards, you must grant the required AWS Identity and Access Management (IAM) permissions to a new or
existing IAM user. Then, sign in with those user credentials to
access S3 Storage Lens dashboards. For more information, see [Setting Amazon S3 Storage Lens permissions](storage_lens_iam_permissions.md "storage_lens_iam_permissions.md") and
[Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
in the _IAM User Guide_.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Storage Lens**,
   **Dashboards**.
3. In the **Dashboards** list, choose the dashboard that you want to
   view.

Your dashboard opens in S3 Storage Lens. The **Snapshot for _date_** section shows the latest date that S3 Storage Lens has collected
metrics for. Your dashboard always loads the latest date that has metrics
available. 4. (Optional) To change the date for your S3 Storage Lens dashboard, in the top-right date
selector, choose a new date. 5. (Optional) To apply temporary filters to further limit the scope of your dashboard
data, do the following:

    1. Expand the **Filters** section.
    2. To filter by specific accounts, AWS Regions, storage classes, buckets, prefixes,
     or Storage Lens groups, choose the options to filter by.


    ###### Note

    The **Prefixes** filter and the **Storage Lens
     groups** filter can’t be applied at the same time.
    3. To update a filter, choose **Apply**.
    4. To remove a filter, click on the **X** next to the filter.

6. In any section in your S3 Storage Lens dashboard, to see data for a specific metric, for
   **Metric**, choose the metric name.
7. In any chart or visualization in your S3 Storage Lens dashboard, you can drill down into
   deeper levels of aggregation by using the **Accounts**,
   **AWS Regions**, **Storage classes**,
   **Buckets**, **Prefixes**, or **Storage Lens
   groups** tabs. For an example, see [Uncover cold Amazon S3 buckets](storage-lens-optimize-storage.md#uncover-cold-buckets "storage-lens-optimize-storage.md#uncover-cold-buckets").

## Understanding your S3 Storage Lens dashboard

Your S3 Storage Lens dashboard has a primary **Overview** tab, and up to five
additional tabs that represent each aggregation level:

- **Accounts**
- **AWS Regions**
- **Storage classes**
- **Buckets**
- **Prefixes**
- **Storage Lens groups**

On the **Overview** tab, your dashboard data is aggregated into three
different sections: **Snapshot for _date_**,
**Trends and distributions**, and **Top N overview**.

For more information about your S3 Storage Lens dashboard, see the following sections.

### Snapshot

The **Snapshot for _date_** section
shows summary metrics that S3 Storage Lens has aggregated for the date selected. These summary
metrics include the following metrics:

- **Total storage** – The total amount of storage used in
  bytes.
- **Object count** – The total number of objects in your
  AWS account.
- **Average object size** – The average object size.
- **Active buckets** – The total number of active buckets in
  active usage with storage > 0 bytes in your account.
- **Accounts** – The number of accounts whose storage is in
  scope. This value is **1** unless you are using AWS Organizations and your
  S3 Storage Lens has trusted access with a valid service-linked role. For more information, see
  [Using service-linked roles for Amazon S3 Storage Lens](using-service-linked-roles.md "using-service-linked-roles.md").
- **Buckets** – The total number of buckets in your
  account.

###### Metric data

For each metric that appears in the snapshot, you can see the following data:

- **Metric name** – The name of the metric.
- **Metric category** – The category that the metric is
  organized into.
- **Total for _date_** – The
  total count for the date selected.
- **% change** – The percentage change from the last snapshot
  date.
- **30-day trend** – A trend-line showing the changes for the
  metric over a 30-day period.
- **Recommendation** – A contextual recommendation based on
  the data that's provided in the snapshot. Recommendations are available with advanced
  metrics and recommendations. For more information, see [Recommendations](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_recommendations "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_recommendations").

###### Metrics categories

You can optionally update your dashboard **Snapshot for _date_** section to display metrics for other
categories. If you want to see snapshot data for additional metrics, you can choose from
the following **Metrics categories**:

- **Cost optimization**
- **Data protection**
- **Activity** (available with advanced metrics)
- **Access management**
- **Performance**
- **Events**

The **Snapshot for _date_** section
displays only a selection of metrics for each category. To see all metrics for a specific
category, choose the metric in the **Trends and distributions** or
**Top N overview** sections. For more information about metric
categories, see [Metrics categories](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_types "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_types"). For a complete list of S3 Storage Lens
metrics, see [Amazon S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").

### Trends and distributions

The second section of the **Overview** tab is **Trends and
distributions**. In the **Trends and distributions** section,
you can choose two metrics to compare over a date range that you define. The
**Trends and distributions** section shows the relationship between two
metrics over time. This section displays charts that you can use to see the
**Storage class** and **Region** distribution between
the two trends that you are tracking. You can optionally drill down into a data point in one
of the charts for deeper analysis.

For a walkthrough that uses the **Trends and distributions** section,
see [Identify buckets that don't use server-side encryption with AWS KMS for default encryption (SSE-KMS)](storage-lens-data-protection.md#storage-lens-sse-kms "storage-lens-data-protection.md#storage-lens-sse-kms").

### Top N overview

The third section of the S3 Storage Lens dashboard is **Top N overview**
(sorted in ascending or descending order). This section displays your selected metrics
across the top number of accounts, AWS Regions, buckets, prefixes, or Storage Lens groups.
If you enabled S3 Storage Lens to work with AWS Organizations, you can also see your selected metrics across
your organization.

For a walkthrough that uses the **Top N overview** section, see [Identify your largest S3 buckets](storage-lens-optimize-storage.md#identify-largest-s3-buckets "storage-lens-optimize-storage.md#identify-largest-s3-buckets").

### Drill down and analyze by options

To provide a fluid experience for analysis, the S3 Storage Lens dashboard provides an action
menu, which appears when you choose any chart value. To use this menu, choose any chart
value to see the associated metrics values, and then choose from two options in the box that
appears:

- The **Drill down** action applies the selected value as a filter
  across all tabs of your dashboard. You can then drill down into that value for deeper
  analysis.
- The **Analyze by** action takes you to the
  **Dimension** tab that you select and applies that tab value as a
  filter. These tabs include **Accounts**,
  **AWS Regions**, **Storage classes**,
  **Buckets**, **Prefixes** (for dashboards that have
  **Advanced metrics** and **Prefix aggregation**
  enabled), and **Storage Lens groups** (for dashboards that have
  **Advanced metrics** and **Storage Lens group
  aggregation** enabled).
  With **Analyze by**, you can view
  the data in the context of the new dimension for deeper analysis.

The **Drill down** and **Analyze by** actions might be
disabled if the outcome would yield illogical results or would not have any value. Both the
**Drill down** and **Analyze by** actions apply filters
on top of any existing filters across all tabs of the dashboard. You can also remove the
filters as needed.

### Tabs

The dimension-level tabs provide a detailed view of all values within a particular
dimension. For example, the **AWS Regions** tab shows metrics for all
AWS Regions, and the **Buckets** tab shows metrics for all buckets. Each
dimension tab contains an identical layout consisting of four sections:

- A trend chart that displays your top _N_ items
  within the dimension over the last 30 days for the selected metric. By default, this
  chart displays the top 10 items, but you can decrease it to at least 3 items or increase
  it up to 50 items.
- A histogram chart that shows a vertical bar chart for the selected date and metric.
  If you have a large number of items to display in this chart, you might need to scroll
  horizontally.
- A bubble analysis chart that plots all items within the dimension. This chart
  represents the first metric on the x axis and the second metric on the y axis. The third
  metric is represented by the size of the bubble.
- A metric grid view that contains each item in the dimension listed in rows. The
  columns represent each available metric, arranged in metrics category tabs for easier
  navigation.
