# Setting up access to transaction log backups

To set up access to transaction log backups, complete the list of requirements in the [Requirements](USER.SQLServer.AddlFeat.md#USER.SQLServer.AddlFeat.TransactionLogAccess.Requirements "USER.SQLServer.AddlFeat.md#USER.SQLServer.AddlFeat.TransactionLogAccess.Requirements") section,
and then run the `rds_tlog_copy_setup` stored procedure. The procedure will enable the access to transaction log backups feature at the DB instance level. You don't need to run it for each individual database on the DB instance.

###### Important

The database user must be granted the `db_owner` role within SQL Server on each
database to configure and use the access to transaction log backups feature.

###### Example usage:

```

exec msdb.dbo.rds_tlog_copy_setup
@target_s3_arn='arn:aws:s3:::`amzn-s3-demo-bucket`/`myfolder`';


```

The following parameter is required:

- `@target_s3_arn` – The ARN of the target Amazon S3 bucket to copy transaction log backups files to.

###### Example of setting an Amazon S3 target bucket:

```

exec msdb.dbo.rds_tlog_copy_setup @target_s3_arn='arn:aws:s3:::`amzn-s3-demo-logging-bucket`/`mytestdb1`';

```

To validate the configuration, call the `rds_show_configuration` stored procedure.

###### Example of validating the configuration:

```

exec rdsadmin.dbo.rds_show_configuration @name='target_s3_arn_for_tlog_copy';

```

To modify access to transaction log backups to point to a different Amazon S3 bucket, you can view the current Amazon S3 bucket value and
re-run the `rds_tlog_copy_setup` stored procedure using a new value for the `@target_s3_arn`.

###### Example of viewing the existing Amazon S3 bucket configured for access to transaction log backups

```

exec rdsadmin.dbo.rds_show_configuration @name='target_s3_arn_for_tlog_copy';

```

###### Example of updating to a new target Amazon S3 bucket

```

exec msdb.dbo.rds_tlog_copy_setup @target_s3_arn='arn:aws:s3:::`amzn-s3-demo-logging-bucket1`/`mynewfolder`';

```
