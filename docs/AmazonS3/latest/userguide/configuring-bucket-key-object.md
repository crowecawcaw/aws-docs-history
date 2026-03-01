# Configuring an S3 Bucket Key at the object level

When you perform a PUT or COPY operation using the REST API, AWS SDKs, or AWS CLI, you can
enable or disable an S3 Bucket Key at the object level by adding the
`x-amz-server-side-encryption-bucket-key-enabled` request header with a
`true` or `false` value. S3 Bucket Keys reduce the cost of server-side
encryption using AWS Key Management Service (AWS KMS) (SSE-KMS) by decreasing request traffic from Amazon S3 to AWS KMS.
For more information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md").

When you configure an S3 Bucket Key for an object using a PUT or COPY operation, Amazon S3 only
updates the settings for that object. The S3 Bucket Key settings for the destination bucket do
not change. If you submit a PUT or COPY request for a KMS-encrypted object into a bucket with
S3 Bucket Keys enabled, your object level operation will automatically use S3 Bucket Keys unless you disable
the keys in the request header. If you don't specify an S3 Bucket Key for your object, Amazon S3
applies the S3 Bucket Key settings for the destination bucket to the object.

###### Prerequisite:

Before you configure your object to use an S3 Bucket Key, review  [Changes to note before enabling an S3 Bucket Key](bucket-key.md#bucket-key-changes "bucket-key.md#bucket-key-changes").

###### Topics

- [Amazon S3 Batch Operations](#bucket-key-object-bops "#bucket-key-object-bops")
- [Using the REST API](#bucket-key-object-rest "#bucket-key-object-rest")
- [Using the AWS SDK for Java (PutObject)](#bucket-key-object-sdk "#bucket-key-object-sdk")
- [Using the AWS CLI (PutObject)](#bucket-key-object-cli "#bucket-key-object-cli")

## Amazon S3 Batch Operations

To encrypt your existing Amazon S3 objects, you can use Amazon S3 Batch Operations. You provide
S3 Batch Operations with a list of objects to operate on, and Batch Operations calls the respective API
to perform the specified operation.

You can use the [S3 Batch Operations Copy
operation](batch-ops-copy-object.md "batch-ops-copy-object.md") to copy existing unencrypted objects and write them back to the same
bucket as encrypted objects. A single Batch Operations job can perform the specified operation on
billions of objects. For more information, see [Performing object operations in bulk with Batch Operations](batch-ops.md "batch-ops.md") and [Encrypting objects with
Amazon S3 Batch Operations](https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations/ "https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations/").

## Using the REST API

When you use SSE-KMS, you can enable an S3 Bucket Key for an object by using the
following API operations:

- [PutObject](../API/API_PutObject.md "../API/API_PutObject.md") – When you upload an object, you can specify
  the `x-amz-server-side-encryption-bucket-key-enabled` request header to
  enable or disable an S3 Bucket Key at the object level.
- [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") – When you copy an object and configure SSE-KMS, you can
  specify the `x-amz-server-side-encryption-bucket-key-enabled` request header
  to enable or disable an S3 Bucket Key for your object.
- [POST
  Object](../API/RESTObjectPOST.md "../API/RESTObjectPOST.md") – When you use a `POST` operation to upload an object
  and configure SSE-KMS, you can use the
  `x-amz-server-side-encryption-bucket-key-enabled` form field to enable or
  disable an S3 Bucket Key for your object.
- [CreateMultipartUpload](../API/API_CreateMultipartUpload.md "../API/API_CreateMultipartUpload.md") – When you upload large objects by using the
  `CreateMultipartUpload` API operation and configure SSE-KMS, you can use
  the `x-amz-server-side-encryption-bucket-key-enabled` request header to
  enable or disable an S3 Bucket Key for your object.

To enable an S3 Bucket Key at the object level, include the
`x-amz-server-side-encryption-bucket-key-enabled` request header. For more
information about SSE-KMS and the REST API, see [Using the REST API](specifying-kms-encryption.md#KMSUsingRESTAPI "specifying-kms-encryption.md#KMSUsingRESTAPI").

## Using the AWS SDK for Java (PutObject)

You can use the following example to configure an S3 Bucket Key at the object level using
the AWS SDK for Java.

Java

```

AmazonS3 s3client = AmazonS3ClientBuilder.standard()
    .withRegion(Regions.DEFAULT_REGION)
    .build();

String bucketName = "`amzn-s3-demo-bucket1`";
String keyName = "`key name for object`";
String contents = "`file contents`";

PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, keyName, contents)
    .withBucketKeyEnabled(true);
    
s3client.putObject(putObjectRequest);

```

## Using the AWS CLI (PutObject)

You can use the following AWS CLI example to configure an S3 Bucket Key at the object level
as part of a `PutObject` request.

```
aws s3api put-object --bucket `amzn-s3-demo-bucket` --key `object key name` --server-side-encryption aws:kms --bucket-key-enabled --body `filepath`
```
