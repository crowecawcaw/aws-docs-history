

# Security considerations for upgrading from Aurora MySQL version 3 to version 8.4
<a name="AuroraMySQL.Upgrade-v3-v84-security"></a>

When migrating from Aurora MySQL version 3 (MySQL 8.0-compatible) to Aurora MySQL version 8.4, several important security-related changes require careful planning and consideration. This guide outlines the key security changes and provides recommendations for a smooth migration.

**Topics**
+ [Authentication policy (new in 8.4)](#AuroraMySQL.Upgrade-v3-v84-security.auth-policy)
+ [Master user behavior](#AuroraMySQL.Upgrade-v3-v84-security.master-user)
+ [Encryption and TLS changes](#AuroraMySQL.Upgrade-v3-v84-security.tls)
+ [Password validation component migration](#AuroraMySQL.Upgrade-v3-v84-security.validate-password)
+ [New dynamic privileges](#AuroraMySQL.Upgrade-v3-v84-security.new-privileges)
+ [Protected user enforcement for `rdsproxyadmin`](#AuroraMySQL.Upgrade-v3-v84-security.rdsproxyadmin)

## Authentication policy (new in 8.4)
<a name="AuroraMySQL.Upgrade-v3-v84-security.auth-policy"></a>

Aurora MySQL version 3 (compatible with MySQL 8.0) uses the `default_authentication_plugin` parameter to configure the default authentication plugin used when creating database users. In Aurora MySQL version 8.4, this parameter is replaced with the `authentication_policy` parameter, set to `*:caching_sha2_password` by default.

Supported values in Aurora MySQL:
+ `*:caching_sha2_password` (Default value. Allows any single factor authentication plugin, using `caching_sha2_password` if none is specified)
+ `*:mysql_native_password` (Allows any single factor authentication plugin, using `mysql_native_password` if none is specified)

**Note**  
Multi-factor authentication configurations are not supported in Aurora MySQL version 8.4.

The upgrade precheck [deprecatedDefaultAuth](AuroraMySQL.upgrade-prechecks.descriptions.md#deprecatedDefaultAuth) warns if your source cluster has `default_authentication_plugin` set to `mysql_native_password`. Review this warning and configure the `authentication_policy` parameter on your target cluster parameter group when upgrading.

## Master user behavior
<a name="AuroraMySQL.Upgrade-v3-v84-security.master-user"></a>

### New clusters
<a name="AuroraMySQL.Upgrade-v3-v84-security.master-user.new-clusters"></a>

The master user is created with the authentication plugin set by the `authentication_policy` parameter at cluster creation time. If you use the default parameter group, the master user is created with `caching_sha2_password` authentication plugin. If you use a custom parameter group with the `authentication_policy` parameter set to `*:mysql_native_password`, the master user is created with `mysql_native_password` authentication plugin.

### Master user password reset
<a name="AuroraMySQL.Upgrade-v3-v84-security.master-user.password-reset"></a>

When you reset the master user password – via the AWS Management Console, CLI (`modify-db-cluster --master-user-password`), or API – Aurora uses the current default plugin defined by the `authentication_policy` parameter at the time of reset.

### Secrets Manager and password rotation
<a name="AuroraMySQL.Upgrade-v3-v84-security.master-user.secrets-manager"></a>

When using AWS Secrets Manager to manage your master user password, if you update the value of the `authentication_policy` parameter, the next password rotation will set the master user's authentication plugin to match the new `authentication_policy` parameter value.

### Database users created after upgrade
<a name="AuroraMySQL.Upgrade-v3-v84-security.master-user.new-users"></a>

Existing database users that use the `mysql_native_password` authentication plugin continue to work after upgrade. Database users that you create after upgrade without specifying an `IDENTIFIED WITH` clause use the authentication plugin defined by the `authentication_policy` parameter. When the parameter is at its default value of `*:caching_sha2_password`, new users are created with the `caching_sha2_password` authentication plugin.

To change the default authentication plugin for all new users, update the value of `authentication_policy`. For more information about supported values, see [Authentication policy (new in 8.4)](#AuroraMySQL.Upgrade-v3-v84-security.auth-policy).

To create a user with a different authentication plugin than the default, specify it explicitly in the `CREATE USER` statement:

```
CREATE USER '{{username}}'@'{{host}}' IDENTIFIED WITH {{authentication-plugin}} BY '{{password}}';
```

## Encryption and TLS changes
<a name="AuroraMySQL.Upgrade-v3-v84-security.tls"></a>

To require TLS for all user connections to your Aurora MySQL DB cluster, use the `require_secure_transport` DB cluster parameter. By default, this parameter is set to `ON` in Aurora MySQL version 8.4.

Aurora MySQL version 8.4 enforces stricter cryptographic standards aligned with the latest security requirements on the `ssl_ciphers` (TLS 1.2) and `tls_ciphersuites` (TLS 1.3) DB cluster parameters. For more information, see [Security with Amazon Aurora MySQL](AuroraMySQL.Security.md).

To prevent connection disruptions, verify the TLS configurations for your MySQL client and your target DB cluster before migration.

## Password validation component migration
<a name="AuroraMySQL.Upgrade-v3-v84-security.validate-password"></a>

Aurora MySQL version 8.4 introduces the `aurora_enable_validate_password_component` cluster parameter to enable or disable the `validate_password` component. This removes the need to manually install or uninstall it. If you had previously installed the `validate_password` plugin and have since enabled the component after upgrading, only the component is effective – the plugin is ignored.

Starting from Aurora MySQL version 8.4, if you had previously installed the `validate_password` plugin through the `INSTALL PLUGIN` command, you can migrate to the `validate_password` component. Enable the parameter `aurora_enable_validate_password_component` and then remove the plugin through the `UNINSTALL PLUGIN` command on your writer instance.

If you previously installed the `validate_password` component manually using `INSTALL COMPONENT 'file://component_validate_password'`, set the `aurora_enable_validate_password_component` parameter in your target DB cluster parameter group when upgrading. After upgrading, the component will no longer be listed in the `mysql.component` table. You can use the `aurora_enable_validate_password_component` global variable to verify the status of the component.

On the first DB engine startup after upgrade, you will see the following message in your MySQL error log if you had previously installed the component manually:

```
Component 'file://component_validate_password' is being removed from mysql.component table.
validate_password component can be enabled/disabled through 'aurora_enable_validate_password_component' cluster parameter.
```

The upgrade precheck [auroraValidatePasswordPluginCheck](AuroraMySQL.upgrade-prechecks.descriptions.md#auroraValidatePasswordPluginCheck) warns if the `validate_password` plugin is installed on your source cluster. This warning does not block the upgrade, but you should plan to transition to the component after upgrading.

## New dynamic privileges
<a name="AuroraMySQL.Upgrade-v3-v84-security.new-privileges"></a>

Aurora MySQL version 8.4 supports the following new privileges:
+ `ALLOW_NONEXISTENT_DEFINER`
+ `FLUSH_PRIVILEGES`
+ `OPTIMIZE_LOCAL_TABLE`
+ `SET_ANY_DEFINER`

These privileges are automatically granted to the [Master user account privileges](UsingWithRDS.MasterAccounts.md) for your master user accounts on upgrade.

## Protected user enforcement for `rdsproxyadmin`
<a name="AuroraMySQL.Upgrade-v3-v84-security.rdsproxyadmin"></a>

Starting in Aurora MySQL version 8.4.7, `rdsproxyadmin` is a protected user. The engine rejects `CREATE`, `DROP`, `RENAME`, `GRANT`, `REVOKE`, and `SET PASSWORD` operations against `rdsproxyadmin` at any host. For the full list of rejected operations and example errors, see [Reserved users in Aurora MySQL](AuroraMySQL.Security.md#AuroraMySQL.Security.ReservedUsers).

Aurora MySQL version 3 does not reserve the `rdsproxyadmin` name. If you created a database user named `rdsproxyadmin` in version 3 (rather than letting the system create it when you register a proxy target), review this section before upgrading to version 8.4.

### Before you upgrade
<a name="AuroraMySQL.Upgrade-v3-v84-security.rdsproxyadmin.before-upgrade"></a>

If you created an `rdsproxyadmin` user in your version 3 cluster, rename or drop the account before you upgrade to version 8.4. You can use a version 3 connection to run one of the following statements:

```
-- Rename the existing account to a non-reserved name
RENAME USER 'rdsproxyadmin'@'{{host}}' TO '{{new_user}}'@'{{host}}';

-- Or drop the account if it is no longer needed
DROP USER 'rdsproxyadmin'@'{{host}}';
```

Update any applications or stored credentials that reference the old user name before starting the upgrade.

### If you don't rename or drop the user before upgrading
<a name="AuroraMySQL.Upgrade-v3-v84-security.rdsproxyadmin.after-upgrade"></a>

If you upgrade a cluster that already has an `rdsproxyadmin` user that you created, the upgrade completes successfully. The account is preserved with its existing password and privileges, and you can still connect to the cluster as `rdsproxyadmin` by using the original password.

However, after the upgrade, you can't modify the account. If you try to drop, rename, change privileges on, or change the password for `rdsproxyadmin`, the statement returns an error.

If you want to remove the account after the upgrade, or reclaim the `rdsproxyadmin` name for RDS Proxy to use, contact [AWS Support](https://aws.amazon.com/premiumsupport/). AWS Support can remove a pre-existing `rdsproxyadmin` user carried forward from version 3.