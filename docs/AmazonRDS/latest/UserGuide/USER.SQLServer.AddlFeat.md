# Access to transaction log backups with RDS for SQL Server

With access to transaction log backups for RDS for SQL Server, you can list the transaction log backup files for a database and copy them
to a target Amazon S3 bucket. By copying transaction log backups in an Amazon S3 bucket, you can use them in combination with full and differential
database backups to perform point in time database restores. You use RDS stored procedures
to set up access to transaction log backups, list available transaction log backups, and copy them to your Amazon S3 bucket.

Access to transaction log backups provides the following capabilities and benefits:

- List and view the metadata of available transaction log backups for a database on an RDS for SQL Server DB instance.
- Copy available transaction log backups from RDS for SQL Server to a target Amazon S3 bucket.
- Perform point-in-time restores of databases without the need to restore an entire DB instance.
  For more information on restoring a DB instance to a point in time, see
  [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

## Availability and support

Access to transaction log backups is supported in all AWS Regions. Access to transaction log backups is available for all editions
and versions of Microsoft SQL Server supported on Amazon RDS.

## Requirements

The following requirements must be met before enabling access to transaction log backups:

- Automated backups must be enabled on the DB instance and the backup retention must be set to a value of one or more days.
  For more information on enabling automated backups and configuring a retention policy, see
  [Enabling automated backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").
- An Amazon S3 bucket must exist in the same account and Region as the source DB instance. Before enabling access to transaction log backups, choose an existing
  Amazon S3 bucket or [create a new bucket](../../../AmazonS3/latest/userguide/CreatingaBucket.md "../../../AmazonS3/latest/userguide/CreatingaBucket.md") to use for your transaction log backup files.
- An Amazon S3 bucket permissions policy must be configured as follows to allow Amazon RDS to copy transaction log files into it:
  1.  Set the object account ownership property on the bucket to **Bucket Owner Preferred**.
  2.  Add the following policy. There will be no policy by default, so use the bucket Access Control Lists (ACL)
      to edit the bucket policy and add it.

The following example uses an ARN to specify a resource. We recommend using the `SourceArn` and `SourceAccount`
global condition context keys in resource-based trust relationships to limit the service's permissions to a specific resource.
For more information on working with ARNs, see [Amazon resource
names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") and [Amazon Resource Names (ARNs) in Amazon RDS](USER_Tagging.md "USER_Tagging.md").

###### Example of an Amazon S3 permissions policy for access to transaction log backups

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Only allow writes to my bucket with bucket owner full control",
 "Effect": "Allow",
 "Principal": {
 "Service": "backups.rds.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`{customer_path}`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:sourceAccount": "{customer_account}",
 "aws:sourceArn": "{db_instance_arn}"
 }
 }
 }
 ]
}`

```

- An AWS Identity and Access Management (IAM) role to access the Amazon S3 bucket. If you already have an IAM role, you can use that.
  You can choose to have a new IAM role created for you when you add the `SQLSERVER_BACKUP_RESTORE` option by using the AWS Management Console.
  Alternatively, you can create a new one manually. For more information on creating and configuring an IAM role with `SQLSERVER_BACKUP_RESTORE`, see
  [Manually creating an IAM role for native backup and restore](SQLServer.Procedural.Importing.Native.md#SQLServer.Procedural.Importing.Native.Enabling.IAM "SQLServer.Procedural.Importing.Native.md#SQLServer.Procedural.Importing.Native.Enabling.IAM").
- The `SQLSERVER_BACKUP_RESTORE` option must be added to an option group on your DB instance. For more information on adding the
  `SQLSERVER_BACKUP_RESTORE` option, see [Support for native backup and restore in SQL Server](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").

###### Note

If your DB instance has storage encryption enabled, the AWS KMS (KMS) actions and key must be
provided in the IAM role provided in the native backup and restore option
group.

Optionally, if you intend to use the `rds_restore_log` stored procedure to perform point in time database restores,
we recommend using the same Amazon S3 path for the native backup and restore option group and access to transaction log backups. This method ensures
that when Amazon RDS assumes the role from the option group to perform the restore log functions, it has access to retrieve transaction log
backups from the same Amazon S3 path.

- If the DB instance is encrypted, regardless of encryption type (AWS managed key or
  customer managed key), you must provide a customer managed KMS key in the IAM
  role and in the `rds_tlog_backup_copy_to_S3` stored procedure.

## Limitations and recommendations

Access to transaction log backups has the following limitations and recommendations:

- You can list and copy up to the last seven days of transaction log backups for any DB instance that has backup retention configured between one to 35 days.
- The Amazon S3 bucket used for access to transaction log backups must exist in the same account and Region as the source DB instance.
  Cross-account and cross-region copy is not supported.
- Only one Amazon S3 bucket can be configured as a target to copy transaction log backups into. You can choose a new target Amazon S3 bucket with
  the `rds_tlog_copy_setup` stored procedure. For more information on choosing a new target Amazon S3 bucket, see
  [Setting up access to transaction log backups](USER.SQLServer.AddlFeat.TransactionLogAccess.md "USER.SQLServer.AddlFeat.TransactionLogAccess.md").
- You cannot specify the KMS key when using the `rds_tlog_backup_copy_to_S3` stored procedure if your RDS instance is not
  enabled for storage encryption.
- Multi-account copying is not supported. The IAM role used for copying will only permit write access to Amazon S3 buckets within the owner account of the DB instance.
- Only two concurrent tasks of any type may be run on an RDS for SQL Server DB instance.
- Only one copy task can run for a single database at a given time. If you want to copy transaction log backups for multiple databases
  on the DB instance, use a separate copy task for each database.
- If you copy a transaction log backup that already exists with the same name in the Amazon S3 bucket, the existing transaction log backup will be overwritten.
- You can only run the stored procedures that are provided with access to transaction log backups on the primary DB instance.
  You can’t run these stored procedures on an RDS for SQL Server read replica or on a secondary instance of a Multi-AZ DB cluster.
- If the RDS for SQL Server DB instance is rebooted while the `rds_tlog_backup_copy_to_S3` stored procedure is running, the task will automatically
  restart from the beginning when the DB instance is back online. Any transaction log backups that had been copied to the Amazon S3 bucket while the task
  was running before the reboot will be overwritten.
- The Microsoft SQL Server system databases and the `RDSAdmin` database cannot be configured for access to transaction log backups.
- Copying to buckets encrypted by SSE-KMS isn't supported.
