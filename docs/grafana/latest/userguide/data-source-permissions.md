

# Data source permissions
<a name="data-source-permissions"></a>

By default, data sources can be queried by any user. For example, a user with the `Viewer` role can issue any possible query to a data source, not just queries that exist on dashboards to which they have access.

You can use data source permissions to restrict access for users to query a data source. For each data source, there is a permission page where you can enable or restrict query permissions to specific **Users** and **Teams**.

## Enabling data source permissions
<a name="enable-data-source-permissions"></a>

When permissions are enabled for a data source, you restrict admin and query access for that data source to Admin users by default. You can selectively add access for specific users and teams.

**To enable permissions for a data source**

1. Navigate to **Configuration**, **Data Sources**. For workspaces that support Grafana version 10, Navigate to **Connections**, **Data Sources**.

1. Select the data source for which you want to enable permissions.

1. On the **Permissions** tab, choose **Enable**.

**Warning**  
If you enable permissions for the default data source, users who are not listed in the permissions are unable to invoke queries. Panels that use the default data source will return the `Access denied to data source` error for those users.

## Allowing users and teams to query a data source
<a name="allow-users-and-teams-to-query-a-data-source"></a>

After you enable permissions for a data source, only admins have access to that data source by default. You can assign query permissions to users or teams. The query permissions will allow access to query the data source.

**To assign query permissions to users and teams**

1. Navigate to **Configuration**, **Data Sources**. For workspaces that support Grafana version 10, Navigate to **Connections**, **Data Sources**.

1. Select the data source for which you want to assign query permissions.

1. On the **Permissions** tab, choose **Add Permission**.

1. Select **Team** or **User**. For workspaces that support Grafana version 10 or newer, you can also select **Service account** or **Role**.

1. Select the team, user, service account, or role that you want to grant query access to, and then choose **Save**.

## Disabling data source permissions
<a name="disable-data-source-permissions"></a>

If you have enabled permissions for a data source and want to return data source permissions to the default, follow these steps.

**Note**  
*All* existing permissions created for the data source will be deleted.

**To disable permissions for a data source**

1. Navigate to **Configuration**, **Data Sources**. For workspaces that support Grafana version 10, Navigate to **Connections**, **Data Sources**.

1. Select the data source for which you want to disable permissions.

1. On the **Permissions** tab, choose **Disable Permissions**.