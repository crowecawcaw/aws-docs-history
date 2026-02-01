# Update object encryption

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
The Batch Operations [`UpdateObjectEncryption`](../API/API_control_UpdateObjectEncryptionOperation.md "../API/API_control_UpdateObjectEncryptionOperation.md") operation updates the
server-side encryption type of more than one Amazon S3 object with a single request.
A single `UpdateObjectEncryption` operation job can support a manifest with up to 20 billion objects.

The `UpdateObjectEncryption` operation is supported for all Amazon S3 storage
classes that are supported by general purpose buckets. You can use the `UpdateObjectEncryption`
operation to change encrypted objects from [server-side encryption with Amazon S3 managed keys (SSE- S3)](UsingServerSideEncryption.md "UsingServerSideEncryption.md") to
[AWS Key Management Service (AWS KMS) keys (SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md"), or to apply S3 Bucket Keys.
You can also use the `UpdateObjectEncryption` operation to change the customer-managed
KMS key used to encrypt your data so that you can comply with custom key-rotation standards.

When you create a Batch Operations job, you can generate an object list based on the source
location and filter criteria that you specify. You can use the
`MatchAnyObjectEncryption` filter to generate a list of objects from your
bucket that you want to update and include in your manifest. The generated object list
includes only source bucket objects with the indicated server-side encryption type. If you
select SSE-KMS, you can optionally further filter your results by specifying a specific KMS
Key ARN and Bucket Key enabled status. For more information, see [`JobManifestGeneratorFilter`](../API/API_control_JobManifestGeneratorFilter.md "../API/API_control_JobManifestGeneratorFilter.md") and [`SSEKMSFilter` in the
_Amazon S3API Reference_](../API/API_control_SSEKMSFilter.md "../API/API_control_SSEKMSFilter.md").

## Restrictions and considerations

When you're using the Batch Operations `UpdateObjectEncryption` operation, the following
restrictions and considerations apply:

- The `UpdateObjectEncryption` operation doesn't support objects that are unencrypted
  or objects that are encrypted with either dual-layer server-side encryption with AWS KMS keys
  (DSSE-KMS) or customer-provided encryption keys (SSE-C). Additionally, you cannot specify SSE-S3
  encryption type `UpdateObjectEncryption` request.
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
  had their server-side encryption type updated from SSE-S3 to SSE-KMS, you may need additional
  permissions. On the source region bucket, you must have `kms:decrypt` permissions.
  Then, you will need the `kms:decrypt` and `kms:encrypt` permissions for
  the bucket in the destination region.
- Provide a full KMS key ARN in your `UpdateObjectEncryption` request. You can't
  use an alias name or alias ARN. You can determine the full KMS Key ARN in the AWS KMS Console
  or using the AWS KMS `DescribeKey` API.

For more information about `UpdateObjectEncryption`, see [Updating server-side encryption for existing data](update-sse-encryption.md "update-sse-encryption.md").

## Required permissions

To perform the `UpdateObjectEncryption` operation, add the following AWS Identity and Access Management (IAM)
policy to your IAM principal (user, role, or group). To use this policy, replace
`amzn-s3-demo-bucket` with the name of the bucket that
contains the objects that you want to update encryption for. Replace
`amzn-s3-demo-manifest-bucket` with the name of the bucket
that contains your manifest, and replace
`amzn-s3-demo-completion-report-bucket` with the name of the
bucket where you want to store your completion report.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3BatchOperationsUpdateEncryption",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:PutObject",
                "s3:UpdateObjectEncryption"
            ],
            "Resource": [
                 "arn:aws:s3:::`amzn-s3-demo-bucket-target`"
                "arn:aws:s3:::`amzn-s3-demo-bucket-target`-target/*"
            ]
        },
        {
            "Sid": "S3BatchOperationsPolicyForManifestFile",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket-manifest`/*"
            ]
        },
        {
            "Sid": "S3BatchOperationsPolicyForCompletionReport",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket-completion-report`/*"
            ]
        },
        {
            "Sid": "S3BatchOperationsPolicyManifestGeneration",
            "Effect": "Allow",
            "Action": [
                "s3:PutInventoryConfiguration"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket-target`"
            ]
        },
        {
            "Sid": "AllowKMSOperationsForS3BatchOperations",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:Encrypt",
                "kms:ReEncrypt*"
            ],
            "Resource": [                "arn:aws:kms:`us-east-1`:111122223333:key/`01234567-89ab-cdef-0123-456789abcdef`"
            ]
        }
    ]
}
```

For the trust policy and permissions policy that you must attach to the IAM role that the
S3 Batch Operations service principal assumes to run Batch Operations jobs on your behalf, see [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md") and [Update object encryption](batch-ops-iam-role-policies.md#batch-ops-update-encryption-policies "batch-ops-iam-role-policies.md#batch-ops-update-encryption-policies").
