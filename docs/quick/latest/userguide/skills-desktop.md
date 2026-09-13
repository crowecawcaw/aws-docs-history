

# Skills
<a name="skills-desktop"></a>

Skills are reusable sets of instructions that teach your agents how to do a specific task. Each skill packages the steps and know-how for that task. Instead of re-explaining how you want a task done every time, you capture it once as a skill, and Quick applies those instructions whenever the task comes up, for example writing a blog post that follows your brand guidelines, or preparing a weekly status update from your template. You can create your own skills, publish and share them, and install skills that other people in your organization share with you. You manage these from the **Skills** tab (**Customize > Skills**).

## Skill definition
<a name="desktop-skill-definition"></a>

A skill is a folder with a `SKILL.md` file at its root. That file holds a description (a short summary of what the skill is for, which Quick uses to recognize when the skill applies to your request) and instructions (the steps and guidance Quick follows when the skill is active, which can define a multi-step process, not just a single prompt).

A skill can also reference tools and bundle reference files.
+ Referenced tools: the tools the skill relies on. Tools are defined separately, as connectors or built-in capabilities. A skill points to the tools it needs rather than containing them, and Quick makes them available when the skill activates.
+ Reference files: supporting files the instructions draw on, such as scripts, templates, or examples.

## How agents load skills
<a name="desktop-how-quick-loads-skills"></a>

Agents load skills in two stages.

1. Discovery: agents search skills by name and description to know when a skill is relevant.

1. Activation: when your request matches a skill's description, or you name the skill, the agent reads its full instructions into the conversation and then follows them, including the referenced tools and files.

## Owner and viewer
<a name="desktop-skill-owner-viewer"></a>

What you can do with a skill you created or installed depends on your role for it.
+ Owner: you created the skill or duplicated one into your own. You can edit, publish, share, export, and delete it.
+ Viewer: someone shared the skill with you. You can add and use it, and it stays in sync with the owner's published version. You cannot edit, publish, re-share, or delete it. To make a version you can change, duplicate it. Duplicating creates a separate skill that you own.

## System skills
<a name="desktop-builtin-skills"></a>

Quick includes system skills, pre-installed skills for capabilities such as document creation, presentations, spreadsheets, web browsing, code execution, knowledge graph management, and transcription. They carry a System badge. You can try one and turn it on or off, but you cannot edit, duplicate, export, publish, share, or delete it.

## Creating a skill
<a name="desktop-creating-a-skill"></a>

To create a skill, choose **Customize > Skills**, choose **Create**, and then choose a method.

**To create a skill from chat**

1. Choose **Create**, and then choose **From chat**.

1. Describe the skill you want. Quick drafts the instructions, selects the tools to reference, and creates the `SKILL.md` file.

1. Review and edit the skill, and then save it.

**To create a skill from a file**

1. Choose **Create**, and then choose **From file**.

1. Select a `.md` or `.zip` file from your computer.

1. Review and edit the skill, and then save it.

**To create a skill from a folder**

1. Choose **Create**, and then choose **From folder**.

1. Select a folder that contains a `SKILL.md` file at its root, along with any reference files the skill uses.

1. Review and edit the skill, and then save it.

**Tip**  
When you finish a multi-step task in chat, Quick might offer to save those steps as a reusable skill.

## Using a skill
<a name="desktop-using-a-skill"></a>

You can use a skill in one of the following ways.
+ By name: mention the skill in your message. For example, enter "use the Web Browser skill to check this page."
+ Automatic activation: Quick detects when a skill matches your request and loads it without you asking. For example, when you ask Quick to build a presentation, the Presentations skill loads.
+ Try it: on a skill's detail panel, choose Try it to start a conversation with the skill loaded. Use Try it to test a skill you created, imported, or have in draft before you publish it.

## The skill detail panel
<a name="desktop-skill-detail-panel"></a>

Choose a skill to open its detail panel. The panel shows the skill's description, its instructions, and its reference files. The available actions depend on whether it is a built-in skill or one of your own, your role for it, and whether it is published.


