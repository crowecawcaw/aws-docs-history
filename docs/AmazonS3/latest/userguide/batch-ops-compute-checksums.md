# Compute checksums

You can use S3 Batch Operations with the **Compute checksum** operation to
perform checksum calculations for objects stored in Amazon S3 at rest. The
**Compute checksum** operation calculates object checksums which you
can use to validate data integrity without downloading or restoring objects for stored data.
You can use the **Compute checksum** operation to calculate checksums for
both composite and full object checksum types, for all supported checksum algorithms.

With the **Compute checksum** operation, you can process billions of
objects through a single job request. This batch operation is compatible with all S3 storage
classes, regardless of object size. To create a **Compute checksum** job,
use the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the AWS SDKs, or the Amazon S3 REST API.

When you [enable server access logging](ServerLogs.md "ServerLogs.md"), you can also receive log entries about your
**Compute checksum** job. The **Compute checksum**
job operation emits separate server access log events after completing the checksum
computations. These log entries follow the standard [S3 server access logging format](LogFormat.md "LogFormat.md")
and include fields such as operation type, timestamp, [error codes](../API/ErrorResponses.md#ErrorCodeList "../API/ErrorResponses.md#ErrorCodeList"), and the
associated **Compute checksum** job ID. This logging provides an audit
trail of checksum verification activities performed on your objects, helping you track and
verify data integrity operations.

###### Note

The **Compute checksum** operation doesn’t support server-side encryption with customer-provided encryption keys (SSE-C)
encrypted objects. However, you can use the **Compute checksum**
operation with objects that are encrypted by using [server-side encryption with
S3 managed keys (SSE-S3)](UsingKMSEncryption.md "UsingKMSEncryption.md"), server-side encryption with AWS Key Management Service (DSSE-KMS).
Make sure that you’ve [granted the
proper AWS KMS permissions](UsingKMSEncryption.md#require-sse-kms "UsingKMSEncryption.md#require-sse-kms") to perform the
**Compute checksum** operation.

To get started with the **Compute checksum** operation using Batch Operations,
you can either:

- Manually create a new manifest file.
- Use an existing manifest.
- Direct Batch Operations to automatically generate a manifest based on object filter
  criteria that you [specify when you create your job](batch-ops-create-job.md#specify-batchjob-manifest "batch-ops-create-job.md#specify-batchjob-manifest").
  Then, submit your **Compute checksum** job request and monitor its
  status. After the **Compute checksum** job finishes, you automatically
  receive a completion report in the specified destination bucket. This completion report
  contains checksum information for every object in the bucket, allowing you to verify data
  consistency. For more information about how to use this report to examine the job, see
  [Tracking job status and completion reports](batch-ops-job-status.md "batch-ops-job-status.md").

For more information about **Compute checksum** capabilities and how to
use **Compute checksum** in the console, see [Checking object integrity for data at
rest in Amazon S3](checking-object-integrity-at-rest.md "checking-object-integrity-at-rest.md"). For information about how to send
REST requests to **Compute checksum**, see [DescribeJob](../API/API_control_DescribeJob.md "../API/API_control_DescribeJob.md") and [CreateJob](../API/API_control_CreateJob.md "../API/API_control_CreateJob.md") in
the _Amazon S3 API Reference_.

The following sections explain how you can get started using the
**Compute checksum** operation with S3 Batch Operations.

###### Topics

- [S3 Batch Operations
  Compute checksum considerations](#batch-ops-compute-checksum-considerations "#batch-ops-compute-checksum-considerations")
- [S3 Batch Operations completion
  report](#batch-ops-compute-checksum-completion-report "#batch-ops-compute-checksum-completion-report")

## S3 Batch Operations

**Compute checksum** considerations

Before using the **Compute checksum** operation, review the
following list of considerations:

- If your manifest includes a version ID field, you must provide a version ID
  for all objects in the manifest. If the version ID isn’t specified, the
  **Compute checksum** request performs the operation on the
  latest version of the object.
- To receive **Compute checksum** operation details in your
  [server access logs](ServerLogs.md "ServerLogs.md"), you must first [enable
  server access logging](enable-server-access-logging.md "enable-server-access-logging.md") on the source bucket and specify a destination
  bucket to store the logs. The destination bucket must also exist in the same
  AWS Region and AWS account as the source bucket. After configuring server
  access logging, the **Compute checksum** operation generates
  [log
  records](LogFormat.md#log-record-fields "LogFormat.md#log-record-fields") that include standard fields such as operation type, HTTP
  status code, [S3 error codes](../API/ErrorResponses.md#ErrorCodeList "../API/ErrorResponses.md#ErrorCodeList"), timestamps, and the associated
  **Compute checksum** job ID. The
  **Compute checksum** operation runs asynchronously. As a
  result, the [log
  entries](LogFormat.md#log-record-fields "LogFormat.md#log-record-fields") use a **Compute checksum** job ID, rather
  than a request ID, in its log entries.
- The report generation can take up to a few hours for stored objects.
- For the following S3 Glacier storage classes, the
  **Compute checksum** job can take up to a week to
  finish:
  - S3 Glacier Flexible Retrieval
  - S3 Glacier Deep Archive

- For buckets where the completion report will be written, you must use the
  [bucket owner condition](bucket-owner-condition.md#bucket-owner-condition-when-to-use "bucket-owner-condition.md#bucket-owner-condition-when-to-use") when running the
  **Compute checksum** operation. If the actual bucket owner
  doesn't match the expected bucket owner for the submitted job request, then the
  job fails. For a list of S3 operations that don't support bucket owner
  condition, see [Restrictions and limitations](bucket-owner-condition.md#bucket-owner-condition-restrictions-limitations "bucket-owner-condition.md#bucket-owner-condition-restrictions-limitations").

## S3 Batch Operations completion

report

When you create a **Compute checksum** job, you can request an
S3 Batch Operations completion report. This CSV file shows the objects, success or failure
codes, outputs, and descriptions. For more information about job tracking and completion
reports, see [Completion reports](batch-ops-job-status.md#batch-ops-completion-report "batch-ops-job-status.md#batch-ops-completion-report").
