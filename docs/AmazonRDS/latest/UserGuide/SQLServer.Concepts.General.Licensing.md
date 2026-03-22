# Licensing Microsoft SQL Server on Amazon RDS

When you set up an Amazon RDS DB instance for Microsoft SQL Server, the software license is
included.

This means that you don't need to purchase SQL Server licenses separately. AWS holds the
license for the SQL Server database software. Amazon RDS pricing includes the software license,
underlying hardware resources, and Amazon RDS management capabilities.

Amazon RDS supports the following Microsoft SQL Server editions:

- Enterprise
- Standard
- Web
- Express

###### Note

SQL Server Web Edition is designed for Web hosters and Web VAPs to host public and
internet-accessible web pages, websites, web applications, and web services.
This level of support is required for
compliance with Microsoft's usage rights. For more information, see [AWS service terms](http://aws.amazon.com/serviceterms "http://aws.amazon.com/serviceterms").

Amazon RDS supports Multi-AZ deployments for DB instances running Microsoft SQL Server
by using SQL Server Database Mirroring (DBM), Always On Availability Groups (AGs), and
block level replication for SQL Server Web Edition. There are no additional licensing requirements
for Multi-AZ deployments. For more information, see
[Multi-AZ deployments for Amazon RDS for Microsoft SQL Server](USER_SQLServerMultiAZ.md "USER_SQLServerMultiAZ.md").

## Restoring license-terminated DB instances

Amazon RDS takes snapshots of license-terminated DB instances. If your instance is
terminated for licensing issues, you can restore it from the snapshot to a new DB
instance. New DB instances have a license included.

For more information, see
[Restoring license-terminated DB instances for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.RestoreLTI.md "Appendix.SQLServer.CommonDBATasks.RestoreLTI.md").

## Development and test

For development and testing scenarios, you can use Express Edition for many development, testing, and other non-production needs. You can also use Developer Edition, which includes all SQL Server Enterprise Edition features but is licensed only for non-production use. You can download and install SQL Server Developer Edition on RDS for SQL Server. For more information, see [Working with SQL Server Developer Edition on RDS for SQL Server](sqlserver-dev-edition.md "sqlserver-dev-edition.md") using a Custom Engine Version (CEV) with Bring Your Own Media (BYOM).You can also download and install SQL Server Developer Edition on RDS Custom for SQL Server using the same approach. For more information, see [Preparing a CEV using Bring Your Own Media (BYOM)](custom-cev-sqlserver.preparing.md#custom-cev-sqlserver.preparing.byom "custom-cev-sqlserver.preparing.md#custom-cev-sqlserver.preparing.byom"). For more information on the difference between SQL Server
editions, see [Editions and supported features of SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver15 "https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver15")
in the Microsoft documentation.
