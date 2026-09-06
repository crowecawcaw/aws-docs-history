

# Creating a usage budget
<a name="create-usage-budget"></a>

Use this procedure to create a budget that's based on your usage.<a name="usage-budget"></a>

**To create a usage budget**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/cost-management/](https://console.aws.amazon.com/cost-management/).

1. In the navigation pane, choose **Budgets**.

1. At the top of the page, choose **Create budget**.

1. Under **Budget setup**, choose **Customize (advanced)**.

1. Under **Budget types**, choose **Usage budget**. Then, choose **Next**.

1. Under **Details**, for **Budget name**, enter the name of your budget. Your budget name must be unique within your account. It can contain A-Z, a-z, spaces, and the following characters:

   ```
   _.:/=+-%@
   ```

1. Under **Choose what you’re budgeting against**, for **Budget against**, choose **Usage type groups** or **Usage types**. A usage type group is a collection of usage types that have the same unit of measure. For example, resources that measure usage by the hour is one usage type group.
   + For **Usage type groups**, choose the unit of measurement and the applicable service usage that you want the budget to monitor.
   + For **Usage types**, choose the specific service usage measurements that you want the budget to monitor.

1. Under **Set budget amount**, for **Period**, choose how often you want the budget to reset the actual and forecasted usage.
   + **Daily** for every day
   + **Monthly** for every month
   + **Quarterly** for every three months
   + **Annually** for every 12 months
   + **Custom** to specify your own start and end dates
**Note**  
With a **Monthly** or **Quarterly** budget period, you can set future budgeted amounts using the budget planning feature. **Custom** period budgets align with time periods outside of standard reset options. For example, you can create a budget period that matches your fiscal year or project timeline.

1. For **Budget renewal type**, choose **Recurring budget** for a budget that resets at the end of each budget period. Or, choose **Expiring budget** for a one-time budget that doesn't reset after the given budget period.

1. Choose the start date or period to begin tracking against your budgeted amount. For an **Expiring budget**, choose the end date or period for the budget to end on.

   All budget times are in the UTC format.

1. For **Budgeting method**, select the way that you want your budget amount to be determined each budget period:
   + **Fixed**: Set one amount to monitor every budget period.
   + **Planned**: Set different amounts to monitor each budget period.
   + **Auto-adjusting**: Set your budget amount to be adjusted automatically based on your usage pattern over a time range that you specify.

   For more information about each method, see [Budget methods](budget-methods.md)

1. (Optional) Under **Budget scope**, for **Filters**, choose **Add filter** to apply one or more of the [available filters](budgets-create-filters.md). Your choice of budget type determines the set of filters that's displayed on the console.
**Note**  
You can't use the **Linked account** filter within a linked account.

1. Choose **Next**.

1. Choose **Add an alert threshold**.

1. Under **Set alert threshold**, for **Threshold**, enter the amount that must be reached for you to be notified. This can be either an absolute value or a percentage. For example, say you have a budget of 200 hours. To be notiﬁed at 160 hours (80% of your budget), enter **160** for an absolute budget or **80** for a percentage budget.

   Next to the amount, choose **Absolute value** to be notiﬁed when your usage exceeds the threshold amount. Or, choose **% of budgeted amount** to be notiﬁed when your usage exceeds the threshold percentage.

   Next to the threshold, choose **Actual** to create an alert for actual usage. Or, choose **Forecasted** to create an alert for forecasted usage.

1. (Optional) Under **Notification preferences**, for **Email recipients**, enter the email addresses that you want the alert to notify. Separate multiple email addresses with commas. A notification can be sent to a maximum of 10 email addresses.

1. (Optional) Under **Notification preferences**, for **Amazon SNS Alerts**, enter the Amazon Resource Name (ARN) for your Amazon SNS topic. For instructions on how to create a topic, see [Creating an Amazon SNS topic for budget notifications](budgets-sns-policy.md).
**Important**  
After you create a budget with Amazon SNS notifications, Amazon SNS sends a confirmation email to the email addresses that you specified. The subject line is **AWS Notification - Subscription Confirmation**. The recipient must choose **Confirm subscription** in the confirmation email to receive future notifications.

1. (Optional) Under **Notification preferences**, for **AWS Chatbot Alerts**, you can choose to configure AWS Chatbot to send budget alerts to an Amazon Chime or Slack chat room. You configure these alerts on the AWS Chatbot console.

1. Choose **Next**.

1. (Optional) For **Attach actions**, you can configure an action that AWS Budgets performs on your behalf when the alert threshold is exceeded. For more information and instructions, see [To configure a budget action](budgets-action-configure.md#create-budget-action).

1. Choose **Next**.
**Note**  
To proceed, you must configure at least one of the following parameters for each alert:  
An email recipient for notifications
An Amazon SNS topic for notifications
A budget action

1. Review your budget settings, and then choose **Create budget**.