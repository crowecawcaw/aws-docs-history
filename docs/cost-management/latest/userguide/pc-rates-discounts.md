# Understanding rates, discounts, and purchase commitments

This section outlines AWS rates, discounts, and commitments supported by Pricing Calculator and how they apply to
both workload and bill estimate types. Before discount and after discount rates only apply to workload estimates. Bill estimate considers
your own rates based on your existing usage and commitments, other discounts, and credits. Your choice
of a rate type does not impact the bill estimate calculation.

###### Topics

- [Before discount rates](#pc-rates-discounts-before "#pc-rates-discounts-before")
- [After discount rates](#pc-rates-discounts-after "#pc-rates-discounts-after")
- [Purchase commitments](#pc-rates-discounts-commitments "#pc-rates-discounts-commitments")
- [Setting your rates for member accounts](pc-setting-rates.md "pc-setting-rates.md")

## Before discount rates

The before discount rates refer to the public, On-Demand pricing for AWS services, without any
discounts or commitments applied. These are the standard rates that are available to any AWS customer.

The before discount rates can be helpful in the following use cases:

- If you're a new AWS customer without any discounts or commitments, the before discount rates
  accurately represent the pricing you would pay for On-Demand usage.
- When estimating the cost of using a new AWS service or feature that you don't currently have
  discounts for, the before discount rates provide a baseline cost comparison.

###### Note

- Before discount rates don’t take into account any discounts or commitments that you may be
  eligible for as an existing AWS customer.
- If you are using before discount rates, tiered pricing is only accounted for if the modeled
  usage crosses a tier of usage. For example, if you want to model 100TB/month of S3 standard
  storage use, Pricing Calculator uses tiered S3 standard rates for the first 50 TB/Month and
  the next tiered rate for the remaining 50 TB/Month.

## After discount rates

AWS Pricing Calculator offers two ways to estimate costs that account for your organization's discounts:

- [After discounts](pc-rates-discounts.md#pc-rates-after "pc-rates-discounts.md#pc-rates-after")
- [After discounts and purchase commitments](pc-rates-discounts.md#pc-rates-discounts-after-commitments "pc-rates-discounts.md#pc-rates-discounts-after-commitments")

These options help you understand how different
types of discounts impact your estimated costs, whether from usage-based discounts alone or combined with
commitment-based savings.

### After discounts

After discount rates refer to what you pay for AWS services, after applying any usage-based discounts you
have with AWS. These rates can help you estimate your actual AWS costs, taking the
following into account:

- Your organization's volume or pricing discounts.
- Tiered pricing based on your usage volumes. Tiered pricing is only accounted for if the modeled
  usage crosses a tier of usage. For example, if you want to model 100TB/month of S3 standard
  storage use, Pricing Calculator uses tiered S3 standard rates for the first 50 TB/Month and
  the next tiered rate for the remaining 50 TB/Month.

###### Note

If you are using after discount rates, then a single rate is used based on your highest
usage tier for that product SKU as of the last completed anniversary bill.

After discount rates are the increase in cost for using one additional unit of a
SKU, considering all usage-based discounts at the consolidated billing family level.
For SKUs that you used last month, the effective rate is the net unblended rate of the
SKUs in the Cost and Usage Report. For SKUs that you have not yet used, we will construct
mock workloads by adding one unit of usage for each of the SKUs on top of prior month's
usage, and get the net unblended rate from the resulting anniversary bill output.

If you have any purchase commitments (Savings Plans or Reservations), the calculated
after discount rate will not be affected by the commitment discount. This means that
the after discount rate we use is based solely on your actual usage based on On-Demand
usage rates and applicable discounts, such as tiering discounts, volume discounts, but
not commitment discounts.

###### Note

AWS Pricing Calculator doesn’t take AWS Free Tier into account when calculating after discount rates. The calculator sets a minimum
usage threshold that excludes Free Tier levels. For example, if the Free Tier covers up to 100 units, the calculator
sets the usage to 101 units when calculating rates. This means that if you input usage amounts that would normally
fall within the Free Tier, the calculator applies standard pricing rates to provide a cost estimate.

When you use After discount rates to generate a cost estimate, the estimate is tailored to your
specific AWS usage-based pricing terms. This can help you to make informed decisions about how changes to your usage would
impact your actual AWS spend.

###### Note

- After discount rates don't include the impact of active commitments, such as Savings Plans and
  Reserved Instances. The calculator assumes you don't have any unused commitments that may be applied
  to the estimate. The estimated cost might be larger than your actual spend if you have unused commitments
  that can be applied to your usage.
- For accounts opting in to Cost Explorer, after discount rates will become available
  for use within 72-90 hours of enabling Cost Explorer.
- Your most recent after discount rates are calculated based on the last completed anniversary bill
  month and are available by the 15th of the current month.
- After discounts aren't available to any product launched after the 15th of
  the current month. In this case, the after discount rates will become available on
  15th of the following month.

### After discounts and purchase commitments

The After discounts and purchase commitments rate calculates the effective pricing based on your usage patterns.
For a specific AWS resource (SKU), the total cost combines various pricing models and commitment terms, including
1-year and 3-year Compute Savings Plans, Instance Savings Plans, Convertible RIs, and Standard RIs with no upfront
payment options. For each commitment type, the calculation multiplies the coverage percentage by the corresponding
commitment rate for that SKU. Any remaining On-Demand usage is calculated by multiplying the On-Demand coverage
percentage by the SKU's After discount rate. For an example of how a purchase commitment applies to your usage, see
[Understanding how Savings Plans apply to your usage](../../../savingsplans/latest/userguide/sp-applying.md "../../../savingsplans/latest/userguide/sp-applying.md").

For EC2 instances, the calculation considers your previous month's usage patterns and determines coverage percentages
based on whether the instance family was used in the same AWS Region, in different Regions, or not used at all. For example,
if you used m5.2xlarge instances in a specific Region last month, the formula will calculate coverage based on that Region's
specific usage patterns. If there was no usage of a particular instance family, the formula defaults to using the overall
EC2 usage patterns across all Regions to determine coverage percentages. All these coverage percentages (including On-Demand usage)
must add up to 100%.

Similar approaches apply to other commitment-eligible services like Lambda, Fargate, SageMaker, and Amazon RDS, where
we calculate service-specific coverage percentages based on your usage patterns.

###### Note

- For accounts opting in to Cost Explorer, After discount and purchase commitments rates will become available
  for use within 72-90 hours of enabling Cost Explorer.
- Your most recent After discount and purchase commitments rates are calculated based on the last completed anniversary bill
  month and are available by the 15th of the current month.
- After discount and purchase commitments aren't available to any product launched after the 15th of
  the current month. In this case, the rates will become available on
  15th of the following month.

## Purchase commitments

The purchase commitments supported by AWS Pricing Calculator
are Amazon EC2 Reserved Instances (RIs) and Compute and EC2 Instance Savings Plans. For more information, see [Compute and EC2 Instance Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/ "https://aws.amazon.com/savingsplans/compute-pricing/") and [Amazon EC2 Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/ "https://aws.amazon.com/ec2/pricing/reserved-instances/").

You can use Pricing Calculator to model the impact of adding new Savings Plans or Reserved Instances, or removing
existing commitments as part of a bill scenario. This allows you to see how these commitments would
affect your overall estimated AWS costs.

###### Note

Any Savings Plans or Reserved Instances you have modeled in your public Pricing Calculator estimates won't be included
when you're adding these estimates from the public Pricing Calculator to a workload estimate or bill scenario.
