# Using Password Policy for SQL Server logins on RDS for SQL Server

Amazon RDS allows you to set the password policy for your Amazon RDS DB instance running Microsoft SQL Server.
Use this to set complexity, length, and lockout requirements
for logins that use SQL Server Authentication to authenticate to your DB instance.

## Key terms

**Login**

In SQL Server, a server-level principal that can authenticate to a database instance is referred to as a **login**.
Other database engines might refer to this principal as a _user_.
In RDS for SQL Server, a login can authenticate using SQL Server Authentication or Windows Authentication.

**SQL Server login**

A login that uses a username and password to authenticate using SQL Server Authentication is a SQL Server login.
The password policy you configure through DB parameters only applies to SQL Server logins.

**Windows login**

A login that is based on a Windows principal and authenticates using Windows Authentication is a Windows login.
You can configure the password policy for your Windows logins in Active Directory.
For more information, see [Working with Active Directory with RDS for SQL Server](User.SQLServer.md "User.SQLServer.md").

## Enabling and disabling policy for each login

Each SQL Server login has flags for `CHECK_POLICY` and `CHECK_EXPIRATION`.
By default, new logins are created with `CHECK_POLICY`
set to `ON` and `CHECK_EXPIRATION` set to `OFF`.

If `CHECK_POLICY` is enabled for a login, RDS for SQL Server validates the password
against the complexity and minimum length requirements. Lockout policies also apply.
An example T-SQL statement to enable `CHECK_POLICY` and `CHECK_EXPIRATION`:

```
ALTER LOGIN [master_user] WITH CHECK_POLICY = ON, CHECK_EXPIRATION = ON;
```

If `CHECK_EXPIRATION` is enabled, passwords are subject to password age policies.
The T-SQL statement to check if `CHECK_POLICY` and `CHECK_EXPIRATION` are set:

```
SELECT name, is_policy_checked, is_expiration_checked FROM sys.sql_logins;
```

## Password policy parameters

All password policy parameters are dynamic and do not require DB reboot to take effect.
The following table lists the DB parameters you can set to modify the password policy for SQL Server logins:

| DB parameter                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Allowed Values | Default Value |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------- |
| rds.password_complexity_enabled          | Password complexity requirements must be satisfied<br>when creating or changing passwords for SQL Server logins.<br>The following constraints must be met:<br>• The password must include characters from three of the following categories:<br>+ Latin lowercase letter (a through z)<br>+ Latin uppercase letter (A through Z)<br>+ Non-alphanumeric characters such as: exclamation point (!), dollar sign ($), number sign (#), or percent (%).<br>• The password doesn't contain the account name of the user. | 0,1            | 0             |
| rds.password_min_length                  | The minimum number of characters required in a password for a SQL Server login.                                                                                                                                                                                                                                                                                                                                                                                                                                     | 0-14           | 0             |
| rds.password_min_age                     | The minimum number of days a SQL Server login password must be used before the user can change it.<br>Passwords can be changed immediately when set to 0.                                                                                                                                                                                                                                                                                                                                                           | 0-998          | 0             |
| rds.password_max_age                     | The maximum number of days a SQL Server login password can be used after which<br>the user is required to change it. Passwords never expire when set to 0.                                                                                                                                                                                                                                                                                                                                                          | 0-999          | 42            |
| rds.password_lockout_threshold           | The number of consecutive failed login attempts that cause a SQL Server login to become locked out.                                                                                                                                                                                                                                                                                                                                                                                                                 | 0-999          | 0             |
| rds.password_lockout_duration            | The number of minutes a locked out SQL Server login must wait before being unlocked.                                                                                                                                                                                                                                                                                                                                                                                                                                | 1-60           | 10            |
| rds.password_lockout_reset_counter_after | The number of minutes that must elapse after a failed login<br>attempt before the failed login attempt counter is reset to 0.                                                                                                                                                                                                                                                                                                                                                                                       | 1-60           | 10            |

###### Note

For more information about SQL Server password policy,
see [Password Policy](https://learn.microsoft.com/en-us/sql/relational-databases/security/password-policy "https://learn.microsoft.com/en-us/sql/relational-databases/security/password-policy").

The password complexity and minimum length policies
also apply to DB users in contained databases. For more information, see
[Contained Databases](https://learn.microsoft.com/en-us/sql/relational-databases/databases/contained-databases "https://learn.microsoft.com/en-us/sql/relational-databases/databases/contained-databases").

The following constraints apply to the password policy parameters:

- The `rds.password_min_age` parameter must be less than `rds.password_max_age parameter`,
  unless `rds.password_max_age` is set to 0
- The `rds.password_lockout_reset_counter_after` parameter must be
  less than or equal to the `rds.password_lockout_duration` parameter.
- If `rds.password_lockout_threshold` is set to 0,
  `rds.password_lockout_duration` and `rds.password_lockout_reset_counter_after` do not apply.

### Considerations for existing logins

After modifying the password policy on an instance, existing passwords for logins are
**not** retroactively evaluated
against the new password complexity and length requirements. Only new passwords are validated against the new policy.

SQL Server **does** evaluate existing passwords for age requirements.

It is possible for passwords to expire immediately once a password policy is modified.
For example, if a login has `CHECK_EXPIRATION` enabled and its password was last changed 100 days ago
and you set the `rds.password_max_age` parameter to 5 days,
the password immediately expires and the login needs to change their password at their next attempt to log in.

###### Note

RDS for SQL Server doesn't support password history policies. History policies prevent logins from reusing previously used passwords.

### Considerations for Multi-AZ deployments

The failed login attempt counter and lockout state for Multi-AZ instances does not replicate between nodes.
In the event of a login being locked out when a Multi-AZ instance fails over, it is possible for the login to
be already unlocked on the new node.
