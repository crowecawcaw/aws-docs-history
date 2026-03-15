# Data control language for Aurora MySQL

This topic provides reference information foruser permissions and access control in Amazon Aurora MySQL compared to Microsoft SQL Server. You can understand the similarities and differences in how these database systems manage user privileges, including the types of permissions available, the granularity of access control, and the commands used to grant or revoke permissions.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Four star feature compatibility | No automation                      | N/A                       | Difference.     |

## SQL Server Usage

The ANSI standard specifies, and most Relational Database Management Systems (RDBMS) use `GRANT` and `REVOKE` commands to control permissions.

However, SQL Server also provides a `DENY` command to explicitly restrict access to a resource. `DENY` takes precedence over `GRANT` and is needed to avoid potentially conflicting permissions for users having multiple logins. For example, if a user has `DENY` for a resource through group membership but `GRANT` access for a personal login, the user is denied access to that resource.

SQL Server allows granting permissions at multiple levels from lower-level objects such as columns to higher level objects such as servers. Permissions are categorized for specific services and features such as the service broker.

Permissions are used in conjunction with database users and roles.

For more information, see [Users and Roles](chap-sql-server-aurora-mysql.security.md "chap-sql-server-aurora-mysql.security.md").

### Syntax

The following examples show the simplified syntax for SQL Server DCL commands:

```
GRANT { ALL [ PRIVILEGES ] } | <permission> [ ON <securable> ] TO <principal>
```

```
DENY { ALL [ PRIVILEGES ] } | <permission> [ ON <securable> ] TO <principal>
```

```
REVOKE [ GRANT OPTION FOR ] {[ ALL [ PRIVILEGES ] ]|<permission>} [ ON <securable> ] { TO | FROM } <principal>
```

For more information, see [Permissions Hierarchy (Database Engine)](https://docs.microsoft.com/en-us/sql/relational-databases/security/permissions-hierarchy-database-engine?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/security/permissions-hierarchy-database-engine?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports the ANSI Data Control Language (DCL) commands `GRANT` and `REVOKE`.

Administrators can grant or revoke permissions for individual objects such as a column, a stored function, or a table. Administrators can grant permissions to multiple objects using wildcards.

Only explicitly granted permissions can be revoked. For example, if a user was granted `SELECT` permissions for the entire database using the following command:

```
GRANT SELECT
ON database.*
TO UserX;
```

It isn’t possible to `REVOKE` the permission for a single table. Instead, revoke the `SELECT` permission for all tables using the following command:

```
REVOKE SELECT
ON database.*
FROM UserX;
```

Aurora MySQL provides a `GRANT` permission option, which is very similar to the `WITH GRANT OPTION` clause in SQL Server. This permission gives a user permission to further grant the same permission to other users.

```
GRANT EXECUTE
ON PROCEDURE demo.Procedure1
TO UserY
WITH GRANT OPTION;
```

###### Note

Aurora MySQL users can have resource restrictions associated with their accounts similar to the SQL Server resource governor. For more information, see [Resource Governor](chap-sql-server-aurora-mysql.management.md "chap-sql-server-aurora-mysql.management.md").

The following table identifies Aurora MySQL privileges:

| Permissions               | Use to                                                                                                                |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `ALL [PRIVILEGES]`        | Grant all privileges at the specified access level except `GRANT OPTION` and `PROXY`.                                 |
| `ALTER`                   | Enable use of `ALTER TABLE`. Levels: Global, database, table.                                                         |
| `ALTER ROUTINE`           | Enable stored routines to be altered or dropped. Levels: Global, database, procedure.                                 |
| `CREATE`                  | Enable database and table creation. Levels: Global, database, table.                                                  |
| `CREATE ROUTINE`          | Enable stored routine creation. Levels: Global, database.                                                             |
| `CREATE TEMPORARY TABLES` | Enable the use of `CREATE TEMPORARY TABLE`. Levels: Global, database.                                                 |
| `CREATE USER`             | Enable the use of `CREATE USER`, `DROP USER`, `RENAME USER`, and `REVOKE ALL PRIVILEGES`. Level: Global.              |
| `CREATE VIEW`             | Enable views to be created or altered. Levels: Global, database, table.                                               |
| `DELETE`                  | Enable the use of `DELETE`. Level: Global, database, table.                                                           |
| `DROP`                    | Enable databases, tables, and views to be dropped. Levels: Global, database, table.                                   |
| `EVENT`                   | Enable the use of events for the Event Scheduler. Levels: Global, database.                                           |
| `EXECUTE`                 | Enable the user to run stored routines. Levels: Global, database, table.                                              |
| `GRANT OPTION`            | Enable privileges to be granted to or removed from other accounts. Levels: Global, database, table, procedure, proxy. |
| `INDEX`                   | Enable indexes to be created or dropped. Levels: Global, database, table.                                             |
| `INSERT`                  | Enable the use of `INSERT`. Levels: Global, database, table, column.                                                  |
| `LOCK TABLES`             | Enable the use of `LOCK TABLES` on tables for which you have the `SELECT` privilege. Levels: Global, database.        |
| `PROXY`                   | Enable user proxying. Level: From user to user.                                                                       |
| `REFERENCES`              | Enable foreign key creation. Levels: Global, database, table, column.                                                 |
| `REPLICATION CLIENT`      | Enable the user to determine the location of primary and secondary servers. Level: Global.                            |
| `REPLICATION SLAVE`       | Enable replication replicas to read binary log events from the primary. Level: Global.                                |
| `SELECT`                  | Enable the use of `SELECT`. Levels: Global, database, table, column.                                                  |
| `SHOW DATABASES`          | Enable `SHOW DATABASES` to show all databases. Level: Global.                                                         |
| `SHOW VIEW`               | Enable the use of `SHOW CREATE VIEW`. Levels: Global, database, table.                                                |
| `TRIGGER`                 | Enable trigger operations. Levels: Global, database, table.                                                           |
| `UPDATE`                  | Enable the use of `UPDATE`. Levels: Global, database, table, column.                                                  |

### Syntax

```
GRANT <privilege type>...
ON [object type] <privilege level>
TO <user> ...
```

```
REVOKE <privilege type>...
ON [object type] <privilege level>
FROM <user> ...
```

###### Note

Table, Function, and Procedure object types can be explicitly stated but aren’t mandatory.

### Examples

Attempt to `REVOKE` a partial permission that was granted as a wild card permission.

```
CREATE USER TestUser;
GRANT SELECT
    ON Demo.*
    TO TestUser;
REVOKE SELECT ON Demo.Invoices
    FROM TestUser
```

For the preceding example, the result looks as shown following.

```
SQL ERROR [1147][42000]: There is no such grant defined for user TestUser on host '%'
on table 'Invoices'
```

Grant the `SELECT` permission to a user on all tables in the demo database.

```
GRANT SELECT
ON Demo.*
TO 'user'@'localhost';
```

Revoke `EXECUTE` permissions from a user on the `EmployeeReport` stored procedure.

```
REVOKE EXECUTE
ON Demo.EmployeeReport
FROM 'user'@'localhost';
```

For more information, see [GRANT Statement](https://dev.mysql.com/doc/refman/5.7/en/grant.html "https://dev.mysql.com/doc/refman/5.7/en/grant.html") in the _MySQL documentation_.
