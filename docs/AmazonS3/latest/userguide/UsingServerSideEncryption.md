# Using server-side encryption with Amazon S3 managed keys

(SSE-S3)

###### Important

Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3. Starting January 5, 2023, all new object uploads to Amazon S3 are automatically encrypted at no additional cost and with no impact on performance. The automatic encryption status for S3 bucket default encryption configuration and for new object uploads is available in CloudTrail logs, S3 Inventory, S3 Storage Lens, the Amazon S3 console, and as an additional Amazon S3 API response header in the AWS CLI and AWS SDKs. For more information, see [Default encryption FAQ](default-encryption-faq.md "default-encryption-faq.md").

All new object uploads to Amazon S3 buckets are encrypted by default with server-side encryption
with Amazon S3 managed keys (SSE-S3).

Server-side encryption protects data at rest. Amazon S3 encrypts each object with a unique key.
As an additional safeguard, it encrypts the key itself with a key that it rotates regularly.
Amazon S3 server-side encryption uses 256-bit Advanced Encryption Standard Galois/Counter Mode (AES-GCM) to encrypt all uploaded objects.

There are no additional fees for using server-side encryption with Amazon S3 managed keys
(SSE-S3). However, requests to configure the default encryption feature incur standard Amazon S3
request charges. For information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

If you require your data uploads to be encrypted using only Amazon S3 managed keys, you can use
the following bucket policy. For example, the following bucket policy denies permissions to
upload an object unless the request includes the `x-amz-server-side-encryption`
header to request server-side encryption:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PutObjectPolicy",
 "Statement": [
 {
 "Sid": "DenyObjectsThatAreNotSSES3",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
 "Condition": {
 "StringNotEquals": {
 "s3:x-amz-server-side-encryption": "AES256"
 }
 }
 }
 ]
}`

```

###### Note

Server-side encryption encrypts only the object data, not the object metadata.

## API support for server-side

encryption

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

To configure server-side encryption by using the object creation REST APIs, you must
provide the `x-amz-server-side-encryption` request header. For information
about the REST APIs, see [Using the REST API](specifying-s3-encryption.md#SSEUsingRESTAPI "specifying-s3-encryption.md#SSEUsingRESTAPI").

The following Amazon S3 APIs support this header:

- **PUT operations** – Specify the request
  header when uploading data using the `PUT` API. For more information,
  see [PUT Object](../API/RESTObjectPUT.md "../API/RESTObjectPUT.md").
- **Initiate Multipart Upload** – Specify
  the header in the initiate request when uploading large objects using the
  multipart upload API operation. For more information, see [Initiate Multipart
  Upload](../API/mpUploadInitiate.md "../API/mpUploadInitiate.md").
- **COPY operations** – When you copy an
  object, you have both a source object and a target object. For more information,
  see [PUT Object -
  Copy](../API/RESTObjectCOPY.md "../API/RESTObjectCOPY.md").

###### Note

When using a `POST` operation to upload an object, instead of providing
the request header, you provide the same information in the form fields. For more
information, see [POST Object](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md").

The AWS SDKs also provide wrapper APIs that you can use to
request server-side encryption. You can also use the AWS Management Console to upload objects and
request server-side encryption.

For more general information, see [AWS KMS
concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the _AWS Key Management Service Developer Guide_.

###### Topics

- [Specifying server-side encryption with Amazon S3 managed
  keys (SSE-S3)](specifying-s3-encryption.md "specifying-s3-encryption.md")
