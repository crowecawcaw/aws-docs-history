Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Troubleshooting data loads

When you load data into Amazon Redshift tables you might encounter errors from Amazon S3, invalid input data, and COPY command errors.
The following sections provide information about identifying and resolving data load errors.

###### Topics

- [Troubleshooting S3 event integration and COPY JOB errors](s3-integration-troubleshooting.md "s3-integration-troubleshooting.md")
- [S3ServiceException errors](s3serviceexception-error.md "s3serviceexception-error.md")
- [System tables for
  troubleshooting data loads](system-tables-for-troubleshooting-data-loads.md "system-tables-for-troubleshooting-data-loads.md")
- [Multibyte character load
  errors](multi-byte-character-load-errors.md "multi-byte-character-load-errors.md")
- [Load error reference](r_Load_Error_Reference.md "r_Load_Error_Reference.md")
