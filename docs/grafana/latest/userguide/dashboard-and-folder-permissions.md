# Dashboard and folder

permissions

For dashboards and dashboard folders, you can use the
**Permissions** page to remove the default role based
permissions for **Editors** and **Viewers**. On
this page, you can add and assign permissions to specific
**Users** and **Teams**.

Amazon Managed Grafana provides the following permission levels. The permissions vary based
on the version of Grafana the workspace supports.

**For workspaces that support version 8:**

- `Admin`: Can edit and create dashboards and edit permissions.
  Can also add, edit, and delete folders.
- `Edit`: Can edit and create dashboards.
  **Can't** edit folder or
  dashboard permissions, or add, edit, or delete folders.
- `View`: Can only view existing dashboards and folders.
  **For workspaces that support version 9 and above:**

- `Admin`: Can create, edit or delete a dashboard. Can add,
  edit, or delete folders, and create dashboards and subfolders in a folder.
  Administrators can also change dashboard and folder permissions.
- `Edit`: Can create, edit, or delete a dashboard. Can edit or
  delete a folder, and create dashboards and subfolders in a folder. An
  editor **can't** change folder or dashboard
  permissions.
- `View`: Can only view existing dashboards and folders.

## Granting folder permissions

###### To grant folder permissions

1. In the sidebar, hover over the **Dashboards**
   (squares) icon, and then choose **Manage**.
2. Hover over a folder, and then choose **Go to
   folder**.
3. On the **Permissions** tab, choose **Add
   Permission**.
4. In the **Add Permission For** dialog box, choose
   **User**, **Team**, or one of the
   role options. If your workspace uses Grafana version 10 or newer, choose
   **User, Team, Service account, or Role**.
5. In the second box, select the user, team, service account, or role
   to which you want to add permissions.
   If your workspace is using Grafana version 9 or earlier, and you
   selected a role option in the previous step, then skip this step.
6. In the third box, select the permission that you want to add.
7. Choose **Save**.

## Granting dashboard

permissions

###### To grant dashboard permissions

1. In the top right corner of your dashboard, choose the cog icon to go
   to **Dashboard settings**.
2. On the **Permissions** tab, choose **Add
   Permission**.
3. In the **Add Permission For** dialog box, choose
   **User**, **Team**, or one of the
   role options. If your workspace uses Grafana version 10 or newer, choose
   **User, Team, Service account, or Role**.
4. In the second box, select the user, team, service account, or role
   to which you want to add permissions.
   If your workspace is using Grafana version 9 or earlier, and you
   selected a role option in the previous step, then skip this step.
5. In the third box, select the permission you that want to add.
6. Choose **Save**.

## Restricting access

The highest permission always wins.

- You cannot override permissions for users with the `Admin`
  role. Admins always have access to everything.
- A more specific permission with a lower permission level does not
  have any effect if a more general rule exists with a higher permission
  level. You need to remove or lower the permission level of the more
  general rule.

## How

Amazon Managed Grafana resolves multiple permissions – examples

The following examples show how multiple permissions are resolved.

### Example 1:

`user1` has the `Editor` role

Permissions for a dashboard:

- Everyone with the `Editor` role can edit.
- `user1` can view.

Result: `user1` has Edit permission because the highest
permission always wins.

### Example 2: `user1` has the Viewer role and is a member

of `team1`

Permissions for a dashboard:

- Everyone with the `Viewer` role can view.
- `user1` has the `Editor` role and can
  edit.
- `team1` has the `Admin` role.

Result: `user1` has Admin permission because the highest
permission always wins.

### Example 3: `user1` has multiple

permissions at different levels

Permissions for a dashboard:

- `user1` has the `Admin` role (inherited
  from parent folder).
- `user1` has the `Editor` role and can
  edit.

Result: You cannot override to a lower permission. `user1`
has Admin permission because the highest permission always wins.

## Summary

- **View**: Can only view existing
  dashboards or folders.
- A more specific permission with a lower permission level will not
  have any effect if a more general rule exists with higher permission
  level.
