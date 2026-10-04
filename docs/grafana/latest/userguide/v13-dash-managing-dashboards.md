

# Managing dashboards
<a name="v13-dash-managing-dashboards"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 13.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).

On the **Dashboards** page of your workspace (available by selecting **Dashboards** from the left menu), you can perform dashboard management tasks, including organizing your dashboards into folders.

For more information about creating dashboards, see [Building dashboards](v13-dash-building-dashboards.md).

## Browse dashboards
<a name="v13-dash-browse-dashboards"></a>

On the **Dashboards** page, you can browse and manage folders and dashboards. This includes options to:
+ Create folders and dashboards.
+ Move dashboards between folders.
+ Delete multiple dashboards and folders.
+ Navigate to a folder.
+ Manage folder permissions. For more information, see [Dashboard and folder permissions](dashboard-and-folder-permissions.md).

## Restoring deleted dashboards
<a name="v13-dash-restore-deleted-dashboards"></a>

When you delete a dashboard, it is kept in a **Recently deleted** list, from which you can restore it. Deleted dashboards are retained for up to 12 months, or until the deletion history reaches its limit of 1,000 dashboards, after which the oldest deleted dashboards are permanently removed. Deleting a folder is immediate and can't be reversed.

**Note**  
You can restore dashboards that you deleted. Users with administrator permissions can restore dashboards deleted by any user. To restore a dashboard, you also need edit permissions on the target folder.

**To restore a deleted dashboard**

1. From the left menu, select **Dashboards** > **Recently deleted**, or select the **Recently deleted** button on the **Dashboards** page.

1. Select the dashboards that you want to restore.

1. Select **Restore**, and then choose the folder to which the dashboards will be restored.

1. Select **Restore** to confirm.

Restoring a dashboard has the following limitations:
+ **Permissions aren't preserved** – Dashboard-specific permissions are not restored. After restoration, you must manually reconfigure any custom permissions that were previously set on the dashboard.
+ **Folder-level permissions apply** – Restored dashboards inherit the permissions of the target folder that you select during restoration.
+ **Version history is reset** – The dashboard's version history is not preserved. After restoration, the dashboard starts at version 1, and all previous versions are lost.

## Creating dashboard folders
<a name="v13-dash-create-dashboard-folder"></a>

Folders help you organize and group dashboards, which is useful when you have many dashboards or multiple teams using the same Grafana instance. Subfolders allow you to create a nested hierarchy in your dashboard organization.

**Prerequisites**

Ensure that you have Grafana Admin permissions. For more information about dashboard permissions, see [Dashboard and folder permissions](dashboard-and-folder-permissions.md).

**To create a dashboard folder**

1. Sign in to Grafana. 

1. On the left menu, select **Dashboards**.

1. On the **Dashboards** page, select **New** then choose **New folder** in the drop down.

1. Enter a unique name and click **Create**.

**Note**  
When you save a dashboard, you can either select a folder for the dashboard to be saved in or create a new folder.

**To edit the name of a folder**

1. Select **Dashboards** in the left menu.

1. Select the folder to rename

1. Select the **Edit title** (pencil) icon in the header and update the name of the folder.

   The new folder name is automatically saved.

**Folder permissions**

You can assign permissions to a folder. Dashboards in the folder inherit any permissions that you've assigned to the folder. You can assign permissions to organization roles, teams, and users.

**To modify permissions for a folder**

1. Select **Dashboards** from the left menu.

1. Select the folder in the list.

1. On the folder's details page, select **Folder actions** and select **Manage permissions** in the drop down list.

1. Update the permissions as desired.

Changes are saved automatically.