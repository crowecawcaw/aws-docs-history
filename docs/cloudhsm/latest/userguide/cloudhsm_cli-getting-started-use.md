# Use the CloudHSM CLI

Use the following commands to start and use the CloudHSM CLI.

1. Use the following command to start CloudHSM CLI.

Linux

```
`$` `/opt/cloudhsm/bin/cloudhsm-cli interactive`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive`
```

2. Use the **login** command to log in to the cluster. All users can use this command.

The command in the following example logs in _admin_,
which is the default [admin](understanding-users.md "understanding-users.md") account. You set
this user's password when you [activated the cluster](activate-cluster.md "activate-cluster.md").

```
`aws-cloudhsm >` `login --username admin --role admin`
```

The system prompts you for your password. You enter the password, and the output shows that the command was successful.

```
`Enter password:
{
 "error_code": 0,
 "data": {
 "username": "admin",
 "role": "admin"
 }
}`
```

3. Run the **user list** command to list all the users on the cluster.

```
`aws-cloudhsm >` `user list``{
 "error_code": 0,
 "data": {
 "users": [
 {
 "username": "admin",
 "role": "admin",
 "locked": "false",
 "mfa": [],
 "cluster-coverage": "full"
 },
 {
 "username": "app_user",
 "role": "internal(APPLIANCE_USER)",
 "locked": "false",
 "mfa": [],
 "cluster-coverage": "full"
 }
 ]
 }
}`
```

4. Use **user create** to create a CU user named
   `example_user`.

You can create CUs because in a previous step you logged in as an admin user.
Only admin users can perform user management tasks, such as creating and deleting users and changing the passwords of other users.

```
`aws-cloudhsm >` `user create --username example_user --role crypto-user` `Enter password:
Confirm password:
{
 "error_code": 0,
 "data": {
 "username": "example_user",
 "role": "crypto-user"
 }
}`
```

5. Use **user list** to list all the users on the cluster.

```
`aws-cloudhsm >` `user list``{
 "error_code": 0,
 "data": {
 "users": [
 {
 "username": "admin",
 "role": "admin",
 "locked": "false",
 "mfa": [],
 "cluster-coverage": "full"
 },
 {
 "username": "example_user",
 "role": "crypto_user",
 "locked": "false",
 "mfa": [],
 "cluster-coverage": "full"
 },
 {
 "username": "app_user",
 "role": "internal(APPLIANCE_USER)",
 "locked": "false",
 "mfa": [],
 "cluster-coverage": "full"
 }
 ]
 }
}`
```

6. Use the **logout** command to log out of AWS CloudHSM cluster.

```
`aws-cloudhsm >` `logout``{
 "error_code": 0,
 "data": "Logout successful"
}`
```

7. Use the **quit** command to stop the CLI.

```
`aws-cloudhsm >` `quit`
```
