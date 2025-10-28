# External identity providers

With IAM Identity Center, you can connect your existing workforce identities from external identity
providers (IdPs) through the Security Assertion Markup Language (SAML) 2.0 and System for
Cross-Domain Identity Management (SCIM) protocols. This enables your users to sign in to the
AWS access portal with their corporate credentials. They can then navigate to their assigned accounts,
roles, and applications hosted in external IdPs.

For example, you can connect an external IdP such as Okta or Microsoft
Entra ID, to IAM Identity Center. Your users can then sign in to the AWS access portal with their existing
Okta or Microsoft Entra ID credentials. To control what your
users can do once they've signed in, you can assign them access permissions centrally across all
the accounts and applications in your AWS organization. In addition, developers can simply
sign in to the AWS Command Line Interface (AWS CLI) using their existing credentials, and benefit from automatic
short-term credential generation and rotation.

If you are using a self-managed directory in Active Directory or an AWS Managed Microsoft AD, see [Microsoft AD
directory](manage-your-identity-source-ad.md "manage-your-identity-source-ad.md").

###### Note

The SAML protocol does not provide a way to query the IdP to learn about users and groups.
Therefore, you must make IAM Identity Center aware of those users and groups by provisioning them into
IAM Identity Center.

## Provisioning when users come from an external

IdP

When using an external IdP, you must provision all applicable users and groups into IAM Identity Center
before you can make any assignments to AWS accounts or applications. To do this, you can
configure [Provision users and groups from an external identity provider using SCIM](provision-automatically.md "provision-automatically.md")
for your users and groups, or use [Manual provisioning](provision-automatically.md#provision-manually "provision-automatically.md#provision-manually"). Regardless of how you provision users, IAM Identity Center redirects
the AWS Management Console, command line interface, and application authentication to your external IdP.
IAM Identity Center then grants access to those resources based on policies you create in IAM Identity Center. For more
information about provisioning, see [User and group provisioning](users-groups-provisioning.md#user-group-provision "users-groups-provisioning.md#user-group-provision").

###### Topics

- [How to connect to an external identity provider](how-to-connect-idp.md "how-to-connect-idp.md")
- [How to change an external identity provider's
  metadata in IAM Identity Center](how-to-change-idp-metadata.md "how-to-change-idp-metadata.md")
- [Using SAML and SCIM identity federation with external identity
  providers](other-idps.md "other-idps.md")
- [SCIM profile and SAML 2.0 implementation](scim-profile-saml.md "scim-profile-saml.md")
