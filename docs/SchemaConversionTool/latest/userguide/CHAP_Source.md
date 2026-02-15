# Connecting to Oracle Databases with the AWS Schema Conversion Tool

You can use AWS SCT to convert schemas, database code objects, and application code from Oracle Database to the following targets:

- Amazon RDS for MySQL
- Amazon Aurora MySQL-Compatible Edition
- Amazon RDS for PostgreSQL
- Amazon Aurora PostgreSQL-Compatible Edition
- Amazon RDS for Oracle
- Amazon RDS for MariaDB
  When the source is an Oracle database, comments can be converted to the
  appropriate format in, for example, a PostgreSQL database. AWS SCT can convert comments on
  tables, views, and columns. Comments can include apostrophes; AWS SCT doubles the apostrophes
  when converting SQL statements, just as it does for string literals.

For more information, see the following.

###### Topics

- [Privileges for Oracle as a source](#CHAP_Source.Oracle.Permissions "#CHAP_Source.Oracle.Permissions")
- [Connecting to Oracle as a source](#CHAP_Source.Oracle.Connecting "#CHAP_Source.Oracle.Connecting")
- [Migrating from Oracle to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL with AWS Schema Conversion Tool](CHAP_Source.Oracle.md "CHAP_Source.Oracle.md")
- [Migrating from Oracle to Amazon RDS for MySQL or Amazon Aurora MySQL with the AWS Schema Conversion Tool](CHAP_Source.Oracle.md "CHAP_Source.Oracle.md")
- [Migrating from Oracle Database to Amazon RDS for Oracle with AWS Schema Conversion Tool](CHAP_Source.Oracle.md "CHAP_Source.Oracle.md")

##

Privileges for Oracle as a source

The privileges required for Oracle as a source
are as follows:

- CONNECT
- SELECT_CATALOG_ROLE
- SELECT ANY DICTIONARY
- SELECT ON SYS.ARGUMENT$

## Connecting to Oracle as a source

Use the following procedure to connect to your Oracle source database
with the AWS Schema Conversion Tool.

###### To connect to an Oracle source database

1. In the AWS Schema Conversion Tool,
   choose **Add source**.
2. Choose **Oracle**, then choose **Next**.

The **Add source** dialog box appears. 3. For **Connection name**, enter a name for your database.
AWS SCT displays this name in the tree in the left panel. 4. Use database credentials from AWS Secrets Manager or enter them manually:

    * To use database credentials from Secrets Manager, use the following
     instructions:




    	1. For **AWS Secret**, choose
    	 the name of the secret.
    	2. Choose **Populate** to automatically fill in
    	 all values in the database connection dialog box from Secrets Manager.
    For information about using database credentials from Secrets Manager, see [Configuring AWS Secrets Manager in the AWS Schema Conversion Tool](CHAP_UserInterface.md "CHAP_UserInterface.md").
    * To enter the Oracle source database connection
     information manually, use the following instructions:




    | Parameter | Action |
    | --- | --- |
    | **Type** | Choose the connection type to your database.<br>Depending on your type, provide the following additional information:<br>+ **SID**<br>• **Server name**: The Domain Name System (DNS) name or IP address of your<br>source database server.<br>• **Server port**: The port used to connect to your<br>source database server.<br>• **Oracle SID**: The Oracle System ID (SID).<br>To find the Oracle SID, submit the following query to your Oracle database:<br>`SELECT sys_context('userenv','instance_name') AS SID FROM dual;`<br>+ **Service name**<br>• **Server name**: The DNS name or IP address of your<br>source database server.<br>You can connect to your source Oracle database using an IPv6 address protocol. To do so,<br>make sure that you use square brackets to enter the IP address, as shown in the following<br>example.<br>```<br>[2001:db8:ffff:ffff:ffff:ffff:ffff:fffe]<br>```<br>• **Server port**: The port used to connect to your<br>source database server.<br>• **Service name**: The name of the Oracle service<br>to connect to.<br>+ **TNS alias**<br>• **TNS file path**: The path to the<br>file that contains the Transparent Network<br>Substrate (TNS) name connection information.<br>After you choose the TNS file, AWS SCT adds all Oracle database<br>connections from the file to the **TNS alias*<br>• list.<br>Choose this option to connect to Oracle Real Application Clusters (RAC).<br>• **TNS alias**: The TNS alias from this file<br>to use to connect to the source database.<br>+ **TNS connect identifier**<br>• **TNS connect identifier**: The identifier for the<br>registered TNS connection information. |
    | **User name*<br>• and **Password** | Enter the database credentials to connect to your<br>source database server.<br>The first time you connect to the Oracle database, you enter the path to<br>the Oracle Driver file (ojdbc8.jar). You can download the file at [http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html](http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html "http://www.oracle.com/technetwork/database/features/jdbc/index-091264.html").<br>Make sure to register on the free Oracle Technical Network website to complete<br>the download. AWS SCT uses the selected driver for any future Oracle database<br>connections. The driver path can be modified using the **Drivers*<br>• tab<br>in **Global Settings**.<br>AWS SCT uses the password to connect to your source database<br>only when you choose to connect to your database in a project.<br>To guard against exposing the password for your source database,<br>AWS SCT doesn't store the password by default.<br>If you close your AWS SCT project and reopen it,<br>you are prompted for the password to connect to your source database as needed. |
    | **Use SSL** | Choose this option to use Secure Sockets Layer (SSL) to connect<br>to your database. Provide the following additional information,<br>as applicable, on the **SSL*<br>• tab:<br>+ **SSL authentication**: Select this option<br>to use SSL authentication by certificate Set up your trust store and key<br>store in **Settings**, **Global settings**,<br>**Security**.<br>+ **Trust store**: The trust store to use.<br>+ **Key store**: The key store to use. |
    | **Store password** | AWS SCT creates a secure vault to store SSL certificates and database passwords.<br>Choose this option to store the database password and to connect quickly to the<br>database without having to enter the password. |
    | **Oracle driver path** | Enter the path to the driver to use to connect to the source database.<br>For more information,<br>see [Installing JDBC drivers for AWS Schema Conversion Tool](CHAP_Installing.md "CHAP_Installing.md").<br>If you store the driver path in the global project settings, the driver path<br>doesn't appear in the connection dialog box. For more information, see [Storing driver paths in the global settings](CHAP_Installing.md#CHAP_Installing.JDBCDrivers.Settings "CHAP_Installing.md#CHAP_Installing.JDBCDrivers.Settings"). |

5. Choose **Test Connection** to verify
   that AWS SCT can connect to your source database.
6. Choose **Connect** to connect to your source database.
