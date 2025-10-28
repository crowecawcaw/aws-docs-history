# Granting and revoking privileges for RDS for Db2

Users gain access to databases through membership in groups that are attached to
databases.

Use the following procedures to grant and revoke privileges to control access to your
database.

These procedures use IBM Db2 CLP running on a local machine to connect to an RDS for Db2 DB
instance. Be sure to catalog the TCPIP node and the database to connect to your RDS for Db2 DB
instance running on your local machine. For more information, see [Connecting to your Amazon RDS for Db2 DB instance
with IBM Db2 CLP](db2-connecting-with-clp-client.md "db2-connecting-with-clp-client.md").

###### Topics

- [Granting a user access to your
  database](#db2-granting-user-access "#db2-granting-user-access")
- [Changing a user's password](#db2-changing-user-password "#db2-changing-user-password")
- [Adding groups to a user](#db2-adding-group-to-user "#db2-adding-group-to-user")
- [Removing groups from a user](#db2-removing-groups-from-user "#db2-removing-groups-from-user")
- [Removing a user](#db2-removing-user "#db2-removing-user")
- [Listing users](#db2-listing-users-database "#db2-listing-users-database")
- [Creating a role](#db2-creating-role "#db2-creating-role")
- [Granting a role](#db2-granting-role "#db2-granting-role")
- [Revoking a role](#db2-revoking-role "#db2-revoking-role")
- [Dropping a role](#db2-dropping-role "#db2-dropping-role")
- [Granting database authorization](#db2-granting-dbadmin-auth "#db2-granting-dbadmin-auth")
- [Revoking database authorization](#db2-revoking-dbadmin-auth "#db2-revoking-dbadmin-auth")

## Granting a user access to your

database

###### To grant a user access to your database

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

This command produces output similar to the following example:

```
Database Connection Information

Database server        = DB2/LINUXX8664 11.5.8.0
SQL authorization ID   = ADMIN
Local database alias   = RDSADMIN
```

2. Add a user to your authorization list by calling
   `rdsadmin.add_user`. For more information, see [rdsadmin.add_user](db2-sp-granting-revoking-privileges.md#db2-sp-add-user "db2-sp-granting-revoking-privileges.md#db2-sp-add-user").

```
db2 "call rdsadmin.add_user(
    '`username`',
    '`password`',
    '`group_name`,`group_name`')"
```

3. (Optional) Add additional groups to the user by calling
   `rdsadmin.add_groups`. For more information, see [rdsadmin.add_groups](db2-sp-granting-revoking-privileges.md#db2-sp-add-groups "db2-sp-granting-revoking-privileges.md#db2-sp-add-groups").

```
db2 "call rdsadmin.add_groups(
    '`username`',
    '`group_name`,`group_name`')"
```

4. Confirm the authorities that are available to the user. In the following
   example, replace `rds_database_alias`,
   `master_user`, and
   `master_password` with your own information. Also,
   replace `username` with the user's username.

```
db2 terminate
db2 connect to `rds_database_alias` user `master_user` using `master_password`
db2 "SELECT SUBSTR(AUTHORITY,1,20) AUTHORITY, D_USER, D_GROUP, D_PUBLIC
       FROM TABLE (SYSPROC.AUTH_LIST_AUTHORITIES_FOR_AUTHID ('`username`', 'U') ) AS T
       ORDER BY AUTHORITY"
```

This command produces output similar to the following example:

```
AUTHORITY            D_USER D_GROUP D_PUBLIC
-------------------- ------ ------- --------
ACCESSCTRL           N      N       N
BINDADD              N      N       N
CONNECT              N      N       N
CREATETAB            N      N       N
CREATE_EXTERNAL_ROUT N      N       N
CREATE_NOT_FENCED_RO N      N       N
CREATE_SECURE_OBJECT N      N       N
DATAACCESS           N      N       N
DBADM                N      N       N
EXPLAIN              N      N       N
IMPLICIT_SCHEMA      N      N       N
LOAD                 N      N       N
QUIESCE_CONNECT      N      N       N
SECADM               N      N       N
SQLADM               N      N       N
SYSADM               *      N       *
SYSCTRL              *      N       *
SYSMAINT             *      N       *
SYSMON               *      N       *
WLMADM               N      N       N
```

5. Grant the RDS for Db2 roles `ROLE_NULLID_PACKAGES`,
   `ROLE_TABLESPACES`, and `ROLE_PROCEDURES` to the group
   that you added the user to. For more information, see [Amazon RDS for Db2 default roles](db2-default-roles.md "db2-default-roles.md").

###### Note

We create RDS for Db2 DB instances in `RESTRICTIVE` mode.
Therefore, the RDS for Db2 roles `ROLE_NULLID_PACKAGES`,
`ROLE_TABLESPACES`, and `ROLE_PROCEDURES` grant
execute privileges on `NULLID` packages for IBM Db2 CLP and
Dynamic SQL. These roles also grant user privileges on
tablespaces.

    1. Connect to your Db2 database. In the following example, replace
     `database_name`,
     `master_user`, and
     `master_password` with your own
     information.



    ```
    db2 connect to `database_name` user `master_user` using `master_password`
    ```
    2. Grant the role `ROLE_NULLED_PACKAGES` to a group. In the
     following example, replace `group_name` with
     the name of the group that you want to add the role to.



    ```
    db2 "grant role ROLE_NULLID_PACKAGES to group `group_name`"
    ```
    3. Grant the role `ROLE_TABLESPACES` to the same group. In the
     following example, replace `group_name` with
     the name of the group that you want to add the role to.



    ```
    db2 "grant role ROLE_TABLESPACES to group `group_name`"
    ```
    4. Grant the role `ROLE_PROCEDURES` to the same group. In the
     following example, replace `group_name` with
     the name of the group that you want to add the role to.



    ```
    db2 "grant role ROLE_PROCEDURES to group `group_name`"
    ```

6. Grant `connect`, `bindadd`, `createtab`, and
   `IMPLICIT_SCHEMA` authorities to the group that you added the
   user to. In the following example, replace `group_name`
   with the name of the second group that you added the user to.

```
db2 "grant usage on workload SYSDEFAULTUSERWORKLOAD to public"
db2 "grant connect, bindadd, createtab, implicit_schema on database to group `group_name`"
```

7. Repeat steps 4 through 6 for each additional group that you added the user
   to.
8. Test the user's access by connecting as the user, creating a table, inserting
   values into the table, and returning data from the table. In the following
   example, replace `rds_database_alias`,
   `username`, and `password`
   with the name of the database and the user's username and password.

```
db2 connect to `rds_database_alias` user `username` using `password`
db2 "create table t1(c1 int not null)"
db2 "insert into t1 values (1),(2),(3),(4)"
db2 "select * from t1"
```

## Changing a user's password

###### To change a user's password

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Change the password by calling `rdsadmin.change_password`. For more
   information, see [rdsadmin.change_password](db2-sp-granting-revoking-privileges.md#db2-sp-change-password "db2-sp-granting-revoking-privileges.md#db2-sp-change-password").

```
db2 "call rdsadmin.change_password(
    '`username`',
    '`new_password`')"
```

## Adding groups to a user

###### To add groups to a user

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Add groups to a user by calling `rdsadmin.add_groups`. For more
   information, see [rdsadmin.add_groups](db2-sp-granting-revoking-privileges.md#db2-sp-add-groups "db2-sp-granting-revoking-privileges.md#db2-sp-add-groups").

```
db2 "call rdsadmin.add_groups(
    '`username`',
    '`group_name`,`group_name`')"
```

## Removing groups from a user

###### To remove groups from a user

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Remove groups by calling `rdsadmin.remove_groups`. For more
   information, see [rdsadmin.remove_groups](db2-sp-granting-revoking-privileges.md#db2-sp-remove-groups "db2-sp-granting-revoking-privileges.md#db2-sp-remove-groups").

```
db2 "call rdsadmin.remove_groups(
    '`username`',
    '`group_name`,`group_name`')"
```

## Removing a user

###### To remove a user from the authorization list

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Remove a user from your authorization list by calling
   `rdsadmin.remove_user`. For more information, see [rdsadmin.remove_user](db2-sp-granting-revoking-privileges.md#db2-sp-remove-user "db2-sp-granting-revoking-privileges.md#db2-sp-remove-user").

```
db2 "call rdsadmin.remove_user('`username`')"
```

## Listing users

To list users on an authorization list, call the `rdsadmin.list_users`
stored procedure. For more information, see [rdsadmin.list_users](db2-sp-granting-revoking-privileges.md#db2-sp-list-users "db2-sp-granting-revoking-privileges.md#db2-sp-list-users").

```
db2 "call rdsadmin.list_users()"
```

## Creating a role

You can use the [rdsadmin.create_role](db2-sp-granting-revoking-privileges.md#db2-sp-create-role "db2-sp-granting-revoking-privileges.md#db2-sp-create-role") stored procedure to create a role.

###### To create a role

1. Connect to the `rdsadmin` database. In the following example,
   replace `master_username` and
   `master_password` with your information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Set Db2 to output content.

```
db2 set serveroutput on
```

3. Create a role. For more information, see [rdsadmin.create_role](db2-sp-granting-revoking-privileges.md#db2-sp-create-role "db2-sp-granting-revoking-privileges.md#db2-sp-create-role").

```
db2 "call rdsadmin.create_role(
    '`database_name`',
    '`role_name`')"
```

4. Set Db2 to not output content.

```
db2 set serveroutput off
```

## Granting a role

You can use the [rdsadmin.grant_role](db2-sp-granting-revoking-privileges.md#db2-sp-grant-role "db2-sp-granting-revoking-privileges.md#db2-sp-grant-role")
stored procedure to assign a role to a role, user, or group.

###### To assign a role

1. Connect to the `rdsadmin` database. In the following example,
   replace `master_username` and
   `master_password` with your information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Set Db2 to output content.

```
db2 set serveroutput on
```

3. Assign a role. For more information, see [rdsadmin.grant_role](db2-sp-granting-revoking-privileges.md#db2-sp-grant-role "db2-sp-granting-revoking-privileges.md#db2-sp-grant-role").

```
db2 "call rdsadmin.grant_role(
    '`database_name`',
    '`role_name`',
    '`grantee`',
    '`admin_option`')"
```

4. Set Db2 to not output content.

```
db2 set serveroutput off
```

## Revoking a role

You can use the [rdsadmin.revoke_role](db2-sp-granting-revoking-privileges.md#db2-sp-revoke-role "db2-sp-granting-revoking-privileges.md#db2-sp-revoke-role") stored procedure to revoke a role from a role, user, or group.

###### To revoke a role

1. Connect to the `rdsadmin` database. In the following example,
   replace `master_username` and
   `master_password` with your information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Revoke a role. For more information, see [rdsadmin.revoke_role](db2-sp-granting-revoking-privileges.md#db2-sp-revoke-role "db2-sp-granting-revoking-privileges.md#db2-sp-revoke-role").

```
db2 "call rdsadmin.revoke_role(
    ?,
    '`database_name`',
    '`role_name`',
    '`grantee`')"
```

## Dropping a role

You can use the [rdsadmin.drop_role](db2-sp-granting-revoking-privileges.md#db2-sp-drop-role "db2-sp-granting-revoking-privileges.md#db2-sp-drop-role")
stored procedure to drop a role.

###### To drop a role

1. Connect to the `rdsadmin` database. In the following example,
   replace `master_username` and
   `master_password` with your information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Drop a role. For more information, see [rdsadmin.drop_role](db2-sp-granting-revoking-privileges.md#db2-sp-drop-role "db2-sp-granting-revoking-privileges.md#db2-sp-drop-role").

```
db2 "call rdsadmin.drop_role(
    ?,
    '`database_name`',
    '`role_name`')"
```

## Granting database authorization

The master user, who has `DBADM` authorization, can grant
`DBADM`, `ACCESSCTRL`, or `DATAACCESS`
authorization to a role, user, or group.

###### To grant database authorization

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Grant a user access by calling `rdsadmin.dbadm_grant`. For more
   information, see [rdsadmin.dbadm_grant](db2-sp-granting-revoking-privileges.md#db2-sp-dbadm-grant "db2-sp-granting-revoking-privileges.md#db2-sp-dbadm-grant").

```
db2 "call rdsadmin.dbadm_grant(
    ?,
    '`database_name`,
    '`authorization`',
    '`grantee`')"
```

**Example use case**

The following procedure walks you through creating a role, granting `DBADM`
authorization to the role, assigning the role to a user, and granting the role to a
group.

######

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Create a role called `PROD_ROLE` for a database called
   `TESTDB`. For more information, see [rdsadmin.create_role](db2-sp-granting-revoking-privileges.md#db2-sp-create-role "db2-sp-granting-revoking-privileges.md#db2-sp-create-role").

```
db2 "call rdsadmin.create_role(
    'TESTDB',
    'PROD_ROLE')"
```

3. Assign the role to a user called `PROD_USER`. The
   `PROD_USER` is given admin authorization to assign roles. For
   more information, see [rdsadmin.grant_role](db2-sp-granting-revoking-privileges.md#db2-sp-grant-role "db2-sp-granting-revoking-privileges.md#db2-sp-grant-role").

```
db2 "call rdsadmin.grant_role(
    ?,
    'TESTDB',
    'PROD_ROLE',
    'USER PROD_USER',
    'Y')"
```

4. (Optional) Provide additional authorization or privileges. The following
   example grants `DBADM` authorization to a role named
   `PROD_ROLE` for a database called `FUNDPROD`. For more
   information, see [rdsadmin.dbadm_grant](db2-sp-granting-revoking-privileges.md#db2-sp-dbadm-grant "db2-sp-granting-revoking-privileges.md#db2-sp-dbadm-grant").

```
db2 "call rdsadmin.dbadm_grant(
    ?,
    'FUNDPROD',
    'DBADM',
    'ROLE PROD_ROLE')"
```

5. Terminate your session.

```
db2 terminate
```

6. Connect to the `TESTDB` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to TESTDB user `master_username` using `master_password`
```

7. Add more authorizations to the role.

```
db2 "grant connect, implicit_schema on database to role PROD_ROLE"
```

8. Grant the role `PROD_ROLE` to a group.

```
db2 "grant role PROD_ROLE to group PRODGRP"
```

Users who belong to the group `PRODGRP` can now perform actions such as
connecting to the `TESTDB` database, creating tables, or creating
schemas.

## Revoking database authorization

The master user, who has `DBADM` authorization, can revoke
`DBADM`, `ACCESSCTRL`, or `DATAACCESS`
authorization from a role, user, or group.

###### To revoke database authorization

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Revoke user access by calling `rdsadmin.dbadm_revoke`. For more
   information, see [rdsadmin.dbadm_revoke](db2-sp-granting-revoking-privileges.md#db2-sp-dbadm-revoke "db2-sp-granting-revoking-privileges.md#db2-sp-dbadm-revoke").

```
db2 "call rdsadmin.dbadm_revoke(
    ?,
    '`database_name`,
    '`authorization`',
    '`grantee`')"
```
