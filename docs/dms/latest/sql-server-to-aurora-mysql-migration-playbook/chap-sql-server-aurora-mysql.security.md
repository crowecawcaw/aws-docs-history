# Users and roles for Aurora MySQL

This topic provides reference information comparing security features between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can understand the key differences in user management, authentication methods, and access control between these two database systems.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                  |
| ------------------------------ | ---------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------ |
| Two star feature compatibility | N/A                                | N/A                       | No native role support in the database. Use AWS IAM accounts with the AWS Authentication Plugin. |

## SQL Server Usage

SQL Server provides two layers of security principals: Logins at the server level and Users at the database level. Logins are mapped to users in one or more databases. Administrators can grant logins server-level permissions that aren’t mapped to particular databases such as Database Creator, System Administrator and Security Administrator.

SQL Server also supports Roles for both the server and the database levels. At the database level, administrators can create custom roles in addition to the general purpose built-in roles.

For each database, administrators can create users and associate them with logins. At the database level, the built-in roles include `db_owner`, `db_datareader`, `db_securityadmin`, and others. A database user can belong to one or more roles (users are assigned to the public role by default and can’t be removed). Administrators can grant permissions to roles and then assign individual users to the roles to simplify security management.

Logins are authenticated using either Windows Authentication, which uses the Windows Server Active Directory framework for integrated single sign-on, or SQL authentication, which is managed by the SQL Server service and requires a password, certificate, or asymmetric key for identification. Logins using windows authentication can be created for individual users and domain groups.

In previous versions of SQL server, the concepts of user and schema were interchangeable. For backward compatibility, each database has several existing schemas, including a default schema named dbo which is owned by the `db_owner` role. Logins with system administrator privileges are automatically mapped to the dbo user in each database. Typically, you don’t need to migrate these schemas.

### Examples

The following example creates a login.

```
CREATE LOGIN MyLogin WITH PASSWORD = 'MyPassword'
```

The following example creates a database user for `MyLogin`.

```
USE MyDatabase; CREATE USER MyUser FOR LOGIN MyLogin;
```

The following example assigns `MyLogin` to a server role.

```
ALTER SERVER ROLE dbcreator ADD MEMBER 'MyLogin'
```

The following example assigns `MyUser` to the `db_datareader` role.

```
ALTER ROLE db_datareader ADD MEMBER 'MyUser';
```

