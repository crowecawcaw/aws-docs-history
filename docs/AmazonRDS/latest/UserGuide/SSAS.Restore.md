

# Restoring an SSAS database
<a name="SSAS.Restore"></a>

Use the following stored procedure to restore an SSAS database from a backup. 

You can't restore a database if there is an existing SSAS database with the same name. The stored procedure for restoring doesn't support encrypted backup files.

```
exec msdb.dbo.rds_msbi_task
@task_type='SSAS_RESTORE_DB',
@database_name='{{mynewssasdb}}',
@file_path='D:\S3\{{ssas_db_backup}}.abf';
```

The following parameters are required:
+ `@task_type` – The type of the MSBI task, in this case `SSAS_RESTORE_DB`.
+ `@database_name` – The name of the new SSAS database that you're restoring to.
+ `@file_path` – The path to the SSAS backup file.

## Restoring a DB instance to a specified time
<a name="SSAS.PITR"></a>

Point-in-time recovery (PITR) doesn't apply to SSAS databases. If you do PITR, only the SSAS data in the last snapshot before the requested time is available on the restored instance.

**To have up-to-date SSAS databases on a restored DB instance**

1. Back up your SSAS databases to the `D:\S3` folder on the source instance.

1. Transfer the backup files to the S3 bucket.

1. Transfer the backup files from the S3 bucket to the `D:\S3` folder on the restored instance.

1. Run the stored procedure to restore the SSAS databases onto the restored instance.

   You can also reprocess the SSAS project to restore the databases.