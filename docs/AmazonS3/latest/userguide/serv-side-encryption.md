# Protecting data with server-side encryption

###### Important

Starting in April 2026, AWS will disable server-side encryption with customer-provided keys (SSE-C) for all new buckets. In addition, SSE-C encryption will be disabled for all existing buckets in AWS accounts that do not have any SSE-C encrypted data. With these changes, the few applications that need SSE-C encryption must deliberately enable the use SSE-C via the [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") API after creating the bucket. In these cases, you might need to update automation scripts, CloudFormation templates, or other infrastructure configuration tools to configure these settings. For more information, see the [AWS Storage Blog post](https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/ "https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/").

###### Important

Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3)
as the base level of encryption for every bucket in Amazon S3. Starting January 5, 2023, all new object uploads to Amazon S3 are automatically encrypted at no
additional cost and with no impact on performance. The automatic encryption status for S3 bucket default encryption configuration
and for new object uploads is available in AWS CloudTrail logs, S3 Inventory, S3 Storage Lens, the Amazon S3 console, and as an additional Amazon S3 API response header
in the AWS Command Line Interface and AWS SDKs. For more information,
see [Default encryption FAQ](default-encryption-faq.md "default-encryption-faq.md").

Server-side encryption is the encryption of data at its destination by the application or
service that receives it. Amazon S3 encrypts your data at the object level as it writes it to
disks in AWS data centers and decrypts it for you when you access it. As long as you
authenticate your request and you have access permissions, there is no difference in the
way you access encrypted or unencrypted objects. For example, if you share your objects
by using a presigned URL, that URL works the same way for both encrypted and unencrypted
objects. Additionally, when you list objects in your bucket, the list API operations
return a list of all objects, regardless of whether they are encrypted.

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

###### Note

You can't apply different types of server-side encryption to the same object
simultaneously.

If you need to encrypt your existing objects, use S3 Batch Operations and S3 Inventory. For more
information, see [Encrypting
objects with Amazon S3 Batch Operations](https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations/ "https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations/") and [Performing object operations in bulk with Batch Operations](batch-ops.md "batch-ops.md").

When storing data in Amazon S3 you have four mutually exclusive options for server-side encryption, depending on how you
choose to manage the encryption keys and the number of encryption layers that you want
to apply.

###### Server-side encryption with Amazon S3 managed keys (SSE-S3)

All Amazon S3 buckets have encryption configured by default. The default option for server-side
encryption is with Amazon S3 managed keys (SSE-S3). Each object is encrypted with a
unique key. As an additional safeguard, SSE-S3 encrypts the key itself with a root
key that it regularly rotates. SSE-S3 uses one of the strongest block ciphers
available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data. For
more information, see [Using server-side encryption with Amazon S3 managed keys
(SSE-S3)](UsingServerSideEncryption.md "UsingServerSideEncryption.md").

###### Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS)

Server-side encryption with AWS KMS keys (SSE-KMS) is provided through an integration of
the AWS KMS service with Amazon S3. With AWS KMS, you have more control over your keys. For
example, you can view separate keys, edit control policies, and follow the keys in
AWS CloudTrail. Additionally, you can create and manage customer managed keys or use
AWS managed keys that are unique to you, your service, and your Region. For more
information, see [Using server-side encryption with AWS KMS keys
(SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md").

###### Dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys (DSSE-KMS)

Dual-layer server-side encryption with AWS KMS keys (DSSE-KMS) is similar to SSE-KMS,
but DSSE-KMS applies two independent layers of AES-256 encryption instead of one
layer: first using a AWS KMS data encryption key, then using a separate Amazon S3-managed encryption key. Because both layers of encryption are applied to an object on the server
side, you can use a wide range of AWS services and tools to analyze data in S3
while using an encryption method that can satisfy compliance requirements for multilayer encryption. For
more information, see [Using dual-layer server-side encryption with AWS KMS keys
(DSSE-KMS)](UsingDSSEncryption.md "UsingDSSEncryption.md").

###### Server-side encryption with customer-provided keys (SSE-C)

With server-side encryption with customer-provided keys (SSE-C), you manage the encryption
keys, and Amazon S3 manages the encryption as it writes to disks and the decryption when
you access your objects. For more information, see [Using server-side encryption with
customer-provided keys (SSE-C)](ServerSideEncryptionCustomerKeys.md "ServerSideEncryptionCustomerKeys.md").

###### Note

When using access points for Amazon FSx file systems using S3 access points you have one option for server-side encryption.

###### Server-side encryption with Amazon FSx (SSE-FSX)

All Amazon FSx file systems have encryption configured by default and are encrypted
at rest with keys managed using AWS Key Management Service. Data is
automatically encrypted and decrypted by on the file system as data is being
written to and read from the file system. These processes are handled
transparently by Amazon FSx.
