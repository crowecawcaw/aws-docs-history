# Using a budget template (simplified)

You can create a budget using a template with recommended configurations. Budget
templates are a simplified way to start using AWS Budgets, with a single page
workflow, unlike the 5-step workflow that is required for [Customizing a budget (advanced)](custom-budgets.md "custom-budgets.md").

###### To create a budget using a template

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/cost-management/](https://console.aws.amazon.com/cost-management/ "https://console.aws.amazon.com/cost-management/").
2. In the navigation pane, choose **Budgets**.
3. At the top of the page, choose **Create budget**.
4. Under **Budget setup**, choose **Use a template
   (simplified)**.
5. Under **Templates**, choose a template that best matches your
   use case:
   - **Zero spend budget**: A budget that notifies you
     after your spending exceeds AWS Free Tier limits.
   - **Monthly cost budget**: A monthly budget that
     notifies you if you exceed, or are forecasted to exceed, the budget
     amount.
   - **Daily Savings Plans coverage budget**: A coverage
     budget for your Savings Plans that notifies you when you fall below the defined
     target. This helps you to identify your on-demand spend sooner so that
     you can consider purchasing a new commitment.
   - **Daily reservation utilization budget**: A
     utilization budget for your Reserved Instances that notifies you when
     you fall below the defined target. This helps you to identify when
     you're not using some of your hourly commitment that you already
     purchased.

6. Update the details and settings for your specific template.
7. Choose **Create budget**.
   While each template has default configurations, they can be changed later. This way,
   you can use it to create most of the budget, and then edit certain settings in the
   advanced workflow, such as adding a linked account or a cost category filter. To change
   any of the settings, under **Template settings**, choose
   **Custom**.

You can also download a template for offline use in [AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") or [CloudFormation](../../../AWSCloudFormation/latest/UserGuide/AWS_Budgets.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Budgets.md"), for
example. To download a template, under **Template settings**, choose
**JSON**.
