# Using the password validation plugins for RDS for MariaDB

Starting with RDS for MariaDB version 11.4, you can use the following password validation
plugins to enhance the security of your database connections:

- [simple_password_check](https://mariadb.com/kb/en/simple-password-check-plugin/ "https://mariadb.com/kb/en/simple-password-check-plugin/") – checks whether a password contains at
  least a specific number of characters of a specific type.
- [cracklib_password_check](https://mariadb.com/kb/en/cracklib_password_check/ "https://mariadb.com/kb/en/cracklib_password_check/") – checks whether a password appears in a dictionary file of the
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
