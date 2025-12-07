# Amazon RDS for Microsoft SQL Server

Amazon RDS supports several versions and editions of Microsoft SQL Server. The following table shows the most recent supported minor version of each major version.
For the full list of supported versions, editions, and RDS engine versions, see [Microsoft SQL Server versions on Amazon RDS](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md").

| Major version   | Service Pack / GDR | Cumulative Update | Minor version | Knowledge Base Article                                                                                                                                                                                                                                                                                                                                           | Release Date       |
| --------------- | ------------------ | ----------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| SQL Server 2022 | Not applicable     | CU21              | 16.0.4215.2   | [KB5065865](https://learn.microsoft.com/en-us/troubleshoot/sql/releases/sqlserver-2022/cumulativeupdate21 "https://learn.microsoft.com/en-us/troubleshoot/sql/releases/sqlserver-2022/cumulativeupdate21")                                                                                                                                                       | September 11, 2025 |
| SQL Server 2019 | GDR                | CU32 GDR          | 15.0.4445.1   | [KB5065222](https://support.microsoft.com/en-us/topic/kb5065222-description-of-the-security-update-for-sql-server-2019-cu32-september-9-2025-152ac456-cb04-4b88-8177-a77fe24ac80d "https://support.microsoft.com/en-us/topic/kb5065222-description-of-the-security-update-for-sql-server-2019-cu32-september-9-2025-152ac456-cb04-4b88-8177-a77fe24ac80d")       | September 9, 2025  |
| SQL Server 2017 | GDR                | CU31 GDR          | 14.0.3505.1   | [KB5065225](https://support.microsoft.com/en-us/topic/kb5065225-description-of-the-security-update-for-sql-server-2017-cu31-september-9-2025-b1addb22-3bfd-4870-b914-c020c2a3d2be "https://support.microsoft.com/en-us/topic/kb5065225-description-of-the-security-update-for-sql-server-2017-cu31-september-9-2025-b1addb22-3bfd-4870-b914-c020c2a3d2be")       | September 9, 2025  |
| SQL Server 2016 | SP3 GDR            | Not applicable    | 13.0.6470.1   | [KB5065226](https://support.microsoft.com/en-us/topic/kb5065226-description-of-the-security-update-for-sql-server-2016-sp3-gdr-september-9-2025-7cf66f6b-dda8-47e1-bcb2-2f4630e5c48a "https://support.microsoft.com/en-us/topic/kb5065226-description-of-the-security-update-for-sql-server-2016-sp3-gdr-september-9-2025-7cf66f6b-dda8-47e1-bcb2-2f4630e5c48a") | September 9, 2025  |

For information about licensing for SQL Server, see [Licensing Microsoft SQL Server on Amazon RDS](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md"). For information about SQL Server
builds, see this Microsoft support article about
[Where to find information about the latest SQL Server builds](https://support.microsoft.com/en-us/topic/kb957826-where-to-find-information-about-the-latest-sql-server-builds-43994ba5-9aed-2323-ea7c-d29fe9c4fbe8 "https://support.microsoft.com/en-us/topic/kb957826-where-to-find-information-about-the-latest-sql-server-builds-43994ba5-9aed-2323-ea7c-d29fe9c4fbe8").

With Amazon RDS, you can create DB instances and DB snapshots, point-in-time restores, and
automated or manual backups. DB instances running SQL Server can be used inside a VPC. You
can also use Secure Sockets Layer (SSL) to connect to a DB instance running SQL Server,
and you can use transparent data encryption (TDE) to
encrypt data at rest. Amazon RDS currently supports Multi-AZ deployments for SQL Server using SQL
Server Database Mirroring (DBM) or Always On Availability Groups (AGs) as a high-availability, failover solution.

To deliver a managed service experience, Amazon RDS does not provide shell access to DB
instances, and it restricts access to certain system procedures and tables that require
advanced privileges. Amazon RDS supports access to databases on a DB instance using any standard
SQL client application such as Microsoft SQL Server Management Studio. Amazon RDS does not allow
direct host access to a DB instance via Telnet, Secure Shell (SSH), or Windows Remote
Desktop Connection. When you create a DB instance, the master user is assigned to the
_db_owner_ role for all user databases on that instance, and has all
database-level permissions except for those that are used for backups. Amazon RDS manages backups
for you.

Before creating your first DB instance, you should complete the steps in the setting up section of this
guide. For more information, see [Setting up your Amazon RDS environment](CHAP_SettingUp.md "CHAP_SettingUp.md").

###### Topics

- [Common management tasks for Microsoft SQL Server on Amazon RDS](#SQLServer.Concepts.General "#SQLServer.Concepts.General")
- [Limitations for Microsoft SQL Server DB instances](#SQLServer.Concepts.General.FeatureSupport.Limits "#SQLServer.Concepts.General.FeatureSupport.Limits")
- [DB instance class support for Microsoft SQL Server](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md")
- [Optimize CPUs for RDS for SQL Server license-included instances](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md")
- [Microsoft SQL Server security](SQLServer.Concepts.General.FeatureSupport.md "SQLServer.Concepts.General.FeatureSupport.md")
- [Compliance program support for Microsoft SQL Server DB instances](#SQLServer.Concepts.General.Compliance "#SQLServer.Concepts.General.Compliance")
- [Microsoft SQL Server versions on Amazon RDS](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md")
- [Microsoft SQL Server features on Amazon RDS](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md")
- [Multi-AZ deployments using Microsoft SQL Server Database Mirroring or Always On availability groups](#SQLServer.Concepts.General.Mirroring "#SQLServer.Concepts.General.Mirroring")
- [Using Transparent Data Encryption to encrypt data at rest](#SQLServer.Concepts.General.Options "#SQLServer.Concepts.General.Options")
- [Functions and stored procedures for Amazon RDS
  for Microsoft SQL Server](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md")
- [Local time zone for Microsoft SQL Server DB instances](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md")
- [Licensing Microsoft SQL Server on Amazon RDS](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md")
- [Connecting to your Microsoft SQL Server
  DB instance](USER_ConnectToMicrosoftSQLServerInstance.md "USER_ConnectToMicrosoftSQLServerInstance.md")
- [Working with SQL Server Developer Edition on RDS for SQL Server](sqlserver-dev-edition.md "sqlserver-dev-edition.md")
- [Working with Active Directory with RDS for SQL Server](User.SQLServer.md "User.SQLServer.md")
- [Upgrades of the Microsoft SQL Server DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md")
- [Working with storage in
  RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")
- [Importing and exporting SQL Server databases using native
  backup and restore](SQLServer.Procedural.md "SQLServer.Procedural.md")
- [Working with read replicas for Microsoft SQL Server in Amazon RDS](SQLServer.md "SQLServer.md")
- [Multi-AZ deployments for Amazon RDS for Microsoft SQL Server](USER_SQLServerMultiAZ.md "USER_SQLServerMultiAZ.md")
- [Additional features for Microsoft SQL Server on Amazon RDS](User.SQLServer.md "User.SQLServer.md")
- [Options for the Microsoft SQL Server database engine](Appendix.SQLServer.md "Appendix.SQLServer.md")
- [Common DBA tasks for Amazon RDS for Microsoft SQL Server](Appendix.SQLServer.md "Appendix.SQLServer.md")

## Common management tasks for Microsoft SQL Server on Amazon RDS

The following are the common management tasks you perform with an Amazon RDS for SQL Server DB instance, with links to relevant
documentation for each task.

| Task area                                   | Description                                                                                                                                                                                                                                                                                | Relevant documentation                                                                                                                                                                                                                                                             |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instance classes, storage, and<br>PIOPS** | If you are creating a DB instance for production purposes, you<br>should understand how instance classes, storage types, and<br>Provisioned IOPS work in Amazon RDS.                                                                                                                       | [DB instance class support for Microsoft SQL Server](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md")<br>[Amazon RDS storage types](CHAP_Storage.md#Concepts.Storage "CHAP_Storage.md#Concepts.Storage")                                                             |
| **Multi-AZ deployments**                    | A production DB instance should use Multi-AZ deployments. Multi-AZ<br>deployments provide increased availability, data durability, and<br>fault tolerance for DB instances. Multi-AZ deployments for SQL<br>Server are implemented using SQL Server's native DBM or AGs<br>technology.     | [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md")<br>[Multi-AZ deployments using Microsoft SQL Server Database Mirroring or Always On availability groups](#SQLServer.Concepts.General.Mirroring "#SQLServer.Concepts.General.Mirroring") |
| **Amazon Virtual Private Cloud (VPC)**      | If your AWS account has a default VPC, then your DB instance is<br>automatically created inside the default VPC. If your account does<br>not have a default VPC, and you want the DB instance in a VPC, you<br>must create the VPC and subnet groups before you create the DB<br>instance. | [Working with a DB instance in a VPC](USER_VPC.md "USER_VPC.md")                                                                                                                                                                                                                   |
| **Security groups**                         | By default, DB instances are created with a firewall that prevents<br>access to them. You therefore must create a security group with the<br>correct IP addresses and network configuration to access the DB<br>instance.                                                                  | [Controlling access with security<br>groups](Overview.md "Overview.md")                                                                                                                                                                                                            |
| **Parameter groups**                        | If your DB instance is going to require specific database<br>parameters, you should create a parameter group before you create<br>the DB instance.                                                                                                                                         | [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md")                                                                                                                                                                                 |
| **Option groups**                           | If your DB instance is going to require specific database options,<br>you should create an option group before you create the DB instance.                                                                                                                                                 | [Options for the Microsoft SQL Server database engine](Appendix.SQLServer.md "Appendix.SQLServer.md")                                                                                                                                                                              |
| **Connecting to your DB<br>instance**       | After creating a security group and associating it to a DB<br>instance, you can connect to the DB instance using any standard SQL<br>client application such as Microsoft SQL Server Management Studio.                                                                                    | [Connecting to your Microsoft SQL Server<br>DB instance](USER_ConnectToMicrosoftSQLServerInstance.md "USER_ConnectToMicrosoftSQLServerInstance.md")                                                                                                                                |
| **Backup and restore**                      | When you create your DB instance, you can configure it to take<br>automated backups. You can also back up and restore your databases<br>manually by using full backup files (.bak files).                                                                                                  | [Introduction to backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md")<br>[Importing and exporting SQL Server databases using native<br>backup and restore](SQLServer.Procedural.md "SQLServer.Procedural.md")                                       |
| **Monitoring**                              | You can monitor your SQL Server DB instance by using CloudWatch Amazon RDS<br>metrics, events, and enhanced monitoring.                                                                                                                                                                    | [Viewing metrics in the Amazon RDS console](USER_Monitoring.md "USER_Monitoring.md")<br>[Viewing Amazon RDS events](USER_ListEvents.md "USER_ListEvents.md")                                                                                                                       |
| **Log files**                               | You can access the log files for your SQL Server DB instance.                                                                                                                                                                                                                              | [Monitoring Amazon RDS log files](USER_LogAccess.md "USER_LogAccess.md")<br>[Amazon RDS for Microsoft SQL Server database log<br>files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md")                                                                                   |

There are also advanced administrative tasks for working with SQL Server DB instances.
For more information, see the following documentation:

- [Common DBA tasks for Amazon RDS for Microsoft SQL Server](Appendix.SQLServer.md "Appendix.SQLServer.md").
- [Working with AWS Managed Active Directory with RDS for SQL Server](USER_SQLServerWinAuth.md "USER_SQLServerWinAuth.md")
- [Accessing the tempdb database](SQLServer.md "SQLServer.md")

## Limitations for Microsoft SQL Server DB instances

The Amazon RDS implementation of Microsoft SQL Server on a DB instance has some limitations that you should be aware of:

- The maximum number of databases supported on a DB instance depends on the instance class
  type and the availability mode—Single-AZ, Multi-AZ Database Mirroring
  (DBM), or Multi-AZ Availability Groups (AGs). The Microsoft SQL Server system
  databases don't count toward this limit.

The following table shows the maximum number of supported databases for each
instance class type and availability mode. Use this table to help you decide if
you can move from one instance class type to another, or from one availability
mode to another. If your source DB instance has more databases than the target
instance class type or availability mode can support, modifying the DB instance
fails. You can see the status of your request in the **Events**
pane.

| Instance class type              | Allowed vCPU range      | Single-AZ | Multi-AZ with DBM | Multi-AZ with Always On AGs |
| -------------------------------- | ----------------------- | --------- | ----------------- | --------------------------- |
| db.\*.micro to db.\*.medium      | N/A                     | 30        | N/A               | N/A                         |
| db.\*.large                      | N/A                     | 30        | 30                | 30                          |
| db.\*.xlarge to db.\*.16xlarge   | 4 vCPUs<br>• 64 vCPUs   | 100       | 50                | 75                          |
| db.\*.24xlarge to db.\*.32xlarge | 4 vCPUs<br>• 64 vCPUs   | 100       | 50                | 100                         |
| db.\*.24xlarge to db.\*.32xlarge | 96 vCPUs<br>• 128 vCPUs | 100       | 50                | 100                         |

\* Represents the different instance class types.

For example, let's say that your DB instance runs on a db.\*.16xlarge with Single-AZ and that
it has 76 databases. You modify the DB instance to upgrade to using Multi-AZ
Always On AGs. This upgrade fails, because your DB instance contains more
databases than your target configuration can support. If you upgrade your
instance class type to db.\*.24xlarge instead, the modification succeeds.

If the upgrade fails, you see events and messages similar to the following:

    + **`Unable to modify database instance class. The instance has 76
     databases, but after conversion it would only support
     75.`**
    + **`Unable to convert the DB instance to Multi-AZ: The instance
     has 76 databases, but after conversion it would only support
     75.`**

If the point-in-time restore or snapshot restore fails, you see events and messages
similar to the following:

    + **`Database instance put into incompatible-restore. The instance
     has 76 databases, but after conversion it would only support
     75.`**

- The following ports are reserved for Amazon RDS, and you can't use them when you create a DB
  instance: `1234, 1434, 3260, 3343, 3389, 47001,` and `49152-49156`.
- Client connections from IP addresses within the range 169.254.0.0/16 are not permitted.
  This is the Automatic Private IP Addressing Range (APIPA), which is used for
  local-link addressing.
- SQL Server Standard Edition uses only a subset of the available processors if the DB instance has more processors than the
  software limits (24 cores, 4 sockets, and 128GB RAM). Examples of this are the db.m5.24xlarge and db.r5.24xlarge
  instance classes.

For more information, see the table of scale limits under [Editions and supported features
of SQL Server 2019 (15.x)](https://docs.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-version-15 "https://docs.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-version-15") in the Microsoft documentation.

- Amazon RDS for SQL Server doesn't support importing data into the msdb database.
- You can't rename databases on a DB instance in a SQL Server Multi-AZ deployment.
- Make sure that you use these guidelines when setting the following DB parameters on RDS for SQL Server:

      + `max server memory (mb)` >= 256 MB
      + `max worker threads` >= (number of logical CPUs \* 7)

  For more information on setting DB parameters, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

- The maximum storage size for SQL Server DB instances is the following:

      + General Purpose (SSD) storage – 16 TiB for all editions
      + Provisioned IOPS storage – 64 TiB for all editions
      + Magnetic storage – 1 TiB for all editions

  If you have a scenario that requires a larger amount of storage, you can use
  sharding across multiple DB instances to get around the limit. This approach
  requires data-dependent routing logic in applications that connect to the
  sharded system. You can use an existing sharding framework, or you can write
  custom code to enable sharding. If you use an existing framework, the framework
  can't install any components on the same server as the DB instance.

- The minimum storage size for SQL Server DB instances is the following:
  - General Purpose (SSD) storage – 20 GiB for Enterprise, Standard, Web, and Express Editions
  - Provisioned IOPS storage – 20 GiB for Enterprise, Standard, Web, and Express Editions
  - Magnetic storage – 20 GiB for Enterprise, Standard, Web, and Express Editions

- Amazon RDS doesn't support running these services on the same server as your RDS DB instance:

      + Data Quality Services
      + Master Data Services

  To use these features, we recommend that you install SQL Server on an Amazon EC2 instance, or
  use an on-premises SQL Server instance. In these cases, the EC2 or SQL Server
  instance acts as the Master Data Services server for your SQL Server DB instance
  on Amazon RDS. You can install SQL Server on an Amazon EC2 instance with Amazon EBS storage,
  pursuant to Microsoft licensing policies.

- Because of limitations in Microsoft SQL Server, restoring to a point in time before
  successfully running `DROP DATABASE` might not reflect the state of
  that database at that point in time. For example, the dropped database is
  typically restored to its state up to 5 minutes before the `DROP
DATABASE` command was issued. This type of restore means that you
  can't restore the transactions made during those few minutes on your dropped
  database. To work around this, you can reissue the `DROP DATABASE`
  command after the restore operation is completed. Dropping a database removes
  the transaction logs for that database.
- For SQL Server, you create your databases after you create your DB instance. Database names follow the usual SQL Server naming rules
  with the following differences:
  - Database names can't start with `rdsadmin`.
  - They can't start or end with a space or a tab.
  - They can't contain any of the characters that create a new line.
  - They can't contain a single quote (`'`).

- SQL Server Web Edition only allows you to use the **Dev/Test** template when
  creating a new RDS for SQL Server DB instance.
- SQL Server Web Edition is designed for web hosters and web VAPs to host public and
  internet-accessible web pages, websites, web applications, and web services. For more information, see
  [Licensing Microsoft SQL Server on Amazon RDS](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md").

## Compliance program support for Microsoft SQL Server DB instances

AWS Services in scope have been fully assessed by a third-party auditor and result in a certification, attestation of compliance, or
Authority to Operate (ATO). For more information, see [AWS services in scope by compliance program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").

### HIPAA support for Microsoft SQL Server DB instances

You can use Amazon RDS for Microsoft SQL Server databases to build HIPAA-compliant applications.
You can store healthcare-related information, including protected health information
(PHI), under a Business Associate Agreement (BAA) with AWS. For more information,
see [HIPAA compliance](https://aws.amazon.com/compliance/hipaa-compliance/ "https://aws.amazon.com/compliance/hipaa-compliance/").

Amazon RDS for SQL Server supports HIPAA for the following versions and editions:

- SQL Server 2022 Enterprise, Standard, and Web Editions
- SQL Server 2019 Enterprise, Standard, and Web Editions
- SQL Server 2017 Enterprise, Standard, and Web Editions
- SQL Server 2016 Enterprise, Standard, and Web Editions

To enable HIPAA support on your DB instance, set up the following three components.

| Component            | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Auditing             | To set up auditing, set the parameter `rds.sqlserver_audit` to the value `fedramp_hipaa`. If your DB<br>instance is not already using a custom DB parameter group, you must create a custom parameter group and<br>attach it to your DB instance before you can modify the `rds.sqlserver_audit` parameter. For<br>more information, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").                                                                                                                                            |
| Transport encryption | To set up transport encryption, force all connections to your DB instance to use Secure Sockets Layer (SSL). For more<br>information, see [Forcing connections to your DB<br>instance to use SSL](SQLServer.Concepts.General.SSL.md#SQLServer.Concepts.General.SSL.Forcing "SQLServer.Concepts.General.SSL.md#SQLServer.Concepts.General.SSL.Forcing").                                                                                                                                                                                                                                 |
| Encryption at rest   | To set up encryption at rest, you have two options:<br>1. If you're running SQL Server 2016–2022 Enterprise Edition or 2022<br>Standard Edition, you can use Transparent Data<br>Encryption (TDE) to achieve encryption at rest. For more<br>information, see [Support for Transparent Data Encryption in SQL Server](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").<br>2. You can set up encryption at rest by using AWS Key Management Service (AWS KMS) encryption keys. For more information, see [Encrypting Amazon RDS<br>resources](Overview.md "Overview.md"). |

## Multi-AZ deployments using Microsoft SQL Server Database Mirroring or Always On availability groups

Amazon RDS supports Multi-AZ deployments for DB instances running Microsoft SQL Server by using
SQL Server Database Mirroring (DBM) or Always On Availability Groups (AGs).
Multi-AZ deployments provide increased availability, data
durability, and fault tolerance for DB instances. In the event of planned database
maintenance or unplanned service disruption, Amazon RDS automatically fails over to the
up-to-date secondary replica so database operations can resume quickly without manual
intervention. The primary and secondary instances use the same endpoint, whose physical
network address transitions to the passive secondary replica as part of the failover
process. You don't have to reconfigure your application when a failover occurs.

Amazon RDS manages failover by actively monitoring your Multi-AZ deployment and initiating a
failover when a problem with your primary occurs. Failover doesn't occur unless the
standby and primary are fully in sync. Amazon RDS actively maintains your Multi-AZ deployment
by automatically repairing unhealthy DB instances and re-establishing synchronous
replication. You don't have to manage anything. Amazon RDS handles the primary, the witness,
and the standby instance for you. When you set up SQL Server Multi-AZ, RDS configures
passive secondary instances for all of the databases on the instance.

For more information, see [Multi-AZ deployments for Amazon RDS for Microsoft SQL Server](USER_SQLServerMultiAZ.md "USER_SQLServerMultiAZ.md").

## Using Transparent Data Encryption to encrypt data at rest

Amazon RDS supports Microsoft SQL Server Transparent Data Encryption (TDE), which
transparently encrypts stored data. Amazon RDS uses option groups to enable and configure
these features. For more information about the TDE option, see [Support for Transparent Data Encryption in SQL Server](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").
