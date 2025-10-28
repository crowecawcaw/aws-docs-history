# User roles

In Amazon Managed Grafana, each user enabled to use the Amazon Managed Grafana workspace are assigned to one of
three [roles](AMG-manage-users-and-groups-AMG.md "AMG-manage-users-and-groups-AMG.md") in the Amazon Managed Grafana
console.

- **Admin role**— Users with the Admin role
  can do the following:
  - Can add, edit, and delete data sources.
  - Can add and edit users and teams.
  - Can add, edit, and delete folders containing dashboards.
  - Can do everything allowed by the Editor role.

- **Editor role**— Users with the Editor
  role can do the following:
  - Can view, add, and edit dashboards, panels, and alert rules in
    dashboards they have access to. This can be disabled on specific folders
    and dashboards.
  - Can create, update, or delete playlists.
  - Can access Explore.
  - Can add, edit, and delete notification channels.
  - Cannot add, edit, or delete data sources.
  - Can do everything allowed by the Viewer role.

- **Viewer role**— Users with the Viewer
  role can do the following:

      + Can view any dashboard they have access to. This can be disabled on
       specific folders and dashboards.
      + Cannot create, update, or delete playlists.
      + Cannot access Explore.
      + Cannot add, edit, and delete notification channels.
      + Cannot add, edit, or delete data sources.
      + Cannot add, edit, or delete dashboards or panels.
      + Cannot manage other users or teams.

  User assignment and user access management from the Grafana workspace is not
  supported in Amazon Managed Grafana. How you manage user and group access depends on whether you
  use IAM Identity Center or SAML for authentication:

- If your workspace uses IAM Identity Center for authentication, you can use Amazon Managed Grafana
  console or APIs to assign roles. For more information, see [Manage user and group access to
  Amazon Managed Grafana workspaces](AMG-manage-users-and-groups-AMG.md "AMG-manage-users-and-groups-AMG.md").
- If your workspace uses SAML for authentication, user roles are defined only
  by assertion attributes. For more information, see
  [Assertion mapping](authentication-in-AMG-SAML.md#AMG-SAML-Assertion-Mapping "authentication-in-AMG-SAML.md#AMG-SAML-Assertion-Mapping").
