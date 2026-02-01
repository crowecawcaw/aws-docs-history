Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Uploading files to Amazon S3 to use with COPY

There are a couple approaches to take when uploading text files to Amazon S3:

- If you have compressed files, we recommend that you split large files to take advantage of parallel processing in Amazon Redshift.
- On the other hand, COPY automatically splits large, uncompressed, text-delimited file data to facilitate parallelism and effectively distribute the data from large files.
  Create an Amazon S3 bucket to hold your data files, and then upload the data files to
  the bucket. For information about creating buckets and uploading files, see [Working with Amazon S3 Buckets](../../../AmazonS3/latest/userguide/UsingBucket.md "../../../AmazonS3/latest/userguide/UsingBucket.md") in the
  _Amazon Simple Storage Service User Guide._

###### Important

The Amazon S3 bucket that holds the data files must be created in the same AWS
Region as your cluster unless you use the [REGION](copy-parameters-data-source-s3.md#copy-region "copy-parameters-data-source-s3.md#copy-region") option to
specify the Region in which the Amazon S3 bucket is located.

Ensure that the S3 IP ranges are added to your allowlist. To learn more about the
required S3 IP ranges, see [Network isolation](../mgmt/security-network-isolation.md#network-isolation "../mgmt/security-network-isolation.md#network-isolation").

You can create an Amazon S3 bucket in a specific Region either by selecting the Region
when you create the bucket by using the Amazon S3 console, or by specifying an endpoint
when you create the bucket using the Amazon S3 API or CLI.

Following the data load, verify that the correct files are present on Amazon S3.

###### Topics

- [Managing data consistency](managing-data-consistency.md "managing-data-consistency.md")
- [Uploading encrypted data to
  Amazon S3](t_uploading-encrypted-data.md "t_uploading-encrypted-data.md")
- [Verifying that the
  correct files are present in your bucket](verifying-that-correct-files-are-present.md "verifying-that-correct-files-are-present.md")
