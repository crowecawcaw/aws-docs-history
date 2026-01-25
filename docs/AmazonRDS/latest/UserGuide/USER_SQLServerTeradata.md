# Linked Servers with Teradata ODBC in RDS for SQL Server

Support for linked servers with the Teradata ODBC driver on RDS for SQL Server lets you access external data sources
on a Teradata database. You can read data and run commands from remote Teradata database servers outside of your RDS for SQL Server instance.
Use linked-servers with Teradata ODBC to enable the following capabilities:

- Directly access data sources other than SQL Server.
- Query against diverse Teradata data sources with the same query without moving the data.
- Issue distributed queries, updates, commands, and transactions on data sources across an enterprise ecosystem.
- Integrate connections to a Teradata database from within the Microsoft Business Intelligence Suite (SSIS, SSRS, SSAS).
- Migrate from a Teradata database to RDS for SQL Server.
  You can choose to activate one or more linked servers for Teradata on either an existing or new RDS for SQL Server DB instance. You can then integrate
  external Teradata data sources with your DB instance.

###### Topics

- [Supported versions and Regions](#USER_SQLServerTeradata.VersionRegionSupport "#USER_SQLServerTeradata.VersionRegionSupport")
- [Limitations and recommendations](#USER_SQLServerTeradata.LimitsandRecommendations "#USER_SQLServerTeradata.LimitsandRecommendations")
- [Considerations for Multi-AZ deployment](#USER_SQLServerTeradata.MultiAZ "#USER_SQLServerTeradata.MultiAZ")
- [Activating linked servers with Teradata](USER_SQLServerTeradata.md "USER_SQLServerTeradata.md")
- [Creating linked servers with Teradata](USER_SQLServerTeradata.md "USER_SQLServerTeradata.md")
- [Deactivating servers linked to Teradata](USER_SQLServerTeradata.md "USER_SQLServerTeradata.md")

## Supported versions and Regions

RDS for SQL Server supports linked servers with Teradata ODBC in all AWS Regions for SQL Server Standard and Enterprise Edition for the following versions:

- SQL Server 2022, all versions
- SQL Server 2019, all versions
- SQL Server 2017, all versions

The following Teradata database versions support linking with RDS for SQL Server

- Teradata 17.20, all versions

## Limitations and recommendations

The following limitations apply to linked servers with Teradata ODBC:

- RDS for SQL Server support only simple authentication with a username and password for the Teradata source.
- RDS for SQL Server supports only Teradata ODBC driver version 17.20.0.33.
- RDS for SQL Server does not support creating data source names (DSNs) to use as shortcuts for a connection string.
- RDS for SQL Server does not support ODBC driver tracing. Use SQL Server Extended Events to trace ODBC events. For more information, see [Set up Extended Events in RDS for SQL Server](https://aws.amazon.com/blogs/database/set-up-extended-events-in-amazon-rds-for-sql-server/ "https://aws.amazon.com/blogs/database/set-up-extended-events-in-amazon-rds-for-sql-server/").
- RDS for SQL Server does not support access to the catalogs folder for a Teradata linked server when using SQL Server Management Studio (SSMS).

Consider the following recommendations when using linked servers with Teradata ODBC:

- Allow network traffic by adding the applicable TCP port in the security group for each RDS for SQL Server DB instance.
  If you're configuring a linked server between an EC2 Teradata DB instance and an RDS for SQL Server DB instance,
  then you must allow traffic from the IP address of the EC2 Teradata DB instance. You also must allow traffic on the
  port that the RDS for SQL Server DB instance is using to listen for database communication.
  For more information on security groups, see [Controlling access with security
  groups](Overview.md "Overview.md").
- Distributed transactions (XA) are supported. To activate distributed transactions, turn on the `MSDTC` option in the
  option group for your DB instance and make sure XA transactions are turned on. For more information, see [Support for Microsoft Distributed Transaction Coordinator in RDS for SQL Server](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").
- Linked Teradata ODBC support SSL/TLS as long as configured on the Teradata Server.
  For more information, see [Enable TLS Connectivity on Teradata Vantage](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-Call-Level-Interface-Version-2-Reference-for-Workstation-Attached-Systems-20.00/Mainframe-TLS-Connectivity-Supplement/Enable-TLS-Connectivity-on-Teradata-Vantage "https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-Call-Level-Interface-Version-2-Reference-for-Workstation-Attached-Systems-20.00/Mainframe-TLS-Connectivity-Supplement/Enable-TLS-Connectivity-on-Teradata-Vantage").

## Considerations for Multi-AZ deployment

RDS for SQL Server currently doesn't replicate linked servers to the mirrored database server
(or Always-On availability group secondary server) in a Multi-AZ deployment. If the linked servers
are added before the configuration is changed to add mirroring or Always-On,
then the linked servers are copied for the existing linked servers.

Alternatively, you can create the linked servers on the primary instance, fail over to the high
availability server instance and then create the linked servers again so that they are on both RDS for SQL Server instances.
