# ARC Region switch plan execution block

The Region switch plan execution block allows you to orchestrate the order in which multiple applications switch
over to the Region that you want to activate, by referencing other, child Region switch plans. Using this
parent/child relationship, you can create complex, coordinated recovery processes that manage
multiple resources and dependencies across your infrastructure.

## Configuration

When you use the Region switch plan execution block, you select a specific Region switch plan that you want to be
executed in the workflow of the plan you're creating.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [Region switch plan execution block sample policy](security_iam_region_switch_plan_execution.md "security_iam_region_switch_plan_execution.md").

To configure a Region switch plan execution block, enter the following values:

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **Region switch plan:** Select a plan to execute
   in the workflow for the current plan.

Then, choose **Save step.**

## How it works

Use the Region switch plan execution block to create parent workflows with parent/child relationships.
Note that this execution block does not support additional levels of child plans, and limits the number of parent child plans.
Child plans must support the same Regions that the parent plan supports, and must have the same recovery approach
as the parent plan (that is, active/active or active/passive).

This block supports both graceful and ungraceful execution modes. Ungraceful settings will start child
plans with their ungraceful configuration. If Region switch block was executed gracefully, and then switched to
ungraceful execution mode, any child plan will also switch to ungraceful execution mode.

## What is evaluated as part of plan evaluation

If you share a plan across accounts, and the plan is no longer shared with the account of the parent plan,
Region switch evaluation returns a warning that the plan is not valid.
