

# Comparing Aurora MySQL version 3 and Aurora MySQL version 8.4
<a name="AuroraMySQL.Compare-v3-v84"></a>

Amazon Aurora MySQL version 8.4 introduces significant enhancements and changes compared to Aurora MySQL version 3 (compatible with MySQL 8.0). This guide highlights the key differences to help you understand what is new and what has changed.

**Topics**
+ [Authentication and Security](#AuroraMySQL.Compare-v3-v84.auth)
+ [Password Management](#AuroraMySQL.Compare-v3-v84.password)
+ [Parameter default changes](#AuroraMySQL.Compare-v3-v84.parameters)
+ [Privileges and Roles](#AuroraMySQL.Compare-v3-v84.privileges)

## Authentication and Security
<a name="AuroraMySQL.Compare-v3-v84.auth"></a>

### Authentication plugin management
<a name="AuroraMySQL.Compare-v3-v84.auth-plugin"></a>

**Aurora MySQL version 3** uses the `default_authentication_plugin` parameter to configure the default authentication plugin for new database users.

**Aurora MySQL version 8.4** replaces the `default_authentication_plugin` with the `authentication_policy` parameter, which provides more flexible authentication configuration.

### TLS and encryption
<a name="AuroraMySQL.Compare-v3-v84.tls"></a>

**Aurora MySQL version 8.4** enforces stricter security standards:
+ The `require_secure_transport` parameter is set to `ON` by default, requiring TLS for all connections.
+ Supports only TLS 1.2 and TLS 1.3.
+ Enforces modern cryptographic standards with restricted cipher suites.

For more information, see [Security with Amazon Aurora MySQL](AuroraMySQL.Security.md).

## Password Management
<a name="AuroraMySQL.Compare-v3-v84.password"></a>

### Password validation
<a name="AuroraMySQL.Compare-v3-v84.password-validation"></a>

Aurora MySQL version 3 supports the `validate_password` plugin and component through manual installation, limited to default parameters with no customization available.

Aurora MySQL version 8.4 supports managing the `validate_password` component through DB cluster parameters:
+ New cluster parameter: `aurora_enable_validate_password_component`
+ No manual installation needed – simply enable or disable via parameter.
+ Component not listed in `mysql.component` table.
+ Component status can be checked via cluster parameter group APIs or global variable `aurora_enable_validate_password_component`.

Aurora MySQL version 8.4 introduces the following cluster-level parameters for password validation customization:
+ `validate_password.check_user_name`
+ `validate_password.length`
+ `validate_password.mixed_case_count`
+ `validate_password.number_count`
+ `validate_password.policy` (supports LOW and MEDIUM levels only)
+ `validate_password.special_char_count`

For more information, see [Password policies and Password validation in Aurora MySQL](AuroraMySQL.PasswordPolicies.md).

The following non-modifiable instance-level `validate_password` plugin parameters are removed in Aurora MySQL version 8.4:
+ `validate-password`
+ `validate_password_dictionary_file`
+ `validate_password_length`
+ `validate_password_mixed_case_count`
+ `validate_password_number_count`
+ `validate_password_policy`
+ `validate_password_special_char_count`

For more information, see [Aurora MySQL configuration parameters](AuroraMySQL.Reference.ParameterGroups.md).

### Password policies
<a name="AuroraMySQL.Compare-v3-v84.password-policies"></a>

**Aurora MySQL version 8.4** adds comprehensive password policy support through new cluster parameters:
+ `default_password_lifetime`
+ `password_history`
+ `password_reuse_interval`
+ `password_require_current`
+ `disconnect_on_expired_password`

These parameters work alongside per-account password policies for granular control. For more information, see [Password policies and Password validation in Aurora MySQL](AuroraMySQL.PasswordPolicies.md).

## Parameter default changes
<a name="AuroraMySQL.Compare-v3-v84.parameters"></a>

### temptable\_max\_mmap
<a name="AuroraMySQL.Compare-v3-v84.temptable-max-mmap"></a>

**Aurora MySQL version 3** uses a fixed default of 1 GiB (`1073741824`) for the `temptable_max_mmap` parameter across all instance classes and storage configurations.

**Aurora MySQL version 8.4.7 and higher** calculates the default dynamically based on the cluster's allocated storage. The formula is:

```
LEAST(4294967296, {AllocatedStorage*3/100})
```

This sets the default to 3% of allocated storage, capped at a maximum of 4 GiB. The default scales with storage capacity while remaining bounded, which helps reduce query failures on reader instances that use the TempTable storage engine.

For the parameter reference entry, see [Aurora MySQL configuration parameters](AuroraMySQL.Reference.ParameterGroups.md).

## Privileges and Roles
<a name="AuroraMySQL.Compare-v3-v84.privileges"></a>

### New dynamic privileges
<a name="AuroraMySQL.Compare-v3-v84.new-privileges"></a>

**Aurora MySQL version 8.4** supports new privileges, granted to `rds_superuser_role`:
+ `ALLOW_NONEXISTENT_DEFINER`
+ `FLUSH_PRIVILEGES`
+ `OPTIMIZE_LOCAL_TABLE`
+ `SET_ANY_DEFINER`

The `SET_USER_ID` privilege is removed as it is replaced by `ALLOW_NONEXISTENT_DEFINER` and `SET_ANY_DEFINER`.

For more information, see [Master user account privileges](UsingWithRDS.MasterAccounts.md).

### Master user behavior
<a name="AuroraMySQL.Compare-v3-v84.master-user"></a>

**Aurora MySQL version 3:** Master user uses `mysql_native_password` auth plugin for password-based authentication by default.

**Aurora MySQL version 8.4:** Master user authentication plugin is set to the default value defined in the `authentication_policy` cluster parameter (By default, `caching_sha2_password` plugin).

When resetting the master user password via the AWS Management Console, CLI, or API, or through AWS Secrets Manager rotation, Aurora automatically uses the authentication plugin defined by the current `authentication_policy` parameter value at the time of the reset.

### Protected user enforcement for `rdsproxyadmin`
<a name="AuroraMySQL.Compare-v3-v84.reserved-users"></a>

**Aurora MySQL version 3:** `rdsproxyadmin` is a reserved user name for RDS Proxy. However, the engine does not prevent you from creating, modifying, or dropping a database user with that name.

**Aurora MySQL version 8.4 (starting in 8.4.7):** `rdsproxyadmin` is a protected user. The engine rejects `CREATE`, `DROP`, `RENAME`, `GRANT`, `REVOKE`, and `SET PASSWORD` operations against `rdsproxyadmin` at any host. For the full list of rejected operations and example errors, see [Reserved users in Aurora MySQL](AuroraMySQL.Security.md#AuroraMySQL.Security.ReservedUsers).

If you created an `rdsproxyadmin` user in a version 3 cluster, see [Protected user enforcement for `rdsproxyadmin`](AuroraMySQL.Upgrade-v3-v84-security.md#AuroraMySQL.Upgrade-v3-v84-security.rdsproxyadmin) for pre-upgrade guidance.