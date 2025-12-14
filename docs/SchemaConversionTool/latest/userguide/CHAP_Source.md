# Connect Microsoft SQL Servers with AWS Schema Conversion Tool

You can use AWS SCT to convert schemas, database code objects, and application code
from SQL Server to the following targets:

- Amazon RDS for MySQL
- Amazon Aurora MySQL-Compatible Edition
- Amazon RDS for PostgreSQL
- Amazon Aurora PostgreSQL-Compatible Edition
- Amazon RDS for SQL Server
- Amazon RDS for MariaDB

###### Note

AWS SCT does not support using Amazon RDS for SQL server as a source.

You can use AWS SCT to create an assessment report for the migration of
schemas, database code objects, and application code from SQL Server to Babelfish for Aurora PostgreSQL, as described following.

###### Topics

- [Privileges for Microsoft SQL Server as a source](#CHAP_Source.SQLServer.Permissions "#CHAP_Source.SQLServer.Permissions")
- [Using Windows Authentication when using Microsoft SQL Server as a source](#CHAP_Source.SQLServer.Permissions.WinAuth "#CHAP_Source.SQLServer.Permissions.WinAuth")
- [Connecting to SQL Server as a source](#CHAP_Source.SQLServer.Connecting "#CHAP_Source.SQLServer.Connecting")
- [Converting SQL Server to MySQL](CHAP_Source.SQLServer.md "CHAP_Source.SQLServer.md")
- [Migrating from SQL Server to PostgreSQL with AWS Schema Conversion Tool](CHAP_Source.SQLServer.md "CHAP_Source.SQLServer.md")
- [Migrating from SQL Server to Amazon RDS for SQL Server with AWS Schema Conversion Tool](CHAP_Source.SQLServer.md "CHAP_Source.SQLServer.md")

## Privileges for Microsoft SQL Server as a source

The privileges required for Microsoft SQL Server as a source
are as follows:

- VIEW DEFINITION
- VIEW DATABASE STATE

The `VIEW DEFINITION` privilege enables users that have public
access to see object definitions. AWS SCT uses the `VIEW DATABASE STATE`
privilege to check the features of the SQL Server Enterprise edition.

Repeat the grant for each database whose schema you are converting.

In addition, grant the following privileges on the `master` database:

- VIEW SERVER STATE
- VIEW ANY DEFINITION

AWS SCT uses the `VIEW SERVER STATE` privilege to collect server
settings and configuration. Make sure that you grant the `VIEW ANY DEFINITION`
privilege to view endpoints.

To read information about Microsoft Analysis Services, run the following command
on the `master` database.

```
EXEC master..sp_addsrvrolemember @loginame = N'`<user_name>`', @rolename = N'sysadmin'
```

In the preceding example, replace the
`<user_name>` placeholder with the
name of the user that you granted with the privileges before.

To read information about SQL Server Agent, add your user to the
`SQLAgentUser` role. Run the following command on the `msdb`
database.

```
EXEC sp_addrolemember `<SQLAgentRole>`, `<user_name>`;
```

In the preceding example, replace the
`<SQLAgentRole>` placeholder with
the name of the SQL Server Agent role. Then replace the
`<user_name>` placeholder with the
name of the user that you granted with the privileges before. For more information, see
[Adding a user to the SQLAgentUser role](../../../AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.md#SQLServerAgent.AddUser "../../../AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.md#SQLServerAgent.AddUser") in the
_Amazon RDS User Guide_.

To detect log shipping, grant the `SELECT on dbo.log_shipping_primary_databases`
privilege on the `msdb` database.

To use the notification approach of the DDL replication, grant the `RECEIVE ON
 `<schema_name>`.`<queue_name>`  privilege on your source databases. In this example, replace the
 `<schema_name>`placeholder with the
 schema name of your database. Then, replace the
`<queue_name>`` placeholder with the
name of a queue table.

## Using Windows Authentication when using Microsoft SQL Server as a source

If your application runs on a Windows-based intranet, you might be able to use
Windows Authentication for database access. Windows Authentication uses the current Windows
identity established on the operating system thread to access the SQL Server database. You can
then map the Windows identity to a SQL Server database and permissions. To connect to SQL
Server using Windows Authentication, you must specify the Windows identity that your
application is using. You must also grant the Windows identity access to the SQL Server
database.

SQL Server has two modes of access: Windows Authentication mode and Mixed Mode. Windows
Authentication mode enables Windows Authentication and disables SQL Server Authentication.
Mixed Mode enables both Windows Authentication and SQL Server Authentication. Windows
Authentication is always available and cannot be disabled. For more information about Windows
Authentication, see the Microsoft Windows documentation.

The possible example for creating a user in TEST_DB is shown following.

```
USE [TEST_DB]
CREATE USER [TestUser] FOR LOGIN [TestDomain\TestUser]
GRANT VIEW DEFINITION TO [TestUser]
GRANT VIEW DATABASE STATE TO [TestUser]
```

### Using Windows Authentication with a JDBC connection

The JDBC driver does not support Windows Authentication when the driver is
used on non-Windows operating systems. Windows Authentication credentials, such as user name
and password, are not automatically specified when connecting to SQL Server from non-Windows operating systems. In such
cases, the applications must use SQL Server Authentication instead.

In JDBC connection string, the parameter `integratedSecurity` must
be specified to connect using Windows Authentication. The JDBC driver supports Integrated
Windows Authentication on Windows operating systems through the
`integratedSecurity` connection string parameter.

To use integrated authentication

1. Install the JDBC driver.
2. Copy the `sqljdbc_auth.dll` file to a directory on the Windows system path on
   the computer where the JDBC driver is installed.

The `sqljdbc_auth.dll` files are installed in the
following location:

<_installation
directory_>\sqljdbc\_<_version_>\<_language_>\auth\

When you try to establish a connection to SQL Server database using Windows
Authentication, you might get this error: This driver is not configured for
integrated authentication. This problem can be solved by performing the following
actions:

- Declare two variables that point to the installed path of your JDBC:

`variable name: SQLJDBC_HOME; variable value: D:\lib\JDBC4.1\enu` (where your sqljdbc4.jar exists);

`variable name: SQLJDBC_AUTH_HOME; variable value:
 D\lib\JDBC4.1\enu\auth\x86` (if you are running 32bit OS) or
`D\lib\JDBC4.1\enu\auth\x64` (if you are running 64bit OS). This is where your
`sqljdbc_auth.dll` is located.

- Copy `sqljdbc_auth.dll` to the folder where your JDK/JRE is running. You
  may copy to lib folder, bin folder, and so on. As an example, you might copy
  to the following folder.

```
[JDK_INSTALLED_PATH]\bin;
[JDK_INSTALLED_PATH]\jre\bin;
[JDK_INSTALLED_PATH]\jre\lib;
[JDK_INSTALLED_PATH]\lib;
```

- Ensure that in your JDBC library folder, you have only the SQLJDBC4.jar file. Remove any other
  sqljdbc\*.jar files from that folder (or copy them to another folder). If you
  are adding the driver as part of your program, ensure that you add only
  SQLJDBC4.jar as the driver to use.
- Copy sqljdbc_auth.dll the file in the folder with your application.

###### Note

If you are running a 32-bit Java Virtual Machine (JVM), use the sqljdbc_auth.dll file in the x86 folder, even if the operating system is the x64 version. If you are running a 64-bit JVM on a x64 processor, use the sqljdbc_auth.dll file in the x64 folder.

When you connect to a SQL Server database, you can choose either
**Windows Authentication** or **SQL Server
Authentication** for the **Authentication**
option.

## Connecting to SQL Server as a source

Use the following procedure to connect to your Microsoft SQL Server source database
with the AWS Schema Conversion Tool.

###### To connect to a Microsoft SQL Server source database

1. In the AWS Schema Conversion Tool, choose **Add source**.
2. Choose **Microsoft SQL Server**, then choose
   **Next**.

The **Add source** dialog box appears. 3. For **Connection name**, enter a name for your database.
AWS SCT displays this name in the tree in the left panel. 4. Use database credentials from AWS Secrets Manager or enter them manually:

    * To use database credentials from Secrets Manager, use the following
     instructions:




    	1. For **AWS Secret**, choose
    	 the name of the secret.
    	2. Choose **Populate** to automatically fill in
    	 all values in the database connection dialog box from Secrets Manager.
    For information about using database credentials from Secrets Manager, see [Configuring AWS Secrets Manager in the AWS Schema Conversion Tool](CHAP_UserInterface.md "CHAP_UserInterface.md").
    * To enter the Microsoft SQL Server source database connection
     information manually, use the following instructions:




    | Parameter | Action |
    | --- | --- |
    | **Server name** | Enter the Domain Name Service (DNS) name or IP address of your<br>source database server.<br>You can connect to your source SQL Server database using an IPv6 address protocol. To do so,<br>make sure that you use square brackets to enter the IP address, as shown in the following<br>example.<br>```<br>[2001:db8:ffff:ffff:ffff:ffff:ffff:fffe]<br>``` |
    | **Server port** | Enter the port used to connect to your source database server. |
    | **Instance name** | Enter the instance name for the SQL Server database. To find the<br>instance name, run the query `SELECT @@servername;` on your<br>SQL Server database. |
    | **Authentication** | Choose the authentication type from **Windows Authentication**<br>and **SQL Server Authentication**. |
    | **User name*<br>• and **Password** | Enter the database credentials to connect to your source database server.<br>AWS SCT uses the password to connect to your source database only when you choose<br>to connect to your database in a project. To guard against exposing the password for<br>your source database, AWS SCT doesn't store the password by default. If you close<br>your AWS SCT project and reopen it, you are prompted for the password to connect<br>to your source database as needed. |
    | **Use SSL** | Choose this option to use Secure Sockets Layer (SSL) to connect to your database.<br>Provide the following additional information, as applicable, on the<br>**SSL*<br>• tab:<br>+ **Trust server certificate**: Select this option<br>to trust the server certificate.<br>+ **Trust store**: The location of a trust store<br>containing certificates. For this location to appear in the<br>**Global settings*<br>• section, make sure to add it. |
    | **Store password** | AWS SCT creates a secure vault to store SSL certificates and database passwords.<br>Enabling this option lets you store the database password and to connect quickly<br>to the database without having to enter the password. |
    | **Sql Server Driver Path** | Enter the path to the driver to use to connect to the source database. For more<br>information, see [Installing JDBC drivers for AWS Schema Conversion Tool](CHAP_Installing.md "CHAP_Installing.md").<br>If you store the driver path in the global project settings, the driver path<br>doesn't appear on the connection dialog box. For more information, see [Storing driver paths in the global settings](CHAP_Installing.md#CHAP_Installing.JDBCDrivers.Settings "CHAP_Installing.md#CHAP_Installing.JDBCDrivers.Settings"). |
    | **Windows Authentication library** | Enter the path to the `sqljdbc_auth.dll` file.<br>By default, this file is installed in the following location:<br>``<installation directory of the JDBC<br>driver>`sqljdbc_`<version>`\`<language>`\auth\` |

5. Choose **Test Connection** to verify
   that AWS SCT can connect to your source database.
6. Choose **Connect** to connect to your source database.
