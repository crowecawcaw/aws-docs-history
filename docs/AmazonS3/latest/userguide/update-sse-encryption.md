# Updating server-side encryption for existing data

All Amazon S3 buckets have encryption configured by default, and objects are automatically encrypted by
using server-side encryption with Amazon S3 managed keys (SSE-S3). This default encryption setting applies to
all new objects in your Amazon S3 buckets.

Using the `UpdateObjectEncryption` API operation, you can atomically update the server-side
encryption type of an existing encrypted object in a general purpose bucket from server-side encryption
with Amazon S3 managed encryption (SSE-S3) to server-side encryption with AWS Key Management Service (AWS KMS) encryption keys
(SSE-KMS). The `UpdateObjectEncryption` API operation uses [envelope encryption](../../../kms/latest/developerguide/kms-cryptography.md#enveloping "../../../kms/latest/developerguide/kms-cryptography.md#enveloping") to
re-encrypt the data key used to encrypt and decrypt your object with your newly specified server-side
encryption type.

Amazon S3 performs this encryption type update without any data movement. In other words, when you use the
`UpdateObjectEncryption` operation, your data isn't copied, archived objects in the
S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive aren't restored, and objects in the S3 Intelligent-Tiering
storage class aren't moved between tiers. Additionally, the `UpdateObjectEncryption` operation
preserves all object metadata properties, including the storage class, creation date, last modified date,
ETag, and checksum properties.

The `UpdateObjectEncryption` operation is supported for all S3 storage classes that are
supported by general purpose buckets. You can use the `UpdateObjectEncryption` operation to do
the following:

- Change encrypted objects from server-side encryption with Amazon S3 managed encryption (SSE-S3) to
  server-side encryption with AWS Key Management Service (AWS KMS) encryption keys (SSE-KMS).
- Update object-level SSE-KMS encrypted objects to use S3 Bucket Keys, which decreases the AWS KMS request
  traffic from Amazon S3 to AWS KMS. For more information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md").
- Change the customer-managed KMS key that's used to encrypt your data so that you can comply with
  custom key-rotation standards.

###### Note

Source objects that are unencrypted, or encrypted with either dual-layer server-side encryption with
AWS KMS keys (DSSE-KMS) or customer-provided encryption keys (SSE-C) aren't supported by this
operation.

The `UpdateObjectEncryption` operation is typically completed in milliseconds regardless of
the size of the object or the storage class, including S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive. This
operation doesn't count as an access for S3 Intelligent-Tiering, so objects in the Infrequent Access tier or the
Archive Instant Access tier won't automatically tier back to the Frequent Access tier if you change the server-side
encryption type of your object.

`UpdateObjectEncryption` is an object-level (data plane) API operation that's logged to
Amazon S3 server access logs and AWS CloudTrail data events. For more information, see [Logging options for Amazon S3](logging-with-S3.md "logging-with-S3.md").

The `UpdateObjectEncryption` operation is priced the same as `PUT`,
`COPY`, `POST`, and `LIST` requests (per 1,000 requests) and is always
charged as an S3 Standard storage class request regardless of the underlying object's storage class. For
more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Restrictions and considerations

When using the `UpdateObjectEncryption` operation, the following restrictions and
considerations apply:

- The `UpdateObjectEncryption` operation doesn't support objects that are unencrypted
  or objects that are encrypted with either dual-layer server-side encryption with AWS KMS keys
  (DSSE-KMS) or customer-provided encryption keys (SSE-C). Additionally, you cannot specify SSE-S3
  as the requested new encryption type `UpdateObjectEncryption` request.
- You can use the `UpdateObjectEncryption` operation to update objects in buckets that
  have S3 Versioning enabled. To update the encryption type of a particular version, you must specify a
  version ID in your `UpdateObjectEncryption` request. If you don't specify version ID, the
  `UpdateObjectEncryption` request acts on the current version of the object. For more
  information about S3 Versioning, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").
- The `UpdateObjectEncryption` operation fails on any object that has an
  S3 Object Lock retention mode or legal hold applied to it. If an object has a governance-mode
  retention period or a legal hold, you must first remove the Object Lock status on the object before
  you issue your `UpdateObjectEncryption` request. You can't use the
  `UpdateObjectEncryption` operation with objects that have an Object Lock compliance
  mode retention period applied to them. For more information about S3 Object Lock, see [Locking objects with Object Lock](object-lock.md "object-lock.md").
- `UpdateObjectEncryption` requests on source buckets with live replication enabled
  won't initiate replica events in the destination bucket. If you want to change the encryption type
  of objects in both your source and destination buckets, you must initiate separate
  `UpdateObjectEncryption` requests on the objects in the source and destination
  buckets.
- By default, all `UpdateObjectEncryption` requests that specify a customer-managed
  KMS key are restricted to KMS keys that are owned by the bucket owner's AWS account. If you're
  using AWS Organizations, you can request the ability to use AWS KMS keys owned by other member accounts
  within your organization by contacting AWS Support.
- If you use S3 Batch Replication to replicate datasets cross region and your objects previously
  had their server-side encryption type updated from SSE-S3 to SSE-KMS, you might need additional
  permissions. On the source region bucket, you must have `kms:decrypt` permissions.
  Then, you will need the `kms:decrypt` and `kms:encrypt` permissions for
  the bucket in the destination region.
- You must provide a full KMS key ARN in your `UpdateObjectEncryption` request.
  You can't use an alias name or alias ARN. You can determine the full KMS Key ARN in the AWS KMS
  Console or using the AWS KMS `DescribeKey` API.

## Required permissions

To perform the `UpdateObjectEncryption` operation, you must have the following
permissions:

- `s3:PutObject`
- `s3:UpdateObjectEncryption`
- `kms:Encrypt`
- `kms:Decrypt`
- `kms:GenerateDataKey`
- `kms:ReEncrypt*`

If you're using AWS Organizations, to use this operation with customer-managed KMS keys from other
AWS accounts within your organization, you must have the `organizations:DescribeAccount`
permission. You must also request the ability to use AWS KMS keys owned by other member accounts
within your organization by contacting AWS Support.

To perform the `UpdateObjectEncryption` operation, add the following AWS Identity and Access Management (IAM)
policy to your IAM role. To use this policy, replace `amzn-s3-demo-bucket` with the name of
your general purpose bucket, and replace the other `user input
 placeholders` with your own information.

```
{
    "Version": "2012-10-17",
    "Statement": [{
            "Sid": "AllowUpdateObjectEncryption",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:UpdateObjectEncryption",
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:ReEncrypt*",
                "organizations:DescribeAccount"
            ],
            "Resource": [
                "arn:aws:s3:::``amzn-s3-demo-bucket``",
                "arn:aws:s3:::``amzn-s3-demo-bucket``/*",
                "arn:aws:kms:`us-east-1`:`111122223333`:key/`01234567-89ab-cdef-0123-456789abcdef`"
            ]
        }
    ]
}
```

## Updating encryption in bulk

To update the server-side encryption type of more than one Amazon S3 object with a single request, you
can use S3 Batch Operations. You can provide S3 Batch Operations with a list of objects to operate on, or you can
direct Batch Operations to generate an object list based object metadata, including prefix, storage class,
creation date, encryption type, KMS key ARN, or S3 Bucket Key status. S3 Batch Operations calls the
respective API operation to perform the specified operation. A single Batch Operations job can perform the
specified operation on billions of objects within a bucket containing petabytes of data. For more
information about Batch Operations, see [Performing object operations in bulk with Batch Operations](batch-ops.md "batch-ops.md").

The S3 Batch Operations feature tracks progress, sends notifications, and stores a detailed completion
report of all actions, providing a fully managed, auditable, serverless experience. You can use
S3 Batch Operations through the Amazon S3 console, AWS Command Line Interface (AWS CLI) AWS SDKs, or the Amazon S3 REST API. For more
information, see [Update object encryption](batch-ops-update-encryption.md "batch-ops-update-encryption.md").

## Updating encryption for objects

You can update the server-side encryption type for an object through the AWS Command Line Interface (AWS CLI) AWS
SDKs, or the Amazon S3 REST API.

### Update encryption for an object

To run the following commands, you must have the AWS CLI installed and configured. If you don’t
have the AWS CLI installed, see [Install or update to the latest version
of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

Alternatively, you can run AWS CLI commands from the console by using AWS CloudShell. AWS CloudShell is a
browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. For more
information, see [What
is CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") and [Getting started with AWS CloudShell](../../../cloudshell/latest/userguide/getting-started.md "../../../cloudshell/latest/userguide/getting-started.md") in
the _AWS CloudShell User Guide_.

###### To update encryption for an object by using the AWS CLI

To use the following example command, replace the `user input
 placeholders` with your own information.

1. Use the following command to update encryption for a single object
   (`index.html`) in your general purpose bucket (for
   example, `amzn-s3-demo-bucket`) to use SSE-KMS with an S3 Bucket Key:

```
aws s3api update-object-encryption \
--bucket `amzn-s3-demo-bucket` \
--key `index.html` \
--object-encryption '{"SSEKMS": { "KMSKeyArn": "arn:aws:kms:us-east-1:111122223333:key/f12a345a-678e-9bbb-1025-62e317037583", "BucketKeyEnabled": true }}'
```

###### Note

You must specify the full AWS KMS key Amazon Resource Name (ARN). The KMS key ID and
KMS key alias aren't supported. 2. Run the `head-object` command to view the updated encryption type of your
object:

```
aws s3api head-object --bucket ``amzn-s3-demo-bucket`` --key `index.html`
```

You can send REST requests to update encryption for an object. For more information, see
[UpdateObjectEncryption](../API/API_UpdateObjectEncryption.md "../API/API_UpdateObjectEncryption.md").

You can use the AWS SDKs to update encryption for an object. For more information, see the
[list of supported SDKs](../API/API_UpdateObjectEncryption.md#API_UpdateObjectEncryption_SeeAlso "../API/API_UpdateObjectEncryption.md#API_UpdateObjectEncryption_SeeAlso").

Java

###### Example

The following AWS SDK for Java 2.x example updates the encryption type to SSE-KMS for an
object in a general purpose bucket.

```
    public void updateObjectEncryption(String bucketName,
                                       String objectKey,
                                       String versionId,
                                       String kmsKeyArn,
                                       boolean bucketKeyEnabled) {
        // Create the target object encryption type.
        ObjectEncryption objectEncryption = ObjectEncryption.builder()
                .ssekms(SSEKMSEncryption.builder()
                        .kmsKeyArn(kmsKeyArn)
                        .bucketKeyEnabled(bucketKeyEnabled)
                        .build())
                .build();

        // Create the UpdateObjectEncryption request.
        UpdateObjectEncryptionRequest request = UpdateObjectEncryptionRequest.builder()
                .bucket(bucketName)
                .key(objectKey)
                .versionId(versionId)
                .objectEncryption(objectEncryption)
                .build();

        // Update the object encryption.
        try {
            getS3Client().updateObjectEncryption(request);
            logger.info("Object encryption updated to SSE-KMS for {} in bucket {}", objectKey, bucketName);
        } catch (S3Exception e) {
            logger.error("Failed to update to object encryption: {} - Error code: {}", e.awsErrorDetails().errorMessage(),
                    e.awsErrorDetails().errorCode());
            throw e;
        }
    }
```

Python

###### Example

The following AWS SDK for Python (Boto3) example shows how to update the encryption type to SSE-KMS
for an object in a general purpose bucket.

```
response = client.update_object_encryption(
    Bucket='string',
    Key='string',
    VersionId='string',
    ObjectEncryption={
        'SSEKMS': {
                'KMSKeyArn': 'string',
                'BucketKeyEnabled': True|False
        }
    }
)
```
