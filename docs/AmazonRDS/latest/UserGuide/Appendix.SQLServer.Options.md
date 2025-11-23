# Support for SQL Server Analysis Services in Amazon RDS for SQL Server

Microsoft SQL Server Analysis Services (SSAS) is part of the Microsoft Business Intelligence (MSBI) suite. SSAS is an online
analytical processing (OLAP) and data mining tool that is installed within SQL Server. You use SSAS to analyze data to help make
business decisions. SSAS differs from the SQL Server relational database because SSAS is optimized for queries and calculations
common in a business intelligence environment.

You can turn on SSAS for existing or new DB instances. It's installed on the same DB
instance as your database engine. For more information on SSAS, see the Microsoft [Analysis services
documentation](https://docs.microsoft.com/en-us/analysis-services "https://docs.microsoft.com/en-us/analysis-services").

Amazon RDS supports SSAS for SQL Server Standard and Enterprise Editions on the following versions:

- Tabular mode:
  - SQL Server 2019, version 15.00.4043.16.v1 and higher
  - SQL Server 2017, version 14.00.3223.3.v1 and higher
  - SQL Server 2016, version 13.00.5426.0.v1 and higher

- Multidimensional mode:
  - SQL Server 2019, version 15.00.4153.1.v1 and higher
  - SQL Server 2017, version 14.00.3381.3.v1 and higher
  - SQL Server 2016, version 13.00.5882.1.v1 and higher

###### Contents

- [Limitations](Appendix.SQLServer.Options.md#SSAS.Limitations "Appendix.SQLServer.Options.md#SSAS.Limitations")
- [Turning on SSAS](SSAS.md "SSAS.md")
  - [Creating an option group for SSAS](SSAS.md#SSAS.OptionGroup "SSAS.md#SSAS.OptionGroup")
  - [Adding the SSAS option to the option group](SSAS.md#SSAS.Add "SSAS.md#SSAS.Add")
  - [Associating the option group with your DB instance](SSAS.md#SSAS.Apply "SSAS.md#SSAS.Apply")
  - [Allowing inbound access to your VPC security group](SSAS.md#SSAS.InboundRule "SSAS.md#SSAS.InboundRule")
  - [Enabling Amazon S3 integration](SSAS.md#SSAS.EnableS3 "SSAS.md#SSAS.EnableS3")

- [Deploying SSAS projects on Amazon RDS](SSAS.md "SSAS.md")
- [Monitoring the status of a deployment task](SSAS.md "SSAS.md")
- [Using SSAS on Amazon RDS](SSAS.md "SSAS.md")
  - [Setting up a Windows-authenticated user for SSAS](SSAS.md#SSAS.Use.Auth "SSAS.md#SSAS.Use.Auth")
  - [Adding a domain user as a database administrator](SSAS.md#SSAS.Admin "SSAS.md#SSAS.Admin")
  - [Creating an SSAS proxy](SSAS.md#SSAS.Use.Proxy "SSAS.md#SSAS.Use.Proxy")
  - [Scheduling SSAS database processing using SQL Server Agent](SSAS.md#SSAS.Use.Schedule "SSAS.md#SSAS.Use.Schedule")
  - [Revoking SSAS access from the proxy](SSAS.md#SSAS.Use.Revoke "SSAS.md#SSAS.Use.Revoke")

- [Backing up an SSAS database](SSAS.md "SSAS.md")
- [Restoring an SSAS database](SSAS.md "SSAS.md")
  - [Restoring a DB instance to a specified time](SSAS.md#SSAS.PITR "SSAS.md#SSAS.PITR")

- [Changing the SSAS mode](SSAS.md "SSAS.md")
- [Turning off SSAS](SSAS.md "SSAS.md")
- [Troubleshooting SSAS issues](SSAS.md "SSAS.md")

## Limitations

The following limitations apply to using SSAS on RDS for SQL Server:

- RDS for SQL Server supports running SSAS in Tabular or Multidimensional mode. For more information, see [Comparing tabular and
  multidimensional solutions](https://docs.microsoft.com/en-us/analysis-services/comparing-tabular-and-multidimensional-solutions-ssas "https://docs.microsoft.com/en-us/analysis-services/comparing-tabular-and-multidimensional-solutions-ssas") in the Microsoft documentation.
- You can only use one SSAS mode at a time. Before changing modes, make sure to
  delete all of the SSAS databases.

For more information, see [Changing the SSAS mode](SSAS.md "SSAS.md").

- Multi-AZ instances aren't supported.
- Instances must use self-managed Active Directory or AWS Directory Service for Microsoft Active Directory for SSAS authentication. For more information, see [Working with Active Directory with RDS for SQL Server](User.SQLServer.md "User.SQLServer.md").
- Users aren't given SSAS server administrator access, but they can be granted
  database-level administrator access.
- The only supported port for accessing SSAS is 2383.
- You can't deploy projects directly. We provide an RDS stored procedure to do this. For more information, see [Deploying SSAS projects on Amazon RDS](SSAS.md "SSAS.md").
- Processing during deployment isn't supported.
- Using .xmla files for deployment isn't supported.
- SSAS project input files and database backup output files can only be in the
  `D:\S3` folder on the DB instance.
