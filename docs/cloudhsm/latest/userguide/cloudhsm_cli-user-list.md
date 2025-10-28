# List all AWS CloudHSM users with CloudHSM CLI

The **user list** command in the CloudHSM CLI lists the user accounts present
in your AWS CloudHSM cluster. You do not need to be logged in to CloudHSM CLI to run this command.

###### Note

If you add or delete HSMs, update the
configuration files that the AWS CloudHSM client and the command line tools use.
Otherwise, the changes that you make might not be effective on all HSMs in the
cluster.

## User type

The following types of users can run this command.

- All users. You do not need to be logged in to run this command.

## Syntax

```
`aws-cloudhsm >` `help user list``List the users in your cluster

USAGE:
 user list

Options:
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 -h, --help Print help`
```

## Example

This command lists the users present in your CloudHSM cluster.

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
 "username": "test_user",
 "role": "admin",
 "locked": "false",
 "mfa": [
 {
 "strategy": "token-sign",
 "status": "enabled"
 }
 ],
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

The output includes the following user attributes:

- **Username**: Displays the user-defined friendly name for the user. Username is always displayed in lowercase.
- **Role**: Determines the operations that the user can perform on the HSM.
- **Locked**: Indicates whether this user account has been locked out.
- **MFA**: Indicates the supported multi-factor authentication mechanisms for this user account.
- **Cluster coverage**: Indicates the cluster-wide availability of this user account.

## Related topics

- [listUsers](key_mgmt_util-listUsers.md "key_mgmt_util-listUsers.md") in key_mgmt_util
- [user create](cloudhsm_cli-user-create.md "cloudhsm_cli-user-create.md")
- [user delete](cloudhsm_cli-user-delete.md "cloudhsm_cli-user-delete.md")
- [user change-password](cloudhsm_cli-user-change-password.md "cloudhsm_cli-user-change-password.md")
