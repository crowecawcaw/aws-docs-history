# Manage users in the Identity Center directory

IAM Identity Center provides the following capabilities for your users and groups:

- Create your users and groups.
- Add your users as members to the groups.
- Assign the groups with the desired level of access to your AWS accounts and
  applications.
  To manage users and groups in the IAM Identity Center store, AWS supports the API operations listed in [Identity
  Center Actions](../IdentityStoreAPIReference/API_Operations.md "../IdentityStoreAPIReference/API_Operations.md").

## Provisioning when users are in IAM Identity Center

When you create users and groups directly in IAM Identity Center, provisioning is automatic. These
identities are immediately available for use in making assignments and for use by
applications. For more information, see [User and group provisioning](users-groups-provisioning.md#user-group-provision "users-groups-provisioning.md#user-group-provision").

## Changing your identity source

If you prefer to manage users in AWS Managed Microsoft AD, you can stop using your Identity Center
directory at any time and instead connect IAM Identity Center to your directory in Microsoft AD by
using Directory Service. For more information, see considerations for [Changing between IAM Identity Center
directory and Active Directory](manage-your-identity-source-considerations.md#changing-between-sso-and-active-directory "manage-your-identity-source-considerations.md#changing-between-sso-and-active-directory").

If you prefer to manage users in an external identity provider (IdP), you can connect
IAM Identity Center to your IdP and enable automatic provisioning. For more information, see
considerations for [Changing from IAM Identity Center to an external
IdP](manage-your-identity-source-considerations.md#changing-from-idc-and-idp "manage-your-identity-source-considerations.md#changing-from-idc-and-idp").

###### Topics

- [Add users to your Identity Center directory](addusers.md "addusers.md")
- [Add groups to your Identity Center directory](addgroups.md "addgroups.md")
- [Add users to groups](adduserstogroups.md "adduserstogroups.md")
- [Delete groups in IAM Identity Center](deletegroups.md "deletegroups.md")
- [Delete users in IAM Identity Center](deleteusers.md "deleteusers.md")
- [Remove users from groups](removeusersfromgroups.md "removeusersfromgroups.md")
- [Edit Identity Center directory user properties](edituser.md "edituser.md")
