# Forecasting and monitoring costs for sensitive data

discovery jobs

Amazon Macie pricing is based partly on the amount of data that you analyze by running
sensitive data discovery jobs. To forecast and monitor your estimated costs for running
sensitive data discovery jobs, you can review cost estimates that Macie provides when you
create a job and after you start running jobs.

To review and monitor your actual costs, you can use AWS Billing and Cost Management. AWS Billing and Cost Management provides features
that are designed to help you track and analyze your costs for AWS services, and manage
budgets for your account or organization. It also provides features that can help you
forecast usage costs based on historical data. To learn more, see the [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md").

For information about Macie pricing, see [Amazon Macie pricing](https://aws.amazon.com/macie/pricing/ "https://aws.amazon.com/macie/pricing/").

###### Topics

- [Forecasting the cost of a
  job](#discovery-jobs-costs-forecast "#discovery-jobs-costs-forecast")
- [Monitoring estimated costs for
  jobs](#discovery-jobs-costs-track "#discovery-jobs-costs-track")

## Forecasting the cost of a sensitive data

discovery job

When you create a sensitive data discovery job, Amazon Macie can calculate and display estimated
costs during two key steps in the job creation process: when you review the table of S3
buckets that you selected for the job (step 2) and when you review all the settings for
the job (step 8). These estimates can help you determine whether to adjust the job's
settings before you save the job. The availability and nature of the estimates depends
on the settings that you choose for the job.

Reviewing estimated costs for individual buckets (step 2)

If you explicitly select individual buckets for a job to analyze, you can review the
estimated cost of analyzing objects in each of those buckets. Macie displays
these estimates during step 2 of the job creation process, when you review
your bucket selections. In the table for this step, the **Estimated
cost** field indicates the total estimated cost (in US dollars)
of running the job once to analyze objects in a bucket.

Each estimate reflects the projected amount of uncompressed data that the job will
analyze in a bucket, based on the size and types of objects that are
currently stored in the bucket. The estimate also reflects Macie pricing for
the current AWS Region.

Only classifiable objects are included in the cost estimate for a bucket. A _classifiable object_ is an S3 object that uses a
[supported Amazon S3 storage
class](discovery-supported-storage.md#discovery-supported-s3-classes "discovery-supported-storage.md#discovery-supported-s3-classes") and has a file name extension for a [supported file or storage
format](discovery-supported-storage.md#discovery-supported-formats "discovery-supported-storage.md#discovery-supported-formats"). If any classifiable objects are compressed or archive
files, the estimate assumes that the files use a 3:1 compression ratio and
the job can analyze all extracted files.

Reviewing the total estimated cost of a job (step 8)

If you create a one-time job or you create and configure a periodic job to include
existing S3 objects, Macie calculates and displays the job's total estimated
cost during the final step of the job creation process. You can review this
estimate while you review and verify all the settings that you selected for
the job.

This estimate indicates the total projected cost (in US dollars) of
running the job once in the current Region. The estimate reflects the
projected amount of uncompressed data that the job will analyze. It's based
on the size and types of objects that are currently stored in buckets that
you explicitly selected for the job or up to 500 buckets that currently
match bucket criteria that you specified for the job, depending on the job's
settings.

Note that this estimate doesn't reflect any options that you selected to
refine and reduce the scope of the job—for example, a lower sampling
depth, or criteria that exclude certain S3 objects from the job. It also
doesn't reflect your monthly [sensitive data
discovery quota](macie-quotas.md "macie-quotas.md"), which might limit the scope and cost of the
job's analysis, or any discounts that might apply to your account.

In addition to the total estimated cost of the job, the estimate provides
aggregated data that offers insight into the projected scope and cost of the
job:

- **Size** values indicate the total storage size
  of the objects that the job can and can't analyze.
- **Object count** values indicate the total number
  of objects that the job can and can't analyze.

In these values, a **Classifiable** object is an S3 object that uses a
[supported Amazon S3 storage
class](discovery-supported-storage.md#discovery-supported-s3-classes "discovery-supported-storage.md#discovery-supported-s3-classes") and has a file name extension for a [supported file or storage
format](discovery-supported-storage.md#discovery-supported-formats "discovery-supported-storage.md#discovery-supported-formats"). Only classifiable objects are included in the cost
estimate. A **Not classifiable** object is an object that
doesn't use a supported storage class or doesn't have a file name extension
for a supported file or storage format. These objects aren't included in the
cost estimate.

The estimate provides additional aggregated data for S3 objects that are
compressed or archive files. The **Compressed** value
indicates the total storage size of objects that use a supported Amazon S3
storage class and have a file name extension for a supported type of
compressed or archive file. The **Uncompressed** value
indicates the approximate size of these objects if they're decompressed,
based on a specified compression ratio. This data is relevant due to the way
that Macie analyzes compressed files and archive files.

When Macie analyzes a
compressed or archive file, it inspects both the full file and the contents
of the file. To inspect the file’s contents, Macie decompresses the file,
and then inspects each extracted file that uses a supported format. The
actual amount of data that a job analyzes therefore depends on:

- Whether a file uses compression and, if so, the compression ratio
  that it uses.
- The number, size, and format of the extracted files.

By default, Macie assumes the following when it calculates cost estimates
for a job:

- All compressed and archive files use a 3:1 compression
  ratio.
- All the extracted files use a supported file or storage
  format.

These assumptions can result in a larger size estimate for the scope of
the data that the job will analyze, and, consequently, a higher cost
estimate for the job.

You can recalculate the job's total estimated cost based on a different
compression ratio. To do this, choose the ratio from the **Choose an
estimated compression ratio** list in the **Estimated
cost** section. Macie then updates the estimate to match your
selection.

For more information about how Macie calculates estimated costs, see [Understanding estimated
usage costs](account-mgmt-costs-calculations.md "account-mgmt-costs-calculations.md").

## Monitoring estimated costs for sensitive

data discovery jobs

If you’re already running sensitive data discovery jobs, the **Usage** page
on the Amazon Macie console can help you monitor the estimated cost of those jobs. The page
shows your estimated costs (in US dollars) for using Macie in the current AWS Region
during the current calendar month. For information about how Macie calculates these
estimates, see [Understanding estimated
usage costs](account-mgmt-costs-calculations.md "account-mgmt-costs-calculations.md").

###### To review your estimated costs for running jobs

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to review your estimated costs.
3. In the navigation pane, choose **Usage**.
4. On the **Usage** page, refer to the breakdown of estimated costs for your
   account. The **Sensitive data discovery jobs** item reports the
   total estimated cost of the jobs that you've run thus far during the current
   month in the current Region.

If you're the Macie administrator for an organization, the **Estimated costs**
section shows estimated costs for your organization overall for the current
month in the current Region. To show the total estimated cost of the jobs that
were run for a specific account, choose the account in the table. The
**Estimated costs** section then shows a breakdown of
estimated costs for the account, including the estimated cost of the jobs that
were run. To show this data for a different account, choose the account in the
table. To clear your account selection, choose **X** next to
the account ID.

To review and monitor your actual costs, use [AWS Billing and Cost Management](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md").
