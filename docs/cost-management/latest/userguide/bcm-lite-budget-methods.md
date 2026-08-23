# Budget methods in the AWS Billing and Cost Management console

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

The following information is about budget methods in the AWS Billing and Cost Management console for
our new AWS experience. A budget method is how you set your budget. Your budget doesn't need
to be USD 30 per month but can reflect the flexibility in your growth and
development.

## Fixed

A fixed budget lets you monitor the same amount every budget period.

## Planned

A planned budget lets you set a different amount to monitor each month or
quarter.

With a planned budget, you can set the budget amount for up to 12 months or 4
quarters. After 12 months or 4 quarters, your budget amount is fixed at the last budget
amount.

## Auto-adjusting

An auto-adjusting budget dynamically sets your budget amount based on your spending
or usage over a time range that you specify.

The historical or forecast time range that you select is the auto-adjustment baseline
for your budget.

At the beginning of each new period, AWS Budgets calculates your budget amount from
your cost or usage data within the baseline time range. If AWS Budgets updates your
budget, all budget alert notification subscribers get a notification that the budget
amount changed.

When using auto-adjusting budgets, consider the following:

- AWS Budgets doesn't include periods at the beginning of your baseline
  time range that don't have cost or usage data. This might impact your budget
  amount.
- You see a temporary forecast while you're creating or editing a budget.
  After you save your budget, your auto-adjusted budget is set for the first
  time.
