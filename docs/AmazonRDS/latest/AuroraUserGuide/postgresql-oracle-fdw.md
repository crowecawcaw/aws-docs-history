# Working with Oracle databases by using the oracle_fdw extension

To access an Oracle database from your Aurora PostgreSQL DB cluster
you can install and use the
`oracle_fdw` extension. This extension is a foreign data wrapper for Oracle databases. To learn more about
this extension, see the [oracle_fdw](https://github.com/laurenz/oracle_fdw "https://github.com/laurenz/oracle_fdw")
documentation.

The `oracle_fdw` extension is supported on Aurora PostgreSQL 12.7 (Amazon Aurora release 4.2)
and higher versions.

###### Topics

- [Turning on the oracle_fdw extension](#postgresql-oracle-fdw.enabling "#postgresql-oracle-fdw.enabling")
- [Example: Using a foreign server linked to an Amazon RDS for Oracle database](#postgresql-oracle-fdw.example "#postgresql-oracle-fdw.example")
- [Working with encryption in transit](#postgresql-oracle-fdw.encryption "#postgresql-oracle-fdw.encryption")
- [Understanding the pg_user_mappings view and permissions](#postgresql-oracle-fdw.permissions "#postgresql-oracle-fdw.permissions")

## Turning on the oracle_fdw extension

To use the oracle_fdw extension, perform the following procedure.

###### To turn on the oracle_fdw extension

- Run the following command using an account that has
  `rds_superuser` permissions.

```
CREATE EXTENSION oracle_fdw;
```

## Example: Using a foreign server linked to an Amazon RDS for Oracle database

The following example shows the use of a foreign server linked to an Amazon RDS for Oracle database.

###### To create a foreign server linked to an RDS for Oracle database

1. Note the following on the RDS for Oracle DB instance:
   - Endpoint
   - Port
   - Database name

2. Create a foreign server.

```
`test=>` `CREATE SERVER oradb FOREIGN DATA WRAPPER oracle_fdw OPTIONS (dbserver '//`endpoint`:`port`/`DB_name`');`
`CREATE SERVER`
```

3. Grant usage to a user who doesn't have `rds_superuser`
   privileges, for example `user1`.

```
`test=>` `GRANT USAGE ON FOREIGN SERVER oradb TO user1;`
`GRANT`
```

4. Connect as `user1`, and create a mapping to an Oracle user.

```
`test=>` `CREATE USER MAPPING FOR user1 SERVER oradb OPTIONS (user '`oracleuser'`, password '`mypassword'`);`
`CREATE USER MAPPING`
```

5. Create a foreign table linked to an Oracle table.

```
`test=>` `CREATE FOREIGN TABLE `mytab` (a int) SERVER oradb OPTIONS (table '`MYTABLE'`);`
`CREATE FOREIGN TABLE`
```

6. Query the foreign table.

```
`test=>`  `SELECT * FROM mytab;`
`a
---
1
(1 row)`
```

If the query reports the following error, check your security group and access
control list (ACL) to make sure that both instances can communicate.

```
ERROR: connection for foreign table "mytab" cannot be established
DETAIL: ORA-12170: TNS:Connect timeout occurred
```

## Working with encryption in transit

PostgreSQL-to-Oracle encryption in transit is based on a combination of client and server configuration parameters. For an
example using Oracle 21c, see [About the Values for Negotiating Encryption and Integrity](https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/configuring-network-data-encryption-and-integrity.html#GUID-3A2AF4AA-AE3E-446B-8F64-31C48F27A2B5 "https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/configuring-network-data-encryption-and-integrity.html#GUID-3A2AF4AA-AE3E-446B-8F64-31C48F27A2B5") in the Oracle documentation. The client used for
oracle_fdw on Amazon RDS is configured with `ACCEPTED`, meaning that the encryption depends on the Oracle database
server configuration and it uses Oracle Security Library (libnnz) for encryption.

If your database is on RDS for Oracle, see [Oracle native network encryption](../UserGuide/Appendix.Oracle.Options.md "../UserGuide/Appendix.Oracle.Options.md")
to configure the encryption.

## Understanding the pg_user_mappings view and permissions

The PostgreSQL catalog `pg_user_mapping` stores the mapping from an
Aurora PostgreSQL user to the user on a foreign
data (remote) server. Access to the catalog is restricted, but you use the `pg_user_mappings` view
to see the mappings. In the following, you can find an example that shows how permissions apply with an example
Oracle database, but this information applies more generally to any foreign data wrapper.

In the following output, you can find roles and permissions mapped to three different
example users. Users `rdssu1` and `rdssu2` are members of the
`rds_superuser` role, and `user1` isn't. The example uses the
`psql` metacommand `\du` to list existing roles.

```
`test=>`  `\du`
 `List of roles
 Role name | Attributes | Member of
-----------------+------------------------------------------------------------+-------------------------------------------------------------
 rdssu1 | | {rds_superuser}
 rdssu2 | | {rds_superuser}
 user1 | | {}`
```

All users, including users that have `rds_superuser` privileges, are allowed to view
their own user mappings (`umoptions`) in
the `pg_user_mappings` table. As shown in the following example, when
`rdssu1` tries to obtain all user mappings, an error is raised even though
`rdssu1``rds_superuser` privileges:

```
`test=>` `SELECT * FROM pg_user_mapping;`
`ERROR: permission denied for table pg_user_mapping`
```

Following are some examples.

```
`test=>` `SET SESSION AUTHORIZATION rdssu1;`
`SET`
`test=>` `SELECT * FROM pg_user_mappings;`
 `umid | srvid | srvname | umuser | usename | umoptions
-------+-------+---------+--------+------------+----------------------------------
 16414 | 16411 | oradb | 16412 | user1 |
 16423 | 16411 | oradb | 16421 | rdssu1 | {user=oracleuser,password=mypwd}
 16424 | 16411 | oradb | 16422 | rdssu2 |
 (3 rows)`

`test=>` `SET SESSION AUTHORIZATION rdssu2;`
`SET`
`test=>` `SELECT * FROM pg_user_mappings;`
 `umid | srvid | srvname | umuser | usename | umoptions
-------+-------+---------+--------+------------+----------------------------------
 16414 | 16411 | oradb | 16412 | user1 |
 16423 | 16411 | oradb | 16421 | rdssu1 |
 16424 | 16411 | oradb | 16422 | rdssu2 | {user=oracleuser,password=mypwd}
 (3 rows)`

`test=>` `SET SESSION AUTHORIZATION user1;`
`SET`
`test=>` `SELECT * FROM pg_user_mappings;`
 `umid | srvid | srvname | umuser | usename | umoptions
-------+-------+---------+--------+------------+--------------------------------
 16414 | 16411 | oradb | 16412 | user1 | {user=oracleuser,password=mypwd}
 16423 | 16411 | oradb | 16421 | rdssu1 |
 16424 | 16411 | oradb | 16422 | rdssu2 |
 (3 rows)`
```

Because of implementation differences between `information_schema._pg_user_mappings` and
`pg_catalog.pg_user_mappings`, a manually created `rds_superuser` requires additional permissions
to view passwords in `pg_catalog.pg_user_mappings`.

No additional permissions are required for an `rds_superuser` to view passwords in
`information_schema._pg_user_mappings`.

Users who don't have the `rds_superuser` role can view passwords in `pg_user_mappings` only
under the following conditions:

- The current user is the user being mapped and owns the server or holds the `USAGE` privilege on
  it.
- The current user is the server owner and the mapping is for `PUBLIC`.
