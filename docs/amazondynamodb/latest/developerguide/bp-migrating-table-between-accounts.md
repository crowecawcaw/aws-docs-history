# Migrating a DynamoDB table from one account to another

You can migrate an Amazon DynamoDB table from one account to another to implement a multi-account
strategy or a backup strategy. You can also do it for testing, debugging, or compliance reasons.
A common use case is copying DynamoDB tables across production, staging, test, and development
environments where each environment utilizes a different AWS account.

DynamoDB offers two options for migrating tables from one AWS account to another:

- **AWS Backup for Cross-Account Backup and Restore:** AWS Backup is a
  fully managed backup service that enables you to centrally manage backups across multiple
  AWS services. With its cross-account backup and restore functionality, you can back up a
  DynamoDB table in one account and restore the backup to another account in the same AWS
  Organization.
- **DynamoDB Export and Import to Amazon S3:** Using the DynamoDB Export
  and Import to Amazon S3 features allows you to do a full export to an Amazon S3 bucket and then import
  that data into a new table in another AWS account. This approach is suitable when you need
  to migrate between accounts that are not part of the same AWS Organization or if you do
  not want to use AWS Backup.

###### Note

Import from Amazon S3 does not support tables with Local Secondary Indexes (LSIs), but it does
support Global Secondary Indexes (GSIs). For more information on LSIs and GSIs, see [Improving data access with secondary indexes in DynamoDB](SecondaryIndexes.md "SecondaryIndexes.md").

###### Topics

- [Migrate a table using AWS Backup for cross-account backup and restore](bp-migrating-table-between-accounts-backup.md "bp-migrating-table-between-accounts-backup.md")
- [Migrate a table using export to S3 and import from S3](bp-migrating-table-between-accounts-s3.md "bp-migrating-table-between-accounts-s3.md")
