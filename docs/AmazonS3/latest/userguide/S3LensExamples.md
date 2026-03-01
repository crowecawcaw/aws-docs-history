# Working with Amazon S3 Storage Lens by using the console and API

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
the metrics directly to an AWS-managed S3 table bucket.

###### Note

Storage Lens only aggregates metrics for [S3 general purpose buckets](UsingBucket.md "UsingBucket.md").

The following sections contain examples of creating, updating, and viewing S3 Storage Lens
configurations and performing operations related to the feature. If you are using S3 Storage Lens
with AWS Organizations, these examples also cover those use cases. In the examples, replace any
placeholder values.

###### Topics

- [Create an Amazon S3 Storage Lens dashboard](storage_lens_creating_dashboard.md "storage_lens_creating_dashboard.md")
- [Update an Amazon S3 Storage Lens dashboard](storage_lens_editing.md "storage_lens_editing.md")
- [Disable an Amazon S3 Storage Lens dashboard](storage_lens_disabling.md "storage_lens_disabling.md")
- [Delete an Amazon S3 Storage Lens dashboard](storage_lens_deleting.md "storage_lens_deleting.md")
- [List Amazon S3 Storage Lens dashboards](storage_lens_list_dashboard.md "storage_lens_list_dashboard.md")
- [View an Amazon S3 Storage Lens dashboard configuration details](storage_lens_viewing.md "storage_lens_viewing.md")
- [Managing AWS resource tags with S3 Storage Lens](storage-lens-groups-manage-tags-dashboard.md "storage-lens-groups-manage-tags-dashboard.md")
- [Helper files for using Amazon S3 Storage Lens](S3LensHelperFilesCLI.md "S3LensHelperFilesCLI.md")
