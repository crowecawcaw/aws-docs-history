Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations for data sharing with

data lake tables in Amazon Redshift

The following are considerations when working with data lake tables in
Amazon Redshift:

- Data sharing of data lake tables does not support customer managed
  AWS KMS keys for Amazon S3 bucket encryption. You can use AWS managed keys for
  encryption. For more information, see [Using
  server-side encryption with Amazon S3 managed keys (SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md") .
- To data share data lake tables from an encrypted AWS Glue catalog,
  you must delegate AWS KMS operations to an IAM role by following the instructions
  in [Encrypting your Data Catalog](../../../glue/latest/dg/encrypt-glue-data-catalog.md "../../../glue/latest/dg/encrypt-glue-data-catalog.md").
- External tables that explicitly specify manifest files in the `LOCATION`
  clause aren't supported for data sharing. This includes the following tables
  that Amazon Redshift Spectrum supports:
  - Delta Lake
  - Hudi
