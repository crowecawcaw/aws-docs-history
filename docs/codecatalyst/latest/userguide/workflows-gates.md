

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Gating a workflow run
<a name="workflows-gates"></a>

A *gate* is a workflow component that you can use to prevent a workflow run from proceeding unless certain conditions are met. An example of a gate is the **Approval** gate where users must submit an approval in the CodeCatalyst console before the workflow run is allowed to continue.

You can add gates between sequences of actions in a workflow, or before the first action (which runs immediately after the **Source** downloads). You can also add gates after the last action, if you have a need to do so.

For more information about workflow runs, see [Running a workflow](workflows-working-runs.md).

**Topics**
+ [Gate types](#workflows-gates-types)
+ [Can I set up a gate to run in parallel to another action?](#workflows-approval-parallel)
+ [Can I use a gate to prevent a workflow run from starting?](#workflows-gates-prevent)
+ [Limitations of gates](#workflows-gate-limitations)
+ [Adding a gate to a workflow](workflows-gates-add.md)
+ [Sequencing gates and actions](workflows-gates-depends-on.md)
+ [Specifying the version of a gate](workflows-gates-version.md)

## Gate types
<a name="workflows-gates-types"></a>

Currently, Amazon CodeCatalyst supports one type of gate: the **Approval** gate. For more information, see [Requiring approvals on workflow runs](workflows-approval.md).

## Can I set up a gate to run in parallel to another action?
<a name="workflows-approval-parallel"></a>

No. Gates can only run before or after an action. For more information, see [Sequencing gates and actions](workflows-gates-depends-on.md).

## Can I use a gate to prevent a workflow run from starting?
<a name="workflows-gates-prevent"></a>

Yes, with qualifications.

You can prevent a workflow run from *performing tasks*, which is slightly different from preventing it from *starting*.

To prevent a workflow from performing tasks, add a gate before the very first action in a workflow. In this scenario, a workflow run *will start*—meaning it will download your source repository files—but it will be prevented from performing tasks until the gate is unlocked.

**Note**  
Workflows that start and then get blocked by a gate still count against your *Maximum number of concurrent workflow runs per space* quota and other quotas. To ensure that you do not exceed workflow quotas, consider using a workflow trigger to conditionally start a workflow instead of using a gate. Also consider using a pull request approval rule instead of a gate. For more information about quotas, triggers, and pull request approval rules, see [Quotas for workflows in CodeCatalyst](workflows-quotas.md), [Starting a workflow run automatically using triggers](workflows-add-trigger.md), and [Managing requirements for merging a pull request with approval rules](source-pull-requests-approval-rules.md).

## Limitations of gates
<a name="workflows-gate-limitations"></a>

Gates have the following limitations:
+ Gates cannot be used in conjunction with the compute sharing feature. For more information about this feature, see [Sharing compute across actions](compute-sharing.md).
+ Gates cannot be used within action groups. For more information about action groups, see [Grouping actions into action groups](workflows-group-actions.md).