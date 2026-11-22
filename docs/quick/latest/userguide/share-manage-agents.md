

# Share and manage agents

You must publish an agent before you can share it.

**To share an agent**

1. Choose **Customize**, and then choose the **Agents** tab.

1. Open the agent's menu, and then choose **Share**.

1. Add the people or groups you want to share the agent with, and choose a role for each.

You can assign one of two roles:

**Owner**  
Can use, edit, share, and delete the agent.

**Viewer**  
Can view and use the agent.

**Note**  
Sharing an agent doesn't share its spaces or connectors. To give people access to the same content, share the underlying spaces. If another owner adds a resource that you can't access, it appears as **Resource unavailable**.

The **Agents** tab lists your agents, and supports search, sorting, and list or grid views. You can filter by **Favorites**, **Owned by me**, and **Shared with me**, and use **More filters** for status or version.

Each agent has a menu whose actions depend on your ownership and whether the agent is published. From the menu, you can do the following:
+ Open or chat with the agent.
+ Edit the agent, publish it, or discard its draft.
+ Manage its versions or its routines.
+ Share, duplicate, or export the agent as a JSON file.
+ Add the agent to favorites, or make it your default.
+ Uninstall or delete the agent.

Uninstalling and deleting are different. **Uninstall** removes the agent from your list only, and the agent stays available to everyone else it is shared with.

**Deleting an agent is permanent**  
Deleting an agent removes it for everyone it is shared with, not just you. This can't be undone.

**Delete** removes an agent that you own.

## Admin controls for agents
<a name="admin-controls-agents"></a>

Administrators control who can use and create agents, the default agent, and the behavior of the Quick system agent.

Installed by default  
When an agent is published as installed by default and then shared, it is installed automatically. Users can't uninstall it while the setting is on.

Quick system agent owners  
Administrators own the Quick system agent. To assign owners, use [Manage assets](https://docs.aws.amazon.com/quicksuite/latest/userguide/manage-qs-assets.html) in the admin console.

Permissions for agents  
Administrators set permissions for agents with [custom permissions](https://docs.aws.amazon.com/quicksuite/latest/userguide/create-custom-permissions-profile.html) in the admin console. If you restrict **Agents**, you turn off agents, including chat and creation. If you restrict **Create agents**, users can chat with agents but can't create them. When you restrict spaces, knowledge bases, or actions, agents follow the same restrictions. Users without access to agents don't see agents in the navigation pane.

Blocked words and guardrails  
Administrators set blocked words and phrases for the account. These apply to every agent, including Quick.

To learn how to customize the Quick system agent as an administrator owner, see [Managing chat agent customization](https://docs.aws.amazon.com/quicksuite/latest/userguide/manage-agent.html).