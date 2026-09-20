

# Using MySQL as a source for AWS SCT
<a name="CHAP_Source.MySQL"></a>

You can use AWS SCT to convert schemas, database code objects, and application code from MySQL to the following targets: 
+ Amazon RDS for PostgreSQL
+ Amazon Aurora PostgreSQL-Compatible Edition
+ Amazon RDS for MySQL

For more information, see the following sections:

**Topics**
+ [Privileges for MySQL as a source database](#CHAP_Source.MySQL.Permissions)
+ [Connecting to MySQL as a source](#CHAP_Source.MySQL.Connecting)
+ [Privileges for PostgreSQL as a target database](#CHAP_Source.MySQL.ConfigurePostgreSQL)

## Privileges for MySQL as a source database
<a name="CHAP_Source.MySQL.Permissions"></a>

The privileges required for MySQL as a source are as follows: 
+ SELECT ON \*.\* 
+ SHOW VIEW ON \*.\* 

## Connecting to MySQL as a source
<a name="CHAP_Source.MySQL.Connecting"></a>

Use the following procedure to connect to your MySQL source database with the AWS Schema Conversion Tool. 

**To connect to a MySQL source database**

1. In the AWS Schema Conversion Tool, choose **Add source**. 

1. Choose **MySQL**, then choose **Next**.

   The **Add source** dialog box appears.

1. For **Connection name**, enter a name for your database. AWS SCT displays this name in the tree in the left panel. 

1. Use database credentials from AWS Secrets Manager or enter them manually:
   + To use database credentials from Secrets Manager, use the following instructions:

     1. For **AWS Secret**, choose the name of the secret.

     1. Choose **Populate** to automatically fill in all values in the database connection dialog box from Secrets Manager.

     For information about using database credentials from Secrets Manager, see [Configuring AWS Secrets Manager in the AWS Schema Conversion Tool](CHAP_UserInterface.SecretsManager.md).
   + To enter the MySQL source database connection information manually, use the following instructions:



<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td><b>Server name</b></td><td>Enter the Domain Name System (DNS) name or IP address of your source database server. <br />You can connect to your source MySQL database using an IPv6 address protocol. To do so, make sure that you use square brackets to enter the IP address, as shown in the following example.<pre>[2001:db8:ffff:ffff:ffff:ffff:ffff:fffe]</pre></td></tr>
  <tr><td><b>Server port</b></td><td>Enter the port used to connect to your source database server. </td></tr>
  <tr><td><b>User name</b> and <b>Password</b></td><td>Enter the database credentials to connect to your source database server. <br />AWS SCT uses the password to connect to your source database only when you choose to connect to your database in a project. To guard against exposing the password for your source database, AWS SCT doesn't store the password by default. If you close your AWS SCT project and reopen it, you are prompted for the password to connect to your source database as needed. </td></tr>
  <tr><td><b>Use SSL</b></td><td>Choose this option to use Secure Sockets Layer (SSL) to connect to your database. Provide the following additional information, as applicable, on the <b>SSL</b> tab: <ul><li> <b>Require SSL</b>: Choose this option to connect to the server only through SSL. <br />If you choose <b>Require SSL</b>, it means that if the server doesn't support SSL, you can't connect to the server. If you don't choose <b>Require SSL</b> and the server doesn't support SSL, you can still connect to the server without using SSL. For more information, see <a href="https://dev.mysql.com/doc/mysql-secure-deployment-guide/5.7/en/secure-deployment-secure-connections.html">Configuring MySQL to Use Secure Connections</a>.  </li><li> <b>Verify server certificate</b>: Select this option to verify the server certificate by using a trust store.  </li><li> <b>Trust store</b>: The location of a trust store containing certificates.  </li></ul></td></tr>
  <tr><td><b>Store password</b></td><td>AWS SCT creates a secure vault to store SSL certificates and database passwords. Enabling this option lets you store the database password and to connect quickly to the database without having to enter the password. </td></tr>
  <tr><td><b>MySql driver path</b></td><td>Enter the path to the driver to use to connect to the source database. For more information, see <a href="CHAP_Installing.JDBCDrivers.md">Installing JDBC drivers for AWS Schema Conversion Tool</a>. <br />If you store the driver path in the global project settings, the driver path doesn't appear on the connection dialog box. For more information, see <a href="CHAP_Installing.JDBCDrivers.md#CHAP_Installing.JDBCDrivers.Settings">Storing driver paths in the global settings</a>. </td></tr>
</tbody>
</table>


1. Choose **Test Connection** to verify that AWS SCT can connect to your source database. 

1. Choose **Connect** to connect to your source database.

## Privileges for PostgreSQL as a target database
<a name="CHAP_Source.MySQL.ConfigurePostgreSQL"></a>

To use PostgreSQL as a target, AWS SCT requires the `CREATE ON DATABASE` privilege. Make sure that you grant this privilege for each target PostgreSQL database.

To use the converted public synonyms, change the database default search path to `"$user", public_synonyms, public`.

You can use the following code example to create a database user and grant the privileges.

```
CREATE ROLE {{user_name}} LOGIN PASSWORD '{{your_password}}';
GRANT CREATE ON DATABASE {{db_name}} TO {{user_name}};
ALTER DATABASE {{db_name}} SET SEARCH_PATH = "$user", public_synonyms, public;
```

In the preceding example, replace {{user\_name}} with the name of your user. Then, replace {{db\_name}} with the name of your target database. Finally, replace {{your\_password}} with a secure password.

In PostgreSQL, only the schema owner or a `superuser` can drop a schema. The owner can drop a schema and all objects that this schema includes even if the owner of the schema doesn't own some of its objects.

When you use different users to convert and apply different schemas to your target database, you can get an error message when AWS SCT can't drop a schema. To avoid this error message, use the `superuser` role. 