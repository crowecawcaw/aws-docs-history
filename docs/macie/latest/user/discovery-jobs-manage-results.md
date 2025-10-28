# Reviewing the results of a sensitive data

discovery job

When you run a sensitive data discovery job, Amazon Macie automatically calculates and reports
certain statistical data for the job. For example, Macie reports the number of times that
the job has run, and the approximate number of Amazon Simple Storage Service (Amazon S3) objects that the job has yet
to process during its current run. Macie also produces several types of results for the job:
_log events_, _sensitive data
findings_, and _sensitive data discovery
results_.

###### Topics

- [Types of job
  results](#discovery-jobs-manage-results-types "#discovery-jobs-manage-results-types")
- [Reviewing job statistics and
  results](#discovery-jobs-manage-results-review "#discovery-jobs-manage-results-review")

## Types of results for sensitive

data discovery jobs

As a sensitive data discovery job progresses, Amazon Macie produces the following types
of results for the job.

Log event

This is a record of an event that occurred while the job was running.
Macie automatically logs and publishes data for certain events to Amazon CloudWatch Logs.
The data in these logs provides a record of changes to the job's progress or
status, such as the exact date and time when the job started or stopped
running. The data also provides details about any account- or bucket-level
errors that occurred while the job ran.

Log events can help you monitor a job and address any issues that
prevented the job from analyzing the data that you want. If a job uses
runtime criteria to determine which S3 buckets to analyze, log events can
also help you determine whether and which S3 buckets matched the criteria
when the job ran.

You can access log events by using the Amazon CloudWatch console or the Amazon CloudWatch Logs
API. To help you navigate to the log events for a job, the Amazon Macie console
provides a link to them. For more information, see [Monitoring jobs with
CloudWatch Logs](discovery-jobs-monitor-cw-logs.md "discovery-jobs-monitor-cw-logs.md").

Sensitive data finding

This is a report of sensitive data that Macie found in an S3 object. Each
finding provides a severity rating and details such as:

- The date and time when Macie found the sensitive data.
- The category and types of sensitive data that Macie found.
- The number of occurrences of each type of sensitive data that
  Macie found.
- The unique identifier for the job that produced the
  finding.
- The name, public access settings, encryption type, and other
  information about the affected S3 bucket and object.

Depending on the affected S3 object's file type or storage format, the details can also
include the location of as many as 15 occurrences of the sensitive data that
Macie found. To report location data, sensitive data findings use a [standardized JSON
schema](findings-locate-sd-schema.md "findings-locate-sd-schema.md").

A sensitive data finding doesn't include the sensitive data that Macie
found. Instead, it provides information that you can use for further
investigation and remediation as necessary.

Macie stores sensitive data findings for 90 days. You can access them by
using the Amazon Macie console or the Amazon Macie API. You can also monitor and
process them by using other applications, services, and systems. For more
information, see [Reviewing and analyzing findings](findings.md "findings.md").

Sensitive data discovery result

This is a record that logs details about the analysis of an S3 object. Macie
automatically creates a sensitive data discovery result for each object that you configure a job to
analyze. This includes objects that Macie doesn't find sensitive data in,
and therefore don't produce sensitive data findings, and objects that Macie
can't analyze due to errors or issues such as permissions settings or use of
an unsupported file or storage format.

If Macie finds sensitive data in an S3 object, the sensitive data discovery result includes data from the
corresponding sensitive data finding. It provides additional information
too, such as the location of as many as 1,000 occurrences of each type of
sensitive data that Macie found in the object. For example:

- The column and row number for a cell or field in a Microsoft Excel
  workbook, CSV file, or TSV file
- The path to a field or array in a JSON or JSON Lines file
- The line number for a line in a non-binary text file other than a
  CSV, JSON, JSON Lines, or TSV file—for example, an HTML, TXT,
  or XML file
- The page number for a page in an Adobe Portable Document Format
  (PDF) file
- The record index and the path to a field in a record in an Apache
  Avro object container or Apache Parquet file

If the affected S3 object is an archive file, such as a .tar or .zip file, the sensitive data discovery result
also provides detailed location data for occurrences of sensitive data in
individual files that Macie extracted from the archive. Macie doesn’t
include this information in sensitive data findings for archive files. To
report location data, sensitive data discovery results use a [standardized JSON
schema](findings-locate-sd-schema.md "findings-locate-sd-schema.md").

A sensitive data discovery result doesn't include the sensitive data that Macie found. Instead, it provides you
with an analysis record that can be helpful for data privacy and protection
audits or investigations.

Macie stores your sensitive data discovery results for 90 days. You can’t access them directly on the
Amazon Macie console or with the Amazon Macie API. Instead, you configure Macie to
encrypt and store them in an S3 bucket. The bucket can serve as a
definitive, long-term repository for all of your sensitive data discovery results. You can then
optionally access and query the results in that repository. To learn how to
configure these settings, see [Storing and retaining
sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md").

After you configure the settings, Macie writes your sensitive data discovery results to JSON
Lines (.jsonl) files, and it encrypts and adds those files to the S3 bucket
as GNU Zip (.gz) files. To help you navigate to the results, the Amazon Macie
console provides links to them.

Sensitive data findings and sensitive data discovery results both adhere to standardized schemas. This can help
you optionally query, monitor, and process them by using other applications, services,
and systems.

###### Tips

For a detailed, instructional example of how you might query and use sensitive data discovery results to
analyze and report potential data security risks, see the following blog post on the
_AWS Security Blog_: [How to query and visualize Macie sensitive data discovery results with Amazon Athena and
Amazon Quick Suite](https://aws.amazon.com/blogs/security/how-to-query-and-visualize-macie-sensitive-data-discovery-results-with-athena-and-quicksight/ "https://aws.amazon.com/blogs/security/how-to-query-and-visualize-macie-sensitive-data-discovery-results-with-athena-and-quicksight/").

For samples of Amazon Athena queries that you can use to analyze sensitive data discovery results, visit
the [Amazon Macie Results Analytics repository](https://github.com/aws-samples/amazon-macie-results-analytics "https://github.com/aws-samples/amazon-macie-results-analytics") on GitHub. This repository also
provides instructions for configuring Athena to retrieve and decrypt your results,
and scripts for creating tables for the results.

## Reviewing statistics and results for a

sensitive data discovery job

To review processing statistics and the results of a sensitive data discovery job, you can
use the Amazon Macie console or the Amazon Macie API. Follow these steps to review the
statistics and results by using the console.

To access a job's processing statistics programmatically, use the [DescribeClassificationJob](../APIReference/jobs-jobid.md "../APIReference/jobs-jobid.md") operation of the Amazon Macie API. For programmatic
access to the findings that a job produced, use the [ListFindings](../APIReference/findings.md "../APIReference/findings.md") operation and
specify the job's unique identifier in a filter condition for the
`classificationDetails.jobId` field. To learn how, see [Creating and applying filters to Macie
findings](findings-filter-procedure.md "findings-filter-procedure.md"). You
can then use the [GetFindings](../APIReference/findings-describe.md "../APIReference/findings-describe.md") operation
to retrieve the details of the findings.

###### To review statistics and results for a job

1.  Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2.  In the navigation pane, choose **Jobs**.
3.  On the **Jobs** page, choose the name of the job whose
    statistics and results you want to review. The details panel displays
    statistics, settings, and other information about the job.
4.  In the details panel, do any of the following:
    - To review processing statistics for the job, refer to the
      **Statistics** section of the panel. This section
      displays statistics such as the number of times that the job has run,
      and the approximate number of objects that the job has yet to process
      during its current run.
    - To review log events for the job, choose **Show
      results** at the top of the panel, and then choose
      **Show CloudWatch logs**. Macie opens the Amazon CloudWatch
      console and displays a table of the log events that Macie published for
      the job.
    - To review all the sensitive data findings that the job produced, choose **Show
      results** at the top of the panel, and then choose
      **Show findings**. Macie opens the
      **Findings** page and displays all the findings
      from the job. To review the details of a particular finding, choose the
      finding, and then refer to the details panel.

    ###### Tip

    In the finding details panel, you can use the link in the **Detailed result
    location** field to navigate to the corresponding
    sensitive data discovery result in Amazon S3:

        + If the finding applies to a large archive or compressed
         file, the link displays the folder that contains the
         discovery results for the file. An archive or compressed
         file is *large* if it
         generates more than 100 discovery results.
        + If the finding applies to a small archive or compressed
         file, the link displays the file that contains the discovery
         results for the file. An archive or compressed file is
         *small* if it generates
         100 or fewer discovery results.
        + If the finding applies to another type of file, the link
         displays the file that contains the discovery results for
         the file.

    - To review all the sensitive data discovery results that the job produced, choose **Show
      results** at the top of the panel, and then choose
      **Show classifications**. Macie opens the Amazon S3
      console and displays the folder that contains all the discovery results
      for the job. This option is available only after you configure Macie to
      [store your sensitive
      data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md") in an S3 bucket.
