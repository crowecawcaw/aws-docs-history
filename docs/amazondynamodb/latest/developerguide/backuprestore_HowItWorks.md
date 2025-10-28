# Using on-demand DynamoDB backup and restore

Amazon DynamoDB supports stand-alone on-demand backup and restore features. Those features are
available to you independent of whether you use AWS Backup.

You can use the DynamoDB on-demand backup capability to create full backups of your tables for
long-term retention and archival for regulatory compliance needs. You can back up and restore
your table data anytime with a single click on the AWS Management Console or with a single API
call. Backup and restore actions run with zero impact on table performance or availability.

You can create table backups using the console, the AWS Command Line Interface (AWS CLI), or
the DynamoDB API. For more information, see [Backing up a DynamoDB table](Backup.md "Backup.md").

For information about restoring a table from a backup, see [Restoring a DynamoDB table from a backup](Restore.md "Restore.md").
