

# Comparing Aurora MySQL version 8.4 and MySQL 8.4 Community Edition
<a name="AuroraMySQL.Compare-v84-community"></a>

This topic describes the differences between Aurora MySQL version 8.4 and MySQL 8.4 Community Edition.

**Topics**
+ [Authentication](#AuroraMySQL.Compare-v84-community.auth)
+ [Reserved users](#AuroraMySQL.Compare-v84-community.reserved-users)
+ [rds\_superuser\_role](#AuroraMySQL.Compare-v84-community.rds-superuser)
+ [Password validation component support in Aurora MySQL version 8.4](#AuroraMySQL.Compare-v84-community.validate-password)
+ [Parameter default changes](#AuroraMySQL.Compare-v84-community.parameters)

## Authentication
<a name="AuroraMySQL.Compare-v84-community.auth"></a>

Aurora MySQL version 8.4 only supports the following values for the `authentication_policy` parameter:
+ `*:caching_sha2_password` (Default value. Allows any single factor authentication plugin, using `caching_sha2_password` if none is specified)
+ `*:mysql_native_password` (Allows any single factor authentication plugin, using `mysql_native_password` if none is specified)

**Note**  
Multi-factor authentication configurations are not supported in Aurora MySQL.

## Reserved users
<a name="AuroraMySQL.Compare-v84-community.reserved-users"></a>

Aurora MySQL reserves certain usernames for internal features. These usernames cannot be used for your database user accounts. For more information, see [Reserved users in Aurora MySQL](AuroraMySQL.Security.md#AuroraMySQL.Security.ReservedUsers).

Starting in Aurora MySQL version 8.4.7, the engine protects `rdsproxyadmin` because it is the monitoring user for RDS Proxy. Aurora creates the `rdsproxyadmin` account automatically when you register a proxy target. For details about the rejected operations and error output, see [Reserved users in Aurora MySQL](AuroraMySQL.Security.md#AuroraMySQL.Security.ReservedUsers).

## rds\_superuser\_role
<a name="AuroraMySQL.Compare-v84-community.rds-superuser"></a>

Aurora MySQL version 8.4 includes a special role that has all the following privileges. This role is named `rds_superuser_role`. The master user for each cluster already has this role granted. The `rds_superuser_role` role includes the following privileges for all database objects:
+ `ALTER`
+ `ALLOW_NONEXISTENT_DEFINER`
+ `APPLICATION_PASSWORD_ADMIN`
+ `ALTER ROUTINE`
+ `CONNECTION_ADMIN`
+ `CREATE`
+ `CREATE ROLE`
+ `CREATE ROUTINE`
+ `CREATE TEMPORARY TABLES`
+ `CREATE USER`
+ `CREATE VIEW`
+ `DELETE`
+ `DROP`
+ `DROP ROLE`
+ `EVENT`
+ `EXECUTE`
+ `FLUSH_OPTIMIZER_COSTS`
+ `FLUSH_PRIVILEGES`
+ `FLUSH_STATUS`
+ `FLUSH_TABLES`
+ `FLUSH_USER_RESOURCES`
+ `INDEX`
+ `INSERT`
+ `LOCK TABLES`
+ `OPTIMIZE_LOCAL_TABLE`
+ `PROCESS`
+ `REFERENCES`
+ `RELOAD`
+ `REPLICATION CLIENT`
+ `REPLICATION SLAVE`
+ `ROLE_ADMIN`
+ `SELECT`
+ `SET_ANY_DEFINER`
+ `SHOW DATABASES`
+ `SHOW_ROUTINE`
+ `SHOW VIEW`
+ `TRIGGER`
+ `UPDATE`
+ `XA_RECOVER_ADMIN`

## Password validation component support in Aurora MySQL version 8.4
<a name="AuroraMySQL.Compare-v84-community.validate-password"></a>
+ The `validate_password` component is supported, including its customizations. The component is managed through the database parameter `aurora_enable_validate_password_component` instead of `INSTALL COMPONENT` and `UNINSTALL COMPONENT` commands.
+ The `validate_password` plugin is partially supported to allow migration to the component.

For more information, see [Password policies and Password validation in Aurora MySQL](AuroraMySQL.PasswordPolicies.md).

## Parameter default changes
<a name="AuroraMySQL.Compare-v84-community.parameters"></a>

### temptable\_max\_mmap
<a name="AuroraMySQL.Compare-v84-community.temptable-max-mmap"></a>

In MySQL 8.4 Community Edition, the default value of `temptable_max_mmap` is `0`, which disables memory-mapped temporary tables.

Aurora MySQL version 8.4.7 and higher overrides this default. Aurora sets `temptable_max_mmap` to a value calculated from the cluster's allocated storage, using the following formula:

```
LEAST(4294967296, {AllocatedStorage*3/100})
```

This sets the default to 3% of allocated storage, capped at a maximum of 4 GiB. Memory-mapped temporary tables remain enabled by default in Aurora MySQL version 8.4.7 and higher, in contrast to community MySQL 8.4.

For the parameter reference entry, see [Aurora MySQL configuration parameters](AuroraMySQL.Reference.ParameterGroups.md).