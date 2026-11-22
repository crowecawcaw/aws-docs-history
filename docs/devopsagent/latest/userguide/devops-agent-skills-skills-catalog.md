

# Skills Catalog

The AWS DevOps Agent Skills Catalog, available in the DevOps Agent web app, lists published skills, such as skills that investigate AWS Health events or check service quotas. The skills come from the [AWS DevOps Agent Tools repository](https://github.com/aws/tools-for-devops-agent) on the GitHub website. You can add a skill to your Agent Space without a GitHub account or a zip file. Agents use it the same way they use the skills that you create.

When you add a skill, AWS DevOps Agent copies it into your Agent Space as a *catalog skill*. Its name, description, files, and agent types come from the Skills Catalog, and you can't edit them. You can activate, deactivate, and delete it, and you can sync it to the current version in the Skills Catalog. Catalog skills don't count toward the limit of 200 user-created skills in an Agent Space.

## Browsing the Skills Catalog
<a name="browsing-the-skills-catalog"></a>

You can search the Skills Catalog and read a skill's files before you add it.

**Prerequisites:**
+ Permissions to use the Skills Catalog. The `AIDevOpsOperatorAppAccessPolicy` AWS managed policy includes them. If your operator role uses its own policy instead, add `aidevops:ListCatalogCapabilities`, `aidevops:GetCatalogCapability`, and `aidevops:ListCatalogCapabilityFiles` to it in a statement with `"Resource": "*"`. For more information about these actions, see [Catalog actions](aws-devops-agent-security-devops-agent-iam-permissions.md#catalog-actions).
+ Permissions to add and sync skills. The managed policy includes them too. If your operator role uses its own policy, it also needs `aidevops:CreateAsset` and `aidevops:UpdateAsset`.

**To browse the Skills Catalog:**

1. On the **Knowledge** page in the DevOps Agent web app, choose the **Skills** tab.

1. Next to **Add skill**, choose **Browse catalog**. The **Skills Catalog** tab opens.

1. To find a skill, enter text in **Find skills**, or filter by agent type, AWS service, technical domain, or tier.

1. To see a skill's summary, agent types, and files, choose **Details**.

1. To read a file, such as README.md, choose it under **Included files**. To browse all of the skill's files, choose **View all files**.

You can also open the Skills Catalog by choosing **Add skill** and then **Browse catalog**.

Each skill in the Skills Catalog shows its tier, which says who maintains the skill:
+ **Partner-managed** – A partner maintains the skill.
+ **Community** – A member of the community contributed the skill.

Skills that don't specify a tier appear as **Community**. The tier filter lists only the tiers that skills in the Skills Catalog have.

If your operator role doesn't have the catalog actions, the **Skills Catalog** tab shows **The Skills Catalog isn't available in this environment yet.**

## Adding a skill to your Agent Space
<a name="adding-a-skill-to-your-agent-space"></a>

Before you add a skill, check what it needs to work. Some skills need more AWS Identity and Access Management (IAM) permissions in the roles that AWS DevOps Agent uses to access your accounts. Others need an integration, such as a Model Context Protocol (MCP) server. To find out what a skill needs, read its README.md file, or its SKILL.md file if it has no README.md. If you haven't set up what a skill needs yet, you can add it as inactive.

**To add a skill to your Agent Space:**

1. On the **Skills Catalog** tab, find the skill that you want to add.

1. To add the skill as inactive, choose the dropdown arrow next to **Add to agent space**, and then for **Status**, choose **Inactive**. Agents don't use an inactive skill until you activate it on the **Skills** tab.

1. Choose **Add to agent space**. When the button shows **Installed**, the skill is in your Agent Space. To go to the skill's row on the **Skills** tab, choose **View in Skills**.

Your Agent Space can have one copy of each catalog skill. If you delete your copy, you can add the skill again, as long as the Skills Catalog still lists it.

## How agents use catalog skills
<a name="how-agents-use-catalog-skills"></a>

Agents use a catalog skill only after you add it to your Agent Space, and only while it's active and targets their agent type. They don't browse the Skills Catalog. To check a skill's agent types before you add it, choose **Details**. For more information about how agents use skills, see [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills-index.md).

Your Agent Space can also have another skill with the same name, such as a copy that you imported from GitHub. Agents might use only one of them, so delete the copy that you don't need.

## Viewing catalog skills
<a name="viewing-catalog-skills"></a>

Catalog skills appear in the **Custom skills** section of the **Skills** tab. Each one has a **Latest source on GitHub** link to its folder in the repository. To activate, deactivate, or delete one, use its row, as you do for your other skills. For more information about activating and deleting skills, see [Managing Skills](about-aws-devops-agent-devops-agent-skills-index.md#managing-skills).

To read a catalog skill's files, choose the skill. It opens in its own tab, which shows the skill's current version in the Skills Catalog. If that version is newer than the one in your Agent Space, agents keep using yours until you sync the skill. If the catalog no longer lists the skill, the skill opens in its detail view instead. It also opens there if your operator role doesn't have the catalog actions. The detail view shows the files in your Agent Space.

## Syncing catalog skills
<a name="syncing-catalog-skills"></a>

Syncing updates a catalog skill to its current version in the Skills Catalog. Catalog skills don't update automatically. To sync one, choose **Sync** on the skill's row. AWS DevOps Agent replaces the skill's files, name, description, and agent types with those of the current version. The skill keeps its status. If the skill is already up to date, nothing changes.

If the Skills Catalog no longer lists a skill that you added, the skill stays in your Agent Space and keeps working. You can't sync it, and its row has no **Latest source on GitHub** link. If you delete the skill, you can't add it again.