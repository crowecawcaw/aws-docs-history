# Role-based privilege model for RDS for MySQL

Starting with RDS for MySQL version 8.0.36, you can't modify the tables in the
`mysql` database directly. In particular, you can't create database users
by performing data manipulation language (DML) operations on the `grant`
tables. Instead, you use MySQL account-management statements such as `CREATE
 USER`, `GRANT`, and `REVOKE` to grant role-based
privileges to users. You also can't create other kinds of objects such as stored
procedures in the `mysql` database. You can still query the
`mysql` tables. If you use binary log replication, changes made directly
to the `mysql` tables on the source DB instance aren't replicated to the
target cluster.

In some cases, your application might use shortcuts to create users or other objects by inserting into the
`mysql` tables. If so, change your application code to use the corresponding statements such as `CREATE
 USER`.

To export metadata for database users during the migration from an external MySQL
database, use one of the following methods:

- Use MySQL Shell's instance dump utility with a filter to exclude users, roles, and grants. The following example shows you the command syntax to use. Make sure that
  `outputUrl` is empty.

```
mysqlsh user@host -- util.dumpInstance(outputUrl,{excludeSchemas:['mysql'],users: true})
```

For more information, see [Instance Dump Utility, Schema Dump Utility, and Table Dump Utility](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-utilities-dump-instance-schema.html "https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-utilities-dump-instance-schema.html") in the MySQL Reference Manual.

- Use the `mysqlpump` client utility. This example includes all tables except for tables in the `mysql` system database.
  It also includes `CREATE USER` and `GRANT` statements to reproduce all MySQL users in the migrated database.

```
mysqlpump --exclude-databases=mysql --users
```

The `mysqlpump` client utility is no longer available with MySQL
8.4. Instead, use `mysqldump`.
To simplify managing permissions for many users or applications, you can use the
`CREATE ROLE` statement to create a role that has a set of
permissions. Then you can use the `GRANT` and `SET ROLE`
statements and the `current_role` function to assign roles to users or
applications, switch the current role, and check which roles are in effect. For more
information on the role-based permission system in MySQL 8.0, see [Using Roles](https://dev.mysql.com/doc/refman/8.0/en/roles.html "https://dev.mysql.com/doc/refman/8.0/en/roles.html") in
the MySQL Reference Manual.

###### Important

We strongly recommend that you do not use the master user directly in your applications. Instead, adhere to the best
practice of using a database user created with the minimal privileges required for your application.

Starting with version 8.0.36, RDS for MySQL includes a special role that has all of the
following privileges. This role is named `rds_superuser_role`. The primary
administrative user for each DB instance already has this role granted. The
`rds_superuser_role` role includes the following privileges for all
database objects:

- `ALTER`
- `APPLICATION_PASSWORD_ADMIN`
- `ALTER ROUTINE`
- `CREATE`
- `CREATE ROLE`
- `CREATE ROUTINE`
- `CREATE TEMPORARY TABLES`
- `CREATE USER`
- `CREATE VIEW`
- `DELETE`
- `DROP`
- `DROP ROLE`
- `EVENT`
- `EXECUTE`
- `INDEX`
- `INSERT`
- `LOCK TABLES`
- `PROCESS`
- `REFERENCES`
- `RELOAD`
- `REPLICATION CLIENT`
- `REPLICATION SLAVE`
- `ROLE_ADMIN`
- `SET_USER_ID`
- `SELECT`
- `SHOW DATABASES`
- `SHOW VIEW`
- `TRIGGER`
- `UPDATE`
- `XA_RECOVER_ADMIN`
  The role definition also includes `WITH GRANT OPTION` so that an
  administrative user can grant that role to other users. In particular, the administrator
  must grant any privileges needed to perform binary log replication with the MySQL
  cluster as the target.

###### Tip

To see the full details of the permissions, use the following statement.

```
SHOW GRANTS FOR rds_superuser_role@'%';
```

When you grant access by using roles in RDS for MySQL version 8.0.36 and higher, you also activate the role by using the `SET ROLE
 `role_name``or`SET ROLE ALL`statement. The following example shows how.
 Substitute the appropriate role name for`CUSTOM_ROLE`.

```
# Grant role to user
`mysql>` GRANT CUSTOM_ROLE TO '`user`'@'`domain-or-ip-address`'

# Check the current roles for your user. In this case, the CUSTOM_ROLE role has not been activated.
# Only the rds_superuser_role is currently in effect.
`mysql>` SELECT CURRENT_ROLE();
`+--------------------------+
| CURRENT_ROLE() |
+--------------------------+
| `rds_superuser_role`@`%` |
+--------------------------+
1 row in set (0.00 sec)`

# Activate all roles associated with this user using SET ROLE.
# You can activate specific roles or all roles.
# In this case, the user only has 2 roles, so we specify ALL.
`mysql>` SET ROLE ALL;
`Query OK, 0 rows affected (0.00 sec)`

# Verify role is now active
`mysql>` SELECT CURRENT_ROLE();
`+--------------------------------------------------+
| CURRENT_ROLE() |
+--------------------------------------------------+
| `CUSTOM_ROLE`@`%`,`rds_superuser_role`@`%` |
+--------------------------------------------------+`

```
