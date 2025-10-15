# Data protection and encryption

 For more information about how you can configure encryption for directory buckets, see
 the following topics.

###### Topics

* [Server-side encryption](#s3-express-ecnryption "#s3-express-ecnryption")
* [Setting and monitoring default encryption for directory buckets](s3-express-bucket-encryption.md "s3-express-bucket-encryption.md")
* [Using server-side encryption with AWS KMS keys
 (SSE-KMS) in directory buckets](s3-express-UsingKMSEncryption.md "s3-express-UsingKMSEncryption.md")
* [Encryption in transit](#s3-express-ecnryption-transit "#s3-express-ecnryption-transit")
* [Data deletion](#s3-express-data-deletion "#s3-express-data-deletion")

## Server-side encryption


All directory buckets have encryption configured by default, and all new objects that are uploaded to directory buckets are automatically encrypted at rest. 
 Server-side encryption with Amazon S3 managed keys (SSE-S3) is the default encryption configuration for every directory bucket. 
 If you want to specify a different encryption type, you can use server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), by setting the default encryption configuration of the bucket. 
 For more information about SSE-KMS in directory buckets, see [Using server-side encryption with AWS KMS keys
 (SSE-KMS) in directory buckets](s3-express-UsingKMSEncryption.md "s3-express-UsingKMSEncryption.md").


We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your 
 `CreateSession` requests or `PUT` object requests. Then, new objects 
 are automatically encrypted with the desired encryption settings. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md").


SSE-KMS with directory buckets differs from SSE-KMS in general purpose buckets in the following aspects.



* Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") per directory bucket for the lifetime of the bucket. 
The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported. Also, after you specify a customer managed key for SSE-KMS, you can't override the customer managed key for the bucket's SSE-KMS configuration.


You can identify the customer managed key you specified for the bucket's SSE-KMS configuration, in the following way:




	+ You make a `HeadObject` API operation request to find the value of `x-amz-server-side-encryption-aws-kms-key-id` in your response.
To use a new customer managed key for your data, we recommend copying your existing objects to a new directory bucket with a new customer managed key.
* For [Zonal endpoint (object-level) API operations](s3-express-differences.md#s3-express-differences-api-operations "s3-express-differences.md#s3-express-differences-api-operations") except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), 
you authenticate and authorize requests through [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md") for low latency. 
 We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your 
 `CreateSession` requests or `PUT` object requests. Then, new objects 
 are automatically encrypted with the desired encryption settings. 
 To encrypt new objects in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")). Then, when a session is created for Zonal endpoint API operations, new objects are automatically encrypted and decrypted with SSE-KMS and S3 Bucket Keys during the session. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md").


In the Zonal endpoint API calls (except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")), you can't override the values of the encryption settings (`x-amz-server-side-encryption`, `x-amz-server-side-encryption-aws-kms-key-id`, `x-amz-server-side-encryption-context`, and `x-amz-server-side-encryption-bucket-key-enabled`) from the `CreateSession` request. 
 You don't need to explicitly specify these encryption settings values in Zonal endpoint API calls, and 
 Amazon S3 will use the encryption settings values from the `CreateSession` request to protect new objects in the directory bucket. 


###### Note

When you use the AWS CLI or the AWS SDKs, for `CreateSession`, the session token refreshes automatically to avoid service interruptions when a session expires. The AWS CLI or the AWS SDKs use the bucket's default encryption configuration for the 
 `CreateSession` request. It's not supported to override the encryption settings values in the `CreateSession` request. Also, in the Zonal endpoint API calls (except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")), 
 it's not supported override the values of the encryption settings from the `CreateSession` request.
* For [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), 
 to encrypt new object copies in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")). 
 
 Then, when you specify server-side encryption settings for new object copies with SSE-KMS, you must make sure the encryption key is the same customer managed key that you specified for the directory bucket's default encryption configuration. 
 For [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), to encrypt new object part copies in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")). 
You can't specify server-side encryption settings for new object part copies with SSE-KMS in the [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md") request headers. Also, the encryption settings that you provide in the [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md") request must match the default encryption configuration of the destination bucket.
* S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets 
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), [the Copy operation in Batch Operations](directory-buckets-objects-Batch-Ops.md "directory-buckets-objects-Batch-Ops.md"), or 
 [the import jobs](create-import-job.md "create-import-job.md"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.
* When you specify an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.

Directory buckets don't support dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys (DSSE-KMS), or
 server-side encryption with customer-provided encryption keys (SSE-C).


## Encryption in transit


Directory buckets use Regional and Zonal API endpoints. Depending on the Amazon S3 API operation
 that you use, either a Regional or Zonal endpoint is required. You can access Zonal and
 Regional endpoints through a gateway virtual private cloud (VPC) endpoint. There is no
 additional charge for using gateway endpoints. To learn more about Regional and Zonal
 API endpoints, see [Networking for directory buckets](s3-express-networking.md "s3-express-networking.md"). 


## Data deletion


You can delete one or more objects directly from your directory buckets by using the
 Amazon S3 console, AWS SDKs, AWS Command Line Interface (AWS CLI), or Amazon S3 REST API. Because all objects in
 your directory buckets incur storage costs, we recommend deleting objects that you no
 longer need.


Deleting an object that's stored in a directory bucket also recursively deletes any
 parent directories, if those parent directories don't contain any objects other than the
 object that's being deleted.


###### Note

Multi-factor authentication (MFA) delete and S3 Versioning are not supported for
 S3 Express One Zone.
