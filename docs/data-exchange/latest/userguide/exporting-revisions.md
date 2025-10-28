# Exporting revisions from AWS Data Exchange

Both providers and subscribers can export revisions of a data set to an S3 bucket that
they have permissions to access.

AWS Data Exchange supports configurable encryption parameters when exporting revisions to Amazon S3. In
your export job details, you can specify the Amazon S3 server-side encryption configuration that
you want to apply to the exported objects. You can choose to use server-side encryption with
Amazon S3-Managed Keys (SSE-S3) or server-side encryption with KMS keys stored in AWS Key Management Service
(SSE-KMS). For more information, see [Protecting data using server-side
encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md") in the _Amazon Simple Storage Service Developer Guide_.

###### Important

If the provider has marked a product as containing protected health information (PHI)
subject to the Health Insurance Portability and Accountability Act of 1996 (HIPAA), you may
not export the product's data sets into your AWS account unless such AWS account is
designated as a HIPAA account (as defined in the AWS Business Associate Addendum found in
[AWS Artifact](../../../artifact/latest/ug/what-is-aws-artifact.md "../../../artifact/latest/ug/what-is-aws-artifact.md")).

###### Topics

- [Key patterns when exporting
  revisions](revision-export-keypatterns.md "revision-export-keypatterns.md")
- [Using AWS SDKs](export-rev-s3-prog.md "export-rev-s3-prog.md")
- [Using the console
  (Subscriber)](export-rev-s3-console-sub.md "export-rev-s3-console-sub.md")
- [Using the console
  (Provider)](export-rev-s3-console-pro.md "export-rev-s3-console-pro.md")
- [Automatically exporting
  revisions (Subscriber)](auto-export-rev-s3-console-sub.md "auto-export-rev-s3-console-sub.md")
  The following video explains more about how to export assets from AWS Data Exchange
  (starting at 2:18).
