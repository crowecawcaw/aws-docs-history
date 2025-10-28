# Migrate from previous KCL versions

This topic explains how to migrate from previous versions of the Kinesis Client Library
(KCL).

## What's new in KCL 3.0?

Kinesis Client Library (KCL) 3.0 introduces several major enhancements compared
to previous versions:

- It lowers compute costs for consumer applications by automatically
  redistributing the work from over-utilized workers to under-utilized workers in
  the consumer application fleet. This new load balancing algorithm ensures the
  evenly distributed CPU utilization across workers and removes the need to
  over-provision workers.
- It reduces the DynamoDB cost associated with KCL by optimizing read operations
  on the lease table.
- It minimizes reprocessing of data when leases are reassigned to another worker
  by allowing the current worker to complete checkpointing the records that it has
  processed.
- It uses AWS SDK for Java 2.x for improved performance and security features, fully
  removing the dependency on AWS SDK for Java 1.x.

For more information, see [KCL
3.0 release note](https://github.com/awslabs/amazon-kinesis-client/blob/master/CHANGELOG.md "https://github.com/awslabs/amazon-kinesis-client/blob/master/CHANGELOG.md").

###### Topics

- [Migrate from KCL 2.x to KCL
  3.x](kcl-migration-from-2-3.md "kcl-migration-from-2-3.md")
- [Roll back to the previous KCL
  version](kcl-migration-rollback.md "kcl-migration-rollback.md")
- [Roll forward to KCL 3.x after a
  rollback](kcl-migration-rollforward.md "kcl-migration-rollforward.md")
- [Best practices for the lease table with
  provisioned capacity mode](kcl-migration-lease-table.md "kcl-migration-lease-table.md")
- [Migrating from KCL 1.x to KCL
  3.x](kcl-migration-1-3.md "kcl-migration-1-3.md")
