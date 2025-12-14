# Organizing costs using AWS Cost Categories

Cost allocation helps you identify who is spending what, within your organization.
Cost categories is a cost allocation service to help you map your AWS costs, to your
unique internal business structures.

With cost categories, you create rules to group your costs into meaningful categories.

###### Example scenario 1

Say that your business is organized into several teams,
`Team1`, `Team2`, and so on. Your
teams use 10 AWS accounts in your business. You can define rules to group your AWS
costs, so that it's allocated between these teams.

1. You created a cost category named `Team` for your
   business.
2. For this cost category, you defined a rule so that:
   - All costs for accounts 1-3 are categorized as `Team :
Team1`.
   - All costs for accounts 4-5 are categorized as `Team :
Team2`.
   - For all other accounts, all costs are categorized as `Team
: Team3`.

3. Using this rule, every cost line item from account 6 will be categorized with
   a cost category value `Team3`. These categorizations
   will appear as a column in your AWS Cost and Usage Report (AWS CUR) like in the following example.
   Based on your rule, costs for account 3 are categorized as
   `Team1`. and costs for account 6 is allocated to
   `Team3`.

| Resource Id | AccountID | LineItemType            | UsageType          | Unblended Cost | NetUnblended Cost | ResourceTag/Project | costCategory/Team |
| ----------- | --------- | ----------------------- | ------------------ | -------------- | ----------------- | ------------------- | ----------------- |
| i-11223     | 3         | Usage                   | BoxUsage:c1.xlarge | 3.36           | 3.36              | Beta                | `Team1`           |
| i-12345     | 6         | SavingsPlanCoveredUsage | BoxUsage:m5.xl     | 150            | 140               | Alpha               | `Team3`           |

You can also use these categories across multiple products in the AWS Billing and Cost Management console. This
includes AWS Cost Explorer, AWS Budgets, AWS CUR, and AWS Cost Anomaly Detection. For example, you can filter costs
allocated to `Team1` in Cost Explorer. by applying the filter `value =
 Team 1`, to the cost category named _Team_.

You can also create multilevel hierarchical relationships among your cost categories to
replicate your organizational structure.

###### Example scenario 2

1. You create another cost category named `BusinessUnit`
   that includes groupings of multiple teams.
2. You then define a cost category value that's named
   `BU1`. For this cost category value, you select
   `Team 1` and `Team 2` from
   your `Team` cost category.
3. You then define a cost category value that's named
   `BU2`. For this cost category value, you select
   `Team 3` and `Team 4`
   from the `Team` cost category.
   This example will appear in your cost and usage report, as shown below.

| Resource Id | AccountID | LineItemType            | UsageType          | Unblended Cost | NetUnblended Cost | ResourceTag/Project | costCategory/Team | costCategory/BusinessUnit |
| ----------- | --------- | ----------------------- | ------------------ | -------------- | ----------------- | ------------------- | ----------------- | ------------------------- |
| i-11223     | 3         | Usage                   | BoxUsage:c1.xlarge | 3.36           | 3.36              | Beta                | `Team1`           | `BU1`                     |
| i-12345     | 6         | SavingsPlanCoveredUsage | BoxUsage:m5.xl     | 150            | 140               | Alpha               | `Team3`           | `BU2`                     |

After you create the cost categories, they appear in Cost Explorer,
AWS Budgets, AWS CUR, and Cost Anomaly Detection. In Cost Explorer and AWS Budgets, a
cost category appears as an additional billing dimension. You can use this to filter for
the specific cost category value, or group by the cost category. In AWS CUR, the
cost category appears as a new column with the cost category value in each row. In
Cost Anomaly Detection, you can use cost category as a monitor type to monitor your total
costs across specified cost category values.

###### Notes

- Similar to resource tags, which are key-value pairs applied to AWS
  resources, a cost category is a key-value pair, applied to every cost line item.
  The key is the cost category name. The value is the cost category value. In the
  previous examples, this means that the cost category name
  `Team` is the key.
  `Team1`, `Team2`, and
  `Team3` are the cost category values.
- Cost categories are effective at the start of the current month. If you
  create or update your cost category in the middle of the month, your change is
  automatically applied to cost and usage from the start of the month. For
  example, if you updated your rules for a cost category on Oct 15, any cost and
  usage since Oct 1 will use your updated rules.
- Only the management account in AWS Organizations or individual accounts can create and
  manage cost categories.
- If you use billing transfer and you sign in as a bill source account, you manage the cost categories for your AWS Organizations. You can view your cost categories metadata in your pro forma Cost Explorer and AWS Cost and Usage Report. The bill transfer account can view your cost categories metadata in the AWS Cost and Usage Report reflecting your usage. When you sign in as a bill transfer account, you can configure cost categories only to categorize costs for your own AWS Organizations.

###### Topics

