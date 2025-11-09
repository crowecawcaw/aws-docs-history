# Working with MySQL databases by using the mysql_fdw extension

To access a MySQL-compatible database from your Aurora PostgreSQL DB cluster, you can install and
use the `mysql_fdw` extension. This foreign data wrapper lets you
work with RDS for MySQL, Aurora MySQL, MariaDB, and other MySQL-compatible databases.
The connection from Aurora PostgreSQL DB cluster to the MySQL database
is encrypted on a best-effort basis, depending on the client and server configurations. However, you can enforce
encryption if you like. For more information, see [Using encryption in transit with the extension](#postgresql-mysql-fdw.encryption-in-transit "#postgresql-mysql-fdw.encryption-in-transit").

The `mysql_fdw` extension is supported on Amazon Aurora PostgreSQL version 15.4, 14.9, 13.12, 12.16, and higher releases.
It supports selects, inserts, updates, and deletes from an RDS for PostgreSQL DB to tables on a MySQL-compatible database instance.

###### Topics

- [Setting up your Aurora PostgreSQL DB to use the mysql_fdw extension](#postgresql-mysql-fdw.setting-up "#postgresql-mysql-fdw.setting-up")
- [Example: Working with an Aurora MySQL
  database from Aurora PostgreSQL](#postgresql-mysql-fdw.using-mysql_fdw "#postgresql-mysql-fdw.using-mysql_fdw")
- [Using encryption in transit with the extension](#postgresql-mysql-fdw.encryption-in-transit "#postgresql-mysql-fdw.encryption-in-transit")

## Setting up your Aurora PostgreSQL DB to use the mysql_fdw extension

Setting up the `mysql_fdw` extension on your Aurora PostgreSQL DB cluster involves loading the extension
in your DB cluster and then creating the connection point to the MySQL DB instance. For that task, you need to have
the following details about the MySQL DB instance:

- Hostname or endpoint. For an Aurora MySQL DB cluster, you can find the endpoint by
  using the Console. Choose the Connectivity & security tab and look in the "Endpoint and port" section.
- Port number. The default port number for MySQL is 3306.
- Name of the database. The DB identifier.

You also need to provide access on the security group or the access control list (ACL) for the MySQL port, 3306.
Both the Aurora PostgreSQL DB cluster and the Aurora MySQL DB cluster
need access to port 3306. If access isn't configured correctly,
when you try to connect to MySQL-compatible table you see an error message similar to the following:

```
ERROR: failed to connect to MySQL: Can't connect to MySQL server on '`hostname`.`aws-region`.rds.amazonaws.com:3306' (110)
```

In the following procedure, you (as the `rds_superuser` account) create the foreign server. You then grant access to the
foreign server to specific users. These users then create their own mappings to the appropriate MySQL user accounts to work with
the MySQL DB instance.

###### To use mysql_fdw to access a MySQL database server

1. Connect to your PostgreSQL DB instance using an account that has the `rds_superuser` role.
   If you accepted the defaults when you created your Aurora PostgreSQL DB cluster
   , the user name is `postgres`,
   and you can connect using the `psql` command line tool as follows:

```
psql --host=`your-DB-instance`.`aws-region`.rds.amazonaws.com --port=5432 --username=postgres –-password
```

2. Install the `mysql_fdw` extension as follows:

```
`postgres=>` `CREATE EXTENSION mysql_fdw;`
`CREATE EXTENSION`
```

After the extension is installed on your Aurora PostgreSQL DB cluster
, you set up the foreign server that
provides the connection to a MySQL database.

###### To create the foreign server

Perform these tasks on the Aurora PostgreSQL DB cluster
. The steps assume that you're connected as a
user with `rds_superuser` privileges, such as `postgres`.

1. Create a foreign server in the Aurora PostgreSQL DB cluster
   :

```
`postgres=>` `CREATE SERVER `mysql-db` FOREIGN DATA WRAPPER mysql_fdw OPTIONS (host '`db-name.111122223333`.`aws-region`.rds.amazonaws.com', port '3306');`
`CREATE SERVER`
```

2. Grant the appropriate users access to the foreign server. These should be non-administrator users, that is, users without the
   `rds_superuser` role.

```
`postgres=>` `GRANT USAGE ON FOREIGN SERVER `mysql-db` to `user1`;`
`GRANT`
```

PostgreSQL users create and manage their own connections to the MySQL database through the foreign server.

## Example: Working with an Aurora MySQL

database from Aurora PostgreSQL

Suppose that you have a simple table on an Aurora PostgreSQL DB instance
. Your Aurora PostgreSQL
users want to query (`SELECT`), `INSERT`, `UPDATE`,
and `DELETE` items on that table. Assume that the `mysql_fdw`
extension was created on your RDS for PostgreSQL DB instance, as detailed in the preceding
procedure. After you connect to the RDS for PostgreSQL DB instance as a user that
has `rds_superuser` privileges, you can proceed with the following steps.

1. On the Aurora PostgreSQL DB instance, create a foreign server:

```
`test=>` `CREATE SERVER `mysqldb` FOREIGN DATA WRAPPER mysql_fdw OPTIONS (host '`your-DB`.`aws-region`.rds.amazonaws.com', port '3306');`
`CREATE SERVER`
```

2. Grant usage to a user who doesn't have `rds_superuser` permissions, for example, `user1`:

```
`test=>` `GRANT USAGE ON FOREIGN SERVER mysqldb TO user1;`
`GRANT`
```

3. Connect as `user1`, and then create a mapping to the MySQL user:

```
`test=>` `CREATE USER MAPPING FOR `user1` SERVER mysqldb OPTIONS (username '`myuser`', password '`mypassword`');`
`CREATE USER MAPPING`
```

4. Create a foreign table linked to the MySQL table:

```
`test=>` `CREATE FOREIGN TABLE `mytab` (a int, b text) SERVER mysqldb OPTIONS (dbname 'test', table_name '');`
`CREATE FOREIGN TABLE`
```

5. Run a simple query against the foreign table:

```
`test=>` `SELECT * FROM mytab;`
`a | b
---+-------
1 | apple
(1 row)`
```

6. You can add, change, and remove data from the MySQL table. For example:

```
`test=>` `INSERT INTO mytab values (2, 'mango');`
`INSERT 0 1`
```

Run the `SELECT` query again to see the results:

```
`test=>` `SELECT * FROM mytab ORDER BY 1;`
 a |   b
---+-------
1 | apple
2 | mango
(2 rows)
```

## Using encryption in transit with the extension

The connection to MySQL from Aurora PostgreSQL uses encryption in transit (TLS/SSL) by default. However,
the connection falls back to non-encrypted when the client and server configuration differ. You can enforce encryption
for all outgoing connections by specifying the `REQUIRE SSL` option on the RDS for MySQL user accounts.
This same approach also works for MariaDB and Aurora MySQL user accounts.

For MySQL user accounts configured to `REQUIRE SSL`, the connection attempt fails if a secure connection
can't be established.

To enforce encryption for existing MySQL database user accounts, you can use the `ALTER USER`
command. The syntax varies, depending on the MySQL version, as shown in the following table. For more
information, see [ALTER USER](https://dev.mysql.com/doc/refman/8.0/en/alter-user.html "https://dev.mysql.com/doc/refman/8.0/en/alter-user.html") in
_MySQL Reference Manual_.

| MySQL 5.7, MySQL 8.0                   | MySQL 5.6                                             |
| -------------------------------------- | ----------------------------------------------------- |
| `ALTER USER '`user`'@'%' REQUIRE SSL;` | `GRANT USAGE ON *.<br>• to '`user`'@'%' REQUIRE SSL;` |

For more information about the `mysql_fdw` extension, see the
[mysql_fdw](https://github.com/EnterpriseDB/mysql_fdw "https://github.com/EnterpriseDB/mysql_fdw") documentation.
