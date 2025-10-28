# Importing data from Db2 to Amazon RDS for Db2 with the INSERT command

You can use the `INSERT` command from a self-managed Db2 server to insert your
data into an Amazon RDS for Db2 database. With this migration approach, you use a nickname for the
remote RDS for Db2 DB instance. Your self-managed Db2 database (source) must be able to connect
to the RDS for Db2 database (target).

###### Important

The `INSERT` command method is useful for migrating small tables. If your
network bandwidth between your self-managed Db2 database and RDS for Db2 database is
limited, we recommend that you use a different migration approach. For more information,
see [Using native Db2 tools to migrate data from Db2 to Amazon RDS for Db2](db2-native-db2-tools.md "db2-native-db2-tools.md").

###### To copy data from a self-managed Db2 database to an RDS for Db2 database

1. Catalog the RDS for Db2 DB instance on the self-managed Db2 instance.
   1. Catalog the node. In the following example, replace
      `dns_ip_address` and
      `port` with the DNS name or the IP address and
      the port number of the self-managed Db2 database.

   ```
   db2 catalog tcpip node remnode REMOTE `dns_ip_address` SERVER `port`
   ```

   2. Catalog the database. In the following example, replace
      `rds_database_name` with the name of the
      database on your RDS for Db2 DB instance.

   ```
   db2 catalog database `rds_database_name` as remdb at node remnode \
       authentication server_encrypt
   ```

2. Enable federation on the self-managed Db2 instance. In the following example,
   replace `source_database_name` with the name of your
   database on the self-managed Db2 instance.

```
db2 update dbm cfg using FEDERATED YES `source_database_name`
```

3. Create tables on the RDS for Db2 DB instance.
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

4. Attach to the source database. In the following example, replace
   `source_database_alias`,
   `user_id`, and `user_password`
   with the alias that you created in the previous step and the user ID and password
   for the self-managed Db2 database.

```
db2look -d `source_database_alias` -i `user_id` -w `user_password` -e -l -a -f -wlm \
    -cor -createdb -printdbcfg -o db2look.sql
```

5. Set up federation, and create a nickname for the RDS for Db2 database table on the
   self-managed Db2 instance.
   1. Connect to your local database. In the following example, replace
      `source_database_name` with the name of the
      database on your self-managed Db2 instance.

   ```
   db2 connect to `source_database_name`
   ```

   2. Create a wrapper to access Db2 data sources.

   ```
   db2 create wrapper drda
   ```

   3. Define a data source on a federated database. In the following example,
      replace `admin` and
      `admin_password` with your credentials for your
      self-managed Db2 instance. Replace
      `rds_database_name` with the name of the
      database on your RDS for Db2 DB instance.

   ```
   db2 "create server rdsdb2 type DB2/LUW version '11.5.9.0' \
       wrapper drda authorization "`admin`" password "`admin_password`" \
       options( dbname '`rds_database_name`', node 'remnode')"
   ```

   4. Map the users on the two databases. In the following example, replace
      `master_username` and
      `master_password` with your credentials for
      your RDS for Db2 DB instance.

   ```
   db2 "create user mapping for user server rdsdb2 \
       options (REMOTE_AUTHID '`master_username`', REMOTE_PASSWORD '`master_password`')"
   ```

   5. Verify the connection to the RDS for Db2 server.

   ```
   db2 set passthru rdsdb2
   ```

   6. Create a nickname for the table in the remote RDS for Db2 database. In the
      following example, replace `NICKNAME` and
      `TABLE_NAME` with a nickname for the table and
      the name of the table.

   ```
   db2 create nickname REMOTE.`NICKNAME` for RDSDB2.`TABLE_NAME.`NICKNAME``
   ```

6. Insert data into the table in the remote RDS for Db2 database. Use the nickname in a
   `select` statement on the local table in the self-managed Db2
   instance. In the following example, replace `NICKNAME` and
   `TABLE_NAME` with a nickname for the table and the name
   of the table.

```
db2 "INSERT into REMOTE.`NICKNAME` select * from RDS2DB2.`TABLE_NAME.NICKNAME`"
```
