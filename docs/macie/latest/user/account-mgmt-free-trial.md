# Participating in the free trial of Macie

When you enable Amazon Macie for the first time, your AWS account is automatically
enrolled in the 30-day free trial of Macie. This includes individual member accounts in
an AWS Organizations organization.

During the free trial, there’s no charge for using Macie in a specific AWS Region to:

- Perform preventative control monitoring
  – This includes generating and maintaining an inventory of your Amazon Simple Storage Service
  (Amazon S3) general purpose buckets in the Region. It also includes evaluating and
  monitoring the buckets for security and access control.

For more information, see [How Macie monitors Amazon S3 data
security](monitoring-s3-how-it-works.md "monitoring-s3-how-it-works.md").

- Perform automated sensitive data discovery – This includes monitoring and
  evaluating your S3 bucket inventory in the Region to identify S3 objects that
  are eligible for analysis. It also includes analyzing eligible objects and
  reporting sensitive data statistics, findings, and other types of results. To
  configure and manage this feature, you must be the Macie administrator for an
  organization or have a standalone Macie account. If you're a Macie administrator, you
  can use this feature to analyze objects in S3 buckets that your member accounts
  own.

For more information, see [How automated sensitive data discovery works](discovery-asdd-how-it-works.md "discovery-asdd-how-it-works.md").
For a list of Regions where Macie is currently available, see [Amazon Macie endpoints and quotas](../../../general/latest/gr/macie.md "../../../general/latest/gr/macie.md") in the
_AWS General Reference_.

The free trial runs for 30 consecutive days. You can’t pause it after it starts. After the
free trial ends, charges begin to accrue for performing preventative control monitoring.
Charges also begin to accrue for performing automated sensitive data discovery. If you’re the Macie administrator for an
organization, charges accrue as applicable for each account in your organization. You
can use Macie to review breakdowns of estimated usage costs for individual accounts in
your organization.

###### Notes

During the free trial, you might incur charges for other AWS services that you
use with certain Macie features—for example, using customer managed
AWS KMS keys to decrypt S3 objects that you want to inspect for sensitive
data.

The free trial doesn’t include analysis of S3 objects by sensitive data discovery jobs. You’ll
incur charges if you create and run sensitive data discovery jobs that analyze more than 1 GB of
uncompressed data during the free trial. (Macie provides a monthly free tier for
sensitive data discovery. Each month, there’s no charge to analyze up to 1 GB of
uncompressed data in S3 objects. After the first 1 GB of data, costs accrue.)

During the free trial, you can check the status of your trial and review estimated usage
costs for your account. The cost estimates are based on your use of Macie thus far
during the free trial. They can help you understand what some of your usage costs might
be after the trial ends. For details about how Macie calculates these values, see [Understanding estimated
usage costs](account-mgmt-costs-calculations.md "account-mgmt-costs-calculations.md").

###### To check your status and estimated costs during the free trial

Follow these steps to check the status of your trial and review your estimated usage costs
by using the Amazon Macie console. To access this data programmatically, you can use
the [GetUsageStatistics](../APIReference/usage-statistics.md "../APIReference/usage-statistics.md")
operation of the Amazon Macie API.

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to check the status of your free trial and your estimated
   usage costs.
3. In the navigation pane, choose **Usage**.
   The **Usage** page indicates the number of remaining days in your free
   trial. It also shows a breakdown of your estimated usage costs in US dollars
   (USD):

- **Preventative control monitoring** – This is the total projected
  cost of maintaining an inventory of your S3 general purpose buckets, and
  evaluating and monitoring the buckets for security and access control after the
  free trial ends.
- **Sensitive data discovery jobs** – This is the total
  estimated cost of any sensitive data discovery jobs that you ran. Sensitive data
  discovery jobs aren’t included in the free trial.
- **Automated sensitive data discovery** – These are the total projected costs of
  performing automated sensitive data discovery after the free trial ends, broken down by pricing
  dimension—object monitoring and object analysis. To review these
  estimates on the console, you must be the Macie administrator for an organization or
  have a standalone Macie account.
  If you’re the Macie administrator for an organization, the **Usage** page provides
  details about the accounts in your organization. In the table:

- **Service quota – Jobs** – This is the current
  monthly quota for running sensitive data discovery jobs to analyze S3 objects in
  buckets that an account owns.
- **Free trial** – These fields indicate whether an
  account is currently participating in the free trial for preventative control
  monitoring or automated sensitive data discovery. A **Free trial** field is empty if
  the applicable free trial has ended for an account.
- **Total** – This is the total estimated cost for an
  account.
  The **Estimated costs** section shows estimated costs for your organization
  overall. To review the breakdown of estimated costs for a specific account in your
  organization, choose the account in the table. The **Estimated costs**
  section then shows this breakdown. To show this data for another account, choose the
  account in the table. To clear your account selection, choose **X**
  next to the account ID.

###### Notes

If an account stores more than 150 TB of data in Amazon S3, the account's estimated and actual
costs for automated sensitive data discovery might be higher than the cost projections that Macie provides
during the 30-day free trial. This is because object analysis by automated sensitive data discovery is
paused when 150 GB of uncompressed data has been analyzed for an account that's
enrolled in the free trial. Object analysis resumes for the account after the free
trial ends. For assistance forecasting costs for an account that stores more than
150 TB of data in Amazon S3, contact AWS Support.

To manage costs for automated sensitive data discovery after the free trial ends, you can exclude individual S3
buckets from subsequent analyses. If you’re the Macie administrator for an organization, an
additional option is to selectively enable or disable automated sensitive data discovery for individual
accounts in your organization. For information about these options, see [Configuring settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md").
