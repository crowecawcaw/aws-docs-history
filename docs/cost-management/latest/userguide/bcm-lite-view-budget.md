# View your budget in the AWS Billing and Cost Management console

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You can view all your budgets, including spend limits in the AWS Billing and Cost Management console.
AWS Budgets information is updated up to three times a day. There can be a delay between
when you incur a charge and when you receive a notification from AWS Budgets for the
charge. This is due to a delay between when an AWS resource is used and when that resource
usage is billed. You might incur additional costs or usage that exceed your budget
notification threshold before AWS Budgets can notify you, and your actual costs or usage
may continue to increase or decrease after you receive the notification.

Both project owners and project team members can view budgets.

## View your budget

You can view your budget in two ways. First, you can choose the checkbox next to your
budget to open the split-view panel. Second, you can choose the budget name to open the
budget details page.

## View your budget using the split-view panel

To view your budget using the split-view panel, choose the checkbox next to your
budget. You'll have access to the following:

- **Budget preview.** Your budget preview shows a
  filterable table with the following:

  - Current costs and usage for a budget during the budget
    period.
  - Budgeted costs or usage for the budget
    period.
  - Forecasted usage or costs for the budget
    period.
  - Indicators of when your alerts will be
    triggered.

- **Alerts.** Your alerts are listed with any
  notifications or information about the state of your budget.

## View your budget in the budget details page

To view your budget using the budget details page, choose your budget name to open
the budget details page. You'll have access to the following:

- **Budget health**: This is the overall state of
  your budget. This includes two key values:

  - **Current vs. budgeted** – Your
    current incurred costs compared to your budgeted costs.
  - **Forecasted vs. budgeted** – Your
    current forecasted costs compared to your budgeted
    costs.

- **Alerts**: Your alerts are listed with any
  notifications or budget actions that AWS Budgets might take on your resources.
  You can choose **View all alerts** to open the Alerts tab to
  edit or delete alerts.
- **Details**: This shows the budget type, amount,
  and additional parameters for your budget.
- **Budget history**: This chart and table show the
  history of your budget. This history is only supported for quarterly budgets
  which show the last four quarters of history and monthly budgets which show the
  last 12 months of budget history.

If you have a custom time period for your budget, if you have multi-year data
disabled, you can view up to 14 months of historical data.

- **Tags**: You can view or add tags associated
  with your budget.

## Download your data in a CSV file

You can download your budgets as a CSV file. The file includes all of the data for all
of your budgets, such as Budget Name, Current Value and Forecasted Value, Budgeted
Value, and more.

###### To download a budget

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/cost-management/](https://console.aws.amazon.com/cost-management/ "https://console.aws.amazon.com/cost-management/").
2. On the navigation pane, choose **Budgets**.
3. Choose **Download CSV**.
4. Open or save your file.
