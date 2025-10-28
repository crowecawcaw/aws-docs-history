# Understanding coverage metrics and

calculations

You can find the following high-level metrics in the **Coverage
report** section:

- **On-Demand spend not covered** – The amount of
  eligible savings spend that was not covered by Savings Plans or Reserved Instances
  over the lookback period.
- **Average coverage** – The aggregated Savings Plans
  coverage percentage based on the selected filters and look-back
  period.
- **Potential monthly savings vs On-Demand** – Your
  potential savings amount based on your Savings Plans recommendations. This is shown
  as a monthly amount.
  Coverage is calculated as:

(On-Demand equivalent of usage covered by your Savings Plans)

÷

(On-Demand equivalent usage covered by your Savings Plans + Savings Plans eligible amount that was
billed at On-Demand rates)

For example, if you are running 10 identical instances with an
On-Demand price of $1.00/hour, and 9 of the 10 instances that you're running are
covered by your Savings Plans commitment, your coverage would be 90 percent.

(9 Savings Plans covered instance \* $1.00/hour OD rate)

÷

(9 Savings Plans covered instances \* $1.00/hour OD rate + 1 On-Demand
Instance \* $1.00/hour OD rate)

You can see your usage at an hourly, daily, or monthly granularity. Usage is
calculated using your selected lookback period. You can customize your filters by
member account, AWS Region, instance family, service, and cost category in the
**Filters** section.

If you’re a user in the management account, you can see the aggregated coverage for
the entire Consolidated Billing family.
