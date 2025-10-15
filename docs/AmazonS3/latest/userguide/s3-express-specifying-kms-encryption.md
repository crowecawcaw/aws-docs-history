# Specifying server-side encryption with AWS KMS
 (SSE-KMS) for new object uploads in directory buckets

For directory buckets, to encrypt your data with server-side encryption, you can use either server-side encryption with Amazon S3 managed keys (SSE-S3)
 (the default) or server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS). We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your 
 `CreateSession` requests or `PUT` object requests. Then, new objects 
 are automatically encrypted with the desired encryption settings. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md").

All Amazon S3 buckets have encryption configured by default, and all new objects that are uploaded 
 to an S3 bucket are automatically encrypted at rest. Server-side encryption with Amazon S3 managed keys (SSE-S3) is the default encryption 
 configuration for every bucket in Amazon S3. If you want to specify a different encryption type for a directory bucket, you can use server-side encryption with 
 AWS Key Management Service (AWS KMS) keys (SSE-KMS).
 To encrypt new objects in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")). 
 The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported. Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") per directory bucket for the lifetime of the bucket. After you specify a customer managed key for SSE-KMS, you can't override the customer managed key for the bucket's SSE-KMS configuration. 
 Then, when you specify server-side encryption settings for new objects with SSE-KMS, you must make sure the encryption key is the same customer managed key that you specified for the directory bucket's default encryption configuration. 
 To use a new customer managed key for your data, we recommend copying your existing objects to a new directory bucket with a new customer managed key.

You can apply encryption when you are either uploading a new object or copying an existing
 object. If you change an object's encryption, a new object is created to replace the old one.

You can specify SSE-KMS by using the REST API operations, AWS SDKs, and the
 AWS Command Line Interface (AWS CLI). 

###### Note


