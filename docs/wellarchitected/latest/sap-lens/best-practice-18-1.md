# Best Practice 18.1 – Understand the

payment and commitment options available for Amazon EC2

Consider the use of Reserved Instances and Savings Plans to provide a significant
discount compared to on-demand pricing. They are available with 1-year and 3-year
commitment terms with three payment options: All Upfront, Partial Upfront, and No
Upfront.

**Suggestion 18.1.1 – Understand the breakeven points between pricing
models**

[Reserved Instances](../../../AWSEC2/latest/UserGuide/reserved-instances-types.md "../../../AWSEC2/latest/UserGuide/reserved-instances-types.md") are categorized into Standard Reserved Instances (up to 72%
discount off on-demand rates) and Convertible Reserved Instances (up to 54% discount off
on-demand rates). [Savings Plans](../../../savingsplans/latest/userguide/what-is-savings-plans.md#plan-types "../../../savingsplans/latest/userguide/what-is-savings-plans.md#plan-types") are categorized into Compute Savings Plans (up to 66% discount
off on-demand rates) and EC2 Instance Savings Plans (up to 72% discount off on-demand
rates).

The discount off the Amazon EC2 on-demand hourly rate you can achieve will depend on
the following factors:

- Commitment term selected
- Payment option selected
- Reserved Instance or Savings Plan type selected
- Instance family
  Memory-optimized instance families, such as `X2`, `X1`, and
  `X1e`, provide higher savings for commitment. Therefore, understanding pricing
  options is important for SAP, particularly for SAP HANA workloads.

Use the advanced option within the AWS Pricing Calculator to determine the
break-even point. You should be aware of the assumptions used by this calculator. To
illustrate this, consider the example where we use the following formula to determine the
point using a Reserved Instance or Savings Plan will provide a lower TCO than using
on-demand for each instance family.

_(Effective Hourly rate of Commitment / Hourly rate of On-Demand) \* 730
hours_

