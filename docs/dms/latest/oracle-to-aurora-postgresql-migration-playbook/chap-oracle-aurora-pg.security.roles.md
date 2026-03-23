# Oracle and PostgreSQL roles

With AWS DMS, you can manage database user roles and permissions when migrating data from Oracle or PostgreSQL databases. Database roles define the privileges and access control for database users, specifying which operations they can perform on database objects like tables, views, and stored procedures.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                     |
| -------------------------------- | ---------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------- |
| Three star feature compatibility | N/A                                | N/A                       | Syntax and option differences, similar functionality. There are no users, only roles in PostgreSQL. |

## Oracle usage

Oracle roles are groups of privileges granted to database users. A database role can contain individual system and object permissions as well as other roles. Database roles enable you to grant multiple database privileges to users in one operation. It is convenient to group permissions together to ease the management of privileges.

Oracle 12c introduces a new multi-tenant database architecture that supports the creation of both common and local roles:

- **Common roles** — Roles created at the container database (CDB) level. A common role is a database role that exists in the root and in every existing and future pluggable database (PDB). Common roles are useful for cross-container operations such as ensuring a common user has a role in every container.
- **Local roles** — Roles created in a specific pluggable database (PDB). A local role exists only in a single pluggable database and can only contain roles and privileges that apply within the pluggable database in which the role exists.

Common role names must start with a c## prefix. Starting with Oracle 12.1.0.2, these prefixes can be changed using the COMMON_USER_PREFIX parameter.

A `CONTAINER` clause can be added to `CREATE ROLE` statement to choose the container applicable for the role.

**Examples**

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

