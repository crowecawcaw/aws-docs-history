# Connecting to Microsoft Azure SQL Databases with the AWS SCT

You can use AWS SCT to convert schemas, code objects, and application code from
Azure SQL Database to the following targets:

- Amazon RDS for MySQL
- Amazon Aurora MySQL-Compatible Edition
- Amazon RDS for PostgreSQL
- Amazon Aurora PostgreSQL-Compatible Edition

###### Topics

- [Privileges for Azure SQL Database as a source](#CHAP_Source.AzureSQL.Permissions "#CHAP_Source.AzureSQL.Permissions")
- [Connecting to Azure SQL Database as a source](#CHAP_Source.AzureSQL.Connecting "#CHAP_Source.AzureSQL.Connecting")

## Privileges for Azure SQL Database as a source

The privileges required for Azure SQL Database as a source are as follows:

- VIEW DEFINITION
- VIEW DATABASE STATE

Repeat the grant for each database
whose schema you are converting.

The privileges required for target MySQL and PostgreSQL databases
are described in the following sections.

- [Privileges for MySQL as a target database](CHAP_Source.SQLServer.ToMySQL.md#CHAP_Source.SQLServer.ToMySQL.ConfigureTarget "CHAP_Source.SQLServer.ToMySQL.md#CHAP_Source.SQLServer.ToMySQL.ConfigureTarget")
- [Privileges for PostgreSQL as a target database](CHAP_Source.SQLServer.ToPostgreSQL.md#CHAP_Source.SQLServer.ToPostgreSQL.ConfigurePostgreSQL "CHAP_Source.SQLServer.ToPostgreSQL.md#CHAP_Source.SQLServer.ToPostgreSQL.ConfigurePostgreSQL")

## Connecting to Azure SQL Database as a source

Use the following procedure to connect to your Azure SQL Database source
database with the AWS Schema Conversion Tool.

###### To connect to an Azure SQL Database source database

1. In the AWS Schema Conversion Tool,
   choose **Add source**.
2. Choose **Azure SQL Database**, then choose
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
    * To enter the Azure SQL Database source database connection
     information manually, use the following instructions:




    | Parameter | Action |
    | --- | --- |
    | **Server name** | Enter the Domain Name Service (DNS) name or IP address of your source database server. |
    | **Database** | Enter the database name to connect to. |
    | **User name*<br>• and **Password** | Enter the database credentials to connect to your source database server.<br>AWS SCT uses the password to connect to your source database<br>only when you choose to connect to your database in a project.<br>To guard against exposing the password for your source database,<br>AWS SCT doesn't store the password by default. If you close your<br>AWS SCT project and reopen it, you are prompted for the password<br>to connect to your source database as needed. |
    | **Store password** | AWS SCT creates a secure vault to store SSL certificates<br>and database passwords. By turning this option on, you can<br>store the database password and connect quickly to the database<br>without having to enter the password. |

5. Choose **Test Connection** to verify
   that AWS SCT can connect to your source database.
6. Choose **Connect** to connect to your source database.
