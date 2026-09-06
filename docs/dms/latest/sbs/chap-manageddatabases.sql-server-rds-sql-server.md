

# Migrating SQL Server Databases to Amazon RDS for SQL Server
<a name="chap-manageddatabases.sql-server-rds-sql-server"></a>

This walkthrough gets you started with homogeneous database migration from Microsoft SQL Server to Amazon Relational Database Service (Amazon RDS) for SQL Server. This guide provides a quick overview of the data migration process and provides suggestions on how to select the best option to use.

Customers looking to migrate self-managed SQL Server databases to Amazon RDS for SQL Server, can use one of the three main approaches.
+ Use a native database migration method such as backup and restore.
+ Use a managed service such as AWS DMS.
+ Use a native tool for full load and a managed AWS DMS service for ongoing replication. We call this strategy the *hybrid approach*.

The following diagram shows the hybrid approach. Here, we use one of the three native tools for full load, and AWS DMS for ongoing replication.

![Hybrid approach for SQL Server to Amazon RDS for SQL Server migration](http://docs.aws.amazon.com/dms/latest/sbs/images/sql-server-rds-sql-server-hybrid-migration.png)


The hybrid approach provides the simplicity of the native tools with additional built-in capabilities of AWS DMS. These include:
+ Data validation
+ Customizable source object selection rules
+ Data filtering
+ Renaming target tables or columns
+ Data transformations
+ Data partitioning

This document describes in detail the three full load migration methods. This guide helps you evaluate each method for your migration requirements. In the end, you can find a brief description of how to use AWS DMS for ongoing replication.

**Topics**
+ [Summary](#_summary)
+ [Full load SQL Server database migration](chap-manageddatabases.sql-server-rds-sql-server-full-load.md)
+ [Full load SQL Server database migration options performance comparison](chap-manageddatabases.sql-server-rds-sql-server-performance.md)
+ [Migrate SQL Server database with AWS DMS ongoing replication](chap-manageddatabases.sql-server-rds-sql-server-replication.md)

## Summary
<a name="_summary"></a>

The following table helps understand how each migration approach fits to different use cases.


| SQL Server native tools | Data transformation | Table filtering | Metadata rename | Migration of secondary objects | Data validation | 
| --- | --- | --- | --- | --- | --- | 
| Backup and restore | No | No | No | Yes | No | 
| Import and export wizard | Yes | Yes | Yes | No | Yes | 
| SQL Server - Generate and Publish Scripts Wizard and bulk copy program utility (bcp) | No | Yes | No | No | No | 

You can see that the SQL Server backup and restore has the best performance among the three full load options. This is the preferred approach where the database size is less than 16 TiB and when you don’t have transformation or filtering requirements. Backup and restore has the additional advantage of migrating your secondary database objects such as stored procedures, functions, and so on.

SQL Server Import and Export Wizard supports a wide range of features. Consider this approach as the next option to evaluate if you don’t need to migrate secondary database objects such as views, stored procedures, triggers, and so on. Also, use this approach to overcome the backup and restore limitations. SQL Server Import and Export can also be used for smaller migrations where ease of use considerations override the minor performance gains provided by SQL Server Backup and Restore.

Using Generate and Publish Scripts Wizard and bulk copy program utility (bcp) is slower than SQL Server Import and Export Wizard. You can use this approach in some cases because in bcp you can parallelize the load. That said, data files created by bcp may be orders of magnitude larger than the original table size. Because of this, you might need a significant amount of storage space when you use bcp to migrate in parallel.