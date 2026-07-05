Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Managing data consistency

Amazon S3 provides strong read-after-write consistency for COPY, UNLOAD, INSERT (external table), CREATE EXTERNAL TABLE AS, and Amazon Redshift Spectrum operations on Amazon S3 buckets in all AWS Regions. In addition, read operations on Amazon S3 Select, Amazon S3 Access Control Lists, Amazon S3 Object Tags, and object metadata (for example, HEAD object) are strongly consistent. For more information about data consistency, see [Amazon S3 Data Consistency
Model](../../../AmazonS3/latest/userguide/Introduction.md#ConsistencyModel "../../../AmazonS3/latest/userguide/Introduction.md#ConsistencyModel") in the _Amazon Simple Storage Service User Guide_.
