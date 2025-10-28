# What is AWS Billing Conductor?

AWS Billing Conductor is a custom billing service for AWS Marketplace Channel Partners (Partners) and
organizations that have _chargeback_ requirements. For Partners, chargebacks
are a prerequisite to getting paid by their customers and follow an AWS account or an AWS Organizations
billing boundary. For organizations, chargeback activities ensure that organizations allocate the
costs of a specific team (for example, a collection of accounts) to the correct internal budget or
profit and loss (P&L) statement.

To achieve these activities, Billing Conductor enables customers to create a second, pro forma version of
their costs to share with their customers or account owners. Pro forma costs represent the usage
within Billing Conductor managed accounts (those assigned to billing groups) at the pricing rates defined
within Billing Conductor (for example, by using a global pricing rule to apply public pricing to all
usage).

###### Note

Customers will observe minor usage differences between _billable costs_
(matching the AWS invoice) and _pro forma costs_ (matching the Billing Conductor
configuration) throughout the month. However, usage values will match at the end of each month,
once the AWS invoice is issued.

Defining pro forma costs enables customers to model their costs uniformly to match one of the
following use cases:

1. Customer agreements, which can be a Partner use case negotiated outside of AWS
2. Internal accounting practices, often an organization-specific use case
   Billing Conductor configurations don't affect customers’ existing invoices from AWS or billing
   configurations (for example, sharing of credits or commitment-based discounts like Reserved
   Instances or Savings Plans).

Customers can analyze pro forma costs from the management account by doing the following
tasks:

- Analyze margins (the difference between pro forma costs and billable costs for the same set
  of accounts) within Billing Conductor
- View pro forma costs on AWS Cost Explorer
- View monthly pro forma costs on the billing details page
- Create an AWS Cost and Usage Report (CUR) per billing group
- View Reservation and Savings Plans coverage and utilization reports reflecting pro forma costs
  Billing Conductor managed accounts (accounts in billing groups) can analyze pro forma costs in AWS Cost Explorer,
  Cost and Usage Reports, the Billing dashboard, and the billing details page. Managed accounts can also create budgets to monitor their pro forma spend and be alerted when they exceed, or they are forecasted to exceed, their desired pro forma spending limit.

You can configure billing groups, pricing plans, pricing rules, and custom line items in the
[Billing Conductor console](https://console.aws.amazon.com/billingconductor "https://console.aws.amazon.com/billingconductor") or by using the [Billing Conductor
API](../APIReference/Welcome.md "../APIReference/Welcome.md").

For more information about AWS Billing Conductor service quotas, see [Quotas and restrictions](limits.md "limits.md").

## Features in AWS Billing Conductor

You can use the AWS Billing Conductor features to do the following:

**Group accounts**

Organize accounts into billing groups for an aggregated view of pro forma costs. Simulate
individual customer benefits like cross-service discounts and AWS Free Tier for each
group.

**Custom pricing**

Set global or specific markups or discounts, and control Free Tier access.

**Charges and credits**

Add one-time or recurring flat or percentage-based charges or credits to billing
groups.

**Pro forma analysis**

Analyze costs based on pricing configurations in the Billing console. Accounts in your
billing groups can visualize, forecast, and create custom reports of their pro forma costs in AWS Cost Explorer. Accounts in the billing groups can view Reservation and Savings Plans coverage and utilization reports that reflects their pro forma costs. The primary account will have a cross-account view of all costs accrued by accounts
in the billing group, while non-primary accounts will see their own costs.

**Reporting**

Configure Cost and Usage Reports for each billing group.

**Rate analysis**

Compare the applied rates to actual AWS rates with the billing group margin
report.

**Budget**

Accounts in billing groups can create budgets to monitor their pro forma spend and be alerted when they exceed, or they are forecasted to exceed, their desired pro forma spending limit.

## Pricing for AWS Billing Conductor

For more information about pricing, see [AWS Billing Conductor Pricing](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/pricing/ "https://aws.amazon.com/aws-cost-management/aws-billing-conductor/pricing/").

## Related services

\***\*AWS Billing console\*\***

The AWS Billing console is the portal for all AWS customers, from students and
startup companies to large enterprises. You can use the console to see the resources that are
running in your AWS accounts, manage billing preferences, and access billing artifacts that
are needed to make payments to AWS. The AWS Billing console also provides a high-level
explanation of the spending for your account, and serves as the entry point for enrolling in
products in the AWS Cost Management products.

For more information, see the _[AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md")_.

**AWS Cost Explorer**

You can use the Cost Explorer interface to visualize, understand, and manage your AWS costs and
usage over time. Get started quickly by creating custom reports that analyze cost and usage
data. Analyze your data at a high level (for example, total costs and usage across all
accounts), or dive deeper into your cost and usage data to identify trends, pinpoint cost
drivers, and detect anomalies.

For more information, see the following topics:

- [Performing ad hoc analysis on pro forma costs
  in AWS Cost Explorer](ad-hoc-cost-explorer-analysis.md "ad-hoc-cost-explorer-analysis.md")
- [Analyzing your costs with AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md") in the _AWS Cost Management User
  Guide_

\***\*AWS Cost and Usage Reports\*\***

The AWS Cost and Usage Reports (AWS CUR) contain the most comprehensive set of cost and usage data
available. You can use Cost and Usage Reports to publish your AWS billing reports to an Amazon Simple Storage Service (Amazon S3)
bucket that you own. You can receive reports that break down your costs by the hour or day, by
product or product resource, or by tags that you define yourself.

AWS updates the report in your bucket once a day in comma-separated values (CSV) or
Apache Parquet format. You can view the reports using spreadsheet software such as Microsoft
Excel or Apache OpenOffice Calc. You can also access them from an application using the Amazon S3
or Amazon Athena APIs.

AWS Cost and Usage Reports track your AWS usage and provide estimated charges associated with your
account. Each report contains line items for each unique combination of AWS products, usage
type, and operation that you use in your AWS account.

\***\*AWS Identity and Access Management (IAM)\*\***

The AWS Billing Conductor service is integrated with AWS Identity and Access Management (IAM). You can use IAM with AWS Billing Conductor to
ensure that other people who work in your account have only as much access as they need to get
their job done.

You also use IAM to control access to all of your AWS resources. This includes but is
not limited to your billing information. It's important that you familiarize yourself with the
basic concepts and best practices of IAM before you get too far along with setting up the
structure of your AWS account.

For more information about how to work with IAM, see [What Is IAM?](../../../IAM/latest/UserGuide/IAM_Concepts.md "../../../IAM/latest/UserGuide/IAM_Concepts.md") and [Security Best Practices in IAM](../../../IAM/latest/UserGuide/IAMBestPractices.md "../../../IAM/latest/UserGuide/IAMBestPractices.md") in the
_IAM User Guide_.

\***\*AWS Organizations (Consolidated billing)\*\***

AWS products and services can accommodate every size of company, from small startups to
enterprises. If your company is large or likely to grow, you might want to set up multiple
AWS accounts that reflect your company's structure. For example, you can have one account
for the entire company and accounts for each employee, or an account for the entire company
with IAM users for each employee. You can have an account for the entire company, accounts
for each department or team within the company, and accounts for each employee.

If you create multiple accounts, you can use the consolidated billing feature of AWS Organizations
to combine all your member accounts under one management account and receive a single bill.
For more information, see [Consolidated billing for
Organizations](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md") in the _AWS Billing User Guide_.
