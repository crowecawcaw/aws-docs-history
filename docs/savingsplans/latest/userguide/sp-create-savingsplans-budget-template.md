

# Using a template to create a Savings Plans budget
<a name="sp-create-savingsplans-budget-template"></a>

Use the following procedure to create a coverage budget for your Savings Plans using a template.

You can create a budget using a template with recommended configurations. Budget templates are a simplified way to start using AWS Budgets, with a single page workflow, unlike the 5-step workflow that is required for [Customizing a budget (advanced)](https://docs.aws.amazon.com/cost-management/latest/userguide/custom-budgets.html).

**To create a Savings Plans coverage budget using a template**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Budgets**.

1. At the top of the page, choose **Create budget**.

1. Under **Budget setup**, choose **Use a template (simplified)**.

1. Under **Templates**, choose **Daily Savings Plans coverage budget**.

1. For **Budget name**, enter the name of your budget. Your budget name must be unique within your account and can use A-Z, a-z, spaces, and the following characters:

   ```
   _.:/=+-%@
   ```

1. For **Coverage threshold**, enter the coverage percentage that you want AWS to notify you at. For example, for a coverage budget where you want to stay above 80 percent, enter **80**. Budget notifies you when your overall coverage goes below 80 percent.

1. For **Email recipients**, enter the email addresses that you want the notifications to be sent to. Separate multiple email addresses with a comma. A notification can have up to 10 email addresses.

1. Choose **Create budget**.