

# Limitations and recommendations
<a name="SSRS.Limitations"></a>

The following limitations and recommendations apply to running SSRS and Power BI Report Server (PBIRS) on RDS for SQL Server:
+ You can't use reporting services on DB instances that have read replicas.
+ Instances must use self-managed Active Directory or AWS Directory Service for Microsoft Active Directory for reporting services web portal and web server authentication. For more information, see [Working with Active Directory with RDS for SQL Server](User.SQLServer.ActiveDirectoryWindowsAuth.md). 
+ You can't back up the reporting server databases that are created with the reporting services option.
+ Importing and restoring report server databases from other instances of reporting services isn't supported. For more information, see [Report server databases](SSRS.DBs.md).
+ You can't configure reporting services to listen on the default SSL port (443). The allowed values are 1150–49511, except 1234, 1434, 3260, 3343, 3389, and 47001.
+ Subscriptions through a Microsoft Windows file share aren't supported.
+ Using Reporting Services Configuration Manager isn't supported.
+ Creating and modifying roles isn't supported.
+ Modifying report server properties isn't supported.
+ System administrator and system user roles aren't granted.
+ You can't edit system-level role assignments through the web portal.