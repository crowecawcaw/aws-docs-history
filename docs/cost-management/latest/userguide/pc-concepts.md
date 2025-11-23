# Understanding AWS Pricing Calculator concepts

To help you get started, this page explains the key concepts of the in-console AWS Pricing Calculator and how they interact.

## Key concepts

The in-console AWS Pricing Calculator enables you to estimate your planned cloud costs using your discount rates and purchase
commitments. Here are the key concepts you'll work within the Pricing Calculator.

**Before discount rates**

The before discount rates refer to the public, On-Demand pricing for AWS services, without any
discounts or commitments applied. These are the standard rates that are available to any AWS customer.
For more information, see [Before discount rates](pc-rates-discounts.md#pc-rates-discounts-before "pc-rates-discounts.md#pc-rates-discounts-before").

**After discount rates**

After discount rates refer to what you pay for AWS services, after applying any pricing discounts you
have with AWS. For more information, see [After discount rates](pc-rates-discounts.md#pc-rates-discounts-after "pc-rates-discounts.md#pc-rates-discounts-after").

**Workload estimate**

A workload estimate represents the incremental AWS usage you want to model. You can add and
modify usage details in a workload estimate. However, workload estimates don’t allow you to
model changes to your AWS commitments. You can refer to a workload estimate resource using an
Amazon Resource Name (ARN). For more information about workload estimates, see [Workload estimates](pc-workload-estimate.md "pc-workload-estimate.md").

**Usage**

This represents your general AWS usage across all services, showing how much of each product is used.

**Commitments**

This represents your AWS commitments like Savings Plans or Reserved Instances, which provide discounted
pricing in exchange for a term-based commitment. For more information, see [Compute and EC2 Instance Savings Plans](https://aws.amazon.com//savingsplans/compute-pricing/ "https://aws.amazon.com//savingsplans/compute-pricing/") and [Amazon EC2 Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/ "https://aws.amazon.com/ec2/pricing/reserved-instances/").

###### Note

You can’t use a workload estimate to model your commitments.

**Bill scenario**

A bill scenario acts as a container that allows you to model anticipated usage and commitments for
future needs. You can refer to a bill scenario resource using an ARN. For more information, see
[Bill estimates](pc-bill-estimate.md "pc-bill-estimate.md").

**Bill estimate**

A bill estimate incorporates all inputs from a bill scenario together with your usage and
commitments from the most recent anniversary bill to calculate estimated costs. The pre-tax
cost of the entire consolidated billing family will be displayed. You can refer to a bill
estimate resource using an ARN. For more information, see
[Bill estimates](pc-bill-estimate.md "pc-bill-estimate.md").

###### Note

Bill estimates are only available to management and standalone accounts.

**Groups**

You can organize your estimates by defining groups. A group can reflect how your company is organized.
A group can also reflect other organization methods, such as by product stack or product architecture.
For example, if you want to price out different ways to build your AWS setup, you can use different
groups for each variation of your setup and compare the estimates.

**Anniversary bill**

This is the line items for services that you used during the month. For more information about
billing term definitions, see [Billing details](../../../cur/latest/userguide/billing-columns.md "../../../cur/latest/userguide/billing-columns.md")
in the _AWS Data Exports User Guide_.
