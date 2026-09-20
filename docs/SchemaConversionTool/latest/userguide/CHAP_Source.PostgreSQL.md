

# Connecting to PostgreSQL Databases with the AWS Schema Conversion Tool
<a name="CHAP_Source.PostgreSQL"></a>

You can use AWS SCT to convert schemas, database code objects, and application code from PostgreSQL to the following targets: 
+ Amazon RDS for MySQL
+ Amazon Aurora MySQL-Compatible Edition
+ Amazon RDS for PostgreSQL
+ Amazon Aurora PostgreSQL-Compatible Edition

For more information, see the following sections:

**Topics**
+ [Privileges for PostgreSQL as a source database](#CHAP_Source.PostgreSQL.Permissions)
+ [Connecting to PostgreSQL as a source](#CHAP_Source.PostgreSQL.Connecting)
+ [Privileges for MySQL as a target database](#CHAP_Source.PostgreSQL.ConfigureMySQL)

## Privileges for PostgreSQL as a source database
<a name="CHAP_Source.PostgreSQL.Permissions"></a>

The privileges required for PostgreSQL as a source are as follows: 
+ CONNECT ON DATABASE {{<database\_name>}} 
+ USAGE ON SCHEMA {{<database\_name>}} 
+ SELECT ON ALL TABLES IN SCHEMA {{<database\_name>}} 
+ SELECT ON ALL SEQUENCES IN SCHEMA {{<database\_name>}} 

## Connecting to PostgreSQL as a source
<a name="CHAP_Source.PostgreSQL.Connecting"></a>

Use the following procedure to connect to your PostgreSQL source database with the AWS Schema Conversion Tool. 

**To connect to a PostgreSQL source database**

1. In the AWS Schema Conversion Tool, choose **Add source**. 

1. Choose **PostgreSQL**, then choose **Next**.

   The **Add source** dialog box appears.

1. For **Connection name**, enter a name for your database. AWS SCT displays this name in the tree in the left panel. 

1. Use database credentials from AWS Secrets Manager or enter them manually:
   + To use database credentials from Secrets Manager, use the following instructions:

     1. For **AWS Secret**, choose the name of the secret.

     1. Choose **Populate** to automatically fill in all values in the database connection dialog box from Secrets Manager.

     For information about using database credentials from Secrets Manager, see [Configuring AWS Secrets Manager in the AWS Schema Conversion Tool](CHAP_UserInterface.SecretsManager.md).
   + To enter the PostgreSQL source database connection information manually, use the following instructions:



<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><b>Server name</b></td><td>Enter the Domain Name System (DNS) name or IP address of your source database server. <br />You can connect to your source PostgreSQL database using an IPv6 address protocol. To do so, make sure that you use square brackets to enter the IP address, as shown in the following example.<pre>[2001:db8:ffff:ffff:ffff:ffff:ffff:fffe]</pre></td></tr>
  <tr><td><b>Server port</b></td><td>Enter the port used to connect to your source database server. </td></tr>
  <tr><td><b>Database</b></td><td>Enter the name of the PostgreSQL database.</td></tr>
  <tr><td><b>User name</b> and <b>Password</b></td><td>Enter the database credentials to connect to your source database server. <br />AWS SCT uses the password to connect to your source database only when you choose to connect to your database in a project. To guard against exposing the password for your source database, AWS SCT doesn't store the password by default. If you close your AWS SCT project and reopen it, you are prompted for the password to connect to your source database as needed. </td></tr>
  <tr><td><b>Use SSL</b></td><td>Choose this option to use Secure Sockets Layer (SSL) to connect to your database. Provide the following additional information, as applicable, on the <b>SSL</b> tab:<ul><li> <b>Verify server certificate</b>: Select this option to verify the server certificate by using a trust store.  </li><li> <b>Trust store</b>: The location of a trust store containing certificates. For this location to appear in the <b>Global settings</b> section, make sure to add it. </li></ul></td></tr>
  <tr><td><b>Store password</b></td><td>AWS SCT creates a secure vault to store SSL certificates and database passwords. Enabling this option lets you store the database password and to connect quickly to the database without having to enter the password.</td></tr>
  <tr><td><b>PostgreSQL driver path</b></td><td>Enter the path to the driver to use to connect to the source database. For more information, see <a href="CHAP_Installing.JDBCDrivers.md">Installing JDBC drivers for AWS Schema Conversion Tool</a>. <br />If you store the driver path in the global project settings, the driver path doesn't appear on the connection dialog box. For more information, see <a href="CHAP_Installing.JDBCDrivers.md#CHAP_Installing.JDBCDrivers.Settings">Storing driver paths in the global settings</a>. </td></tr>
</tbody>
</table>


1. Choose **Test Connection** to verify that AWS SCT can connect to your source database. 

1. Choose **Connect** to connect to your source database.

## Privileges for MySQL as a target database
<a name="CHAP_Source.PostgreSQL.ConfigureMySQL"></a>

The privileges required for MySQL as a target when you migrate from PostgreSQL are as follows:
+ CREATE ON \*.\*
+ ALTER ON \*.\*
+ DROP ON \*.\*
+ INDEX ON \*.\*
+ REFERENCES ON \*.\*
+ SELECT ON \*.\*
+ CREATE VIEW ON \*.\*
+ SHOW VIEW ON \*.\*
+ TRIGGER ON \*.\*
+ CREATE ROUTINE ON \*.\*
+ ALTER ROUTINE ON \*.\*
+ EXECUTE ON \*.\*
+ INSERT, UPDATE ON AWS\_POSTGRESQL\_EXT.\*
+ INSERT, UPDATE, DELETE ON AWS\_POSTGRESQL\_EXT\_DATA.\*
+ CREATE TEMPORARY TABLES ON AWS\_POSTGRESQL\_EXT\_DATA.\*

You can use the following code example to create a database user and grant the privileges.

```
CREATE USER '{{user_name}}' IDENTIFIED BY '{{your_password}}';
GRANT CREATE ON *.* TO '{{user_name}}';
GRANT ALTER ON *.* TO '{{user_name}}';
GRANT DROP ON *.* TO '{{user_name}}';
GRANT INDEX ON *.* TO '{{user_name}}';
GRANT REFERENCES ON *.* TO '{{user_name}}';
GRANT SELECT ON *.* TO '{{user_name}}';
GRANT CREATE VIEW ON *.* TO '{{user_name}}';
GRANT SHOW VIEW ON *.* TO '{{user_name}}';
GRANT TRIGGER ON *.* TO '{{user_name}}';
GRANT CREATE ROUTINE ON *.* TO '{{user_name}}';
GRANT ALTER ROUTINE ON *.* TO '{{user_name}}';
GRANT EXECUTE ON *.* TO '{{user_name}}';
GRANT INSERT, UPDATE ON AWS_POSTGRESQL_EXT.* TO '{{user_name}}';
GRANT INSERT, UPDATE, DELETE ON AWS_POSTGRESQL_EXT_DATA.* TO '{{user_name}}';
GRANT CREATE TEMPORARY TABLES ON AWS_POSTGRESQL_EXT_DATA.* TO '{{user_name}}';
```

In the preceding example, replace {{user\_name}} with the name of your user. Then, replace {{your\_password}} with a secure password.

To use Amazon RDS for MySQL or Aurora MySQL as a target, set the `lower_case_table_names` parameter to `1`. This value means that the MySQL server handles identifiers of such object names as tables, indexes, triggers, and databases as case insensitive. If you have turned on binary logging in your target instance, then set the `log_bin_trust_function_creators` parameter to `1`. In this case, you don't need to use the `DETERMINISTIC`, `READS SQL DATA` or `NO SQL` characteristics to create stored functions. To configure these parameters, create a new DB parameter group or modify an existing DB parameter group.