# Users and roles for Aurora PostgreSQL

This topic provides reference information about the security and authentication differences between Microsoft SQL Server and Amazon Aurora PostgreSQL. You can understand how user management, role-based access control, and authentication mechanisms differ between these two database systems. The topic explains the fundamental concepts of users, roles, and permissions in both SQL Server and PostgreSQL, highlighting the key differences in terminology and implementation.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                     |
| -------------------------------- | ---------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------- |
| Three star feature compatibility | N/A                                | N/A                       | Syntax and option differences, similar functionality. There are no users in PostgreSQL, only roles. |

## SQL Server Usage

SQL Server provides two layers of security principals: logins at the server level and users at the database level. Logins are mapped to users in one or more databases. Administrators can grant logins server-level permissions that aren’t mapped to particular databases such as database creator, system administrator, and security administrator.

SQL Server also supports roles for both the server and the database levels. At the database level, administrators can create custom roles in addition to the general purpose built-in roles.

For each database, administrators can create users and associate them with logins. At the database level, the built-in roles include `db_owner`, `db_datareader`, `db_securityadmin`, and others. A database user can belong to one or more roles (users are assigned to the public role by default and can’t be removed). Administrators can grant permissions to roles and then assign individual users to the roles to simplify security management.

Logins are authenticated using either Windows Authentication, which uses the Windows Server Active Directory framework for integrated single sign-on, or SQL authentication, which is managed by the SQL Server service and requires a password, certificate, or asymmetric key for identification. You can create logins that use Windows Authentication for individual users and domain groups.

In previous versions of SQL server, the concepts of user and schema were interchangeable. For backward compatibility, each database has several existing schemas, including a default schema named dbo which is owned by the `db_owner` role. Logins with system administrator privileges are automatically mapped to the dbo user in each database. Typically, you don’t need to migrate these schemas.

### Examples

Create a login.

```
CREATE LOGIN MyLogin WITH PASSWORD = 'MyPassword'
```

Create a database user for `MyLogin`.

```
USE MyDatabase; CREATE USER MyUser FOR LOGIN MyLogin;
```

Assign `MyLogin` to a server role.

```
ALTER SERVER ROLE dbcreator ADD MEMBER 'MyLogin'
```

Assign `MyUser` to the `db_datareader` role.

```
ALTER ROLE db_datareader ADD MEMBER 'MyUser';
```

For more information, see [Database-level roles](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

PostgreSQL supports only roles; there are no users. However, there is a `CREATE USER` command, which is an alias for `CREATE ROLE` that automatically includes the `LOGIN` permission.

Roles are defined at the database cluster level and are valid in all databases in the PostgreSQL cluster.

### Syntax

The following example shows a simplified syntax for `CREATE ROLE` in Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL).

```
CREATE ROLE name [ [ WITH ] option [ ... ] ]

where option can be:

  SUPERUSER | NOSUPERUSER
  | CREATEDB | NOCREATEDB
  | CREATEROLE | NOCREATEROLE
  | INHERIT | NOINHERIT
  | LOGIN | NOLOGIN
  | REPLICATION | NOREPLICATION
  | BYPASSRLS | NOBYPASSRLS
  | CONNECTION LIMIT connlimit
  | [ ENCRYPTED | UNENCRYPTED ] PASSWORD 'password'
  | VALID UNTIL 'timestamp'
  | IN ROLE role_name [, ...]
  | IN GROUP role_name [, ...]
  | ROLE role_name [, ...]
  | ADMIN role_name [, ...]
  | USER role_name [, ...]
  | SYSID uid
```

The `UNENCRYPTED PASSWORD` option was dropped in PostgreSQL 10, the password must be kept encrypted.

### Example

Create a new database role called `hr_role`. Users can use this role to create new databases in the PostgreSQL cluster. Note that this role isn’t able to login to the database and act as a database user. In addition, grant `SELECT`, `INSERT`, and `DELETE` privileges on the `hr.employees` table to the role.

```
CREATE ROLE hr_role;
GRANT SELECT, INSERT,DELETE on hr.employees to hr_role;
```

## Summary

The following table summarizes common security tasks and the differences between SQL Server and Aurora PostgreSQL.

| Task                       | SQL Server                                             | Aurora PostgreSQL                                                    |
| -------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------- |
| View database users        | `SELECT Name FROM sys.sysusers`                        | `SELECT<br>• FROM pg_roles where rolcanlogin = true;`                |
| Create a user and password | `CREATE USER <User Name> WITH PASSWORD = <PassWord>;`  | `CREATE USER <User Name> WITH PASSWORD '<PassWord>';`                |
| Create a role              | `CREATE ROLE <Role Name>`                              | `CREATE ROLE <Role Name>`                                            |
| Change a user’s password   | `ALTER LOGIN <SQL Login> WITH PASSWORD = <PassWord>;`  | `ALTER USER <SQL Login> WITH PASSWORD '<PassWord>';`                 |
| External authentication    | Windows Authentication                                 | N/A                                                                  |
| Add a user to a role       | `ALTER ROLE <Role Name> ADD MEMBER <User Name>`        | `ALTER ROLE <Role Name> SET <property and value>`                    |
| Lock a user                | `ALTER LOGIN <Login Name> DISABLE`                     | `REVOKE CONNECT ON DATABASE <database_name> from <Role Name>;`       |
| Grant `SELECT` on a schema | `GRANT SELECT ON SCHEMA::<Schema Name> to <User Name>` | `GRANT SELECT ON ALL TABLES IN SCHEMA <Schema Name> TO <User Name>;` |

For more information, see [CREATE ROLE](https://www.postgresql.org/docs/13/sql-createrole.html "https://www.postgresql.org/docs/13/sql-createrole.html") in the _PostgreSQL documentation_.
