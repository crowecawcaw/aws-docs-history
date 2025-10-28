# Protect Data at Rest Using Encryption

Amazon SageMaker AI automatically encrypts your data using an AWS managed key for Amazon S3 (SSE-S3) by
default for the following features: Studio notebooks, notebook instances, model-building data,
model artifacts, and output from Training, Batch Transform, and Processing jobs.

For cross-account access, you must specify your own customer managed key when creating SageMaker AI
resources, as the default AWS managed key for Amazon S3 can't be shared across accounts. For
data output to Amazon S3 Express One Zone, the data is encrypted using server-side encryption with Amazon S3
managed keys (SSE-S3). Additionally, data output to Amazon S3 directory buckets can't be
encrypted with server-side encryption using AWS Key Management Service keys (SSE-KMS). For more information
on AWS KMS, see [What
is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")

###### Topics

- [Studio notebooks](encryption-at-rest-studio.md "encryption-at-rest-studio.md")
- [Notebook instances, SageMaker AI jobs, and
  Endpoints](encryption-at-rest-nbi.md "encryption-at-rest-nbi.md")
- [SageMaker geospatial capabilities](geospatial-encryption-at-rest.md "geospatial-encryption-at-rest.md")
