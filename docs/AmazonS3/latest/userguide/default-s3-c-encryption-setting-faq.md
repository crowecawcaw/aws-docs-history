# Default SSE-C setting for new buckets FAQ

###### Important

Starting in April 2026, AWS will disable server-side encryption with customer-provided keys (SSE-C) for all new buckets. In addition, SSE-C encryption will be disabled for all existing buckets in AWS accounts that do not have any SSE-C encrypted data. With these changes, the few applications that need SSE-C encryption must deliberately enable the use SSE-C via the [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") API after creating the bucket. In these cases, you might need to update automation scripts, CloudFormation templates, or other infrastructure configuration tools to configure these settings. For more information, see the [AWS Storage Blog post](https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/ "https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/").

The following sections answer questions about this update.

**1. In April 2026, will the new SSE-C setting take effect for all newly created buckets?**

Yes. During April 2026, the
new default setting will gradually be rolled out across all AWS Regions.

**2. How long will it take before this rollout covers all AWS Regions?**

This update will take several weeks to roll out. We will publish a What's New post
when we start to deploy this update.

**3. How will I know that the update is complete?**

You can easily determine if the change has completed in your AWS Region by creating a new bucket
and calling the [GetBucketEncryption](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md") API operation to determine if SSE-C encryption is
disabled. After the update is complete, all new general purpose buckets will automatically
have SSE-C encryption disabled by default. You can adjust these settings after creating your
S3 bucket by calling the [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") API operation.

**4. Will Amazon S3 update my existing bucket configurations?**

If your AWS account does not have any SSE-C encrypted objects, AWS will disable
SSE-C encryption on all of your existing buckets. If any bucket in your AWS account has
SSE-C encrypted objects, AWS will not change the bucket configurations on any of your
buckets in that account. After the `CreateBucket` change is complete for your AWS Region,
the new default setting will apply to all new general purpose buckets.

**5. Can I disable SSE-C encryption for my buckets before the update is complete?**

Yes. You can disable SSE-C encryption for any bucket by calling the [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") API operation and specifying the new `BlockedEncryptionTypes` header.

**6. Can I use SSE-C to encrypt data in my new buckets?**

Yes. Most modern use cases in Amazon S3 no longer use SSE-C because it lacks the flexibility of server-side encryption is with Amazon S3 managed keys (SSE-S3) or server-side encryption with AWS KMS keys (SSE-KMS). If you need to use SSE-C encryption in a new bucket, you can create the new bucket and then enable the use of SSE-C encryption in a separate `PutBucketEncryption` request.

**Example**

```

aws s3api create-bucket \
bucket amzn-s3-demo-bucket \
region us-east-1 \

aws s3api put-bucket-encryption \
-- bucket amzn-s3-demo-bucket \
-- server-side-encryption-configuration \
'{ \Rules\: [{
   {
   \ApplyServerSideEncryptionByDefault\: {
     \SSEAlgorithm\: \AES256\,
    },
   \BlockedEncryptionTypes\: [
     \EncryptionType\:\NONE\]
   }
   }]
}'

```

###### Note

You must have the
`s3:PutEncryptionConfiguration`permission to call the
`PutBucketEncryption` API.

**7. How does blocking SSE-C
affect requests to my bucket?**

When SSE-C is blocked for a bucket, any
`PutObject`, `CopyObject`, `PostObject`, or Multipart Upload or replication requests that specify SSE-C encryption will be rejected with an HTTP 403 `AccessDenied` error.
