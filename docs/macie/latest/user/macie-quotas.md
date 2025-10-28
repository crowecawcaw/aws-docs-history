# Quotas for Macie

Your AWS account has certain default quotas, formerly referred to as _limits_, for each AWS service. These quotas are the maximum
number of service resources or operations for your account. This topic lists the quotas that
apply to Amazon Macie resources and operations for your account. Unless otherwise noted, each
quota applies to your account in each AWS Region.

Some quotas can be increased, while others cannot. To request an increase to a quota, use the
[Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). To learn how to
request an increase, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_. If a quota isn't available
on the Service Quotas console, use the [service limit increase
form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase") on the AWS Support Center Console to request an increase to the quota.

###### Findings

- Filter rules and suppression rules per account: 1,000
- Findings per run of a sensitive data discovery job: 100,000 + 5% of any remaining findings
  after the 100,000 threshold is met

This quota applies only to the Amazon Macie console and the Amazon Macie API. There
isn't a quota for the number of finding events that Macie publishes to Amazon EventBridge or
the number of sensitive data discovery results that Macie creates for each run of a
job.

- Detection locations per sensitive data finding: 15
- Requests to retrieve and reveal sensitive data samples from an Amazon S3 object: 100 per
  day

This quota resets every 24 hours at 00:00:01 UTC+0.

- Size of an Amazon S3 object to retrieve and reveal sensitive data samples from:

      + Apache Avro object container (.avro) file: 70 MB
      + Apache Parquet (.parquet) file: 100 MB
      + CSV (.csv) file: 255 MB
      + GNU Zip compressed archive (.gz or .gzip) file: 90 MB
      + JSON or JSON Lines (.json or .jsonl) file: 25 MB
      + Microsoft Excel workbook (.xlsx) file: 20 MB
      + Non-binary text (*text/plain*) file: 100 MB
      + TSV (.tsv) file: 75 MB
      + ZIP compressed archive (.zip) file: 355 MB

  If a finding applies to an archive file that generates multiple .gz files for the
  corresponding [sensitive data
  discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md"), sensitive data samples can't be retrieved and revealed
  from the archive file.

###### Organizations

- Member accounts by invitation: 1,000
- Member accounts through AWS Organizations: 10,000

###### Preventative control monitoring

- S3 buckets per account: 10,000

If your account exceeds this quota, Macie provides full monitoring functionality for the
10,000 buckets that were most recently created or changed. For all other buckets,
Macie doesn't evaluate or monitor the buckets for security and access control,
generate policy findings, or maintain complete inventory data.

###### Sensitive data discovery

- Monthly analysis per account by sensitive data discovery jobs: 5 TB

This quota applies only to sensitive data discovery jobs. To increase the quota to
as much as 1,000 TB (1 PB), use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). To request an increase for more than 1 PB, use the
[service limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase") on the
AWS Support Center Console.

- Custom data identifiers per account: 10,000
- Allow lists per account: 10, 1–5 allow lists that specify predefined text
  and 1–5 allow lists that specify regular expressions

Additional quotas apply to an allow list that specifies predefined text. The list
can't contain more than 100,000 entries and the storage size of the list can't
exceed 35 MB.

- S3 buckets to exclude from automated sensitive data discovery: 1,000

If your account is the Macie administrator account for an organization, this quota applies to
your organization overall.

- S3 buckets per sensitive data discovery job: 1,000

This quota doesn't apply to jobs that use runtime bucket criteria to determine which
buckets to analyze. It applies to a job only if you configure the job to analyze
specific buckets that you select. If your account is the Macie administrator account for an
organization, you can select as many as 1,000 buckets spanning as many as 1,000
accounts in your organization.

- Custom data identifiers per sensitive data discovery job: 30
- Allow lists per sensitive data discovery job: 10, 1–5 allow lists that
  specify predefined text and 1–5 allow lists that specify regular
  expressions
- [CreateClassificationJob](../APIReference/jobs.md "../APIReference/jobs.md") operation: 0.1 requests per second
- Time to analyze an individual file: 10 hours
- Size of an individual file to analyze:

      + Adobe Portable Document Format (.pdf) file: 1,024 MB
      + Apache Avro object container (.avro) file: 8 GB
      + Apache Parquet (.parquet) file: 8 GB
      + Email message (.eml) file: 20 GB
      + GNU Zip compressed archive (.gz or .gzip) file: 8 GB
      + Microsoft Excel workbook (.xls or .xlsx) file: 512 MB
      + Microsoft Word document (.doc or .docx) file: 512 MB
      + Non-binary text file: 20 GB
      + TAR archive (.tar) file: 20 GB
      + ZIP compressed archive (.zip) file: 8 GB

  If a file is larger than the applicable quota, Macie doesn't analyze any data in
  the file.

- Extraction and analysis of data in a compressed or archive file:

      + Storage size (compressed): 8 GB for a GNU Zip compressed archive (.gz or
       .gzip) file or ZIP compressed archive (.zip) file; 20 GB for a TAR archive
       (.tar) file
      + Nested archive depth: 10 levels
      + Extracted files: 1,000,000
      + Extracted bytes: 10 GB of uncompressed data overall. 3 GB of uncompressed
       data for each extracted file that uses a [supported file type or storage
       format](discovery-supported-storage.md#discovery-supported-formats "discovery-supported-storage.md#discovery-supported-formats").

  If the metadata for a compressed or archive file indicates that the file contains more than
  10 nested levels or exceeds the applicable quota for storage size or extracted
  bytes, Macie doesn't extract or analyze any data in the file. If Macie begins to
  extract and analyze data in a compressed or archive file and subsequently determines
  that the file contains more than 1,000,000 files or exceeds the quota for extracted
  bytes, Macie stops analyzing data in the file and creates sensitive data findings
  and discovery results only for the data that was processed.

- Analysis of nested elements in structured data: 256 levels per file

This quota applies only to JSON (.json) and JSON Lines (.jsonl) files. If the
nested depth of either type of file exceeds this quota, Macie doesn't analyze any
data in the file.

- Detection locations per sensitive data discovery result: 1,000 per sensitive data
  detection type
- Detection of full names: 1,000 per file, including archive files

After Macie detects the first 1,000 occurrences of full names in a file, Macie
stops incrementing the count and reporting location data for full names.

- Detection of mailing addresses: 1,000 per file, including archive files

After Macie detects the first 1,000 occurrences of mailing addresses in a file,
Macie stops incrementing the count and reporting location data for mailing
addresses.
