# Log in with MFA to an HSM using

CloudHSM CLI

Use the **login mfa-token-sign** command in AWS CloudHSM CloudHSM CLI to log in
to a hardware security module (HSM) using multi-factor authentication (MFA). To use this
command, you must first set up [MFA for
CloudHSM CLI](login-mfa-token-sign.md "login-mfa-token-sign.md").

## User type

The following users can run these commands.

- Admin
- Crypto user (CU)

## Syntax

```
`aws-cloudhsm >` `help login mfa-token-sign``Login with token-sign mfa

USAGE:
 login --username `<username>` --role `<role>` mfa-token-sign --token `<token>`

OPTIONS:
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 --token `<TOKEN>` Filepath where the unsigned token file will be written
 -h, --help Print help`
```

## Example

###### Example

```
`aws-cloudhsm >` `login --username test_user --role admin mfa-token-sign --token /home/valid.token``Enter password:
Enter signed token file path (press enter if same as the unsigned token file):
{
 "error_code": 0,
 "data": {
 "username": "test_user",
 "role": "admin"
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<TOKEN>`**

Filepath where the unsigned token file will be written.

Required: Yes

## Related topics

- [Getting Started with
  CloudHSM CLI](cloudhsm_cli-getting-started.md "cloudhsm_cli-getting-started.md")
- [Activate the
  Cluster](activate-cluster.md "activate-cluster.md")
- [Using CloudHSM CLI to manage MFA](login-mfa-token-sign.md "login-mfa-token-sign.md")
