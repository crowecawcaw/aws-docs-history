# Change HSM user passwords using

CloudHSM CLI

Use the **user change-password** command in the CloudHSM CLI to change
a hardware security module (HSM) user's password.

User types and passwords are
case sensitive, but user names are not case sensitive.

Admin, crypto user (CU), and appliance user (AU) can change their own password. To change the
password of another user, you must log in as an admin. You cannot change the password of a user who
is currently logged in.

###### To change your own password

1. Use the following command to start CloudHSM CLI interactive mode.

Linux

```
`$` `/opt/cloudhsm/bin/cloudhsm-cli interactive`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive`
```

2. Use the **login** command and log in as the user with the password you want to change.

```
`aws-cloudhsm >` `login --username `<username>` --role `<role>``
```

3. Enter the user's password.

```
`Enter password:
{
 "error_code": 0,
 "data": {
 "username": "`<username>`",
 "role": "`<role>`"
 }
}`
```

4. Enter the **user change-password** command.

```
`aws-cloudhsm >` `user change-password --username `<username>` --role `<role>``
```

5. Enter the new password.
6. Re-enter the new password.

###### To change the password of another user

1. Use the following command to start CloudHSM CLI interactive mode.

Linux

```
`$` `/opt/cloudhsm/bin/cloudhsm-cli interactive`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive`
```

2. Using CloudHSM CLI, log in as an admin.

```
`aws-cloudhsm >` `login --username `<admin>` --role admin``Enter password:
{
 "error_code": 0,
 "data": {
 "username": "`<admin>`",
 "role": "admin"
 }
}`
```

3. Enter the **user change-password** command along with the username of the user whose password you want to change.

```
`aws-cloudhsm >` `user change-password --username `<username>` --role `<role>``
```

4. Enter the new password.
5. Re-enter the new password.
   For more information about **user change-password**, see [user change-password](cloudhsm_cli-user-change-password.md "cloudhsm_cli-user-change-password.md").
