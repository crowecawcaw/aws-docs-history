

# Customizing a Savings Plans budget
<a name="sp-create-savingsplans-budget"></a>

Use the following procedure to create a customized budget for Savings Plans utilization or Savings Plans coverage.

You can customize a budget to set parameters specific to your use case. You can customize the time period, the start month, and specific accounts. Creating a customized budget involves a 5-step workflow.<a name="savingsplans-budget"></a>

**To create a Savings Plans budget**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Budgets**.

1. At the top of the page, choose **Create budget**.

1. Under **Budget setup**, choose **Customize (advanced)**.

1. Under **Budget types**, choose **Savings Plans budget**.

1. Choose **Next**.

1. For **Budget name**, enter the name of your budget. Your budget name must be unique within your account and can use A-Z, a-z, spaces, and the following characters:

   ```
   _.:/=+-%@
   ```

1. For **Period**, choose how often you want the budget to reset the actual and forecasted spend. Choose **Daily** for every day, **Monthly** for every month, **Quarterly** for every three months, or **Annually** for every year. All budget times are in UTC.

1. For **Monitor my spend against**, choose what you want the budget to track.

   **Utilization of Savings Plans** is how much of your Savings Plans you've used.

   **Coverage of Savings Plans** is how much of your usage a Savings Plan covers.

1. For **Utilization threshold**, enter the utilization percentage that you want AWS to notify you at. For example, for a utilization budget where you want to stay above 90 percent Savings Plans utilization, enter **90**, and the budget notifies you when your overall Savings Plans utilization goes below 90 percent.

1. For **Coverage threshold**, enter the coverage percentage that you want AWS to notify you at. For example, for a coverage budget where you want to stay above 80 percent, enter **80**. Budget notifies you when your overall coverage goes below 80 percent.

1. Under **Budget scope**, add [filtering](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-create-filters.html) and use advanced options to narrow the set of cost information tracked as part of your budget.

1. Choose **Next**.

1. Under **Alert settings**, choose whether to send budget alerts via email and/or Amazon SNS topic.

1. For **Email recipients**, enter the email addresses that you want the notifications to be sent to. Separate multiple email addresses with a comma. A notification can have up to 10 email addresses.

1. (Optional) For **Amazon SNS ARN**, enter the Amazon Resource Name (ARN) for your Amazon SNS topic.

   If you want to use an Amazon SNS topic for your notification but don't have one, see [Create a Topic](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) in the *Amazon Simple Notification Service Developer Guide*.

   AWS verifies that your budget has permission to send notifications to your Amazon SNS topic by sending a test email to your Amazon SNS topic. 

   For a sample policy and instructions on granting your budget permissions, see [Creating an Amazon SNS Topic for Budget Notifications](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-sns-policy.html). A notification can be subscribed to only one Amazon SNS topic.

1. Choose **Next**.

1. Choose **Create budget**.