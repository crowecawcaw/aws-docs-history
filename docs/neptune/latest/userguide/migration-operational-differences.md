# Operational differences between Neptune and Neo4j

Neptune is a fully managed service that automates many of the normal operational
tasks you would have to do when using on-premise or self-managed databases such as Neo4j
Enterprise or Community Edition:

- **[Automated
  backups](backup-restore.md#backup-restore-overview-backups "backup-restore.md#backup-restore-overview-backups")**   –  
  Neptune backs up your cluster volume automatically and retains the backup for a
  retention period that you specify (from 1 to 35 days). These backups are continuous
  and incremental, so you can quickly restore to any point within the retention period.
  No performance impact or interruption of database service occurs as backup data is
  being written.
- **[Manual Snapshots](backup-restore.md "backup-restore.md")**   –  
  Neptune lets you make a storage-volume snapshot of your DB cluster to back up the entire
  DB cluster. This kind of snapshot can then be used to restore the database, make a copy
  of it, and share it across accounts.
- **[Cloning](manage-console-cloning.md "manage-console-cloning.md")**   –  
  Neptune supports a cloning feature that lets you create cost-effective clones of a database
  quickly. The clones use a copy-on-write protocol to require only minimal additional space after
  they are created. Database cloning is an effective way to try out new Neptune features or
  upgrades with no disruption to the originating cluster.
- **[Monitoring](monitoring.md "monitoring.md")**   –  
  Neptune provides various methods to monitor the performance and usage of your cluster,
  including:
  - Instance status
  - Integration with Amazon CloudWatch and AWS CloudTrail
  - Audit log capabilities
  - Event notifications
  - Tagging

- **[Security](security.md "security.md")**   –  
  Neptune provides a secure environment by default. A cluster resides within a private VPC
  that provides network isolation from other resources. All traffic is encrypted via SSL, and
  all data is encrypted at rest using AWS KMS.

In addition, Neptune integrates with AWS Identity and Access Management (IAM) to provide [authentication](iam-auth.md "iam-auth.md"). By specifying [IAM condition keys](iam-condition-keys.md "iam-condition-keys.md"), you can use IAM policies
to provide fine-grained access control over [data
actions](iam-data-access-policies.md "iam-data-access-policies.md").

## Tooling and integration differences between Neptune and Neo4j

Neptune has a different architecture for integrations and tools than Neo4j, which
may impact the architecture of your application. Neptune uses the compute resources
of the cluster to process queries, but leverages other best-in-class AWS services for
functionality like full-text search (using OpenSearch), ETL ( using Glue), and so forth.
For a full listing of these integrations, see [Neptune integrations](integrations.md "integrations.md").
