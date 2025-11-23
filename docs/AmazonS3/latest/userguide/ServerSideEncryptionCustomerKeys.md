# Using server-side encryption with

customer-provided keys (SSE-C)

Server-side encryption is about protecting data at rest. Server-side encryption encrypts only
the object data, not the object metadata. You can use server-side encryption with
customer-provided keys (SSE-C) in your general purpose buckets to encrypt your data with your own encryption keys. With the encryption
key that you provide as part of your request, Amazon S3 manages data encryption as it writes to
disks and data decryption when you access your objects. Therefore, you don't need to
maintain any code to perform data encryption and decryption. The only thing that you need to
do is manage the encryption keys that you provide.

Most modern use cases in Amazon S3 no longer use SSE-C because it lacks the flexibility of server-side encryption with Amazon S3 managed keys (SSE-S3) or server-side encryption with AWS KMS keys (SSE-KMS). SSE-C's requirement to provide the encryption key each time you interact with your SSE-C encrypted data makes it impractical to share your SSE-C key with other users, roles, or AWS services who read data from your S3 buckets in order to operate on your data. Due to the widespread support for SSE-KMS across AWS, most modern workloads do not use SSE-C encryption because it lacks the flexibility of SSE-KMS. To learn more about SSE-KMS, see [Using server-side encryption with AWS KMS keys
(SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md").

If you want to prevent SSE-C encryption from being used for objects written to your bucket, you can block SSE-C encryption when changing your bucket's default encryption configuration. When SSE-C is blocked for a general purpose bucket, any `PutObject`, `CopyObject`, `PostObject`, Multipart Upload or replication requests that specify SSE-C encryption will be rejected with an `HTTP 403 AccessDenied` error. To learn more about blocking SSE-C, see [Blocking or unblocking SSE-C for a general purpose bucket](blocking-unblocking-s3-c-encryption-gpb.md "blocking-unblocking-s3-c-encryption-gpb.md").

There are no additional charges for using SSE-C. However, requests to configure and use SSE-C
incur standard Amazon S3 request charges. For information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### Important

Starting in April 2026, AWS will disable server-side encryption with customer-provided keys (SSE-C) for all new buckets. In addition, SSE-C encryption will be disabled for all existing buckets in AWS accounts that do not have any SSE-C encrypted data. With these changes, the few applications that need SSE-C encryption must deliberately enable the use SSE-C via the [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") API after creating the bucket. In these cases, you might need to update automation scripts, CloudFormation templates, or other infrastructure configuration tools to configure these settings. For more information, see the [AWS Storage Blog post](https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/ "https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/").

## Considerations before using SSE-C

- S3 never stores the encryption key when you use SSE-C. You must supply the encryption key
  every time you want anyone to download your SSE-C encrypted data from S3.
  - You manage a mapping of which encryption key was used to encrypt which object. You are
    responsible for tracking which encryption key you provided for which
    object. That also means if you lose the encryption key, you lose the
    object.
  - Because you manage encryption keys on the client side, you manage any additional
    safeguards, such as key rotation, on the client side.
  - This design can make it difficult to share your SSE-C key with other users, roles, or
    AWS services you to operate on your data. Due to the widespread
    support for SSE-KMS across AWS, most modern workloads do not use SSE-C
    because it lacks the flexibility of SSE-KMS. To learn more about
    SSE-KMS, see [Using server-side encryption with AWS KMS keys (SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md").
  - This means that objects encrypted with SSE-C cannot be natively decrypted by AWS
    managed services.

- You must use HTTPS when specifying SSE-C headers on your requests.
  - Amazon S3 rejects any requests made over HTTP when using SSE-C. For security considerations,
    we recommend that you consider any key that you erroneously send over
    HTTP to be compromised. Discard the key and rotate as appropriate.

- If your bucket is versioning-enabled, each object version that you upload can have its own
  encryption key. You are responsible for tracking which encryption key was used
  for which object version.
- SSE-C is not supported in the Amazon S3 Console. You cannot use the Amazon S3 console to upload an
  object and specify SSE-C encryption. You also cannot use the console to update
  (for example, change the storage class or add metadata) an existing object
  stored using SSE-C.

###### Topics

- [Specifying server-side encryption with
  customer-provided keys (SSE-C)](specifying-s3-c-encryption.md "specifying-s3-c-encryption.md")
- [Blocking or unblocking SSE-C for a general purpose bucket](blocking-unblocking-s3-c-encryption-gpb.md "blocking-unblocking-s3-c-encryption-gpb.md")
- [Default SSE-C setting for new buckets FAQ](default-s3-c-encryption-setting-faq.md "default-s3-c-encryption-setting-faq.md")
