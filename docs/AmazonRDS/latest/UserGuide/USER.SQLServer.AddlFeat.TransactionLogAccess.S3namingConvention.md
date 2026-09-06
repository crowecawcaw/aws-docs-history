

# Amazon S3 bucket folder and file structure
<a name="USER.SQLServer.AddlFeat.TransactionLogAccess.S3namingConvention"></a>

Transaction log backups have the following standard structure and naming convention within an Amazon S3 bucket:
+ A new folder is created under the `target_s3_arn` path for each database with the naming structure as `{db_id}.{family_guid}`.
+ Within the folder, transaction log backups have a filename structure as `{db_id}.{family_guid}.{rds_backup_seq_id}.{backup_file_epoch}`.
+ You can view the details of `family_guid,db_id,rds_backup_seq_id and backup_file_epoch` with the `rds_fn_list_tlog_backup_metadata`function.

The following example shows the folder and file structure of a set of transaction log backups within an Amazon S3 bucket.

![Amazon S3 bucket structure with access to transaction logs.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/sql_accesstransactionlogs_s3.png)
