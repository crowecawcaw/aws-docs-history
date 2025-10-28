# Copying database metadata from Db2 to Amazon RDS for Db2 with db2look

`db2look` is a native Db2 tool that extracts data definition language (DDL)
files, objects, authorizations, configurations, WLM, and database layouts. You can use
`db2look` to copy database metadata from a self-managed Db2 database to an
Amazon RDS for Db2 database. For more information, see [Mimicking databases using
db2look](https://www.ibm.com/docs/en/db2/11.5?topic=tools-db2look "https://www.ibm.com/docs/en/db2/11.5?topic=tools-db2look") in the IBM Db2 documentation.

###### To copy the database metadata

1. Run the `db2look` tool on your self-managed Db2 system to extract the
   DDL file. In the following example, replace `database_name`
   with the name of your Db2 database.

```
db2look -d `database_name` -e -l -a -f -wlm -cor -createdb -printdbcfg -o db2look.sql
```

2. If your client machine has access to the source (self-managed Db2)
   database and the RDS for Db2 DB instance, you can create the
   `db2look.sql` file on the client machine by directly
   attaching to the remote instance. Then catalog the remote self-managed Db2
   instance.
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
      `user_id`, and
      `user_password` with the alias that you created
      in the previous step and the user ID and password for the self-managed Db2
      database.

   ```
   db2look -d `source_database_alias` -i `user_id` -w `user_password` -e -l -a -f -wlm \
       -cor -createdb -printdbcfg -o db2look.sql
   ```

3. If you can't access the remote self-managed Db2 database from the client
   machine, copy the `db2look.sql` file to the client machine.
   Then catalog the RDS for Db2 DB
   instance.
   1. Catalog the node. In the following example, replace
      `dns_ip_address` and
      `port` with the DNS name or the IP address and
      the port number of the RDS for Db2 DB instance.

   ```
   db2 catalog tcpip node remnode REMOTE `dns_ip_address` server `port`
   ```

   2. Catalog the database. In the following example, replace
      `rds_database_name` and
      `rds_database_alias` with the name of the
      RDS for Db2 database and the alias that you want to use for this
      database.

   ```
   db2 catalog database `rds_database_name` as `rds_database_alias` at node remnode \
       authentication server_encrypt
   ```

   3. Catalog the admin database that manages RDS for Db2. You can't use
      this database to store any data.

   ```
   db2 catalog database rdsadmin as rdsadmin at node remnode authentication server_encrypt
   ```

4. Create buffer pools and tablespaces. The administrator doesn't have privileges
   to create buffer pools or tablespaces. However, you can use Amazon RDS stored
   procedures to create them.
   1. Find the names and definitions of the buffer pools and tablespaces in the
      `db2look.sql` file.
   2. Connect to Amazon RDS using the master username and master password for your
      RDS for Db2 DB instance. In the following example, replace
      `master_username` and
      `master_password` with your own
      information.

   ```
   db2 connect to rdsadmin user `master_username` using `master_password`
   ```

   3. Create a buffer pool by calling `rdsadmin.create_bufferpool`.
      For more information, see [rdsadmin.create_bufferpool](db2-sp-managing-buffer-pools.md#db2-sp-create-buffer-pool "db2-sp-managing-buffer-pools.md#db2-sp-create-buffer-pool").

   ```
   db2 "call rdsadmin.create_bufferpool(
       '`database_name`',
       '`buffer_pool_name`',
       `buffer_pool_size`,
       '`immediate`',
       '`automatic`',
       `page_size`,
       `number_block_pages`,
       `block_size`)"
   ```

   4. Create a tablespace by calling `rdsadmin.create_tablespace`.
      For more information, see [rdsadmin.create_tablespace](db2-sp-managing-tablespaces.md#db2-sp-create-tablespace "db2-sp-managing-tablespaces.md#db2-sp-create-tablespace").

   ```
   db2 "call rdsadmin.create_tablespace(
       '`database_name`',
       '`tablespace_name`',
       '`buffer_pool_name`',
       `tablespace_initial_size`,
       `tablespace_increase_size`,
       '`tablespace_type`')"
   ```

   5. Repeat steps c or d for each additional buffer pool or tablespace
      that you want to add.
   6. Terminate your connection.

   ```
   db2 terminate
   ```

5. Create tables and objects.
   1. Connect to your RDS for Db2 database using the master username and master
      password for your RDS for Db2 DB instance. In the following example, replace
      `rds_database_name`,
      `master_username`, and
      `master_password` with your own
      information.

   ```
   db2 connect to `rds_database_name` user `master_username` using `master_password`
   ```

   2. Run the `db2look.sql` file.

   ```
   db2 -tvf db2look.sql
   ```

   3. Terminate your connection.

   ```
   db2 terminate
   ```
