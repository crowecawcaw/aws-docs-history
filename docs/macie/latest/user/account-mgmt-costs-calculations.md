# Understanding estimated usage costs

for Macie

Amazon Macie pricing is based on the following dimensions.

Preventative control monitoring

These costs derive from maintaining an inventory of your Amazon Simple Storage Service (Amazon S3) general purpose
buckets, and evaluating and monitoring the buckets for security and access
control. For more information, see [How Macie monitors Amazon S3 data
security](monitoring-s3-how-it-works.md "monitoring-s3-how-it-works.md").

You’re charged based on the total number of S3 general purpose buckets that Macie
evaluates and monitors for your account, for up to 10,000 buckets. The
charges are prorated per day.

Object monitoring for automated sensitive data discovery

These costs derive from monitoring and evaluating your S3 bucket inventory to identify S3
objects that are eligible for analysis by automated sensitive data discovery. For more information,
see [How automated sensitive data discovery works](discovery-asdd-how-it-works.md "discovery-asdd-how-it-works.md").

You’re charged based on the total number of S3 objects that are stored in general purpose
buckets for your account. The charges are prorated per day.

Object analysis by sensitive data discovery jobs and
automated sensitive data discovery

These costs derive from analyzing S3 objects and reporting sensitive data that Macie
finds in the objects. This includes analyses and reporting by
sensitive data discovery jobs and by automated sensitive data discovery. For more information, see [Discovering sensitive data](data-classification.md "data-classification.md").

You’re charged based on the amount of uncompressed data that Macie analyzes in S3
objects. There’s no charge for objects that Macie can’t analyze for reasons
such as use of an unsupported Amazon S3 storage class, use of an unsupported file
or storage format, or permissions settings. In addition, these costs don’t
vary based on the number of sensitive data findings produced by your jobs or
by automated sensitive data discovery.

To manage costs for automated sensitive data discovery, you can exclude individual S3 buckets from the analyses.
For example, you might exclude buckets that are known to meet your
organization's security and compliance requirements. If your account is part
of an organization that centrally manages multiple Macie accounts, an
additional option is to selectively enable or disable automated sensitive data discovery for
individual accounts in your organization. For more information, see [Configuring settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md").

Costs for sensitive data discovery jobs are restricted by the monthly [sensitive data discovery quota](macie-quotas.md "macie-quotas.md") for your account. (The default
quota is 5 TB of data.) If a job is running and the analysis of eligible
objects reaches this quota, Macie automatically pauses the job until the
next calendar month starts and the monthly quota is reset for your account,
or you increase the quota for your account.

If you’re the Macie administrator for an organization, costs for sensitive data discovery jobs are restricted
by the monthly sensitive data discovery quota for each account that you
analyze data for. The quota for a member account defines the maximum amount
of data that your jobs and the member account’s jobs can analyze for the
account during a calendar month. If a job is running and the analysis of
eligible objects reaches this quota for a member account, Macie stops
analyzing objects in buckets that the account owns. When Macie finishes
analyzing objects for all other accounts that haven’t met the quota, Macie
automatically pauses the job. If it’s a one-time job, Macie automatically
resumes the job when the next calendar month starts or the quota is
increased for all the affected accounts, whichever occurs first. If it’s a
periodic job, Macie automatically resumes the job when the next run is
scheduled to start or the next calendar month starts, whichever occurs
first. If a scheduled run starts before the next calendar month starts or
the quota is increased for an affected account, Macie doesn’t analyze
objects in buckets that the account owns.

###### Tip

For helpful tips about managing or reducing sensitive data discovery costs, see the
following blog post on the _AWS Security Blog_:
[How to use Amazon Macie to reduce the cost of discovering sensitive
data](https://aws.amazon.com/blogs/security/how-to-use-amazon-macie-to-reduce-the-cost-of-discovering-sensitive-data/ "https://aws.amazon.com/blogs/security/how-to-use-amazon-macie-to-reduce-the-cost-of-discovering-sensitive-data/").

For detailed information and examples of usage costs, see [Amazon Macie pricing](https://aws.amazon.com/macie/pricing/ "https://aws.amazon.com/macie/pricing/").

When you use Macie to review your estimated usage costs, it’s important to understand
how the cost estimates are calculated. Consider the following:

- The estimates are reported in US dollars (USD) and are for the current AWS Region only.
  If you use Macie in multiple Regions, the data isn’t aggregated for all the
  Regions in which you use Macie.
- On the console, the estimates are inclusive for the current calendar month to
  date. If you query the data programmatically with the Amazon Macie API, you can
  choose an inclusive time range for the estimates. This can be a rolling time
  range of the preceding 30 days or the current calendar month to date.
- The estimates don’t reflect all the discounts that might apply to your
  account. The exception is discounts that derive from Regional volume pricing
  tiers, as described in [Amazon Macie
  pricing](https://aws.amazon.com/macie/pricing/ "https://aws.amazon.com/macie/pricing/"). If your account qualifies for this type of discount, the
  estimates reflect that discount.
- If you're the Macie administrator for an organization, the estimates don’t reflect
  combined usage volume discounts for your organization. For information about
  these discounts, see [Volume discounts](../../../awsaccountbilling/latest/aboutv2/useconsolidatedbilling-effective.md "../../../awsaccountbilling/latest/aboutv2/useconsolidatedbilling-effective.md") in the _AWS Billing User Guide_.
- For preventative control monitoring, the estimate is based on the average
  daily cost for the applicable time range. The cost is prorated per day.
- For automated sensitive data discovery, the overall estimate is based on the average daily cost for object
  monitoring (prorated per day) and the amount of uncompressed data that Macie has
  analyzed thus far during the applicable time range. If you're the Macie administrator
  for an organization and you enable automated sensitive data discovery for member accounts, the estimated
  costs of those activities are included in the estimates for each applicable
  member account.
- For sensitive data discovery jobs, the estimate is based on the amount of uncompressed data that your
  jobs have analyzed thus far during the applicable time range. If you're the
  Macie administrator for an organization and you run jobs that analyze data for member
  accounts, the estimated costs of those jobs are included in the estimate for
  each applicable member account.
- If your account is a member account in an organization and your Macie administrator enables
  automated sensitive data discovery or runs sensitive data discovery jobs that analyze your data, the estimated costs
  of those activities are included in the estimates for your account.
- The estimates don’t include costs that you incur for using other
  AWS services with certain Macie features. For example, using customer managed
  AWS KMS keys to decrypt S3 objects that you want to inspect for sensitive
  data.
  Also note that Macie provides a monthly free tier for analysis of S3 objects by
  sensitive data discovery jobs and automated sensitive data discovery. Each month, there’s no charge to analyze up to 1 GB of
  data to discover and report sensitive data in S3 objects. If more than 1 GB of data is
  analyzed during a given month, sensitive data discovery charges begin to accrue for your
  account after the first 1 GB of data. If less than 1 GB of data is analyzed during a
  given month, the remaining allocation doesn't roll over to the next month. If your
  account is part of an organization with consolidated billing, the free tier applies to
  the combined amount of data analyzed for your organization. In other words, there’s no
  charge to analyze up to 1 GB of data each month for all the accounts in your
  organization.
