# Password considerations for the master login

When you create an RDS for SQL Server DB instance, the master user password is not evaluated against the password policy.
A new master password is also not evaluated against the password when performing operations
to the master user, specifically when setting `MasterUserPassword` in the `ModifyDBInstance` command.
In both cases, you can set a password for the master user that does not satisfy your password policy,
and the operation still succeeds. If the policy is not satisfied, RDS attempts to raise an RDS event,
with the recommendation to set a strong password. Take care to only use strong passwords for the master user.

RDS attempts to generate the following event messages when the master user password does not meet the password policy requirements:

- The master user was created, but the password doesn't meet the
  minimum length requirement of your password policy.
  Consider using a stronger password.
- The master user was created, but the password doesn't meet the
  complexity requirement of your password policy.
  Consider using a stronger password.
- The master user password was reset, but the password doesn't
  meet the minimum length requirement of your password policy.
  Consider using a stronger password.
- The master user password was reset, but the password doesn't
  meet the complexity requirement of your password policy.
  Consider using a stronger password.
  By default, the master user is created with `CHECK_POLICY`
  and `CHECK_EXPIRATION` set to `OFF`.
  To apply the password policy to the master user, you must manually enable these flags for
  the master user after DB instance creation. After you enable these flags, modify the master user
  password directly in SQL Server (eg. via T-SQL statements or SSMS) to validate the new password
  against the password policy.

###### Note

If the master user gets locked out, you can unlock the user by resetting
the master user password using the `ModifyDBInstance` command.

## Modifying the master user password

You can modify the master user password by using the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") command.

###### Note

When you reset the master user password, RDS resets various permissions
for the master user and the master user might lose certain permissions.
Resetting the master user password also unlocks the master user, if it was locked out.

RDS validates the new master user password and attempts to emit an RDS event
if the password does not satisfy the policy.
RDS sets the password even if it does not satisfy the password policy.
