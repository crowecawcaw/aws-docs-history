# What is AWS Billing and Cost Management?

Welcome to the AWS Cost Management User Guide.

AWS Billing and Cost Management provides a suite of features to help you set up your billing, retrieve and pay
invoices, and analyze, organize, plan, and optimize your costs.

To get started, set up your billing to match your requirements. For individuals or small
organizations, AWS will automatically charge the credit card provided.

For larger organizations, you can use AWS Organizations to consolidate your charges across multiple
AWS accounts. You can then configure invoicing, tax, purchase order, and payment methods
to match your organization’s procurement processes.

You can allocate your costs to teams, applications, or environments by using cost
categories or cost allocation tags, or using AWS Cost Explorer. You can also export data to your
preferred data warehouse or business intelligence tool.

See the following overview of features to help you manage your cloud finances.

## Features of AWS Billing and Cost Management

###### Topics

- [Billing and payments](#billing-and-payments-features "#billing-and-payments-features")
- [Cost analysis](#cost-analysis-features "#cost-analysis-features")
- [Cost organization](#cost-organization-features "#cost-organization-features")
- [Budgeting and planning](#budgeting-planning-features "#budgeting-planning-features")
- [Savings and commitments](#savings-commitments-features "#savings-commitments-features")

### Billing and payments

Understand your monthly charges, view and pay invoices, and manage preferences
for billing, invoices, tax, and payments.

- **Bills page** – Download invoices and view
  detailed monthly billing data to understand how your charges were
  calculated.
- **Purchase orders** – Create and manage your
  purchase orders to comply with your organization’s unique procurement
  processes.
- **Payments** – Understand your outstanding or
  past-due payment balance and payment history.
- **Payment profiles** – Set up multiple
  payment methods for different AWS service providers or parts of your
  organization.
- **Credits** – Review credit balances and choose
  where credits should be applied.
- **Billing preferences** – Enable invoice delivery
  by email and your preferences for credit sharing, alerts, and discount
  sharing.

### Cost analysis

Analyze your costs, export detailed cost and usage data, and forecast your
spending.

- **AWS Cost Explorer** – Analyze your cost and usage data
  with visuals, filtering, and grouping. You can forecast your costs and create
  custom reports.
- **Data exports** – Create custom data exports from
  Billing and Cost Management datasets.
- **Cost Anomaly Detection** – Set up automated
  alerts when AWS detects a cost anomaly to reduce unexpected costs.
- **AWS Free Tier** – Monitor current and
  forecasted usage of free tier services to avoid unexpected costs.
- **Split cost allocation data** – Enable detailed
  cost and usage data for shared Amazon Elastic Container Service (Amazon ECS) resources.
- **Cost Management preferences** – Manage what data
  that member accounts can view, change account data granularity, and
  configure cost optimization preferences.

### Cost organization

Organize your costs across teams, applications, or end customers.

- **Cost categories** – Map costs to teams,
  applications, or environments, and then view costs along these dimensions in
  Cost Explorer and data exports. Define split charge rules to allocate shared
  costs.
- **Cost allocation tags** – Use resource tags to
  organize, and then view costs by cost allocation tag in Cost Explorer and data
  exports.

### Budgeting and planning

Estimate the cost of a planned workload, and create budgets to track and control
costs.

- **Budgets** – Set custom budgets for cost and usage to
  govern costs across your organization and receive alerts when costs exceed your
  defined thresholds.
- **In-console Pricing calculator** – Use this
  feature to estimate your planned cloud costs using your discount and purchase commitments.
- **Public Pricing calculator website** – Create cost
  estimates for using AWS services with On-Demand rates.

### Savings and commitments

Optimize resource usage and use flexible pricing models to lower your bill.

- **AWS Cost Optimization Hub** – Identify savings opportunities
  with tailored recommendations including deleting unused resources,
  rightsizing, Savings Plans, and reservations.
- **Savings Plans** – Reduce your bill compared to On-Demand
  prices with flexible pricing models. Manage your Savings Plans inventory, review purchase
  recommendations, run purchase analyses, and analyze Savings Plans utilization and coverage.
- **Reservations** – Reserve capacity at discounted
  rates for Amazon Elastic Compute Cloud (Amazon EC2), Amazon Relational Database Service (Amazon RDS), Amazon Redshift, Amazon DynamoDB, and
  more.

## Related services

### AWS Billing Conductor

Billing Conductor is a custom billing service that supports the showback and chargeback
workflows of AWS Solution Providers and AWS Enterprise customers. You can
customize a second, alternative version of your monthly billing data. The service
models the billing relationship between you and your customers or business units.

Billing Conductor doesn't change the way that you're billed by AWS each month. Instead, you
can use the service to configure, generate, and display rates to specific customers
over a given billing period. You can also use it to analyze the difference between
the rates that you apply to your groupings relative to the actual rates for those
same accounts from AWS.

As a result of your Billing Conductor configuration, the payer account (management account) can
also see the custom rate that's applied on the billing details page of the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing/home#/bills "https://console.aws.amazon.com/billing/home#/bills"). The
payer account can also configure AWS Cost and Usage Reports per billing group.

For more information about Billing Conductor, see the [AWS Billing Conductor User Guide](../../../billingconductor/latest/userguide/what-is-billingconductor.md "../../../billingconductor/latest/userguide/what-is-billingconductor.md").

### IAM

You can use AWS Identity and Access Management (IAM) to control who in your account or organization has
access to specific pages on the Billing and Cost Management console. For example, you can control access to
invoices and detailed information about charges and account activity, budgets,
payment methods, and credits. IAM is a feature of your AWS account. You don't
need to do anything else to sign up for IAM and there's no charge to use
it.

When you create an account, you begin with one sign-in identity that has complete
access to all AWS services and resources in the account. This identity is called
the AWS account root user and is accessed by signing in with the email address and password
that you used to create the account. We strongly recommend that you don't use the
root user for your everyday tasks. Safeguard your root user credentials and use them to
perform the tasks that only the root user can perform.

For the complete list of tasks that require you to sign in as the root user, see
[Tasks that require root user credentials](../../../IAM/latest/UserGuide/root-user-tasks.md "../../../IAM/latest/UserGuide/root-user-tasks.md") in the _IAM User Guide_.

By default, IAM users and roles in your account can't access the Billing and Cost Management console.
To grant access, enable the **Activate IAM Access** setting. For
more information, see [About IAM Access](../../../awsaccountbilling/latest/aboutv2/control-access-billing.md#ControllingAccessWebsite-Activate "../../../awsaccountbilling/latest/aboutv2/control-access-billing.md#ControllingAccessWebsite-Activate").

If you have multiple AWS accounts in your organization, you can manage linked
account access to Cost Explorer data by using the **Cost Management
preferences** page. For more information, see [Controlling access to Cost Explorer](ce-access.md "ce-access.md").

For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

### AWS Organizations

You can use the consolidated billing feature in Organizations to consolidate billing and
payment for multiple AWS accounts. Every organization has a
_management account_ that pays the charges of all the
_member accounts_.

Consolidated billing has the following benefits:

- **One bill** – Get one bill for multiple accounts.
- **Easy tracking** – Track charges across multiple
  accounts and download the combined cost and usage data.
- **Combined usage** – Combine the usage across all
  accounts in the organization to share the volume pricing discounts, Reserved
  Instances discounts, and Savings Plans. This can result in a lower charge for your
  project, department, or company than with individual standalone accounts.
  For more information, see [Volume discounts](../../../awsaccountbilling/latest/aboutv2/useconsolidatedbilling-effective.md#useconsolidatedbilling-discounts "../../../awsaccountbilling/latest/aboutv2/useconsolidatedbilling-effective.md#useconsolidatedbilling-discounts").
- **No extra fee** – Consolidated billing is offered
  at no additional cost.

For more information about Organizations, see the [AWS Organizations User
Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md").

### AWS Price List API

AWS Price List API is a centralized catalog that you can programmatically query AWS for services, products, and pricing information. You can use the bulk API to retrieve up-to-date AWS service information in bulk, available in both JSON and CSV formats.

For more information, see [What is AWS Price List API?](../../../awsaccountbilling/latest/aboutv2/price-changes.md "../../../awsaccountbilling/latest/aboutv2/price-changes.md").
