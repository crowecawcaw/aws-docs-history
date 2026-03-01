# Using server-side encryption with AWS KMS keys (SSE-KMS) in directory buckets

The security controls in AWS KMS can help you meet encryption-related compliance
requirements. You can choose to configure directory buckets to use server-side encryption with AWS Key Management Service (AWS KMS)
keys (SSE-KMS) and use these KMS keys to protect your data in Amazon S3 directory buckets. For more information about SSE-KMS, see [Using server-side encryption with AWS KMS keys (SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md").

###### Permissions

To upload or download an object encrypted with an AWS KMS key to or from Amazon S3, you need
`kms:GenerateDataKey` and `kms:Decrypt` permissions on the key. For more information, see [Allow key
users to use a KMS key for cryptographic operations](../../../kms/latest/developerguide/key-policies.md#key-policy-users-crypto "../../../kms/latest/developerguide/key-policies.md#key-policy-users-crypto") in the _AWS Key Management Service Developer Guide_. For
information about the AWS KMS permissions that are required for multipart uploads, see
[Multipart upload API and permissions](mpuoverview.md#mpuAndPermissions "mpuoverview.md#mpuAndPermissions").

For more information about KMS keys for SSE-KMS, see [Specifying server-side encryption with AWS KMS (SSE-KMS)](specifying-kms-encryption.md "specifying-kms-encryption.md").

###### Topics

- [AWS KMS keys](#s3-express-aws-managed-customer-managed-keys "#s3-express-aws-managed-customer-managed-keys")
- [Using SSE-KMS for cross-account operations](#s3-express-bucket-encryption-update-bucket-policy "#s3-express-bucket-encryption-update-bucket-policy")
- [Amazon S3 Bucket Keys](#s3-express-sse-kms-bucket-keys "#s3-express-sse-kms-bucket-keys")
- [Requiring SSE-KMS](#s3-express-require-sse-kms "#s3-express-require-sse-kms")
- [Encryption context](#s3-express-encryption-context "#s3-express-encryption-context")
- [Sending requests for AWS KMS encrypted objects](#s3-express-aws-signature-version-4-sse-kms "#s3-express-aws-signature-version-4-sse-kms")
- [Auditing SSE-KMS encryption in directory buckets](#s3-express-bucket-encryption-sse-auditing "#s3-express-bucket-encryption-sse-auditing")
- [Specifying server-side encryption with AWS KMS (SSE-KMS) for new object uploads in directory buckets](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md")

## AWS KMS keys

Your SSE-KMS configuration can only support 1 [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") per directory bucket for the lifetime of the bucket.
The [AWS managed key](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") (`aws/s3`) isn't supported. Also, after you specify a customer managed key for SSE-KMS, you can't override the customer managed key for the bucket's SSE-KMS configuration.

You can identify the customer managed key you specified for the bucket's SSE-KMS configuration, in the following way:

- You make a `HeadObject` API operation request to find the value of `x-amz-server-side-encryption-aws-kms-key-id` in your response.

To use a new customer managed key for your data, we recommend copying your existing objects to a new directory bucket with a new customer managed key.

When you specify an [AWS KMS customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.

For more information about KMS keys for SSE-KMS, see [AWS KMS keys](UsingKMSEncryption.md#aws-managed-customer-managed-keys "UsingKMSEncryption.md#aws-managed-customer-managed-keys").

## Using SSE-KMS for cross-account operations

When using encryption for cross-account operations in directory buckets, be aware of the following:

- If you want to grant cross-account access to your S3 objects, configure a policy of a customer managed key to allow access from another account.
- To specify a customer managed key, you must use a fully qualified
  KMS key ARN.

## Amazon S3 Bucket Keys

S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md"), [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"), [the Copy operation in Batch Operations](directory-buckets-objects-Batch-Ops.md "directory-buckets-objects-Batch-Ops.md"), or
[the import jobs](create-import-job.md "create-import-job.md"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.

For [Zonal endpoint (object-level) API operations](s3-express-differences.md#s3-express-differences-api-operations "s3-express-differences.md#s3-express-differences-api-operations") except [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") and [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md"),
you authenticate and authorize requests through [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md") for low latency.
We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your
`CreateSession` requests or `PUT` object requests. Then, new objects
are automatically encrypted with the desired encryption settings.
To encrypt new objects in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with an KMS key (specifically, a [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk")). Then, when a session is created for Zonal endpoint API operations, new objects are automatically encrypted and decrypted with SSE-KMS and S3 Bucket Keys during the session. For more information about the encryption overriding behaviors in directory buckets, see [Specifying server-side encryption with AWS KMS for new object uploads](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md").

S3 Bucket Keys are used for a time-limited period within Amazon S3,
further reducing the need for Amazon S3 to make requests to AWS KMS to complete encryption
operations. For more information about using S3 Bucket Keys, see [Amazon S3 Bucket Keys](UsingKMSEncryption.md#sse-kms-bucket-keys "UsingKMSEncryption.md#sse-kms-bucket-keys") and [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md").

## Requiring SSE-KMS

To require SSE-KMS of all objects in a particular directory bucket, you can
use a bucket policy. For example, when you use the `CreateSession` API operation to grant permission to upload a new object (`PutObject`, `CopyObject`,
and `CreateMultipartUpload`), the following bucket policy denies the upload object permission (`s3express:CreateSession`) to everyone if the `CreateSession` request doesn't include
an `x-amz-server-side-encryption-aws-kms-key-id` header that requests SSE-KMS.

JSON

```
`{
 "Version":"2012-10-17",
 "Id":"UploadObjectPolicy",
 "Statement":[{
 "Sid":"DenyObjectsThatAreNotSSEKMS",
 "Effect":"Deny",
 "Principal":"*",
 "Action":"s3express:CreateSession",
 "Resource":"arn:aws:s3express:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket--usw2-az1--x-s3`",
 "Condition":{
 "Null":{
 "s3express:x-amz-server-side-encryption-aws-kms-key-id":"true"
 }
 }
 }
 ]
}`

```

To require that a particular AWS KMS key be used to encrypt the objects in a
bucket, you can use the `s3express:x-amz-server-side-encryption-aws-kms-key-id`
condition key. To specify the KMS key, you must use a key Amazon Resource Name (ARN)
that is in the
`arn:aws:kms:`region`:`acct-id`:key/`key-id`` format. AWS Identity and Access Management does not validate if the string for`s3express:x-amz-server-side-encryption-aws-kms-key-id` exists.
The AWS KMS key ID that Amazon S3 uses for object encryption
must match the AWS KMS key ID in the policy, otherwise Amazon S3 denies the request.

For more information about how to use SSE-KMS for new object uploads, see [Specifying server-side encryption with AWS KMS (SSE-KMS) for new object uploads in directory buckets](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md").

For a complete list of specific condition keys for directory buckets, see [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md").

## Encryption context

For directory buckets, an _encryption context_ is a set of key-value pairs
that contains contextual information about the data. An additional encryption context value is not supported. For more information about the encryption
context, see [Encryption context](UsingKMSEncryption.md#encryption-context "UsingKMSEncryption.md#encryption-context").

By default, if you use SSE-KMS on a directory bucket, Amazon S3 uses the bucket Amazon Resource Name (ARN) as the encryption context pair:

```
arn:aws:s3express:`region`:`account-id`:bucket/`bucket-base-name`--`zone-id`--x-s3
```

Make sure your IAM policies or AWS KMS key policies
use your bucket ARN as the encryption context.

You can optionally provide an explicit encryption context pair by using the
`x-amz-server-side-encryption-context` header in a Zonal endpoint API request, such as [CreateSession](../API/API_CreateSession.md#API_CreateSession_RequestSyntax "../API/API_CreateSession.md#API_CreateSession_RequestSyntax"). The value of
this header is a Base64-encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs.
For directory buckets, the encryption context must match the default encryption context – the bucket Amazon Resource Name (ARN).
Also, because the encryption context is not
encrypted, make sure it does not include sensitive information.

You can use the encryption context to identify and categorize your cryptographic
operations. You can also use the default encryption context ARN value to track relevant
requests in AWS CloudTrail by viewing which directory bucket ARN was used with which encryption
key.

In the `requestParameters` field of a CloudTrail log file, if you use SSE-KMS on a directory bucket, the encryption context
value is the ARN of the bucket.

```
"encryptionContext": {
    "aws:s3express:arn": "arn:aws:s3:::`arn:aws:s3express:`region`:`account-id`:bucket/`bucket-base-name`--`zone-id`--x-s3`"
}
```

Also, for object encryption with SSE-KMS in a directory bucket, your AWS KMS CloudTrail events log your bucket ARN instead of
your object ARN.

## Sending requests for AWS KMS encrypted objects

Directory buckets can only be accessed through HTTPS (TLS). Also, directory buckets sign requests by using AWS Signature Version 4 (SigV4). For more information about
sending requests for AWS KMS encrypted objects, see [Sending requests for AWS KMS encrypted objects](UsingKMSEncryption.md#aws-signature-version-4-sse-kms "UsingKMSEncryption.md#aws-signature-version-4-sse-kms").

If your object uses SSE-KMS, don't send encryption request headers for
`GET` requests and `HEAD` requests. Otherwise, you’ll get
an **`HTTP 400 Bad Request`** error.

## Auditing SSE-KMS encryption in directory buckets

To audit the usage of your AWS KMS keys for your SSE-KMS encrypted data, you can use
AWS CloudTrail logs. You can get insight into your [cryptographic operations](../../../kms/latest/developerguide/concepts.md#cryptographic-operations "../../../kms/latest/developerguide/concepts.md#cryptographic-operations"), such as [GenerateDataKey](../../../kms/latest/developerguide/ct-generatedatakey.md "../../../kms/latest/developerguide/ct-generatedatakey.md") and [Decrypt](../../../kms/latest/developerguide/ct-decrypt.md "../../../kms/latest/developerguide/ct-decrypt.md").
CloudTrail supports numerous [attribute
values](../../../awscloudtrail/latest/APIReference/API_LookupEvents.md "../../../awscloudtrail/latest/APIReference/API_LookupEvents.md") for filtering your search, including event name, user name, and
event source.

###### Topics

- [Specifying server-side encryption with AWS KMS (SSE-KMS) for new object uploads in directory buckets](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md")
