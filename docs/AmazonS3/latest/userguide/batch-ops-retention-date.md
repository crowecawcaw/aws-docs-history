# S3 Object Lock retention

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
You can use the **Object Lock retention** operation to apply retention
dates for your objects by using either _governance_ mode or
_compliance_ mode. These retention modes apply different levels of
protection. You can apply either retention mode to any object version. Retention dates, like
legal holds, prevent an object from being overwritten or deleted. Amazon S3 stores the
_retain until date_ specified in the object's metadata and protects
the specified version of the object version until the retention period expires.

You can use S3 Batch Operations with Object Lock to manage the retention dates of many Amazon S3
objects at once. You specify the list of target objects in your manifest and submit the
manifest to Batch Operations for completion. For more information, see S3 Object Lock [Retention periods](object-lock.md#object-lock-retention-periods "object-lock.md#object-lock-retention-periods").

Your S3 Batch Operations job with retention dates runs until completion, until cancellation, or
until a failure state is reached. We recommend using S3 Batch Operations and S3 Object Lock
retention when you want to add, change, or remove the retention date for many objects with a
single request.

Batch Operations verifies that Object Lock is enabled on your bucket before processing any keys
in the manifest. To perform the operations and validation, Batch Operations needs the
`s3:GetBucketObjectLockConfiguration` and `s3:PutObjectRetention`
permissions in an AWS Identity and Access Management (IAM) role to allow Batch Operations to call Object Lock on your
behalf. For more information, see [Object Lock considerations](object-lock-managing.md "object-lock-managing.md").

For information about using this operation with the REST API, see
`S3PutObjectRetention` in the [CreateJob](../API/API_control_CreateJob.md "../API/API_control_CreateJob.md") operation
in the _Amazon Simple Storage Service API Reference_.

For an AWS Command Line Interface (AWS CLI) example of using this operation, see [Using the AWS CLI](batch-ops-object-lock-retention.md#batch-ops-cli-object-lock-retention-example "batch-ops-object-lock-retention.md#batch-ops-cli-object-lock-retention-example"). For an AWS SDK for Java example, see
[Using the AWS SDK for Java](batch-ops-object-lock-retention.md#batch-ops-examples-java-object-lock-retention "batch-ops-object-lock-retention.md#batch-ops-examples-java-object-lock-retention").

## Restrictions and limitations

When you're using Batch Operations to apply Object Lock retention periods, the following
restrictions and limitations apply:

- S3 Batch Operations doesn't make any bucket-level changes.
- Versioning and S3 Object Lock must be configured on the bucket where the job
  is performed.
- All objects listed in the manifest must be in the same bucket.
- The operation works on the latest version of the object unless a version is
  explicitly specified in the manifest.
- You need `s3:PutObjectRetention` permission in your IAM role to
  use an **Object Lock retention** job.
- The `s3:GetBucketObjectLockConfiguration` IAM permission is
  required to confirm that Object Lock is enabled for the S3 bucket that you're
  performing the job on.
- You can only extend the retention period of objects with
  `COMPLIANCE` mode retention dates applied, and this retention
  period can't be shortened.
- A single S3 Object Lock retention job can support a manifest with up to 20 billion objects.
