# Specifying server-side encryption with AWS KMS

(SSE-KMS)

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

You can specify SSE-KMS by using the Amazon S3 console, REST API operations, AWS SDKs, and the
AWS Command Line Interface (AWS CLI). For more information, see the following topics.

###### Note

You can use multi-Region AWS KMS keys in Amazon S3. However, Amazon S3 currently treats multi-Region keys
as though they were single-Region keys, and does not use the multi-Region features of the key. For more
information, see
[Using multi-Region keys](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md") in the _AWS Key Management Service Developer Guide_.

###### Note

If you want to use a KMS key that's owned by a different account, you must have permission
to use the key. For more information about cross-account permissions for KMS keys, see
[Creating KMS keys that other accounts can use](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md#cross-account-console "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md#cross-account-console") in the
_AWS Key Management Service Developer Guide_.

This topic describes how to set or change the type of encryption of an object to use
server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) by using the Amazon S3 console.

###### Note

- You can change an object's encryption if your object is less than 5 GB. If your object is greater than 5 GB, you must use the [AWS CLI](mpu-upload-object.md#UsingCLImpUpload "mpu-upload-object.md#UsingCLImpUpload") or [AWS SDKs](CopyingObjectsMPUapi.md "CopyingObjectsMPUapi.md") to change an object's encryption.
- For a list of additional permissions required to change an object's encryption, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md"). For example policies that grant this permission, see [Identity-based policy examples for Amazon S3](example-policies-s3.md "example-policies-s3.md").
- If you change an object's encryption, a new object is created to replace the old one.
  If S3 Versioning is enabled, a new version of the object is created, and the existing
  object becomes an older version. The role that changes the property also becomes the owner
  of the new object (or object version).

###### To add or change encryption for an object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Buckets**, and then choose
   the **General purpose buckets** tab. Navigate to the Amazon S3 bucket or
   folder that contains the objects you want to change.
3. Select the check box for the objects you want to
   change.
4. On the **Actions** menu, choose **Edit server-side encryption** from
   the list of options that appears.
5. Scroll to the **Server-side encryption** section.
6. Under **Encryption settings**, choose **Use bucket settings for default encryption** or **Override bucket settings for default encryption**.

###### Important

If you use the SSE-KMS option for your default encryption configuration, you are
subject to the requests per second (RPS) quotas of AWS KMS. For more information about AWS KMS
quotas and how to request a quota increase, see [Quotas](../../../kms/latest/developerguide/limits.md "../../../kms/latest/developerguide/limits.md") in the _AWS Key Management Service Developer Guide_. 7. If you chose **Override bucket settings for default encryption**,
configure the following encryption settings.

    1. Under **Encryption type**, choose **Server-side encryption with AWS Key Management Service keys (SSE-KMS)**.
    2. Under **AWS KMS key**, do one of the following to choose your
     KMS key:




    	* To choose from a list of available KMS keys, choose **Choose from your
    	 AWS KMS keys**, and then choose your **KMS key** from
    	 the list of available keys.


    	Both the AWS managed key (`aws/s3`) and your customer managed keys appear in this
    	 list. For more information about customer managed keys, see [Customer keys and AWS
    	 keys](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") in the *AWS Key Management Service Developer Guide*.
    	* To enter the KMS key ARN, choose **Enter AWS KMS key ARN**,
    	 and then enter your KMS key ARN in the field that appears.
    	* To create a new customer managed key in the AWS KMS console, choose **Create a
    	 KMS key**.


    	For more information about creating an AWS KMS key, see [Creating
    	 keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the *AWS Key Management Service Developer Guide*.
    ###### Important

    You can use only KMS keys that are available in the same AWS Region as the bucket.
     The Amazon S3 console lists only the first 100 KMS keys in the same Region as the
     bucket. To use a KMS key that is not listed, you must enter your KMS key ARN. If you
     want to use a KMS key that is owned by a different account, you must first have
     permission to use the key and then you must enter the KMS key ARN.

    Amazon S3 supports only symmetric encryption KMS keys, and not asymmetric KMS keys. For
     more information, see [Identifying symmetric and
     asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md") in the *AWS Key Management Service Developer Guide*.

8. Under **Additional copy settings**, choose whether you want to **Copy source settings**, **Don’t specify settings**, or **Specify settings**. **Copy source settings** is the default option. If you only want to copy the object without the source settings attributes, choose **Don’t specify settings**. Choose **Specify settings** to specify settings for storage class, ACLs, object tags, metadata, server-side encryption, and additional checksums.
9. Choose **Save changes**.

###### Note

This action applies encryption to all specified objects. When you're encrypting folders,
wait for the save operation to finish before adding new objects to the folder.

When you create an object—that is, when you upload a new object or copy an
existing object—you can specify the use of server-side encryption with AWS KMS keys
(SSE-KMS) to encrypt your data. To do this, add the
`x-amz-server-side-encryption` header to the request. Set the value of the
header to the encryption algorithm `aws:kms`. Amazon S3 confirms that your object is
stored using SSE-KMS by returning the response header
`x-amz-server-side-encryption`.

If you specify the `x-amz-server-side-encryption` header with a value of
`aws:kms`, you can also use the following request headers:

- `x-amz-server-side-encryption-aws-kms-key-id`
- `x-amz-server-side-encryption-context`
- `x-amz-server-side-encryption-bucket-key-enabled`

###### Topics

- [Amazon S3 REST API operations that support
  SSE-KMS](#sse-request-headers-kms "#sse-request-headers-kms")
- [Encryption context
  (x-amz-server-side-encryption-context)](#s3-kms-encryption-context "#s3-kms-encryption-context")
- [AWS KMS key ID
  (x-amz-server-side-encryption-aws-kms-key-id)](#s3-kms-key-id-api "#s3-kms-key-id-api")
- [S3 Bucket Keys
  (x-amz-server-side-encryption-aws-bucket-key-enabled)](#bucket-key-api "#bucket-key-api")

### Amazon S3 REST API operations that support

SSE-KMS

The following REST API operations accept the
`x-amz-server-side-encryption`,
`x-amz-server-side-encryption-aws-kms-key-id`, and
`x-amz-server-side-encryption-context` request headers.

- [PutObject](../API/API_PutObject.md "../API/API_PutObject.md") – When you upload data by using the
  `PUT` API operation, you can specify these request headers.
- [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") – When you copy an object, you have both a
  source object and a target object. When you pass SSE-KMS headers with the
  `CopyObject` operation, they're applied only to the target object. When
  you're copying an existing object, regardless of whether the source object is
  encrypted or not, the destination object isn't encrypted unless you explicitly request
  server-side encryption.
- [POST Object](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md")
  – When you use a `POST` operation to upload an object, instead of
  the request headers, you provide the same information in the form fields.
- [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md") – When you upload large objects
  by using the multipart upload API operation, you can specify these headers. You
  specify these headers in the `CreateMultipartUpload` request.

The response headers of the following REST API operations return the
`x-amz-server-side-encryption` header when an object is stored by using
server-side encryption.

- [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
- [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")
- [POST
  Object](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md")
- [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md")
- [UploadPart](../API/API_UploadPart.md "../API/API_UploadPart.md")
- [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md")
- [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
- [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
- [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")

###### Important

- All `GET` and `PUT` requests for an object protected by
  AWS KMS fail if you don't make these requests by using Secure Sockets Layer (SSL),
  Transport Layer Security (TLS), or Signature Version 4.
- If your object uses SSE-KMS, don't send encryption request headers for
  `GET` requests and `HEAD` requests, or you’ll get an
  **`HTTP 400 BadRequest`** error.

### Encryption context

(`x-amz-server-side-encryption-context`)

If you specify `x-amz-server-side-encryption:aws:kms`, the Amazon S3 API
supports an encryption context with the `x-amz-server-side-encryption-context`
header. An encryption context is a set of key-value pairs that contain additional
contextual information about the data.

Amazon S3 automatically uses the object or bucket Amazon Resource Name (ARN) as the
encryption context pair. If you use SSE-KMS without enabling an S3 Bucket Key, you use the
object ARN as your encryption context; for example,
`arn:aws:s3:::`object_ARN``. However, if you use
 SSE-KMS and enable an S3 Bucket Key, you use the bucket ARN for your encryption context;
 for example, `arn:aws:s3:::`bucket_ARN``.

You can optionally provide an additional encryption context pair by using the
`x-amz-server-side-encryption-context` header. However, because the
encryption context isn't encrypted, make sure it doesn't include sensitive information.
Amazon S3 stores this additional key pair alongside the default encryption context.

For information about the encryption context in Amazon S3, see [Encryption context](UsingKMSEncryption.md#encryption-context "UsingKMSEncryption.md#encryption-context"). For general
information about the encryption context, see [AWS Key Management Service Concepts -
Encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") in the _AWS Key Management Service Developer Guide_.

### AWS KMS key ID

(`x-amz-server-side-encryption-aws-kms-key-id`)

You can use the `x-amz-server-side-encryption-aws-kms-key-id` header to
specify the ID of the customer managed key that's used to protect the data. If you specify the
`x-amz-server-side-encryption:aws:kms` header but don't provide the
`x-amz-server-side-encryption-aws-kms-key-id` header, Amazon S3 uses the
AWS managed key (`aws/s3`) to protect the data. If you want to use a
customer managed key, you must provide the `x-amz-server-side-encryption-aws-kms-key-id`
header of the customer managed key.

###### Important

When you use an AWS KMS key for server-side encryption in Amazon S3, you must choose a symmetric encryption KMS key.
Amazon S3 supports only symmetric encryption KMS keys. For more information about these keys, see
[Symmetric encryption KMS keys](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks") in the _AWS Key Management Service Developer Guide_.

### S3 Bucket Keys

(`x-amz-server-side-encryption-aws-bucket-key-enabled`)

You can use the `x-amz-server-side-encryption-aws-bucket-key-enabled`
request header to enable or disable an S3 Bucket Key at the object level. S3 Bucket Keys reduce
your AWS KMS request costs by decreasing the request traffic from Amazon S3 to AWS KMS. For more
information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md").

If you specify the `x-amz-server-side-encryption:aws:kms` header but don't
provide the `x-amz-server-side-encryption-aws-bucket-key-enabled` header, your
object uses the S3 Bucket Key settings for the destination bucket to encrypt your object.
For more information, see [Configuring an S3 Bucket Key at the object
level](configuring-bucket-key-object.md "configuring-bucket-key-object.md").

To use the following example AWS CLI commands, replace the `user input
 placeholders` with your own information.

When you upload a new object or copy an existing object, you can specify the use of
server-side encryption with AWS KMS keys to encrypt your data. To do this, add the
`--server-side-encryption aws:kms` header to the request. Use the
`--ssekms-key-id `example-key-id``to add your [customer
 managed AWS KMS key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") that you created. If you specify`--server-side-encryption
aws:kms`, but don't provide an AWS KMS key ID, Amazon S3 will use an AWS managed
key.

```
aws s3api put-object --bucket `amzn-s3-demo-bucket` --key `example-object-key` --server-side-encryption aws:kms --ssekms-key-id `example-key-id` --body `filepath`
```

You can additionally enable or disable Amazon S3 Bucket Keys on your PUT or COPY operations
by adding `--bucket-key-enabled` or `--no-bucket-key-enabled`. Amazon S3 Bucket Keys can reduce your AWS KMS request costs by decreasing the request traffic from
Amazon S3 to AWS KMS. For more information, see [Reducing the cost of SSE-KMS with Amazon S3
Bucket Keys](bucket-key.md "bucket-key.md").

```
aws s3api put-object --bucket `amzn-s3-demo-bucket` --key `example-object-key` --server-side-encryption aws:kms --bucket-key-enabled --body `filepath`
```

You can encrypt an unencrypted object to use SSE-KMS by copying the object back in
place.

```
aws s3api copy-object --bucket `amzn-s3-demo-bucket` --key `example-object-key` --body `filepath` --bucket `amzn-s3-demo-bucket` --key `example-object-key` --sse aws:kms --sse-kms-key-id `example-key-id` --body `filepath`
```

When using AWS SDKs, you can request Amazon S3 to use AWS KMS keys for server-side
encryption. The following examples show how to use SSE-KMS with the AWS SDKs for Java and
.NET. For information about other SDKs, see [Sample code
and libraries](https://aws.amazon.com/code "https://aws.amazon.com/code") on the AWS Developer Center.

###### Important

When you use an AWS KMS key for server-side encryption in Amazon S3, you must choose a symmetric encryption KMS key.
Amazon S3 supports only symmetric encryption KMS keys. For more information about these keys, see
[Symmetric encryption KMS keys](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks") in the _AWS Key Management Service Developer Guide_.

### `CopyObject` operation

When copying objects, you add the same request properties
(`ServerSideEncryptionMethod` and
`ServerSideEncryptionKeyManagementServiceKeyId`) to request Amazon S3 to use an
AWS KMS key. For more information about copying objects, see [Copying, moving, and renaming objects](copy-object.md "copy-object.md").

### `PUT` operation

Java
When uploading an object by using the AWS SDK for Java, you can request Amazon S3 to use an
AWS KMS key by adding the `SSEAwsKeyManagementParams` property as
shown in the following request:

```
PutObjectRequest putRequest = new PutObjectRequest(bucketName,
   keyName, file).withSSEAwsKeyManagementParams(new SSEAwsKeyManagementParams());
```

In this case, Amazon S3 uses the AWS managed key (`aws/s3`). For more
information, see [Using server-side encryption with AWS KMS keys
(SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md"). You can optionally create a symmetric
encryption KMS key and specify that in the request, as shown in the following
example:

```
PutObjectRequest putRequest = new PutObjectRequest(bucketName,
   keyName, file).withSSEAwsKeyManagementParams(new SSEAwsKeyManagementParams(keyID));
```

For more information about creating customer managed keys, see [Programming the AWS KMS API](../../../kms/latest/developerguide/programming-top.md "../../../kms/latest/developerguide/programming-top.md") in
the _AWS Key Management Service Developer Guide_.

For working code examples of uploading an object, see the following topics. To
use these examples, you must update the code examples and provide encryption
information as shown in the preceding code fragment.

- For uploading an object in a single operation, see [Uploading objects](upload-objects.md "upload-objects.md").
- For multipart uploads that use the high-level or low-level multipart upload
  API operations, see [Uploading an object using multipart upload](mpu-upload-object.md "mpu-upload-object.md").

.NET
When uploading an object by using the AWS SDK for .NET, you can request Amazon S3 to use an
AWS KMS key by adding the `ServerSideEncryptionMethod` property as
shown in the following request:

```
PutObjectRequest putRequest = new PutObjectRequest
 {
     BucketName = ``amzn-s3-demo-bucket``,
     Key = `keyName`,
     // other properties
     ServerSideEncryptionMethod = ServerSideEncryptionMethod.AWSKMS
 };
```

In this case, Amazon S3 uses the AWS managed key. For more information, see [Using server-side encryption with AWS KMS keys
(SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md"). You can
optionally create your own symmetric encryption customer managed key and specify that in the
request, as shown in the following example:

```
PutObjectRequest putRequest1 = new PutObjectRequest
{
  BucketName = ``amzn-s3-demo-bucket``,
  Key = `keyName`,
  // other properties
  ServerSideEncryptionMethod = ServerSideEncryptionMethod.AWSKMS,
  ServerSideEncryptionKeyManagementServiceKeyId = keyId
};
```

For more information about creating customer managed keys, see [Programming the AWS KMS API](../../../kms/latest/developerguide/programming-top.md "../../../kms/latest/developerguide/programming-top.md") in
the _AWS Key Management Service Developer Guide_.

For working code examples of uploading an object, see the following topics. To
use these examples, you must update the code examples and provide encryption
information as shown in the preceding code fragment.

- For uploading an object in a single operation, see [Uploading objects](upload-objects.md "upload-objects.md").
- For multipart uploads that use the high-level or low-level multipart upload
  API operations, see [Uploading an object using multipart upload](mpu-upload-object.md "mpu-upload-object.md").

### Presigned URLs

Java
When creating a presigned URL for an object that's encrypted with an
AWS KMS key, you must explicitly specify Signature Version 4, as shown in the
following example:

```
ClientConfiguration clientConfiguration = new ClientConfiguration();
clientConfiguration.setSignerOverride("AWSS3V4SignerType");
AmazonS3Client s3client = new AmazonS3Client(
        new ProfileCredentialsProvider(), clientConfiguration);
...
```

For a code example, see [Sharing objects with presigned URLs](ShareObjectPreSignedURL.md "ShareObjectPreSignedURL.md").

.NET
When creating a presigned URL for an object that's encrypted with an
AWS KMS key, you must explicitly specify Signature Version 4, as shown in the
following example:

```
AWSConfigs.S3Config.UseSignatureVersion4 = true;
```

For a code example, see [Sharing objects with presigned URLs](ShareObjectPreSignedURL.md "ShareObjectPreSignedURL.md").
