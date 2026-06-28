# Connecting to SAP Databases with the AWS Schema Conversion Tool

You can use AWS SCT to convert schemas, database code objects, and application code
from SAP (Sybase) Adaptive Server Enterprise (ASE) to the following targets:

- Amazon RDS for MySQL
- Amazon Aurora MySQL-Compatible Edition
- Amazon RDS for MariaDB
- Amazon RDS for PostgreSQL
- Amazon Aurora PostgreSQL-Compatible Edition
  For more information, see the following sections:

###### Topics

- [Privileges for SAP ASE as a source database](#CHAP_Source.SAP.Permissions "#CHAP_Source.SAP.Permissions")
- [Connecting to SAP ASE (Sybase) as a source](#CHAP_Source.SAP.Connecting "#CHAP_Source.SAP.Connecting")
- [Privileges for MySQL as a target database](#CHAP_Source.SAP.ConfigureMySQL "#CHAP_Source.SAP.ConfigureMySQL")
- [SAP ASE to MySQL conversion settings](#CHAP_Source.SAP.MySQLConversionSettings "#CHAP_Source.SAP.MySQLConversionSettings")
- [Privileges for PostgreSQL as a target database](#CHAP_Source.SAP.ConfigurePostgreSQL "#CHAP_Source.SAP.ConfigurePostgreSQL")
- [SAP ASE to PostgreSQL conversion settings](#CHAP_Source.SAP.PostgreSQLConversionSettings "#CHAP_Source.SAP.PostgreSQLConversionSettings")

## Privileges for SAP ASE as a source database

To use an SAP ASE database as a source, you create a database user and grant permissions. To do this,
take the following steps.

###### Create and configure a database user

1. Connect to the source database.
2. Create a database user with the following commands. Provide a password for the new user.

```
USE master
CREATE LOGIN min_privs WITH PASSWORD `<password>`
sp_adduser min_privs
grant select on dbo.spt_values to min_privs
grant select on asehostname to min_privs
```

3. For every database you are going to migrate, grant the following privileges.

```
USE `<database_name>`
sp_adduser min_privs
grant select on dbo.sysusers to min_privs
grant select on dbo.sysobjects to min_privs
grant select on dbo.sysindexes to min_privs
grant select on dbo.syscolumns to min_privs
grant select on dbo.sysreferences to min_privs
grant select on dbo.syscomments to min_privs
grant select on dbo.syspartitions to min_privs
grant select on dbo.syspartitionkeys to min_privs
grant select on dbo.sysconstraints to min_privs
grant select on dbo.systypes to min_privs
grant select on dbo.sysqueryplans to min_privs
```

## Connecting to SAP ASE (Sybase) as a source

Use the following procedure to connect to your SAP ASE source database
with the AWS Schema Conversion Tool.

###### To connect to a SAP ASE source database

1. In the AWS Schema Conversion Tool, choose **Add source**.
2. Choose **SAP ASE**, then choose **Next**.

The **Add source** dialog box appears. 3. For **Connection name**, enter a name for your database.
AWS SCT displays this name in the tree in the left panel. 4. Use database credentials from AWS Secrets Manager or enter them manually:

    * To use database credentials from Secrets Manager, use the following
     instructions:




    	1. For **AWS Secret**, choose
    	 the name of the secret.
    	2. Choose **Populate** to automatically fill in
    	 all values in the database connection dialog box from Secrets Manager.
    For information about using database credentials from Secrets Manager, see [Configuring AWS Secrets Manager in the AWS Schema Conversion Tool](CHAP_UserInterface.SecretsManager.md "CHAP_UserInterface.SecretsManager.md").
    * To enter the SAP ASE source database connection
     information manually, use the following instructions:




    | Parameter | Action |
    | --- | --- |
    | **Server name** | Enter the Domain Name System (DNS) name or IP address of your source database server. |
    | **Server port** | Enter the port used to connect to your source database server. |
    | **Database** | Enter the name of the SAP ASE database. |
    | **User name*<br>• and **Password** | Enter the database credentials to connect to your source database server.<br>NoteAWS SCT uses the password to connect to your source database<br>only when you choose to connect to your database in a project.<br>To guard against exposing the password for your source database,<br>AWS SCT doesn't store the password by default.<br>If you close your AWS SCT project and reopen it, you are prompted<br>for the password to connect to your source database as needed. |
    | **Use SSL** | Choose this option to use Secure Sockets Layer (SSL) to connect to your<br>database. Provide the following additional information, as applicable,<br>on the **SSL*<br>• tab:<br>+ **Verify server certificate**:<br>Select this option to verify the server certificate by using a trust store.<br>+ **Trust store**:<br>The location of a trust store containing certificates. |
    | **Store password** | AWS SCT creates a secure vault to store SSL certificates<br>and database passwords. Enabling this option lets you store<br>the database password and to connect quickly to the database<br>without having to enter the password. |
    | **SAP ASE driver path** | Enter the path to the driver to use to connect to the source database.<br>For more information, see [Installing JDBC drivers for AWS Schema Conversion Tool](CHAP_Installing.JDBCDrivers.md "CHAP_Installing.JDBCDrivers.md").<br>If you store the driver path in the global project settings,<br>the driver path doesn't appear on the connection dialog box.<br>For more information, see<br>[Storing driver paths in the global settings](CHAP_Installing.JDBCDrivers.md#CHAP_Installing.JDBCDrivers.Settings "CHAP_Installing.JDBCDrivers.md#CHAP_Installing.JDBCDrivers.Settings"). |

5. Choose **Test Connection** to verify
that AWS SCT can connect to your source database. 6. Choose **Connect** to connect to your source database.

## Privileges for MySQL as a target database

The privileges required for MySQL as a target are as follows:

- CREATE ON \*.\*
- ALTER ON \*.\*
- DROP ON \*.\*
- INDEX ON \*.\*
- REFERENCES ON \*.\*
- SELECT ON \*.\*
- CREATE VIEW ON \*.\*
- SHOW VIEW ON \*.\*
- TRIGGER ON \*.\*
- CREATE ROUTINE ON \*.\*
- ALTER ROUTINE ON \*.\*
- EXECUTE ON \*.\*
- INSERT, UPDATE ON AWS\_SAPASE\_EXT.\*
- CREATE TEMPORARY TABLES ON AWS\_SAPASE\_EXT.\*

You can use the following code example to create a database user and grant the privileges.

```
CREATE USER '`user_name`' IDENTIFIED BY '`your_password`';
GRANT CREATE ON *.* TO '`user_name`';
GRANT ALTER ON *.* TO '`user_name`';
GRANT DROP ON *.* TO '`user_name`';
GRANT INDEX ON *.* TO '`user_name`';
GRANT REFERENCES ON *.* TO '`user_name`';
GRANT SELECT ON *.* TO '`user_name`';
GRANT CREATE VIEW ON *.* TO '`user_name`';
GRANT SHOW VIEW ON *.* TO '`user_name`';
GRANT TRIGGER ON *.* TO '`user_name`';
GRANT CREATE ROUTINE ON *.* TO '`user_name`';
GRANT ALTER ROUTINE ON *.* TO '`user_name`';
GRANT EXECUTE ON *.* TO '`user_name`';
GRANT INSERT, UPDATE ON AWS_SAPASE_EXT.* TO '`user_name`';
GRANT CREATE TEMPORARY TABLES ON AWS_SAPASE_EXT.* TO '`user_name`';
```

In the preceding example, replace `user_name` with the name of your user.
Then, replace `your_password` with a secure password.

To use Amazon RDS for MySQL or Aurora MySQL as a target, set the `lower_case_table_names` parameter
to `1`. This value means that the MySQL server handles identifiers of such object names as tables,
indexes, triggers, and databases as case insensitive.
If you have turned on binary logging in your target instance, then set the
`log_bin_trust_function_creators` parameter to `1`.
In this case, you don't need to use the `DETERMINISTIC`,
`READS SQL DATA` or `NO SQL` characteristics to create stored functions.
To configure these parameters, create a new DB parameter group or modify an existing DB parameter group.

## SAP ASE to MySQL conversion settings

To edit SAP ASE to MySQL conversion settings, choose **Settings**,
and then choose **Conversion settings**. From the upper list, choose
**SAP ASE**, and then choose **SAP ASE – MySQL**
or **SAP ASE – Amazon Aurora (MySQL compatible)**.
AWS SCT displays all available settings for SAP ASE to PostgreSQL conversion.

SAP ASE to MySQL conversion settings in AWS SCT include options for the
following:

- To limit the number of comments with action items in the converted
  code.

For **Add comments in the converted code for the action items of selected severity and higher**,
choose the severity of action items. AWS SCT adds comments in the converted code
for action items of the selected severity and higher.

For example, to minimize the number of comments in your converted code, choose
**Errors only**. To include comments for all action items in your
converted code, choose **All messages**.

- To use the exact names of the source database objects in the converted code.

By default, AWS SCT converts the names of database objects, variables, and
parameters to lowercase. To keep the original case for these names, select
**Treat source database object names as case sensitive**.
Choose this option if you use case-sensitive object names in your source SAP ASE
database server.

## Privileges for PostgreSQL as a target database

To use PostgreSQL as a target, AWS SCT requires the `CREATE ON DATABASE` privilege.
Make sure that you grant this privilege for each target PostgreSQL database.

To use the converted public synonyms, change the database default search path to
`"$user", public_synonyms, public`.

You can use the following code example to create a database user and grant the privileges.

```
CREATE ROLE `user_name` LOGIN PASSWORD '`your_password`';
GRANT CREATE ON DATABASE `db_name` TO `user_name`;
ALTER DATABASE `db_name` SET SEARCH_PATH = "$user", public_synonyms, public;
```

In the preceding example, replace `user_name` with the name of your user.
Then, replace `db_name` with the name of your target database.
Finally, replace `your_password` with a secure password.

In PostgreSQL, only the schema owner or a `superuser` can drop a schema. The owner can drop a schema
and all objects that this schema includes even if the owner of the schema doesn't own some of its objects.

When you use different users to convert and apply different schemas to your target database,
you can get an error message when AWS SCT can't drop a schema. To avoid this error message,
use the `superuser` role.

## SAP ASE to PostgreSQL conversion settings

To edit SAP ASE to PostgreSQL conversion settings, choose **Settings**,
and then choose **Conversion settings**. From the upper list, choose
**SAP ASE**, and then choose **SAP ASE – PostgreSQL**
or **SAP ASE – Amazon Aurora (PostgreSQL compatible)**.
AWS SCT displays all available settings for SAP ASE to PostgreSQL conversion.

SAP ASE to PostgreSQL conversion settings in AWS SCT include options for the
following:

- To limit the number of comments with action items in the converted
  code.

For **Add comments in the converted code for the action items of selected severity and higher**,
choose the severity of action items. AWS SCT adds comments in the converted code
for action items of the selected severity and higher.

For example, to minimize the number of comments in your converted code, choose
**Errors only**. To include comments for all action items in your
converted code, choose **All messages**.

- To define the template to use for the schema names in the converted code. For
  **Schema name generation template**, choose one of the following options:

  - **<source\_db>** – Uses the SAP ASE database name
    as a schema name in PostgreSQL.
  - **<source\_schema>** – Uses the SAP ASE schema name
    as a schema name in PostgreSQL.
  - **<source\_db>\_<schema>** – Uses a combination
    of the SAP ASE database and schema names as a schema name in PostgreSQL.

- To use the exact names of the source database objects in the converted code.

By default, AWS SCT converts the names of database objects, variables, and
parameters to lowercase. To keep the original case for these names, select
**Treat source database object names as case sensitive**.
Choose this option if you use case-sensitive object names in your source SAP ASE
database server.

For case-sensitive operations, AWS SCT can avoid the conversion of database
object names to lowercase. To do so, select **Avoid casting to lowercase
for case sensitive operations**.

- To allow the use of indexes with the same name in different tables in SAP
  ASE.

In PostgreSQL, all index names that you use in the schema must be unique. To
make sure that AWS SCT generates unique names for all your indexes, select
**Generate unique names for indexes**.
