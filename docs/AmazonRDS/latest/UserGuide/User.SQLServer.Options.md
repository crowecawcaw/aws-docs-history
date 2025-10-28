# Integrating an Amazon RDS for SQL Server

DB instance with Amazon S3

You can transfer files between a DB instance running Amazon RDS for SQL Server and an Amazon S3
bucket. By doing this, you can use Amazon S3 with SQL Server features such as BULK INSERT. For
example, you can download .csv, .xml, .txt, and other files from Amazon S3 to the DB instance
host and import the data from `D:\S3\` into the database. All files are
stored in `D:\S3\` on the DB instance.

The following limitations apply:

###### Note

Traffic between the RDS host and S3 routes through VPC endpoints in RDS internal VPCs for all SQL Server features that use S3. This traffic doesn't use the RDS instance endpoint ENI. S3 bucket policies can't restrict RDS traffic by networking conditions.

- Files in the `D:\S3` folder are deleted on the standby replica after a failover
  on Multi-AZ instances. For more information, see [Multi-AZ limitations for S3 integration](#S3-MAZ "#S3-MAZ").
- The DB instance and the S3 bucket must be in the same AWS Region.
- If you run more than one S3 integration task at a time, the tasks run sequentially, not in parallel.

###### Note

S3 integration tasks share the same queue as native backup and restore tasks. At maximum, you can have only two tasks in progress at any time in this queue.
Therefore, two running native backup and restore tasks will block any S3 integration tasks.

- You must re-enable the S3 integration feature on restored instances. S3 integration isn't propagated from the source instance to
  the restored instance. Files in `D:\S3` are deleted on a restored instance.
- Downloading to the DB instance is limited to 100 files. In other words, there can't be more than 100 files in `D:\S3\`.
- Only files without file extensions or with the following file extensions are supported for download: .abf, .asdatabase, .bcp,
  .configsettings, .csv, .dat, .deploymentoptions, .deploymenttargets, .fmt, .info, .ispac, .lst, .tbl, .txt, .xml, and .xmla.
- The S3 bucket must have the same owner as the related AWS Identity and Access Management (IAM) role. Therefore, cross-account S3 integration isn't supported.
- The S3 bucket can't be open to the public.
- The file size for uploads from RDS to S3 is limited to 50 GB per file.
- The file size for downloads from S3 to RDS is limited to the maximum supported by S3.

###### Topics

- [Prerequisites for integrating RDS for SQL Server with S3](Appendix.SQLServer.Options.S3-integration.md "Appendix.SQLServer.Options.S3-integration.md")
- [Enabling RDS for SQL Server integration with S3](Appendix.SQLServer.Options.S3-integration.md "Appendix.SQLServer.Options.S3-integration.md")
- [Transferring files between RDS for SQL Server and Amazon S3](Appendix.SQLServer.Options.S3-integration.md "Appendix.SQLServer.Options.S3-integration.md")
- [Listing files on the RDS DB instance](Appendix.SQLServer.Options.S3-integration.using.md "Appendix.SQLServer.Options.S3-integration.using.md")
- [Deleting files on the RDS DB instance](Appendix.SQLServer.Options.S3-integration.using.md "Appendix.SQLServer.Options.S3-integration.using.md")
- [Monitoring the status of a file transfer
  task](Appendix.SQLServer.Options.S3-integration.using.md "Appendix.SQLServer.Options.S3-integration.using.md")
- [Canceling a task](Appendix.SQLServer.Options.S3-integration.md "Appendix.SQLServer.Options.S3-integration.md")
- [Multi-AZ limitations for S3 integration](#S3-MAZ "#S3-MAZ")
- [Disabling RDS for SQL Server integration with S3](Appendix.SQLServer.Options.S3-integration.md "Appendix.SQLServer.Options.S3-integration.md")
  For more information on working with files in Amazon S3, see [Getting started with Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md").

## Multi-AZ limitations for S3 integration

On Multi-AZ instances, files in the `D:\S3` folder are deleted on the standby
replica after a failover. A failover can be planned, for example, during DB instance
modifications such as changing the instance class or upgrading the engine version. Or a
failover can be unplanned, during an outage of the primary.

###### Note

We don't recommend using the `D:\S3` folder for file storage. The
best practice is to upload created files to Amazon S3 to make them durable, and download
files when you need to import data.

To determine the last failover time, you can use the `msdb.dbo.rds_failover_time` stored procedure. For more information,
see [Determining the last failover time for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md").

###### Example of no recent failover

This example shows the output when there is no recent failover in the error logs. No failover has happened since 2020-04-29 23:59:00.01.

Therefore, all files downloaded after that time that haven't been deleted using the
`rds_delete_from_filesystem` stored procedure are still accessible on
the current host. Files downloaded before that time might also be available.

| errorlog_available_from     | recent_failover_time        |
| --------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2020-04-29 23:59:00.0100000 | null                        | ###### Example of recent failover This example shows the output when there is a failover in the error logs. The most recent failover was at 2020-05-05 18:57:51.89. All files downloaded after that time that haven't been deleted using the `rds_delete_from_filesystem` stored procedure are still accessible on the current host. |
| errorlog_available_from     | recent_failover_time        |
| ---                         | ---                         |
| 2020-04-29 23:59:00.0100000 | 2020-05-05 18:57:51.8900000 |
