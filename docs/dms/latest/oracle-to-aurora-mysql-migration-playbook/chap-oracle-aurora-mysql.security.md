# Oracle database users and MySQL users

With AWS DMS, you can migrate existing Oracle and MySQL databases to Amazon Aurora with minimal downtime. Oracle Database users and MySQL users refer to the user accounts that have been granted specific privileges to access and manipulate data within the respective database systems. Scenarios where you might need to learn about these users include migrating production databases with existing user accounts, consolidating multiple databases with different user configurations, or recreating a development environment with the same user structure as production.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                       |
| -------------------------------- | ---------------------------------- | ------------------------- | ----------------------------------------------------- |
| Three star feature compatibility | N/A                                | N/A                       | Syntax and option differences, similar functionality. |

## Oracle usage

Database user accounts are used for authenticating connecting sessions and authorizing access for individual users to specific database objects. Database Administrators grant privileges to user accounts, and applications use user accounts to access database objects.

### Steps for providing database access to applications

1. Create a user account in the database. User accounts are typically authenticated using a password. Additional methods of authenticating users also exist.
2. Assign permissions to the database user account enabling access to certain database objects and system permissions.
3. Connecting applications, authenticate using the database username and password.

### Oracle database users common properties

- Granting privileges or roles (collection of privileges) to the database user.
- Defining the default database tablespace for the user.
- Assigning tablespace quotas for the user.
- Configuring password policy, password complexity, lock, or unlock the account.

### Authentication mechanisms

- **Username** and **password** — This is the default option.
- **External** — Using the operating system or third-party software, such as Kerberos.
- **Global** — Enterprise directory service, such as Active Directory or Oracle Internet Directory.

### Oracle Schemas Compared to Users

In an Oracle database, a user equals a schema. This relationship is special because users and schemas are essentially the same thing. Consider an Oracle database user as the account you use to connect to a database while a database schema is the set of objects such as tables, views, and so on, that belong to that account.

- You can’t create schemas and users separately. When you create a database user, you also create a database schema with the same name.
- When you run the `CREATE USER` command in Oracle, you create a user for login and a schema in which to store database objects.
- Newly created schemas are empty, but objects such as tables can be created within them.

### Database users in Oracle 12c

Two types of users exist in the Oracle 12c database:

- **Common users** — Created in all database containers, root, and Pluggable Databases (PDB). Common users must have the C## prefix in the username.
- **Local users** — Created only in a specific PDB. Different database users with identical usernames can be created in multiple PDBs.

### Examples

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

For more information, see [Managing Security for Oracle Database Users](https://docs.oracle.com/database/121/DBSEG/users.htm#DBSEG002 "https://docs.oracle.com/database/121/DBSEG/users.htm#DBSEG002") in the _Oracle documentation_.

## MySQL usage

Database user accounts are used for authenticating connecting sessions and authorizing access for individual users to specific database objects. Database Administrators grant privileges to database user accounts that are used by applications to authenticate with an Aurora MySQL database.

For each account, CREATE USER creates a new row in the `mysql.user` system table. The account row reflects the properties specified in the statement. Unspecified properties are set to their default values:

- **Authentication** — The authentication plugin defined by the `default_authentication_plugin` system variable, and empty credentials.
- **SSL/TLS** — None.
- **Resource limits** — Unlimited.
- **Password management** — `PASSWORD EXPIRE DEFAULT`.
- **Account locking** — `ACCOUNT UNLOCK`.

When first created, accounts have no privileges. To assign privileges, use the GRANT statement.

### Steps for providing database access to applications

1. Create a user account in the database. Typically, users authenticate using a username and password. Additional methods of authenticating users also exist.
2. Assign permissions to the database user account enabling access to certain database objects and system permissions.
3. Connecting applications, use the database username and password combination to authenticate with the database.

### MySQL database users common properties

- Granting privileges to the database user.
- Configuring password policy, password complexity, lock, or unlock the account.
- Specifying authentication methods.
- User naming to indicate from which host names the user can login.
- Profiling, for example: `MAX_QUERIES_PER_HOUR` or `MAX_USER_CONNECTIONS`.

### Authentication mechanisms

- **Username** and **password** — This is the default option.
- **External** — Using the operating system or third-party software, such as an IAM user.
- **Global** — Enterprise directory service, such as Active Directory.

### IAM authentication

This feature is the equivalent to Oracle OS authentication.

With Amazon RDS for MySQL or Aurora MySQL, you can authenticate to your DB instance or DB cluster using AWS Identity and Access Management (IAM) database authentication. With this authentication method, you don’t need to use a password when you connect to a DB instance. Instead, you use an authentication token.

IAM database authentication provides the following benefits:

- Network traffic to and from the database is encrypted using Secure Sockets Layer (SSL).
- You can use IAM to centrally manage access to your database resources, instead of managing access individually on each DB instance or DB cluster.
- For applications running on Amazon EC2, you can use EC2 instance profile credentials to access the database instead of a password, for greater security.

###### Note

With IAM database authentication, you are limited to a maximum of 20 new connections in a single second.

### Examples

The following example demonstrates the following operations:

- Create a database use using the `PASSWORD EXPIRE` option.
- Grant privileges to the user.
- Assign profiling properties to the user.

```
CREATE USER 'testuser'
    IDENTIFIED BY 'new_password' PASSWORD EXPIRE;
GRANT ALL ON test_db.* to 'testuser';
GRANT CREATE USER on *.* to 'testuser';
ALTER USER 'testuser' WITH MAX_QUERIES_PER_HOUR 90;
```

To create an IAM user, make sure that the IAM user or role exists and is named by the same database username.

```
CREATE USER jane_doe IDENTIFIED WITH AWSAuthenticationPlugin AS 'RDS';
```

For more information, see [CREATE USER Statement](https://dev.mysql.com/doc/refman/5.7/en/create-user.html "https://dev.mysql.com/doc/refman/5.7/en/create-user.html") and [Specifying Account Names](https://dev.mysql.com/doc/refman/5.7/en/account-names.html "https://dev.mysql.com/doc/refman/5.7/en/account-names.html") in the _MySQL documentation_ and [IAM database authentication for MariaDB, MySQL, and PostgreSQL](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md") in the _Amazon Relational Database Service User Guide_.
