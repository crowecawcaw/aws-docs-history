# Using the password validation plugins for RDS for MariaDB

Starting with RDS for MariaDB version 11.4, you can use the following password validation
plugins to enhance the security of your database connections:

- [simple\_password\_check](https://mariadb.com/kb/en/simple-password-check-plugin/ "https://mariadb.com/kb/en/simple-password-check-plugin/") – checks whether a password contains at
  least a specific number of characters of a specific type.
- [cracklib\_password\_check](https://mariadb.com/kb/en/cracklib_password_check/ "https://mariadb.com/kb/en/cracklib_password_check/") – checks whether a password appears in a dictionary file of the
  [CrackLib](https://github.com/cracklib/cracklib "https://github.com/cracklib/cracklib") library.
  To enable these plugins, set the value of the parameter `simple_password_check`
  or `cracklib_password_check` to `FORCE_PLUS_PERMANENT` in the DB
  parameter group associated with the DB instance. When this value is set, the plugin can't be
  uninstalled by using the `UNINSTALL PLUGIN` statement at runtime.

To disable these plugins, set the value of the parameter
`simple_password_check` or `cracklib_password_check` to
`OFF` in the DB parameter group associated with the DB instance. When this
value is set, the plugin validation rules no longer apply for new passwords.

For information about setting the values of parameters in parameter groups, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.Modifying.md "USER_WorkingWithParamGroups.Modifying.md").

After enabling the plugin, reset existing passwords to comply with your new validation
policies.

Your MariaDB DB instance handles password validation for Amazon RDS. To change a password, you
first submit a password update request through the AWS Management Console, `modify-db-instance`
AWS CLI command, or `ModifyDBInstance` API operation. Amazon RDS initially accepts your
request, even if the password doesn't meet your policies. Amazon RDS then processes the request
asynchronously. It updates the password in your MariaDB DB instance only if the password
meets your defined policies. If the password doesn't meet these policies, Amazon RDS keeps the
existing password and logs an error event.

```

    Unable to reset your password. Error information: Password failed to meet validation rules.

```

For more information about Amazon RDS events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").
