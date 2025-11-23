# Creating a budget

You can create budgets to track and take action on your costs and usage. You can also
create budgets to track your aggregate Reserved Instance (RI) and Savings Plans utilization and
coverage. By default, single accounts, the management account, and member accounts in an
organization can create budgets.

When you create a budget, AWS Budgets provides a Cost Explorer graph to help you see
your incurred costs and usage. If you didn't enable Cost Explorer yet, this graph is blank
and AWS Budgets will enable Cost Explorer when you create your first budget. You can
create your budget without enabling Cost Explorer. It can take up to 24 hours for this
graph to appear after you or AWS Budgets enable Cost Explorer.

You can create and set up a budget in two ways:

- [Using a budget template (simplified)](budget-templates.md "budget-templates.md")
- [Customizing a budget (advanced)](custom-budgets.md "custom-budgets.md")

## Billing view prerequisites and monitoring

AWS Budgets supports billing views, allowing you to create and manage budgets based
on filtered cost and usage data across multiple accounts within your organization. When
creating a budget, you can select a billing view to define the scope of cost and usage
data the budget will track. For more information on controlling access to cost
management data using billing views, see [Controlling cost management data access with Billing View](billing-view.md "billing-view.md").

###### Note

AWS doesn't support billing transfer views for bill transfer accounts.

Before you use billing views with budgets, consider the following permissions
requirements:

- For cross-account billing views, the source account administrator must
  grant:
  - `budgets:ModifyBudget` permission on the billing view to
    allow target accounts/users to create budgets
  - `billing:GetBillingViewData` permission to access the
    billing view data

- Target accounts/users also need:
  - `iam:CreateServiceLinkedRole` permission for the Budgets service principal
    (budgets.amazonaws.com):

- The service-linked role monitors the health status of your billing view
  access:
  - `HEALTHY`: Indicates the budget has proper access to the
    billing view data
  - `UNHEALTHY`: Indicates the budget cannot access the billing
    view data, which might occur if permissions have been revoked or the
    view has been deleted. Reasons for unhealthy status can be:
    - `BILLING_VIEW_NO_ACCESS`: Indicates that access to
      the billing view associated with the budget has been removed
      (unshared) or the view was deleted.
    - `INVALID_FILTER`: Indicates that the budget's
      filter is invalid. This occurs when a management account becomes
      a linked account but has a budget that references an account
      outside their organization. In this situation, budget spend
      updates are paused.

## Tutorials

You can also use our [walk-through
tutorials](https://console.aws.amazon.com/billing/home#/budgets/overview?tutorials=visible "https://console.aws.amazon.com/billing/home#/budgets/overview?tutorials=visible") to learn how to achieve your objectives with AWS Budgets.

###### To access tutorials

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/cost-management/](https://console.aws.amazon.com/cost-management/ "https://console.aws.amazon.com/cost-management/").
2. In the navigation pane, choose **Budgets**.
3. Next to **Overview**, choose
   **Info**.
4. In the help panel, choose **Tutorials**.
