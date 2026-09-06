

# Password policies and Password validation in Aurora MySQL
<a name="AuroraMySQL.PasswordPolicies"></a>

**Topics**
+ [Password policies](#AuroraMySQL.PasswordPolicies.overview)
+ [Using the validate\_password component](#AuroraMySQL.PasswordPolicies.validate-password)
+ [Related documentation](#AuroraMySQL.PasswordPolicies.related)

## Password policies
<a name="AuroraMySQL.PasswordPolicies.overview"></a>

Aurora MySQL supports the following MySQL password policy features. For more information on these policies, see [MySQL Password Management documentation](https://dev.mysql.com/doc/refman/8.4/en/password-management.html).

### Password expiration
<a name="AuroraMySQL.PasswordPolicies.expiration"></a>


**Password expiration parameters**  

| Parameter/Clause | Notes | 
| --- | --- | 
| Cluster parameter `default_password_lifetime` | Available in Aurora MySQL version 3 (compatible with MySQL 8.0) and higher. | 
| Per account DCL clause `PASSWORD EXPIRE INTERVAL N DAY` | None | 
| Per account DCL clause `PASSWORD EXPIRE NEVER` | None | 
| Per account DCL clause `PASSWORD EXPIRE DEFAULT` | None | 
| Cluster parameter `disconnect_on_expired_password` | Available in Aurora MySQL version 8.4 and higher. | 

### Password reuse restrictions
<a name="AuroraMySQL.PasswordPolicies.reuse"></a>


**Password reuse restriction parameters**  

| Parameter/Clause | Notes | 
| --- | --- | 
| Cluster parameter `password_history` | Available in Aurora MySQL version 8.4 and higher. | 
| Cluster parameter `password_reuse_interval` | Available in Aurora MySQL version 8.4 and higher. | 
| Per account DCL clause `PASSWORD HISTORY N` | None | 
| Per account DCL clause `PASSWORD REUSE INTERVAL N DAY` | None | 
| Per account DCL clause `PASSWORD HISTORY DEFAULT` | None | 

### Current password verification
<a name="AuroraMySQL.PasswordPolicies.current-verification"></a>


**Current password verification parameters**  

| Parameter/Clause | Notes | 
| --- | --- | 
| Parameter `password_require_current` | Available in Aurora MySQL version 8.4 and higher. | 
| Per account DCL clause `PASSWORD REQUIRE CURRENT` | None | 
| Per account DCL clause `PASSWORD REQUIRE CURRENT OPTIONAL` | None | 
| Per account DCL clause `PASSWORD REQUIRE CURRENT DEFAULT` | None | 

### Dual password support
<a name="AuroraMySQL.PasswordPolicies.dual-password"></a>


**Dual password support clauses**  

| Parameter/Clause | Notes | 
| --- | --- | 
| Per account DCL clause `RETAIN CURRENT PASSWORD` | None | 
| Per account DCL clause `DISCARD OLD PASSWORD` | None | 

### Failed-login tracking and temporary account locking
<a name="AuroraMySQL.PasswordPolicies.failed-login"></a>


**Failed-login tracking clauses**  

| Parameter/Clause | Notes | 
| --- | --- | 
| Per account DCL clause `FAILED_LOGIN_ATTEMPTS N` | None | 
| Per account DCL clause `PASSWORD_LOCK_TIME N` | None | 
| Per account DCL clause `PASSWORD_LOCK_TIME UNBOUNDED` | None | 

## Using the validate\_password component
<a name="AuroraMySQL.PasswordPolicies.validate-password"></a>

The `validate_password` component is a MySQL server component that provides password strength validation and enforcement capabilities. It tests passwords against configurable rules to ensure they meet the specified security requirements before being accepted. 

When enabled, the `validate_password` component automatically validates passwords during:
+ User account creation (`CREATE USER`)
+ Password changes (`ALTER USER`, `SET PASSWORD`)

This helps organizations maintain strong password hygiene across their database users and comply with security policies and regulatory requirements.

Aurora MySQL version 8.4 provides a parameter-based approach to enable and manage the `validate_password` component, eliminating the need for manual `INSTALL COMPONENT` and `UNINSTALL COMPONENT` commands.

### Enabling the validate\_password component
<a name="AuroraMySQL.PasswordPolicies.validate-password.enabling"></a>

To enable password validation in your Aurora MySQL cluster, use the cluster parameter:

Parameter name: `aurora_enable_validate_password_component`

To enable: Set `aurora_enable_validate_password_component` to `true` (or `1`) in your DB cluster parameter group.

To disable: Set `aurora_enable_validate_password_component` to `false` (or `0`) in your DB cluster parameter group.

**Note**  
You will not be able to use the `INSTALL/UNINSTALL COMPONENT` commands for the `validate_password` component.

**Note**  
Starting from Aurora MySQL version 8.4, the `validate_password` component is not listed in the `mysql.component` table. You can see the status of the component in your DB cluster parameter group or through the global variable `aurora_enable_validate_password_component`:  

```
SELECT @@global.aurora_enable_validate_password_component;
```

### Supported validate\_password component parameters
<a name="AuroraMySQL.PasswordPolicies.validate-password.parameters"></a>


**validate\_password component parameters**  

| Parameter name | Notes | 
| --- | --- | 
| `validate_password.check_user_name` | Available in Aurora MySQL version 8.4 and higher. | 
| `validate_password.length` | Available in Aurora MySQL version 8.4 and higher. | 
| `validate_password.mixed_case_count` | Available in Aurora MySQL version 8.4 and higher. | 
| `validate_password.number_count` | Available in Aurora MySQL version 8.4 and higher. | 
| `validate_password.policy` | Available in Aurora MySQL version 8.4 and higher. Only LOW and MEDIUM levels are supported. | 
| `validate_password.special_char_count` | Available in Aurora MySQL version 8.4 and higher. | 

For more information on MySQL validate\_password parameters, see [MySQL Password Validation Options and Variables documentation](https://dev.mysql.com/doc/refman/8.4/en/validate-password-options-variables.html).

### validate\_password plugin and component migration from RDS for MySQL or Aurora MySQL version 3 to Aurora MySQL version 8.4
<a name="AuroraMySQL.PasswordPolicies.validate-password.migration"></a>

Starting from Aurora MySQL version 8.4, if you had previously installed the `validate_password` plugin through the `INSTALL PLUGIN` command, you can migrate to the `validate_password` component. Enable the parameter `aurora_enable_validate_password_component` and then remove the plugin through the `UNINSTALL PLUGIN` command on your writer instance.

**Note**  
If you have both the plugin installed and the parameter `aurora_enable_validate_password_component` enabled, the `validate_password` component will take precedence over the plugin.

If you previously installed the `validate_password` component manually using `INSTALL COMPONENT 'file://component_validate_password'`, set the `aurora_enable_validate_password_component` parameter in your target DB cluster parameter group when upgrading. After upgrading, the component will no longer be listed in the `mysql.component` table. You can use the `aurora_enable_validate_password_component` global variable to verify the status of the component.

On the first DB engine startup after upgrade, you will see the following message in your MySQL error log if you had previously installed the component manually:

```
Component 'file://component_validate_password' is being removed from mysql.component table.
validate_password component can be enabled/disabled through 'aurora_enable_validate_password_component' cluster parameter.
```

### Manual installation restrictions
<a name="AuroraMySQL.PasswordPolicies.validate-password.restrictions"></a>

Starting Aurora MySQL version 8.4 releases, manual `validate_password` component install and uninstall commands are not allowed:

```
mysql> INSTALL COMPONENT 'file://component_validate_password';
ERROR HY000: Cannot load component from specified URN: 'validate_password component can be
enabled/disabled through 'aurora_enable_validate_password_component' cluster parameter.'
```

### Monitoring component status
<a name="AuroraMySQL.PasswordPolicies.validate-password.monitoring"></a>

Aurora MySQL logs component state changes to the MySQL error log:

When enabled:

```
Component 'validate_password' is enabled by parameter aurora_enable_validate_password_component
```

When disabled:

```
Component 'validate_password' is disabled by parameter aurora_enable_validate_password_component
```

### Password validation impact on master user password
<a name="AuroraMySQL.PasswordPolicies.validate-password.master-user"></a>

When resetting the master user password through the `modify-db-cluster` API, if the new password does not comply with the configured password validation rules, Aurora MySQL emits a customer-visible event indicating the failure. You must retry the operation with a compliant password.

### Password validation impact on Amazon RDS managed master user password
<a name="AuroraMySQL.PasswordPolicies.validate-password.managed-password"></a>

For clusters using Amazon RDS-managed master user credentials stored in AWS Secrets Manager, if the automatically generated password during rotation does not comply with the configured validation requirements, the rotation will fail. Adjust your password validation parameters to allow the rotation to succeed. We suggest not using the `validate_password` component and managed master user password together.

## Related documentation
<a name="AuroraMySQL.PasswordPolicies.related"></a>
+ [Aurora MySQL configuration parameters](AuroraMySQL.Reference.ParameterGroups.md)
+ [Security with Amazon Aurora MySQL](AuroraMySQL.Security.md)
+ [MySQL validate\_password Component Documentation](https://dev.mysql.com/doc/refman/8.4/en/validate-password.html)
+ [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md)