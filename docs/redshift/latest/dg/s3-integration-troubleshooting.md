

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Troubleshooting S3 event integration and COPY JOB errors
<a name="s3-integration-troubleshooting"></a>

Use the following information to troubleshoot common issues with Amazon S3 event integrations and COPY JOB with Amazon Redshift.

## Creation of the S3 event integration failed
<a name="s3-integration-troubleshooting-creation"></a>

If the creation of the S3 event integration failed, the status of the integration is `Inactive`. Make sure that the following are correct for your Amazon Redshift data warehouse.
+ You added the correct authorized principal and integration source for your target namespace in Amazon Redshift. See [Prerequisites to creating an S3 event integration](loading-data-copy-job.md#loading-data-copy-job-prerequisites).
+ You added the correct resource-based policy to the source Amazon S3 bucket. See [Prerequisites to creating an S3 event integration](loading-data-copy-job.md#loading-data-copy-job-prerequisites).

## Your Amazon S3 data is not appearing in the target database
<a name="s3-integration-troubleshooting-missing-data"></a>

If data from a COPY JOB doesn't appear, check the following.
+ Query SYS\_COPY\_JOB\_DETAIL to view if the Amazon S3 file has been loaded, whether its pending ingestion, or there is an error. For more information, see [SYS\_COPY\_JOB\_DETAIL](SYS_COPY_JOB_DETAIL.md).
+ Consult STL\_ERROR or SYS\_COPY\_JOB\_INFO if the Amazon S3 file is not there or there is unexpected wait time. Look for credential errors or anything that suggests the integration is inactive. For more information, see [STL\_ERROR](r_STL_ERROR.md) and [SYS\_COPY\_JOB\_INFO](SYS_COPY_JOB_INFO.md).