# Deploying an SSIS project

On RDS, you can't deploy SSIS projects directly by using SQL Server Management Studio
(SSMS) or SSIS procedures. To download project files from Amazon S3 and then deploy them, use
RDS stored procedures.

To run the stored procedures, log in as any user that you granted permissions for running
the stored procedures. For more information, see [Setting up a Windows-authenticated user for SSIS](SSIS.md#SSIS.Use.Auth "SSIS.md#SSIS.Use.Auth").

###### To deploy the SSIS project

1. Download the project (.ispac) file.

```
exec msdb.dbo.rds_download_from_s3
@s3_arn_of_file='arn:aws:s3:::`bucket_name`/`ssisproject`.ispac',
@rds_file_path='D:\S3\`ssisproject`.ispac',
@overwrite_file=1;
```

2. Submit the deployment task, making sure of the following:
   - The folder is present in the SSIS catalog.
   - The project name matches the project name that you used while developing the SSIS
     project.

```
exec msdb.dbo.rds_msbi_task
@task_type='SSIS_DEPLOY_PROJECT',
@folder_name='`DEMO`',
@project_name='`ssisproject`',
@file_path='D:\S3\`ssisproject`.ispac';
```
