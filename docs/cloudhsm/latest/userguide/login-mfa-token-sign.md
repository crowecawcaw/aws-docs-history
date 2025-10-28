# Manage MFA for HSM users using CloudHSM CLI

For increased security, you can configure multi-factor authentication (MFA) for users to
help protect the AWS CloudHSM cluster.

When you log in to a cluster with an MFA enabled hardware security module (HSM) user
account, you provide the CloudHSM CLI with your password—the first factor, what you know—and
CloudHSM CLI provides you with a token and prompts you to have the token signed.

To provide the second factor—what you have—you sign the token
with a private key from a key pair you've already created and associated with the HSM user. To access
the cluster, you provide the signed token to CloudHSM CLI.

For more information on setting up MFA for
a user see [Set up MFA for CloudHSM CLI](set-up-mfa-for-cloudhsm-cli.md "set-up-mfa-for-cloudhsm-cli.md")

The following topics provide more information about working with quorum authentication in AWS CloudHSM.

###### Topics

- [Quorum authentication](quorum-mfa-cloudhsm-cli.md "quorum-mfa-cloudhsm-cli.md")
- [Key pair requirements](mfa-key-pair-cloudhsm-cli.md "mfa-key-pair-cloudhsm-cli.md")
- [Set up MFA](set-up-mfa-for-cloudhsm-cli.md "set-up-mfa-for-cloudhsm-cli.md")
- [Create users](create-mfa-users-cloudhsm-cli.md "create-mfa-users-cloudhsm-cli.md")
- [Log in users](login-mfa-cloudhsm-cli.md "login-mfa-cloudhsm-cli.md")
- [Rotate keys](rotate-mfa-cloudhsm-cli.md "rotate-mfa-cloudhsm-cli.md")
- [Deregister an MFA public key](deregister-mfa-cloudhsm-cli.md "deregister-mfa-cloudhsm-cli.md")
- [Token file reference](reference-mfa-cloudhsm-cli.md "reference-mfa-cloudhsm-cli.md")
