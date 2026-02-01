# Log in to an HSM using CloudHSM CLI

You can use the **login** command in CloudHSM CLI to log in and out of each
hardware security (HSM) in a AWS CloudHSM cluster. This command has the following
sub-command:

- [mfa-token-sign](cloudhsm_cli-login-mfa-token-sign.md "cloudhsm_cli-login-mfa-token-sign.md")

###### Note

If you exceed five incorrect login attempts, your account is locked out. To unlock the
account, an admin must reset your password using the [user change-password](cloudhsm_cli-user-change-password.md "cloudhsm_cli-user-change-password.md") command in
cloudhsm_cli.

If you have more than one HSM in your cluster, you may be allowed additional
incorrect login attempts before your account is locked out. This is because the
CloudHSM client balances load across various HSMs. Therefore, the login attempt may
not begin on the same HSM each time. If you are testing this functionality, we
recommend you do so on a cluster with only one active HSM.

If you created your cluster before February 2018, your account is locked out after
20 incorrect login attempts.

## User type

The following users can run these commands.

- Unactivated admin
- Admin
- Crypto user (CU)

## Syntax

```
`aws-cloudhsm >` `help login``Login to your cluster

USAGE:
 cloudhsm-cli login [OPTIONS] --username `<USERNAME>` --role `<ROLE>` [COMMAND]

Commands:
 mfa-token-sign Login with token-sign mfa
 help Print this message or the help of the given subcommand(s)

OPTIONS:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error

 --username `<USERNAME>`
 Username to access the Cluster

 --role `<ROLE>`
 Role the user has in the Cluster

 Possible values:
 - crypto-user: A CryptoUser has the ability to manage and use keys
 - admin: An Admin has the ability to manage user accounts

 --password `<PASSWORD>`
 Optional: Plaintext user's password. If you do not include this argument you will be prompted for it

 -h, --help
 Print help (see a summary with '-h')`
```

## Example

This command logs you in to all HSMs in a cluster with the credentials of an admin
user named `admin1`.

```
`aws-cloudhsm >` `login --username admin1 --role admin`
Enter password:
`{
 "error_code": 0,
 "data": {
 "username": "admin1",
 "role": "admin"
 }
}`
```

## Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<USERNAME>`**

Specifies a friendly name for the user. The maximum length is 31 characters. The only special character permitted is an underscore ( \_ ). The username is not case sensitive in this command, username is always displayed in lowercase.

Required: Yes

**`<ROLE>`**

Specifies the role assigned to this user.
Valid values are **admin**, **crypto-user**.

To get the user's role, use the **user list** command. For detailed information about the user types on an HSM, see [Understanding HSM users](manage-hsm-users.md "manage-hsm-users.md").

Required: Yes

**`<PASSWORD>`**

Specifies the password of the user who is logging in to the HSMs.

Required: Customers must provide the password either via the `--password` command line argument or omit it to be prompted interactively.

###### Note

Using the `--password` argument on the command line may expose credentials in your shell history. Consider prompting the password interactively or clear your shell history after use.

## Related topics

- [Getting Started with
  CloudHSM CLI](cloudhsm_cli-getting-started.md "cloudhsm_cli-getting-started.md")
- [Activate the
  Cluster](activate-cluster.md "activate-cluster.md")
