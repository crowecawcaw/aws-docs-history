# Understanding your recommendation

calculations

Savings Plans recommendations examine your usage over a selected time period. Based on the
usage, we calculate what your bill could have been if you had purchased an additional
Savings Plans commitment for that time period. We identify and recommend the commitment value
that we estimate will result in the largest savings.

###### Important

- The recommendations don’t forecast your usage. Recommendations are based
  on your historical usage over the selected lookback period. Be sure to
  select a lookback period that reflects your future usage. If you've
  recently switched to CPU-optimized EC2 instances, select a lookback period
  after the change since license costs are no longer eligible for Savings
  Plans coverage. Recommendations don't account for any queued or scheduled
  purchases because recommendations are based on the usage in the lookback
  period. Recommendations are also generated for immediate purchases, and not
  for future purchases.

Recommendations are calculated based on your **Reserved Instances
and Savings Plans discount sharing** preferences. To view or change
your preferences, see [Turning off
reserved instances and Savings Plans discount sharing](../../../awsaccountbilling/latest/aboutv2/ri-turn-off.md "../../../awsaccountbilling/latest/aboutv2/ri-turn-off.md") in the
_AWS Billing User Guide_.

- Recommendations at the management account level are calculated considering
  usage across all of the accounts in your AWS organization that have
  Reserved Instances or Savings Plans discount sharing enabled, to recommend a
  commitment that maximizes savings across accounts. Member account
  recommendations are calculated at the individual account level, to maximize
  savings for each isolated account.
- Recommendations are generated for customers that have an average On-Demand
  spend of $0.10/hour during the lookback period (7, 30, or 60 days). If you
  recently purchased a Savings Plan, returned a Savings Plan, or if your
  Savings Plans recently expired, refresh your Savings Plans recommendations to take your
  current Savings Plans inventory and latest usage data into account.
- Compute and EC2 Instance Savings Plans recommendations are created using the same
  set of usage. You can purchase both Compute Savings Plans and EC2 Instance Savings Plans to
  cover your usage, but the two sets of recommendations are not meant to be
  taken together simultaneously.
- Recommendations are calculated using Savings Plans rates referenced in [Pricing with Savings
  Plans](https://aws.amazon.com/savingsplans/pricing/ "https://aws.amazon.com/savingsplans/pricing/").
