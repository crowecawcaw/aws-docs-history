

# Remediating grouped findings with remediation plans

In the AWS Transform web application, continuous modernization groups your findings by the problem they share. Instead of remediating findings one at a time, you review each group, choose how to fix it, and remediate several groups together in a *remediation plan*. When no AWS managed or custom transformation covers a group, AWS Transform can generate a *specialized skill* for it.

The workflow has three parts:

1. [Reviewing grouped findings](#ct-finding-groups) – Find the groups that matter most and check how each one can be fixed.

1. [Generating specialized skills](#ct-specialized-skills) – Generate a fix for a group that has none.

1. [Remediating groups with a remediation plan](#ct-plans) – Put groups in a plan, approve each group's fix, and remediate.

## Reviewing grouped findings
<a name="ct-finding-groups"></a>

AWS Transform creates and maintains groups for you; you can't create or edit a group. A group collects the findings, across your repositories, that share the same problem. Findings that aren't in a group are *standalone* findings.

To view groups, open the **Findings** tab. The tab has the following views:
+ **Recommended** – High-severity groups that have a remediation, followed by high-severity standalone findings that have a remediation. This is the default view.
+ **Groups** – Every group that has open findings. Standalone findings are listed in **Recommended** (high severity, with a remediation) and in **All findings**.
+ **Skill generations** – Specialized skills that are being generated, or are ready for review. This view appears after you start generating a specialized skill. For more information, see [Generating specialized skills](#ct-specialized-skills).
+ **All findings** – Every finding, without grouping.

### Groups list
<a name="ct-finding-groups-list"></a>

For each group, the list shows the following:
+ **Finding** – The problem the group's findings share, and the number of findings in the group. Expand the row to see the findings.
+ **Scope** – The number of repositories that the group's findings are in.
+ **Remediation** – How the group can be fixed. For example: 
  + **Ready** – An AWS managed or custom transformation, or an approved specialized skill, fixes the group.
  + **Needs review** – A specialized skill is ready for you to review.
  + **No matching skill yet** or **Generate specialized skill** – No transformation covers the group. You can generate a specialized skill for it.
  + **Generating skill** – A specialized skill is being generated for the group.
  + **View remediation plan** – A plan that hasn't started yet already holds the group.
  + **No remediation available** – AWS Transform can't remediate the group.
+ **Severity** – The highest severity among the group's open findings.

A warning icon means that the group misses the safety bar. For more information, see [Safety bar](#ct-finding-groups-safety). The **AWS Health** tag means that the group has findings from an AWS Health readiness analysis.

To narrow the list, use the search box and the **Repository**, **Remediation**, and **Analysis** filters. The **Remediation** filter has the options **Transformation ready**, **Needs a skill**, and **Generating skill**.

### Group details
<a name="ct-finding-groups-details"></a>

Choose a group's name to open its page. The page shows the following:
+ **Summary** and **Technology** – What the problem is, and the technology it affects.
+ **Group status** – **Actionable** if the group has open findings, or **Inactive** if it doesn't.
+ **Recommendation** – The fix AWS Transform recommends: an AWS managed transformation, a custom transformation, or a specialized skill.
+ **Affected repositories** – The repositories that the group's findings are in.
+ **Progress** – How many of the group's findings are change ready.
+ **Safety bar** – Whether the group meets the safety bar.
+ **Skill creation job** – The status of the group's specialized skill generation, if one was started.
+ **Findings** – Each finding in the group, with its repository, analysis, severity, status, and transformation.

From a group's page, you can choose **Create remediation plan**. If a plan that hasn't started yet already holds the group, choose **View remediation plan** instead.

### Safety bar
<a name="ct-finding-groups-safety"></a>

The safety bar is a set of conditions that AWS Transform checks before it remediates a group. A group either **Meets the safety bar**, **Misses the safety bar**, or the safety bar **Doesn't apply** to it. A group can miss the following conditions:
+ **Cross-repository dependency** – Some of the group's repositories might depend on each other. AWS Transform can't order changes across repositories yet, so merging their pull requests out of order might break the build. Merge them in dependency order.
+ **Mixed environments** – The group's findings span programming languages or package ecosystems that one fix can't serve.
+ **Multiple fixes** – Some of the group's findings need a different change from the rest.

Each condition the group misses comes with a sentence that says which findings or repositories it applies to.

You can still remediate a group that misses the safety bar. When you approve its fix, you must confirm that you have seen the conditions it misses.

**Note**  
AWS Transform detects only build-time links between repositories, such as one repository that consumes another's artifact. Check runtime links, such as service-to-service calls, before you remediate.

## Generating specialized skills
<a name="ct-specialized-skills"></a>

When no AWS managed or custom transformation covers a group, AWS Transform can build a *specialized skill* for it. A specialized skill is a set of instructions, written to a `SKILL.md` file, that remediates the group's findings. You review the skill before AWS Transform uses it.

### Prerequisites
<a name="ct-specialized-skills-prerequisites"></a>
+ A deployed AWS Batch or Amazon EC2 stack in your AWS account, and an up-to-date dispatcher. AWS Transform generates the skill on this stack. To deploy or update them, open the **Settings** tab. For more information, see [Infrastructure modes](ct-working-with.md#ct-web-application-prerequisites).
+ The group has open findings, and no skill is already being generated for it.

### Generate a specialized skill
<a name="ct-specialized-skills-generate"></a>

1. On the **Findings** tab, find the group, and then choose **Generate specialized skill** in its **Remediation** column.

1. Review the estimate. Generating a skill typically takes 2–4 hours and uses 300–600 agent minutes, billed at your account's agent-minute rate. This is more than running an existing transformation.

1. Select the stack to run on, and then choose **Generate specialized skill**.

The job runs in the background, so you can leave the page. To track it, open the **Skill generations** view on the **Findings** tab, or the group's page. The view shows the job's progress and the agent minutes it has used so far. If a job fails, see [If generation fails](#ct-specialized-skills-failures).

To stop a job, choose **Stop**, and then choose **Stop generating**. The job stops where it is, and nothing is saved from it. You can generate the skill again afterwards.

**Important**  
If you stop a job, you still pay for the agent minutes it used up to that point.

### Review a specialized skill
<a name="ct-specialized-skills-review"></a>

When a skill is ready, its group shows **Needs review**. You review the skill from a remediation plan that holds the group. For more information, see [Review and approve groups](#ct-plans-approve).

The review shows the skill's **Target**, **Approach**, **Guardrails**, and **Validation**. To change the skill, choose **Edit skill** and edit its `SKILL.md` file. The file's front matter must keep its `name` and `description`, you can't change the name, and the name can't start with `AWS/`.

When you approve a skill, choose how to save it:
+ **Publish** – Saves the skill to your registry, where it's listed with your transformations.
+ **Save as draft** – Saves the skill to your registry as a draft. Drafts expire 30 days after they are saved.
+ **One-off** – Uses the skill for this group only. Nothing is saved.

### If generation fails
<a name="ct-specialized-skills-failures"></a>

The **Skill generations** view shows why a job failed. Common reasons include the following:
+ The job used up its agent-minute budget.
+ None of the sample repositories could be built.
+ The specialized skill did not pass its validation.
+ The job ran past its time limit.

To try again, choose **Generate specialized skill** for the group again.

## Remediating groups with a remediation plan
<a name="ct-plans"></a>

A remediation plan holds groups that you remediate together. Nothing runs when you create a plan. On the plan's page, you approve each group's fix, and then you choose **Remediate**. Each repository gets one pull request, with the changes from all of its groups.

Your remediation plans are listed on the **Remediations** tab, above your remediations. The list shows each plan's progress and whether it needs your attention.

### Create a remediation plan
<a name="ct-plans-create"></a>

1. In the AWS Transform web application, open the **Findings** tab, and then open the **Recommended** or **Groups** view.

1. Select the groups to remediate.

1. Choose **Create remediation plan**.

AWS Transform creates the plan, named after its groups, and opens its page. To rename the plan or edit its description, choose **Actions** on the plan's page. To create a plan for one group, you can also choose **Create remediation plan** on the group's page.

To remediate only some of a group's repositories, expand the group and select findings in those repositories instead of the whole group. The plan keeps every finding in each repository that you select a finding from, and leaves out the group's other repositories.

### Review and approve groups
<a name="ct-plans-approve"></a>

The plan's page shows how many of its groups are ready. A group is ready after you approve its fix.

1. Choose **Review next**, or choose **Review** in a group's row.

1. Review the recommended fix. To use an AWS managed or custom transformation instead of the specialized skill, choose that transformation.

1. If the group misses the safety bar, review the conditions it misses, and then confirm that you have seen them.

1. Choose **Approve specialized skill** or **Use this transformation**.

An approved fix becomes the group's chosen recommendation in every plan, and stays after you delete the plan. To change an approval, choose **Change** in the group's row.

#### Auto-approve specialized skills
<a name="ct-plans-auto-approve"></a>

To approve every specialized skill in the plan that's ready for review without reviewing each one, turn on **Auto-approve specialized skills** on the plan's page, review the list of skills, and then choose **Approve**. Skills that are still being generated aren't included.

**Important**  
Auto-approve also approves groups that miss safety conditions. Before you use it, check which groups miss the safety bar.

### Change what a plan covers
<a name="ct-plans-scope"></a>

After you create a plan, you can change what it covers of each group. These changes apply to this plan only. The group and its findings don't change.

To leave repositories out of a group:

1. In the group's row, choose the edit icon after the group's counts.

1. In **Edit repositories**, clear the repositories to leave out. For a repository that the plan covers only in part, choose **Leave out** to leave all of it out, or select it to cover all of its findings.

1. Choose **Save**.

The row then shows how many findings the plan leaves out. If the change affects the safety bar, the group might need review again, or its recommendation might become approved. Keep at least one repository. To leave the whole group out, remove it from the plan instead.

To remove a group from the plan, choose **Remove from this plan** in its row. Removed groups are listed on the plan's page, where you can choose **Add back**.

You can't change a group's repositories in the following cases:
+ A remediation is running for the group.
+ The group has no open findings.
+ The group has 1,000 or more open findings. To remediate one repository's findings in a group that large, filter **All findings** by repository and create a remediation.

### Remediate the plan
<a name="ct-plans-remediate"></a>

To remediate a plan, you need deployed infrastructure in your AWS account that is up to date. Remediating a plan uses a newer remediation command than single remediations do, so if your stack was deployed before remediation plans were available, update it on the **Settings** tab first, as you would to generate a specialized skill. For more information, see [Infrastructure modes](ct-working-with.md#ct-web-application-prerequisites).

1. On the plan's page, choose **Remediate**.

1. Review what starts. Groups that can't start now are listed under **Not started with the rest**, with the reason. For the limits on what one start takes, see [Plan limits](#ct-plans-limits).

1. Choose **Start {{n}} remediations**.

Each repository's pull request opens when its remediation succeeds. The **Remediations** section of the plan's page shows each group's progress.

To see the result for each repository, choose **View outcome** in a group's row. Each repository shows one of the following outcomes: **Applied**, **No changes**, **Failed**, **Cancelled**, **Skipped**, **In progress**, or **Waiting to start**. To retry a repository, choose its retry action. The group starts again in that repository only.

If a group needs attention after its remediation, choose **Remediate** again. The group starts again only where it still has open findings.

### Delete a remediation plan
<a name="ct-plans-delete"></a>

On the plan's page, choose **Actions**, and then choose **Delete plan**. The plan's groups and findings stay as they are, and remediations that already started from the plan are kept.

### Plan limits
<a name="ct-plans-limits"></a>

When you create plans:
+ You can create a plan with up to 40 groups.
+ A group can be in up to 50 plans, and an account can have up to 20,000 plans.
+ A plan name can be up to 256 characters, and a description up to 2,048 characters.
+ You can select part of a group only if it has fewer than 1,000 findings.

When you remediate a plan:
+ A repository's pull request holds up to 10 groups and 250 findings. If a repository has more, the extra groups wait. Start them after the first groups have started.
+ A group starts only if it has 250 or fewer open findings in each repository. To remediate a repository with more, filter **All findings** by repository and create a remediation, with up to 250 findings at a time.
+ One **Remediate** starts up to 20 remediations, 200 groups, and 5,000 open findings. Groups past that wait under **Not started with the rest**. Start them after the others have started.
+ A group that includes a repository from a local upload can't start. Leave that repository out of the group in the plan, or create a plan without its findings. For more information, see [Change what a plan covers](#ct-plans-scope).