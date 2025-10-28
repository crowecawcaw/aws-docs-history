# Budget methods

You can set the budgeted amount of your cost or usage budget in one of the following
ways. You can set one of these budgets no matter whether you're budgeting in a
traditional sense—tracking to plan, for example—or if you want to monitor spend and
receive alerts when costs increase beyond your threshold.

**Fixed**

With a fixed budget, you can monitor the same amount every budget period.
For example, you can use a cost budget with the fixed method to monitor your
costs against $100 every budget period.

**Planned**

The planned budgeting method is available for only monthly or quarterly
budgets. With a planned budget, you can set a different amount to monitor
each budget period. For example, you can use a monthly cost budget with the
planned method to monitor your costs against $100 in the first month, $110
in the second month, and other amounts in the remaining months.

With a planned budget, you can set the budget amount for up to 12 months
or 4 quarters. After 12 months or 4 quarters, your budget amount is fixed at
the last budget amount.

**Auto-adjusting**

An auto-adjusting budget dynamically sets your budget amount based on your
spending or usage over a time range that you specify. The historical or
forecast time range that you select is the auto-adjustment baseline for your
budget.

At the beginning of each new period, AWS Budgets calculates your budget
amount from your cost or usage data within the baseline time range. Make
sure to select a time range that best matches your expectations for your
account’s AWS costs or usage. If you select a time range with lower usage
than you typically expect, then you might get more budget alerts than you
need. If you select a time range with higher usage than you typically
expect, then you might not get as many budget alerts as you need.

For example, you can create an auto-adjusting cost budget with a baseline
time range of the last six months. In this scenario, if your average
spending each budget period in the last six months was $100, your
auto-adjusted budget amount in the new period is $100.

If AWS Budgets updates your budget amount based on changes in your
spending or usage, all budget alert notification subscribers get a
notification that the budget amount changed.

###### Note

- When calculating your auto-adjusted budget amount,
  AWS Budgets doesn't include periods at the beginning of your
  baseline time range that don't have cost or usage data. For
  example, assume that you set your baseline time range as the
  last four quarters. However, your account had no cost data in
  the first quarter. Then, in this case, AWS Budgets calculates
  your auto-adjusted budget amount from only the last three
  quarters.
- You see a temporary forecast while you're creating or editing
  a budget. After you save your budget, your auto-adjusted budget
  is set for the first time.
