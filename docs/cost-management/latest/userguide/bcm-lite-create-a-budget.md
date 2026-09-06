

# Create a budget in the AWS Billing and Cost Management console
<a name="bcm-lite-create-a-budget"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You can create budgets for each project to track and take action on your costs and usage. In the AWS Billing and Cost Management console, you can create cost budgets and usage budgets, but you cannot create spend limits. For more information about budgets, see [Use a budget in the AWS Billing and Cost Management console](bcm-lite-use-budget.md).

When you create a budget, AWS Budgets creates a graph to help you see your costs. It can take up to 24 hours for this graph to appear.

**To create a budget**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Budgets**.

1. For **Budget monitoring**, choose **Create budget**.

1. For **Budget setup**, choose a setup type. We recommend that you use a template budget.
   + If you choose **Use a template (simplified)**, do the following:

     1. Choose a template.

     1. For **Budget name**, enter a name for your budget.

     1. For **Email recipients**, enter up to 10 email recipients you want to notify when this project exceeds your budget.

     1. Choose **Create**.

        You can change the default configuration, like which services are included in the budget after your budget is created.
   + If you choose **Customize (advanced)**, follow the instructions for [Creating a cost budget or Creating a usage budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) based on your budget type.