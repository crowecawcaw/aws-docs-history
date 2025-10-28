# Budget filters

Based on your choice of budget type, you can choose one or more of the available
budget filters.

**API operation**

Choose an action, such as `CreateBucket`.

**Availability zone**

Choose the `Availability zone` in which the resource that you want to create a
budget for is running.

**Billing entity**

Helps you identify whether your invoices or transactions are for AWS Marketplace or for purchases
of other AWS services. Possible values include:

- AWS: Identifies a transaction for AWS services other than in
  AWS Marketplace.
- AWS Marketplace: Identifies a purchase in AWS Marketplace.

**Charge type**

Different types of charges or fees.

- **Credit**: Any AWS credits that
  are applied to your account.
- **Other out-of-cycle charges**: Any
  subscription charges that aren't upfront reservation charges or
  support charges.
- **Recurring reservation fee**: Any
  recurring charges to your account. When you purchase a Partial
  Upfront or No Upfront Reserved Instance from AWS, you pay a
  recurring charge in exchange for a lower rate for using the
  instance. The recurring fees can result in spikes on the first day
  of every month, when AWS charges your account.
- **Refund**: Any refunds that you
  received. Refunds are listed as a separate line item in the data
  table. They don't appear as an item in the chart because they
  represent a negative value in the calculation of your costs. The
  chart displays only positive values.
- **Reservation applied usage**: Usage
  that AWS applied reservation discounts to.
- **Savings Plan covered usage**: Any
  on-demand cost that's covered by your Savings Plan. In an Unblended
  costs view, this represents the covered usage at on-demand rates. In
  an Amortized costs view, this represents the covered usage at your
  Savings Plan rates. Savings Plan covered usage line items are offset
  by the corresponding Savings Plan negation items.
- **Savings Plan negation**: Any offset
  cost through your Savings Plan benefit that’s associated with the
  corresponding Savings Plan covered usage item.
- **Savings Plan recurring fee**: Any
  recurring hourly charges that correspond with your No Upfront or
  Partial Upfront Savings Plan. The Savings Plan recurring fee is
  initially added to your bill on the day that you purchase a No
  Upfront or Partial Upfront Savings Plan. After the initial purchase,
  AWS adds the recurring fee hourly. For an All Upfront Savings
  Plan, the line item indicates the portion of the Savings Plan unused
  during the billing period. For example, if a Savings Plan was 100%
  utilized for a billing period, this shows as “0” in your amortized
  costs view. Any number greater than “0” indicates an unused Savings
  Plan.
- **Savings Plan upfront fee**: Any
  one-time upfront fee from your purchase of an All Upfront or Partial
  Upfront Savings Plan.
- **Support fee**: Any charges that
  AWS charges you for a support plan. When you purchase a support
  plan from AWS, you pay a monthly charge in exchange for service
  support. The monthly fees can result in spikes on the first day of
  every month, when AWS charges your account.
- **Tax**: Any taxes that are
  associated with the charges or fees in your cost chart. Cost
  Explorer adds all taxes together as a single component of your
  costs. If you select five or fewer filters, Cost Explorer displays
  your tax expenses as a single bar. If you select six or more
  filters, Cost Explorer displays five bars, stacks, or lines, and
  then aggregates all remaining items, including taxes, into a sixth
  bar, stack slice, or plot line that's labeled **Other**.
- **Upfront reservation fee**: Any
  upfront fees that are charged to your account. When you purchase an
  All Upfront or Partial Upfront Reserved Instance from AWS, you pay
  an upfront fee in exchange for a lower rate for using the instance.
  The upfront fees can result in spikes in the chart for the days or
  months when you make your purchases.
- **Usage**: Usage that AWS didn't
  apply reservation discounts to.

**Cost category**

Choose the cost category group and value to track with this budget. To learn more about
setting up cost categories, see [Organizing costs using AWS Cost
Categories](../../../awsaccountbilling/latest/aboutv2/manage-cost-categories.md "../../../awsaccountbilling/latest/aboutv2/manage-cost-categories.md").

**Instance family**

Choose the family of instances to track using this budget.

**Instance type**

Choose the type of instance that you want to track with this budget.

**Invoicing entity**

The AWS entity that issues the invoice. Possible values include:

- Amazon Web Services, Inc. – The entity that issues invoices to customer globally, where
  applicable.
- Amazon Web Services India Private Limited – The entity that issues invoices to customers
  based in India.
