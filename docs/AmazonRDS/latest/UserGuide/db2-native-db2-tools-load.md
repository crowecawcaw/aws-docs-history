# Importing data from a client machine to Amazon RDS for Db2 with the LOAD command

You can use the `LOAD CLIENT` command to load data from a file on a client
machine to the RDS for Db2 server. Because no SSH connectivity exists to the RDS for Db2
server, you can use the `LOAD CLIENT` command on either your self-managed Db2
server or your Db2 client machine.

###### Important

The `LOAD CLIENT` command method is useful for migrating small tables. If your
network bandwidth between the client and RDS for Db2 is limited, we recommend that you use
a different migration approach. For more information, see the [Using native Db2 tools to migrate data from Db2 to Amazon RDS for Db2](db2-native-db2-tools.md "db2-native-db2-tools.md").

If your data file includes references to large object file names, then the
`LOAD` command won't work because large objects (LOBs) need to reside on
the Db2 server. If you try to load LOBs from the client machine to the RDS for Db2 server,
you will receive an SQL3025N error. Use the [IMPORT command](db2-native-db2-tools-import.md "db2-native-db2-tools-import.md")
instead.

###### To load data to the RDS for Db2 server

1. Log in to your client machine with IBM Db2 Data Management Console. For more information, see [Connecting to your Amazon RDS for Db2 DB instance with IBM Db2 Data Management Console](db2-connecting-with-ibm-data-management-console.md "db2-connecting-with-ibm-data-management-console.md").
2. Catalog the RDS for Db2 database on the client machine.
   1. Catalog the node. In the following example, replace
      `dns_ip_address` and
      `port` with the DNS name or the IP address and
      the port number of the self-managed Db2 database.

   ```
   db2 catalog tcpip node srcnode REMOTE `dns_ip_address` server `port`
   ```

   2. Catalog the database. In the following example, replace
      `source_database_name` and
      `source_database_alias` with the name of the
      self-managed Db2 database and the alias that you want to use for this
      database.

   ```
   db2 catalog database `source_database_name` as `source_database_alias` at node srcnode \
       authentication server_encrypt
   ```

3. Attach to the source database. In the following example, replace
   `source_database_alias`,
   `user_id`, and `user_password`
   with the alias you that created in the previous step and the user ID and password
   for the self-managed Db2 database.

```
db2look -d `source_database_alias` -i `user_id` -w `user_password` -e -l -a -f -wlm \
    -cor -createdb -printdbcfg -o db2look.sql
```

4. Generate the data file by using the `EXPORT` command on your
   self-managed Db2 system. In the following example, replace
   `directory` with the directory on your client
   machine where your data file exists. Replace
   `file_name` and
   `TABLE_NAME` with the name of the data file and
   the name of the table.

```
db2 "export to /`directory`/`file_name`.txt of del modified by coldel\| \
    select * from TPCH.`TABLE_NAME`"
```

5. Connect to your RDS for Db2 database using the master username and master password
   for your RDS for Db2 DB instance. In the following example, replace
   `rds_database_alias`,
   `master_username`, and
   `master_password` with your own information.

```
db2 connect to ``rds_database_alias`` user `master_username` using `master_password`
```

6. Use the `LOAD` command to load data from a file on the client machine
   to the remote RDS for Db2 database. For more information, see [LOAD command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-load "https://www.ibm.com/docs/en/db2/11.5?topic=commands-load") in the IBM Db2 documentation. In the
   following example, replace `directory` with the directory
   on your client machine where your data file exists. Replace
   `file_name` and `TABLE_NAME`
   with the name of the data file and the name of the table.

```
db2 "LOAD CLIENT from /`directory`/`file_name`.txt \
    modified by coldel\| replace into TPCH.`TABLE_NAME` \
    nonrecoverable without prompting"
```

7. Terminate your connection.

```
db2 terminate
```
