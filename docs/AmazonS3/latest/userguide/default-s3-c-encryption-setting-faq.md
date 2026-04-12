# Default SSE-C setting for new buckets FAQ

###### Important

As [announced on November 19, 2025](https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/ "https://aws.amazon.com/blogs/storage/advanced-notice-amazon-s3-to-disable-the-use-of-sse-c-encryption-by-default-for-all-new-buckets-and-select-existing-buckets-in-april-2026/"), Amazon Simple Storage Service is deploying a new default bucket security setting that automatically disables server-side encryption with customer-provided keys (SSE-C) for all new general purpose buckets. For existing buckets in AWS accounts with no SSE-C encrypted objects, Amazon S3 will also disable SSE-C for all new write requests. For AWS accounts with SSE-C usage, Amazon S3 will not change the bucket encryption configuration on any of the existing buckets in those accounts. This deployment started on April 6, 2026, and will complete over the next few weeks in 37 AWS Regions, including the AWS China and AWS GovCloud (US) Regions.

With these changes, applications that need SSE-C encryption must deliberately enable SSE-C by using the [PutBucketEncryption](../API/API_PutBucketEncryption.md "../API/API_PutBucketEncryption.md") API operation after creating a new bucket.

The following sections answer questions about this update.

**1. In April 2026, will the new SSE-C setting take effect for all newly created buckets?**

Yes. This deployment started on April 6, 2026, and will complete over the next few weeks in 37 AWS Regions, including the AWS China and AWS GovCloud (US) Regions.

###### Note

After the deployment is complete, newly created buckets in all AWS Regions except Middle East (Bahrain) and Middle East (UAE) will have SSE-C disabled by default.

**2. How long will it take before this rollout covers all AWS Regions?**

The deployment started on April 6, 2026, and will complete in a few weeks.

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