- Amazon Web Services South Africa Proprietary Limited – The entity that issues invoices to
  customers in South Africa.

**Legal entity**

The Seller of Record of a specific product or service. In most cases, the
invoicing entity and legal entity are the same. The values might differ for
third-party AWS Marketplace transactions. Possible values include:

- Amazon Web Services, Inc. – The entity that sells AWS
  services.
- Amazon Web Services India Private Limited – The local Indian
  entity that acts as a reseller for AWS services in India.

###### Note

Amazon Web Services EMEA SARL is the marketplace operator for your purchases if
your account is located in EMEA (excluding Turkey and South Africa), and
the seller is eligible in EMEA. Purchases include subscriptions.
Amazon Web Services, Inc. is the marketplace operator for purchases if the seller
isn’t eligible for EMEA. For more information, see [AWS Europe](https://aws.amazon.com/legal/aws-emea/ "https://aws.amazon.com/legal/aws-emea/").

**Linked account**

Choose an AWS account that is a member of the consolidated billing family that
you're creating the budget for. For more information, see [Consolidated billing for AWS Organizations](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md") in the
_AWS Billing User Guide_.

###### Note

Do not use this filter within a member account. If the current account is a member account,
filtering by `linked account` is not supported.

**Platform**

Choose the operating system that your RI runs on. **Platform** is either **Linux** or **Windows**.

**Purchase option**

Choose `On Demand Instances`, `Standard Reserved Instances`, or `Savings Plans`.

**Region**

Choose the Region in which the resource that you want to create a budget
for is running.

**Savings Plans type**

Choose what you want to budget for, between **Compute Savings Plans** and **EC2 Instance Savings Plans**. The Savings Plans type filter is only available for Savings Plans utilization budgets.

**Scope**

Choose the scope of your RI. The scope is either regional or zonal.

**Service**

Choose an AWS service. Combined with **Billing entity**,
**Invoicing entity**, and **Legal
entity**, you can also use the **Service**
dimension to filter costs by specific AWS Marketplace purchases. This includes your
costs for specific AMIs, web services, and desktop apps. For more
information, see [What Is AWS Marketplace?](../../../marketplace/latest/controlling-access/what-is-marketplace.md "../../../marketplace/latest/controlling-access/what-is-marketplace.md")

###### Note

You can use this filter only for cost, Savings Plans and Reserved Instance (RI) utilization, or Savings Plans and RI
coverage budgets. Cost Explorer doesn't show revenue or usage for
the AWS Marketplace software seller.

The Savings Plans utilization, RI utilization, Savings Plans coverage reports, and RI coverage reports lets you filter by only one service at a time and only for the following services:

- Amazon Elastic Compute Cloud
- Amazon Redshift
- Amazon Relational Database Service
- Amazon ElastiCache
- Amazon OpenSearch Service

**Tag**

If you activated any tags, choose a resource tag. A tag is a label that you can use to
organize your resource costs and track them on a detailed level. There are
AWS generated tags and user-defined tags. User-defined tag keys must use
the `user:` prefix. You must activate tags to use them. For more
information, see [Activating the AWS-Generated Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/activate-built-in-tags.md "../../../awsaccountbilling/latest/aboutv2/activate-built-in-tags.md") and
[Activating
User-Defined Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/activating-tags.md "../../../awsaccountbilling/latest/aboutv2/activating-tags.md").

**Tenancy**

Choose whether you share an RI with another user. **Tenancy** is either
**Dedicated** or **Default**.

**Usage type**

Usage types are the units each service uses to measure the usage for specific types of
resources. If you choose a filter such as `S3` and then choose a
usage type value, such as `DataTransfer-Out-Bytes (GB)`, your
costs are limited to S3 `DataTransfer-Out-Bytes (GB)`. You can
create a usage budget only for a specific unit of measure. If you choose
**Usage type** but not **Usage type
group**, the budget monitors all of the available units of
measure for the usage type.

**Usage type group**

A usage type group is a collection of usage types that have the same unit of measure. If
you choose both the **Usage type group** and the
**Usage type** filters, Cost Explorer shows you usage
types that are automatically constrained to the group unit of measure. For
example, assume you choose the group `EC2: Running Hours (Hrs)`,
and then choose the `EC2-Instances` filter for **Usage
type**. Cost Explorer shows you only the usage types that are
measured in hours.
