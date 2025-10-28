# Reviewing and approving your budget

action

You receive a notification to inform you that an action is pending or has already run
on your behalf, regardless of your action preferences. The notification includes a link
to the **Budget details** page of the action. You can also navigate to
the **Budget details** page by choosing the budget name on the
AWS Budgets page.

On the **Budget details** page, you can review and approve your
budget action.

###### To review and approve your budget action

1. On the **Budget details** page, in the
   **Alerts** section, choose **Requires
   approval**.
2. In the **Actions** pop-up, choose the name of the alert that
   requires an action.
3. On the **Alert details** page, in the
   **Action** section, review the action that requires
   approval.
4. Select the action that you want to run, and then choose **Run
   action**.
5. Choose **Yes, I am sure**.
   Your pending actions move from the `pending` status in **Action
   history**, listing the newest actions at the top. AWS Budgets shows
   actions configured and run in the last 60 days. You can view the full history of actions
   by using AWS CloudTrail or by calling the `DescribeBudgetActionHistories`
   API.

## Reversing a previous action

You can review and undo previously completed actions from the **Action
history** table. Each status is defined as follows:

- **Standby** - AWS Budgets is actively evaluating the
  action.
- **Requires approval** - The action was initiated, and is
  waiting for your approval.
- **Completed** - The action successfully completed.
- **Reversed** - The action was undone, and AWS Budgets
  will no longer evaluate the action for the remaining budgeted period.

If you want AWS Budgets to re-evaluate the reversed action during the same
period, you can choose **Reset**. You can do this, for example, if
you initiated a read-only policy but then received approval from your manager to
increase your budget and adjust your budgeted amount during the current
period.
