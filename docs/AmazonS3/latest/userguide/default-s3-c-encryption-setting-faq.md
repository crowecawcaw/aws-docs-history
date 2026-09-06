

# Default SSE-C setting for new buckets FAQ
<a name="default-s3-c-encryption-setting-faq"></a>

**Important**  
Amazon Simple Storage Service now applies a new default bucket security setting that automatically disables server-side encryption with customer-provided keys (SSE-C) for all new general purpose buckets. In April 2026, Amazon S3 deployed an update so all new general purpose buckets have SSE-C encryption disabled for all new write requests. For existing buckets in AWS accounts with no SSE-C encrypted objects, Amazon S3 also disabled SSE-C for all new write requests. With this change, applications that need SSE-C encryption must deliberately enable SSE-C by using the [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html) API operation after creating a new bucket.

The following sections answer questions about this update.

**1. Does the new SSE-C setting take effect for all newly created buckets?**

Yes. This deployment completed in 37 AWS Regions, including the AWS China and AWS GovCloud (US) Regions, in April 2026.

**Note**  
All newly created buckets in all AWS Regions except Middle East (Bahrain) and Middle East (UAE) will have SSE-C disabled by default.

**2. Did Amazon S3 update my existing bucket configurations?**

If your AWS account did not have any SSE-C encrypted objects, then AWS disabled SSE-C encryption on all of your existing buckets. If any bucket in your AWS account had SSE-C encrypted objects, then AWS did not change the bucket configurations on any of your buckets in that account. The new default setting applies to all new general purpose buckets. 

 **3. Can I disable SSE-C encryption for my buckets?** 

Yes. You can disable SSE-C encryption for any bucket by calling the [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html) API operation and specifying the new `BlockedEncryptionTypes` header. 

**4. Can I use SSE-C to encrypt data in my new buckets?**

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

**Note**  
You must have the `s3:PutEncryptionConfiguration`permission to call the `PutBucketEncryption` API. 

**5. How does blocking SSE-C affect requests to my bucket?**

When SSE-C is blocked for a bucket, any `PutObject`, `CopyObject`, `PostObject`, or Multipart Upload or replication requests that specify SSE-C encryption will be rejected with an HTTP 403 `AccessDenied` error. 