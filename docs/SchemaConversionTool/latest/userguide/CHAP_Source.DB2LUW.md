# ConnConnecting to IBM DB2 for Linux, UNIX, and Windows Databases with the AWS Schema Conversion Tool

You can use AWS SCT to convert schemas, code objects in the SQL language, and application code
from IBM Db2 for Linux, Unix, and Windows (Db2 LUW) to the following targets.

- Amazon RDS for MySQL
- Amazon Aurora MySQL-Compatible Edition
- Amazon RDS for PostgreSQL
- Amazon Aurora PostgreSQL-Compatible Edition
- Amazon RDS for MariaDB
  AWS SCT supports as a source Db2 LUW versions 9.1, 9.5, 9.7, 10.1, 10.5, 11.1, and 11.5.

## Privileges for Db2 LUW as a source

The privileges needed to connect to a Db2 LUW database, to check available
privileges and read schema metadata for a source are as follows:

- Privilege needed to establish a connection:

  - CONNECT ON DATABASE

- Privilege needed to run SQL statements:

  - EXECUTE ON PACKAGE NULLID.SYSSH200

- Privileges needed to get instance-level information:

  - EXECUTE ON FUNCTION SYSPROC.ENV_GET_INST_INFO
  - SELECT ON SYSIBMADM.ENV_INST_INFO
  - SELECT ON SYSIBMADM.ENV_SYS_INFO

- Privileges needed to check privileges granted through roles, groups, and
  authorities:

  - EXECUTE ON FUNCTION SYSPROC.AUTH_LIST_AUTHORITIES_FOR_AUTHID
  - EXECUTE ON FUNCTION SYSPROC.AUTH_LIST_GROUPS_FOR_AUTHID
  - EXECUTE ON FUNCTION SYSPROC.AUTH_LIST_ROLES_FOR_AUTHID
  - SELECT ON SYSIBMADM.PRIVILEGES

- Privileges needed on system catalogs and tables:

  - SELECT ON SYSCAT.ATTRIBUTES
  - SELECT ON SYSCAT.CHECKS
  - SELECT ON SYSCAT.COLIDENTATTRIBUTES
  - SELECT ON SYSCAT.COLUMNS
  - SELECT ON SYSCAT.DATAPARTITIONEXPRESSION
  - SELECT ON SYSCAT.DATAPARTITIONS
  - SELECT ON SYSCAT.DATATYPEDEP
  - SELECT ON SYSCAT.DATATYPES
  - SELECT ON SYSCAT.HIERARCHIES
  - SELECT ON SYSCAT.INDEXCOLUSE
  - SELECT ON SYSCAT.INDEXES
  - SELECT ON SYSCAT.INDEXPARTITIONS
  - SELECT ON SYSCAT.KEYCOLUSE
  - SELECT ON SYSCAT.MODULEOBJECTS
  - SELECT ON SYSCAT.MODULES
  - SELECT ON SYSCAT.NICKNAMES
  - SELECT ON SYSCAT.PERIODS
  - SELECT ON SYSCAT.REFERENCES
  - SELECT ON SYSCAT.ROUTINEPARMS
  - SELECT ON SYSCAT.ROUTINES
  - SELECT ON SYSCAT.ROWFIELDS
  - SELECT ON SYSCAT.SCHEMATA
  - SELECT ON SYSCAT.SEQUENCES
  - SELECT ON SYSCAT.TABCONST
  - SELECT ON SYSCAT.TABLES
  - SELECT ON SYSCAT.TRIGGERS
  - SELECT ON SYSCAT.VARIABLEDEP
  - SELECT ON SYSCAT.VARIABLES
  - SELECT ON SYSCAT.VIEWS
  - SELECT ON SYSIBM.SYSDUMMY1

- To run SQL statements, the user account needs a privilege to use at least one of the
  workloads enabled in the database. If none of the workloads are assigned to
  the user, ensure that the default user workload is accessible to the
  user:

  - USAGE ON WORKLOAD SYSDEFAULTUSERWORKLOAD

To run queries, you need to create system temporary tablespaces with page size
8K, 16K, and 32K, if they don't exist. To create the temporary tablespaces, run the
following scripts.

