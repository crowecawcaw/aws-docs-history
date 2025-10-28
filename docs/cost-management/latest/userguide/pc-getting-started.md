# Getting started with AWS Pricing Calculator

Before you can use AWS Pricing Calculator, you must make sure that you have properly set up your
AWS account and user permissions. For instructions about how to set up your AWS account and permissions,
see [Getting started with AWS Cost Management](billing-getting-started.md "billing-getting-started.md").

## Accounts supported by AWS Pricing Calculator

The following AWS account types are supported by Pricing Calculator:

- Standalone AWS account — A standalone AWS account that doesn't have AWS Organizations enabled.
- Member account of an organization — An AWS account that's a member of an AWS Organization.
- Management account of an organization — An AWS account that administers an AWS Organization.

For more information about AWS Organizations, see [What is AWS Organizations?](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")

## Accessing Pricing Calculator

You can access the Pricing Calculator within the AWS Billing and Cost Management Console and through a set
of [APIs](../../../aws-cost-management/latest/APIReference/Welcome.md "../../../aws-cost-management/latest/APIReference/Welcome.md"). You can
also access the calculator through the AWS SDK and CLI.

AWS Pricing Calculator provides service-specific resources, actions, and condition context keys for use in IAM permission policies.
For more information, see [Actions, resources, and condition keys for AWS Pricing Calculator](../../../service-authorization/latest/reference/list_awsbillingandcostmanagementpricingcalculator.md "../../../service-authorization/latest/reference/list_awsbillingandcostmanagementpricingcalculator.md").

For member accounts to create estimates using discounted rates, the management account of the organization must
enable access to use discounts from the Pricing Calculator console preferences. If the management
account hasn't enabled access, the estimates default to public pricing rates.

###### Important

- You must enable Cost Explorer to allow Pricing Calculator to import your historical AWS workload
  usage. For instructions on how to import your historical workload usage, see [Adding historical usage to my workload estimate](pc-create-workload-historical-usage.md "pc-create-workload-historical-usage.md").
- Pricing Calculator will override any Cost Management preferences you have set, such as Linked account
  discounts. That means that if `After_discount` is selected, you will be able to see
  `netUnblendedRate` based cost, irrespective of your Linked
  account discount preference.
- For access to the Pricing Calculator console, you must migrate your policies from
  under `aws-portal` to fine-grained access controls.
  For information about how to do this, see [Migrating access control for AWS Billing](../../../awsaccountbilling/latest/aboutv2/migrate-granularaccess-whatis.md "../../../awsaccountbilling/latest/aboutv2/migrate-granularaccess-whatis.md").
- Amazon Billing Conductor (ABC) proforma data views aren't available in Pricing Calculator. If your
  member accounts have access to Pricing Calculator, they will be able to view chargeable cost and
  usage depending on their rate type preference setting in Pricing Calculator.
