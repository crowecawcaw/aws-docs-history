# Understanding how Savings Plans apply to your usage

If you have active Savings Plans, they apply automatically to your eligible AWS usage to reduce
your bill.

## Calculating bills with Savings Plans

Savings Plans apply to your usage after the Amazon EC2 Reserved Instances (RI) are applied.

Your current Savings Plans are grouped together and applied to the eligible usage.
**EC2 Instance Savings Plans** are applied before **Compute
Savings Plans** because **Compute Savings Plans** have broader
applicability.

In a _Consolidated Billing Family_, Savings Plans are applied
first to the owner account's usage, and then to other accounts' usage. This occurs only
if you have sharing enabled.

We calculate your potential savings percentages of each combination of eligible usage.
This percentage compares the Savings Plans rates with your current On-Demand rates. Your Savings Plans
are applied to your highest savings percentage first. If there are multiple usages with
equal savings percentages, Savings Plans are applied to the first usage with the lowest Savings Plans
rate. Savings Plans continue to apply until there are no more remaining usages, or your
commitment is exhausted. Any remaining usage is charged at the On-Demand rates.

## Savings Plans example

The rates in these examples are illustrative only. In this example, you have the
following usage in a single hour:

- 4x `r5.4xlarge` Linux, shared tenancy instances in us-east-1,
  running for the duration of a full hour
- 1x `m5.24xlarge` Windows, dedicated tenancy instance in
  us-east-1, running for the duration of a full hour
- 400 vCPU and 1,600 GB of Fargate usage in us-west-1
- 1 million requests for 512 MB (0.5 GB) memory of AWS Lambda usage in us-east-2,
  lasting for 3 seconds each

| Pricing example                   |           | On-Demand rate | Compute Savings Plans rate | Compute Savings Plans savings % | EC2 Instance Savings Plans rate | EC2 Instance Savings Plans savings % |
| --------------------------------- | --------- | -------------- | -------------------------- | ------------------------------- | ------------------------------- | ------------------------------------ |
| r5.4xlarge Linux                  | $1.00     | $0.70          | 30%                        | $0.60                           | 40%                             |
| Fargate vCPU                      | $0.04     | $0.03          | 25%                        | N/A                             | N/A                             |
| Fargate GB                        | $0.004    | $0.003         | 25%                        | N/A                             | N/A                             |
| m5.24xlarge Windows               | $10.00    | $8.20          | 18%                        | $7.80                           | 22%                             |
| Lambda duration (per GB/sec)      | $0.000015 | $0.00001275    | 15%                        | N/A                             | N/A                             |
| Lambda requests (per 1M requests) | $0.20     | $0.20          | 0%                         | N/A                             | N/A                             |

This example assumes one-year duration, partial upfront Savings Plans matching the
configuration of your usage. Rates and discount percentages are hypothetical for
simplification.

###### Example scenarios

- [Scenario 1: Savings Plans apply to all usage](#scenario-1 "#scenario-1")
- [Scenario 2: Savings Plans apply to some usage](#scenario-2 "#scenario-2")
- [Scenario 3: Savings Plans apply to some usage, across
  products](#scenario-3 "#scenario-3")
- [Scenario 4: Savings Plans and EC2 reserved instances apply
  to the usage](#scenario-4 "#scenario-4")
- [Scenario 5: Multiple Savings Plans apply to the
  usage](#scenario-5 "#scenario-5")

### Scenario 1: Savings Plans apply to all usage

You purchase a one-year, partial upfront Compute Savings Plan with a $50.00/hour
commitment.

Your Savings Plan covers all of your usage because multiplying each of your
usages by the equivalent Compute Savings Plans is $47.13. This is still less than the
$50.00/hour commitment.

Without Savings Plans, you would be charged at On-Demand rates in the amount of
$59.10.

###### Note

Each hour's commitment can only be used within that hour and cannot be carried
over.

### Scenario 2: Savings Plans apply to some usage

You purchase a one-year, partial upfront Compute Savings Plan with a
$2.00/hour commitment.

In any hour, your Savings Plans apply to your usage starting with the highest discount
percentage (30 percent).

Your $2.00/hour commitment is used to cover approximately 2.9 units of this
usage. The remaining 1.1 units are charged at On-Demand rates, resulting in
$1.14 of On-Demand charges for `r5`.

The Fargate `m5.24xlarge` and Lambda usage are also charged at
On-Demand rates, resulting in $55.10 of On-Demand charges. The total On-Demand
charges for this usage are $56.24.

### Scenario 3: Savings Plans apply to some usage, across

products

You purchase a one-year, partial upfront Compute Savings Plan with a
$19.60/hour commitment.

Your Savings Plans are first applied to the `r5.4xlarge` because it has the
highest discount percentage (30 percent).

Savings Plans apply to the Fargate usage next because it has the next highest
discount percentage (25 percent). Savings Plans apply to memory (GB) before compute
(vCPU) because it has the lower Savings Plans rate. The hourly commitment of $19.60 is
met, and the remaining usage is charged at On-Demand rates.

The `m5.24xlarge` and Lambda usage on On-Demand charges are
$32.70.

### Scenario 4: Savings Plans and EC2 reserved instances apply

to the usage

You purchase a one-year, partial upfront Compute Savings Plan with an
$18.20/hour commitment. You have two EC2 Reserved Instances (RI) for
`r5.4xlarge` Linux shared tenancy in us-east-1.

First, the RI covers two of the `r5.4xlarge` instances. Then, the
Savings Plans rate is applied to the remaining `r5.4xlarge` and the Fargate
usage, which exhausts the hourly commitment of $18.20.

The `m5.24xlarge` and Lambda usage On-Demand charges are $32.70.

### Scenario 5: Multiple Savings Plans apply to the

usage

You purchase a one-year, partial upfront EC2 Instance Family Savings Plan for
the `r5` family in us-east-1 with a $3.00/hour commitment. You also
have a one-year, partial upfront Compute Savings Plan with a $16.80/hour
commitment.

Your EC2 Instance Family Savings Plan (`r5`, us-east-1) covers all
of the `r5.4xlarge` usage because multiplying the usage by the EC2
Instance Family Savings Plan rate is $2.40. This is less than the $3.00/hour
commitment.

Next, the Compute Savings Plan is applied to the Fargate usage because it
has the highest discount percentage (25 percent) of the remaining usage. Savings Plans
apply to memory (GB) before compute (vCPU) because memory has the lower Savings Plans
rate. The hourly commitment of $16.80 is met, and the remaining usage is charged
at On-Demand rates.

The `m5.24xlarge` and Lambda usage On-Demand charges are $32.70.

For more information, see [Understanding Consolidated Bills](../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#cb_savingsplans "../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#cb_savingsplans") in the _AWS Billing and Cost Management User
Guide_.
