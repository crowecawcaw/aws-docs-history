# Launch a Workspace in EMR Studio

To start working with notebook files, launch a Workspace to access the notebook
editor. The **Workspaces** page in a Studio lists all of
the Workspaces that you have access to with details including
**Name**, **Status**, **Creation
time**, and **Last modified**.

###### Note

If you had EMR notebooks in the old Amazon EMR console, you can find them in the
console as EMR Studio Workspaces. EMR Notebooks users need additional IAM
role permissions to access or create Workspaces. If you recently created a
notebook in the old console, you might need to refresh the Workspaces list to see
it in the console. For more information about the transition, see [Amazon EMR Notebooks are available as
Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Managing Amazon EMR clusters with the console](whats-new-in-console.md "whats-new-in-console.md")

###### To launch a Workspace for editing and running notebooks

1. On the **Workspaces** page of your Studio, find
   the Workspace. You can filter the list by keyword or by column value.
2. Choose the Workspace name to launch the Workspace in a new browser
   tab. It may take a few minutes for the Workspace to open if it's
   **Idle**. Alternatively, select the row for the Workspace and then
   select **Launch Workspace**. You can choose from the following launch
   options:
   - Quick launch – Quickly launch your
     Workspace with default options. Choose **Quick launch** if
     you want to attach clusters to the Workspace in JupyterLab.
   - Launch with options – Launch your
     Workspace with custom options. You can choose to launch in either Jupyter
     or JupyterLab, attach your Workspace to an EMR cluster, and select your
     security groups.

###### Note

Only one user can open and work in a Workspace at a time. If you select a
Workspace that is already in use, EMR Studio displays a notification when
you try to open it. The **User** column on the
**Workspaces** page shows the user working in the
Workspace.
