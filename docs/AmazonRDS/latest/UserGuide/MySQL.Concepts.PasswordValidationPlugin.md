

# Password validation for RDS for MySQL

MySQL provides the `validate_password` plugin for improved security. The plugin enforces password policies using parameters in the DB parameter group for your MySQL DB instance. The plugin is supported for DB instances running MySQL version 5.7, 8.0, and 8.4. For more information about the `validate_password` plugin, see [The Password Validation Plugin](https://dev.mysql.com/doc/refman/5.7/en/validate-password.html) in the MySQL documentation. 

The `validate_password` plugin is removed in MySQL 9.7, and you can't install it on DB instances running MySQL 9.7. To turn on password validation for these DB instances, use the `rds.validate_password` parameter. For more information, see [Using password validation for MySQL 9.7](#MySQL.Concepts.PasswordValidationPlugin.9-7).

**To enable the `validate_password` plugin for a MySQL 8.4 or lower DB instance**

1. Connect to your MySQL DB instance and run the following command.

   ```sql
   INSTALL PLUGIN validate_password SONAME 'validate_password.so';                    
   ```

1. Configure the parameters for the plugin in the DB parameter group used by the DB instance.

   For more information about the parameters, see [Password Validation Plugin Options and Variables](https://dev.mysql.com/doc/refman/5.7/en/validate-password-options-variables.html) in the MySQL documentation.

   For more information about modifying DB instance parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.Modifying.md).

1. Restart the DB instance.

After enabling the `validate_password` plugin, reset existing passwords to comply with your new validation policies.

Your MySQL DB instance handles password validation for Amazon RDS. To change a password, you first submit a password update request through the AWS Management Console, `modify-db-instance` CLI command, or `ModifyDBInstance` API operation. RDS initially accepts your request, even if the password doesn't meet your policies. RDS then processes the request asynchronously. It updates the password in your MySQL DB instance only if the password meets your defined policies. If the password doesn't meet these policies, RDS keeps the existing password and logs an error event.

```
    Unable to reset your password. Error information: Password failed to meet validation rules.            
```

For more information about Amazon RDS events, see [Working with Amazon RDS event notification](USER_Events.md).

## Using password validation for MySQL 9.7
<a name="MySQL.Concepts.PasswordValidationPlugin.9-7"></a>

The `validate_password` plugin is removed in MySQL 9.7, and you can't install it. To turn on password validation for MySQL 9.7, set the `rds.validate_password` parameter in the DB parameter group for your DB instance. The `rds.validate_password` parameter isn't set by default, so password validation is off.

**To enable the `validate_password` component for a MySQL 9.7 DB instance**

1. Set the `rds.validate_password` parameter to `ON` in the custom DB parameter group that your DB instance uses.

   For more information about modifying DB instance parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.Modifying.md).

1. (Optional) Configure the parameters for the component in the same custom DB parameter group. The component parameters use dot notation, such as `validate_password.length`, `validate_password.policy`, `validate_password.changed_characters_percentage`, and `validate_password.check_user_name`.

   For more information about the parameters, see [Password Validation Options and Variables](https://dev.mysql.com/doc/refman/9.7/en/validate-password-options-variables.html) in the MySQL documentation.

After you enable the `validate_password` component, reset existing passwords to comply with your new validation policies.

To turn off the `validate_password` component, set the `rds.validate_password` parameter to `OFF` in the custom DB parameter group that your DB instance uses.

When you upgrade a DB instance from MySQL 8.4 to MySQL 9.7, the `validate-password` and `validate_password_*` parameters from MySQL 8.4 don't apply. In your custom DB parameter group for MySQL 9.7, use `rds.validate_password` and the `validate_password.*` parameters instead.

The upgrade to MySQL 9.7 removes the `validate_password` plugin, and the upgrade precheck reports a warning if the plugin is installed. After the upgrade, password validation is off until you set `rds.validate_password` to `ON` in the DB parameter group for MySQL 9.7.