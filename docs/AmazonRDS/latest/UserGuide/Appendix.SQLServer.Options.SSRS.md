# Support for SQL Server Reporting Services in Amazon RDS for SQL Server

Microsoft SQL Server Reporting Services (SSRS) is a server-based application used for report
generation and distribution. It's part of a suite of SQL Server services that also
includes SQL Server Analysis Services (SSAS) and SQL Server Integration Services (SSIS).
SSRS is a service built on top of SQL Server. You can use it to collect data from various
data sources and present it in a way that's easily understandable and ready for
analysis.

Amazon RDS for SQL Server supports running SSRS directly on RDS DB instances. You can use SSRS with existing or new DB instances.

RDS supports SSRS for SQL Server Standard and Enterprise Editions on the following versions:

- SQL Server 2022, all versions
- SQL Server 2019, version 15.00.4043.16.v1 and higher
- SQL Server 2017, version 14.00.3223.3.v1 and higher
- SQL Server 2016, version 13.00.5820.21.v1 and higher

###### Contents

- [Limitations and recommendations](Appendix.SQLServer.Options.SSRS.md#SSRS.Limitations "Appendix.SQLServer.Options.SSRS.md#SSRS.Limitations")
- [Turning on SSRS](SSRS.Enabling.md "SSRS.Enabling.md")

  - [Creating an option group for SSRS](SSRS.Enabling.md#SSRS.OptionGroup "SSRS.Enabling.md#SSRS.OptionGroup")
  - [Adding the SSRS option to your option group](SSRS.Enabling.md#SSRS.Add "SSRS.Enabling.md#SSRS.Add")
  - [Associating your option group with your DB instance](SSRS.Enabling.md#SSRS.Apply "SSRS.Enabling.md#SSRS.Apply")
  - [Allowing inbound access to your VPC security group](SSRS.Enabling.md#SSRS.Inbound "SSRS.Enabling.md#SSRS.Inbound")

- [Report server databases](Appendix.SQLServer.Options.SSRS.md#SSRS.DBs "Appendix.SQLServer.Options.SSRS.md#SSRS.DBs")
- [SSRS log files](Appendix.SQLServer.Options.SSRS.md#SSRS.Logs "Appendix.SQLServer.Options.SSRS.md#SSRS.Logs")
- [Accessing the SSRS web portal](SSRS.Access.md "SSRS.Access.md")

  - [Using SSL on RDS](SSRS.Access.md#SSRS.Access.SSL "SSRS.Access.md#SSRS.Access.SSL")
  - [Granting access to domain users](SSRS.Access.md#SSRS.Access.Grant "SSRS.Access.md#SSRS.Access.Grant")
  - [Accessing the web portal](SSRS.Access.md#SSRS.Access "SSRS.Access.md#SSRS.Access")

- [Deploying reports and configuring report data sources](SSRS.DeployConfig.md "SSRS.DeployConfig.md")

  - [Deploying reports to SSRS](SSRS.DeployConfig.md#SSRS.Deploy "SSRS.DeployConfig.md#SSRS.Deploy")
  - [Configuring the report data source](SSRS.DeployConfig.md#SSRS.ConfigureDataSource "SSRS.DeployConfig.md#SSRS.ConfigureDataSource")

- [Using SSRS Email to send reports](SSRS.Email.md "SSRS.Email.md")
- [Revoking system-level permissions](SSRS.Access.Revoke.md "SSRS.Access.Revoke.md")
- [Monitoring the status of a task](SSRS.Monitor.md "SSRS.Monitor.md")
- [Disabling and deleting SSRS databases](SSRS.DisableDelete.md "SSRS.DisableDelete.md")

  - [Turning off SSRS](SSRS.DisableDelete.md#SSRS.Disable "SSRS.DisableDelete.md#SSRS.Disable")
  - [Deleting the SSRS databases](SSRS.DisableDelete.md#SSRS.Drop "SSRS.DisableDelete.md#SSRS.Drop")

## Limitations and recommendations

The following limitations and recommendations apply to running SSRS on RDS for SQL Server:

- You can't use SSRS on DB instances that have read replicas.
- Instances must use self-managed Active Directory or AWS Directory Service for Microsoft Active Directory for SSRS web portal and web server authentication. For more information, see [Working with Active Directory with RDS for SQL Server](User.SQLServer.ActiveDirectoryWindowsAuth.md "User.SQLServer.ActiveDirectoryWindowsAuth.md").
- You can't back up the reporting server databases that are created with the SSRS option.
- Importing and restoring report server databases from other instances of SSRS isn't
  supported. For more information, see [Report server databases](#SSRS.DBs "#SSRS.DBs").
- You can't configure SSRS to listen on the default SSL port (443). The allowed values are
  1150–49511, except 1234, 1434, 3260, 3343, 3389, and 47001.
- Subscriptions through a Microsoft Windows file share aren't supported.
- Using Reporting Services Configuration Manager isn't supported.
- Creating and modifying roles isn't supported.
- Modifying report server properties isn't supported.
- System administrator and system user roles aren't granted.
- You can't edit system-level role assignments through the web portal.

## Report server databases

When your DB instance is associated with the SSRS option, two new databases are created on your DB instance:

- `rdsadmin_ReportServer`
- `rdsadmin_ReportServerTempDB`

These databases act as the ReportServer and ReportServerTempDB databases.
SSRS stores its data in the ReportServer database and caches its data in the ReportServerTempDB database.
For more information, see [Report Server Database](https://learn.microsoft.com/en-us/sql/reporting-services/report-server/report-server-database-ssrs-native-mode?view=sql-server-ver15 "https://learn.microsoft.com/en-us/sql/reporting-services/report-server/report-server-database-ssrs-native-mode?view=sql-server-ver15")
in the Microsoft documentation.

RDS owns and manages these databases, so database operations on them such as ALTER and DROP aren't permitted.
Access isn't permitted on the `rdsadmin_ReportServerTempDB` database. However,
you can perform read operations on the `rdsadmin_ReportServer`database.

## SSRS log files

You can list, view, and download SSRS log files. SSRS log files follow a naming convention of ReportServerService\_`timestamp`.log.
These report server logs are located in the `D:\rdsdbdata\Log\SSRS` directory. (The `D:\rdsdbdata\Log` directory is also the
parent directory for error logs and SQL Server Agent logs.). For more information, see [Viewing and listing database log files](USER_LogAccess.Procedural.Viewing.md "USER_LogAccess.Procedural.Viewing.md").

For existing SSRS instances, restarting the SSRS service might be necessary to access report server logs. You can restart the
service by updating the `SSRS` option.

For more information, see [Working with Amazon RDS for Microsoft SQL Server logs](Appendix.SQLServer.CommonDBATasks.Logs.md "Appendix.SQLServer.CommonDBATasks.Logs.md").
