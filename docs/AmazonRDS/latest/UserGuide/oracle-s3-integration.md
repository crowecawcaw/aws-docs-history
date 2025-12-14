# Transferring files between Amazon RDS for Oracle and an

Amazon S3 bucket

To transfer files between an RDS for Oracle DB instance and an Amazon S3 bucket, you can use the
Amazon RDS package `rdsadmin_s3_tasks`. You can compress files with GZIP when
uploading them, and decompress them when downloading.

###### Topics

- [Requirements and limitations for file
  transfers](#oracle-s3-integration.using.reqs "#oracle-s3-integration.using.reqs")
- [Uploading files from your RDS for Oracle DB instance to an Amazon S3 bucket](#oracle-s3-integration.using.upload "#oracle-s3-integration.using.upload")
- [Downloading files from an Amazon S3 bucket to an Oracle DB instance](#oracle-s3-integration.using.download "#oracle-s3-integration.using.download")
- [Monitoring the status of a file transfer](#oracle-s3-integration.using.task-status "#oracle-s3-integration.using.task-status")

## Requirements and limitations for file

transfers

Before transferring files between your DB instance and an Amazon S3 bucket, note the
following:

- The `rdsadmin_s3_tasks` package transfers files located in a single
  directory. You can't include subdirectories in a transfer.
- The maximum object size in an Amazon S3 bucket is 5 TB.
- Tasks created by `rdsadmin_s3_tasks` run asynchronously.
- You can upload files from the Data Pump directory, such as
  `DATA_PUMP_DIR`, or any user-created directory. You can't upload
  files from a directory used by Oracle background processes, such as the
  `adump`, `bdump`, or `trace`
  directories.
- The download limit is 2000 files per procedure call for
  `download_from_s3`. If you need to download more than 2000 files
  from Amazon S3, split your download into separate actions, with no more than 2000
  files per procedure call.
- If a file exists in your download folder, and you attempt to download a file
  with the same name, `download_from_s3` skips the download. To remove
  a file from the download directory, use the PL/SQL procedure [UTL_FILE.FREMOVE](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_FILE.html#GUID-09B09C2A-2C21-4F70-BF04-D0EEA7B59CAF "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_FILE.html#GUID-09B09C2A-2C21-4F70-BF04-D0EEA7B59CAF").

## Uploading files from your RDS for Oracle DB instance to an Amazon S3 bucket

To upload files from your DB instance to an Amazon S3 bucket, use the procedure
`rdsadmin.rdsadmin_s3_tasks.upload_to_s3`. For example, you can upload
Oracle Recovery Manager (RMAN) backup files or Oracle Data Pump files. For more
information about working with objects, see [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/dev/UsingObjects.md "../../../AmazonS3/latest/dev/UsingObjects.md"). For more
information about performing RMAN backups, see [Performing common RMAN tasks for
Oracle DB instances](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").

The `rdsadmin.rdsadmin_s3_tasks.upload_to_s3` procedure has the following parameters.

| Parameter name                | Data type | Default | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | --------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `p_bucket_name`               | VARCHAR2  | –       | required | The name of the Amazon S3 bucket to upload files to.                                                                                                                                                                                                                                                                                                                                                                                         |
| `p_directory_name`            | VARCHAR2  | –       | required | The name of the Oracle directory object to upload files from. The<br>directory can be any user-created directory object or the Data Pump<br>directory, such as `DATA_PUMP_DIR`. You can't upload<br>files from a directory used by background processes, such as<br>`adump`, `bdump`, and<br>`trace`.<br>NoteYou can only upload files from the specified directory. You can't upload files in subdirectories in the<br>specified directory. |
| `p_s3_prefix`                 | VARCHAR2  | –       | required | An Amazon S3 file name prefix that files are uploaded to. An empty prefix uploads all files to the top level in the<br>specified Amazon S3 bucket and doesn't add a prefix to the file names.<br>For example, if the prefix is `folder_1/oradb`, files are uploaded to `folder_1`. In this<br>case, the `oradb` prefix is added to each file.                                                                                                |
| `p_prefix`                    | VARCHAR2  | –       | required | A file name prefix that file names must match to be uploaded. An empty prefix uploads all files in the specified<br>directory.                                                                                                                                                                                                                                                                                                               |
| `p_compression_level`         | NUMBER    | `0`     | optional | The level of GZIP compression. Valid values range from `0` to `9`:<br>• `0` – No compression<br>• `1` – Fastest compression<br>• `9` – Highest compression                                                                                                                                                                                                                                                                                   |
| `p_bucket_owner_full_control` | VARCHAR2  | –       | optional | The access control setting for the bucket. The only valid values are null or `FULL_CONTROL`. This setting<br>is required only if you upload files from one account (account A) into a bucket owned by a different account (account<br>B), and account B needs full control of the files.                                                                                                                                                     |

The return value for the `rdsadmin.rdsadmin_s3_tasks.upload_to_s3` procedure is a task ID.

The following example uploads all of the files in the `DATA_PUMP_DIR` directory to the Amazon S3 bucket
named `amzn-s3-demo-bucket`. The files aren't compressed.

```
SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(
      p_bucket_name    =>  '`amzn-s3-demo-bucket`',
      p_prefix         =>  '',
      p_s3_prefix      =>  '',
      p_directory_name =>  '`DATA_PUMP_DIR`')
   AS TASK_ID FROM DUAL;
```

The following example uploads all of the files with the prefix `db` in the
`DATA_PUMP_DIR` directory to the Amazon S3 bucket named
`amzn-s3-demo-bucket`. Amazon RDS applies the highest level of GZIP compression to the files.

```
SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(
      p_bucket_name       =>  '`amzn-s3-demo-bucket`',
      p_prefix            =>  '`db`',
      p_s3_prefix         =>  '',
      p_directory_name    =>  '`DATA_PUMP_DIR`',
      p_compression_level =>  `9`)
   AS TASK_ID FROM DUAL;
```

The following example uploads all of the files in the `DATA_PUMP_DIR` directory to the Amazon S3 bucket
named `amzn-s3-demo-bucket`. The files are uploaded to a `dbfiles` folder. In this example, the
GZIP compression level is `1`, which is the fastest level of compression.

```
SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(
      p_bucket_name       =>  '`amzn-s3-demo-bucket`',
      p_prefix            =>  '',
      p_s3_prefix         =>  '`dbfiles/`',
      p_directory_name    =>  '`DATA_PUMP_DIR`',
      p_compression_level =>  `1`)
   AS TASK_ID FROM DUAL;
```

The following example uploads all of the files in the `DATA_PUMP_DIR` directory to the Amazon S3 bucket
named `amzn-s3-demo-bucket`. The files are uploaded to a `dbfiles` folder and `ora` is
added to the beginning of each file name. No compression is applied.

```
SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(
      p_bucket_name    =>  '`amzn-s3-demo-bucket`',
      p_prefix         =>  '',
      p_s3_prefix      =>  '`dbfiles/ora`',
      p_directory_name =>  '`DATA_PUMP_DIR`')
   AS TASK_ID FROM DUAL;
```

The following example assumes that the command is run in account A, but account B requires full control of the bucket contents. The
command `rdsadmin_s3_tasks.upload_to_s3` transfers all files in the `DATA_PUMP_DIR`
directory to the bucket named `s3bucketOwnedByAccountB`. Access control is set to
`FULL_CONTROL` so that account B can access the files in the bucket. The GZIP compression level is
`6`, which balances speed and file size.

```
SELECT rdsadmin.rdsadmin_s3_tasks.upload_to_s3(
      p_bucket_name               =>  '`s3bucketOwnedByAccountB`',
      p_prefix                    =>  '',
      p_s3_prefix                 =>  '',
      p_directory_name            =>  '`DATA_PUMP_DIR`',
      p_bucket_owner_full_control =>  'FULL_CONTROL',
      p_compression_level         =>  `6`)
   AS TASK_ID FROM DUAL;
```

In each example, the `SELECT` statement returns the ID of the task in a `VARCHAR2` data type.

You can view the result by displaying the task's output file.

```
SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','dbtask-`task-id`.log'));
```

Replace `task-id` with the task ID returned by the procedure.

###### Note

Tasks are executed asynchronously.

## Downloading files from an Amazon S3 bucket to an Oracle DB instance

To download files from an Amazon S3 bucket to an RDS for Oracle instance, use the Amazon RDS procedure
`rdsadmin.rdsadmin_s3_tasks.download_from_s3`.

The `download_from_s3` procedure has the following parameters.

| Parameter name              | Data type | Default | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------- | --------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `p_bucket_name`             | VARCHAR2  | –       | Required | The name of the Amazon S3 bucket to download files from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `p_directory_name`          | VARCHAR2  | –       | Required | The name of the Oracle directory object to download files to. The<br>directory can be any user-created directory object or the Data Pump<br>directory, such as `DATA_PUMP_DIR`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `p_error_on_zero_downloads` | VARCHAR2  | FALSE   | Optional | A flag that determines whether the task raises an error when no<br>objects in the Amazon S3 bucket match the prefix. If this parameter is<br>not set or set to FALSE (default), the task prints a message that no<br>objects were found, but doesn't raise an exception or fail. If this<br>parameter is TRUE, the task raises an exception and fails.<br>Examples of prefix specifications that can fail match tests are<br>spaces in prefixes, as in `' import/test9.log'`, and case<br>mismatches, as in `test9.log` and<br>`test9.LOG`.                                                                                                                                                                                                                                                                                                                                |
| `p_s3_prefix`               | VARCHAR2  | –       | Required | A file name prefix that file names must match to be downloaded. An<br>empty prefix downloads all of the top level files in the specified<br>Amazon S3 bucket, but not the files in folders in the bucket.<br>The procedure downloads Amazon S3 objects only from the first level<br>folder that matches the prefix. Nested directory structures matching<br>the specified prefix are not downloaded.<br>For example, suppose that an Amazon S3 bucket has the folder structure<br>`folder_1/folder_2/folder_3`. You specify the<br>`'folder_1/folder_2/'` prefix. In this case, only the<br>files in `folder_2` are downloaded, not the files in<br>`folder_1` or `folder_3`.<br>If, instead, you specify the `'folder_1/folder_2'`<br>prefix, all files in `folder_1` that match the<br>`'folder_2'` prefix are downloaded, and no files in<br>`folder_2` are downloaded. |
| `p_decompression_format`    | VARCHAR2  | –       | Optional | The decompression format. Valid values are `NONE` for<br>no decompression and `GZIP` for decompression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

The return value for the `rdsadmin.rdsadmin_s3_tasks.download_from_s3` procedure is a task ID.

The following example downloads all files in the Amazon S3 bucket named `amzn-s3-demo-bucket` to the
`DATA_PUMP_DIR` directory. The files aren't compressed, so no decompression is
applied.

```
SELECT rdsadmin.rdsadmin_s3_tasks.download_from_s3(
      p_bucket_name    =>  '`amzn-s3-demo-bucket`',
      p_directory_name =>  '`DATA_PUMP_DIR`')
   AS TASK_ID FROM DUAL;
```

The following example downloads all of the files with the prefix
`db` in the Amazon S3 bucket named
`amzn-s3-demo-bucket` to the
`DATA_PUMP_DIR` directory. The files are
compressed with GZIP, so decompression is applied. The parameter
`p_error_on_zero_downloads` turns on prefix error checking, so if the
prefix doesn't match any files in the bucket, the task raises and exception and
fails.

```
SELECT rdsadmin.rdsadmin_s3_tasks.download_from_s3(
      p_bucket_name               =>  '`amzn-s3-demo-bucket`',
      p_s3_prefix                 =>  '`db`',
      p_directory_name            =>  '`DATA_PUMP_DIR`',
      p_decompression_format      =>  '`GZIP`',
      p_error_on_zero_downloads   =>  '`TRUE`')
   AS TASK_ID FROM DUAL;
```

The following example downloads all of the files in the folder `myfolder/` in the Amazon S3 bucket
named `amzn-s3-demo-bucket` to the `DATA_PUMP_DIR` directory. Use the
`p_s3_prefix` parameter to specify the Amazon S3 folder. The uploaded files are compressed with GZIP, but aren't decompressed
during the download.

```
SELECT rdsadmin.rdsadmin_s3_tasks.download_from_s3(
      p_bucket_name          =>  '`amzn-s3-demo-bucket`',
      p_s3_prefix            =>  '`myfolder/`',
      p_directory_name       =>  '`DATA_PUMP_DIR`',
      p_decompression_format =>  '`NONE`')
   AS TASK_ID FROM DUAL;
```

The following example downloads the file `mydumpfile.dmp` in the Amazon S3 bucket named
`amzn-s3-demo-bucket` to the `DATA_PUMP_DIR` directory. No
decompression is applied.

```
SELECT rdsadmin.rdsadmin_s3_tasks.download_from_s3(
      p_bucket_name    =>  '`amzn-s3-demo-bucket`',
      p_s3_prefix      =>  '`mydumpfile.dmp`',
      p_directory_name =>  '`DATA_PUMP_DIR`')
   AS TASK_ID FROM DUAL;
```

In each example, the `SELECT` statement returns the ID of the task in a `VARCHAR2` data type.

You can view the result by displaying the task's output file.

```
SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','dbtask-`task-id`.log'));
```

Replace `task-id` with the task ID returned by the procedure.

###### Note

Tasks are executed asynchronously.

You can use the `UTL_FILE.FREMOVE` Oracle procedure to remove files from a directory. For more information, see [FREMOVE procedure](https://docs.oracle.com/database/121/ARPLS/u_file.htm#ARPLS70924 "https://docs.oracle.com/database/121/ARPLS/u_file.htm#ARPLS70924") in the Oracle
documentation.

## Monitoring the status of a file transfer

File transfer tasks publish Amazon RDS events when they start and when they complete. The
event message contains the task ID for the file transfer. For information about viewing
events, see [Viewing Amazon RDS events](USER_ListEvents.md "USER_ListEvents.md").

You can view the status of an ongoing task in a bdump file. The bdump files are located in the `/rdsdbdata/log/trace`
directory. Each bdump file name is in the following format.

```
dbtask-`task-id`.log
```

Replace `task-id` with the ID of the task that you want to monitor.

###### Note

Tasks are executed asynchronously.

You can use the `rdsadmin.rds_file_util.read_text_file` stored procedure to
view the contents of bdump files. For example, the following query returns the contents
of the `dbtask-1234567890123-1234.log` bdump
file.

```
SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','`dbtask-1234567890123-1234.log`'));
```

The following sample shows the log file for a failed transfer.

```
TASK_ID
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1234567890123-1234


TEXT
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2023-04-17 18:21:33.993 UTC [INFO ] File #1: Uploading the file /rdsdbdata/datapump/A123B4CDEF567890G1234567890H1234/sample.dmp to Amazon S3 with bucket name `amzn-s3-demo-bucket` and key sample.dmp.
2023-04-17 18:21:34.188 UTC [ERROR] RDS doesn't have permission to write to Amazon S3 bucket name `amzn-s3-demo-bucket` and key sample.dmp.
2023-04-17 18:21:34.189 UTC [INFO ] The task failed.
```
