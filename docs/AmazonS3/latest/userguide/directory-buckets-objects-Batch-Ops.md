# Using Batch Operations with directory buckets

You can use Amazon S3 Batch Operations to perform operations on objects stored in S3 buckets. To
learn more about S3 Batch Operations, see [Performing large-scale batch operations
on Amazon S3 objects](batch-ops.md "batch-ops.md").

The following topics discuss performing batch operations on objects stored in the
S3 Express One Zone storage class in directory buckets.

###### Topics

- [Using Batch Operations with directory buckets](#UsingBOPsDirectoryBuckets "#UsingBOPsDirectoryBuckets")
- [Key differences](#UsingBOPsDirectoryBucketsKeyDiffs "#UsingBOPsDirectoryBucketsKeyDiffs")

## Using Batch Operations with directory buckets

You can perform the **Copy** operation and the **Invoke
AWS Lambda function** operations on objects that are stored in
directory buckets. With **Copy**, you can copy objects between
buckets of the same type (for example, from a directory bucket to a
directory bucket). You can also copy between general purpose buckets and
directory buckets. With **Invoke AWS Lambda function**, you can use a
Lambda function to perform actions on objects in your directory bucket with code that
you define.

###### Copying objects

You can copy between the same bucket type or between directory buckets and general
purpose buckets. When you copy to a directory bucket, you must use the correct
Amazon Resource Name (ARN) format for this bucket type. The ARN format for a
directory bucket is `arn:aws:s3express:`region`:`account-id`:bucket/`bucket-base-name`--x-s3`.

###### Note

Copying objects across different AWS Regions isn't supported when the source or destination bucket is in an AWS Local Zone. The
source and destination buckets must have the same parent AWS Region. The source and destination buckets can be different bucket location types (Availability Zone or Local Zone).

You can also populate your directory bucket with data by using the
**Import** action in the S3 console.
**Import** is a streamlined method for creating Batch Operations jobs
to copy objects from general purpose buckets to directory buckets. For
**Import** copy jobs from general purpose buckets to
directory buckets, S3 automatically generates a manifest. For more information,
see [Importing objects to a
directory bucket](create-import-job.md "create-import-job.md") and [Specifying a
manifest](specify-batchjob-manifest.md "specify-batchjob-manifest.md").

###### Invoking Lambda functions (`LambdaInvoke`)

There are special requirements for using Batch Operations to invoke Lambda functions that
act on directory buckets. For example, you must structure your Lambda request by
using a v2 JSON invocation schema, and specify
InvocationSchemaVersion 2.0 when you create the job. For more
information, see [Invoke AWS Lambda
function](batch-ops-invoke-lambda.md "batch-ops-invoke-lambda.md").

## Key differences

The following is a list of key differences when you're using Batch Operations to perform
bulk operations on objects that are stored in directory buckets with the
S3 Express One Zone storage class:

- For
  directory buckets, SSE-S3 and server-side encryption with AWS Key Management Service (AWS KMS)
  keys (SSE-KMS) are supported. If you make a
  `CopyObject` request that specifies to use server-side encryption with
  customer-provided keys (SSE-C) on a directory bucket (source or destination), the response
  returns an HTTP `400 (Bad Request)` error.

We recommend that the bucket's default encryption uses the desired encryption configuration and you don't override the bucket default encryption in your
`CreateSession` requests or `PUT` object requests. Then, new objects
are automatically encrypted with the desired encryption settings.
For more information about the encryption overriding behaviors in directory buckets and how to encrypt new object copies in a directory bucket with SSE-KMS, see [Specifying server-side encryption with AWS KMS for new object uploads](s3-express-specifying-kms-encryption.md "s3-express-specifying-kms-encryption.md").

S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [the Copy operation in Batch Operations](directory-buckets-objects-Batch-Ops.md "directory-buckets-objects-Batch-Ops.md"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.
For more information about using SSE-KMS on directory buckets, see [Setting and monitoring default encryption for directory buckets](s3-express-bucket-encryption.md "s3-express-bucket-encryption.md") and [Using server-side encryption with AWS KMS keys (SSE-KMS) in directory buckets](s3-express-UsingKMSEncryption.md "s3-express-UsingKMSEncryption.md").

- Objects in directory buckets can't be tagged. You can only specify an empty
  tag set. By default, Batch Operations copies tags. If you copy an object that has tags
  between general purpose buckets and directory buckets, you receive a `501 (Not
Implemented)` response.
- S3 Express One Zone offers you the option to choose the checksum algorithm that is
  used to validate your data during uploads or downloads. You can select one of
  the following Secure Hash Algorithms (SHA) or Cyclic Redundancy Check (CRC)
  data-integrity check algorithms: CRC32, CRC32, SHA-1, and SHA-256. MD5-based
  checksums are not supported with the S3 Express One Zone storage class.
- By default, all Amazon S3 buckets set the S3 Object Ownership setting to bucket
  owner enforced and access control lists (ACLs) are disabled. For directory
  buckets, this setting can't be modified. You can copy an object from general
  purpose buckets to directory buckets. However, you can't overwrite the default
  ACL when you copy to or from a directory bucket.
- Regardless of how you specify your manifest, the list itself must be stored in
  a general purpose bucket. Batch Operations can't import existing manifests from (or
  save generated manifests to) directory buckets. However, objects described
  within the manifest can be stored in directory buckets.
- Batch Operations can't specify a directory bucket as a location in an S3 Inventory
  report. Inventory reports don't support directory buckets. You can create a
  manifest file for objects within a directory bucket by using the
  `ListObjectsV2` API operation to list the objects. You can then
  insert the list in a CSV file.

### Granting access

To perform copy jobs, you must have the following permissions:

- To copy objects from one directory bucket to another directory bucket,
  you must have the `s3express:CreateSession` permission.
- To copy objects from directory buckets to general purpose buckets, you must
  have the `s3express:CreateSession` permission and the
  `s3:PutObject` permission to write the object copy to the
  destination bucket.
- To copy objects from general purpose buckets to directory buckets, you must
  have the `s3express:CreateSession` permission and the
  `s3:GetObject` permission to read the source object that is
  being copied.

For more information, see [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") in the _Amazon Simple Storage Service API Reference_.

- To invoke a Lambda function, you must grant permissions to your resource
  based on your Lambda function. To determine which permissions are required,
  check the corresponding API operations.
