# Connecting to Apache Cassandra databases with the AWS Schema Conversion Tool

You can use AWS SCT to convert keyspaces from
Apache Cassandra to Amazon DynamoDB.

## Connecting to Apache Cassandra

as a source

Use the following procedure to connect to your Apache Cassandra source
database with the AWS Schema Conversion Tool.

###### To connect to an Apache Cassandra source database

1. In the AWS Schema Conversion Tool,
   choose **Add source**.
2. Choose **Cassandra**, then choose **Next**.

The **Add source** dialog box appears. 3. For **Connection name**, enter a name for your database.
AWS SCT displays this name in the tree in the left panel. 4. Use database credentials from AWS Secrets Manager or enter them manually:

    * To use database credentials from Secrets Manager, use the following
     instructions:




    	1. For **AWS Secret**, choose
    	 the name of the secret.
    	2. Choose **Populate** to automatically fill in
    	 all values in the database connection dialog box from Secrets Manager.
    For information about using database credentials from Secrets Manager, see [Configuring AWS Secrets Manager in the AWS Schema Conversion Tool](CHAP_UserInterface.md "CHAP_UserInterface.md").
    * To enter the Apache Cassandra source database connection
     information manually, use the following instructions:




    | Parameter | Action |
    | --- | --- |
    | **Server name** | Enter the Domain Name Service (DNS) name or IP address of your source database server. |
    | **Server port** | Enter the port used to connect to your source database server. |
    | **User name*<br>• and **Password** | Enter the database credentials to connect to your source database server.<br>AWS SCT uses the password to connect to your source database<br>only when you choose to connect to your database in a project.<br>To guard against exposing the password for your source database,<br>AWS SCT doesn't store the password by default.<br>If you close your AWS SCT project and reopen it,<br>you are prompted for the password to connect to your source database as needed. |
    | **Use SSL** | Choose this option if you want to use Secure Sockets Layer (SSL) to connect<br>to your database. Provide the following additional information, as applicable,<br>on the **SSL*<br>• tab:<br>+ **Trust store**:<br>The trust store to use.<br>+ **Key store**:<br>The key store to use. |
    | **Store password** | AWS SCT creates a secure vault to store SSL certificates and database passwords.<br>By turning this option on, you can store the database password and connect quickly<br>to the database without having to enter the password. |

5. Choose **Test Connection** to verify
   that AWS SCT can connect to your source database.
6. Choose **Connect** to connect to your source database.
