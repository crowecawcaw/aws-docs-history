# Accessing discovery results from

automated sensitive data discovery

When Amazon Macie performs automated sensitive data discovery, it creates an analysis record for each Amazon Simple Storage Service (Amazon S3)
object that it selects for analysis. These records, referred to as _sensitive data discovery results_, log details about the analysis that Macie performs on individual S3
objects. This includes objects that Macie doesn't find sensitive data in, and objects that Macie
can't analyze due to errors or issues such as permissions settings or use of an unsupported file
or storage format. Sensitive data discovery results provide you with analysis records that can be
helpful for data privacy and protection audits or investigations.

If Macie finds sensitive data in an S3 object, the sensitive data discovery result provides information about the
sensitive data that Macie found. The information includes the same types of details that a
sensitive data finding provides. It provides additional information too, such as the location of
as many as 1,000 occurrences of each type of sensitive data that Macie found. For example:

- The column and row number for a cell or field in a Microsoft Excel workbook, CSV file, or
  TSV file
- The path to a field or array in a JSON or JSON Lines file
- The line number for a line in a non-binary text file other than a CSV, JSON, JSON Lines,
  or TSV file—for example, an HTML, TXT, or XML file
- The page number for a page in an Adobe Portable Document Format (PDF) file
- The record index and the path to a field in a record in an Apache Avro object container or
  Apache Parquet file
  If the affected S3 object is an archive file, such as a .tar or .zip file, the sensitive
  data discovery result also provides detailed location data for occurrences of sensitive data in
  individual files that Macie extracted from the archive. Macie doesn’t include this information in
  sensitive data findings for archive files. To report location data, sensitive data discovery
  results use a [standardized JSON schema](findings-locate-sd-schema.md "findings-locate-sd-schema.md").

###### Note

As is the case with sensitive data findings, sensitive data discovery results don't include sensitive data that
Macie finds in S3 objects. Instead, they provide analysis details that can be helpful for audits
or investigations.

Macie stores your sensitive data discovery results for 90 days. You can’t access them directly on the Amazon Macie
console or with the Amazon Macie API. Instead, you configure Macie to encrypt and store them in an
S3 bucket. The bucket can serve as a definitive, long-term repository for all of your
sensitive data discovery results. To determine where this repository is for your account, choose **Discovery
results** in the navigation pane on the Amazon Macie console. To do this programmatically,
use the [GetClassificationExportConfiguration](../APIReference/classification-export-configuration.md "../APIReference/classification-export-configuration.md") operation of the Amazon Macie API. If you haven't
configured this repository for your account, see [Storing and retaining
sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md") to learn how.

After you configure Macie to store your sensitive data discovery results in an S3 bucket, Macie writes the
results to JSON Lines (.jsonl) files, and it encrypts and adds those files to the bucket as GNU
Zip (.gz) files. For automated sensitive data discovery, Macie adds the files to a folder named
`automated-sensitive-data-discovery` in the bucket. You can then optionally access
and query the results in that folder. If your account is part of an organization that centrally
manages multiple Macie accounts, Macie adds the files to the
`automated-sensitive-data-discovery` folder in the bucket for your Macie
administrator's account.

Sensitive data discovery results adhere to a standardized schema. This can help you query,
monitor, and process them by using other applications, services, and systems. For a detailed,
instructional example of how you might query and use these results, see the following blog post
on the _AWS Security Blog_: [How to query and visualize Macie sensitive data discovery results with Amazon Athena and Amazon Quick Suite](https://aws.amazon.com/blogs/security/how-to-query-and-visualize-macie-sensitive-data-discovery-results-with-athena-and-quicksight/ "https://aws.amazon.com/blogs/security/how-to-query-and-visualize-macie-sensitive-data-discovery-results-with-athena-and-quicksight/"). For samples
of Athena queries that you can use to analyze the results, visit the [Amazon Macie Results Analytics
repository](https://github.com/aws-samples/amazon-macie-results-analytics "https://github.com/aws-samples/amazon-macie-results-analytics") on GitHub. This repository also provides instructions for configuring Athena
to retrieve and decrypt your results, and scripts for creating tables for the results.
