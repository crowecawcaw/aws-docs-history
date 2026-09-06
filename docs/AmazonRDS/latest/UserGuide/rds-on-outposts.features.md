

# Amazon RDS on AWS Outposts support for Amazon RDS features
<a name="rds-on-outposts.features"></a>

The following table describes the Amazon RDS features supported by Amazon RDS on AWS Outposts.


| Feature | Supported | Notes | More information | 
| --- | --- | --- | --- | 
| DB instance provisioning | Yes | You can only create DB instances for RDS for SQL Server, RDS for MySQL, RDS for PostgreSQL, or RDS for Oracle DB engines. The following versions are supported:+  Microsoft SQL Server:   16.00.4085.2.v1 and higher 2022 versions   15.00.4043.16.v1 and higher 2019 versions   14.00.3294.2.v1 and higher 2017 versions   13.00.5820.21.v1 and higher 2016 versions   <br />+  MySQL 8.0 and 8.4 versions <br />+  All PostgreSQL 16 & 15 & 14 & 13 versions, and PostgreSQL version 12.5 and higher PostgreSQL 12 versions  <br />+  All Oracle versions  |  [Creating DB instances for Amazon RDS on AWS Outposts](rds-on-outposts.creating.md)  | 
| Connect to a Microsoft SQL Server DB instance with Microsoft SQL Server Management Studio | Yes | Some TLS versions and encryption ciphers might not be secure. To turn them off, follow the instructions in [Configuring SQL Server security protocols and ciphers](SQLServer.Ciphers.md). |  [Connecting to your Microsoft SQL Server DB instance](USER_ConnectToMicrosoftSQLServerInstance.md)  | 
| Modifying the master user password | Yes | None |  [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md)  | 
| Renaming a DB instance | Yes | None |  [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md)  | 
| Rebooting a DB instance | Yes | None |  [Rebooting a DB instance](USER_RebootInstance.md)  | 
| Stopping a DB instance | Yes | None |  [Stopping an Amazon RDS DB instance temporarily](USER_StopInstance.md)  | 
| Starting a DB instance | Yes | None |  [Starting an Amazon RDS DB instance that was previously stopped](USER_StartInstance.md)  | 
| Multi-AZ deployments | Yes | Multi-AZ deployments are supported on MySQL, PostgreSQL, and Oracle DB instances.<br />Multi-AZ deployments do not support Direct VPC Routing (DVR). | [Creating DB instances for Amazon RDS on AWS Outposts](rds-on-outposts.creating.md) <br />[Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.MultiAZ.md) | 
| DB parameter groups | Yes | None |  [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md)  | 
| Read replicas | Yes | Read replicas are supported for MySQL, PostgreSQL, and Oracle DB instances.<br />Read replicas do not support Direct VPC Routing (DVR). | [Creating read replicas for Amazon RDS on AWS Outposts](rds-on-outposts.rr.md) | 
| Encryption at rest | Yes | RDS on Outposts doesn't support unencrypted DB instances. |  [Encrypting Amazon RDS resources](Overview.Encryption.md)  | 
| AWS Identity and Access Management (IAM) database authentication | No | None |  [IAM database authentication for MariaDB, MySQL, and PostgreSQL](UsingWithRDS.IAMDBAuth.md)  | 
| Associating an IAM role with a DB instance | No | None | [add-role-to-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/add-role-to-db-instance.html) AWS CLI command <br />[AddRoleToDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddRoleToDBInstance.html) RDS API operation | 
| Kerberos authentication | Yes | None |  [Kerberos authentication](database-authentication.md#kerberos-authentication)  | 
| Tagging Amazon RDS resources | Yes | None |  [Tagging Amazon RDS resources](USER_Tagging.md)  | 
| Option groups | Yes | The following RDS for Oracle options are not supported:+  [Amazon EFS integration](oracle-efs-integration.md) <br />+  [Amazon S3 integration](oracle-s3-integration.md)  |  [Working with option groups](USER_WorkingWithOptionGroups.md)  | 
| Modifying the maintenance window | Yes | None |  [Maintaining a DB instance](USER_UpgradeDBInstance.Maintenance.md)  | 
| Automatic minor version upgrade | Yes | None |  [Automatically upgrading the minor engine version](USER_UpgradeDBInstance.Upgrading.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades)  | 
| Modifying the backup window | Yes | None | [Introduction to backups](USER_WorkingWithAutomatedBackups.md)<br />[Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md) | 
| Changing the DB instance class | Yes | None |  [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md)  | 
| Changing the allocated storage | Yes | None |  [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md)  | 
| Storage autoscaling | Yes | None |  [Managing capacity automatically with Amazon RDS storage autoscaling](USER_PIOPS.Autoscaling.md)  | 
| Manual and automatic DB instance snapshots | Yes | You can store automated backups and manual snapshots in your AWS Region, or locally on your Outpost.<br />Local backups require that your Outpost supports and has configured both Amazon S3 on Outposts and Amazon EBS local snapshots. Both are required. If either one is unavailable on your Outpost, you can store backups only in your AWS Region.<br />Amazon EBS local snapshots are not available on every Outpost configuration. Before you choose local backups, confirm that your Outpost supports both Amazon S3 on Outposts and Amazon EBS local snapshots.<br />Local backups are supported on MySQL, PostgreSQL, and Oracle DB instances. Local backups are not supported for Multi-AZ instance deployments. | [Creating DB instances for Amazon RDS on AWS Outposts](rds-on-outposts.creating.md)<br />[Amazon S3 on Outposts](https://aws.amazon.com/s3/outposts/)<br />[Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md) | 
| Restoring from a DB snapshot | Yes | You can store automated backups and manual snapshots for the restored DB instance in the parent AWS Region or locally on your Outpost. | [Considerations for restoring DB instances on Amazon RDS on AWS Outposts](rds-on-outposts.restoring.md)<br />[Restoring to a DB instance](USER_RestoreFromSnapshot.md) | 
| Restoring a DB instance from Amazon S3 | No | None | [Restoring a backup into an Amazon RDS for MySQL DB instance](MySQL.Procedural.Importing.md) | 
| Exporting snapshot data to Amazon S3 | No | None |  [Exporting DB snapshot data to Amazon S3 for Amazon RDS](USER_ExportSnapshot.md)  | 
| Point-in-time recovery | Yes | You can store automated backups and manual snapshots for the restored DB instance in the parent AWS Region or locally on your Outpost, with one exception. | [Considerations for restoring DB instances on Amazon RDS on AWS Outposts](rds-on-outposts.restoring.md)<br />[Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md) | 
| Enhanced monitoring | Yes | None |  [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.OS.md)  | 
| Amazon CloudWatch monitoring | Yes | You can view the same set of metrics that are available for your databases in the AWS Region. |  [Monitoring Amazon RDS metrics with Amazon CloudWatch](monitoring-cloudwatch.md)  | 
| Publishing database engine logs to CloudWatch Logs | Yes | None |  [Publishing database logs to Amazon CloudWatch Logs](USER_LogAccess.Procedural.UploadtoCloudWatch.md)  | 
| Event notification | Yes | None |  [Working with Amazon RDS event notification](USER_Events.md)  | 
| Amazon RDS Performance Insights | No | None |  [Monitoring DB load with Amazon CloudWatch Database Insights on Amazon RDS](USER_PerfInsights.md)  | 
| Viewing or downloading database logs | No | RDS on Outposts doesn't support viewing database logs using the console or describing database logs using the AWS CLI or RDS API.<br />RDS on Outposts doesn't support downloading database logs using the console or downloading database logs using the AWS CLI or RDS API. |  [Monitoring Amazon RDS log files](USER_LogAccess.md)  | 
| Amazon RDS Proxy | No | None |  [Amazon RDS Proxy](rds-proxy.md)  | 
| Stored procedures for Amazon RDS for MySQL | Yes | None |  [RDS for MySQL stored procedure reference](Appendix.MySQL.SQLRef.md)  | 
| Replication with external databases for RDS for MySQL | No | None |  [Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.Repl.md)  | 
| Native backup and restore for Amazon RDS for Microsoft SQL Server | Yes | None |  [Importing and exporting SQL Server databases using native backup and restore](SQLServer.Procedural.Importing.md)  | 