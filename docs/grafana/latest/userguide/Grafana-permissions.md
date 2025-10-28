# Using permissions

What you can do in a Grafana workspace in Amazon Managed Grafana is defined by the
_permissions_ that are associated with your user.

Amazon Managed Grafana uses three types of permissions:

- Permissions granted as a Grafana admin
- Permissions associated with your membership on a team
- Permissions granted to a specific folder or dashboard
  You can be granted permissions based on your admin status, dashboard or folder
  permissions assigned to your user, and data source permissions.

## Dashboard and folder

permissions overview

By using dashboard and folder permissions, you can remove the default role-based
permissions for editors and viewers. You can then assign permissions to specific
users and teams. For more information, see [Dashboard and folder
permissions](dashboard-and-folder-permissions.md "dashboard-and-folder-permissions.md").

## Data source permissions

overview

By default, a data source can be queried by any user. For example, a user with
the `Viewer` role can issue any possible query to a data source, not
just those queries that exist on dashboards to which they have access.

Using data source permissions, you can change the default permissions for data
sources and restrict query permissions to specific **Users** and
**Teams**. For more information, see [Data source permissions](data-source-permissions.md "data-source-permissions.md").
