# Understanding your identity source

IAM Identity Center uses an identity source to define where users are managed. There are two types of
identity sources:

IAM Identity Center directory

This is the default identity source. Users are created and managed directly
within IAM Identity Center. You can create users through the Deadline Cloud console or the IAM Identity Center console.
Users receive email invitations to join your organization, and passwords are managed
within IAM Identity Center.

External identity provider (IdP)

Users are federated from an external system such as Okta,
Microsoft Entra ID, or other SAML 2.0 identity providers. Users
must be created in the external system first. The Deadline Cloud console cannot create users
when an external IdP is configured, but you can assign permissions to existing users.
Passwords are managed by the external IdP.

To check your identity source configuration or change it, see [Manage your identity
source](../../../singlesignon/latest/userguide/manage-your-identity-source.md "../../../singlesignon/latest/userguide/manage-your-identity-source.md") in the IAM Identity Center User Guide.
