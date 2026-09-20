

# Connecting to Oracle Databases with the AWS Schema Conversion Tool
<a name="CHAP_Source.Oracle"></a>

You can use AWS SCT to convert schemas, database code objects, and application code from Oracle Database to the following targets: 
+ Amazon RDS for MySQL
+ Amazon Aurora MySQL-Compatible Edition
+ Amazon RDS for PostgreSQL
+ Amazon Aurora PostgreSQL-Compatible Edition
+ Amazon RDS for Oracle
+ Amazon RDS for MariaDB

When the source is an Oracle database, comments can be converted to the appropriate format in, for example, a PostgreSQL database. AWS SCT can convert comments on tables, views, and columns. Comments can include apostrophes; AWS SCT doubles the apostrophes when converting SQL statements, just as it does for string literals.

For more information, see the following.

**Topics**
+ [Privileges for Oracle as a source](#CHAP_Source.Oracle.Permissions)
+ [Connecting to Oracle as a source](#CHAP_Source.Oracle.Connecting)
+ [Migrating from Oracle to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL with AWS Schema Conversion Tool](CHAP_Source.Oracle.ToPostgreSQL.md)
+ [Migrating from Oracle to Amazon RDS for MySQL or Amazon Aurora MySQL with the AWS Schema Conversion Tool](CHAP_Source.Oracle.ToMySQL.md)
+ [Migrating from Oracle Database to Amazon RDS for Oracle with AWS Schema Conversion Tool](CHAP_Source.Oracle.ToRDSOracle.md)

## Privileges for Oracle as a source
<a name="CHAP_Source.Oracle.Permissions"></a>

The privileges required for Oracle as a source are as follows: 
+ CONNECT 
+ SELECT\_CATALOG\_ROLE 
+ SELECT ANY DICTIONARY 
+ SELECT ON SYS.ARGUMENT$

## Connecting to Oracle as a source
<a name="CHAP_Source.Oracle.Connecting"></a>

Use the following procedure to connect to your Oracle source database with the AWS Schema Conversion Tool. 

**To connect to an Oracle source database**

1. In the AWS Schema Conversion Tool, choose **Add source**. 

1. Choose **Oracle**, then choose **Next**. 

   The **Add source** dialog box appears.

1. For **Connection name**, enter a name for your database. AWS SCT displays this name in the tree in the left panel. 

1. Use database credentials from AWS Secrets Manager or enter them manually:
   + To use database credentials from Secrets Manager, use the following instructions:

     1. For **AWS Secret**, choose the name of the secret.

     1. Choose **Populate** to automatically fill in all values in the database connection dialog box from Secrets Manager.

     For information about using database credentials from Secrets Manager, see [Configuring AWS Secrets Manager in the AWS Schema Conversion Tool](CHAP_UserInterface.SecretsManager.md).
   + To enter the Oracle source database connection information manually, use the following instructions:


<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><b>Type</b></td><td>Choose the connection type to your database. Depending on your type, provide the following additional information: <ul><li><b>SID</b> <ul><li> <b>Server name</b>: The Domain Name System (DNS) name or IP address of your source database server. </li><li> <b>Server port</b>: The port used to connect to your source database server. </li><li><b>Oracle SID</b>: The Oracle System ID (SID). To find the Oracle SID, submit the following query to your Oracle database: <br /><code>SELECT sys_context('userenv','instance_name') AS SID FROM dual;</code> </li></ul> </li><li><b>Service name</b> <ul><li> <b>Server name</b>: The DNS name or IP address of your source database server. <br />You can connect to your source Oracle database using an IPv6 address protocol. To do so, make sure that you use square brackets to enter the IP address, as shown in the following example. <pre>[2001:db8:ffff:ffff:ffff:ffff:ffff:fffe]</pre> </li><li> <b>Server port</b>: The port used to connect to your source database server. </li><li><b>Service name</b>: The name of the Oracle service to connect to.</li></ul> </li><li><b>TNS alias</b> <ul><li><b>TNS file path</b>: The path to the file that contains the Transparent Network Substrate (TNS) name connection information. <br />After you choose the TNS file, AWS SCT adds all Oracle database connections from the file to the <b>TNS alias</b> list. <br />Choose this option to connect to Oracle Real Application Clusters (RAC). </li><li><b>TNS alias</b>: The TNS alias from this file to use to connect to the source database. </li></ul> </li><li><b>TNS connect identifier</b> <ul><li><b>TNS connect identifier</b>: The identifier for the registered TNS connection information.</li></ul> </li></ul></td></tr>
  <tr><td><b>User name</b> and <b>Password</b></td><td>Enter the database credentials to connect to your source database server. <br />The first time you connect to the Oracle database, you enter the path to the Oracle Driver file (ojdbc8.jar). You can download the file at <a href="http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html">http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html</a>. Make sure to register on the free Oracle Technical Network website to complete the download. AWS SCT uses the selected driver for any future Oracle database connections. The driver path can be modified using the <b>Drivers</b> tab in <b>Global Settings</b>.<br />AWS SCT uses the password to connect to your source database only when you choose to connect to your database in a project. To guard against exposing the password for your source database, AWS SCT doesn't store the password by default. If you close your AWS SCT project and reopen it, you are prompted for the password to connect to your source database as needed. </td></tr>
  <tr><td><b>Use SSL</b></td><td>Choose this option to use Secure Sockets Layer (SSL) to connect to your database. Provide the following additional information, as applicable, on the <b>SSL</b> tab: <ul><li> <b>SSL authentication</b>: Select this option to use SSL authentication by certificate Set up your trust store and key store in <b>Settings</b>, <b>Global settings</b>, <b>Security</b>. </li><li> <b>Trust store</b>: The trust store to use. </li><li> <b>Key store</b>: The key store to use. </li></ul></td></tr>
  <tr><td><b>Store password</b></td><td>AWS SCT creates a secure vault to store SSL certificates and database passwords. Choose this option to store the database password and to connect quickly to the database without having to enter the password. </td></tr>
  <tr><td><b>Oracle driver path</b></td><td>Enter the path to the driver to use to connect to the source database. For more information, see <a href="CHAP_Installing.JDBCDrivers.md">Installing JDBC drivers for AWS Schema Conversion Tool</a>. <br />If you store the driver path in the global project settings, the driver path doesn't appear in the connection dialog box. For more information, see <a href="CHAP_Installing.JDBCDrivers.md#CHAP_Installing.JDBCDrivers.Settings">Storing driver paths in the global settings</a>. </td></tr>
</tbody>
</table>


1. Choose **Test Connection** to verify that AWS SCT can connect to your source database. 

1. Choose **Connect** to connect to your source database.