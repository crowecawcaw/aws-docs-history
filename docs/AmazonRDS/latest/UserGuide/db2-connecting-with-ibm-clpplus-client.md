

# Connecting to your Amazon RDS for Db2 DB instance with IBM CLPPlus
<a name="db2-connecting-with-ibm-clpplus-client"></a>

You can use a utility such as IBM CLPPlus to connect to an Amazon RDS for Db2 DB instance. This utility is part of IBM Data Server Runtime Client. To download the client** **from IBM Fix Central, see [IBM Data Server Client Packages Version 11.5 Mod 8 Fix Pack 0](https://www.ibm.com/support/pages/node/6830885) in IBM Support. 

**Important**  
We recommend that you run IBM CLPPlus on an operating system that supports graphical user interfaces such as macOS, Windows, or Linux with Desktop. If running headless Linux, use switch **-nw** with CLPPlus commands.

**Topics**
+ [Installing the client](#db2-connecting-ibm-clpplus-install-client)
+ [Connecting to a DB instance](#db2-connecting-ibm-clpplus-connect-db-instance)
+ [Retrieving CLOB Data from DB2 Stored Procedures](#db2-connecting-ibm-clpplus-retrieve-clob-data)

## Installing the client
<a name="db2-connecting-ibm-clpplus-install-client"></a>

After downloading the package for Linux, install the client. 

**Note**  
To install the client on AIX or Windows, follow the same procedure but modify the commands for your operating system.

**To install the client on Linux**

1. Run **`./db2_install`**.

1. Run **`clientInstallDir/instance/db2icrt -s client` {{instance\_name}}**. Replace {{instance\_name}} with a valid operating system user on Linux. In Linux, the Db2 DB instance name is tied to the operating system username.

   This command creates a **`sqllib`** directory in the home directory of the designated user on Linux.

## Connecting to a DB instance
<a name="db2-connecting-ibm-clpplus-connect-db-instance"></a>

To connect to your RDS for Db2 DB instance, you need its DNS name and port number. For information about finding them, see [Finding the endpoint](db2-finding-instance-endpoint.md). You also need to know the database name, master username, and master password that you defined when you created your RDS for Db2 DB instance. For more information about finding them, see [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating).

**To connect to an RDS for Db2 DB instance with IBM CLPPlus**

1. Review the command syntax. In the following example, replace {{clientDir}} with the location where the client is installed. 

   ```
   cd {{clientDir}}/bin
       ./clpplus -h
   ```

1. Configure your Db2 server. In the following example, replace {{dsn\_name}}, {{database\_name}}, {{endpoint}}, and {{port}} with the DSN name, database name, endpoint, and port for your RDS for Db2 DB instance. For more information, see [Finding the endpoint of your Amazon RDS for Db2 DB instance](db2-finding-instance-endpoint.md).

   ```
   db2cli writecfg add -dsn {{dsn_name}} -database {{database_name}} -host {{endpoint}} -port {{port}} -parameter "Authentication=SERVER_ENCRYPT"
   ```

1. Connect to your RDS for Db2 DB instance. In the following example, replace {{master\_username}} and {{dsn\_name}} with the master username and DSN name.

   ```
   ./clpplus -nw {{master_username}}@{{dsn_name}}
   ```

1. A Java Shell window opens. Enter the master password for your RDS for Db2 DB instance. 
**Note**  
If a Java Shell window doesn't open, run `./clpplus -nw` to use the same command line window.

   ```
   Enter password: {{*********}}
   ```

   A connection is made and produces output similar to the following example:

   ```
   Database Connection Information :
   ---------------------------------
   Hostname = database-1.abcdefghij.us-east-1.rds.amazonaws.com
   Database server = DB2/LINUXX8664  SQL110590
   SQL authorization ID = admin
   Local database alias = DB2DB
   Port = 50000
   ```

1. Run queries and view results. The following example shows a SQL statement that selects the database you created. 

   ```
   SQL > select current server from sysibm.dual;
   ```

   This command produces output similar to the following example:

   ```
   1
       --------------------
       DB2DB
       SQL>
   ```

## Retrieving CLOB Data from DB2 Stored Procedures
<a name="db2-connecting-ibm-clpplus-retrieve-clob-data"></a>

Stored procedures like rdsadmin.db2pd\_command return results in CLOB columns, which support up to 2 GB of data. However, DB2 CLP limits CLOB output to 8 KB (8192 bytes), truncating any data beyond this threshold. To retrieve the complete output, use CLPPLUS instead.

1. Get Task ID (task\_id) 

   ```
   db2 "select task_id, task_type, database_name, lifecycle, varchar(bson_to_json(task_input_params), 500) as task_params,
   cast(task_output as varchar(500)) as task_output, CREATED_AT, LAST_UPDATED_AT from table(rdsadmin.get_task_status(null,null,null))"
   ```

1. Execute CLPPLUS Command

   After obtaining the task\_id, execute the following command from the Unix prompt (replace TASK\_ID with the actual numeric task ID):

   ```
   $ (echo "select task_output from table(rdsadmin.get_task_status({{task_id}},null,null));" ; echo "disconnect;" ; echo "exit;") | clpplus -nw -silent {{masteruser}}/{{MasterUserPassword}}@{{hostname}}:{{port_num}}/rdsadmin
   ```