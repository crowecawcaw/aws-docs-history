# Data control language for Aurora PostgreSQL

This topic provides reference information about user permissions and access control in Amazon Aurora PostgreSQL, comparing it to Microsoft SQL Server. You can understand how Aurora PostgreSQL implements the ANSI standard for data control language commands, including GRANT and REVOKE. The topic explains the various permission levels available in Aurora PostgreSQL, from individual object permissions to schema-wide access.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                           |
| ------------------------------- | ---------------------------------- | ------------------------- | ----------------------------------------- |
| Five star feature compatibility | N/A                                | N/A                       | Similar syntax and similar functionality. |

## SQL Server Usage

The ANSI standard specifies, and most Relational Database Management Systems (RDBMS) use, `GRANT` and `REVOKE` commands to control permissions.

However, SQL Server also provides a `DENY` command to explicitly restrict access to a resource. `DENY` takes precedence over GRANT and is needed to avoid potentially conflicting permissions for users having multiple logins. For example, if a user has DENY for a resource through group membership but GRANT access for a personal login, the user is denied access to that resource.

In SQL Server, you can grant permissions at multiple levels from lower-level objects such as columns to higher-level objects such as servers. Permissions are categorized for specific services and features such as the service broker.

You can use permissions in conjunction with database users and roles. For more information, see [Users and Roles](chap-sql-server-aurora-pg.security.md "chap-sql-server-aurora-pg.security.md").

### Syntax

Simplified syntax for SQL Server DCL commands:

```
GRANT { ALL [ PRIVILEGES ] } | <permission> [ ON <securable> ] TO <principal>

DENY { ALL [ PRIVILEGES ] } | <permission> [ ON <securable> ] TO <principal>

REVOKE [ GRANT OPTION FOR ] {[ ALL [ PRIVILEGES ] ]|<permission>} [ ON <securable> ] { TO | FROM } <principal>
```

For more information, see [Permissions Hierarchy (Database Engine)](https://docs.microsoft.com/en-us/sql/relational-databases/security/permissions-hierarchy-database-engine?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/security/permissions-hierarchy-database-engine?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) supports the ANSI Data Control Language (DCL) commands `GRANT` and `REVOKE`.

Administrators can grant or revoke permissions for individual objects such as a column, a stored function, or a table. You can grant permissions to multiple objects using `ALL % IN SCHEMA`. In the example preceding, `%` can be `TABLES`, `SEQUENCES`, or `FUNCTIONS`.

Use the following command to grant select on all tables in schema to a specific user.

```
GRANT SELECT ON ALL TABLES IN SCHEMA <Schema Name> TO <Role Name>;
```

Aurora PostgreSQL provides a `GRANT` permission option that is similar to SQL Server `WITH GRANT OPTION` clause. This permission grants a user permission to further grant the same permission to other users.

```
GRANT EXECUTE
ON FUNCTION demo.Procedure1
TO UserY
WITH GRANT OPTION;
```

The following table identifies Aurora PostgreSQL privileges.

| Permissions               | Use to                                                                                                                                                                                                                                   |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SELECT`                  | Use to query rows from table.                                                                                                                                                                                                            |
| `INSERT`                  | Use to insert rows into a table.                                                                                                                                                                                                         |
| `UPDATE`                  | Use to update rows in table.                                                                                                                                                                                                             |
| `DELETE`                  | Use to delete rows from table.                                                                                                                                                                                                           |
| `TRUNCATE`                | Use to truncate a table.                                                                                                                                                                                                                 |
| `REFERENCES`              | Use to create a foreign key constraint.                                                                                                                                                                                                  |
| `TRIGGER`                 | Use to create a trigger on the specified table.                                                                                                                                                                                          |
| `CREATE`                  | The purpose of this permission depends on the target object. For more information, see [GRANT](https://www.postgresql.org/docs/13/sql-grant.html "https://www.postgresql.org/docs/13/sql-grant.html") in the _PostgreSQL documentation_. |
| `CONNECT`                 | Use to connect to the specified database.                                                                                                                                                                                                |
| `TEMPORARY` or `TEMP`     | Use to create temporary tables.                                                                                                                                                                                                          |
| `EXECUTE`                 | Use to run a function.                                                                                                                                                                                                                   |
| `USAGE`                   | The purpose of this permission depends on the target object. For more information, see [GRANT](https://www.postgresql.org/docs/13/sql-grant.html "https://www.postgresql.org/docs/13/sql-grant.html") in the _PostgreSQL documentation_. |
| `ALL` or `ALL PRIVILEGES` | Grant all available privileges.                                                                                                                                                                                                          |

### Syntax

```
GRANT { { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER }
  [, ...] | ALL [ PRIVILEGES ] }
  ON { [ TABLE ] table_name [, ...]
    | ALL TABLES IN SCHEMA schema_name [, ...] }
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { { SELECT | INSERT | UPDATE | REFERENCES } ( column_name [, ...] )
  [, ...] | ALL [ PRIVILEGES ] ( column_name [, ...] ) }
  ON [ TABLE ] table_name [, ...]
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { { USAGE | SELECT | UPDATE }
  [, ...] | ALL [ PRIVILEGES ] }
  ON { SEQUENCE sequence_name [, ...]
    | ALL SEQUENCES IN SCHEMA schema_name [, ...] }
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { { CREATE | CONNECT | TEMPORARY | TEMP } [, ...] | ALL [ PRIVILEGES ] }
  ON DATABASE database_name [, ...]
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { USAGE | ALL [ PRIVILEGES ] }
  ON DOMAIN domain_name [, ...]
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { USAGE | ALL [ PRIVILEGES ] }
  ON FOREIGN DATA WRAPPER fdw_name [, ...]
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { USAGE | ALL [ PRIVILEGES ] }
  ON FOREIGN SERVER server_name [, ...]
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { EXECUTE | ALL [ PRIVILEGES ] }
  ON { FUNCTION function_name ( [ [ argmode ] [ arg_name ] arg_type [, ...] ] ) [,...]
    | ALL FUNCTIONS IN SCHEMA schema_name [, ...] }
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { USAGE | ALL [ PRIVILEGES ] }
  ON LANGUAGE lang_name [, ...]
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { { SELECT | UPDATE } [, ...] | ALL [ PRIVILEGES ] }
  ON LARGE OBJECT loid [, ...]
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { { CREATE | USAGE } [, ...] | ALL [ PRIVILEGES ] }
  ON SCHEMA schema_name [, ...]
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { CREATE | ALL [ PRIVILEGES ] }
  ON TABLESPACE tablespace_name [, ...]
  TO role_specification [, ...] [ WITH GRANT OPTION ]

GRANT { USAGE | ALL [ PRIVILEGES ] }
  ON TYPE type_name [, ...]
  TO role_specification [, ...] [ WITH GRANT OPTION ]

where role_specification can be:
  [ GROUP ] role_name
  | PUBLIC
  | CURRENT_USER
  | SESSION_USER

GRANT role_name [, ...] TO role_name [, ...] [ WITH ADMIN OPTION ]
```

### Examples

Grant `SELECT` permission to a user on all tables in the demo database.

```
GRANT SELECT ON ALL TABLES IN SCHEMA emps TO John;
```

Revoke `EXECUTE` permissions from a user on the `EmployeeReport` stored procedure.

```
REVOKE EXECUTE ON FUNCTION EmployeeReport FROM John;
```

For more information, see [GRANT](https://www.postgresql.org/docs/13/sql-grant.html "https://www.postgresql.org/docs/13/sql-grant.html") in the _PostgreSQL documentation_.
