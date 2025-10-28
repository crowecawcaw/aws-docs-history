# Delete quorum tokens using CloudHSM CLI

Use the **quorum token-sign delete** command in CloudHSM CLI to delete one or more tokens for a quorum authorized service.

## User type

The following users can run this command.

- Admin

## Syntax

```
`aws-cloudhsm >` `help quorum token-sign delete` `Delete one or more Quorum Tokens

Usage: quorum token-sign delete --scope `<SCOPE>`

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error

 --scope `<SCOPE>`
 Scope of which token(s) will be deleted

 Possible values:
 - user: Deletes all token(s) of currently logged in user
 - all: Deletes all token(s) on the HSM
 -h, --help
 Print help (see a summary with '-h')`
```

## Example

The following example shows how the **quorum token-sign delete** command in CloudHSM CLI can be used to delete one or more tokens for a quorum authorized service.

###### Example : Delete one or more tokens for a quorum authorized service

```
`aws-cloudhsm >` `quorum token-sign delete --scope all``{
 "error_code": 0,
 "data": "Deletion of quorum token(s) successful"
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<SCOPE>`**

The scope in which token(s) will be deleted in the AWS CloudHSM cluster.

**Valid values**

- **User**: Used to delete only tokens owned by the logged in user.

- **All**: Used to delete all tokens in the AWS CloudHSM cluster.

## Related topics

- [user list](cloudhsm_cli-user-list.md "cloudhsm_cli-user-list.md")
- [user create](cloudhsm_cli-user-create.md "cloudhsm_cli-user-create.md")
- [user delete](cloudhsm_cli-user-delete.md "cloudhsm_cli-user-delete.md")
