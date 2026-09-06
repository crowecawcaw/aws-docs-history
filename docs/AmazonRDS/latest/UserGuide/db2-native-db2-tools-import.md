

# Importing data from a client machine to Amazon RDS for Db2 with the IMPORT command
<a name="db2-native-db2-tools-import"></a>

You can use the `IMPORT` command from a client machine to import your data into the Amazon RDS for Db2 server. 

**Important**  
The `IMPORT` command method is useful for migrating small tables and tables that include large objects (LOBs). The `IMPORT` command is slower than the `LOAD` utility because of the `INSERT` and `DELETE` logging operations. If your network bandwidth between the client machine and RDS for Db2 is limited, we recommend that you use a different migration approach. For more information, see [Using native Db2 tools to migrate data from Db2 to Amazon RDS for Db2](db2-native-db2-tools.md).

**To import data into the RDS for Db2 server**

1. Log in to your client machine with IBM Db2 Data Management Console. For more information, see [Connecting to your Amazon RDS for Db2 DB instance with IBM Db2 Data Management Console](db2-connecting-with-ibm-data-management-console.md).

1. Catalog the RDS for Db2 database on the client machine.

   1. Catalog the node. In the following example, replace {{dns\_ip\_address}} and {{port}} with the DNS name or the IP address and the port number of the self-managed Db2 database.

      ```
      db2 catalog tcpip node srcnode REMOTE {{dns_ip_address}} server {{port}}
      ```

   1. Catalog the database. In the following example, replace {{source\_database\_name}} and {{source\_database\_alias}} with the name of the self-managed Db2 database and the alias that you want to use for this database.

      ```
      db2 catalog database {{source_database_name}} as {{source_database_alias}} at node srcnode \
          authentication server_encrypt
      ```

1. Attach to the source database. In the following example, replace {{source\_database\_alias}}, {{user\_id}}, and {{user\_password}} with the alias you created in the previous step and the user ID and password for the self-managed Db2 database.

   ```
   db2look -d {{source_database_alias}} -i {{user_id}} -w {{user_password}} -e -l -a -f -wlm \
       -cor -createdb -printdbcfg -o db2look.sql
   ```

1. Generate the data file by using the` EXPORT` command on your self-managed Db2 system. In the following example, replace {{directory}} with the directory on your client machine where your data file exists. Replace {{file\_name}} and {{table\_name}} with the name of the data file and the name of the table. 

   ```
   db2 "export to /{{directory}}/{{file_name}}.txt of del lobs to /{{directory}}/lobs/ \
       modified by coldel\| select * from {{table_name}}"
   ```

1. Connect to your RDS for Db2 database using the master username and master password for your RDS for Db2 DB instance. In the following example, replace {{{{rds\_database\_alias}}}}, {{master\_username,}} and {{master\_password}} with your own information.

   ```
   db2 connect to {{{{rds_database_alias}}}} user {{master_username}} using {{master_password}}
   ```

1. Use the `IMPORT` command to import data from a file on the client machine into the remote RDS for Db2 database. For more information, see [IMPORT command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-import) in the IBM Db2 documentation. In the following example, replace {{directory}} and {{file\_name}} with the directory on your client machine where your data file exists and the name of the data file. Replace {{SCHEMA\_NAME}} and {{TABLE\_NAME}} with the name of your schema and table. 

   ```
   db2 "IMPORT from /{{directory}}/{{file_name}}.tbl OF DEL LOBS FROM /{{directory}}/lobs/ \
       modified by coldel\| replace into {{SCHEMA_NAME}}.{{TABLE_NAME}}"
   ```

1. Terminate your connection.

   ```
   db2 terminate
   ```