# Getting started with Macie

This tutorial provides an introduction to Amazon Macie. You'll learn how to enable Macie for
your AWS account. You'll also learn how to assess your Amazon Simple Storage Service (Amazon S3) security posture
and configure key settings and resources for discovering and reporting sensitive data in
your S3 buckets.

###### Tasks

- [Before you begin](#prerequisites "#prerequisites")
- [Step 1: Enable Macie](#enable-macie "#enable-macie")
- [Step 2: Configure a repository for sensitive
  data discovery results](#gs-configure-repository "#gs-configure-repository")
- [Step 3: Explore sample findings](#gs-create-sample-findings "#gs-create-sample-findings")
- [Step 4: Create a job to discover sensitive data](#gs-create-job "#gs-create-job")
- [Step 5: Review findings](#review-findings "#review-findings")

## Before you begin

When you sign up for Amazon Web Services (AWS), your account is automatically signed up for all
AWS services, including Amazon Macie. However, to enable and use Macie, you first have to
set up permissions that allow you to access the Amazon Macie console and API operations.
You or your AWS administrator can do this by using AWS Identity and Access Management (IAM) to attach the
AWS managed policy named `AmazonMacieFullAccess` to your IAM identity. To
learn more, see [AWS managed policies for Macie](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Step 1: Enable Macie

After you set up the required permissions, you can enable Amazon Macie for your AWS account.
Follow these steps to enable Macie for your account.

###### To enable Macie

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to enable and use Macie.
3. On the Amazon Macie page, choose **Get started**.
4. (Optional) When you enable Macie, Macie automatically creates a service-linked role that
   allows it to call other AWS services and monitor AWS resources on your
   behalf. To review the permissions policy for this role, choose **View
   role permissions** on the console. To learn more about this role,
   see [Using service-linked roles for Macie](service-linked-roles.md "service-linked-roles.md").
5. Choose **Enable Macie**.

Within minutes, Macie automatically generates and begins maintaining an inventory of your S3
general purpose buckets in the current Region. Macie also begins evaluating and
monitoring the buckets for security and access control. To learn more, see [Monitoring data security and
privacy](monitoring-s3.md "monitoring-s3.md").

Depending on your account settings, Macie also begins performing automated sensitive data discovery for your S3
buckets. Macie begins to continually identify, select, and analyze representative
objects in your buckets, inspecting the objects for sensitive data. As the analyses
progress, Macie provides statistics and other results that you can review, typically
within 48 hours. You can customize the analyses. To learn more, see [Performing automated sensitive data discovery](discovery-asdd.md "discovery-asdd.md").

To review aggregated statistics for your Amazon S3 data, choose **Summary** in
the navigation pane on the console. To review details about individual S3 buckets in
your inventory, choose **S3 buckets** in the navigation pane. To then
display a bucket's details, choose the bucket. The details panel displays statistics and
other information that provide insight into the security, privacy, and sensitivity of
the bucket’s data. To learn about these details, see [Reviewing your S3 bucket
inventory](monitoring-s3-inventory-review.md "monitoring-s3-inventory-review.md").

## Step 2: Configure a repository for sensitive

data discovery results

With Amazon Macie, you can discover sensitive data in S3 buckets in two ways: by configuring
Macie to perform automated sensitive data discovery and by running sensitive data discovery jobs. A _sensitive data discovery job_ is a job that you create to
analyze objects in S3 buckets to determine whether the objects contain sensitive
data.

Macie creates a record for each S3 object that it analyzes when you run sensitive data
discovery jobs or it performs automated sensitive data discovery. These records, referred to as _sensitive data discovery results_, log details about the
analysis of individual objects. Macie also creates sensitive data discovery results for
objects that it can't analyze due to errors or issues. Sensitive data discovery results
provide you with analysis records that can be helpful for data privacy and protection
audits or investigations.

Macie stores your sensitive data discovery results for only 90 days. To access the results
and enable long-term storage and retention of them, configure Macie to store the results
in an S3 bucket. You should do this within 30 days of enabling Macie. After you do this,
the bucket can serve as a definitive, long-term repository for all of your sensitive
data discovery results.

To learn how to configure this repository, see [Storing and retaining
sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md").

## Step 3: Explore sample findings

In Amazon Macie, there are two categories of findings, _policy
findings_ and _sensitive data findings_.
Macie creates a policy finding when the policies or settings for an S3 general purpose
bucket are changed in a way that reduces the security or privacy of the bucket and the
bucket's objects. Macie creates a sensitive data finding when it detects sensitive data
in an S3 object. Within each category, there are multiple types of findings.

To explore and learn about the different categories and types of findings that Macie
provides, optionally create and review sample findings. Sample findings use example data
and placeholder values to demonstrate the kinds of information that Macie might include
in each type of finding.

Follow these steps to create and review sample findings.

###### To create and review sample findings

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Settings**.
3. Under **Sample findings**, choose **Generate sample
   findings**. Macie generates one sample finding for each type of
   finding that Macie supports.
4. In the navigation pane, choose **Findings**. The
   **Findings** page displays findings for your account in the
   current AWS Region. This includes the sample findings that you created in the
   preceding step.
5. On the **Findings** page, locate findings whose type begins with
   **[SAMPLE]**.
6. To review the details of a particular sample finding, choose the finding. The details
   panel displays the finding's details.

To learn about each type of finding, see [Types of findings](findings-types.md "findings-types.md"). To learn more about creating and reviewing
sample findings, see [Working with sample findings](findings-samples.md "findings-samples.md").

## Step 4: Create a job to discover sensitive data

To discover and report sensitive data in S3 buckets, you can run sensitive data discovery
jobs. A _sensitive data discovery job_ is a job that
you create to analyze objects in S3 buckets to determine whether the objects contain
sensitive data. Unlike automated sensitive data discovery, you define the breadth and depth of the analysis. You
also specify how often to run a job—once or periodically on a scheduled
basis.

Follow these steps to create a job that runs once, immediately after you create it, and
uses default settings. To learn how to create a job that runs periodically or uses custom
settings, see [Creating a sensitive data discovery job](discovery-jobs-create.md "discovery-jobs-create.md").

###### To create a sensitive data discovery job

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Jobs**.
3. Choose **Create job**.
4. For the **Choose S3 buckets** step, choose **Select specific
   buckets**. Then, in the table, select the checkbox for each S3
   bucket that you want the job to analyze.

The table provides an inventory of your S3 general purpose buckets in the current
AWS Region. To find specific buckets more easily, enter filter criteria in the
filter box above the table. You can also sort the table by choosing a column
heading. 5. When you finish selecting buckets, choose **Next**. 6. For the **Review S3 buckets** step, review and verify your bucket
selections, and then choose **Next**. 7. For the **Refine the scope** step, choose **One-time
job**, and then choose **Next**. 8. For the **Select managed data identifiers** step, choose
**Recommended**. Optionally review the table of managed
data identifiers that we recommend for jobs, and then choose
**Next**.

A _managed data identifier_ is a set of built-in criteria
and techniques that are designed to detect a specific type of sensitive
data—for example, credit card numbers, AWS secret access keys, or
passport numbers for a particular country or region. To learn more, see [Using managed data
identifiers](managed-data-identifiers.md "managed-data-identifiers.md"). 9. For the **Select custom data identifiers** step, choose
**Next**.

A _custom data identifier_ is a set of criteria that you
define to detect sensitive data—a regular expression (_regex_) that defines a text pattern to match and,
optionally, character sequences and a proximity rule that refine the results. To
learn more, see [Building custom data
identifiers](custom-data-identifiers.md "custom-data-identifiers.md"). 10. For the **Select allow lists** step, choose
**Next**.

In Macie, an _allow list_ specifies text or a text
pattern that you want Macie to ignore when it inspects S3 objects for sensitive
data. These are typically sensitive data exceptions for particular scenarios or
environments. To learn more, see [Defining sensitive data exceptions with allow
lists](allow-lists.md "allow-lists.md"). 11. For the **Enter general settings** step, enter a name and,
optionally, a description of the job. Then choose
**Next**. 12. For the **Review and create** step, review the job's configuration
settings and verify that they're correct.

You can also review the total estimated cost (in US dollars) of running the job. The
estimate can help you determine whether to adjust the job's settings before you
save the job. To learn more, see [Forecasting the cost of a sensitive data
discovery job](discovery-jobs-costs.md#discovery-jobs-costs-forecast "discovery-jobs-costs.md#discovery-jobs-costs-forecast"). 13. When you finish reviewing and verifying the job's settings, choose
**Submit**.

Macie immediately starts running the job. To learn how to monitor the job, see [checking the status of
sensitive data discovery jobs](discovery-jobs-status-check.md "discovery-jobs-status-check.md").

## Step 5: Review findings

Amazon Macie automatically monitors your S3 general purpose buckets for security and access
control, and it creates policy findings to report potential issues with the security or
privacy of the buckets. If you run a sensitive data discovery job or configure Macie to
perform automated sensitive data discovery, Macie creates sensitive data findings to report sensitive data that
it detects in S3 objects.

Follow these steps to review findings.

###### To review findings

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Findings**. The
   **Findings** page displays findings for your account in the
   current AWS Region.
3. To filter the findings by specific criteria, enter the criteria in the filter box above
   the table.
4. To review the details of a particular finding, choose the finding. The details panel
   displays the finding's details.

To learn more about findings, including how to group and filter them, see [Reviewing and analyzing findings](findings.md "findings.md").
