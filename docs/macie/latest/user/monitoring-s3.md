# Monitoring data security and privacy with Macie

When you enable Amazon Macie for your AWS account, Macie automatically generates and begins
maintaining an inventory of your Amazon Simple Storage Service (Amazon S3) general purpose buckets in the current
AWS Region. Macie also begins evaluating and monitoring the buckets for security and
access control. If Macie detects an event that reduces the security or privacy of a bucket,
Macie creates a [policy finding](findings-types.md#findings-policy-types "findings-types.md#findings-policy-types") for you to
review and remediate as necessary.

To also evaluate and monitor the S3 buckets for the presence of sensitive data, you can
create and run sensitive data discovery jobs. Sensitive data discovery jobs can perform
incremental analysis of bucket objects on a daily, weekly, or monthly basis. If Macie
detects sensitive data in an S3 object, Macie creates a [sensitive data finding](findings-types.md#findings-sensitive-data-types "findings-types.md#findings-sensitive-data-types") to notify you of
the sensitive data that it found. Depending on your account settings, you can also configure
Macie to perform automated sensitive data discovery. Automated sensitive data discovery uses sampling techniques to continually
identify, select, and analyze representative objects in your buckets. For more information
about both options, see [Discovering sensitive data](data-classification.md "data-classification.md").

Macie also provides constant visibility into the security and privacy of your Amazon S3 data. To
assess the security posture of your data and determine where to take action, you can use the
**Summary** dashboard on the console. The dashboard provides a snapshot
of aggregated statistics for your Amazon S3 data. The statistics include data for key security
metrics such as the number of general purpose buckets that are publicly accessible or shared
with other AWS accounts. The dashboard also displays groups of aggregated findings data
for your account—for example, the names of 1–5 buckets that have the most
findings for the preceding seven days. You can drill down on each statistic to review its
supporting data. To query the statistics programmatically, use the [GetBucketStatistics](../APIReference/datasources-s3-statistics.md "../APIReference/datasources-s3-statistics.md") operation of the Amazon Macie API.

For deeper analysis and evaluation, Macie provides detailed information and statistics for
individual S3 buckets in your inventory. This includes breakdowns of each bucket’s public
access and encryption settings, and the size and number of objects that Macie can analyze to
detect sensitive data in the bucket. The inventory also indicates whether you configured
sensitive data discovery jobs or automated sensitive data discovery to analyze objects in a bucket. If you have, it
indicates when that analysis most recently occurred. You can browse, sort, and filter the
inventory by using the Amazon Macie console or the [DescribeBuckets](../APIReference/datasources-s3.md "../APIReference/datasources-s3.md") operation of
the Amazon Macie API.

If you're the Macie administrator for an organization, you can access statistical and other data
about S3 buckets that your member accounts own. You can also access policy findings that
Macie generates for the buckets, and inspect the buckets for sensitive data. This means that
you can use Macie to assess and monitor the overall security posture of your organization’s
Amazon S3 data estate. For more information, see [Managing multiple accounts](macie-accounts.md "macie-accounts.md").

###### Topics

- [How Macie monitors Amazon S3 data security](monitoring-s3-how-it-works.md "monitoring-s3-how-it-works.md")
- [Assessing your Amazon S3 security posture with Macie](monitoring-s3-dashboard.md "monitoring-s3-dashboard.md")
- [Analyzing your Amazon S3 security posture with Macie](monitoring-s3-inventory.md "monitoring-s3-inventory.md")
- [Allowing Macie to access S3 buckets and
  objects](monitoring-restrictive-s3-buckets.md "monitoring-restrictive-s3-buckets.md")
