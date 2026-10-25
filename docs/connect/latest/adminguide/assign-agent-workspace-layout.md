

# Assign an agent workspace layout to agents
<a name="assign-agent-workspace-layout"></a>

To assign a layout to agents, create a workspace, select a layout, and assign the workspace to agents. Agents who are not assigned a workspace continue to use the original layout of the agent workspace.

**Note**  
Your security profile needs permissions to view, edit, create, delete, assign, and edit visibility of workspaces. To add these permissions, go to the **Security profiles** page. For the full list of permissions, see [List of security profile permissions](security-profile-list.md#users-permissions-list).

## Create a workspace and set the layout
<a name="assign-agent-workspace-layout-create"></a>

1. Open the Connect Customer admin workspace.

1. Go to **UI Management** > **Workspaces**.

1. Choose **Add new workspace**.

1. Enter a name for the workspace. Optionally, enter a description, which only administrators see, and a title, which replaces **Amazon Connect Customer** in the header bar unless you use a custom logo.

1. Choose **Save**. Amazon Connect Customer creates the workspace and opens its details page.

1. In the **Pages** section, choose **Add page**.

1. Choose **Use existing Connect page**.

1. For **Page**, choose **Agent Workspace**.

1. For **Page layout**, choose **Agent Workspace - Classic** or **Agent Workspace - Modern**.

1. For **View version**, choose **LATEST**.

1. (Optional) In the **Customize apps on Agent Workspace** section, choose a layout for the Customer Profiles app. For more information, see [Show Profile Explorer in the agent workspace](add-profileexplorer-to-agentworkspace.md).

1. Choose **Save**.

## Assign the workspace to agents
<a name="assign-agent-workspace-layout-assign"></a>

Agents see the layout after you assign them the workspace.

1. On the workspace details page, go to the **Assignments** section.

1. Open the visibility dropdown and choose one of the following:
   + **Visible to all users** shows the workspace to every user in your instance.
   + **Visible to assigned users** shows the workspace only to the users and routing profiles that you assign.
   + **Visible to no users** hides the workspace while you prepare or test it.

1. If you chose **Visible to assigned users**, choose **Add assignments**.

1. For **Users**, search for and choose the agents who use this layout.

1. For **Routing profiles**, search for and choose a routing profile. Assigning a routing profile assigns the workspace to every agent in it, which is the fastest way to reach a team.

1. Choose **Save**.

To remove a user or routing profile from the workspace, select the assignment and choose **Delete**.