* For directory buckets, the encryption overriding behaviors are as follows: 




	+ When you use [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md") with the REST API to authenticate and authorize Zonal endpoint API requests except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), 
	 you can override the encryption settings to SSE-S3 or to SSE-KMS only if you specified the bucket’s default encryption with SSE-KMS previously.
	+ When you use [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md") with the AWS CLI or the AWS SDKs to authenticate and authorize Zonal endpoint API requests except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), you can’t override the encryption settings at all.
	+ When you make [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") requests, you can override the encryption settings to SSE-S3 or to SSE-KMS only if you specified the bucket’s default encryption with SSE-KMS previously. When you make [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md") requests, you can’t override the encryption settings.
* You can use multi-Region AWS KMS keys in Amazon S3. However, Amazon S3 currently treats multi-Region keys 
as though they were single-Region keys, and does not use the multi-Region features of the key. For more 
information, see 
[Using multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html "https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html") in *AWS Key Management Service Developer Guide*.
* If you want to use a KMS key that's owned by a different account, you must have permission
 to use the key. For more information about cross-account permissions for KMS keys, see
 [Creating KMS keys that other accounts can use](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html#cross-account-console "https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html#cross-account-console") in the
 *AWS Key Management Service Developer Guide*.
###### Note


 Only 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") is supported per directory bucket for the lifetime of the bucket. The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported. 
 After you specify SSE-KMS as your bucket's default encryption configuration with a customer managed key, you can't change the customer managed key for the bucket's SSE-KMS configuration.
 

For [Zonal endpoint (object-level) API operations](s3-express-differences.md#s3-express-differences-api-operations "s3-express-differences.md#s3-express-differences-api-operations") except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), 
you authenticate and authorize requests through [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md") for low latency. 
 We recommend that the bucket's default encryption uses the desired encryption configurations and you don't override the bucket default encryption in your 
 `CreateSession` requests or `PUT` object requests. Then, new objects 
 are automatically encrypted with the desired encryption settings. 
 To encrypt new objects in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")). Then, when a session is created for Zonal endpoint API operations, new objects are automatically encrypted and decrypted with SSE-KMS and S3 Bucket Keys during the session. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md").

In the Zonal endpoint API calls (except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")) using the REST API, 
 you can't override the values of the encryption settings (`x-amz-server-side-encryption`, `x-amz-server-side-encryption-aws-kms-key-id`, `x-amz-server-side-encryption-context`, and `x-amz-server-side-encryption-bucket-key-enabled`) from the `CreateSession` request. 
 You don't need to explicitly specify these encryption settings values in Zonal endpoint API calls, and 
 Amazon S3 will use the encryption settings values from the `CreateSession` request to protect new objects in the directory bucket. 
 

###### Note

When you use the AWS CLI or the AWS SDKs, for `CreateSession`, the session token refreshes automatically to avoid service interruptions when a session expires. The AWS CLI or the AWS SDKs use the bucket's default encryption configuration for the 
 `CreateSession` request. It's not supported to override the encryption settings values in the `CreateSession` request. Also, in the Zonal endpoint API calls (except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")), 
 it's not supported to override the values of the encryption settings from the `CreateSession` request. 



For [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), 
 to encrypt new object copies in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")). 
 
 Then, when you specify server-side encryption settings for new object copies with SSE-KMS, you must make sure the encryption key is the same customer managed key that you specified for the directory bucket's default encryption configuration. 
 For [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), to encrypt new object part copies in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")). 
You can't specify server-side encryption settings for new object part copies with SSE-KMS in the [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md") request headers. Also, the encryption settings that you provide in the [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md") request must match the default encryption configuration of the destination bucket. 
 
 

###### Topics

* [Amazon S3 REST API operations that support
 SSE-KMS](#s3-express-sse-request-headers-kms "#s3-express-sse-request-headers-kms")
* [Encryption context
 (x-amz-server-side-encryption-context)](#s3-express-s3-kms-encryption-context "#s3-express-s3-kms-encryption-context")
* [AWS KMS key ID
 (x-amz-server-side-encryption-aws-kms-key-id)](#s3-express-s3-kms-key-id-api "#s3-express-s3-kms-key-id-api")
* [S3 Bucket Keys
 (x-amz-server-side-encryption-aws-bucket-key-enabled)](#s3-express-bucket-key-api "#s3-express-bucket-key-api")

### Amazon S3 REST API operations that support
 SSE-KMS


The following object-level REST API operations in directory buckets accept the
 `x-amz-server-side-encryption`,
 `x-amz-server-side-encryption-aws-kms-key-id`, and
 `x-amz-server-side-encryption-context` request headers.



* [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md") – When you use Zonal endpoint (object-level) API operations (except CopyObject and UploadPartCopy), 
 you can specify these request headers.
* [PutObject](../API/API_PutObject.md "../API/API_PutObject.md") – When you upload data by using the
 `PUT` API operation, you can specify these request headers.
* [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") – When you copy an object, you have both a
 source object and a target object. When you pass SSE-KMS headers with the
 `CopyObject` operation, they're applied only to the target object.
* [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md") – When you upload large objects
 by using the multipart upload API operation, you can specify these headers. You
 specify these headers in the `CreateMultipartUpload` request.

The response headers of the following REST API operations return the
 `x-amz-server-side-encryption` header when an object is stored by using
 server-side encryption.



* [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md")
* [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
* [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")
* [POST
 Object](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md")
* [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
* [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")
* [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")
* [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
* [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
* [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")

###### Important


* All `GET` and `PUT` requests for an object protected by
 AWS KMS fail if you don't make these requests by using 
 Transport Layer Security (TLS), or Signature Version 4.
* If your object uses SSE-KMS, don't send encryption request headers for
 `GET` requests and `HEAD` requests, or you’ll get an
 **`HTTP 400 BadRequest`** error.

### Encryption context
 (`x-amz-server-side-encryption-context`)


If you specify `x-amz-server-side-encryption:aws:kms`, the Amazon S3 API
 supports you to optionally provide an explicit encryption context with the `x-amz-server-side-encryption-context`
 header. For directory buckets, an encryption context is a set of key-value pairs that contain contextual information about the data. 
 The value must match the default encryption context — the bucket Amazon Resource Name (ARN). An additional encryption context value is not supported. 
 


For information about the encryption context in directory buckets, see [Encryption context](s3-express-UsingKMSEncryption.md#s3-express-encryption-context "s3-express-UsingKMSEncryption.md#s3-express-encryption-context"). For general
 information about the encryption context, see [AWS Key Management Service Concepts -
 Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context") in the *AWS Key Management Service Developer Guide*. 


### AWS KMS key ID
 (`x-amz-server-side-encryption-aws-kms-key-id`)


You can use the `x-amz-server-side-encryption-aws-kms-key-id` header to
 specify the ID of the customer managed key that's used to protect the data.


Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") per directory bucket for the lifetime of the bucket. 
The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported. Also, after you specify a customer managed key for SSE-KMS, you can't override the customer managed key for the bucket's SSE-KMS configuration.


You can identify the customer managed key you specified for the bucket's SSE-KMS configuration, in the following way:



* You make a `HeadObject` API operation request to find the value of `x-amz-server-side-encryption-aws-kms-key-id` in your response.

To use a new customer managed key for your data, we recommend copying your existing objects to a new directory bucket with a new customer managed key.


For information about the encryption context in directory buckets, see [AWS KMS keys](s3-express-UsingKMSEncryption.md#s3-express-aws-managed-customer-managed-keys "s3-express-UsingKMSEncryption.md#s3-express-aws-managed-customer-managed-keys"). 


### S3 Bucket Keys
 (`x-amz-server-side-encryption-aws-bucket-key-enabled`)


S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets 
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), [the Copy operation in Batch Operations](directory-buckets-objects-Batch-Ops.md "directory-buckets-objects-Batch-Ops.md"), or 
 [the import jobs](create-import-job.md "create-import-job.md"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object. For information about the S3 Bucket Keys in directory buckets, see [Encryption context](s3-express-UsingKMSEncryption.md#s3-express-encryption-context "s3-express-UsingKMSEncryption.md#s3-express-encryption-context"). 


###### Note

When you use the AWS CLI, for `CreateSession`, the session token refreshes automatically to avoid service interruptions when a session expires. 
 It's not supported to override the encryption settings values for the `CreateSession` request. Also, in the Zonal endpoint API calls (except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")), 
 it's not supported to override the values of the encryption settings from the `CreateSession` request. 
 

To encrypt new objects in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a customer managed key). Then, when a session is created for Zonal endpoint API operations, new objects are automatically encrypted and decrypted with SSE-KMS and S3 Bucket Keys during the session.

To use the following example AWS CLI commands, replace the ``user input
 placeholders`` with your own information.

When you upload a new object or copy an existing object, you can specify the use of
 server-side encryption with AWS KMS keys to encrypt your data. To do this, use the `put-bucket-encryption` command to set the directory bucket's default encryption configuration as SSE-KMS 
 (`aws:kms`). Specifically, add the
 `--server-side-encryption aws:kms` header to the request. Use the
 `--ssekms-key-id `example-key-id`` to add your [customer
 managed AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") that you created. If you specify `--server-side-encryption
 aws:kms`, you must provide an AWS KMS key ID of your customer managed key. Directory buckets don't use an AWS managed
 key. For an example command, see [Using the AWS CLI](s3-express-bucket-encryption.md#s3-express-default-bucket-encryption-cli "s3-express-bucket-encryption.md#s3-express-default-bucket-encryption-cli"). 

Then, when you upload a new object with the following command, Amazon S3 uses the bucket settings for default encryption to encrypt the object by default.


```
aws s3api put-object --bucket ``bucket-base-name`--`zone-id`--x-s3` --key `example-object-key` --body `filepath`
```
You don't need to add `-\-bucket-key-enabled` explicitly in your Zonal endpoint API operations commands. S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets 
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), [the Copy operation in Batch Operations](directory-buckets-objects-Batch-Ops.md "directory-buckets-objects-Batch-Ops.md"), or 
 [the import jobs](create-import-job.md "create-import-job.md"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.

You can copy an object from a source bucket (for example, a general purpose bucket) to a new bucket (for example, a directory bucket) and use SSE-KMS
 encryption for the destination objects. To do this, use the `put-bucket-encryption` command to set the default encryption configuration of the destination bucket (for example, a directory bucket) as SSE-KMS 
 (`aws:kms`). For an example command, see [Using the AWS CLI](s3-express-bucket-encryption.md#s3-express-default-bucket-encryption-cli "s3-express-bucket-encryption.md#s3-express-default-bucket-encryption-cli"). 
 Then, when you copy an object with the following command, Amazon S3 uses the bucket settings for default encryption to encrypt the object by default.


```
aws s3api copy-object --copy-source ``amzn-s3-demo-bucket``/`example-object-key` --bucket ``bucket-base-name`--`zone-id`--x-s3` --key `example-object-key`  
```
When using AWS SDKs, you can request Amazon S3 to use AWS KMS keys for server-side
 encryption. The following examples show how to use SSE-KMS with the AWS SDKs for Java and
 .NET. For information about other SDKs, see [Sample code
 and libraries](https://aws.amazon.com/code "https://aws.amazon.com/code") on the AWS Developer Center.

###### Note

When you use the AWS SDKs, for `CreateSession`, the session token refreshes automatically to avoid service interruptions when a session expires. 
 It's not supported to override the encryption settings values for the `CreateSession` request. Also, in the Zonal endpoint API calls (except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")), 
 it's not supported to override the values of the encryption settings from the `CreateSession` request. 
 
 

To encrypt new objects in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a customer managed key). Then, when a session is created for Zonal endpoint API operations, new objects are automatically encrypted and decrypted with SSE-KMS and S3 Bucket Keys during the session.

For more information about using AWS SDKs to set the default encryption configuration of a directory bucket as SSE-KMS, 
 see [Using the AWS SDKs](s3-express-bucket-encryption.md#s3-express-kms-put-bucket-encryption-using-sdks "s3-express-bucket-encryption.md#s3-express-kms-put-bucket-encryption-using-sdks").

###### Important

When you use an AWS KMS key for server-side encryption in Amazon S3, you must choose a symmetric encryption KMS key. 
Amazon S3 supports only symmetric encryption KMS keys. For more information about these keys, see 
[Symmetric encryption KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks") in the *AWS Key Management Service Developer Guide*.

For more information about creating customer managed keys, see [Programming the AWS KMS API](https://docs.aws.amazon.com/kms/latest/developerguide/programming-top.html "https://docs.aws.amazon.com/kms/latest/developerguide/programming-top.html") in
 the *AWS Key Management Service Developer Guide*.
