# Viewing the settings for an S3 Bucket Key

You can view the settings for an S3 Bucket Key at the bucket or object level by using the
Amazon S3 console, REST API, AWS Command Line Interface (AWS CLI), or AWS SDKs.

S3 Bucket Keys decrease request traffic from Amazon S3 to AWS KMS and reduce the cost of server-side
encryption using AWS Key Management Service (SSE-KMS). For more information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md").

To view the S3 Bucket Key settings for a bucket or an object that has inherited
S3 Bucket Key settings from the bucket configuration, you need permission to perform the
`s3:GetEncryptionConfiguration` action. For more information, see [GetBucketEncryption](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md") in the _Amazon Simple Storage Service API Reference_.

In the S3 console, you can view the S3 Bucket Key settings for your bucket or object.
S3 Bucket Key settings are inherited from the bucket configuration unless the source
objects already has an S3 Bucket Key configured.

Objects and folders in the same bucket can have different S3 Bucket Key settings. For
example, if you upload an object using the REST API and enable an S3 Bucket Key for the
object, the object retains its S3 Bucket Key setting in the destination bucket, even if
S3 Bucket Key is disabled in the destination bucket. As another example, if you enable an
S3 Bucket Key for an existing bucket, objects that are already in the bucket do not use an
S3 Bucket Key. However, new objects have an S3 Bucket Key enabled.

###### To view the S3 Bucket Key setting for your bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, choose the bucket that you want to
   enable an S3 Bucket Key for.
4. Choose **Properties**.
5. In the **Default encryption** section, under **Bucket
   Key**, you see the S3 Bucket Key setting for your bucket.

If you can’t see the S3 Bucket Key setting, you might not have permission to
perform the `s3:GetEncryptionConfiguration` action. For more information,
see [GetBucketEncryption](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md") in the _Amazon Simple Storage Service API Reference_.

###### To view the S3 Bucket Key setting for your object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** list, choose the bucket that you want to
   enable an S3 Bucket Key for.
3. In the **Objects** list, choose your object name.
4. On the **Details** tab, under **Server-side encryption
   settings**, choose **Edit**.

Under **Bucket Key**, you see the S3 Bucket Key setting for your
object. You cannot edit this setting.

###### To return bucket-level S3 Bucket Key settings

To use this example, replace each `user input
 placeholder` with your own information.

```
aws s3api get-bucket-encryption --bucket `amzn-s3-demo-bucket1`
```

For more information, see [get-bucket-encryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-encryption.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-encryption.html") in the _AWS CLI Command Reference_.

###### To return object-level S3 Bucket Key settings

To use this example, replace each `user input
 placeholder` with your own information.

```
aws s3api head-object --bucket `amzn-s3-demo-bucket1` --key `my_images.tar.bz2`
```

For more information, see [head-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html") in the _AWS CLI Command Reference_.

###### To return bucket-level S3 Bucket Key settings

To return encryption information for a bucket, including the settings for an
S3 Bucket Key, use the `GetBucketEncryption` operation. S3 Bucket Key settings
are returned in the response body in the `ServerSideEncryptionConfiguration`
element with the `BucketKeyEnabled` setting. For more information, see [GetBucketEncryption](../API/API_GetBucketEncryption.md "../API/API_GetBucketEncryption.md") in the _Amazon S3 API Reference_.

###### To return object-level settings for an S3 Bucket Key

To return the S3 Bucket Key status for an object, use the `HeadObject`
operation. `HeadObject` returns
the `x-amz-server-side-encryption-bucket-key-enabled` response header to
show whether an S3 Bucket Key is enabled or disabled for the object. For more
information, see [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md") in the *Amazon S3
API Reference*.

The following API operations also return
the `x-amz-server-side-encryption-bucket-key-enabled` response header if an
S3 Bucket Key is configured for an object:

- [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
- [PostObject](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md")
- [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")
- [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
- [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")
- [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")
- [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
- [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
