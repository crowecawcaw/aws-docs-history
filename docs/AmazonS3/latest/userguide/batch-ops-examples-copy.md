# Copying objects using S3 Batch Operations

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
You can use S3 Batch Operations to create a **Copy** (`CopyObject`) job
to copy objects within the same account or to a different destination account.

The following examples show how to store and use a manifest that is in a different
account. The first example shows how you can use Amazon S3 Inventory to deliver the inventory
report to the destination account for use during job creation. The second example shows how to
use a comma-separated values (CSV) manifest in the source or destination account. The third
example shows how to use the **Copy** operation to enable S3 Bucket Keys for
existing objects that have been encrypted by using server-side encryption with AWS Key Management Service
(AWS KMS) keys (SSE-KMS).

###### Copy Operation Examples

- [Using an inventory report to copy objects across AWS accounts](specify-batchjob-manifest-xaccount-inventory.md "specify-batchjob-manifest-xaccount-inventory.md")
- [Using a CSV manifest to copy objects across AWS accounts](specify-batchjob-manifest-xaccount-csv.md "specify-batchjob-manifest-xaccount-csv.md")
- [Using Batch Operations to enable S3 Bucket Keys for SSE-KMS](batch-ops-copy-example-bucket-key.md "batch-ops-copy-example-bucket-key.md")
  For examples that show the copy operation with tags using the AWS CLI and AWS SDK for Java, see
  [Creating a Batch Operations job with job tags used for labeling](batch-ops-tags-create.md "batch-ops-tags-create.md").
