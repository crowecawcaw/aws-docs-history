# Analyzing your Amazon S3 security posture with Macie

To help you perform in-depth analysis and evaluate the security posture of your Amazon Simple Storage Service
(Amazon S3) data, Amazon Macie generates and maintains an inventory of your S3 general purpose
buckets in each AWS Region where you use Macie. To learn how Macie maintains this
inventory for you, see [How Macie monitors Amazon S3 data
security](monitoring-s3-how-it-works.md "monitoring-s3-how-it-works.md"). If you're the Macie administrator for an
organization, the inventory includes data for S3 buckets that your member accounts
own.

By using this inventory, you can review your Amazon S3 data estate, and examine details and
statistics for key security settings and metrics that apply to individual S3 buckets. For
example, you can access breakdowns of each bucket’s public access and encryption settings,
and the size and number of objects that Macie can analyze to detect sensitive data in each
bucket. You can also determine whether you configured sensitive data discovery jobs or
automated sensitive data discovery to analyze objects in a bucket. If you have, your inventory data indicates when
that analysis most recently occurred. If automated sensitive data discovery is enabled, you can also use the
inventory to review the results of automated sensitive data discovery activities that Macie has performed thus far
for your Amazon S3 data. For more information, see [Discovering sensitive data](data-classification.md "data-classification.md").

You can browse and filter inventory data by using the **S3 buckets** page on
the Amazon Macie console. You can also access your inventory data programmatically by using the
[DescribeBuckets](../APIReference/datasources-s3.md "../APIReference/datasources-s3.md") operation of the Amazon Macie API.

###### Topics

- [Reviewing your S3 bucket
  inventory](monitoring-s3-inventory-review.md "monitoring-s3-inventory-review.md")
- [Filtering your S3 bucket
  inventory](monitoring-s3-inventory-filter.md "monitoring-s3-inventory-filter.md")
