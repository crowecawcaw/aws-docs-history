# Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition

You can use the following information to learn about the changes to be aware of when you convert from a different MySQL
8.0–compatible system to Aurora MySQL version 3.

In general, Aurora MySQL version 3 supports the feature set of community MySQL 8.0.23. Some new features from MySQL 8.0
community edition don't apply to Aurora MySQL. Some of those features aren't compatible with some aspect of Aurora, such
as the Aurora storage architecture. Other features aren't needed because the Amazon RDS management service provides equivalent
functionality. The following features in community MySQL 8.0 aren't supported or work differently in Aurora MySQL version 3.

For release notes for all Aurora MySQL version 3 releases, see [Database engine updates for
Amazon Aurora MySQL version 3](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md") in the _Release Notes for Aurora MySQL_.

###### Topics

- [MySQL 8.0 features not available in Aurora MySQL version 3](#AuroraMySQL.Compare-80-v3-features "#AuroraMySQL.Compare-80-v3-features")
- [Role-based privilege model](#AuroraMySQL.privilege-model "#AuroraMySQL.privilege-model")
- [Finding the database server ID](#AuroraMySQL.server-id "#AuroraMySQL.server-id")
- [Authentication](#AuroraMySQL.mysql80-authentication "#AuroraMySQL.mysql80-authentication")

## MySQL 8.0 features not available in Aurora MySQL version 3

The following features from community MySQL 8.0 aren't available or work differently in Aurora MySQL version 3.

- Resource groups and associated SQL statements aren't supported in Aurora MySQL.
- Aurora MySQL doesn't support user-defined undo tablespaces and associated SQL statements, such as `CREATE
UNDO TABLESPACE`, `ALTER UNDO TABLESPACE ... SET INACTIVE`, and `DROP UNDO
TABLESPACE`.
- Aurora MySQL doesn't support undo tablespace truncation for Aurora MySQL versions lower than 3.06. In Aurora MySQL
  version 3.06 and higher, [automated
  undo tablespace truncation](https://dev.mysql.com/doc/refman/8.0/en/innodb-undo-tablespaces.html#truncate-undo-tablespace "https://dev.mysql.com/doc/refman/8.0/en/innodb-undo-tablespaces.html#truncate-undo-tablespace") is supported.
- Password validation plugin is supported.
- You can't modify the settings of any MySQL plugins, including password validation plugin.
- The X plugin isn't supported.
- Multisource replication isn't supported.

## Role-based privilege model

With Aurora MySQL version 3, you can't modify the tables in the `mysql` database directly. In particular,
you can't set up users by inserting into the `mysql.user` table. Instead, you use SQL statements to grant
role-based privileges. You also can't create other kinds of objects such as stored procedures in the `mysql`
database. You can still query the `mysql` tables. If you use binary log replication, changes made directly to the
`mysql` tables on the source cluster aren't replicated to the target cluster.

In some cases, your application might use shortcuts to create users or other objects by inserting into the
`mysql` tables. If so, change your application code to use the corresponding statements such as `CREATE
 USER`. If your application creates stored procedures or other objects in the `mysql` database, use a
different database instead.

To export metadata for database users during the migration from an external MySQL database, you can use a MySQL Shell
command instead of `mysqldump`. For more information, see
[Instance
Dump Utility, Schema Dump Utility, and Table Dump Utility](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-utilities-dump-instance-schema.html#mysql-shell-utilities-dump-about "https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-utilities-dump-instance-schema.html#mysql-shell-utilities-dump-about").

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

###### Topics

- [rds_superuser_role](#AuroraMySQL.privilege-model.rds_superuser_role "#AuroraMySQL.privilege-model.rds_superuser_role")
- [Privilege checks user for
  binary log replication](#AuroraMySQL.privilege-model.binlog "#AuroraMySQL.privilege-model.binlog")
- [Roles for accessing other AWS services](#AuroraMySQL.privilege-model.other "#AuroraMySQL.privilege-model.other")

### rds_superuser_role

Aurora MySQL version 3 includes a special role that has all of the following
privileges. This role is named `rds_superuser_role`. The primary
administrative user for each cluster already has this role granted. The
`rds_superuser_role` role includes the following privileges for
all database objects:

- `ALTER`
- `APPLICATION_PASSWORD_ADMIN`
- `ALTER ROUTINE`
- `CONNECTION_ADMIN`
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
- `FLUSH_OPTIMIZER_COSTS` (Aurora MySQL version 3.09 and higher)
- `FLUSH_STATUS` (Aurora MySQL version 3.09 and higher)
- `FLUSH_TABLES` (Aurora MySQL version 3.09 and higher)
- `FLUSH_USER_RESOURCES` (Aurora MySQL version 3.09 and higher)
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
- `SHOW_ROUTINE` (Aurora MySQL version 3.04 and higher)
- `SHOW VIEW`
- `TRIGGER`
- `UPDATE`
- `XA_RECOVER_ADMIN`

The role definition also includes `WITH GRANT OPTION` so that an
administrative user can grant that role to other users. In particular, the
administrator must grant any privileges needed to perform binary log replication
with the Aurora MySQL cluster as the target.

###### Tip

To see the full details of the permissions, enter the following
statements.

```
SHOW GRANTS FOR rds_superuser_role@'%';
SHOW GRANTS FOR `name_of_administrative_user_for_your_cluster`@'%';

```

### Privilege checks user for

binary log replication

Aurora MySQL version 3 includes a privilege checks user for binary log (binlog)
replication, `rdsrepladmin_priv_checks_user`. In addition to the
privileges of `rds_superuser_role`, this user has the
`replication_applier` privilege.

When you turn on binlog replication by calling the
`mysql.rds_start_replication` stored procedure,
`rdsrepladmin_priv_checks_user` is created.

The `rdsrepladmin_priv_checks_user@localhost` user is a reserved
user. Don't modify it.

### Roles for accessing other AWS services

Aurora MySQL version 3 includes roles that you can use to access other AWS services. You can set many of these roles as an alternative to
granting privileges. For example, you specify `GRANT AWS_LAMBDA_ACCESS TO `user`` instead of `GRANT
 INVOKE LAMBDA ON *.* TO `user``. For the procedures to access other AWS services, see [Integrating Amazon Aurora MySQL with other AWS
services](AuroraMySQL.md "AuroraMySQL.md"). Aurora MySQL version 3 includes the following roles related
to accessing other AWS services:

- `AWS_LAMBDA_ACCESS` – An alternative to the `INVOKE LAMBDA` privilege. For usage information, see
  [Invoking a Lambda function from an Amazon Aurora MySQL DB
  cluster](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- `AWS_LOAD_S3_ACCESS` – An alternative to the `LOAD FROM S3` privilege. For usage information, see
  [Loading data into an Amazon Aurora MySQL DB cluster from
  text files in an Amazon S3 bucket](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- `AWS_SELECT_S3_ACCESS` – An alternative to the `SELECT INTO S3` privilege. For usage information, see
  [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3
  bucket](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- `AWS_COMPREHEND_ACCESS` – An alternative to the `INVOKE COMPREHEND` privilege. For usage information, see
  [Granting database users access to Aurora machine learning](mysql-ml.md#aurora-ml-sql-privileges "mysql-ml.md#aurora-ml-sql-privileges").
- `AWS_SAGEMAKER_ACCESS` – An alternative to the `INVOKE SAGEMAKER` privilege. For usage information, see
  [Granting database users access to Aurora machine learning](mysql-ml.md#aurora-ml-sql-privileges "mysql-ml.md#aurora-ml-sql-privileges").
- `AWS_BEDROCK_ACCESS` – There's no analogous `INVOKE` privilege for Amazon Bedrock. For usage information, see
  [Granting database users access to Aurora machine learning](mysql-ml.md#aurora-ml-sql-privileges "mysql-ml.md#aurora-ml-sql-privileges").

When you grant access by using roles in Aurora MySQL version 3, you also activate the role by using the `SET ROLE `role_name``
 or`SET ROLE ALL`statement. The following example shows how. Substitute the appropriate role name for`AWS_SELECT_S3_ACCESS`.

```
# Grant role to user.

`mysql>` GRANT AWS_SELECT_S3_ACCESS TO '`user`'@'`domain-or-ip-address`'

# Check the current roles for your user. In this case, the AWS_SELECT_S3_ACCESS role has not been activated.
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
`+-----------------------------------------------------+
| CURRENT_ROLE() |
+-----------------------------------------------------+
| `AWS_SELECT_S3_ACCESS`@`%`,`rds_superuser_role`@`%` |
+-----------------------------------------------------+`

```

## Finding the database server ID

The database server ID (`server_id`) is required for binary logging (binlog) replication. The way to find the server ID is
different in Aurora MySQL from Community MySQL.

In Community MySQL, the server ID is a number, which you obtain by using the following syntax while logged into the server:

```
mysql> select @@server_id;

+-------------+
| @@server_id |
+-------------+
| 2           |
+-------------+
1 row in set (0.00 sec)
```

In Aurora MySQL, the server ID is the DB instance ID, which you obtain by using the following syntax while logged into the DB instance:

```
mysql> select @@aurora_server_id;

+------------------------+
| @@aurora_server_id     |
+------------------------+
| mydbcluster-instance-2 |
+------------------------+
1 row in set (0.00 sec)
```

For more information on binlog replication, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB
cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

## Authentication

In community MySQL 8.0, the default authentication plugin is
`caching_sha2_password`. Aurora MySQL version 3 still uses the
`mysql_native_password` plugin. You can't change the
`default_authentication_plugin` setting. You can, however, create new users and alter current users, and their individual passwords use the new authentication plugin. Following is an example.

```
mysql> CREATE USER 'testnewsha'@'%' IDENTIFIED WITH caching_sha2_password BY 'aNewShaPassword';
Query OK, 0 rows affected (0.74 sec)
```
