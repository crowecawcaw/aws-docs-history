# Manual approval execution block

The manual approval execution block enables you to insert an approval step
that you associate with an IAM role. Users with access to the role can approve or decline
the execution of a step, to pause the step until approval is granted, or, potentially,
prevent the plan from progressing.

To ensure that manual approval is required during plan execution, you input a manual
approval step at a specific location in the workflow, and then configure the IAM role
to specify who can approve the step.

## Configuration

To configure a manual approval execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [Manual approval execution block sample policy](security_iam_region_switch_manual_approval.md "security_iam_region_switch_manual_approval.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **IAM approval role:** Enter the ARN for an IAM
   role that has permission to manually approve execution continuing for the Region switch plan.
   The IAM role must be within the account that is the owner of the plan.
4. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## How it works

By configuring a manual approval execution block, you can require an approval
as part of your application recovery. For a manual execution block, Region switch does the following:

- When Region switch runs a manual execution block, it pauses execution
  and sets the plan's execution status to pending approval.
- Anyone who has access to the role defined in the execution block can approve or decline
  execution of the step.
- If they approve the step execution, Region switch proceeds with execution
  the plan. If they decline, Region switch cancels the plan execution.

This block does not support ungraceful execution mode.

## What is evaluated as part of plan evaluation

Region switch does not complete any evaluations for manual approval execution blocks.
