# Change a user's MFA setup with

CloudHSM CLI

Use the **user change-mfa token-sign** command in CloudHSM CLI to update a user
account's multi-factor authentication (MFA) setup. Any user account can run this command.
Accounts with the Admin role can run this command for other users.

## User type

The following users can run this command.

- Admin
- Crypto user

## Syntax

Currently, there is only a single multi-factor strategy available for users: Token Sign.

```
`aws-cloudhsm >` `help user change-mfa`
Change a user's Mfa Strategy

Usage:
    user change-mfa <COMMAND>

Commands:
  token-sign  Register or Deregister a public key using token-sign mfa strategy
  help        Print this message or the help of the given subcommand(s)

```

The Token Sign strategy asks for a Token file to write unsigned tokens to.

```
`aws-cloudhsm >` `help user change-mfa token-sign``Register or Deregister a public key using token-sign mfa strategy

Usage: user change-mfa token-sign [OPTIONS] --username `<USERNAME>` --role `<ROLE>` <--token `<TOKEN>`|--deregister>

Options:
 --cluster-id `<CLUSTER_ID>`
 Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error

 --username `<USERNAME>`
 Username of the user that will be modified

 --role `<ROLE>`
 Role the user has in the cluster

 Possible values:
 - crypto-user: A CryptoUser has the ability to manage and use keys
 - admin: An Admin has the ability to manage user accounts

 --change-password `<CHANGE_PASSWORD>`
 Optional: Plaintext user's password. If you do not include this argument you will be prompted for it

 --token `<TOKEN>`
 Filepath where the unsigned token file will be written. Required for enabling MFA for a user

 --approval `<APPROVAL>`
 Filepath of signed quorum token file to approve operation

 --deregister
 Deregister the MFA public key, if present

 --change-quorum
 Change the Quorum public key along with the MFA key

 -h, --help
 Print help (see a summary with '-h')`
```

## Example

This command will write one unsigned token per HSM in your cluster to the file specified by `token`. When you are prompted, sign the tokens in the file.

###### Example : Write one unsigned token per HSM in your cluster

```
`aws-cloudhsm >` `user change-mfa token-sign --username cu1 --change-password password --role crypto-user --token /path/myfile``Enter signed token file path (press enter if same as the unsigned token file):
Enter public key PEM file path:/path/mypemfile
{
 "error_code": 0,
 "data": {
 "username": "test_user",
 "role": "admin"
 }
}`
```

### Arguments

**`<CLUSTER_ID>`**

The ID of the cluster to run this operation on.

Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md "cloudhsm_cli-configs-multi-cluster.md")

**`<ROLE>`**

Specifies the role given to the user account. This parameter is required. For detailed information about the user types on an HSM, see [Understanding HSM users](manage-hsm-users.md "manage-hsm-users.md").

**Valid values**

- **Admin**: Admins can manage users, but they cannot manage keys.

- **Crypto user**: Crypto users can create an manage keys and use keys in cryptographic operations.

**`<USERNAME>`**

Specifies a friendly name for the user. The maximum length is 31 characters. The only special character permitted is an underscore ( \_ ).

You cannot change the name of a user after it is created. In CloudHSM CLI commands, the role and password are case-sensitive, but the username is not.

**Required**: Yes

**`<CHANGE_PASSWORD>`**

Specifies the plaintext new password of the user whose MFA is being registered/deregistered.

**Required**: Yes

**`<TOKEN>`**

File path where the unsigned token file will be written.

**Required**: Yes

**`<APPROVAL>`**

Specifies the file path to a signed quorum token file to approve operation. Only required if quorum user service quorum value is greater than 1.

**`<DEREGISTER>`**

Deregisters the MFA public key, if present.

**`<CHANGE-QUORUM>`**

Changes the quorum public key along with the MFA key.

## Related topics

- [Understanding 2FA for HSM users](login-mfa-token-sign.md "login-mfa-token-sign.md")
