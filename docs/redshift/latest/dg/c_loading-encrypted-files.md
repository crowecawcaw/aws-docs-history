Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading encrypted data files from

Amazon S3

You can use the COPY command to load data files that were uploaded to Amazon S3
using server-side encryption, client-side encryption, or both.

The COPY command supports the following types of Amazon S3 encryption:

- Server-side encryption with Amazon S3-managed keys (SSE-S3)
- Server-side encryption with AWS KMS keys (SSE-KMS)
- Client-side encryption using a client-side symmetric root key
  The COPY command doesn't support the following types of Amazon S3
  encryption:

- Server-side encryption with customer-provided keys (SSE-C)
- Client-side encryption using an AWS KMS key
- Client-side encryption using a customer-provided asymmetric root
  key
  For more information about Amazon S3 encryption, see [Protecting Data Using Server-Side
  Encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") and [Protecting Data Using Client-Side Encryption](../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md "../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md") in the
  Amazon Simple Storage Service User Guide.

The [UNLOAD](r_UNLOAD.md "r_UNLOAD.md") command automatically
encrypts files using SSE-S3. You can also unload using SSE-KMS or client-side
encryption with a customer managed symmetric key. For more information, see [Unloading encrypted data files](t_unloading_encrypted_files.md "t_unloading_encrypted_files.md")

The COPY command automatically recognizes and loads files encrypted using
SSE-S3 and SSE-KMS. You can load files encrypted using a client-side symmetric
root key by specifying the ENCRYPTED option and providing the key value. For
more information, see [Uploading encrypted data to
Amazon S3](t_uploading-encrypted-data.md "t_uploading-encrypted-data.md").

To load client-side encrypted data files, provide the root key value using
the MASTER_SYMMETRIC_KEY parameter and include the ENCRYPTED option.

```
COPY customer FROM 's3://amzn-s3-demo-bucket/encrypted/customer'
IAM_ROLE 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
MASTER_SYMMETRIC_KEY '`<root_key>`'
ENCRYPTED
DELIMITER '|';
```

To load encrypted data files that are gzip, lzop, or bzip2 compressed, include
the GZIP, LZOP, or BZIP2 option along with the root key value and the ENCRYPTED
option.

```
COPY customer FROM 's3://amzn-s3-demo-bucket/encrypted/customer'
IAM_ROLE 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
MASTER_SYMMETRIC_KEY '`<root_key>`'
ENCRYPTED
DELIMITER '|'
GZIP;
```