```
CREATE BUFFERPOOL BP8K
  IMMEDIATE
  ALL DBPARTITIONNUMS
  SIZE AUTOMATIC
  NUMBLOCKPAGES 0
  PAGESIZE 8K;

CREATE SYSTEM TEMPORARY TABLESPACE TS_SYS_TEMP_8K
  PAGESIZE 8192
  BUFFERPOOL BP8K;

CREATE BUFFERPOOL BP16K
  IMMEDIATE
  ALL DBPARTITIONNUMS
  SIZE AUTOMATIC
  NUMBLOCKPAGES 0
  PAGESIZE 16K;

CREATE SYSTEM TEMPORARY TABLESPACE TS_SYS_TEMP_BP16K
  PAGESIZE 16384
  BUFFERPOOL BP16K;

CREATE BUFFERPOOL BP32K
  IMMEDIATE
  ALL DBPARTITIONNUMS
  SIZE AUTOMATIC
  NUMBLOCKPAGES 0
  PAGESIZE 32K;

CREATE SYSTEM TEMPORARY TABLESPACE TS_SYS_TEMP_BP32K
  PAGESIZE 32768
  BUFFERPOOL BP32K;
```

## Connecting to Db2 LUW as a source

Use the following procedure to connect to your Db2 LUW source database with the
AWS Schema Conversion Tool.

###### To connect to a Db2 LUW source database

1. In the AWS Schema Conversion Tool, choose **Add source**.
2. Choose **Db2 LUW**, then choose
   **Next**.

The **Add source** dialog box appears. 3. For **Connection name**, enter a name for your database.
AWS SCT displays this name in the tree in the left panel. 4. Use database credentials from AWS Secrets Manager or enter them manually:

    * To use database credentials from Secrets Manager, use the following
     instructions:




    	1. For **AWS Secret**, choose
    	 the name of the secret.
    	2. Choose **Populate** to automatically fill in
    	 all values in the database connection dialog box from Secrets Manager.
    For information about using database credentials from Secrets Manager, see [Configuring AWS Secrets Manager in the AWS Schema Conversion Tool](CHAP_UserInterface.SecretsManager.md "CHAP_UserInterface.SecretsManager.md").
    * To enter the IBM Db2 LUW source database connection
     information manually, use the following instructions:




    | Parameter | Action |
    | --- | --- |
    | **Server name** | Enter the Domain Name System (DNS) name or IP address of your source database server. |
    | **Server port** | Enter the port used to connect to your source database server. |
    | **Database** | Enter the name of the Db2 LUW database. |
    | **User name*<br>• and **Password** | Enter the database credentials to connect to your source database server.<br>AWS SCT uses the password to connect to your source database only when<br>you choose to connect to your database in a project. To guard against<br>exposing the password for your source database, AWS SCT doesn't store<br>the password by default. If you close your AWS SCT project and reopen it,<br>you are prompted for the password to connect to your source database as needed. |
    | **Use SSL** | Choose this option if you want to use Secure Sockets Layer (SSL) to connect<br>to your database. Provide the following additional information, as applicable,<br>on the **SSL*<br>• tab:<br>+ **Trust store**: The location of a trust store<br>containing certificates. For this location to appear here, make sure<br>to add it in **Global settings**. |
    | **Store password** | AWS SCT creates a secure vault to store SSL certificates and database passwords.<br>By turning this option on, you can store the database password and connect quickly<br>to the database without having to enter the password. |
    | **Db2 LUW driver path** | Enter the path to the driver to use to connect to the source database.<br>For more information, see [Installing JDBC drivers for AWS Schema Conversion Tool](CHAP_Installing.JDBCDrivers.md "CHAP_Installing.JDBCDrivers.md").<br>If you store the driver path in the global project settings, the driver path<br>doesn't appear on the connection dialog box. For more information, see [Storing driver paths in the global settings](CHAP_Installing.JDBCDrivers.md#CHAP_Installing.JDBCDrivers.Settings "CHAP_Installing.JDBCDrivers.md#CHAP_Installing.JDBCDrivers.Settings"). |

5. Choose **Test Connection** to verify
   that AWS SCT can connect to your source database.
6. Choose **Connect** to connect to your source database.
