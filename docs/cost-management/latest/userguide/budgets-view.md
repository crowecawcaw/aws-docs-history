# Viewing your budgets

You can view the state of your budgets at a glance on the **Budgets
Overview** page. Your budgets are listed in a filterable table along with the
following data:

- Your current costs and usage incurred for a budget during the budget period
- Your budgeted costs or usage for the budget period
- Your
  forecasted
  usage or costs for the budget period
- A percentage that shows your costs or usage compared to your budgeted
  amount
- A percentage that shows your
  forecasted
  costs or usage compared to your budgeted amount
- The billing view associated with the budget and its health status:
  - `HEALTHY`: Indicates the budget has proper access to the
    billing view data
  - `UNHEALTHY`: Indicates the budget cannot access the billing
    view data, which may occur if permissions have been revoked or the view has
    been deleted

###### Note

When accessing budget performance history for a budget based on a cross-account
billing view, you need the `billing:GetBillingViewData` permission. This
permission is required because the operation provides historical cost and usage data
from the source account's billing view.

AWS doesn't support billing transfer views for bill transfer accounts.

###### To view your budgets

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/cost-management/](https://console.aws.amazon.com/cost-management/ "https://console.aws.amazon.com/cost-management/").
2. On the navigation pane, choose **Budgets**.
3. To see the filters and cost variances for your budgets, choose the budget's name
   in your list of budgets.

###### Note

You can view information about multiple budgets at once by selecting the check
boxes in the Overview table. This opens a split-view panel on the right-hand
side, where you can sort or filter the alerts to customize a budget
report.

## Reading your budgets

You can view detailed information about your budgets in two ways.

- Select your budget in the table to open a split-view panel with budget history
  and alert status on the right-hand side. In the split-view panel, navigation
  buttons allow you to move between budgets without leaving the page. To use the
  navigation buttons, select one budget at a time. When multiple budgets are
  selected, the navigation buttons are
  hidden.
- Choose your budget's name to see the budget details page. This page includes
  the following information:
  - **Current vs. budgeted** – Your current
    incurred costs compared to your budgeted costs.
  - **Forecasted vs. budgeted** – Your forecasted
    costs compared to your budgeted costs.
  - **Alerts** – Any alerts or notifications about
    the state of your budgets.
  - **Details** – The amount, type, time period,
    and any other additional parameters for your budget.
  - **Budget history** tab – A chart and table that
    show the history of your budget. `QUARTERLY` budgets show the
    last four quarters of history, and `MONTHLY` budgets show the
    last 12 months. Budget history isn't available for `ANNUAL`
    budgets.

  If you change the budgeted amount for a budget period, then the
  budgeted amount in the table is the last budgeted amount. For example,
  if you have a monthly budget set for 100 in January and you change the
  budget to 200 in February, then the February line in the table shows
  only the 200 budget.
  - **Alerts** tab – More details for any alerts
    about the state of your budget, including a
    **Definition** that describes the conditions for
    exceeding the alert threshold.

- For budgets using **custom** time periods, you can view the following
  information:
  - **Current vs. budgeted costs** - Compare your current incurred costs
    against your total budget for the time period.
  - **Time remaining** - View the remaining duration in your custom budget
    period.
  - **Historical data** - View historical budget data based on the following
    time frames:
    - For Reserved Instance (RI) and Savings Plans(SP) budgets: Up
      to 14 months of historical data
    - For cost and usage budgets:
      - Multi-year data enabled - up to 38 months of
        historical data
      - Multi-year data disabled - up to 14 months of
        historial data

    - For daily views: Up to 14 months of historical data
    - For monthly views: Up to 12 months of historical data

You can use this information to see how well your budget has matched your costs and
usage in the past. You can also download all of the data that Budgets used to create
the table through the following procedure.

###### To download a budget in a CSV file

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/cost-management/](https://console.aws.amazon.com/cost-management/ "https://console.aws.amazon.com/cost-management/").
2. On the navigation pane, choose **Budgets**.
3. To see the filters and cost variances for your budgets, choose the budget name
   in your list of budgets.
4. On the **Budget history** tab, choose **Download as
   CSV**.
5. Follow the instructions onscreen.
