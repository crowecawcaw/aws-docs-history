# Oracle roles and MySQL privileges

With AWS DMS, you can manage access control and security for your databases during migration. Oracle roles and MySQL privileges define permissions and access levels for database users, allowing you to restrict or grant specific operations and data access.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                               |
| -------------------------------- | ---------------------------------- | ------------------------- | --------------------------------------------- |
| Three star feature compatibility | N/A                                | N/A                       | There are no roles in MySQL, only privileges. |

## Oracle usage

Oracle roles are groups of privileges granted to database users. A database role can contain individual system and object permissions as well as other roles. Database roles enable you to grant multiple database privileges to users in one operation. It is convenient to group permissions together to ease the management of privileges.

Oracle 12c introduces a new multi-tenant database architecture that supports the creation of common and local roles:

- **Common** — Roles created at the container database (CDB) level. A common role is a database role that exists in the root and in every existing and future pluggable database (PDB). Common roles are useful for cross-container operations such as ensuring a common user has a role in every container.
- **Local** — Roles created in a specific pluggable database (PDB). A local role exists only in a single pluggable database and can only contain roles and privileges that apply within the pluggable database in which the role exists.

Common role names must start with a `c##` prefix. Starting from Oracle 12.1.0.2, you can change these prefixes using the `COMMON_USER_PREFIX` parameter.

A `CONTAINER` clause can be added to `CREATE ROLE` statement to choose the container applicable for the role.

### Examples

Create a common role.

```
show con_name

CON_NAME
CDB$ROOT

CREATE ROLE c##common_role;

Role created.
```

Create a local role.

```
show con_name

CON_NAME
ORCLPDB

CREATE ROLE local_role;

Role created.
```

Grant privileges and roles to the `local_role` database role.

```
GRANT RESOURCE, ALTER SYSTEM, SELECT ANY DICTIONARY TO local_role;
```

Database users to which the `local_role` role is granted now have all privileges that were granted to the role.

Revoke privileges and roles from the `local_role` database role.

```
REVOKE RESOURCE, ALTER SYSTEM, SELECT ANY DICTIONARY FROM local_role;
```

For more information, see [Overview of PL/SQL](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview.html") in the _Oracle documentation_.

## MySQL usage

Currently in MySQL 5.7, there is no ROLE feature. You must specify required privileges. However, there is an option when granting privileges to use wild-card characters to specify multiple privileges on one or more objects.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL version 8 supports roles which are named collections of privileges. Roles can be created and dropped. Roles can have privileges granted to and revoked from them. Roles can be granted to and revoked from user accounts. The active applicable roles for an account can be selected from among those granted to the account and can be changed during sessions for that account.

For more information, see [Using Roles](https://dev.mysql.com/doc/refman/8.0/en/roles.html "https://dev.mysql.com/doc/refman/8.0/en/roles.html") in the _MySQL documentation_.

```
CREATE ROLE 'app_developer', 'app_read', 'app_write';
```

###### Note

Amazon RDS for MySQL version 8 incorporates the concept of user account categories with system and regular users distinguished according to whether they have the `SYSTEM_USER` privilege. For more information, see [Account Categories](https://dev.mysql.com/doc/refman/8.0/en/account-categories.html "https://dev.mysql.com/doc/refman/8.0/en/account-categories.html") in the _MySQL documentation_.

```
CREATE USER u1 IDENTIFIED BY 'password';

GRANT ALL ON *.* TO u1 WITH GRANT OPTION;

-- GRANT ALL includes SYSTEM_USER, so at this point

-- u1 can manipulate system or regular accounts
```

### Examples

Grant privileges using a wild-card.

```
GRANT ALL ON test_db.* to 'testuser';
GRANT CREATE USER on *.* to 'testuser';
GRANT SELECT ON db2.* TO 'testuser';
GRANT EXECUTE ON PROCEDURE mydb.myproc TO
```

For more information, see [GRANT Statement](https://dev.mysql.com/doc/refman/5.7/en/grant.html "https://dev.mysql.com/doc/refman/5.7/en/grant.html") in the _MySQL documentation_.
