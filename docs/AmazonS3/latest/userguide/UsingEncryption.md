# Protecting data with encryption

###### Important

Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3. Starting January 5, 2023, all new object uploads to Amazon S3 are automatically encrypted at no additional cost and with no impact on performance. The automatic encryption status for S3 bucket default encryption configuration and for new object uploads is available in CloudTrail logs, S3 Inventory, S3 Storage Lens, the Amazon S3 console, and as an additional Amazon S3 API response header in the AWS CLI and AWS SDKs. For more information, see [Default encryption FAQ](default-encryption-faq.md "default-encryption-faq.md").

Data protection refers to protecting data while it's in transit (as it travels to and from
Amazon S3) and at rest (while it is stored on disks in Amazon S3 data centers). You can protect data
in transit by using Secure Socket Layer/Transport Layer Security (SSL/TLS) including hybrid
post-quantum key exchange or client-side encryption. For protecting data at rest in Amazon S3,
you have the following options:

- **Server-side encryption** – Amazon S3 encrypts your
  objects before saving them on disks in AWS data centers and then decrypts the
  objects when you download them.

All Amazon S3 buckets have encryption configured by default, and all new objects that are uploaded
to an S3 bucket are automatically encrypted at rest. Server-side encryption with Amazon S3 managed keys (SSE-S3) is the default encryption
configuration for every bucket in Amazon S3. To use a different type of encryption, you can either specify the type of server-side encryption
to use in your S3 `PUT` requests, or you can update the default encryption configuration in the destination bucket.

If you want to specify a different encryption type in your `PUT` requests, you can use server-side encryption with
AWS Key Management Service (AWS KMS) keys (SSE-KMS), dual-layer server-side encryption with AWS KMS keys (DSSE-KMS), or server-side encryption with
customer-provided keys (SSE-C). If you want to set a different default encryption configuration in the destination bucket, you can use
SSE-KMS or DSSE-KMS.

For more information about changing the default encryption configuration for your general purpose buckets, see [Configuring default encryption](default-bucket-encryption.md "default-bucket-encryption.md").

When you change the default encryption configuration of your bucket to SSE-KMS, the encryption type of the existing Amazon S3 objects in the bucket is not changed. To change the encryption type of your pre-existing objects after updating the default encryption configuration to SSE-KMS, you can use Amazon S3 Batch Operations. You provide S3 Batch Operations with a list of objects, and Batch Operations calls the respective API operation. You can use the [Copy objects](batch-ops-copy-object.md "batch-ops-copy-object.md") action to copy existing objects, which writes them back to the same bucket as SSE-KMS encrypted objects. A single Batch Operations job can perform the specified operation on billions of objects. For more information, see [Performing object operations in bulk with Batch Operations](batch-ops.md "batch-ops.md") and the _AWS Storage Blog_ post [How to retroactively encrypt existing objects in Amazon S3 using S3 Inventory, Amazon Athena, and S3 Batch Operations](https://aws.amazon.com/blogs/security/how-to-retroactively-encrypt-existing-objects-in-amazon-s3-using-s3-inventory-amazon-athena-and-s3-batch-operations/ "https://aws.amazon.com/blogs/security/how-to-retroactively-encrypt-existing-objects-in-amazon-s3-using-s3-inventory-amazon-athena-and-s3-batch-operations/").

For more information about each option for server-side encryption, see [Protecting data with server-side encryption](serv-side-encryption.md "serv-side-encryption.md").

To configure server-side encryption, see:

    + [Specifying server-side encryption with Amazon S3 managed keys (SSE-S3)](specifying-s3-encryption.md "specifying-s3-encryption.md")
    + [Specifying server-side encryption with AWS KMS (SSE-KMS)](specifying-kms-encryption.md "specifying-kms-encryption.md")
    + [Specifying dual-layer server-side encryption with AWS KMS keys (DSSE-KMS)](specifying-dsse-encryption.md "specifying-dsse-encryption.md")
    + [Specifying server-side encryption with customer-provided keys (SSE-C)](specifying-s3-c-encryption.md "specifying-s3-c-encryption.md")

- **Client-side encryption** – You encrypt your data
  client-side and upload the encrypted data to Amazon S3. In this case, you manage the
  encryption process, encryption keys, and related tools.

To configure client-side encryption, see [Protecting data by using client-side encryption](UsingClientSideEncryption.md "UsingClientSideEncryption.md").
To see which percentage of your storage bytes are encrypted, you can use Amazon S3 Storage Lens
metrics. S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide
visibility into object-storage usage and activity. For more information, see [Assessing your storage activity and usage with S3 Storage Lens](storage_lens.md "storage_lens.md"). For a complete list of metrics, see [S3 Storage Lens metrics glossary](storage_lens_metrics_glossary.md "storage_lens_metrics_glossary.md").

For more information about server-side encryption, client-side encryption, and encryption in
transit, review the following topics.

###### Topics

- [Protecting data with server-side encryption](serv-side-encryption.md "serv-side-encryption.md")
- [Protecting data by using client-side encryption](UsingClientSideEncryption.md "UsingClientSideEncryption.md")
- [Protecting data in transit with encryption](UsingEncryptionInTransit.md "UsingEncryptionInTransit.md")
