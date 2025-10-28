# Managing dashboards

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

On the **Dashboards** page of your workspace (available by
selecting **Dashboards** from the left menu), you can perform
dashboard management tasks, including organizing your dashboards into folders.

For more information about creating dashboards, see [Building dashboards](v10-dash-building-dashboards.md "v10-dash-building-dashboards.md").

## Browse dashboards

On the **Dashboards** page, you can browse and manage folders
and dashboards. This includes options to:

- Create folders and dashboards.
- Move dashboards between folders.
- Delete multiple dashboards and folders.
- Navigate to a folder.
- Manage folder permissions. For more information, see
  [Dashboard and folder
  permissions](dashboard-and-folder-permissions.md "dashboard-and-folder-permissions.md").

## Creating dashboard

folders

Folders help you organize and group dashboards, which is useful when you have many
dashboards or multiple teams using the same Grafana instance. Subfolders allow you
to create a nested hierarchy in your dashboard organization.

**Prerequisites**

Ensure that you have Grafana Admin permissions. For more information about
dashboard permissions, see [Dashboard and folder
permissions](dashboard-and-folder-permissions.md "dashboard-and-folder-permissions.md").

###### To create a dashboard folder

1. Sign in to Grafana.
2. On the left menu, select **Dashboards**.
3. On the **Dashboards** page, select
   **New** then choose **New folder** in
   the drop down.
4. Enter a unique name and click **Create**.

###### Note

When you save a dashboard, you can either select a folder for the dashboard to
be saved in or create a new folder.

###### To edit the name of a folder

1. Select **Dashboards**in the left menu.
2. Select the folder to rename
3. Select the **Edit title** (pencil) icon in the header
   and update the name of the folder.

The new folder name is automatically saved.

**Folder permissions**

You can assign permissions to a folder. Dashboard in the folder inherit any
permissions that you've assigned to the folder. You can assign permissions to
organization roles, teams, and users.

###### To modify permissions for a folder

1. Select **Dashboards** from the left menu.
2. Select the folder in the list.
3. On the folder's details page, select **Folder actions**
   and select **Manage permissions** in the drop down list.
4. Update the permissions as desired.

Changes are saved automatically.
