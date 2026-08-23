# Sign in as a federated identity

A federated identity is a user that can access secure AWS account resources with external
identities. External identities can come from a corporate identity store (such as LDAP or Windows
Active Directory) or from a third party (such as Login in with Amazon, Facebook, or Google).
Federated identities don't sign in with the AWS Management Console or AWS access portal. The type of external
identity in use determines how federated identities sign in.

This sign-in method is only supported for accounts created with Sign up for AWS
(advanced). For more information, see [Compare sign-up options](../../../accounts/latest/reference/sign-up-for-aws.md "../../../accounts/latest/reference/sign-up-for-aws.md")
in the _AWS Account Management Reference Guide_.

Administrators must create a custom URL that includes
`https://signin.aws.amazon.com/federation`. For more information, see [Enabling custom
identity broker access to the AWS Management Console](../../../IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.md "../../../IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.md").

###### Note

Your administrator creates federated identities. Contact your administrator for more
details on how to sign in as a federated identity.

For more information about federated identities, see [About web identity
federation](../../../IAM/latest/UserGuide/id_roles_providers_oidc.md "../../../IAM/latest/UserGuide/id_roles_providers_oidc.md").
