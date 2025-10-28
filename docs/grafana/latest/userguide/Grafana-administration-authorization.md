# Users, teams, and permissions

Permissions in Amazon Managed Grafana are managed across the Amazon Managed Grafana console and directly within
the workspace.

- **Users** – Users are [authenticated](authentication-in-AMG.md "authentication-in-AMG.md") in
  IAM Identity Center or an identity provider that you set up through SAML in the Amazon Managed Grafana
  console.
- **Role access** – You can give your users or
  groups [access](AMG-manage-users-and-groups-AMG.md "AMG-manage-users-and-groups-AMG.md") with the
  `User`, `Editor`, or `Admin` roles, to give them
  default permissions to your workspace, using the Amazon Managed Grafana console.
- **Groups, or Teams** – You can create groups
  of users to give access to in two ways. You can create groups in your identity
  provider (or IAM Identity Center). You can then give these groups access, just like a user, in
  the Amazon Managed Grafana console. Or you can create [Teams](Grafana-teams.md "Grafana-teams.md") in the Grafana workspace, and give them the role you want
  them to have.
- **Specific permissions** – If you want to
  [override the permissions](Grafana-permissions.md "Grafana-permissions.md") granted by
  roles for a specific dashboard, folder, or data source, you can remove the default
  permissions, and assign permissions to specific users or teams. This is done within
  the Grafana workspace.
  This section describes how to perform permissions management within the Grafana
  workspace.

###### Topics

- [Users](Grafana-users.md "Grafana-users.md")
- [User roles](Grafana-user-roles.md "Grafana-user-roles.md")
- [Managing teams](Grafana-teams.md "Grafana-teams.md")
- [Using permissions](Grafana-permissions.md "Grafana-permissions.md")
