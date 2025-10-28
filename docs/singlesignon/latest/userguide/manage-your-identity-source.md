# Manage your identity source

Your identity source in IAM Identity Center defines where your users and groups are managed. After you
configure your identity source, you can look up users or groups to grant them single sign-on
access to AWS accounts, applications, or both.

You can have only one identity source per organization in AWS Organizations. You can choose one of the
following as your identity source:

- **[External identity provider](manage-your-identity-source-idp.md "manage-your-identity-source-idp.md") –** Choose this option
  if you want to manage users in an external identity provider (IdP) such as Okta or Microsoft Entra ID.
- **[Your on premises or AWS managed Active Directory](manage-your-identity-source-ad.md "manage-your-identity-source-ad.md") –** Choose this option if you want to
  connect your Active Directory (AD).
- **[Identity Center directory](manage-your-identity-source-sso.md "manage-your-identity-source-sso.md") –** When you enable
  IAM Identity Center for the first time, it is automatically configured with an Identity Center directory as
  your default identity source unless you choose a different identity source. With the
  Identity Center directory, you create your users and groups, and assign their level of
  access to your AWS accounts and applications.

###### Note

IAM Identity Center does not support SAMBA4-based Simple AD as an identity source.

###### Topics

- [Considerations for changing
  your identity source](manage-your-identity-source-considerations.md "manage-your-identity-source-considerations.md")
- [Change your identity source](manage-your-identity-source-change.md "manage-your-identity-source-change.md")
- [Supported user and group attributes in
  IAM Identity Center](manage-your-identity-source-attribute-use.md "manage-your-identity-source-attribute-use.md")
- [External identity providers](manage-your-identity-source-idp.md "manage-your-identity-source-idp.md")
- [Microsoft AD
  directory](manage-your-identity-source-ad.md "manage-your-identity-source-ad.md")
