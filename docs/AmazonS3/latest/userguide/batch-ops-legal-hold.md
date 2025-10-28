# S3 Object Lock legal hold

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
You can use the **Object Lock legal hold** operation to place a legal hold
on an object version. Like setting a retention period, a legal hold prevents an object
version from being overwritten or deleted. However, a legal hold doesn't have an associated
retention period and remains in effect until it's removed.

You can use S3 Batch Operations with Object Lock to add legal holds to many Amazon S3 objects at
once. To do so, specify a list of the target objects in your manifest and submit that list
to Batch Operations. Your S3 Batch Operations **Object Lock legal hold** job runs
until completion, until cancellation, or until a failure state is reached.

S3 Batch Operations verifies that Object Lock is enabled on your S3 bucket before processing
any objects in the manifest. To perform the object operations and bucket-level validation,
S3 Batch Operations needs the `s3:PutObjectLegalHold` and
`s3:GetBucketObjectLockConfiguration` in an AWS Identity and Access Management (IAM) role. These
permissions allow S3 Batch Operations to call S3 Object Lock on your behalf.

When you create an S3 Batch Operations job to remove a legal hold, you only need to specify
`Off` as the legal hold status. For more information, see [Object Lock considerations](object-lock-managing.md "object-lock-managing.md").

For information about how to use this operation with the Amazon S3 REST API, see
`S3PutObjectLegalHold` in the [CreateJob](../API/API_control_CreateJob.md "../API/API_control_CreateJob.md") operation
in the _Amazon Simple Storage Service API Reference_.

For an example of using this operation, see [Using the AWS SDK for Java](batch-ops-legal-hold-off.md#batch-ops-examples-java-object-lock-legalhold "batch-ops-legal-hold-off.md#batch-ops-examples-java-object-lock-legalhold").

## Restrictions and limitations

When you're using Batch Operations to apply or remove an Object Lock legal hold, the
following restrictions and limitations apply:

- S3 Batch Operations doesn't make any bucket-level changes.
- All objects listed in the manifest must be in the same bucket.
- Versioning and S3 Object Lock must be configured on the bucket where the job
  is performed.
- The **Object Lock legal hold** operation works on the latest
  version of the object unless a version is explicitly specified in the
  manifest.
- The `s3:PutObjectLegalHold` permission is required in your IAM
  role to add or remove a legal hold from objects.
- The `s3:GetBucketObjectLockConfiguration` IAM permission is
  required to confirm that S3 Object Lock is enabled for the S3 bucket where the
  job is performed.
- A single S3 Object Lock legal hold job can support a manifest with up to 20 billion objects.