For more information, see [Database-level roles](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports only Users; Roles aren’t supported. Database administrators must specify privileges for individual users. Aurora MySQL uses database user accounts to authenticate sessions and authorize access to specific database objects.

###### Note

When granting privileges, you have the option to use wild-card characters for specifying multiple privileges for multiple objects. For more information, see [Data Control Language](chap-sql-server-aurora-mysql.security.md "chap-sql-server-aurora-mysql.security.md").

When using Identity and Access Management (IAM) database authentication, roles are available as part of the IAM framework and can be used for authentication. This authentication method uses tokens in place of passwords. AWS Signature Version 4 generates authentication tokens with a lifetime of 15 minutes. You don’t need to store user credentials in the database because authentication is managed externally. You can use IAM in conjunction with standard database authentication.

###### Note

In Aurora MySQL, a database is equivalent to an SQL Server schema.

The AWS Authentication Plugin works seamlessly with Aurora MySQL instances. Users logged in with AWS IAM accounts use access tokens to authenticate. This mechanism is similar to the SQL Server windows authentication option.

IAM database authentication provides the following benefits:

- Supports roles for simplifying user and access management.
- Provides a single sign on experience that is safer than using MySQL managed passwords.
- Encrypts network traffic to and from the database using Secure Sockets Layer (SSL) protocol.
- Provides centrally managed access to your database resources, alleviating the need to manage access individually for each database instance or database cluster.

###### Note

IAM database authentication limits the number of new connections to 20 connections/second.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL 8 supports roles which are named collections of privileges. Roles can be created and dropped. Roles can have privileges granted to and revoked from them. Roles can be granted to and revoked from user accounts. The active applicable roles for an account can be selected from among those granted to the account and can be changed during sessions for that account. For more information, see [Using Roles](https://dev.mysql.com/doc/refman/8.0/en/roles.html "https://dev.mysql.com/doc/refman/8.0/en/roles.html").

```
CREATE ROLE 'app_developer', 'app_read', 'app_write';
```

###### Note

Amazon RDS for MySQL 8 incorporates the concept of user account categories with system and regular users distinguished according to whether they have the `SYSTEM_USER` privilege. For more information, see [Account Categories](https://dev.mysql.com/doc/refman/8.0/en/account-categories.html "https://dev.mysql.com/doc/refman/8.0/en/account-categories.html").

```
CREATE USER u1 IDENTIFIED BY 'password';

GRANT ALL ON *.* TO u1 WITH GRANT OPTION;

-- GRANT ALL includes SYSTEM_USER, so at this point

-- u1 can manipulate system or regular accounts
```

### Syntax

Simplified syntax for `CREATE USER` in Aurora MySQL:

```
CREATE USER <user> [<authentication options>] [REQUIRE {NONE | <TLS options>] }]
[WITH <resource options> ] [<Password options> | <Lock options>]
```

```
<Authentication option>:
{IDENTIFIED BY 'auth string'|PASSWORD 'hash string'|WITH auth plugin|auth plugin BY
'auth_string'|auth plugin AS 'hash string'}
<TLS options>: {SSL| X509| CIPHER 'cipher'| ISSUER 'issuer'| SUBJECT 'subject'}
<Resource options>: { MAX_QUERIES_PER_HOUR | MAX_UPDATES_PER_HOUR | MAX_CONNECTIONS_
PER_HOUR | MAX_USER_CONNECTIONS count}
<Password options>: {PASSWORD EXPIRE | DEFAULT | NEVER | INTERVAL N DAY}
<Lock options>: {ACCOUNT LOCK | ACCOUNT UNLOCK}
```

###### Note

In Aurora MySQL, you can assign resource limitations to specific users, similar to SQL Server Resource Governor. For more information, see [Resource Governor](chap-sql-server-aurora-mysql.management.md "chap-sql-server-aurora-mysql.management.md").

### Examples

The following example creates a user, forces a password change, and imposes resource limits.

```
CREATE USER 'Dan'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'Dan''sPassword'
WITH MAX_QUERIES_PER_HOUR 500
PASSWORD EXPIRE;
```

The following example creates a user with IAM authentication.

```
CREATE USER LocalUser
IDENTIFIED WITH AWSAuthenticationPlugin AS 'IAMUser';
```

## Summary

The following table summarizes common security tasks and the differences between SQL Server and Aurora MySQL.

| Task                       | SQL Server                                                       | Aurora MySQL                                                  |
| -------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------- |
| View database users        | `<br>SELECT Name FROM sys.sysusers<br>`                          | `<br>SELECT User FROM mysql.user<br>`                         |
| Create a user and password | `<br>CREATE USER <User Name> WITH<br>PASSWORD = <PassWord>;<br>` | `<br>CREATE USER <User Name><br>IDENTIFIED BY <Password><br>` |
| Create a role              | `<br>CREATE ROLE <Role Name><br>`                                | Use AWS IAM Roles                                             |
| Change a user’s password   | `<br>ALTER LOGIN <SQL Login> WITH<br>PASSWORD = <PassWord>;<br>` | `<br>ALTER USER <User Name><br>IDENTIFIED BY <Password><br>`  |
| External authentication    | Windows Authentication                                           | AWS IAM (Identity and Access Management)                      |
| Add a user to a role       | `<br>ALTER ROLE <Role Name> ADD MEMBER <User Name><br>`          | Use AWS IAM Roles                                             |
| Lock a user                | `<br>ALTER LOGIN <Login Name><br>DISABLE<br>`                    | `<br>ALTER User <User Name><br>ACCOUNT LOCK<br>`              |
| Grant SELECT on a schema   | `<br>GRANT SELECT ON SCHEMA::<Schema Name> to <User Name><br>`   | `<br>GRANT SELECT ON <Schema Name>.<br>• TO <User Name><br>`  |

For more information, see [What is IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") and [IAM Identities (users, user groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md").
