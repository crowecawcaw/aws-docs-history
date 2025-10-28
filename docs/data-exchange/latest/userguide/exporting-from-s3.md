# Exporting AWS Data Exchange assets to an S3 bucket

When you export assets to Amazon S3, the IAM permissions you use must include the ability
to read from the AWS Data Exchange service S3 buckets and to write to the S3 bucket where your assets
are stored. You can export to any S3 bucket you have permission to access, regardless of
ownership. For more information, see [Amazon S3 permissions](access-control.md#additional-s3-permissions "access-control.md#additional-s3-permissions").

AWS Data Exchange supports configurable encryption parameters when exporting data sets to Amazon S3. In
your export job details, you can specify the Amazon S3 server-side encryption configuration that
you want to apply to the exported objects. You can choose to use server-side encryption with
Amazon S3-Managed Keys (SSE-S3) or server-side encryption with AWS KMS keys
stored in AWS Key Management Service (SSE-KMS). For more information, see [Protecting data
using server-side encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md") in the _Amazon Simple Storage Service User Guide_.

###### Important

We recommend that you consider Amazon S3 security features when exporting data to Amazon S3. For
information about general guidelines and best practices, see [Security best practices for
Amazon S3](../../../AmazonS3/latest/dev/security-best-practices.md "../../../AmazonS3/latest/dev/security-best-practices.md") in the _Amazon Simple Storage Service User Guide_.

###### Important

If the provider has marked a product as containing protected health information (PHI)
subject to the Health Insurance Portability and Accountability Act of 1996 (HIPAA), you
may not export the product's data sets into your AWS account unless such AWS account
is designated as a HIPAA account (as defined in the AWS Business Associate Addendum
found in [AWS Artifact](../../../artifact/latest/ug/what-is-aws-artifact.md "../../../artifact/latest/ug/what-is-aws-artifact.md")).

You can export up to 100 assets in a single job.

###### Topics

- [Exporting AWS Data Exchange assets to an S3 bucket (AWS
  SDKs)](export-assets-s3-prog.md "export-assets-s3-prog.md")
- [Exporting AWS Data Exchange assets to an S3 bucket as a
  subscriber (console)](export-asset-s3-console-sub.md "export-asset-s3-console-sub.md")
- [Exporting AWS Data Exchange assets to an S3 bucket as a
  provider (console)](export-asset-s3-console-prov.md "export-asset-s3-console-prov.md")
  The following video explains more about how to export assets from
  AWS Data Exchange.
