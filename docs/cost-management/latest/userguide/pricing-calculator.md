# Generating estimates with Pricing Calculator

The in-console AWS Pricing Calculator is an AWS Billing and Cost Management feature that enables you to estimate your planned cloud costs using your discounts
and purchase commitments. You can use Pricing Calculator to assess the cost impact and understand
the return on investment for migrating workloads, planning new or growth of existing workloads,
and plan for commitment purchases.

## In-console AWS Pricing Calculator and the public Pricing Calculator

AWS provides two separate Pricing Calculator experiences: the in-console
AWS Pricing Calculator and the public Pricing Calculator website. One of the main differences
between the in-console version and the public version is that the public version doesn't
require you to create an AWS account. The in-console Pricing Calculator is a feature of
the AWS Billing and Cost Management service in the AWS console and has its own
[set of APIs](../../../aws-cost-management/latest/APIReference/Welcome.md "../../../aws-cost-management/latest/APIReference/Welcome.md"),
so it requires you to create an AWS account. For more information on how to create an AWS account,
see [Getting started with AWS Cost Management](billing-getting-started.md "billing-getting-started.md").

Both pricing calculators allow you to generate estimates for your specific workloads or applications.
However, the in-console AWS Pricing Calculator has more advanced features that allow you to do the following:

- Model your future usage changes by importing your existing usage. This eliminates the
  need to manually input historical usage data.
- Model purchase commitment changes such as Savings Plans and Reserved Instances. Analyze the cost
  impact of changes to your existing commitments or adding new commitments.
- You can use both public On-Demand rates and after discount rates. This gives you a realistic
  estimate based on your existing usage tier.
- You can generate cost estimates for specific applications or workloads that you model.
  Alternatively, you can generate cost estimates for your consolidated billing family which
  takes into account your modeled usage and commitments. This automatically layers your existing
  usage and active commitments.

For more information about the public Pricing Calculator, see [What is AWS Pricing Calculator?](../../../pricing-calculator/latest/userguide/what-is-pricing-calculator.md "../../../pricing-calculator/latest/userguide/what-is-pricing-calculator.md")

## Features of the in-console AWS Pricing Calculator

The in-console Pricing Calculator consists of two main estimate types:

### Workload estimate

- Allows you to estimate the cost of specific workloads, applications, resources, and architectural
  changes.
- This type of estimate is available to all account types (standalone, management, and member accounts).
- Management accounts can configure the effective rate type
  that is available for use by their member accounts. The rate types available are Before discounts, After discounts, and After discounts and purchase commitments.
- Workload estimates are available immediately upon running the estimate.

For more information, see [Workload estimates](pc-workload-estimate.md "pc-workload-estimate.md").

### Bill estimate

- Allows you to estimate the cost of applying any modeled usage and commitment changes to your entire
  consolidated bill across your AWS organization.
- This type of estimate is only available to management or standalone account users.
- The bill estimate automatically includes your last month's consolidated billing usage. It also includes
  your existing commitments like Savings Plans and Reserved Instances.
- You can model new usage changes as well as modifications to your existing commitments without affecting your
  current commitments. For example, you can add new usage, make a change to existing usage, and remove an existing
  commitment to see how these configurations affect costs without affecting your bill.

For more information, see [Bill estimates](pc-bill-estimate.md "pc-bill-estimate.md").

## Pricing for AWS Pricing Calculator

AWS Pricing Calculator is available to all AWS customers. Workload estimates are provided free of charge.
For bill estimates, you receive five free estimates per month. After your fifth estimate in a calendar month,
the estimates cost $2 each.

AWS Pricing Calculator provides only an estimate of your AWS fees and doesn't include any taxes that might
apply. Your actual fees depend on a variety of factors, including your actual usage of AWS services.

###### Note

If an estimate fails to generate, this will not count as one of your five free estimates per month. You will also not be
charged for any failed estimates.
