# Password validation for

RDS for MySQL

MySQL provides the `validate_password` plugin for improved security. The plugin
enforces password policies using parameters in the DB parameter group for your MySQL DB
instance. The plugin is supported for DB instances running MySQL version 5.7, 8.0, and 8.4.
For more information about the `validate_password` plugin, see [The Password
Validation Plugin](https://dev.mysql.com/doc/refman/5.7/en/validate-password.html "https://dev.mysql.com/doc/refman/5.7/en/validate-password.html") in the MySQL documentation.

###### To enable the `validate_password` plugin for a MySQL DB instance

1. Connect to your MySQL DB instance and run the following command.

```

INSTALL PLUGIN validate_password SONAME 'validate_password.so';

```

2. Configure the parameters for the plugin in the DB parameter group used by the DB
   instance.

For more information about the parameters, see [Password Validation Plugin Options and Variables](https://dev.mysql.com/doc/refman/5.7/en/validate-password-options-variables.html "https://dev.mysql.com/doc/refman/5.7/en/validate-password-options-variables.html") in the MySQL
documentation.

For more information about modifying DB instance parameters, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 3. Restart the DB instance.
After enabling the `validate_password` plugin, reset existing passwords to
comply with your new validation policies.

Your MySQL DB instance handles password validation for Amazon RDS. To change a password,
you first submit a password update request through the AWS Management Console, `modify-db-instance` CLI command,
or `ModifyDBInstance` API operation. RDS initially accepts your request, even if the password doesn't meet your policies.
RDS then processes the request asynchronously. It updates the password in your MySQL DB instance only if the password
meets your defined policies. If the password doesn't meet these policies, RDS keeps the existing password and logs an
error event.

```

    Unable to reset your password. Error information: Password failed to meet validation rules.

```

For more information about Amazon RDS events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").
