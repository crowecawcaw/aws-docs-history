

# Create a budget for a Deadline Cloud queue
<a name="create-budget"></a>

To create a budget, use the following procedure.

1. If you haven't already, sign in to the AWS Management Console, open the Deadline Cloud [ console](https://us-west-2.console.aws.amazon.com/deadlinecloud/home), choose a farm, and then choose **Manage jobs**.

1. From the **Budget manager** page, choose **Create budget**.

1. In the details section, enter a **Budget name** for the budget.

1. (Optional) In the description field, enter a brief description of the budget.

1. From **Resource**, use the **Queue** dropdown to select the queue that you want to create a budget for.

1. For **Period**, set the start and end date for the budget by completing the following steps:

   1. For **Start date**, enter the first date of the budget tracking in YYYY/MM/DD format, or choose the **calendar** icon and select a **date**. 

      The default start date is the date that the budget is created.

   1. For **End date**, enter the last date of the budget tracking in YYYY/MM/DD format or choose the **calendar** icon and select a **date**. 

      The default end date is 120 days from the start date.

1. For **Budget amount**, enter the dollar amount of the budget.

1. (Optional) We recommend that you create limit alerts. In the **Limit actions** section, you can implement automated actions that occur when specific amounts remain in the budget. To do this, complete the following steps:

   1. Choose **Add new action**.

   1. For **Remaining amount**, enter the dollar amount that you want to start the action.

   1. In the **Action** dropdown, choose the action that you want. Actions include:
      + **Stop after finishing current work** – All work currently running when the threshold amount is met continue to run (and incur costs) until finished.
      + **Immediately stop work** – All work is canceled immediately when the threshold amount is met.

      For details about how each action affects running and new work, see [How budget actions affect running and new work](budget-actions.md).

   1. To create additional limit alerts, choose **Add new action** and repeat the previous steps.

1. Choose **Create budget**. 