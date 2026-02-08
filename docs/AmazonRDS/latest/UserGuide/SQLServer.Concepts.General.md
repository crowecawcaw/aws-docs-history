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
[Restoring
license-terminated DB instances for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md").

## Development and

test

Because of licensing requirements, we can't offer SQL Server Developer Edition on Amazon RDS. You can use Express Edition for many
development, testing, and other nonproduction needs. However, if you need the full feature capabilities of an enterprise-level
installation of SQL Server for development, you can download and install SQL Server Developer Edition on RDS Custom for SQL Server using a CEV with BYOM.
For more information, see [Preparing a CEV using Bring Your Own Media (BYOM)](custom-cev-sqlserver.md#custom-cev-sqlserver.preparing.byom "custom-cev-sqlserver.md#custom-cev-sqlserver.preparing.byom").
Dedicated infrastructure isn't required for Developer Edition. By using your own host, you also gain access to
other programmability features that are not accessible on Amazon RDS. For more information on the difference between SQL Server
editions, see [Editions and supported features of SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver15 "https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver15")
in the Microsoft documentation.
