# Delete an AWS CloudHSM user with CloudHSM CLI

The **user delete** command in CloudHSM CLI deletes a user from your AWS CloudHSM cluster. Only user accounts with the admin role may run this command. You cannot delete a user
 who is currently logged into an HSM. 


## User type


The following types of users can run this command.



* Admin

## Requirements



* You can't delete user accounts that own keys.
* Your user account must have the admin role to run this command.

## Syntax

 Because this command does not have named parameters, you must enter the arguments in the
 order specified in the syntax diagram.



```
`aws-cloudhsm >` `help user delete``Delete a user

Usage: user delete [OPTIONS] --username `<USERNAME>` --role `<ROLE>`

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error

 --username `<USERNAME>`
 Username to access the HSM cluster

 --role `<ROLE>`
 Role the user has in the cluster

 Possible values:
 - crypto-user: A CryptoUser has the ability to manage and use keys
 - admin: An Admin has the ability to manage user accounts

 --approval `<APPROVAL>`
 Filepath of signed quorum token file to approve operation`
```

## Example



```
`aws-cloudhsm >` `user delete --username alice --role crypto-user``{
 "error_code": 0,
 "data": {
 "username": "alice",
 "role": "crypto-user"
 }
}`
```

## Arguments




**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.


Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")



**`<USERNAME>`**

Specifies a friendly name for the user. The maximum length is 31 characters. The only special character permitted is an underscore ( \_ ). 
 The username is not case sensitive in this command, username is always displayed in lowercase.


Required: Yes



**`<ROLE>`**

Specifies the role assigned to this user. This parameter is required. 
 Valid values are **admin**, **crypto-user**.


To get the user’s role, use the **user list** command. For detailed information about the user types on an HSM, see [Understanding HSM users](manage-hsm-users.md "manage-hsm-users.md").


Required: Yes



**`<APPROVAL>`**

Specifies the file path to a signed quorum token file to approve operation. Only required if quorum user service quorum value is greater than 1.


Required: Yes




## Related topics



* [user list](cloudhsm_cli-user-list.md "cloudhsm_cli-user-list.md")
* [user create](cloudhsm_cli-user-create.md "cloudhsm_cli-user-create.md")
* [user change-password](cloudhsm_cli-user-change-password.md "cloudhsm_cli-user-change-password.md")
