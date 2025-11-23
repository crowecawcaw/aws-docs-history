# Understanding your AWS Billing Conductor dashboard

The AWS Billing Conductor dashboard provides a high-level summary of the key metrics to help you understand
the impact of your custom pricing dimensions.

## Key performance indicators

This section defines the key performance indicators (KPI) that are available on your AWS Billing Conductor
dashboard. KPIs are all month-to-date. As you create or add accounts to your AWS Organizations, the
accounts accrue to this KPI. When you delete a billing group, the accounts in that billing group
also accrue to this KPI.

- **Charged amount** – The combined charges for usage accrued by all billing groups are based on the custom rate defined by the applied pricing plans. The calculation doesn't include commitment-based discounts purchased outside of the billing group (not applicable to billing transfer users), non-public pricing, or credits consumed in the billable domain. Examples of commitment-based discounts include reserved instances and Savings Plans.
- **AWS costs** – The combined month-to-date charge
  for usage that's accrued by all billing groups, according to the estimated charges on your
  AWS bill. The calculations include any commitment-based discounts purchased outside of the
  billing group if those benefits were applied in the billable domain, any non-public pricing,
  volume-tiered discounts, and credits. Examples of commitment-based discounts include reserved
  instances and Savings Plans.

###### Note

When using billing transfer in a two-level transfer configuration and signed in as the bill transfer account (middle tier level), your view of AWS costs reflects the pricing configuration set by the bill transfer (bill receiver) account. This amount represents what you owe to your bill transfer account for your bill source accounts' usage.

When using billing transfer in either one-level or two-level transfer configurations and signed in as the bill source account to use Billing Conductor for your internal chargeback or showback requirements, the AWS cost metrics reflect the pricing data configured by your bill transfer account. This represents the costs you owe your bill transfer account for usage in your AWS Organizations.

- **Margin** – The aggregated month-to-date margin
  that's accrued by all billing groups. The margin is calculated by subtracting the AWS costs
  from the charged amount. Based on the factors such as the pricing plan and the applied custom
  line items, the margin can also be a negative.

###### Note

Post-billing period adjustments impact your historical margins. For more information, see
[Analyzing your margins](analyzing-abc.md "analyzing-abc.md").

- **Billing groups** – The number of mutually exclusive groups of accounts or, for billing transfer users, AWS Organizations, each with a primary account and an associated pricing plan.

### Viewing your top-five billing groups per charged amount

You can understand your top-five billing groups that generate revenue by referencing the
visual and table view. To manage your existing billing groups, choose **Manage billing
groups** on the dashboard page.
