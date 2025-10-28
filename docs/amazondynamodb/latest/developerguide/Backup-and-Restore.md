# Backup and restore for DynamoDB

DynamoDB offers on-demand backups and point-in-time recovery (PITR) backups to help protect
your DynamoDB data from disaster events and offers data archiving for long-term retention. You can
back up tables from a few megabytes to hundreds of terabytes of data, with no impact on
performance and availability to your production applications. All backups are automatically
encrypted, cataloged, and easily discoverable.

With on-demand backups, you can create a snapshot backup of your table that DynamoDB stores and
manages. You're charged based on the size and duration of your backups. Using on-demand backup,
you can restore your entire DynamoDB table to the exact state it was in when the backup was
created.

There are two options for creating and managing DynamoDB on-demand backups:

- DynamoDB
- [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md")
  You can use the DynamoDB on-demand backup capability to create full backups of your tables for
  long-term retention, and archiving for regulatory compliance needs. You can back up and restore
  your table data anytime from the AWS Management Console or with a single API call.

Point-in-time recovery (PITR) backups are fully managed by DynamoDB and provide up to 35 days
of recovery points at a per second granularity. To use point-in-time recovery, which are continuous backups, enable
point-in-time recovery (PITR) on your DynamoDB table. You get charged based on the size of your
DynamoDB table for the duration you have PITR enabled on the table. Enabling Point-in-Time Recovery
(PITR) on your DynamoDB table continuously backs up your data. This helps you restore your table to
a specific point in time within the PITR recovery period by creating a new DynamoDB table with the
exact state of your original table at that point in time.

Point-in-time recovery helps protect your DynamoDB tables from accidental write or delete
operations. With point-in-time recovery, you don't have to worry about creating, maintaining, or
scheduling on-demand backups. For example, suppose that a test script writes accidentally to a
production DynamoDB table.

With point-in-time recovery, you can restore your table to any point in time during the last
35 days. You can set the recovery period to any value between 1 and 35 days. After you enable
point-in-time recovery, you can restore to any point in time from five minutes before the
current time until the configured recovery period. DynamoDB maintains incremental backups of your
table.

In addition, point-in-time operations don't affect performance or API latencies.

You can restore a DynamoDB table to a point in time using the AWS Management Console, the AWS Command Line Interface (AWS CLI),
or the DynamoDB API. The point-in-time recovery process restores to a new table.

For more information about AWS Region availability and pricing, see [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing "https://aws.amazon.com/dynamodb/pricing").

###### Note

- Tagging and [attribute-based access
  control (ABAC)](access-control-resource-based.md "access-control-resource-based.md") aren't supported for DynamoDB backups. To use ABAC with backups, we
  recommend that you use [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md").
- Tags aren't preserved in restored tables. You need to add tags to restored tables
  before you can use tag-based conditions in your policies.
  The following video will give you an introductory look at the backup and restore concept and
  talk more about point-in-time recovery.

###### Topics

- [Point-in-time backups for DynamoDB](Point-in-time-recovery.md "Point-in-time-recovery.md")
- [Using on-demand DynamoDB backup and restore](backuprestore_HowItWorks.md "backuprestore_HowItWorks.md")
- [Understanding Amazon DynamoDB billing for backups](backup-restore-billing.md "backup-restore-billing.md")
- [Restore a table in DynamoDB](pointintimerecovery_restores.md "pointintimerecovery_restores.md")
- [Using AWS Backup with DynamoDB](backuprestore_HowItWorksAWS.md "backuprestore_HowItWorksAWS.md")
