# Understanding your AWS Billing Conductor dashboard

The AWS Billing Conductor dashboard provides a high-level summary of the key metrics to help you understand
the impact of your custom pricing dimensions.

## Key performance indicators

This section defines the key performance indicators (KPI) that are available on your AWS Billing Conductor
dashboard. KPIs are all month-to-date. As you create or add accounts to your AWS Organizations, the
accounts accrue to this KPI. When you delete a billing group, the accounts in that billing group
also accrue to this KPI.

- **Charged amount** – The combined charges for usage
  that's accrued by all billing groups, based on the custom rate that's defined by the applied
  pricing plans. The calculation doesn't account for any commitment-based discounts that were
  purchased outside of the billing group, any non-public pricing, or any credit consumed in the
  billable domain. Examples of commitment-based discounts include reserved instances and
  Savings Plans.
- **AWS costs** – The combined month-to-date charge
  for usage that's accrued by all billing groups, according to the estimated charges on your
  AWS bill. The calculations include any commitment-based discounts purchased outside of the
  billing group if those benefits were applied in the billable domain, any non-public pricing,
  volume-tiered discounts, and credits. Examples of commitment-based discounts include reserved
  instances and Savings Plans.
- **Margin** – The aggregated month-to-date margin
  that's accrued by all billing groups. The margin is calculated by subtracting the AWS costs
  from the charged amount. Based on the factors such as the pricing plan and the applied custom
  line items, the margin can also be a negative.

###### Note

Post-billing period adjustments impact your historical margins. For more information, see
[Analyzing your margins](analyzing-abc.md "analyzing-abc.md").

- **Billing groups** – The number of mutually exclusive
  groups of accounts, with a primary account and an associated pricing plan.
- **Monitored accounts** – The number of accounts within
  a consolidated billing family that are currently assigned to a billing group.
- **Unmonitored accounts** – The number of accounts
  within a consolidated billing family that haven't been assigned to a billing group.

### Viewing your top-five billing groups per charged amount

You can understand your top-five billing groups that generate revenue by referencing the
visual and table view. To manage your existing billing groups, choose **Manage billing
groups** on the dashboard page.
