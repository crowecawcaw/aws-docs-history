# Managing users in Deadline Cloud

AWS Deadline Cloud uses AWS IAM Identity Center to manage users and groups. IAM Identity Center is a cloud-based single sign-on
service that can be integrated with your enterprise single-sign on (SSO) provider. With
integration, users can sign in with their company account.

Deadline Cloud enables IAM Identity Center by default, and it is required to set up and use Deadline Cloud. An organization
owner for your AWS Organizations is responsible for managing the users and groups that have access to
your Deadline Cloud monitor. For more information, see [What is AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

How you manage users depends on your IAM Identity Center identity source configuration. The identity source
defines where IAM Identity Center gets user information.

###### Topics

- [Understanding your identity source](understanding-identity-source.md "understanding-identity-source.md")
- [Create and manage users with IAM Identity Center directory](manage-monitor-users_users.md "manage-monitor-users_users.md")
- [Manage users with an external identity provider](manage-users-external-idp.md "manage-users-external-idp.md")
- [Understanding access levels](manage-users-by-farm.md "manage-users-by-farm.md")
