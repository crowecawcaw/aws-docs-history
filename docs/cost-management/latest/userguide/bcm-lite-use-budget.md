

# Use a budget in the AWS Billing and Cost Management console
<a name="bcm-lite-use-budget"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

The following information is about creating a budget in the AWS Billing and Cost Management console when you're using our [new AWS experience](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html). If you created your account using [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) or [activated advanced features](https://docs.aws.amazon.com/accounts/latest/reference/activate-advanced-features.html), see [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

You can use AWS Budgets to enable cost and usage tracking. Some examples include:
+ Setting a monthly cost budget with a fixed target amount to track all costs associated with your account.
+ Setting a monthly cost budget with a variable target amount, assuming that each month, your budget should grow by 5 percent.
+ Setting a custom period budget that aligns with your project duration or grant period.

You can create the following types of budgets:
+ **Cost budgets**: Set limits for services and receive alerts when costs approach or exceed your defined threshold.
+ **Usage budgets**: Establish usage limits for one or more services and get notified when usage approaches or exceeds your set threshold.
+ **Spend limits**: Create a total monthly limit for each project you own. AWS will take cost-saving actions such as pausing unused resources to make sure your monthly costs never exceed your monthly limit. You can't create a spend limit in the AWS Billing and Cost Management console, but you can create one in AWS Settings. For more information, see [Create a spend limit in AWS Settings](https://docs.aws.amazon.com/accounts/latest/reference/create-spend-limit.html).

## Budget considerations
<a name="bcm-lite-budget-considerations"></a>

When creating a budget, consider the following:
+ AWS Budgets information is updated up to three times a day. Updates typically occur 8–12 hours after the previous update.
+ There can be a delay between when you incur a charge and when you receive a notification from AWS Budgets for the charge. This is due to a delay between when an AWS resource is used and when that resource usage is billed. You might incur additional costs or usage that exceed your budget notification threshold before AWS Budgets can notify you, and your actual costs or usage may continue to increase or decrease after you receive the notification.
+ Budgets can track your blended, unblended, net unblended, amortized, and net amortized costs.
+ Budgets can include or exclude charges such as discounts, refunds, support fees, and taxes.
+ You can set up optional notifications that warn you if you exceed, or are forecasted to exceed, your budgeted amount for cost or usage budgets. You can have notifications sent to an Amazon SNS topic, to an email address, or to both. For more information, see [Creating an Amazon SNS topic for budget notifications](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-sns-policy.html).
+ Project team members can create budgets, but cannot create spend limits.
+ A budget is visible to project team members.

## Budget actions
<a name="bcm-lite-budget-actions"></a>

Budget actions are actions run by AWS Budgets on your behalf. This could include sending a message, stopping the creation of a new resource, or performing a cost-saving action associated with a usage plan. You cannot create any new service control policies for your budget.

For more information about AWS Budgets actions, see [Configuring budget actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html).

## Best practices
<a name="bcm-lite-budget-best-practices"></a>

Use the following best practices when you're working with budgets.

### Set budgets on a recurring basis
<a name="bcm-lite-setting-budgets"></a>

You can set budgets on a recurring basis or for a specific time frame. This gives you insight into your costs. This also makes sure you don't unexpectedly stop receiving budget alerts.

### Use custom period budgets
<a name="bcm-lite-custom-period-budgets"></a>

You can set a start and end date for your budgeting cycle. Use a custom period budget for your project duration or grant period and combine them with other budget types. When you use a custom budget, consider the following:
+ The end date of your budgeting cycle must be within three years of the start date.
+ For amount calculations, only the date (00:00 UTC) is used. The end date is excluded from calculations.
+ Custom period budgets don't auto-renew and expire on the end date.

### Use advanced options when you need them
<a name="bcm-lite-advanced-cost-budgets"></a>

Cost budgets can be aggregated by blended, unblended, net unblended, amortized, or net amortized costs. Cost budgets can also include or exclude refunds, credits, taxes, and support charges. Create a budget that uses the financial information you care about.

### Set budget alerts
<a name="bcm-lite-budget-alerts"></a>

Send budget alerts to places you regularly access to stay on top of your costs.

When you set budget alerts, consider the following:
+ You can send budget alerts to up to 10 email addresses and one Amazon SNS topic.
+ You can create alerts for actual values or forecasted values.
+ Actual alerts are only sent once per budget, per budget period.
+ Forecasted-based alerts can be sent out more than once per budget, per budget period. This is because forecasted values can change.
+ AWS requires 5 weeks of usage data to generate budget forecasts. Any forecasted-based alerts won't be sent out until AWS has enough historical information.

### Send your budget alerts to an Amazon SNS topic
<a name="bcm-lite-budget-alerts-sns"></a>

You can send your budget alert to an Amazon SNS topic to deliver the alert message to multiple subscribers, including Lambda functions, SMS text messages, and service providers like Datadog or Splunk.

For budget notifications to be sent successfully, your budget must have permissions to send a notification to your topic, and you must accept the subscription to the Amazon SNS notification topic. For more information, see [Creating an Amazon SNS topic for budget notifications](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-sns-policy.html).

### Tag your budgets
<a name="bcm-lite-budget-tagging"></a>

You can use tags to help organize your AWS Budgets resources. You can add, update, or remove tags from your AWS Budgets resources at any time. If you create a tag, you won't see it in any cost or usage data.

### Create a spend limit in AWS Settings
<a name="bcm-lite-create-spend-limit-settings"></a>

You can create a spend limit to set the most you'll ever pay per month for each project. This feature is only available using the AWS Settings console, but you can view your spend limit and service-related costs in the AWS Billing and Cost Management console. Anyone with access to a project can view a spend limit, but only project owners can modify them. Your account must be on the Paid Plan to access a spend limit. For more information, see [Upgrade your account in AWS Settings](https://docs.aws.amazon.com/accounts/latest/reference/upgrade-account.html).