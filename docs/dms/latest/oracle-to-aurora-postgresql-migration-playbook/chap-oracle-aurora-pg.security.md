# Oracle database users and PostgreSQL users

With AWS DMS, you can migrate data from Oracle and PostgreSQL databases to Amazon Aurora. Database users are accounts that control authentication and authorization for a specific database instance.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| -------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Three star feature compatibility | N/A                                | N/A                       | N/A             |

## Oracle usage

Database user accounts are used for authenticating connecting sessions and authorizing access for individual users to specific database objects. Database Administrators grant privileges to user accounts, and applications use user accounts to access database objects.

### Steps for providing database access to applications

1. Create a user account in the database. User accounts are typically authenticated using a password. Additional methods of authenticating users also exist.
2. Assign permissions to the database user account enabling access to certain database objects and system permissions.
3. Connecting applications authenticate using the database username and password.

### Oracle database users common properties

- Granting privileges or roles (collection of privileges) to the database user.
- Defining the default database tablespace for the user.
- Assigning tablespace quotas for the user.
- Configuring password policy, password complexity, lock, or unlock the account.

### Authentication mechanisms

- **Username and Password** — Used by default.
- **External** — Using the operating system or third-party software (such as Kerberos).
- **Global** — Enterprise directory service (such as Active Directory or Oracle Internet Directory).

### Oracle schemas compared to users

In an Oracle database, a user equals a schema. This relationship is special because users and schemas are essentially the same thing. Consider an Oracle database user as the account you use to connect to a database while a database schema is the set of objects (tables, views, and so on) that belong to that account.

- You can’t create schemas and users separately. When you create a database user, you also create a database schema with the same name.
- When you run the `CREATE USER` command in Oracle, you create a user for login and a schema in which to store database objects.
- Newly created schemas are empty, but objects such as tables can be created within them.

### Database users in Oracle 12c

Two types of users exist in the Oracle 12c database:

- **Common Users** — Created in all database containers, root, and Pluggable Databases (PDB). Common users must have the C## prefix in the username.
- **Local Users** — Created only in a specific PDB. Different database users with identical usernames can be created in multiple PDBs.

**Examples**

The following example demonstrates the following operations:

- Create a common database user using the default tablespace.
- Grant privileges and roles to the user.
- Assign a profile to the user, unlock the account, and force the user to change the password (`PASSWORD EXPIRE`).
- Create a local database user in the `my_pdb1` pluggable database.

```
CREATE USER c##test_user IDENTIFIED BY password DEFAULT TABLESPACE USERS;
GRANT CREATE SESSION TO c##test_user;
GRANT RESOURCE TO c##test_user;
ALTER USER c##test_user ACCOUNT UNLOCK;
ALTER USER c##test_user PASSWORD EXPIRE;
ALTER USER c##test_user PROFILE ORA_STIG_PROFILE;
ALTER SESSION SET CONTAINER = my_pdb1;
CREATE USER app_user1 IDENTIFIED BY password DEFAULT TABLESPACE USERS;
```

For more information, see [Managing Security for Oracle Database Users](https://docs.oracle.com/database/121/DBSEG/users.htm "https://docs.oracle.com/database/121/DBSEG/users.htm") in the _Oracle documentation_.

## PostgreSQL usage

In PostgreSQL there are no users, only roles, role with connect privilege can be considered as a user.

For more information, see [PostgreSQL Roles](chap-oracle-aurora-pg.security.md#chap-oracle-aurora-pg.security.roles.pg "chap-oracle-aurora-pg.security.md#chap-oracle-aurora-pg.security.roles.pg").