For more information, see [Configuring Privilege and Role Authorization](https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/configuring-privilege-and-role-authorization.html#GUID-89CE989D-C97F-4CFD-941F-18203090A1AC "https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/configuring-privilege-and-role-authorization.html#GUID-89CE989D-C97F-4CFD-941F-18203090A1AC") in the _Oracle documentation_.

## PostgreSQL usage

In PostgreSQL, roles without login permissions are similar to database roles in Oracle. PostgreSQL roles are most similar to common roles in Oracle 12c as they are global in scope for all the databases in the instance.

- Roles are defined at the database cluster level and are valid in all databases in the PostgreSQL cluster. In terms of database scope, roles in PostgreSQL can be compared to common roles in Oracle 12c as they are global for all the databases and are not created in the individual scope of each database.
- The `CREATE USER` command in PostgreSQL is an alias for the `CREATE ROLE` command with one important difference: when using `CREATE USER` command, it automatically adds `LOGIN` so the role can access to the database as a database user. As such, for creating PostgreSQL roles that are similar in function to Oracle roles, be sure to use the `CREATE ROLE` command.

Roles with connect permissions are essentially database users.

- A role is a database entity that can own objects and have database privileges.
- A role can be considered a user, a group, or both depending on how it is used.
- Roles are defined at the root level and are valid in all databases in the Amazon Aurora cluster. In terms of database scope, roles in PostgreSQL can be compared to common users in Oracle 12c as they are global for all the databases and are not created in the individual scope of a specific database.
- Schemas are created separately from roles/users in PostgreSQL.

| Oracle                                 | PostgreSQL                                        |
| -------------------------------------- | ------------------------------------------------- |
| Common database user (12c)             | Database role with Login                          |
| Local database user (12c)              | N/A                                               |
| Database user (11g)                    | Database role with Login                          |
| Database role                          | Database role without Login                       |
| Database users are identical to schema | Database users and schemas are created separately |

The `CREATE USER` command in PostgreSQL is an alias for the `CREATE ROLE` command with one important difference: the `CREATE USER` command it automatically adds the `LOGIN` argument so that the role can access the database and act as a database user.

**Examples**

Create a new database role called myrole1 that will allow users (to which the role is assigned) to create new databases in the PostgreSQL cluster. Note that this role will not be able to login to the database and act as a database user. In addition, grant `SELECT`, `INSERT`, and `DELETE` privileges on the `hr.employees` table to the role.

```
CREATE ROLE hr_role;
GRANT SELECT, INSERT,DELETE on hr.employees to hr_role;
```

Typically, a role being used as a group of permissions would not have the `LOGIN` attribute, as with the preceding example.

Create a role that can log in to the database and specify a password.

```
CREATE USER test_user1 WITH PASSWORD 'password';

CREATE ROLE test_user2 WITH LOGIN PASSWORD 'password';
```

`CREATE USER` is identical to `CREATE ROLE`, except that it implies a login to the database.

When you provision a new Amazon Aurora cluster, a root user is created as the most powerful user in the database.

Create a role that can log in to the database and assign a password that has an expiration date.

```
CREATE ROLE test_user3 WITH LOGIN PASSWORD 'password' VALID UNTIL '2018-01-01';
```

Create a powerful role `db_admin` that provides users with the ability to create new databases. This role will not be able to log in to the database. Assign this role to the `test_user1` database user.

```
CREATE ROLE db_admin WITH CREATEDB;

GRANT db_admin TO test_user1;
```

Create a new `hello_world` schema and create a new table inside that schema.

```
CREATE SCHEMA hello_world;

CREATE TABLE hello_world.test_table1 (a int);
```

## Summary

| Description                                              | Oracle                                                                                                            | PostgreSQL                                                                                                                               |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| List all roles                                           | `<br>SELECT<br>• FROM dba_roles;<br>`                                                                             | `<br>SELECT<br>• FROM pg_roles;<br>`                                                                                                     |
| Create a new role                                        | `<br>CREATE ROLE c##common_role;<br>or<br>CREATE ROLE local_role1;<br>`                                           | `<br>CREATE ROLE test_role;<br>`                                                                                                         |
| Grant one role privilege to another database role        | `<br>GRANT local_role1 TO local_role2;<br>`                                                                       | `<br>grant myrole1 to myrole2;<br>`                                                                                                      |
| Grant privileges on a database object to a database role | `<br>GRANT CREATE TABLE<br>TO local_role;<br>`                                                                    | `<br>GRANT create<br>ON DATABASE postgresdb<br>to test_user;<br>`                                                                        |
| Grant DML permissions on a database object to a role     | `<br>hr.employees to myrole1;<br>`                                                                                | `<br>GRANT INSERT, DELETE<br>ON hr.employees<br>to myrole1;<br>`                                                                         |
| List all database users                                  | `<br>SELECT<br>• FROM dba_users;<br>`                                                                             | `<br>SELECT<br>• FROM pg_user;<br>`                                                                                                      |
| Create a database user                                   | `<br>CREATE USER c##test_user<br>IDENTIFIED BY test_user;<br>`                                                    | `<br>CREATE ROLE test_user<br>WITH LOGIN<br>PASSWORD 'test_user';<br>`                                                                   |
| Change the password for a database user                  | `<br>ALTER USER c##test_user<br>IDENTIFIED BY test_user;<br>`                                                     | `<br>ALTER ROLE test_user<br>WITH LOGIN<br>PASSWORD 'test_user';<br>`                                                                    |
| External authentication                                  | Supported via Externally Identified Users                                                                         | Currently not supported; future support for AWS Identity and Access Management (IAM) users is possible                                   |
| Tablespace quotas                                        | `<br>Alter User c##test_user QUOTA<br>UNLIMITED ON TABLESPACE users;<br>`                                         | Not supported                                                                                                                            |
| Grant role to user                                       | `<br>GRANT my_role TO c##test_user;<br>`                                                                          | `<br>GRANT my_role TO test_user;<br>`                                                                                                    |
| Lock user                                                | `<br>ALTER USER c##test_user ACCOUNT<br>LOCK;<br>`                                                                | `<br>ALTER ROLE test_user WITH<br>NOLOGIN;<br>`                                                                                          |
| Unlock user                                              | `<br>ALTER USER c##test_user ACCOUNT<br>UNLOCK;<br>`                                                              | `<br>ALTER ROLE test_user WITH LOGIN;<br>`                                                                                               |
| Grant privileges                                         | `<br>GRANT CREATE TABLE TO c##test_user;<br>`                                                                     | `<br>GRANT create<br>ON DATABASE postgres<br>to test_user;<br>`                                                                          |
| Default tablespace                                       | `<br>ALTER USER C##test_user default<br>tablespace users;<br>`                                                    | `<br>ALTER ROLE test_user SET default_<br>tablespace = 'pg_global';<br>`                                                                 |
| Grant select privilege on a table                        | `<br>GRANT SELECT<br>ON hr.employees<br>to c##test_user;<br>`                                                     | `<br>GRANT SELECT<br>ON hr.employees<br>to test_user;<br>`                                                                               |
| Grant DML privileges on a table                          | `<br>GRANT INSERT,DELETE<br>ON hr.employees<br>to c##test_user;<br>`                                              | `<br>GRANT INSERT,DELETE<br>ON hr.employees<br>to test_user;<br>`                                                                        |
| Grant execute                                            | `<br>GRANT EXECUTE<br>ON hr.procedure_name<br>to c##test_user;<br>`                                               | `<br>grant execute<br>on function "newdate"()<br>to test_user;<br>`<br>Specify the arguments types for the function inside the brackets. |
| Limits user connection                                   | `<br>CREATE PROFILE app_users<br>LIMIT SESSIONS_PER_USER 5;<br>ALTER USER C##TEST_USER<br>PROFILE app_users;<br>` | `<br>ALTER ROLE test_user WITH<br>CONNECTION LIMIT 5;<br>`                                                                               |
| Create a new database schema                             | `<br>CREATE USER my_app_schema<br>IDENTIFIED BY password;<br>`                                                    | `<br>CREATE SCHEMA my_app_schema;<br>`                                                                                                   |

For more information, see [CREATE ROLE](https://www.postgresql.org/docs/13/sql-createrole.html "https://www.postgresql.org/docs/13/sql-createrole.html") in the _PostgreSQL documentation_.