| Action | Description | 
| --- | --- | 
| Try it | Start a conversation with the skill loaded. | 
| Edit | Change the skill's instructions and files. Edits are saved to the draft. Owner only. | 
| Publish | Make the draft the live published version, available when the skill has unpublished changes. Owner only. | 
| Duplicate | Copy the skill as the starting point for a new one that you own. | 
| Add to favorites | Pin the skill under the Favorites filter. | 
| Share | Share the skill with people or groups, or with your entire account. Owner only. | 
| Export | Download the skill as a file. Owner only. | 
| Enable or disable | Turn the skill on or off. A disabled skill stays in your list but is not loaded until you turn it back on. | 
| Uninstall or Delete | For a skill shared with you, Uninstall removes it from your list only. For a skill you own, Delete removes it permanently for everyone it is shared with, not just you. | 

## Draft and published versions
<a name="desktop-skill-draft-published"></a>

A skill you own has two versions.
+ Draft: the version you edit. Changes you make are saved to the draft and do not affect how the skill runs until you publish. A skill with unpublished changes shows an Unpublished changes indicator.
+ Published (live): the live published version, which Quick uses when the skill runs.

To update a skill, edit the draft, choose Try it to test it, and then choose Publish. Publishing replaces what is live, and everyone you shared the skill with moves to the update. Because your draft stays separate from what is published, a skill already in use keeps running the same way while you work on its next version.

## Managing skills
<a name="desktop-managing-skills"></a>

The Skills tab lists every skill you can use.
+ Search: find skills by name or description.
+ Filter: narrow to Favorites, Owned by me, or Shared with me.
+ Sort: order the list, for example by Last modified.
+ View: switch between a list view and a grid of cards.
+ Status: the Status column shows whether each skill is enabled.
+ Version indicator: for a skill you own, the list shows a Draft or Unpublished changes label when the draft is ahead of the published version.

## Browsing for more skills
<a name="desktop-browsing-more-skills"></a>

To find skills beyond the ones in your list, choose **Browse all** on the Skills tab. This opens Add to Quick, scoped to skills, with two ways to find them: Official (curated, first-party skills provided by Amazon Quick) and Shared with me (skills that people or teams in your organization have shared with you). Search by name, filter by Owner and Category, and sort the results. Choose a skill to preview its description and details before you add it.

When you add a skill from Official or Shared with me, it enters your list as a reference to the owner's published version, not a copy. It stays in sync and updates automatically as the owner republishes. To make a version you can change, duplicate it.

**Note**  
The Quick official skills span everyday productivity, role-based solutions for teams such as Sales, Marketing, and Legal, and industry depth in areas such as Finance, Healthcare and Life Sciences, and Energy and Utilities. New skills are added over time.

## Sharing your skills
<a name="desktop-sharing-skills"></a>

Publishing and sharing are separate steps. Publishing creates the live version of a skill but does not distribute it. Sharing is a separate action in which you choose who receives the skill. Publishing a skill does not share it with anyone.

**To share a skill you own**

1. Open the skill's detail panel.

1. Choose **Share**.

1. Choose who to share it with: specific people or groups, or your entire account with Share with all.

People you share the skill with find it in Add to Quick under Shared with me and add it to their own list. As viewers, their skill stays in sync with your published version and updates automatically as you republish.

**Note**  
Your administrator can require approval before a skill is shared, and can control whether skills can be shared with your entire account. See Administrator controls (the next section).

## Administrator controls
<a name="desktop-skill-admin-controls"></a>

Administrators can restrict skills through custom permissions. Custom permissions is a scope-down policy that an administrator applies at the account, role, or user level to limit the capabilities people can use. It restricts capabilities; it does not grant them. The following capabilities apply to skills.
+ Skills: restricts access to skills, including sharing them. This is the parent capability; denying it restricts the skill's full feature set.
+ Share skills with individuals: a child of the Skills capability. When denied, users cannot share skills with individuals.
+ Share skills with all: a child of the Skills capability. When denied, users cannot share skills with their entire account; they can still share with specific people or groups if that is allowed.
+ Require approval to share skills: a child of the Skills capability. When enabled, a skill must be approved before it is shared.

For how administrators configure custom permissions profiles and how precedence is resolved across the account, role, and user levels, see [Custom permissions](custom-permissions.md).