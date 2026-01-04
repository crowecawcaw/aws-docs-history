# Deploying SSAS projects on Amazon RDS

On RDS, you can't deploy SSAS projects directly by using SQL Server Management Studio
(SSMS). To deploy projects, use an RDS stored procedure.

###### Note

Using .xmla files for deployment isn't supported.

Before you deploy projects, make sure of the following:

- Amazon S3 integration is turned on. For more information, see [Integrating an Amazon RDS for SQL Server
  DB instance with Amazon S3](User.SQLServer.Options.md "User.SQLServer.Options.md").
- The `Processing Option` configuration setting is set to `Do Not
Process`. This setting means that no processing happens after
  deployment.
- You have both the ``myssasproject`.asdatabase` and
``myssasproject`.deploymentoptions`
  files. They're automatically generated when you build the SSAS
  project.

###### To deploy an SSAS project on RDS

1. Download the `.asdatabase` (SSAS model) file from your S3 bucket to your DB
   instance, as shown in the following example. For more information on the
   download parameters, see [Downloading files
   from an Amazon S3 bucket to a SQL Server DB instance](Appendix.SQLServer.Options.S3-integration.md#Appendix.SQLServer.Options.S3-integration.using.download "Appendix.SQLServer.Options.S3-integration.md#Appendix.SQLServer.Options.S3-integration.using.download").

```
exec msdb.dbo.rds_download_from_s3
@s3_arn_of_file='arn:aws:s3:::`bucket_name`/`myssasproject`.asdatabase',
[@rds_file_path='D:\S3\`myssasproject`.asdatabase'],
[@overwrite_file=1];
```

2. Download the `.deploymentoptions` file from your S3 bucket to your DB
   instance.

```
exec msdb.dbo.rds_download_from_s3
@s3_arn_of_file='arn:aws:s3:::`bucket_name`/`myssasproject`.deploymentoptions',
[@rds_file_path='D:\S3\`myssasproject`.deploymentoptions'],
[@overwrite_file=1];
```

3. Deploy the project.

```
exec msdb.dbo.rds_msbi_task
@task_type='SSAS_DEPLOY_PROJECT',
@file_path='D:\S3\`myssasproject`.asdatabase';
```
