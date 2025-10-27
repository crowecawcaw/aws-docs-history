# Managing users in Deadline Cloud

AWS Deadline Cloud uses AWS IAM Identity Center to manage users and groups. IAM Identity Center is a cloud-based single sign-on
service that can be integrated with your enterprise single-sign on (SSO) provider. With
integration, users can sign in with their company account.

Deadline Cloud enables IAM Identity Center by default, and it is required to set up and use Deadline Cloud. For more
information, see [Manage your
identity source](../../../singlesignon/latest/userguide/manage-your-identity-source.md "../../../singlesignon/latest/userguide/manage-your-identity-source.md").

An organization owner for your AWS Organizations is responsible for managing the users and groups
that have access to your Deadline Cloud monitor. You can create and manage these users and groups
using IAM Identity Center or the Deadline Cloud console. For more information, see [What is
AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

With the Deadline Cloud console, you create and remove users and groups that can manage farms, queues,
and fleets. IAM Identity Center users created in the Deadline Cloud console will receive email invitations from IAM Identity Center.
After the user accepts the invitation, the user will be able to access their assigned Deadline Cloud monitor.

###### Topics

- [Manage users and groups for the
  monitor](manage-monitor-users_users.md "manage-monitor-users_users.md")
- [Manage users and groups for farms, queues, and
  fleets](manage-users-by-farm.md "manage-users-by-farm.md")
