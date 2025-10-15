# Create a budget for a Deadline Cloud queue

To create a budget, use the following procedure.

1. If you haven't already, sign in to the AWS Management Console, open the Deadline Cloud [console](https://us-west-2.console.aws.amazon.com/deadlinecloud/home "https://us-west-2.console.aws.amazon.com/deadlinecloud/home"), choose a farm, and then choose **Manage
 jobs**.
2. From the **Budget manager** page, choose **Create
 budget**.
3. In the details section, enter a **Budget name** for the
 budget.
4. (Optional) In the description field, enter a brief description of the
 budget.
5. From **Resource**, use the **Queue**
 dropdown to select the queue that you want to create a budget for.
6. For **Period**, set the start and end date for the budget by
 completing the following steps:


	1. For **Start date**, enter the first date of the
	 budget tracking in YYYY/MM/DD format, or choose the
	 **calendar** icon and select a
	 **date**. 
	
	
	The default start date is the date that the budget is created.
	2. For **End date**, enter the last date of the budget
	 tracking in YYYY/MM/DD format or choose the
	 **calendar** icon and select a
	 **date**. 
	
	
	The default end date is 120 days from the start date.
7. For **Budget amount**, enter the dollar amount of the
 budget.
8. (Optional) We recommend that you create limit alerts. In the **Limit
 actions** section, you can implement automated actions that occur
 when specific amounts remain in the budget. To do this, complete the following
 steps:


	1. Choose **Add new action**.
	2. For **Remaining amount**, enter the dollar amount
	 that you want to start the action.
	3. In the **Action** dropdown, choose the action that
	 you want. Actions include:
	
	
	
	
		* **Stop after finishing current
		 work** â All work currently running when the
		 threshold amount is met continue to run (and incur costs) until
		 finished.
		* **Immediately stop work**
		 â All work is canceled immediately when the threshold
		 amount is met.
	4. To create additional limit alerts, choose **Add new
	 action** and repeat the previous steps.
9. Choose **Create budget**.
