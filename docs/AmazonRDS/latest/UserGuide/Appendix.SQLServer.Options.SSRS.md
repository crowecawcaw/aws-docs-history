

# Support for SQL Server Reporting Services and Power BI Report Server in Amazon RDS for SQL Server
<a name="Appendix.SQLServer.Options.SSRS"></a>

Starting with SQL Server 2025, Microsoft has consolidated all reporting services under Power BI Report Server (PBIRS), replacing SSRS. If you upgrade an existing RDS DB instance with SSRS to SQL Server 2025, SSRS is automatically replaced by PBIRS. For more information about the upgrade process, see [Upgrading from SSRS to PBIRS](SSRS.Upgrade.md). Like SSRS, PBIRS provides a report server with a web portal where you can display and manage reports and KPIs. With PBIRS, you can run Power BI reports (.pbix) and paginated reports (.rdl), which makes it a superset of SSRS functionality. Everything you can do in SSRS, you can do in PBIRS, with the addition of interactive Power BI report types.

Amazon RDS supports PBIRS for SQL Server Standard and Enterprise Editions on the following versions:
+ SQL Server 2025, all versions

Microsoft SQL Server Reporting Services (SSRS) is a server-based application used for report generation and distribution. It's part of a suite of SQL Server services that also includes SQL Server Analysis Services (SSAS) and SQL Server Integration Services (SSIS). SSRS is a service built on top of SQL Server. You can use it to collect data from various data sources and present it in a way that's easily understandable and ready for analysis.

Amazon RDS for SQL Server supports running SSRS and PBIRS directly on RDS DB instances. You can use SSRS or PBIRS with existing or new DB instances.

Amazon RDS supports SSRS for SQL Server Standard and Enterprise Editions on the following versions:
+ SQL Server 2022, all versions
+ SQL Server 2019, version 15.00.4043.16.v1 and higher
+ SQL Server 2017, version 14.00.3223.3.v1 and higher
+ SQL Server 2016, version 13.00.5820.21.v1 and higher

**Contents**
+ [Upgrading from SSRS to PBIRS](SSRS.Upgrade.md)
+ [Limitations and recommendations](SSRS.Limitations.md)
+ [Turning on SSRS or PBIRS](SSRS.Enabling.md)
  + [Creating an option group for SSRS or PBIRS](SSRS.Enabling.md#SSRS.OptionGroup)
  + [Adding the SSRS or PBIRS option to your option group](SSRS.Enabling.md#SSRS.Add)
  + [Associating your option group with your DB instance](SSRS.Enabling.md#SSRS.Apply)
  + [Allowing inbound access to your VPC security group](SSRS.Enabling.md#SSRS.Inbound)
+ [Report server databases](SSRS.DBs.md)
+ [SSRS and PBIRS log files](SSRS.Logs.md)
+ [Accessing the SSRS or PBIRS web portal](SSRS.Access.md)
  + [Using SSL on RDS](SSRS.Access.md#SSRS.Access.SSL)
  + [Granting access to domain users](SSRS.Access.md#SSRS.Access.Grant)
  + [Accessing the web portal](SSRS.Access.md#SSRS.Access.Portal)
+ [Deploying reports and configuring report data sources](SSRS.DeployConfig.md)
  + [Deploying reports to SSRS](SSRS.DeployConfig.md#SSRS.Deploy)
  + [Configuring the report data source](SSRS.DeployConfig.md#SSRS.ConfigureDataSource)
+ [Using reporting services email to send reports](SSRS.Email.md)
+ [Revoking system-level permissions](SSRS.Access.Revoke.md)
+ [Monitoring the status of a task](SSRS.Monitor.md)
+ [Disabling and deleting SSRS or PBIRS databases](SSRS.DisableDelete.md)
  + [Turning off SSRS or PBIRS](SSRS.DisableDelete.md#SSRS.Disable)
  + [Deleting the SSRS or PBIRS databases](SSRS.DisableDelete.md#SSRS.Drop)