Reference the effective hourly rate for each [RI commitment term
and type](https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/ "https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/") and for each [Savings Plan commitment period and type](https://aws.amazon.com/savingsplans/pricing/ "https://aws.amazon.com/savingsplans/pricing/"). Compare and contrast the following
examples illustrating different break-even points:

_Example 1: In North Virginia (us-east-1), for the M5 family, the breakeven where
a 3 year no upfront Standard Reserved Instance or EC2 Savings Plan would offer a lower
TCO is 315 hours per month (~16 hrs a day, Monday to Friday)._

_Example 2: In North Virginia (us-east-1), for the X1 instance family, the
breakeven where a 3 year no upfront Standard Reserved Instance or EC2 Savings Plan would
offer a lower TCO is 235 hours per month (~12 hrs a day, Monday to Friday)._

Use comprehensive guidance on [cost management](https://aws.amazon.com/aws-cost-management/ "https://aws.amazon.com/aws-cost-management/") and the
Well-Architected Framework [Cost Optimization Pillar](../cost-optimization-pillar/welcome.md "../cost-optimization-pillar/welcome.md"). The following [SAP on
AWS Pricing Guide](../../../sap/latest/general/sap-on-aws-pricing-guide.md "../../../sap/latest/general/sap-on-aws-pricing-guide.md") also provides guidance specific to SAP workloads running on
AWS. When analyzing costs, be aware that all AWS pricing (with the exception of the
AWS China Regions) is in US dollars (USD). However, it is possible to select an
alternative currency for payment: [currencies AWS currently supports](https://aws.amazon.com/premiumsupport/knowledge-center/supported-aws-currencies/ "https://aws.amazon.com/premiumsupport/knowledge-center/supported-aws-currencies/").

- AWS Documentation: [Savings Plans - Compute Savings Plans and Reserved Instances](../../../savingsplans/latest/userguide/what-is-savings-plans.md#sp-ris "../../../savingsplans/latest/userguide/what-is-savings-plans.md#sp-ris")
- AWS Documentation: [Savings Plans - Plan Types](../../../savingsplans/latest/userguide/what-is-savings-plans.md#plan-types "../../../savingsplans/latest/userguide/what-is-savings-plans.md#plan-types")
- AWS Documentation: [Types of Reserved Instances](../../../AWSEC2/latest/UserGuide/reserved-instances-types.md "../../../AWSEC2/latest/UserGuide/reserved-instances-types.md")

**Suggestion 18.1.2 – Understand the considerations of each pricing
model relevant to SAP**

In addition to the hourly rate discount, there are other benefits of Reserved
Instances and Savings Plans you should consider. This AWS Documentation: [Comparing Savings Plans to RIs table](../../../savingsplans/latest/userguide/what-is-savings-plans.md#sp-ris "../../../savingsplans/latest/userguide/what-is-savings-plans.md#sp-ris") provides a comparison of Reserved
Instances and Savings Plans.

[Zonal Reserved Instances](../../../AWSEC2/latest/UserGuide/reserved-instances-scope.md "../../../AWSEC2/latest/UserGuide/reserved-instances-scope.md") can be used to provide capacity reservations within a
specific Availability Zone. Savings Plans do not provide a capacity reservation but you
can combine with [On-demand Capacity Reservations](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md") to provide the same features of a Zonal
Reserved Instance. See [Reliability]: [Best Practice
10.2 - Select an architecture suitable for your availability and capacity
requirements](best-practice-10-2.md "best-practice-10-2.md"), for further information on capacity strategies.

[Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot "https://aws.amazon.com/ec2/spot") let you
take advantage of unused EC2 capacity in the AWS Cloud. Spot Instances are available at
up to a 90% discount compared to On-Demand Instance prices. Spot Instances can be
reclaimed by AWS with two-minutes notice when AWS requires the capacity. Therefore,
Spot Instances are not generally suited for running SAP workloads.

When using [on-demand instances](../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md "../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md"), you should consider the additional operational impact of
stopping and starting the SAP systems and underlying EC2 instances based on the required
operating hours in addition to application performance impact each time the system is
started.

**Suggestion 18.1.3 – Evaluate your enterprise strategy for
consolidated billing and sharing of Reserved Instance and Savings Plans
commitment**

With [Consolidated Billing](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md"), Reserved Instances and Savings Plans are applied to
usage across all accounts within an AWS Organization. The management account of an
organization can turn off the Reserved Instance discount and Savings Plans discount
sharing for any accounts in that organization, including the management account. This
means that Reserved Instances and Savings Plans discounts aren't shared between any
accounts that have sharing turned off. To share a Reserved Instances or Savings Plans
discount with an account, both accounts must have sharing turned on. This preference isn't
permanent, and you can change it at any time.

- AWS Documentation: [Consolidated billing for AWS Organizations](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md")
- AWS Documentation: [Turning off reserved instances and Savings Plans discount sharing](../../../awsaccountbilling/latest/aboutv2/ri-turn-off.md "../../../awsaccountbilling/latest/aboutv2/ri-turn-off.md")
  A key factor that will determine your strategy for sharing of commitment will be the
  overall [AWS account strategy](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md") your organization has adopted. Whether your SAP
  workloads are running in their own dedicated AWS accounts or along with other workloads
  hosted in AWS should also be considered. To understand how discounts for Reserved
  Instances and Savings Plans are applied across your organization’s consolidated bill refer
  to:

- AWS Documentation: [Understanding Consolidated Bills](../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#Instance_Reservations "../../../awsaccountbilling/latest/aboutv2/con-bill-blended-rates.md#Instance_Reservations")
  As detailed in SAP note: [1656250 - SAP on AWS: Support
  prerequisites](https://launchpad.support.sap.com/#/notes/1656250 "https://launchpad.support.sap.com/#/notes/1656250") [Requires SAP Portal Access], SAP on AWS is only supported if a
  fee-based [Support agreement](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")
  (Business support or higher) is in place. Determine the appropriate support plan based on
  cost and requirements.

- AWS Documentation: [Compare Support Plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/")
  Be aware that AWS calculates support fees independently for each member account
  within an organization.
