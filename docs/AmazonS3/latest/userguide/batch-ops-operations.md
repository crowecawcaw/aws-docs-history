# Operations supported by S3 Batch Operations

You can use S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
S3 Batch Operations can perform a single operation on lists of Amazon S3 objects that you specify. A
single job can perform a specified operation on billions of objects containing exabytes of data.
Amazon S3 tracks progress, sends notifications, and stores a detailed completion report of all
actions, providing a fully managed, auditable, and serverless experience. You can use
S3 Batch Operations through the Amazon S3 console, AWS CLI, AWS SDKs, or Amazon S3 REST API.

S3 Batch Operations supports the following operations:

- [Copy objects](batch-ops-copy-object.md "batch-ops-copy-object.md")
- [Compute checksums](batch-ops-compute-checksums.md "batch-ops-compute-checksums.md")
- [Delete all object tags](batch-ops-delete-object-tagging.md "batch-ops-delete-object-tagging.md")
- [Invoke AWS Lambda function](batch-ops-invoke-lambda.md "batch-ops-invoke-lambda.md")
- [Replace all object tags](batch-ops-put-object-tagging.md "batch-ops-put-object-tagging.md")
- [Replace access control list (ACL)](batch-ops-put-object-acl.md "batch-ops-put-object-acl.md")
- [Restore objects with Batch Operations](batch-ops-initiate-restore-object.md "batch-ops-initiate-restore-object.md")
- [Replicating existing objects with
  Batch Replication](s3-batch-replication-batch.md "s3-batch-replication-batch.md")
- [S3 Object Lock retention](batch-ops-retention-date.md "batch-ops-retention-date.md")
- [S3 Object Lock legal hold](batch-ops-legal-hold.md "batch-ops-legal-hold.md")
