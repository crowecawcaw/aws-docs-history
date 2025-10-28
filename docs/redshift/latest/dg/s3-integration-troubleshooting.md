Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Troubleshooting S3 event integration and COPY JOB errors

Use the following information to troubleshoot common issues with Amazon S3 event integrations and COPY JOB with Amazon Redshift.

## Creation of the S3 event integration failed

If the creation of the S3 event integration failed, the status of the integration is `Inactive`. Make sure that the following are correct for your
Amazon Redshift data warehouse.

- You added the correct authorized principal and integration source for your target namespace in Amazon Redshift. See
  [Prerequisites to creating an S3 event integration](loading-data-copy-job.md#loading-data-copy-job-prerequisites "loading-data-copy-job.md#loading-data-copy-job-prerequisites").
- You added the correct resource-based policy to the source Amazon S3 bucket. See
  [Prerequisites to creating an S3 event integration](loading-data-copy-job.md#loading-data-copy-job-prerequisites "loading-data-copy-job.md#loading-data-copy-job-prerequisites").

## Your Amazon S3 data is not appearing in the target database

If data from a COPY JOB doesn't appear, check the following.

- Query SYS_COPY_JOB_DETAIL to view if the Amazon S3 file has been loaded, whether its pending ingestion, or there is an error. For more information, see
  [SYS_COPY_JOB_DETAIL](SYS_COPY_JOB_DETAIL.md "SYS_COPY_JOB_DETAIL.md").
- Consult STL_ERROR or SYS_COPY_JOB_INFO if the Amazon S3 file is not there or there is unexpected wait time.
  Look for credential errors or anything that suggests the integration is inactive. For more information, see
  [STL_ERROR](r_STL_ERROR.md "r_STL_ERROR.md") and [SYS_COPY_JOB_INFO](SYS_COPY_JOB_INFO.md "SYS_COPY_JOB_INFO.md").