- [Supported dimensions](#cost-categories-dimensions "#cost-categories-dimensions")
- [Supported operations](#cost-categories-ops "#cost-categories-ops")
- [Supported rule types](#cost-categories-rule-types "#cost-categories-rule-types")
- [Default value](#cost-categories-default-value "#cost-categories-default-value")
- [Status](#cost-categories-stat "#cost-categories-stat")
- [Quotas](#cost-categories-limits "#cost-categories-limits")
- [Term comparisons](#cost-categories-terms "#cost-categories-terms")
- [Creating cost categories](create-cost-categories.md "create-cost-categories.md")
- [Tagging cost categories](tag-cost-categories.md "tag-cost-categories.md")
- [Viewing cost categories](view-cost-categories.md "view-cost-categories.md")
- [Downloading your cost category
  values](view-cost-categories-details-csv.md "view-cost-categories-details-csv.md")
- [Editing cost categories](edit-cost-categories.md "edit-cost-categories.md")
- [Deleting cost categories](delete-cost-categories.md "delete-cost-categories.md")
- [Splitting charges within
  cost categories](splitcharge-cost-categories.md "splitcharge-cost-categories.md")
- [Using cost categories with
  other cost management and optimization services](cost-categories-other-cost-management.md "cost-categories-other-cost-management.md")

## Supported dimensions

You can select from a list of billing dimensions to create your cost category
rules. These billing dimensions are used to group your data. For example, assume that
you wanted to group a set of accounts to form a team. You need to choose the account
billing dimension, and then choose the list of accounts that you want to include in the
team.

###### Note

Some dimensions might have limited support if you associate resources with a
cost category. For more information, see [Using cost categories with
other cost management and optimization services](cost-categories-other-cost-management.md "cost-categories-other-cost-management.md").

The following billing dimensions are supported.

**Account**

This can be the AWS account name or the account ID, depending on the
operation. If you're using an exact match operation (`is` or
`is not`), account refers to the account ID. If you're using
an approximate match operation (`starts with`, `ends
 with`, or `contains`), account refers to account
name.

**Charge type**

The type of charges based on line items details. Also referred to as the
`RECORD_TYPE` in the Cost Explorer API. For more
information, see [Term comparisons](#cost-categories-terms "#cost-categories-terms").

**Cost category**

A dimension from another cost category. Using cost categories as a
dimension helps you organize the levels of categories.

**Region**

The geographic areas where AWS hosts your resources.

**Service**

AWS services, such as Amazon EC2, Amazon RDS, and Amazon S3.

**Tag key**

The cost allocation tag keys that are specified on the resource. For more
information, see [Organizing and tracking costs using AWS cost allocation tags](cost-alloc-tags.md "cost-alloc-tags.md").

**Usage Type**

Usage types are the units that each service uses to measure the usage of a
specific type of resource. For example, the
BoxUsage:t2.micro(Hrs) usage type filters by the running
hours of Amazon EC2 t2.micro instances.

**Billing Entity**

Billing entities are the units to identify if your invoices or
transactions are for AWS Marketplace or for purchases of other AWS services. For
example, the AWS Marketplace billing entity filters by the invoices or transactions
for purchases of AWS Marketplace.

## Supported operations

You can use these operations to create the filter expression when you're creating a
cost category rule.

The following operations are supported.

**Is**

The exact match operation that's used to filter for the exact value
specified.

**Is not**

The exact match operation that's used to filter for the exact value that
isn't specified.

**Is absent**

The exact match operation that's used to exclude the tag key that matches
this value.

**Contains**

The approximate match that's used to filter for a text string containing
this value. This value is case sensitive.

**Starts with**

The approximate match that's used to filter for a text string that starts
with this value. This value is case sensitive.

**Ends with**

The approximate match that's used to filter for a text string that ends
with this value. This value is case sensitive.

## Supported rule types

Use rule type to define which cost category values to use to categorize your
costs.

The following rule types are supported.

**Regular Rule**

This rule type adds statically defined cost category values that
categorize costs based on the defined dimension rules.

**Inherited Value**

This rule type adds the flexibility of defining a rule that dynamically
inherits the cost category value from the dimension value defined. For
example, assume that you wanted to dynamically group costs based on the
value of a specific tag key. You need to choose the inherited value rule
type, then choose the `Tag` dimension and specify the tag key to
use. Optionally, you can use a tag key, `teams`, to tag your
resources. They can tag them with values such as `alpha`,
`beta`, and `gamma`. Then, with an inherited value
rule, you can select `Tag` as the dimension and use
`teams` as the tag key. This generates the dynamic cost
category values of `alpha`, `beta`, and
`gamma`.

## Default value

Optionally, if no rules are matched for the cost category, you can define this value
to be used instead.

## Status

You can use the console to confirm the status of whether your cost categories
completed processing the cost and usage information. After you create or edit a
cost category, it can take up to 24 hours before it has categorized your cost and
usage information in the AWS Cost and Usage Report, Cost Explorer, and other cost management
products.

There are two status states.

**Applied**

Cost categories completed processing, and the information in AWS Cost and Usage Report,
Cost Explorer, and other cost management products is up to date with the
new rules.

**Processing**

The cost category updates are still in progress.

## Quotas

For more information about cost categories quotas, see [Quotas and restrictions](billing-limits.md "billing-limits.md").

## Term comparisons

`CHARGE_TYPE` is a dimension supported for cost category expressions.
It's the `RECORD_TYPE` value in the Cost Explorer API. This dimension uses
different terms, depending on whether you're using the console or the API/JSON editor.
The following table compares the terminology used for both scenarios.

| Term comparison         | Value in API or JSON editor | Name used in the console |
| ----------------------- | --------------------------- | ------------------------ |
| Credit                  | Credit                      |
| DiscountedUsage         | Reservation applied usage   |
| Fee                     | Fee                         |
| Refund                  | Refund                      |
| RIFee                   | Recurring reservation fee   |
| SavingsPlanCoveredUsage | Savings Plan Covered Usage  |
| SavingsPlanNegation     | Savings Plan Negation       |
| SavingsPlanRecurringFee | Savings Plan Recurring Fee  |
| SavingsPlanUpfrontFee   | Savings Plan Upfront Fee    |
| Tax                     | Tax                         |
| Usage                   | Usage                       |
