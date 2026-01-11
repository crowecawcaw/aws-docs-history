# Using native backup and restore

After you have enabled and configured native backup and restore, you can start using it.
First, you connect to your Microsoft SQL Server database, and then you call an Amazon RDS
stored procedure to do the work. For instructions on connecting to your database, see
[Connecting to your Microsoft SQL Server
DB instance](USER_ConnectToMicrosoftSQLServerInstance.md "USER_ConnectToMicrosoftSQLServerInstance.md").

Some of the stored procedures require that you provide an Amazon Resource Name (ARN) to your
Amazon S3 bucket and file. The format for your ARN is
`arn:aws:s3:::`bucket_name`/`file_name.extension``.
Amazon S3 doesn't require an account number or AWS Region in ARNs.

If you also provide an optional KMS key, the format for the ARN of the key is
`arn:aws:kms:`region`:`account-id`:key/`key-id``.
For more information, see [Amazon resource names (ARNs) and AWS service
namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md"). You must use a symmetric encryption KMS key to encrypt your backups. Amazon RDS doesn't support asymmetric
KMS keys. For more information, see [Creating symmetric encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the
_AWS Key Management Service Developer Guide_.

###### Note

Whether or not you use a KMS key, the native backup and restore tasks enable
server-side Advanced Encryption Standard (AES) 256-bit encryption through SSE-S3 by
default for files uploaded to S3. Passing in
`@enable_bucket_default_encryption=1` to the backup stored procedure uses
your S3 bucket's configured default encryption key.

For instructions on how to call each stored procedure, see the following topics:

- [Backing up a
  database](#SQLServer.Procedural.Importing.Native.Using.Backup "#SQLServer.Procedural.Importing.Native.Using.Backup")
- [Restoring a database](#SQLServer.Procedural.Importing.Native.Using.Restore "#SQLServer.Procedural.Importing.Native.Using.Restore")
- [Restoring a log](#SQLServer.Procedural.Importing.Native.Restore.Log "#SQLServer.Procedural.Importing.Native.Restore.Log")
- [Finishing a database restore](#SQLServer.Procedural.Importing.Native.Finish.Restore "#SQLServer.Procedural.Importing.Native.Finish.Restore")
- [Working with partially restored databases](#SQLServer.Procedural.Importing.Native.Partially.Restored "#SQLServer.Procedural.Importing.Native.Partially.Restored")
- [Canceling a task](#SQLServer.Procedural.Importing.Native.Using.Cancel "#SQLServer.Procedural.Importing.Native.Using.Cancel")
- [Tracking the status of tasks](#SQLServer.Procedural.Importing.Native.Tracking "#SQLServer.Procedural.Importing.Native.Tracking")

## Backing up a

database

To back up your database, use the `rds_backup_database` stored procedure.

###### Note

You can't back up a database during the maintenance window, or while Amazon RDS is taking a
snapshot.

### Usage

```
exec msdb.dbo.rds_backup_database
	@source_db_name='`database_name`',
	@s3_arn_to_backup_to='arn:aws:s3:::`bucket_name`/`file_name.extension`',
	[@kms_master_key_arn='arn:aws:kms:`region`:`account-id`:key/`key-id`'],
	[@overwrite_s3_backup_file=`0|1`],
	[@block_size=`512|1024|2048|4096|8192|16384|32768|65536`],
        [@max_transfer_size=`n`],
        [@buffer_count=`n`],
 [@type='`DIFFERENTIAL|FULL`'],
 [@number\_of\_files=`n`],
	[@enable_bucket_default_encryption=`0|1`];
```

The following parameters are required:

- `@source_db_name` – The name of the database to back up.
- `@s3_arn_to_backup_to` – The ARN indicating the Amazon S3 bucket or
  access point to use for the backup, plus the name of the backup file.

The file can have any extension, but `.bak` is usually used. Note
that access point ARNs must be of the format
`arn:aws:s3:`us-east-1`:`111122223333`:`access-point-name/object/key``.

The following parameters are optional:

- `@kms_master_key_arn` – The ARN for the symmetric encryption KMS key to use to
  encrypt the item.
  - You can't use the default encryption key. If you use the
    default key, the database won't be backed up.
  - If you don't specify a KMS key identifier, the backup file
    won't be encrypted. For more information, see
    [Encrypting Amazon RDS resources](Overview.md "Overview.md").
  - When you specify a KMS key, client-side encryption is used.
  - Amazon RDS doesn't support asymmetric KMS keys. For more information, see [Creating symmetric encryption
    KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_.

- `@overwrite_s3_backup_file` – A value that indicates whether to
  overwrite an existing backup file.
  - `0` – Doesn't overwrite an existing file. This value is the
    default.

  Setting `@overwrite_s3_backup_file` to 0 returns an
  error if the file already exists.
  - `1` – Overwrites an existing file that has the specified name, even
    if it isn't a backup file.

- `@type` – The type of backup.

      + `DIFFERENTIAL` – Makes a differential backup.
      + `FULL` – Makes a full backup. This value is the default.

  A differential backup is based on the last full
  backup. For differential backups to work, you can't take a snapshot
  between the last full backup and the differential backup. If you want a
  differential backup, but a snapshot exists, then do another full backup
  before proceeding with the differential backup.

You can look for the last full backup or snapshot using the following example SQL
query:

```
select top 1
database_name
, 	backup_start_date
, 	backup_finish_date
from    msdb.dbo.backupset
where   database_name='`mydatabase`'
and     type = '`D`'
order by backup_start_date desc;
```

- `@number_of_files` – The number of files into which the backup will be
  divided (chunked). The maximum number is 10.

      + Multifile backup is supported for both full and differential backups.
      + If you enter a value of 1 or omit the parameter, a single
       backup file is created.

  Provide the prefix that the files have in common, then suffix that with an asterisk
  (`*`). The asterisk can be anywhere in the
  `file_name` part of the S3 ARN. The
  asterisk is replaced by a series of alphanumeric strings in the
  generated files, starting with
  `1-of-`number_of_files``.

For example, if the file names in the S3 ARN are
`backup*.bak` and you set
`@number_of_files=4`, the backup files generated are
`backup1-of-4.bak`, `backup2-of-4.bak`,
`backup3-of-4.bak`, and
`backup4-of-4.bak`.

    + If any of the file names already exists, and `@overwrite_s3_backup_file` is 0, an error is returned.
    + Multifile backups can only have one asterisk in the
     `file_name` part of the S3
     ARN.
    + Single-file backups can have any number of asterisks in the
     `file_name` part of the S3 ARN.
     Asterisks aren't removed from the generated file
     name.

- `@block_size` – Block size (in bytes) specifying the physical block size for backup operations.
  Valid values are 512, 1024, 2048, 4096, 8192, 16384, 32768, and 65536
- `@max_transfer_size` – Maximum transfer size denotes the upper limit of data volume (in bytes)
  transmitted per I/O operation during the backup process.
  Valid values are multiples of 65536 bytes (64 KB) up to 4194304 bytes (4 MB).
- `@buffer_count` – Total number of I/O buffers to be use for the backup process.
- `@enable_bucket_default_encryption` – A value that
  indicates whether to use the S3 buckets default encryption configuration for
  server-side encryption in S3.
  - `0` – Server-side encryption uses Advanced
    Encryption Standard (AES) 256-bit encryption through SSE-S3.
  - `1` – Server-side encryption uses your S3
    bucket’s configured [default
    encryption](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md").

### Examples

###### Example of differential backup

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:::`mybucket`/`backup1.bak`',
@overwrite_s3_backup_file=`1`,
@type='`DIFFERENTIAL`';
```

###### Example of full backup with client-side encryption

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:::`mybucket`/`backup1.bak`',
@kms_master_key_arn='arn:aws:kms:`us-east-1`:`123456789012`:key/`AKIAIOSFODNN7EXAMPLE`',
@overwrite_s3_backup_file=`1`,
@type='`FULL`';
```

###### Example of multifile backup

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:::`mybucket`/`backup*.bak`',
@number_of_files=`4`;
```

###### Example of multifile differential backup

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:::`mybucket`/`backup*.bak`',
@type='`DIFFERENTIAL`',
@number_of_files=`4`;
```

###### Example of multifile backup with encryption

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:::`mybucket`/`backup*.bak`',
@kms_master_key_arn='arn:aws:kms:`us-east-1`:`123456789012`:key/`AKIAIOSFODNN7EXAMPLE`',
@number_of_files=`4`;
```

###### Example of multifile backup with S3 overwrite

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:::`mybucket`/`backup*.bak`',
@overwrite_s3_backup_file=1,
@number_of_files=`4`;
```

###### Example of backup with block size

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:::`mybucket`/`backup*.bak`',
@block_size=`512`;
```

###### Example of multifile backup with `@max_transfer_size` and `@buffer_count`

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:::`mybucket`/`backup*.bak`',
@number_of_files=`4`,
@max_transfer_size=`4194304`,
@buffer_count=`10`;
```

###### Example of single-file backup with the @number_of_files parameter

This example generates a backup file named `backup*.bak`.

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:::`mybucket`/`backup*.bak`',
@number_of_files=1;
```

###### Example of full backup with server-side encryption

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:::`mybucket`/`backup*.bak`',
@overwrite_s3_backup_file=1,
@type='FULL',
@enable_bucket_default_encryption=1;
```

###### Example of full backup using an access point

```
exec msdb.dbo.rds_backup_database
@source_db_name='`mydatabase`',
@s3_arn_to_backup_to='arn:aws:s3:`us-east-1`:`111122223333`:`accesspoint/my-access-point/object/backup1.bak`',
@overwrite_s3_backup_file=1,
@type='FULL';
```

## Restoring a database

To restore your database, call the `rds_restore_database` stored procedure.
Amazon RDS creates an initial snapshot of the database after the restore task is
complete and the database is open.

### Usage

```
exec msdb.dbo.rds_restore_database
	@restore_db_name='`database_name`',
	@s3_arn_to_restore_from='arn:aws:s3:::`bucket_name`/`file_name.extension`',
	@with_norecovery=`0|1`,
	[@keep_cdc=`0|1`],
	[@kms_master_key_arn='arn:aws:kms:`region`:`account-id`:key/`key-id`'],
        [@block_size=`512|1024|2048|4096|8192|16384|32768|65536`],
        [@max_transfer_size=`n`],
        [@buffer_count=`n`],
 [@type='`DIFFERENTIAL|FULL`'];
```

The following parameters are required:

- `@restore_db_name` – The name of the database to restore. Database names are unique. You can't restore a
  database with the same name as an existing database.
- `@s3_arn_to_restore_from` – The ARN indicating the Amazon S3 prefix and
  names of the backup files used to restore the database.
  - For a single-file backup, provide the entire file name.
  - For a multifile backup, provide the prefix that the files have in common, then suffix
    that with an asterisk (`*`).
  - If `@s3_arn_to_restore_from` is empty, the following error message
    is returned: **`S3 ARN prefix cannot be empty`**.

The following parameter is required for differential restores, but optional for full
restores:

- `@with_norecovery` – The recovery clause to use for the restore
  operation.
  - Set it to `0` to restore with RECOVERY. In this case, the database is
    online after the restore.
  - Set it to `1` to restore with NORECOVERY. In this case, the database
    remains in the RESTORING state after restore task completion.
    With this approach, you can do later differential restores.
  - For DIFFERENTIAL restores, specify `0` or `1`.
  - For `FULL` restores, this value defaults to `0`.

The following parameters are optional:

- `@keep_cdc` – Indicates whether to retain Change Data
  Capture (CDC) configuration on the restored database. Set to `1`
  to enable KEEP_CDC, `0` to disable. The default value is
  `0`.
- `@kms_master_key_arn` – If you encrypted the backup file, the KMS key
  to use to decrypt the file.

When you specify a KMS key, client-side encryption is used.

- `@type` – The type of restore. Valid types are
  `DIFFERENTIAL` and `FULL`. The default value is `FULL`.
- `@block_size` – Block size (in bytes) specifying the physical block size for backup operations.
  Valid values are 512, 1024, 2048, 4096, 8192, 16384, 32768, and 65536
- `@max_transfer_size` – Maximum transfer size denotes the upper limit of data volume (in bytes)
  transmitted per I/O operation during the backup process.
  Valid values are multiples of 65536 bytes (64 KB) up to 4194304 bytes (4 MB).
- `@buffer_count` – Total number of I/O buffers to be use for the backup process.

###### Note

For differential restores, either the database must be in the
RESTORING state or a task must already exist that restores with NORECOVERY.

You can't restore later differential backups while
the database is online.

You can't submit a restore task for a database that already has a
pending restore task with RECOVERY.

Full restores with both NORECOVERY and KEEP_CDC aren’t supported.

All native restores aren't supported on instances that have cross-region read replicas.

For supported configurations, restoring a database on a Multi-AZ instance with read replicas is similar to restoring a
database on a Multi-AZ instance. You don't have to take any additional actions to restore a database on a replica.

### Examples

###### Example of single-file restore

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak';
```

###### Example of multifile restore

To avoid errors when restoring multiple files, make sure that all the backup files have
the same prefix, and that no other files use that prefix.

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup*';
```

###### Example of full database restore with RECOVERY

The following three examples perform the same task, full restore with RECOVERY.

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak';
```

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak',
[@type='`DIFFERENTIAL|FULL`'];
```

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak',
@type='FULL',
@with_norecovery=0;
```

###### Example of full database restore with encryption

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak',
@kms_master_key_arn='arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE';
```

###### Example of restore with block size

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak',
@block_size=512;
```

###### Example of multifile restore with @max_transfer_size and @buffer_count

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup*',
@max_transfer_size=4194304,
@buffer_count=10;
```

###### Example of full database restore with NORECOVERY

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak',
@type='FULL',
@with_norecovery=1;
```

###### Example of differential restore with NORECOVERY

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak',
@type='DIFFERENTIAL',
@with_norecovery=1;
```

###### Example of differential restore with RECOVERY

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak',
@type='DIFFERENTIAL',
@with_norecovery=0;
```

###### Example of full database restore with RECOVERY using an access point

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_backup_to='arn:aws:s3:`us-east-1`:`111122223333`:`accesspoint/my-access-point/object/backup1.bak`',
@with_norecovery=0;
```

###### Example of full database restore with KEEP_CDC

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak',
@keep_cdc=1;
```

## Restoring a log

To restore your log, call the `rds_restore_log` stored procedure.

### Usage

```
exec msdb.dbo.rds_restore_log
	@restore_db_name='`database_name`',
	@s3_arn_to_restore_from='arn:aws:s3:::`bucket_name`/`log_file_name.extension`',
	[@kms_master_key_arn='arn:aws:kms:`region`:`account-id`:key/`key-id`'],
	[@with_norecovery=`0|1`],
	[@keep_cdc=`0|1`],
	[@stopat='`datetime`'],
	[@block_size=`512|1024|2048|4096|8192|16384|32768|65536`],
        [@max_transfer_size=`n`],
        [@buffer_count=`n`];
```

The following parameters are required:

- `@restore_db_name` – The name of the database whose
  log to restore.
- `@s3_arn_to_restore_from` – The ARN indicating the Amazon S3 prefix and
  name of the log file used to restore the log. The file can have any
  extension, but `.trn` is usually used.

If `@s3_arn_to_restore_from` is empty, the following error message is
returned: **`S3 ARN prefix cannot be empty`**.

The following parameters are optional:

- `@keep_cdc` – Indicates whether to retain Change Data
  Capture (CDC) configuration on the restored database. Set to 1 to enable
  KEEP_CDC, 0 to disable. The default value is 0.
- `@kms_master_key_arn` – If you encrypted the log, the KMS key to use
  to decrypt the log.
- `@with_norecovery` – The recovery clause to use for the restore
  operation. This value defaults to `1`.
  - Set it to `0` to restore with RECOVERY. In this case, the database is
    online after the restore. You can't restore further log backups while the
    database is online.
  - Set it to `1` to restore with NORECOVERY. In this case, the database
    remains in the RESTORING state after restore task completion. With this approach, you
    can do later log restores.

- `@stopat` – A value that specifies that the database is restored to
  its state at the date and time specified (in datetime format). Only
  transaction log records written before the specified date and time are
  applied to the database.

If this parameter isn't specified (it is NULL), the complete log is restored.

- `@block_size` – Block size (in bytes) specifying the physical block size for backup operations.
  Valid values are 512, 1024, 2048, 4096, 8192, 16384, 32768, and 65536
- `@max_transfer_size` – Maximum transfer size denotes the upper limit of data volume (in bytes)
  transmitted per I/O operation during the backup process.
  Valid values are multiples of 65536 bytes (64 KB) up to 4194304 bytes (4 MB).
- `@buffer_count` – Total number of I/O buffers to be use for the backup process.

###### Note

For log restores, either the database must be in a state of restoring or a task must
already exist that restores with NORECOVERY.

You can't restore log backups while the database is online.

You can't submit a log restore task on a database that already has
a pending restore task with RECOVERY.

### Examples

###### Example of log restore

```
exec msdb.dbo.rds_restore_log
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/mylog.trn';
```

###### Example of log restore with encryption

```
exec msdb.dbo.rds_restore_log
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/mylog.trn',
@kms_master_key_arn='arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE';
```

###### Example of log restore with NORECOVERY

The following two examples perform the same task, log restore with
NORECOVERY.

```
exec msdb.dbo.rds_restore_log
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/mylog.trn',
@with_norecovery=1;
```

```
exec msdb.dbo.rds_restore_log
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/mylog.trn';
```

###### Example of restore with block size

```
exec msdb.dbo.rds_restore_log
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/mylog.trn',
@block_size=512;
```

###### Example of log restore with RECOVERY

```
exec msdb.dbo.rds_restore_log
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/mylog.trn',
@with_norecovery=0;
```

###### Example of log restore with STOPAT clause

```
exec msdb.dbo.rds_restore_log
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/mylog.trn',
@with_norecovery=0,
@stopat='2019-12-01 03:57:09';
```

###### Example of log restore with KEEP_CDC

```
exec msdb.dbo.rds_restore_database
@restore_db_name='mydatabase',
@s3_arn_to_restore_from='arn:aws:s3:::mybucket/backup1.bak',
@keep_cdc=1;
```

## Finishing a database restore

If the last restore task on the database was performed using `@with_norecovery=1`,
the database is now in the RESTORING state. Open this database for normal operation by using the
`rds_finish_restore` stored procedure.

### Usage

```
exec msdb.dbo.rds_finish_restore @db_name='`database_name`';
```

###### Note

To use this approach, the database must be in the RESTORING state without any pending
restore tasks.

To finish restoring the database, use the master login. Or use the user login that most
recently restored the database or log with
NORECOVERY.

## Working with partially restored databases

### Dropping a

partially restored database

To drop a partially restored database (left in the RESTORING state), use the
`rds_drop_database` stored procedure.

```
exec msdb.dbo.rds_drop_database @db_name='`database_name`';
```

###### Note

You can't submit a DROP database request for a database that already has a pending
restore or finish restore task.

To drop the database, use the master login. Or use the user login that most recently
restored the database or log with NORECOVERY.

### Snapshot restore and

point-in-time recovery behavior for partially restored databases

Partially restored databases in the source instance (left in the RESTORING state) are
dropped from the target instance during snapshot restore and point-in-time
recovery.

## Canceling a task

To cancel a backup or restore task, call the `rds_cancel_task` stored procedure.

###### Note

You can't cancel a FINISH_RESTORE task.

### Usage

```
exec msdb.dbo.rds_cancel_task @task_id=`ID_number`;
```

The following parameter is required:

- `@task_id` – The ID of the task to cancel. You can get the task ID by
  calling `rds_task_status`.

## Tracking the status of tasks

To track the status of your backup and restore tasks, call the `rds_task_status`
stored procedure. If you don't provide any parameters, the stored procedure returns
the status of all tasks. The status for tasks is updated approximately every two
minutes. Task history is retained for 36 days.

### Usage

```
exec msdb.dbo.rds_task_status
	[@db_name='`database_name`'],
	[@task_id=`ID_number`];
```

The following parameters are optional:

- `@db_name` – The name of the database to show the task status for.
- `@task_id` – The ID of the task to show the task status for.

### Examples

###### Example of listing the status for a specific task

```
exec msdb.dbo.rds_task_status @task_id=5;
```

###### Example of listing the status for a specific database and task

```
exec msdb.dbo.rds_task_status
@db_name='my_database',
@task_id=5;
```

###### Example of listing all tasks and their statuses on a specific database

```
exec msdb.dbo.rds_task_status @db_name='my_database';
```

###### Example of listing all tasks and their statuses on the current instance

```
exec msdb.dbo.rds_task_status;
```

### Response

The `rds_task_status` stored procedure returns the following columns.

| Column                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `task_id`                  | The ID of the task.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `task_type`                | Task type depending on the input parameters, as follows:<br>• For backup tasks:<br>+ BACKUP_DB – Full database backup<br>+ BACKUP_DB_DIFFERENTIAL – Differential database backup<br>• For restore tasks:<br>+ RESTORE_DB – Full database restore with RECOVERY<br>+ RESTORE_DB_NORECOVERY – Full database restore with NORECOVERY<br>+ RESTORE_DB_DIFFERENTIAL – Differential database restore with<br>RECOVERY<br>+ RESTORE_DB_DIFFERENTIAL_NORECOVERY – Differential database restore with<br>NORECOVERY<br>+ RESTORE_DB_LOG – Log restore with RECOVERY<br>+ RESTORE_DB_LOG_NORECOVERY – Log restore with NORECOVERY<br>• For tasks that finish a restore:<br>+ FINISH_RESTORE – Finish restore and<br>open database<br>Amazon RDS creates an initial snapshot of the database after it is open on completion of<br>the following restore tasks:<br>• RESTORE_DB<br>• RESTORE_DB_DIFFERENTIAL<br>• RESTORE_DB_LOG<br>• FINISH_RESTORE |
| `database_name`            | The name of the database that the task is associated with.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `% complete`               | The progress of the task as a percent value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `duration (mins)`          | The amount of time spent on the task, in minutes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `lifecycle`                | The status of the task. The possible statuses are the following:<br>• `CREATED` – As soon as you call<br>`rds_backup_database` or<br>`rds_restore_database`, a task is created and the<br>status is set to `CREATED`.<br>• `IN_PROGRESS` – After a backup or<br>restore task starts, the status is set to<br>`IN_PROGRESS`. It can take up to 5 minutes for<br>the status to change from `CREATED` to<br>`IN_PROGRESS`.<br>• `SUCCESS` – After a backup or restore<br>task completes, the status is set to `SUCCESS`.<br>• `ERROR` – If a backup or restore task fails, the status is set to<br>`ERROR`. For more information about the<br>error, see the `task_info` column.<br>• `CANCEL_REQUESTED` – As soon as you call<br>`rds_cancel_task`, the status of the task is set<br>to `CANCEL_REQUESTED`.<br>• `CANCELLED` – After a task is<br>successfully canceled, the status of the task is set to<br>`CANCELLED`.                  |
| `task_info`                | Additional information about the task. If an<br>error occurs while backing up or restoring a database, this column<br>contains information about the error. For a list of possible errors,<br>and mitigation strategies, see [Troubleshooting](SQLServer.Procedural.Importing.Native.md "SQLServer.Procedural.Importing.Native.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `last_updated`             | The date and time that the task status was last updated. The status is updated after every 5<br>percent of progress.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `created_at`               | The date and time that the task was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `S3_object_arn`            | The ARN indicating the Amazon S3 prefix and the name of the file that is being backed up<br>or restored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `overwrite_s3_backup_file` | The value of the `@overwrite_s3_backup_file` parameter specified when calling a<br>backup task. For more information, see<br>[Backing up a<br>database](#SQLServer.Procedural.Importing.Native.Using.Backup "#SQLServer.Procedural.Importing.Native.Using.Backup").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `KMS_master_key_arn`       | The ARN for the KMS key used for encryption (for backup) and decryption (for<br>restore).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `filepath`                 | Not applicable to native backup and restore tasks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `overwrite_file`           | Not applicable to native backup and restore tasks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
