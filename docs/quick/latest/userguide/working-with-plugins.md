

# Plugins

Plugins are bundles of capabilities that work together for a role, team, or task. A plugin packages the agents, skills, connectors, and flows that a job needs, so you start from a ready setup instead of configuring each piece yourself. Installing a plugin sets up every capability it contains in one step. You can install plugins that AWS Quick and trusted partners publish, install plugins that your organization shares with you, and bundle your own capabilities into a plugin to share with others. You manage plugins from the **Plugins** page in Quick. A plugin can contain up to 50 agents, skills, connectors, and flows.

## Plugin definition
<a name="plugin-definition"></a>

A plugin bundles the following capabilities so that they install and work together.
+ **Agents** – configurable AIs that you give instructions, knowledge sources, and tools so that they can answer questions and complete tasks. For more information, see [Agents in AWS Quick](working-with-agents.md).
+ **Skills** – reusable instruction sets that teach agents how to complete a specific task. For more information, see [Teach agents with skills](working-with-skills.md).
+ **Connectors** – links that let Quick reach external applications and services so that agents can access data and act on your behalf. For more information, see [Work with integrations in AWS Quick](working-with-integrations.md).
+ **Flows** – multi-step workflows that automate repeatable tasks. For more information, see [Flows](working-with-flows.md).

## When to use a plugin
<a name="when-to-use-a-plugin"></a>

Use a plugin when a job needs several capabilities set up together, or when you want to standardize the setup that a team uses. A plugin keeps the related agents, skills, connectors, and flows together, so everyone who installs it starts from the same ready setup.

If you need only a single capability, add that capability on its own instead of creating a plugin for it.

## Browsing and installing a plugin
<a name="browsing-installing-a-plugin"></a>

To find plugins beyond the ones in your list, choose **Browse all** on the **Plugins** page, or open **Discover**. In **Discover**, you can browse by industry, role, and capability type to find plugins that fit the work you do. For more information, see [Discover](working-with-discover.md).

**Note**  
The official plugins that AWS Quick and trusted partners publish span everyday productivity, role-based solutions for teams, and industry depth. New plugins are added over time.

**To install a plugin**

1. Open the **Plugins** page, and then choose **Browse**.

1. Search or filter to find the plugin that you want.

1. Choose the plugin to review the agents, skills, connectors, and flows that it includes.

1. Choose **Install**.

1. If the plugin needs a connector, select an existing connector or create one, and then choose **Continue to install plugin**.

An installed plugin stays in sync with the owner's published version, so it updates automatically as the owner republishes. Each user who installs the plugin signs in to its connectors with their own account. A plugin installs only the capabilities that it contains.

## Creating a plugin
<a name="creating-a-plugin"></a>

You can create a plugin from chat or from the **Plugins** page.

**To create a plugin from chat**

1. Describe the plugin that you want, including the agents, skills, connectors, and flows to include.

1. Review the plugin that Quick assembles, and then adjust it in chat.

1. Save the plugin.

**To create a plugin from the Plugins page**

1. Open the **Plugins** page, and then choose **Create**.

1. Add the agents, skills, connectors, and flows to include.

1. Save the plugin.

## Draft and published versions
<a name="plugin-draft-published"></a>

A plugin that you own has two versions.
+ **Draft** – the version that you edit. Changes you make are saved to the draft and do not affect installed copies until you publish.
+ **Published (live)** – the version that people install and that stays in sync for everyone you shared it with.

You must publish a plugin before you can share it. Publishing replaces the live version, and everyone you shared the plugin with moves to the update.

**To publish a plugin**

1. Open the plugin that you own.

1. Review the draft to confirm that it includes the capabilities that you want.

1. Choose **Publish**.

## Sharing a plugin
<a name="sharing-plugins"></a>

Publishing and sharing are separate steps. Publish the plugin first, and then share it to choose who receives it.

**To share a plugin you own**

1. Open the plugin that you own.

1. Choose **Share**.

1. Choose who to share it with: specific people, or your entire account.

Sharing a plugin also gives the people you share it with view access to the capabilities inside it. Sharing a connector in a plugin does not share your sign-in; each person signs in to the connector with their own account. Your administrator can control whether you can share plugins.

## Owner and viewer
<a name="plugin-owner-viewer"></a>

What you can do with a plugin depends on your role for it.
+ **Owner** – you created the plugin or duplicated one into your own. You can edit, publish, share, duplicate, and delete it.
+ **Viewer** – someone shared the plugin with you. You can install and uninstall it, and it stays in sync with the owner's published version. To make a version you can change, duplicate it. Duplicating creates a separate plugin that you own.

## Managing plugins
<a name="managing-plugins"></a>

The **Plugins** page lists the plugins that you own and the plugins that you installed. From a plugin, you can take the following actions.


**Plugin actions**  

| Action | Description | 
| --- | --- | 
| Edit | Change the capabilities in the plugin. Edits are saved to the draft. Owner only. | 
| Duplicate | Copy the plugin as the starting point for a new one that you own. | 
| Publish | Make the draft the live published version. Owner only. | 
| Add to favorites | Pin the plugin under the Favorites filter. | 
| Copy link | Copy a link to the plugin so that you can share it. | 
| Share | Share the plugin with specific people or with your entire account. Owner only. | 
| Uninstall | Remove a plugin that is shared with you from your list. | 
| Delete | Remove a plugin that you own permanently, for everyone it is shared with. Owner only. | 

Uninstalling a plugin removes the capabilities that it installed, unless you installed a capability separately or another installed plugin references it.

## Administrator controls
<a name="plugin-admin-controls"></a>

Administrators can restrict plugins through custom permissions. Custom permissions is a scope-down policy that an administrator applies at the account, role, or user level to limit the capabilities that people can use. It restricts capabilities; it does not grant them. The following capabilities apply to plugins.
+ **Plugins** – restricts access to plugins, including sharing them. This is the parent capability; denying it restricts the plugin's full feature set.
+ **Share plugins with individuals** – a child of the Plugins capability. When denied, users cannot share plugins with individuals.

For how administrators configure custom permissions profiles and how precedence is resolved across the account, role, and user levels, see [Custom permissions](custom-permissions.md).