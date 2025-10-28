# Configure a location for Amazon EMR cluster output

The most common output format of an Amazon EMR cluster is as text files, either compressed or uncompressed. Typically, these are written to an Amazon S3 bucket. This bucket must be created before you launch the cluster. You specify the S3 bucket as the output location when you launch the cluster.

For more information, see the following topics:

###### Topics

- [Create and configure an Amazon S3 bucket](#create-s3-bucket-output "#create-s3-bucket-output")
- [What formats can Amazon EMR return?](emr-plan-output-formats.md "emr-plan-output-formats.md")
- [How to write data to an Amazon S3 bucket you don't own with Amazon EMR](emr-s3-acls.md "emr-s3-acls.md")
- [Ways to compress the output of your Amazon EMR cluster](emr-plan-output-compression.md "emr-plan-output-compression.md")

## Create and configure an Amazon S3 bucket

Amazon EMR (Amazon EMR) uses Amazon S3 to store input data, log files, and output data. Amazon
S3 refers to these storage locations as _buckets_. Buckets have certain restrictions
and limitations to conform with Amazon S3 and DNS requirements. For more information, go to [Bucket Restrictions and Limitations](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md") in the _Amazon Simple Storage
Service Developers Guide_.

To create a an Amazon S3 bucket, follow the instructions on the [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") page in the _Amazon Simple Storage
Service Developers Guide_.

###### Note

If you enable logging in the **Create a Bucket** wizard, it
enables only bucket access logs, not cluster logs.

###### Note

For more information on specifying Region-specific buckets, refer to [Buckets and Regions](../../../AmazonS3/latest/dev/LocationSelection.md "../../../AmazonS3/latest/dev/LocationSelection.md") in the _Amazon Simple Storage Service
Developer Guide_ and [Available Region Endpoints for the AWS SDKs](https://aws.amazon.com/articles/available-region-endpoints-for-the-aws-sdks/ "https://aws.amazon.com/articles/available-region-endpoints-for-the-aws-sdks/") .

After you create your bucket you can set the appropriate permissions on it.
Typically, you give yourself (the owner) read and write access.
We strongly recommend that you follow [Security Best Practices for Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md") when configuring your bucket.

Required Amazon S3 buckets must exist before you can create a cluster. You must upload
any required scripts or data referenced in the cluster to Amazon S3. The following table
describes example data, scripts, and log file locations.

| Information       | Example Location on Amazon S3                      |
| ----------------- | -------------------------------------------------- |
| script or program | `s3://amzn-s3-demo-bucket1/script/MapperScript.py` |
| log files         | `s3://amzn-s3-demo-bucket1/logs`                   |
| input data        | `s3://amzn-s3-demo-bucket1/input`                  |
| output data       | `s3://amzn-s3-demo-bucket1/output`                 |
